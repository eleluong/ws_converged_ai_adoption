## TRANSITION

**Visual:** Single line: "What if an AI could do this for any domain?"

**Script:**
> "The architecture we built — hierarchical stages, structured workflows, tool integration, human oversight — that pattern is everywhere now. Let's zoom out."

---

## PART II — The Rise of the Agentic AI Stack (40 min)

### Slide 11: Generative AI vs. Agentic AI
**Visual:** Two-column comparison

| Generative AI | Agentic AI |
|---------------|------------|
| Prompt to Response | Goal to Plan to Act to Observe to Reflect to Iterate to Done |
| Single-turn | Multi-turn, iterative |
| Reactive | Autonomous |
| Static output | Adaptive execution |

**Live Example — Travel Agent given "book a weekend trip to Chicago under $600":**
1. Plan: flights, hotel, attractions
2. Act: call flight/hotel APIs
3. Observe: prices over budget
4. Reflect: shift dates, nearby airports
5. Iterate until valid solution
6. Complete: deliver itinerary

**Script:**
> "The language model is no longer the product. It's one component in a larger cognitive architecture. This is the defining shift in modern AI engineering."

---

### Slide 12: The Modern Agentic Stack — Overview
**Visual:** Layered stack diagram

```
+-----------------------------------+
|      5. Memory Systems            |
+-----------------------------------+
|  4. Tools and Protocols           |
|     (MCP, A2A, ACP, AP2...)       |
+-----------------------------------+
|  3. Skills (Packaged Expertise)   |
+-----------------------------------+
|  2. Reasoning Core (LLMs)         |
+-----------------------------------+
|  1. Orchestration Layer           |
+-----------------------------------+
```

---

### Slide 13: Layer 1 — Orchestration

**Responsibilities:** Planning, task decomposition, tool routing, memory management, error handling, retries, multi-agent coordination

**Frameworks:** LangChain, Claude Code, AutoGen, CrewAI

**Example:** In CrewAI, an AnalystAgent plus WriterAgent coordinated by a ManagerAgent — automatic retries on API failure.

---

### Slide 14: Layer 2 — Reasoning Core

**Model types:** Frontier (GPT-4, Claude 3.5), Reasoning (o1, DeepSeek-R1), Multimodal, Small specialized, Hybrid ensembles

**Customer Support Example:**
- Small model: classify issue (billing vs. technical)
- Large model: draft refund justification
- Fine-tuned model: retrieve exact policy clause

**Script:**
> "Part of good agent design is routing tasks to the right model — balancing capability with cost and speed."

---

### Slide 15: Layer 3 — Skills (Packaged Expertise)

**What a Skill contains:** Instructions, workflows, scripts, templates, policies, examples, domain assets

| Skill | Contents |
|-------|----------|
| Lesson planning | Curriculum standards, objective templates, quiz generators |
| Financial reporting | API integration, variance analysis, SEC formatting |
| Code review | Linting rules, security patterns, bug checklists |
| Legal summarization | Citation formats, privilege templates, redaction policies |

**Benefits:** Modularity, reuse, version control, auditability, progressive context loading

---

### Slide 16: Layer 4 — Tools and Protocols

**Tool categories:** Search, databases, APIs, code interpreters, browsers, enterprise software, execution environments

**Core Protocols:**

| Protocol | Creator | Focus |
|----------|---------|-------|
| MCP | Anthropic | Tool/resource discovery — "USB-C for AI" |
| A2A | Community | Agent-to-agent task delegation |
| ACP | Community | Real-time WebSocket agent coordination |

**Commerce Protocols:**

| Protocol | Creator | Focus |
|----------|---------|-------|
| AP2 | Google | Cryptographic payment authorization |
| OpenAI ACP | OpenAI | Conversational commerce / headless checkout |
| UCP | Google | Full commerce workflow orchestration |

**Script:**
> "AP2's Mandate system is particularly interesting: cryptographic proof that an agent acted exactly as the user instructed. That's a meaningful trust layer for autonomous commerce."

---

### Slide 17: Layer 5 — Memory Systems

**Short-Term Memory:** Active reasoning, conversational continuity, temporary task context
Example: "Step 2 complete, proceeding to Step 3"

**Long-Term Memory:** User preferences, project history, retrieved knowledge, historical decisions
Example: "User prefers pytest; deprecated API flagged 3 months ago"

**Techniques:** Vector databases (Chroma, Weaviate), SQLite state, episodic summary buffers

**Script:**
> "Memory is arguably the least solved layer. Poor retrieval or an overloaded context window can corrupt an entire reasoning chain."

---

### Slide 18: The Core Agentic Loop
**Visual:** Animated circular loop

```
PLAN -> ACT -> OBSERVE -> REFLECT -> ITERATE -> COMPLETE
  ^                                                 |
  +-------------------------------------------------+
```

**Worked Example — Research Agent on quantum error correction:**
1. PLAN: search arXiv, download top 3, extract, summarize
2. ACT: call arXiv API
3. OBSERVE: 47 results, too many
4. REFLECT: filter by citation count first
5. ITERATE: fetch metadata, sort, download top 3
6. COMPLETION: summary with citations delivered
