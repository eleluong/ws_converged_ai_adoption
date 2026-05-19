# Workshop Handout
## ConnectED & the Emerging Agentic AI Stack
### Practical Checklists for Building Production Agentic Systems

---

> **How to use this handout:**
> Work through each checklist when building or reviewing an agentic system.
> Items marked [CRITICAL] are non-negotiable for production deployment.
> Items marked [RECOMMENDED] are best practices that significantly improve outcomes.
> Items marked [ADVANCED] apply to mature or high-stakes systems.

---

## QUICK REFERENCE: Core Concepts

### The Agentic Loop
```
PLAN → ACT → OBSERVE → REFLECT → ITERATE → COMPLETE
```

### The Agentic Stack (bottom to top)
```
1. Orchestration Layer    (LangChain, CrewAI, AutoGen, custom)
2. Reasoning Core         (LLMs, reasoning models, multimodal)
3. Skills                 (packaged expertise, versioned modules)
4. Tools & Protocols      (MCP, A2A, ACP, APIs, databases)
5. Memory Systems         (short-term context, long-term vector DB)
```

### ConnectED Pipeline
```
Concept Extraction → Objective Generation → Activity Design
→ Content Development → Visual Materials → Evaluation Review
```

### ADDIE Model
```
Analyze → Design → Develop → Implement → Evaluate → (repeat)
```

---

## CHECKLIST 1: Agentic System Deployment

Use this before taking any agent-based system into production.

### Architecture and Design

- [ ] [CRITICAL] Task has been decomposed into clearly bounded subtasks with defined inputs and outputs
- [ ] [CRITICAL] Each subtask has a specified failure mode and fallback strategy
- [ ] [CRITICAL] Human-in-the-loop checkpoints are defined for high-stakes decision points
- [ ] [RECOMMENDED] Pipeline uses hierarchical decomposition (no monolithic single-prompt architecture)
- [ ] [RECOMMENDED] Each stage produces structured, schema-validated output
- [ ] [RECOMMENDED] Skills are modular and version-controlled (not embedded in monolithic prompts)
- [ ] [RECOMMENDED] Domain localization requirements are documented and embedded in prompts/templates
- [ ] [ADVANCED] Agent has explicit stopping criteria (not just max iteration limits)
- [ ] [ADVANCED] Budget and cost ceiling are enforced at the orchestration layer

### Safety and Guardrails

- [ ] [CRITICAL] Forbidden action types are explicitly defined and enforced (not just mentioned in prompts)
- [ ] [CRITICAL] Agent cannot irreversibly modify production data without human confirmation
- [ ] [CRITICAL] API keys and secrets are never passed into LLM context
- [ ] [CRITICAL] Output sanitization is in place before any agent output is surfaced to users
- [ ] [RECOMMENDED] Prompt injection attack vectors have been assessed and mitigated
- [ ] [RECOMMENDED] Maximum cost per task is hard-capped at the orchestration layer
- [ ] [RECOMMENDED] Agent escalation path is defined (what happens when agent is uncertain?)
- [ ] [ADVANCED] Red-team adversarial testing has been performed
- [ ] [ADVANCED] Compliance and regulatory requirements have been mapped to agent constraints

### Observability (AgentOps)

- [ ] [CRITICAL] Every LLM call is logged with: timestamp, model, prompt, response, latency, tokens
- [ ] [CRITICAL] Every tool call is logged with: tool name, inputs, outputs, success/failure
- [ ] [RECOMMENDED] Full agent trajectories are stored and replayable
- [ ] [RECOMMENDED] Cost per task is tracked and reportable
- [ ] [RECOMMENDED] Failure rates by stage are monitored with alerting thresholds
- [ ] [RECOMMENDED] Reasoning quality metrics are defined (even if manual at first)
- [ ] [ADVANCED] LLM-as-judge evaluation is automated on a sample of trajectories
- [ ] [ADVANCED] Anomaly detection is configured for unusual token usage or error rates

### Infrastructure and Reliability

- [ ] [CRITICAL] All external API calls have retry logic with exponential backoff
- [ ] [CRITICAL] Agent is tested against API unavailability (graceful degradation)
- [ ] [RECOMMENDED] Tool calls are idempotent where possible (safe to retry)
- [ ] [RECOMMENDED] Agent state is persisted so tasks can resume after failure
- [ ] [RECOMMENDED] Timeout limits are configured per stage and per task
- [ ] [RECOMMENDED] Load testing has been performed at expected peak volume
- [ ] [ADVANCED] Circuit breakers are in place for frequently failing tools
- [ ] [ADVANCED] Multi-region or multi-model fallback is configured

