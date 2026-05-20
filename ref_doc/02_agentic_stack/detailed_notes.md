# Workshop — Extended Section Notes
## The Emerging Agentic AI Stack

> These notes extend each section of the presentation with additional depth, design rationale, and practical context for instructors, advanced learners, or post-workshop reference.

---

### Section 2.1: From Generative AI to Agentic AI

**The fundamental architectural shift:**
Generative AI operates on a request-response model. The user provides a prompt; the model produces a completion. This is powerful but fundamentally limited:
- No memory across interactions
- No ability to take actions
- No ability to verify or revise its own outputs
- No ability to coordinate with other systems

Agentic AI introduces a cognitive loop — a repeating cycle of planning, action, observation, and reflection — that allows a system to pursue goals across multiple steps, adapting its behavior based on intermediate results.

**Key conceptual additions:**
* **Agency:** Taking actions with real-world effects (e.g. database querying, payment execution).
* **Planning:** Decomposing goals into subgoals.
* **Observation:** Reading and interpreting outputs.
* **Reflection & Iteration:** Self-correcting and executing refined steps.

**Real-World Production Pattern:**
Instead of a single-turn query, a production agentic system takes a high-level goal (e.g., "Conduct a financial compliance audit on a Q3 report") and executes a multi-stage cognitive pipeline. Each phase (e.g., document parsing, standard validation, report drafting) is executed, verified against compliance policies, and refined iteratively before proceeding to the next stage.

---

### Section 2.2: Layer 1 — Orchestration

**What orchestration actually does:**
The orchestration layer is the "executive function" of an agent system. It holds the plan, tracks progress, routes work to the right components, handles failures, and decides when the task is complete.

**Core orchestration responsibilities:**

| Responsibility | Description |
|---|---|
| Task decomposition | Break a high-level goal into ordered subtasks |
| Tool routing | Select the appropriate tool or model for each subtask |
| State management | Track what has been done and what remains |
| Error handling | Detect failures and execute retry or fallback strategies |
| Memory management | Decide what to keep in context vs. retrieve from memory |
| Policy enforcement | Apply constraints (budget limits, forbidden actions, scope restrictions) |
| Multi-agent coordination | Route subtasks to specialized sub-agents and collect results |
| Reflection triggering | Determine when to pause and re-evaluate the current plan |

**Production Orchestration Patterns:**
Instead of relying on generic multi-agent frameworks, which can introduce non-deterministic state transitions and high token overhead, enterprise production systems often build **custom, deterministic state machines**. When business processes have absolute structural dependencies (e.g., a *Compliance Audit* cannot occur before *Data Extraction* is complete and validated), a custom state harness is used to enforce these transitions, manage API retries, and coordinate structured data handoffs between stages with 100% predictability.

---

### Section 2.3: Layer 2 — Reasoning Core

**Model selection as a system design decision:**
Choosing which model(s) to use in an agentic system is an engineering decision with significant cost, latency, and quality implications.

**Model taxonomy:**

| Category | Examples | Strengths | Weaknesses |
|---|---|---|---|
| Frontier large models | GPT-4o, Claude 4.6 Sonnet | Broad capability, strong reasoning | Cost, latency |
| Reasoning models | OpenAI o1/o3, DeepSeek-R1 | Deep multi-step reasoning | Very slow, expensive |
| Small efficient models | Llama 3.3 70B, Gemini 2.5 Flash | Speed, cost, deployable locally | Lower capability ceiling |
| Domain fine-tuned | Custom models | High accuracy in specific domain | Training cost, maintenance |

