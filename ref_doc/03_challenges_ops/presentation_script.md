## PART III — Persistent Challenges (10 min)

### Slide 19: The Hard Problems

**Reliability:**
Failures: hallucinated tool calls, infinite loops, instruction drift, brittle coordination
Solutions: verification layers, guardrails, structured traces, human oversight

**Evaluation:**
Must assess: reasoning trajectory, planning quality, tool selection, safety compliance, cost efficiency
Approaches: LLM-as-judge, trajectory-based testing, simulation environments

**Cost and Latency:**
One task may: span multiple reasoning steps, many tool calls, long context windows, repeated reflections
Mitigations: model routing, caching, context compression, parallel execution

**Observability and AgentOps:**
Provides: execution tracing, prompt logging, token analytics, failure diagnostics, safety auditing
Critical for: governance, compliance, reproducibility, optimization

---

## CLOSING (5 min)

### Slide 20: Key Takeaways

1. Decompose problems hierarchically — single-shot prompting does not scale
2. Localization is infrastructure — not an afterthought
3. Keep humans in the loop — especially in high-stakes domains
4. Design the system, not just the prompt — models are one layer
5. Invest in observability — you cannot improve what you cannot inspect

---

### Slide 21: Q&A Discussion Prompts
- What domain in your work could benefit from a hierarchical agent pipeline?
- Where in your current AI workflows do you have the least visibility?
- What would a "skill" look like for your organization's core knowledge?

---

*Script v1.0 | Based on WS-Converged.md | Approx 90 min workshop*
