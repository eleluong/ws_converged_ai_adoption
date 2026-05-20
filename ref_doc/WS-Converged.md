# **ConnectED & the Emerging Agentic AI Stack**

## **Part I — ConnectED: An AI-Native Platform for Vietnamese Education**

### **Overview**

**ConnectED** is an AI-powered lesson planning platform designed specifically for the Vietnamese K–12 education system. The platform enables teachers to rapidly generate curriculum-aligned lesson plans, teaching materials, animations, and virtual laboratory experiences while preserving pedagogical quality and local educational standards.

The motivation behind ConnectED emerged from a practical challenge faced by many educators: preparing a single high-quality lesson can require several hours of manual work. While large language models (LLMs) such as ChatGPT have demonstrated strong generative capabilities, their outputs are often too generic, culturally misaligned, or inconsistent with Vietnam’s curriculum when used without careful contextualization. Research and pilot studies have shown that AI can significantly reduce lesson-planning time, but only when the system is grounded in the target educational environment and supported by structured instructional workflows.

Rather than treating AI as a one-shot content generator, ConnectED approaches lesson creation as a multi-stage instructional design process. The system combines pedagogical frameworks, hierarchical AI orchestration, and localized curriculum knowledge to support teachers throughout the full lesson development lifecycle.

---

## **Problem Context**

Teachers frequently spend three to four hours preparing a complete lesson, including:

* defining learning objectives,  
* extracting key concepts from textbooks,  
* designing classroom activities,  
* creating visual materials,  
* preparing assessments, and  
* adapting content to student needs.

Although general-purpose LLMs can generate educational content quickly, they often fail in several important areas:

* **Weak Curriculum Alignment:** Defaulting to Western curriculum structures or out-of-textbook topics.
* **Inaccurate Pedagogical Sequencing:** Poor structural flow that doesn't respect standard 45-minute classroom timelines.
* **Inconsistent Terminology:** Mixing translated terms rather than adhering to official Ministry of Education and Training (MOET) standards.
* **Lack of Cultural Localization:** Presenting examples or contexts unfamiliar to Vietnamese students.
* **Vague Activity Design:** Suggesting class projects that are logistically or financially infeasible for local classrooms.
* **Hallucinated Educational Content:** Misrepresenting historical facts, science formulas, or curriculum requirements.

In early experiments, the team observed that generic prompts consistently defaulted toward Western educational assumptions and curriculum structures. This reinforced a critical insight: educational AI systems must be deeply localized and pedagogically grounded rather than relying solely on raw generative capability.

To address these issues, ConnectED adopted a teacher-centered development process. The team conducted interviews with educators, gathered iterative feedback, and incorporated Vietnamese instructional standards directly into the system architecture and prompting workflows.

---

## **Instructional Design Foundation: ADDIE**

A key differentiator of ConnectED is its integration of the **ADDIE instructional design model**:

1. **Analyze**  
2. **Design**  
3. **Develop**  
4. **Implement**  
5. **Evaluate**

Instead of generating an entire lesson in a single prompt, ConnectED decomposes lesson creation into structured instructional stages.

### **Analyze**

The system first processes textbooks and curriculum documents to identify:

* core concepts,  
* learning outcomes,  
* prerequisite knowledge,  
* competency targets, and  
* instructional constraints.

This stage establishes the semantic and pedagogical foundation for downstream generation.

### **Design**

Based on the extracted objectives, the platform generates:

* lesson structures,  
* classroom activities,  
* interaction flows,  
* timing allocations,  
* discussion prompts, and  
* assessment strategies.

The focus here is pedagogical coherence rather than surface-level content generation.

### **Develop**

The system then creates educational assets, including:

* slide content,  
* animation scripts,  
* virtual laboratory instructions,  
* quizzes,  
* diagrams, and  
* multimedia teaching materials.

A particularly effective design decision was the adoption of a **script-first workflow**, where the instructional narrative is generated before visual assets. This improves consistency, clarity, and instructional accuracy across generated materials.