**Production Reasoning Core Patterns (Model & Semantic Routing):**
Production architectures use a hybrid routing layer to balance execution costs, latency, and performance:
* **Semantic Routing:** Rather than hardcoding model selections per stage, systems implement a semantic router (a lightweight embedding model combined with a fast classifier) that dynamically parses the user's request and intent. Simple queries (e.g. translation, spelling correction, metadata extraction) are routed directly to a small, fast utility model tier, avoiding unnecessary expensive calls to larger models.
* **Frontier / Reasoning Models (e.g., Claude 4.6 Sonnet, DeepSeek-R1):** Routed to for complex, multi-stage reasoning tasks such as *Intent Planning*, *Code Synthesis*, and logical validations where deep reasoning is critical.
* **Utility Models (e.g., Llama 3.3 70B, Gemini 2.5 Flash):** Routed to for low-complexity text classification, metadata tag generation, and formatting tasks.
* *Outcome:* This dynamic semantic routing typically reduces operational token cost by **70%** and cuts task latency by **45%** compared to a monolithic frontier model architecture.

---

### Section 2.4: Layer 3 — Skills

**The skills paradigm:**
Skills represent a fundamental shift in how agent expertise is organized. Rather than encoding all domain knowledge in a single massive system prompt, a skill is a versioned, loadable module of packaged expertise.

**Anatomy of a skill:**
```
skill/
  manifest.json          # metadata, version, description, dependencies
  instructions.md        # natural language instructions for the agent
  templates/             # output format templates
  scripts/               # executable code or tool configurations
  policies/              # constraints and safety rules
  examples/              # few-shot examples
  assets/                # domain-specific data, lookup tables, taxonomies
```

**Production Skills Patterns:**
Production architectures modularize their agent pipelines into discrete, version-controlled skill packages:
* **Data Extraction Skill:** Packages the target data schemas, instructions on how to parse various document formats, and validation rules to verify extraction completeness.
* **Compliance Audit Skill:** Packages domain-specific regulatory rules (e.g., SOC2 or financial auditing policies), few-shot examples, and strict compliance checking logic.
* *Outcome:* Developers can isolate, test, and version-control individual skills in Git without impacting other stages of the pipeline.

---

### Section 2.5: Layer 4 — Tools and Interoperability Protocols

**Model Context Protocol (MCP) in Production:**
Production systems utilize MCP to expose database content, local files, and enterprise documentation to agents as structured **Resources** and **Tools**. For example, data search agents query these resources through standard MCP servers (e.g., `query_database(table="q3_reports")`), removing the need for custom database connectors in the agent code.

**Agent Payments Protocol (AP2) and E-Commerce in Production:**
To acquire high-quality digital assets, APIs, or service licenses dynamically, agents implement AP2 for secure agent-to-merchant commerce:
1. **Intent Mandate:** The user grants the agent permission to purchase necessary API licenses or assets up to a specific budget (e.g., $5.00).
2. **Cart Mandate:** The agent constructs a secure cart detailing the purchase and price, executing the payment via AP2's instant checkout extension.
3. **UCP (Universal Commerce Protocol):** Used to orchestrate checkout delivery status, licensing handoffs, and fulfillment.

---

### Section 2.6: Layer 5 — Memory Systems

**Production Memory Systems Patterns:**
To manage context limits and provide personalized content, production systems use a two-tier memory architecture:
* **Episodic Short-Term Memory:** Retains the step-by-step state of the current active session. If an intermediate generation step fails or requires user correction, the episodic memory maintains the exact progress so the user doesn't lose their draft.
* **Semantic Long-Term Memory:** Stores user profiles and preferences in a local vector database. The agent retrieves past interaction patterns, preferred templates, and style histories to personalize the newly generated content automatically.

---

### Section 2.7: The Core Agentic Loop

**Production Cognitive Loop Cycle:**
Every stage of a production agentic pipeline operates as a cognitive loop:
* **PLAN:** The agent plans the structure of the next output block based on the overall objectives.
* **ACT:** The agent calls the reasoning core to generate the content or execute a tool.
* **OBSERVE:** The output is routed to a validation gate (e.g., checking syntax, format schemas, or semantic rules).
* **REFLECT & ITERATE:** If the output violates a rule, the error is fed back into the reasoning core to re-generate the section. If it fails repeatedly, the loop terminates and escalates to a human operator.
