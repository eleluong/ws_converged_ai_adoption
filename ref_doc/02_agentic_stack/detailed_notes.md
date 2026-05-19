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

**The key conceptual additions:**
- **Agency:** the ability to take actions with real-world effects (API calls, file writes, messages sent)
- **Planning:** decomposing a goal into a sequence of subgoals
- **Observation:** reading and interpreting the results of actions
- **Reflection:** evaluating whether the current plan should continue or be revised
- **Iteration:** repeating steps as needed until a goal is achieved or the system determines it cannot proceed

**Why this matters:**
Single-turn generation is suitable for tasks with clear, complete inputs and expected outputs. Agentic systems become necessary when:
- The full information needed to complete a task is not available at the start
- The task requires multiple distinct operations across different systems
- The correct approach depends on intermediate results
- The problem is inherently exploratory

---

### Section 2.2: Layer 1 — Orchestration

**What orchestration actually does:**
The orchestration layer is the "executive function" of an agent system. It holds the plan, tracks progress, routes work to the right components, handles failures, and decides when the task is complete.

**Core orchestration responsibilities:**

| Responsibility | Description |
|----------------|-------------|
| Task decomposition | Break a high-level goal into ordered subtasks |
| Tool routing | Select the appropriate tool or model for each subtask |
| State management | Track what has been done and what remains |
| Error handling | Detect failures and execute retry or fallback strategies |
| Memory management | Decide what to keep in context vs. retrieve from memory |
| Policy enforcement | Apply constraints (budget limits, forbidden actions, scope restrictions) |
| Multi-agent coordination | Route subtasks to specialized sub-agents and collect results |
| Reflection triggering | Determine when to pause and re-evaluate the current plan |

**Orchestration frameworks comparison:**

| Framework | Strengths | Best For |
|-----------|-----------|----------|
| LangChain | Extensive integrations, mature ecosystem | General-purpose pipelines |
| LangGraph | Graph-based state machines, explicit control flow | Complex multi-step workflows |
| CrewAI | Role-based multi-agent coordination | Team-style agent collaboration |
| AutoGen | Conversational multi-agent patterns | Research and exploration tasks |
| Claude Code | Deep code execution, tool integration | Software engineering tasks |
| Custom orchestration | Full control, domain optimization | Production-grade systems |

**Engineering note:** For production systems, custom orchestration often outperforms general frameworks because it can be optimized for the specific failure modes, latency requirements, and cost profiles of the target domain.

---

### Section 2.3: Layer 2 — Reasoning Core

**Model selection as a system design decision:**
Choosing which model(s) to use in an agentic system is an engineering decision with significant cost, latency, and quality implications.

**Model taxonomy:**

| Category | Examples | Strengths | Weaknesses |
|----------|----------|-----------|------------|
| Frontier large models | GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro | Broad capability, strong reasoning | Cost, latency |
| Reasoning models | OpenAI o1, DeepSeek-R1 | Deep multi-step reasoning | Very slow, expensive |
| Multimodal models | GPT-4V, Gemini 1.5, Claude 3 Opus | Image/video understanding | Cost, specialized inputs needed |
| Small efficient models | Llama 3 8B, Mistral 7B | Speed, cost, deployable locally | Lower capability ceiling |
| Domain fine-tuned | Custom models | High accuracy in specific domain | Training cost, maintenance |

**Practical routing patterns:**
- Classification tasks → small model
- Complex reasoning → frontier model
- Domain-specific retrieval → fine-tuned or RAG-augmented model
- Image analysis → multimodal model

**Cost implication:**
Routing every task to a frontier model is expensive and often unnecessary. A well-designed routing layer can reduce inference costs by 60-80% while maintaining quality on the tasks that matter.

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

**Why skills are architecturally superior to monolithic prompts:**

| Issue | Monolithic Prompt | Skill-Based Architecture |
|-------|-------------------|--------------------------|
| Context size | Everything always loaded | Only relevant skill loaded |
| Versioning | Ad hoc, hard to track | Git-versioned, auditable |
| Reuse | Copy-paste, diverges | Shared module, single source of truth |
| Testing | Difficult to isolate | Each skill independently testable |
| Auditability | Opaque | Every skill execution can be logged |
| Updates | Risky, affects everything | Update one skill without affecting others |

**Real-world skill examples:**
- **Code review skill:** contains company linting rules, security vulnerability patterns, common bug checklists, and escalation criteria — loaded by any agent performing code review
- **Customer onboarding skill:** contains product pricing tables, eligibility rules, required documentation, and handoff criteria — loaded by any agent handling new customer intake
- **Compliance checking skill:** contains regulatory rules, audit logging requirements, and reporting templates — loaded by any agent operating in regulated workflows

---

### Section 2.5: Layer 4 — Tools and Interoperability Protocols

