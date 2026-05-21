# Workshop — Extended Section Notes
## ConnectED: An AI-Native Platform for Vietnamese Education

> These notes extend each section of the presentation with additional depth, design rationale, and practical context for instructors, advanced learners, or post-workshop reference.

---

### Section 1.1: Overview — What is ConnectED?

ConnectED is an AI-native lesson planning platform built specifically for the Vietnamese K-12 education system. Its design philosophy departs significantly from typical AI-content tools, which treat content generation as a single inference step.

**Core distinction:** ConnectED treats lesson creation as an instructional design process — not a content retrieval task. This distinction drives all architectural decisions downstream.

**Three primary outputs:**
1. Curriculum-aligned lesson plans (structured, objective-driven)
2. Teaching animations and narrated visual materials
3. Virtual laboratory experiences for STEM subjects

**Why Vietnam specifically?**
Vietnam operates a unified national curriculum managed by the Ministry of Education and Training (MOET). This creates both a constraint (strict alignment requirements) and an opportunity (a well-defined knowledge graph to ground the system). The team leveraged MOET standards directly as structured inputs to the pipeline.

**Broader significance:**
ConnectED is not just an edtech product — it is a replicable pattern for deploying domain-specialized AI systems in any regulated or culturally-specific environment. The architectural lessons apply equally to healthcare, legal practice, financial advisory, and government services.

---

### Section 1.2: Problem Context — The Hidden Workload

**Time cost breakdown:**
The 3-4 hour estimate for lesson preparation is derived from structured interviews with practicing Vietnamese teachers. The distribution of time across subtasks reveals important design implications:

- Concept extraction from textbooks is cognitively demanding — requires deep domain knowledge
- Activity design requires understanding of classroom dynamics, available materials, and student profiles
- Assessment design requires familiarity with both national exam formats and formative evaluation techniques

Each of these is a distinct cognitive skill. Asking a teacher to perform all of them serially in a single session is cognitively exhausting — and explains why lesson quality often degrades near the end of a preparation session.

**The LLM failure mode:**
When the ConnectED team ran controlled experiments using off-the-shelf LLMs (GPT-4, Claude 2) with generic prompts, they consistently observed:
- Learning objectives written to US Common Core standards instead of MOET standards
- Activity suggestions referencing lab equipment unavailable in typical Vietnamese schools
- Assessment formats incompatible with Vietnamese national testing conventions
- Culturally inappropriate examples (e.g., references to seasons or foods uncommon in Vietnam)

The root cause: large language models are trained predominantly on English-language, Western-education-centric data. Without deliberate grounding, they reproduce the biases of their training distribution.

**Design implication (updated):**  
While the hierarchical agent pipeline primarily relies on prompt engineering, structured templates, and curriculum‑grounding (which remain the most maintainable and updatable approach as curriculum standards evolve), the team also recognized that certain core reasoning tasks — such as concept extraction and multi‑step pedagogical reasoning — benefit from a dedicated, fine‑tuned model. Rather than training from scratch, the team developed a **custom Vietnamese educational LLM** using reinforcement learning (RL) for behavior adjustment and Direct Preference Optimization (DPO) on grounded datasets. This model achieves state‑of‑the‑art performance on Vietnamese educational reasoning tasks (see Section 1.8).

---

### Section 1.3: ADDIE — Instructional Design Foundation

ADDIE is a widely-used instructional design framework originating in US military training in the 1970s, later adopted broadly in corporate learning and higher education. Its five phases create a systematic, iterative approach to curriculum development.

**Why ADDIE for an AI system?**
The genius of the ConnectED architecture is recognizing that ADDIE's phases map naturally to distinct computational subtasks. Each phase has:
- A well-defined input format
- A constrained output format
- Verifiable quality criteria

This makes each phase suitable for a dedicated AI stage with its own prompt, validation logic, and error handling.

**Phase-by-phase technical depth:**

**Analyze:**
- Input: raw textbook pages, curriculum documents, grade-level standards
- Techniques: information extraction, entity recognition, prerequisite graph construction
- Output: structured JSON or schema with concepts, outcomes, constraints
- Challenge: textbook language is often dense and ambiguous; requires careful chunking and extraction

