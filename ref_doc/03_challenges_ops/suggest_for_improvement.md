### Section 3.1: Reliability & Hallucinations

**Why reliability is harder for agents than for LLMs:**  
A single LLM response, even if imperfect, typically fails gracefully — the user sees a bad answer and retries. An agent failure is more consequential:  
- Intermediate failures can propagate through a multi-step pipeline  
- Actions (API calls, file writes, messages sent) may be irreversible  
- The agent may not detect that it has failed (hallucinated success)  
- Failures accumulate: a small error in step 3 may manifest as a catastrophic error in step 12  

**🎯 Workshop hook – Show a real failure log (2 min):**  
Present this anonymised trace and ask: *“Where did the agent go wrong? What was the root cause?”*
```
Step 1: LLM output → {"vendor": "Amaz0n", "amount": "four thousand", "date": "2025-02-30"}
Step 2: Parser → crashes on invalid float
Step 3: Agent retries without context → produces {"vendor": "Amazon", "amount": 4000, "date": "2025-02-30"}
Step 4: Writes to CSV → date fails validation (2025-02-30 does not exist)
Step 5: Agent reports “Successfully wrote invoice” → hallucinated success
```

**How Production Systems Solve Reliability:**  
Production architectures mitigate reliability challenges using a multi-layered verification and recovery strategy:

1. **Guaranteed JSON Generation (Structured Outputs):**  
   Instead of parsing raw text post-inference, production platforms enforce strict JSON outputs directly at the decoding level. Using schema-constrained decoding (via system-level JSON schemas and APIs supported by Claude 4.6 Sonnet), the reasoning core is structurally prevented from producing invalid JSON keys or syntax errors.

   **✋ Code snippet – enforce structured output with Pydantic:**
   ```python
   from pydantic import BaseModel, Field, ValidationError
   from openai import OpenAI

   class Invoice(BaseModel):
       vendor: str = Field(min_length=1)
       amount: float = Field(gt=0)
       date: str = Field(pattern=r"\d{4}-\d{2}-\d{2}")

   client = OpenAI()
   completion = client.beta.chat.completions.parse(
       model="gpt-4o-2024-08-06",
       messages=[...],
       response_format=Invoice
   )
   invoice = completion.choices[0].message.parsed
   ```

2. **Two-Tier Validation Gate:**  
   - *Syntactic Validation:* Platforms feed outputs through a rigid Pydantic schema gate to validate types, ranges, and object relationships immediately upon completion.  
   - *Semantic Grounding Gate:* To prevent the agent from hallucinating domain entities, extracted elements are validated against a local domain metadata index (backed by a localized Trie/Bloom filter).

   **🧠 Workshop exercise (10 min):**  
   Implement the semantic gate: given `allowed_vendors = {"amazon", "walmart", "costco"}`, reject any extracted vendor not in the set (case‑insensitive, fuzzy match allowed) and raise a `ValidationError`.

3. **Contextual Self-Correction (Diff-Based Reflection):**  
   If validation fails, the orchestrator initiates a self-correction loop. Instead of just sending a raw error message, it constructs a structured prompt containing the violating fragment, the specific constraint breached, a semantic diff of what was expected, and corrective guidelines.

   **✋ Code pattern – self‑correction with max attempts:**
   ```python
   for attempt in range(3):
       try:
           result = structured_llm.invoke(prompt + correction_hint)
           validate_syntactic(result)
           validate_semantic(result)
           break
       except ValidationError as e:
           correction_hint = f"Previous error: {e}. Provide only valid JSON matching the schema."
   else:
       # escalate to HITL
       save_to_human_review_queue(context)
   ```

4. **Human-in-the-Loop (HITL) Triaging Interface:**  
   If self-correction fails three times, execution halts, the orchestrator serializes the active state, and a triaging alert is triggered. An operator can review the flagged mismatch via a visual UI, edit the data manually, and hit "Resume" to continue the state machine seamlessly without restarting the pipeline.

   **💬 Debrief question:** *When would you NOT want HITL? (e.g., real‑time trading, high‑throughput batch where human delay is unacceptable)*

---

### Section 3.2: Evaluation

**The trajectory evaluation problem:**  
Traditional LLM evaluation compares a generated answer to a reference answer. Agent evaluation requires evaluating an entire trajectory — every step the agent took, not just its final answer.

**Trajectory evaluation dimensions:**

| Dimension | What to Measure | Production Example |
|---|---|---|
| **Efficiency** | Steps taken vs. minimum possible | Did the agent extract the invoices in under 5 iterations without redundant tool calls? |
| **Planning quality** | Was the initial plan reasonable? | Did the audit plan stay under the target budget and allocate resources appropriately? |
| **Recovery quality** | How well did the agent handle failures? | Did the agent recover from temporary database timeout errors? |
| **Tool selection** | Were the right tools used? | Did the agent query the correct year's customer transaction database? |
| **Safety compliance** | Were guardrails respected? | Did the agent correctly redact PII and sensitive data before exporting results? |
| **Cost efficiency** | Token and API cost for the task | Did the model routing system correctly route low-level steps to cheaper tiers? |