**The interoperability problem:**
As agentic systems proliferated, each team built custom integrations for every tool. An agent needing to call Stripe, query PostgreSQL, and read from Google Drive required three custom integration implementations — each with its own authentication, error handling, and schema.

MCP and related protocols solve this by standardizing the interface between agents and tools.

**MCP (Model Context Protocol) deep dive:**

MCP defines three primitive types:
1. **Tools:** Functions the agent can invoke (get_weather, create_ticket, run_query)
2. **Resources:** Data the agent can read (files, database rows, API responses)
3. **Prompt templates:** Reusable prompt structures for common tasks

An MCP server exposes these primitives; an MCP client (the agent) discovers and calls them. The analogy to a USB-C standard is apt: any compliant client can connect to any compliant server without custom code.

**A2A (Agent-to-Agent Protocol) deep dive:**

A2A enables agents from different frameworks to delegate work to each other. Key design goals:
- Framework-agnostic (LangChain agent can delegate to AutoGen agent)
- Structured task messages with defined schemas
- Status updates, artifact delivery, error reporting
- No requirement for shared infrastructure

**Commerce protocols — why they represent a qualitative shift:**

AP2, OpenAI ACP, and UCP collectively enable agents to participate in commercial transactions autonomously. This is qualitatively different from tool use:
- Tool use: agent reads/writes data
- Commerce participation: agent initiates financial transactions with real consequences

**AP2 Mandate system:**
The mandate system addresses a fundamental trust problem in agentic commerce. If an agent makes a purchase on a user's behalf, how can:
- The merchant verify the user actually authorized it?
- The user prove what they authorized?
- The platform audit the transaction?

AP2 Mandates solve this with cryptographic signatures:
1. User signs an Intent Mandate specifying constraints (price limit, item category, timing)
2. Agent operates within mandate constraints
3. At purchase, agent creates a Cart Mandate (specific items, price) — also cryptographically signed
4. Non-repudiable audit trail exists for every transaction

This enables an entirely new class of agent use cases: autonomous procurement, automated subscription management, agent-led financial services.

---

### Section 2.6: Layer 5 — Memory Systems

**The memory challenge in agentic systems:**

LLMs have a fixed context window — a finite amount of text they can "hold in mind" at once. For simple tasks, this is sufficient. For complex, long-running agentic tasks, it is a fundamental constraint:
- A research agent processing dozens of papers will exceed any context window
- A customer service agent handling a 6-month customer relationship cannot hold all history in context
- A coding agent working on a large codebase cannot load all files simultaneously

Memory systems solve this by externalizing information and retrieving it on demand.

**Memory taxonomy:**

| Memory Type | Storage Location | Retrieval Method | Lifetime |
|-------------|-----------------|------------------|----------|
| In-context (working) | LLM context window | Direct access | Duration of current invocation |
| Episodic (short-term) | In-memory buffer | Sequential access | Duration of session |
| Semantic (long-term) | Vector database | Similarity search | Persistent across sessions |
| Procedural (skill) | Skill files | Keyword/metadata lookup | Persistent, versioned |
| Structured (state) | SQL/KV store | Query by key | Persistent |

**Vector database mechanics:**
Semantic memory works by converting text into vector embeddings and storing them in a database optimized for similarity search. When the agent needs relevant information, it converts its current query into a vector and retrieves the most similar stored vectors. This enables "remembering" relevant past information without loading all history into context.

**Active challenges:**
- **Retrieval precision:** returning relevant information without noise
- **Staleness:** knowing when stored information is out of date
- **Context integration:** seamlessly integrating retrieved information with current reasoning
- **Memory management:** deciding what to store, update, or discard

---

### Section 2.7: The Core Agentic Loop

**Loop anatomy:**

```
PLAN  -- Decompose goal into steps; select tools and approach
  |
ACT   -- Execute the next planned step (call tool, write output, delegate)
  |
OBSERVE -- Read the result; detect success, failure, or unexpected output
  |
REFLECT -- Evaluate: is the current plan still valid? Should it be revised?
  |
ITERATE -- If plan unchanged, execute next step; if plan revised, re-plan
  |
COMPLETE -- When goal is achieved or max iterations reached
```

**Where loops fail:**
- **Hallucinated observations:** the model reports a tool succeeded when it failed
- **Plan fixation:** the model continues with an invalid plan despite evidence to revise
- **Infinite loops:** the model cycles without making progress (no convergence condition)
- **Scope creep:** the model expands the task beyond its original boundaries
- **Premature termination:** the model declares success before the goal is fully achieved

**Loop control mechanisms:**
- Maximum iteration limits (hard stop)
- Budget-based stopping (cost ceiling)
- Progress detection (have intermediate outputs changed?)
- Human escalation triggers (uncertainty threshold exceeded)
- Explicit stopping criteria in the system prompt