### **Implement & Evaluate**

Finally, teachers review, refine, and adapt generated lessons before classroom deployment. Human oversight remains central to the workflow, allowing educators to maintain pedagogical control while benefiting from AI-assisted acceleration.

---

## **Hierarchical Agent Pipeline**

ConnectED does not rely on a monolithic prompt architecture. Instead, it uses a **hierarchical agent pipeline** in which specialized stages handle distinct subtasks.

This decomposition offers several advantages:

* reduced prompt complexity,  
* improved controllability,  
* easier verification,  
* modular debugging,  
* lower hallucination rates, and  
* stronger pedagogical consistency.

Rather than asking a single model to solve the entire problem at once, each stage operates within a constrained scope and passes structured outputs to subsequent stages.

The workflow can be summarized as:

`Concept Extraction → Objective Generation → Activity Design → Content Development → Visual Material Generation → Evaluation`

This architecture mirrors emerging trends in agentic AI systems, where orchestration and structured reasoning outperform purely prompt-based approaches.

---

## **Virtual Labs and Interactive Learning**

ConnectED also integrates virtual laboratory experiences and interactive simulations, particularly for STEM education. These include:

* experiment visualizations,  
* physics simulations,  
* chemistry demonstrations,  
* interactive diagrams, and  
* exploratory learning modules.

Virtual laboratories are especially valuable in contexts where schools lack physical infrastructure or equipment. By combining simulation tools with AI-generated instructional scaffolding, ConnectED helps students engage with abstract concepts through more concrete and experiential learning.

Importantly, these materials are generated within the context of the lesson objectives rather than as disconnected multimedia artifacts.

---

## **Localization as a Core Principle**

One of the most important lessons from the project was that localization cannot be treated as an afterthought.

ConnectED embeds Vietnamese educational context directly into:

* prompts,  
* instructional templates,  
* terminology,  
* assessment structures,  
* examples,  
* classroom language, and  
* curriculum mappings.

This localization extends beyond simple translation. The system reflects local pedagogy, classroom expectations, and curriculum sequencing, enabling outputs that feel native to Vietnamese educators rather than adapted from foreign educational systems.

---

## **Impact**

In practice, ConnectED reduced lesson preparation time dramatically. Tasks that previously required several hours could often be completed in approximately 15–20 minutes while maintaining high instructional quality.

More importantly, the platform demonstrated that educational AI systems become significantly more effective when:

* pedagogy is embedded into the architecture,  
* workflows are decomposed hierarchically,  
* teachers remain in the loop, and  
* localization is treated as foundational infrastructure.

The project illustrates a broader transition in AI engineering: moving from isolated model outputs toward orchestrated, domain-specific intelligent systems.

---

## **Part II — Beyond the Competition: The Rise of the Agentic AI Stack**

### **From Generative AI to Agentic AI**

Traditional generative AI systems operate through a relatively simple interaction pattern:  
**User Prompt → Model Response** (Single-turn conversation).  
While powerful, this paradigm is fundamentally reactive and limited to single-turn generation.  
*Example:* Asking ChatGPT to “write a short story about a detective” produces one response, but the model cannot independently search for crime scene details, update the plot based on new clues, or coordinate with another AI to illustrate a character.  

**Agentic AI** introduces a fundamentally different model of interaction. Instead of merely producing text, the system operates through iterative reasoning and execution loops:  
**Goal → Plan → Act → Observe → Reflect → Iterate → Completion**  

In this framework, the language model becomes only one component within a larger cognitive architecture. The agent can:

* plan tasks,  
* invoke tools,  
* retrieve external information,  
* execute actions,  
* evaluate intermediate results,  
* revise strategies, and  
* coordinate with other agents or systems.

This transition represents one of the most significant shifts in modern AI engineering: from passive generation toward autonomous problem-solving systems.

---

### **The Modern Agentic Stack**

Modern AI agents are not standalone models. They are complex orchestration systems composed of five interconnected layers. Below, we break down each layer and map it directly to how it is implemented in production systems.