**🎯 Workshop case study (15 min):**  
Provide a sanitised trajectory log (10 steps). In pairs, each group evaluates **one dimension** (e.g., efficiency, tool selection) and assigns a 1‑5 score with justification. Share results – the class sees how the agent almost succeeded but was inefficient/unsafe.

**How Production Systems Implement Evaluation:**  
Enterprise systems move beyond manual review by establishing a programmatic evaluation harness:

1. **Multi-Criteria LLM-as-a-Judge (G-Eval Framework):**  
   Production pipelines deploy a panel of independent, specialized evaluator prompts running on Claude 4.6 Sonnet (e.g., Policy Judge, Structural Judge, Factuality Judge). Each evaluator grades specific criteria using step-by-step reasoning on a 1-5 rubric.

   **✋ Hands‑on – implement a simple judge:**
   ```python
   def evaluate_with_judge(trajectory: dict, rubric: str) -> int:
       prompt = f"""You are a Factuality Judge. Grade this trajectory on a 1-5 scale.
       Rubric: {rubric}
       Trajectory: {trajectory}
       Return only the score and one sentence rationale."""
       response = llm.invoke(prompt)
       return extract_score(response)
   ```

2. **Golden Trajectory Regression Suite:**  
   The development team maintains a regression dataset of 200+ curated enterprise planning scenarios representing diverse customer requests, inputs, and database schemas. Any change to prompts or orchestration triggers an automated CI/CD pipeline run to evaluate agent trajectories against this golden dataset, highlighting drop-offs in quality scores.

3. **Trajectory Assertion Invariants:**  
   Programmatic rules are asserted at the orchestrator layer (e.g., asserting that every output segment maps to at least one verified source node, or that computed totals strictly match the arithmetic sum of the segments).

   **🧠 Exercise:** Write an invariant that checks: “total_amount = sum(line_item.amount) for all line items”. Simulate a failing agent and catch it.

4. **Semantic Distance Measurement:**  
   Platforms compare embeddings of generated content against official policy manuals to compute semantic similarity scores, providing quantitative evidence of compliance.

   **💬 Discussion:** *What is a safe similarity threshold? 0.85? 0.95? How do you avoid false positives?*

---

### Section 3.3: Cost and Latency

**Why agentic systems are expensive:**  
A single agentic task may involve:  
- 10-50 LLM inference calls (planning, reflection, tool result interpretation)  
- 5-20 tool calls (API requests, database queries)  
- 2-5 retrieval operations from vector databases  
- Context windows of 10,000-100,000 tokens per call  

**🎯 Live calculation (5 min):**  
Estimate: 15 LLM calls × (8k input + 2k output) × pricing of Claude 4.6 Sonnet ($3 / 1M input, $15 / 1M output) = ~$0.70 per task.  
For 10,000 tasks/day → $7,000/day. *Ask: “What would your manager say?”*

**How Production Systems Mitigate Cost & Latency:**  
Production systems address the cost-latency-quality trade-off with four core optimizations:

1. **Tiered & Semantic Model Routing:**  
   Rather than running all steps on a single expensive model, production architectures utilize a semantic router to classify user intents and route tasks across model tiers:  
   - *Frontier / Reasoning Tier (Claude 4.6 Sonnet / DeepSeek-R1):* Reserved for complex, high-reasoning tasks like initial intent planning and structural graph extraction.  
   - *Synthesis Tier (Claude 4.6 Haiku / GPT-4o-mini):* Used for intermediate text generation, code drafting, and narrative synthesis.  
   - *Utility Tier (Llama 3.3 70B / Gemini 2.5 Flash):* Handles lightweight tasks like translating vocabulary, extracting tags, and structural formatting.

   **✋ Code pattern – semantic router:**
   ```python
   class TieredRouter:
       def route(self, task: str) -> str:
           if any(kw in task for kw in ["plan", "strategy", "reason"]):
               return "claude-4.6-sonnet"
           elif any(kw in task for kw in ["extract", "parse"]):
               return "gpt-4o-mini"
           else:
               return "llama-3.3-70b"
   ```