### Launch Readiness

- [ ] [CRITICAL] End-to-end test suite passes with greater than 90% success rate on representative tasks
- [ ] [CRITICAL] Incident response plan is documented (who to contact, how to roll back)
- [ ] [RECOMMENDED] Rollout is staged (canary deployment before full production)
- [ ] [RECOMMENDED] User feedback mechanism is in place from day one
- [ ] [RECOMMENDED] Documentation of agent capabilities AND limitations is published

---

## CHECKLIST 2: Prompt and Pipeline Optimization

Use this when reviewing or refactoring agent prompts and pipeline structure.

### Prompt Design

- [ ] System prompt is focused on a single, well-defined task
- [ ] Instructions are in imperative form ("Extract the following..." not "You should extract...")
- [ ] Output format is specified explicitly (JSON schema, markdown template, etc.)
- [ ] Examples (few-shot) are included for complex or ambiguous output formats
- [ ] Constraints are stated as explicit rules, not implicit expectations
- [ ] Prompt has been tested on edge cases and adversarial inputs
- [ ] System prompt and user prompt are clearly separated
- [ ] Irrelevant context has been removed to reduce noise and token cost
- [ ] Domain terminology is consistently used (no synonym variation within a prompt)
- [ ] Prompt version is tracked in version control

### Context Management

- [ ] Context window usage is measured per stage (do not assume it is fine)
- [ ] Only the information needed for the current stage is included in context
- [ ] Long-running conversations or sessions use summarization before re-injection
- [ ] Retrieved documents are chunked and filtered before inclusion
- [ ] System prompt is not duplicated across stages (use caching or shared reference)
- [ ] Intermediate outputs are compressed before passing to downstream stages

### Pipeline Structure

- [ ] Each stage has a single, verifiable responsibility (no "and also" stages)
- [ ] Stage boundaries are defined by data contracts (input/output schemas)
- [ ] Stages that can run in parallel are identified and parallelized
- [ ] Validation occurs at every stage boundary, not just at final output
- [ ] Error handling strategy is explicit per stage (retry, skip, fallback, escalate)
- [ ] Stage ordering is optimized (expensive stages run only after cheap validation stages pass)
- [ ] Dead-end stages (stages that never pass validation) are detected and flagged

### Model Routing

- [ ] Classification and routing tasks use the cheapest capable model
- [ ] Complex reasoning tasks use an appropriately powerful model
- [ ] Model selection for each stage is documented with justification
- [ ] Model substitution has been tested (can you swap models without breaking the pipeline?)
- [ ] Latency requirements have been matched to model response time characteristics

---

## CHECKLIST 3: Token Usage Optimization

Use this to systematically reduce inference cost without sacrificing quality.

### Measurement (Do This First)

- [ ] Current token usage per task is measured and logged (input tokens, output tokens, cache hits)
- [ ] Cost per task is calculated and tracked over time
- [ ] Token distribution by stage is known (which stages are most expensive?)
- [ ] Baseline quality metric exists to validate that optimizations do not degrade performance

### Prompt Compression

- [ ] Remove redundant instructions that repeat information already established
- [ ] Replace verbose descriptions with concise directives
- [ ] Use references to shared context rather than repeating context in each prompt
- [ ] Remove examples that are no longer necessary (few-shot can be replaced with fine-tuning for high-volume tasks)
- [ ] Convert tabular or list data to more compact representations when possible
- [ ] Eliminate hedge language ("please", "if possible", "try to") that adds tokens without adding information

### Context Caching

- [ ] System prompts that are reused across tasks are cached (Anthropic, OpenAI both support prompt caching)
- [ ] Shared context (curriculum standards, company policies, terminology glossaries) is cached
- [ ] Cache hit rates are monitored
- [ ] Cache invalidation strategy is defined (when does the cache need to be refreshed?)

### Model Selection for Cost

| Task Type | Recommended Model Size |
|-----------|----------------------|
| Binary classification | Tiny model (1B-3B) or rule-based |
| Entity extraction | Small model (7B-13B) or fine-tuned |
| Summarization | Small to medium model (13B-70B) |
| Complex reasoning | Large frontier model |
| Code generation | Specialized code model or frontier |
| Creative generation | Medium to large model |