```
+-------------------------------------------------------+
|  5. Memory Systems (Short/Long-Term User Profiles)    |
+-------------------------------------------------------+
|  4. Tools & Protocols (MCP DB Querying & AP2 Payments) |
+-------------------------------------------------------+
|  3. Skills (Domain Rules, Pydantic Schema Packages)  |
+-------------------------------------------------------+
|  2. Reasoning Core (Model Routing: Frontier & Small)  |
+-------------------------------------------------------+
|  1. Orchestration Layer (Custom State Machine/Harness)|
+-------------------------------------------------------+
```

#### **1. Orchestration Layer**
The orchestration layer manages the overall execution lifecycle, plan decomposition, state transitions, and error recovery.

* **In General Stack:** Frameworks like LangChain, LangGraph, AutoGen, and CrewAI manage the coordination of agents and tasks.
* **In Production Systems:** Rather than relying on generic multi-agent frameworks, which can introduce non-deterministic state transitions and high token overhead, enterprise production systems often build **custom, deterministic state machines**. When business processes have absolute structural dependencies (e.g., a *Compliance Audit* cannot occur before *Data Extraction* is complete and validated), a custom state harness is used to enforce these transitions, manage API retries, and coordinate structured data handoffs between stages with 100% predictability.

#### **2. Reasoning Core**
At the center sits the reasoning engine—the LLMs that supply semantic understanding and planning capability.

* **In General Stack:** Hybrid ensembles route queries between large frontier models (e.g., Claude 4.6 Sonnet, OpenAI o1/o3) and smaller models (e.g., Llama 3.3 70B, Gemini 2.5 Flash).
* **In Production Systems:** Production systems implement a **Model Routing Pattern** incorporating **Semantic Routing** to optimize the cost-latency-quality triangle:
  * **Semantic Routing:** Rather than hardcoding models per stage, a lightweight semantic intent classifier dynamically routes tasks. Simple, utility-oriented queries (e.g., translations, spelling correction) are sent directly to the small utility tier.
  * **Frontier / Reasoning Models (Claude 4.6 Sonnet / DeepSeek-R1):** Used during the complex planning, design, and extraction stages, where deep reasoning, semantic structure, and domain rules are critical.
  * **Utility Models (Llama 3.3 70B / Gemini 2.5 Flash):** Used for low-complexity steps such as vocabulary translation, keyword tagging, metadata classification, and simple formatting adjustments.
  * *Result:* This routing strategy reduces operational token costs by **70%** and end-to-end latency by **45%** compared to running a frontier model exclusively.

#### **3. Skills: Packaged Expertise**
A skill is a modular, versioned package containing system prompts, output schemas, validation rules, and templates that define specialized capabilities.

* **In General Stack:** Agents load domain-specific skills (e.g., code review, SEC filing analysis) dynamically.
* **In Production Systems:** Production architectures treat each stage of the processing pipeline as an isolated, version-controlled **Skill Module**:
  * **Data Extraction Skill:** Contains a custom system prompt, a strict JSON schema for target document nodes, and lookup reference data.
  * **Compliance Audit Skill:** Implements the domain-specific regulatory rules (e.g., SOC2 or financial auditing policies), few-shot examples, and strict validation checks.
  * *Benefit:* Developers can tweak, test, and version-control individual skill packages (via git) without risking regressions in other parts of the codebase.

#### **4. Tools and Interoperability Protocols (MCP, AP2, ACP, UCP)**
Protocols form the interface enabling agents to securely connect with tools, data, and external payment systems.

* **Model Context Protocol (MCP):** Production systems utilize MCP to expose database content, local files, and enterprise documentation to agents as structured **Resources** and **Tools**. For example, data search agents query these resources through standard MCP servers (e.g., `query_database(table="q3_reports")`), removing the need for custom database connectors in the agent code.
* **Agent Payments Protocol (AP2):** To acquire high-quality digital assets, APIs, or service licenses dynamically, agents implement AP2 for secure agent-to-merchant commerce:
  * **Intent Mandate:** The user signs a cryptographic mandate stating: *"Authorize the agent to acquire API computational resources for this analysis, spending up to $5.00 total."*
  * **Cart Mandate & Checkout:** The buyer agent finds a compliant vendor, constructs a Cart Mandate containing the purchase details and the exact price, and completes the instant checkout securely.