2. **Optimized Prompt Layout for Native Prompt Caching:**  
   Platforms separate static inputs (e.g., static compliance rules, system instructions) from dynamic inputs (e.g., the user's specific request). By placing static blocks at the very beginning of prompt contexts, they maximize native provider prompt caching, achieving up to an **80% reduction** in input token fees and cutting latency in half.

   **🧠 Exercise:** Take a 4k token prompt of static rules + 500 token query. Restructure it, enable caching (Anthropic/DeepSeek), measure cost savings.

3. **Semantic Context Pruning (RAG Optimizations):**  
   To prevent stuffing entire database tables into context windows, systems use hybrid dense-sparse search (vector embeddings combined with BM25) to retrieve only the top-$K$ relevant segments (under 10k tokens), preserving reasoning clarity and reducing token overhead.

4. **Asynchronous Parallel Processing:**  
   Non-dependent steps (such as generating separate report sections or testing independent code modules) are executed in parallel via asynchronous Python code (asyncio), reducing user-perceived latency from minutes down to seconds.

   **✋ Live refactor:** Change sequential calls to `asyncio.gather()` – measure wall‑time drop from 45s → 12s.

---

### Section 3.4: Observability and AgentOps

**Why traditional DevOps tooling fails for agents:**  
Traditional observability tools (logs, metrics, traces) were designed for systems whose internal state is expressed in code and data. Agent internal state is expressed in natural language — reasoning that doesn't map cleanly to structured telemetry.

**🎯 Demo – the opacity problem (3 min):**  
Show a raw log of an agent that failed. *“Can you tell why it called `delete_file`? What was the reasoning?”* Participants cannot answer. Then show the same failure with semantic tracing.

**How Production Systems Implement Observability:**  
Production systems treat observability as a first-class production requirement through a specialized AgentOps infrastructure:

1. **Semantic Tracing with MLflow Tracking:**  
   Using MLflow's automated tracking (integrated via `mlflow.langchain.autolog()`), every action is captured as a "Span." Spans record inputs, outputs, token usage, latency, prompt template versions, and model parameters for every LLM and tool call.

   **✋ Hands‑on instrumentation:**
   ```python
   import mlflow
   mlflow.langchain.autolog()
   with mlflow.start_run(run_name="agent_trace"):
       result = agent.invoke("Analyze this contract")
   # Then open MLflow UI to see each LLM call, token usage, and nested spans
   ```

2. **Visual Execution Tree Dashboard:**  
   Developers can view trace spans as a nested hierarchy, showing exactly how the orchestrator routed intent, retrieved memories, parsed tools, and transitioned state. This makes it trivial to locate the exact node responsible for failures or latency spikes.

3. **Offline Trajectory Replay Sandbox:**  
   If a user reports a failed execution or provides negative feedback, developers can extract the execution log, load it into a local sandbox, freeze the exact input state, tweak the system prompts or agent skills, and replay the step to confirm regression fixes.

   **🧠 Exercise:** Capture a failing trajectory, modify one prompt, replay and verify the fix works.

4. **Safety & Policy Guardrails:**  
   At both the input and output boundaries of all tools, real-time safety guardrails (such as Llama Guard or NeMo Guardrails) monitor and filter queries and generations to audit policies, preventing prompt injection or policy violations.

   **💬 Discussion:** *What guardrails would you implement for a customer‑support agent that can access PII?*

---

## Synthesis: Production Agentic System Architecture

Looking back at a production agentic system through the lens of the modern agentic stack:

| Agentic Stack Layer | Production Implementation |
|---|---|
| **Orchestration** | Custom deterministic state machine managing the processing pipeline |
| **Reasoning Core** | Hybrid routing to Claude 4.6 Sonnet / DeepSeek-R1 and Llama 3.3 70B / Gemini 2.5 Flash |
| **Skills** | Modular packages for Data Extraction, Compliance Auditing, and Report Generation |
| **Tools & Protocols** | MCP database/file servers and AP2 payment mandates |
| **Memory** | Vector DB for user profile semantic memory; short-term session state episodic memory |
| **Cognitive Loop** | PLAN → ACT → OBSERVE → REFLECT validation loops at each stage boundary |

Production architectures arrive at this layout through domain-driven engineering, not by applying an existing generic framework. The architectural patterns of agentic AI are not arbitrary — they emerge naturally from the requirements of complex, multi-step, domain-grounded tasks.

**🎯 Closing workshop activity (team challenge):**  
In small groups, take a real business use case (e.g., “automated invoice processing with human approval”). Map it to the stack above, then identify the top 3 risks per layer and propose one mitigation from Sections 3.1–3.4. Present to the class (5 min per group).

**📚 Take‑home checklist:**  
- [ ] Structured output + two‑tier validation  
- [ ] Self‑correction loop (max 3 attempts → HITL)  
- [ ] Trajectory logging + LLM‑as‑a‑judge in CI  
- [ ] Model routing (tiered) + prompt caching  
- [ ] Async parallelism where independent  
- [ ] MLflow tracing for every run  
- [ ] Replay sandbox for failures  
- [ ] Guardrails on tools