- [ ] Each stage has been assigned the minimum capable model (not the maximum available)
- [ ] Routing logic is implemented so task type determines model selection
- [ ] A/B tests have validated quality equivalence when using smaller models

### Context Window Management

- [ ] Maximum context per stage is defined and enforced
- [ ] Documents exceeding context limits are chunked and processed iteratively
- [ ] Conversation history is summarized before re-injection (do not pass full history)
- [ ] Retrieval results are ranked and trimmed to the most relevant N documents
- [ ] Output length constraints are specified in prompts ("in 3 sentences or fewer")

### Output Length Control

- [ ] Output format is specified to avoid verbose preambles ("Sure! Here is..." wastes tokens)
- [ ] Structured output (JSON) is used instead of narrative when downstream parsing is needed
- [ ] Maximum output length is set where appropriate
- [ ] Post-processing extracts only the needed fields from verbose outputs

### Cost Monitoring

- [ ] Cost alerts are configured for: per-task cost threshold, daily/monthly budget
- [ ] Cost anomalies (tasks suddenly costing 10x normal) trigger investigation
- [ ] Cost trends are reviewed weekly during active development
- [ ] Cost per quality unit (cost per successfully completed task) is tracked, not just absolute cost

---

## CHECKLIST 4: Agent Reliability and Evaluation

Use this to assess and improve agent reliability in production.

### Failure Mode Inventory

Document and test for each of the following:

- [ ] **Hallucinated tool usage:** agent calls a tool that does not exist or with invalid parameters
- [ ] **Infinite reasoning loops:** agent repeats the same step without progress
- [ ] **Context corruption:** earlier errors silently propagate into later stages
- [ ] **Planning instability:** agent changes plan erratically without evidence justifying the change
- [ ] **Instruction drift:** agent gradually deviates from its original instructions over long tasks
- [ ] **Over-delegation:** agent delegates tasks it should handle itself, losing context
- [ ] **Premature termination:** agent declares success before completing the goal
- [ ] **Scope creep:** agent expands the task beyond its authorized boundaries
- [ ] **Brittle coordination:** multi-agent handoffs fail when one agent deviates from expected format

### Evaluation Dimensions

For each agent task, define measurement criteria across:

| Dimension | Measurement Approach | Passing Threshold |
|-----------|---------------------|------------------|
| Task completion rate | % of tasks reaching successful completion | Set per domain (e.g., >85%) |
| Step efficiency | Steps taken / minimum steps possible | < 2x minimum |
| Error recovery rate | % of encountered errors successfully recovered | > 70% |
| Tool selection accuracy | % of tool calls using the optimal tool | > 90% |
| Output quality | LLM-as-judge or human rating | Domain-specific |
| Cost per task | Average token + API cost | Set per task type |
| Latency | End-to-end task completion time | Set per SLA |
| Safety compliance | % of tasks with no guardrail violations | 100% |

### Testing Framework

- [ ] Unit tests exist for each stage in isolation (mock inputs and outputs)
- [ ] Integration tests exist for full pipeline end-to-end on representative tasks
- [ ] Regression test suite covers all known past failure modes
- [ ] Adversarial test suite attempts to trigger common failure modes
- [ ] Tests run automatically on every pipeline change (CI/CD integration)
- [ ] Test coverage is reported by stage

### Trajectory Evaluation

- [ ] Sample of production trajectories is reviewed weekly by a domain expert
- [ ] LLM-as-judge evaluation is run on a random sample of trajectories
- [ ] Failed trajectories are tagged and analyzed for root cause
- [ ] Root causes are categorized (prompt issue, model issue, tool issue, orchestration issue)
- [ ] Fixes are tracked back to the trajectory that exposed the failure

### Human-in-the-Loop Integration