**Design:**
- Input: analysis output (concepts + objectives)
- Techniques: template-driven generation, activity taxonomy mapping (Bloom's Taxonomy alignment)
- Output: lesson blueprint with timing, activity types, assessment strategy
- Key constraint: outputs must fit within realistic classroom time (typically 45 minutes in Vietnam)

**Develop:**
- Input: lesson blueprint
- Key innovation: Script-First approach
  - The system generates a full instructional narrative (what the teacher says/does at each moment) before generating any visual asset
  - This ensures visual materials are anchored to the instructional intent, not generated independently
  - Result: slides, animations, and lab instructions that are narratively coherent
- Output: complete asset package (slides, animation scripts, lab guides, quiz questions)

**Implement:**
- Human-in-the-loop stage: teachers receive outputs and refine before classroom use
- System provides structured review interface for targeted editing
- Teachers can regenerate individual components without rerunning the full pipeline

**Evaluate:**
- Feedback captured: teacher ratings, student performance data (where available), time savings
- Feeds back into prompt improvements and template refinements
- Creates a continuous improvement loop

---

### Section 1.4: Hierarchical Agent Pipeline

**Why hierarchical decomposition matters:**

A monolithic prompt attempting to handle all six stages simultaneously faces several fundamental problems:

1. **Context saturation:** Including all instructions, templates, and examples for every stage simultaneously inflates context size, dilutes attention, and degrades output quality
2. **Verification impossibility:** If a single prompt produces a complete lesson, there is no natural point to check intermediate work — errors in concept extraction silently propagate into assessment design
3. **Debugging opacity:** When a monolithic prompt produces a poor lesson, it is nearly impossible to identify which reasoning step failed
4. **Hallucination amplification:** Without intermediate checkpoints, the model can commit to an incorrect assumption early and build an increasingly coherent but incorrect lesson structure on top of it

**The hierarchical solution:**
Each stage is a focused AI call with:
- A small, targeted prompt
- Structured input from the previous stage
- Structured output validated before passing to the next stage
- Independent retry and error handling

**The pipeline in full:**

| Stage | Input | Output | Key Validation |
|-------|-------|--------|----------------|
| 1. Concept Extraction | Textbook pages, curriculum doc | Concept graph, prerequisite map | Concept coverage check vs. curriculum standards |
| 2. Objective Generation | Concept graph | Learning objectives (Bloom-tagged) | Objective measurability check |
| 3. Activity Design | Objectives, time budget | Activity sequence with timing | Total time within 45-minute limit |
| 4. Content Development | Activity design | Slide content, script, discussion prompts | Curriculum terminology consistency |
| 5. Visual Material Generation | Script, slide content | Animation scripts, diagrams, lab guides | Asset-to-narrative alignment check |
| 6. Evaluation Review | Full lesson package | Teacher-facing review interface | Human checkpoint |

---

### Section 1.5: Mapping to the Modern Agentic Stack

ConnectED is an end-to-end production implementation of the **Modern Agentic Stack** detailed in Part II. Here is the architectural mapping:

* **Layer 1: Orchestration:** Managed by a custom, state-machine-based execution harness. This deterministic routing is preferred over generic multi-agent frameworks (e.g. LangChain/CrewAI) to guarantee that the educational pipeline follows a strict, sequential ADDIE progression with zero state leakage.
* **Layer 2: Reasoning Core:** Utilizes hybrid model routing with dynamic semantic routing. Concept extraction and pedagogical activity design are dynamically routed to Claude 4.6 Sonnet / DeepSeek-R1 (frontier/reasoning models), while low-level formatting, translation, and metadata tagging are handled by Llama 3.3 70B / Gemini 2.5 Flash (utility models) to reduce operational costs by 70%. For core Vietnamese educational reasoning, the system can also switch to the custom-trained **Qwen 3 8B** model described in Section 1.8.
* **Layer 3: Skills:** Each step of the lesson plan pipeline is implemented as an isolated, version-controlled skill. System prompts, standard templates, and Bloom's taxonomy definitions are bundled into modular packages.
* **Layer 4: Tools & Protocols:** Uses **Model Context Protocol (MCP)** to securely expose regional school schedules and textbook databases as structured tools. For visual asset procurement, the agent uses **Agent Payments Protocol (AP2)** to securely process micro-transactions for premium STEM graphics based on cryptographically-signed Intent Mandates.
* **Layer 5: Memory Systems:** Employs long-term semantic memory (vector database of teacher teaching preferences and feedback) and short-term episodic memory (retains the active state of the current lesson draft session).

---

### Section 1.6: Mapping to the Core Agentic Loop

During execution, each stage of ConnectED's hierarchical pipeline undergoes its own internal cognitive loop:

1. **PLAN:** The agent plans the specific lesson section structure (e.g., "Designing a 15-minute concept introduction").
2. **ACT:** The agent calls the designated reasoning model with the structured schema instructions and textbook context.
3. **OBSERVE:** The output is passed to the validation gate (e.g., verifying that the total activity time is $\le 45$ minutes).
4. **REFLECT & ITERATE:** If the time budget is exceeded, the agent reflects on which activity can be shortened, rewrites the step, and re-validates. If validation fails three times, it triggers an escalation (escalates to human teacher or rolls back the state).

---

### Section 1.7: Mitigation of Persistent Challenges

ConnectED serves as a reference case for overcoming the core production hurdles of agentic systems:

* **Reliability:** By enforcing schema gates on each stage boundary, malformed JSON inputs are caught before they propagate. This limits cascade failures.
* **Evaluation:** An offline evaluation framework runs trajectories against an "LLM-as-judge" to verify MOET alignment prior to production deployment.
* **Cost & Latency:** Massive curriculum prompts are structured at the front of the context window to maximize prompt caching, yielding an 80% reduction in input token costs.
* **Observability:** Complete execution trees are exported to AgentOps tools, showing the timing, cost, and exact prompt/response pairs for each stage in the hierarchical pipeline.

---

### Section 1.8: Custom-Trained Vietnamese Educational LLM — Qwen 3 8B

While the hierarchical agent pipeline with frontier models and prompt engineering is effective, the ConnectED team went further by developing a **dedicated LLM specifically for Vietnamese K‑12 education**. This model is not a general‑purpose chat engine; it is optimized for reasoning tasks such as concept extraction, prerequisite mapping, and multi‑step pedagogical inference.

#### 1.8.1 Base Model and Training Strategy: RL for Behavior Adjustment

The team selected **Qwen 3 8B** as the base model — a compact, efficient architecture that balances performance and inference cost. Instead of training a 100‑billion‑parameter model from scratch (prohibitively expensive and data‑intensive), they applied **Reinforcement Learning (RL) for behavior adjustment**. RL fine‑tunes the model’s *decision‑making* and *chain‑of‑thought* patterns on educational tasks, teaching it to follow the ADDIE‑style pipeline more reliably than supervised fine‑tuning alone.

#### 1.8.2 Grounded Datasets: Vietnamese Wiki, Viet Math, and More

To overcome the lack of high‑quality Vietnamese educational data in generic LLMs, the team constructed a **golden dataset** comprising:
- **Vietnamese Wikipedia** (curated and cleaned for educational topics)
- **Viet Math** (a collection of Vietnamese math problems, solutions, and step‑by‑step reasoning)
- MOET‑aligned textbook excerpts and national exam questions

These datasets serve two purposes:
1. **Knowledge grounding** – The model learns correct Vietnamese terminology, cultural references, and curriculum‑specific facts.
2. **Hallucination reduction** – Using **Direct Preference Optimization (DPO)**, the team trained the model to prefer responses that stay faithful to the golden dataset and reject plausible‑sounding but incorrect outputs. DPO is a preference‑based alignment method that directly optimises the model’s policy without requiring a separate reward model, making it more stable and efficient than traditional RLHF.

#### 1.8.3 Results: State‑of‑the‑Art on AIThucchien Competition

The custom Qwen 3 8B model was evaluated on the **AIThucchien competition**, Vietnam’s premier benchmark for educational AI reasoning. On the **private test set** — which includes unseen curriculum‑aligned questions and multi‑step reasoning tasks — ConnectED’s model achieved the **highest scores** among all submitted systems.

Key achievements:
- **Most accurate LLM for reasoning tasks** when the “thinking mode” (explicit chain‑of‑thought) is enabled.
- Superior performance on concept prerequisite inference, multi‑hop science reasoning, and MOET objective mapping.
- Near‑elimination of hallucinated facts in generated lesson plans compared to off‑the‑shelf models.

#### 1.8.4 Integration into the ConnectED Pipeline

The custom Qwen 3 8B model is not used for every stage; rather, it acts as a **specialised reasoning engine** for the most cognitively demanding steps (e.g., concept extraction and objective generation). The orchestrator dynamically routes these stages to the custom model when high precision is required, falling back to frontier models (Claude, DeepSeek) for broader knowledge or creative tasks. This hybrid approach balances accuracy, cost, and latency.

**Takeaway:** Training a domain‑specific LLM using RL + DPO on grounded datasets — starting from a compact base like Qwen 3 8B — is a cost‑effective alternative to training from scratch. It delivers state‑of‑the‑art results on local benchmarks while remaining maintainable and scalable as curriculum standards evolve.