* **ACP (Agent Communication Protocol) & UCP (Universal Commerce Protocol):** Used to orchestrate full order-fulfillment and coordinate real-time asset delivery status.

#### **5. Memory Systems**
Memory systems allow agents to maintain state and context across multi-step execution paths and user sessions.

* **In General Stack:** Short-term memory buffers active session states, while long-term memory retrieval handles semantic search over vector databases.
* **In Production Systems:** Production systems balance two distinct memory paths:
  * **Episodic Short-Term Memory:** Tracks the in-progress state of an active session. If the agent fails or requires human feedback during a complex process, the episodic memory stores the current context (draft state, validated goals, rejected formats) so the user can resume immediately without re-generating previous steps.
  * **Semantic Long-Term Memory:** Utilizes a vector database (e.g., SQLite with Vector Extensions) to store user profiles, including historical preferences, style guidelines, and past feedback. When starting a new task, the agent retrieves this contextual memory to tailor the generation style to the user.

---

## **Part III — Persistent Challenges in Agentic AI & Production Mitigations**

Operating agentic systems in production exposes unique challenges. The table below outlines how these challenges present themselves and how production systems successfully mitigate them.

| Challenge | General Production Failure Mode | Production Engineering Mitigation |
|:---|:---|:---|
| **Reliability & Hallucinations** | System loops infinitely, outputs malformed payloads, or hallucinated tools/APIs. | **JSON Constraints, Multi-Tier Validation & HITL:** Uses guaranteed JSON decoding at the inference level. Incorporates syntactic validation (Pydantic) and semantic grounding validation against a domain index database (Trie/Bloom filter). Employs diff-based self-correction, falling back to a Human-in-the-Loop (HITL) dashboard if validation fails 3 times. |
| **Evaluation** | Traditional LLM benchmarks fail to evaluate multi-step reasoning trajectories. | **Multi-Criteria Judges & Regression Tests:** Employs a G-Eval framework with specialized judge prompts running on Claude 4.6 Sonnet (Policy, Structural, Factuality) scoring 1-5 rubrics. Trajectories are evaluated against a 200+ scenario golden dataset in CI/CD, alongside programmatic assertions and embedding semantic distance checks. |
| **Cost & Latency** | Multi-step agent loops trigger massive token bills and slow response times (2+ minutes). | **Tiered & Semantic Routing, Cache Optimization:** Routes tasks dynamically via a semantic intent classifier to specific tiers (Frontier: Claude 4.6 Sonnet / DeepSeek-R1; Synthesis: Claude 4.6 Haiku; Utility: Llama 3.3 70B / Gemini 2.5 Flash). Pins static templates at the front to achieve up to 80% prompt caching savings, and runs non-dependent tasks in parallel via async routines. |
| **Observability (AgentOps)** | Opaque "black box" agent loops make debugging and compliance auditing impossible. | **Semantic Tracing, Replays & Audits:** Instruments spans using the OpenInference standard (with tools like Langfuse or Arize Phoenix). Surfaces nested hierarchical traces in an execution tree dashboard, enables offline trajectory replay of production failures in local sandboxes to test fixes, and deploys real-time input/output safety guardrails. |

---

## **Conclusion**

The future of AI applications lies not in isolated model outputs, but in carefully engineered intelligent systems that combine:

* deterministic orchestration harnesses,
* specialized skills and domain-specific knowledge,
* standard interoperability protocols like MCP and AP2,
* hybrid reasoning cores,
* and human-in-the-loop collaboration models.

As agentic systems move into enterprise deployment, success will be defined not by the raw capability of the foundation model alone, but by the engineering rigor of the system surrounding it.