- [ ] Escalation triggers are defined (uncertainty threshold, high-stakes action, novel situation)
- [ ] Escalation workflow is implemented (notify human, pause task, await decision)
- [ ] Human decisions are logged and fed back into agent improvement
- [ ] Agent behavior after human decision is tracked (did the agent follow the human's guidance?)
- [ ] Escalation rate is monitored (high rate = agent is not confident enough; near-zero = agent may be overconfident)

---

## CHECKLIST 5: AgentOps and Observability

Use this to build and maintain visibility into agent behavior in production.

### Logging and Tracing

- [ ] Every LLM call logged: model, timestamp, prompt hash, token counts, latency, response
- [ ] Every tool call logged: tool name, input parameters, output, success/failure, latency
- [ ] Every agent decision point logged: what options were considered, what was chosen and why
- [ ] Log storage is configured with appropriate retention (minimum 30 days for debugging)
- [ ] Logs are structured (JSON) and queryable
- [ ] Trace IDs link all log entries for a single task together

### Monitoring and Alerting

- [ ] Success rate monitored per task type with alerting on degradation
- [ ] Average tokens per task monitored with alerting on cost spikes
- [ ] Latency monitored with P50, P90, P99 percentiles tracked
- [ ] Error rate monitored by error type (tool failure, model failure, validation failure)
- [ ] Guardrail violation rate monitored (any violations are high priority)
- [ ] Alerts are configured with clear runbooks for each alert type

### Replay and Debugging

- [ ] Failed trajectories can be fully replayed (inputs, intermediate states, tool responses)
- [ ] Replay environment is isolated from production (no real side effects)
- [ ] Debugging workflow is documented (how to go from alert → log → trajectory → root cause)
- [ ] At least one person on the team has performed a full trajectory debugging session

### Cost Visibility

- [ ] Cost per task is tracked in real time
- [ ] Cost breakdown by stage is available (which stage is most expensive?)
- [ ] Cost breakdown by model is available
- [ ] Daily and monthly cost summaries are reviewed by the team
- [ ] Cost efficiency trend is tracked (cost per successful task should decrease over time as system matures)

### Governance and Compliance

- [ ] All agent actions that could affect external systems are logged with user attribution
- [ ] Log access is restricted to authorized personnel
- [ ] Sensitive data in prompts and responses is masked in logs
- [ ] Data retention policies comply with applicable regulations
- [ ] Agent audit logs can be exported for compliance review
- [ ] Incident response procedure includes log preservation steps

### Continuous Improvement Loop

- [ ] Weekly review of failed trajectories is scheduled
- [ ] Improvement backlog is maintained with priority and expected impact
- [ ] Prompt changes are A/B tested before full deployment
- [ ] Model upgrades are validated against the full regression test suite before adoption
- [ ] Quality metrics trend is reviewed monthly to assess overall system health

---

## QUICK REFERENCE: Design Principles

### From ConnectED

| Principle | Application |
|-----------|------------|
| Decompose hierarchically | Break complex tasks into verifiable subtasks |
| Embed domain knowledge | Put curriculum/domain expertise in templates, not just prompts |
| Script-first | Generate narrative before assets |
| Localization is infrastructure | Embed at every layer, not just translation |
| Human in the loop | Define explicit checkpoints for human review |

### From the Agentic Stack

| Layer | Key Design Question |
|-------|-------------------|
| Orchestration | What is the execution lifecycle and error recovery strategy? |
| Reasoning | Which model is actually needed for each step? |
| Skills | What expertise can be packaged for reuse across agents? |
| Tools/Protocols | Is MCP used to standardize tool integration? |
| Memory | What must be remembered, and for how long? |

### Cost-Quality-Latency Triangle

```
        Quality
           /\
          /  \
         /    \
        /______\
    Cost        Latency
```

**Rule:** Optimizing any one dimension typically increases pressure on the others. Make explicit tradeoffs — do not assume you can optimize all three simultaneously.

---

## COMMON ANTI-PATTERNS TO AVOID

| Anti-Pattern | Description | Better Approach |
|-------------|-------------|-----------------|
| Monolithic prompt | One giant prompt tries to do everything | Hierarchical staged pipeline |
| Model maximalism | Using the most powerful model for every step | Route tasks to minimum capable model |
| Prompt-only localization | Adding "please respond in Vietnamese" at the end | Embed localization in every template and schema |
| Optimism about success | Assuming steps will succeed | Explicit failure handling at every stage |
| Launch and ignore | No observability after deployment | AgentOps from day one |
| Fixed plan execution | Agent never reconsiders its plan | Build reflection into the loop |
| Context dumping | Passing all previous context at every step | Selective, compressed context injection |
| Manual evaluation only | Relying on developers to spot quality issues | Automated trajectory evaluation |

---

*Handout v1.0 | Based on WS-Converged.md | Workshop: ConnectED & the Emerging Agentic AI Stack*
