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

* weak curriculum alignment,  
* inaccurate pedagogical sequencing,  
* inconsistent terminology,  
* lack of cultural localization,  
* vague activity design, and  
* hallucinated educational content.

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

Concept Extraction → Objective Generation → Activity Design → Content Development → Visual Material Generation → Evaluation

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

**Part II — Beyond the Competition: The Rise of the Agentic AI Stack**  
**From Generative AI to Agentic AI**

Traditional generative AI systems operate through a relatively simple interaction pattern:  
**User Prompt → Model Response**  
While powerful, this paradigm is fundamentally reactive and limited to single-turn generation.  
 *Example:* Asking ChatGPT to “write a short story about a detective” produces one response, but the model cannot independently search for crime scene details, update the plot based on new clues, or coordinate with another AI to illustrate a character.  
**Agentic AI** introduces a fundamentally different model of interaction. Instead of merely producing text, the system operates through iterative reasoning and execution loops:  
**Goal → Plan → Act → Observe → Reflect → Iterate → Completion**  
*Example:* A travel planning agent given “book a weekend trip to Chicago under $600” will:

1. **Plan** – break into flights, hotel, attractions.  
2. **Act** – call flight search API, hotel booking tool.  
3. **Observe** – flight prices exceed budget.  
4. **Reflect** – shift dates or consider nearby airports.  
5. **Iterate** – retry with adjusted constraints.  
6. **Complete** – present a final itinerary.

In this framework, the language model becomes only one component within a larger cognitive architecture.  
 The agent can:

* plan tasks,  
* invoke tools,  
* retrieve external information,  
* execute actions,  
* evaluate intermediate results,  
* revise strategies, and  
* coordinate with other agents or systems.

This transition represents one of the most significant shifts in modern AI engineering: from passive generation toward autonomous problem-solving systems.  
**The Modern Agentic Stack**

Modern AI agents are not standalone models. They are complex orchestration systems composed of multiple interconnected layers.  
**1\. Orchestration Layer**  
The orchestration layer — sometimes called the agent harness — manages the overall execution lifecycle.  
 Its responsibilities include:

* planning,  
* task decomposition,  
* tool routing,  
* memory management,  
* error handling,  
* policy enforcement,  
* retry mechanisms,  
* reflection loops, and  
* multi‑agent coordination.

**Frameworks** such as LangChain, Claude Code, AutoGen, CrewAI, and emerging orchestration systems operate within this layer.  
 *Example:* In CrewAI, an “AnalystAgent” and a “WriterAgent” are orchestrated by a manager agent that first routes a data‑gathering task to the analyst, then passes the results to the writer for a summary — including automatic retries if the analyst’s API call fails.  
The orchestration layer effectively transforms raw model intelligence into executable workflows.  
**2\. Reasoning Core**  
At the center of the stack sits the reasoning engine itself:

* large language models (GPT‑4, Claude 3.5),  
* reasoning models (OpenAI o1, DeepSeek‑R1),  
* multimodal models (GPT‑4V, Gemini),  
* smaller domain‑specialized models, or  
* hybrid model ensembles.

These models provide semantic understanding, planning capability, and natural language reasoning.  
 *Example:* A customer support agent might use:

* a **small model** (e.g., 7B parameter Llama) to classify the incoming issue (billing vs. technical).  
* a **large model** (GPT‑4) to draft a refund justification.  
* a **specialized model** (fine‑tuned on internal knowledge base) to retrieve exact policy clauses.

This layered approach improves both efficiency and scalability.  
**3\. Skills: Packaged Expertise**  
A major development in agentic systems is the emergence of **reusable skills**.  
 A skill is a modular package that contains:

* instructions,  
* workflows,  
* scripts,  
* templates,  
* policies,  
* examples, and  
* domain‑specific assets.

Rather than storing all expertise inside a single prompt, agents dynamically load relevant skills when needed.  
 *Examples of skills in action:*

* **Educational lesson planning** – a skill that includes curriculum standards, template for learning objectives, and a script to generate quiz questions.  
* **Financial reporting** – fetches quarterly data from an accounting API, runs variance analysis, and formats an SEC‑compliant MD\&A section.  
* **Code review** – loads company linting rules, security patterns, and a checklist for common bugs.  
* **Legal summarization** – contains citation formats, privilege log templates, and a redaction policy.

This enables:

* modularity,  
* reuse across agents,  
* version control (git for skills),  
* auditability (each skill execution can be logged), and  
* progressive context loading (only the needed skill’s instructions enter the prompt).

Skills effectively function as executable knowledge modules for intelligent systems.  
**4\. Tools and Interoperability Protocols (MCP, A2A, AP2, ACP, UCP, ...)**

Modern agents become significantly more powerful when connected to external tools and real‑world data sources. These tools may include:

* search engines (Google, Bing, Perplexity),  
* databases (PostgreSQL, Pinecone),  
* APIs (Stripe, Salesforce, GitHub),  
* code interpreters (Python REPL, Jupyter),  
* document systems (SharePoint, Notion, Google Drive),  
* browsers (Playwright, Puppeteer),  
* calculators, enterprise software (SAP, ServiceNow), and  
* execution environments (Docker, AWS Lambda).

To connect agents to these tools in a standardized way, several protocols have emerged. These protocols form the connective tissue of the agent ecosystem, enabling interoperability, trust, and complex transactions.

* **MCP (Model Context Protocol)** – Introduced by Anthropic as an open standard for connecting AI assistants with tools and resources. MCP defines how agents discover and invoke **tools** (functions), **resources** (data files, database rows), and **prompt templates**. Developers expose capabilities through MCP‑compatible servers. Often described as "USB‑C for AI."  
   *Example:* An agent using MCP can seamlessly call a get\_weather tool from one server and read a sales\_report.csv resource from another, without custom code per integration.  
* **A2A (Agent‑to‑Agent Protocol)** – A protocol that allows independent agents to delegate subtasks, negotiate goals, and share results. A2A defines message schemas for task requests, status updates, and artifact delivery across different agent frameworks.  
   *Example:* A travel agent built with LangChain sends a “find\_hotels” task to a specialized hotel‑booking agent (running on AutoGen) using A2A messages. The hotel agent replies with structured offers, and the travel agent continues without knowing the other’s internal architecture.  
* **ACP (Agent Communication Protocol)** – A lightweight, WebSocket‑based protocol focused on real‑time agent coordination. ACP supports streaming observations, interrupt signals, and collaborative planning. Often used in robotics or multi‑agent simulations.  
   *Example:* In a warehouse simulation, one robot agent uses ACP to broadcast “I am blocking aisle 3 for 2 seconds” so others can reroute.  
* **Other emerging protocols**:  
  * **AGNTC (Agent Connect)** – A community‑driven spec for agent identity and capability discovery.  
  * **ANP (Agent Network Protocol)** – Designed for decentralized agent marketplaces (e.g., [fetch.ai](https://fetch.ai/)).  
  * **OpenAI’s Function Calling** (proprietary, but de facto tool standard) – often bridged to MCP via adapters.

**Commerce & Payment Protocols**  
A crucial recent development is the emergence of protocols that allow agents to not just use tools, but to transact and execute commercial workflows independently. This represents a major step toward a fully autonomous agent economy.

* **AP2 (Agent Payments Protocol)** – Announced by Google in September 2025, AP2 is an open protocol developed with leading payments and technology companies to securely initiate and transact agent‑led payments across platforms. It can be used as an extension of both the A2A and MCP protocols, creating a unified framework for agents to transact. AP2 addresses critical challenges for agent‑led commerce:  
  * **Authorization**: Proving that a user explicitly authorized an agent to make a specific purchase.  
  * **Authenticity**: Enabling merchants to verify that an agent’s request accurately reflects the user’s true intent.  
  * **Accountability**: Determining responsibility if a fraudulent or incorrect transaction occurs.  
* AP2 builds trust using **Mandates**—tamper-proof, cryptographically-signed digital contracts that serve as verifiable proof of a user's instructions. These mandates come in two forms:  
  * **Intent Mandate**: Captures the user's initial request and rules (e.g., "Find me a green jacket for up to 20% more").  
  * **Cart Mandate**: A secure, unchangeable record of the exact items and price, created upon user approval of a specific cart.  
* *Example of a delegated task:* A user signs an Intent Mandate for "Buy concert tickets the moment they go on sale" with specific rules (price limits, timing). The agent then monitors availability and automatically generates a Cart Mandate and completes the purchase when conditions are met, creating a non-repudiable audit trail.  
   AP2 is designed to be payment-agnostic, supporting credit/debit cards, stablecoins, and real‑time bank transfers. It is supported by a diverse group of over 60 organizations, including Adyen, American Express, Coinbase, Etsy, Mastercard, PayPal, Salesforce, and ServiceNow. In collaboration with Coinbase, Google has also extended AP2 with the **A2A x402 extension**, a production-ready solution for agent‑based crypto payments.  
* **OpenAI Agentic Commerce Protocol (ACP)** – OpenAI’s framework for enabling conversational commerce within ChatGPT. ACP is built for headless checkout, where the interface is the dialogue and the purchase can complete without a traditional website visit. It allows approved merchants to share structured product data so their catalogues can be understood and used in ChatGPT commerce experiences. Key components include:  
  * **Product Feed Specification**: Defines how merchants share structured product data (titles, pricing, inventory, images, availability) with OpenAI using formats like TSV, CSV, XML, or JSON. OpenAI relies on these merchant-provided feeds to ensure accurate pricing, availability, and other key details for product discovery and ranking within ChatGPT.  
  * **Instant Checkout**: A feature that allows users to complete purchases directly within ChatGPT, with the merchant paying a fee on completed purchases.  
  * **Merchant Onboarding**: Currently available to approved partners, with a self-service merchant portal planned for the future.  
* *Example:* A user asks ChatGPT to “find a new winter jacket”. ChatGPT uses ACP to search through merchant product feeds, presents options, and allows the user to complete the purchase via Instant Checkout without leaving the conversational interface.  
* **UCP (Universal Commerce Protocol)** – Developed by Google for ecosystem workflow orchestration across surfaces like Google Search, Shopping, and Gemini. Unlike ACP’s focus on checkout, UCP manages the full commerce workflow: inventory, shipping, identity, returns, loyalty, and fulfillment. It enables deep handoffs to merchant systems while keeping the session coherent, and is optimized for orchestration at scale. UCP is designed to be compatible with AP2 and A2A, allowing agents to perform end-to-end commerce tasks.

These commerce and payment protocols are not mutually exclusive but are often complementary. AP2 focuses on the payment trust layer, ACP enables conversational checkout, and UCP handles full workflow orchestration. Together, they, along with MCP and A2A, provide a comprehensive interoperability stack for the emerging agent economy.  
These protocols create a universal interoperability layer for AI systems. Rather than building custom integrations for every service, developers can expose capabilities through standardized servers. As adoption expands, MCP, A2A, and ACP may become foundational infrastructure for future agent ecosystems.

**5\. Memory Systems**  
Effective agents require memory beyond the immediate context window.  
 Modern agentic systems increasingly combine:

* **Short‑Term Memory**  
   Used for: active reasoning, conversational continuity, temporary planning state, task execution context.  
   *Example:* While planning a 5‑step data analysis, the agent remembers “step 2 (clean data) is complete” without writing to a database.  
* **Long‑Term Memory**  
   Used for: persistent user preferences, project history, retrieved knowledge, historical decisions, organizational context.  
   *Example:* A coding agent remembers that the user prefers pytest over unittest, and that three months ago a particular API wrapper was deprecated – this influences its current code generation.

Memory systems are becoming one of the defining challenges of scalable agent design. Poor retrieval, stale information, or overloaded context can quickly degrade reasoning quality.  
 *Example techniques:* Vector databases (Chroma, Weaviate) for semantic recall, SQLite for structured state, and episodic memory buffers that summarize past failures.  
**Core Agentic Loop**

Most modern agent systems follow some variation of the following loop:  
**PLAN → ACT → OBSERVE → REFLECT**  
For example, an agent tasked with “find and summarize the latest research on quantum error correction”:

1. **PLAN** – search arXiv → download top 3 papers → extract abstract and conclusion → write summary.  
2. **ACT** – call arXiv API with query “quantum error correction 2025”.  
3. **OBSERVE** – API returns 47 papers; the agent observes that step 1 produced more results than expected.  
4. **REFLECT** – “I need to filter by relevance (citation count) before downloading full text.”  
5. **ITERATE** – revised plan: fetch metadata, sort by citations, then download top 3\.  
6. **COMPLETION** – summary delivered with citations.

This iterative architecture allows agents to solve problems that are impossible through single‑pass prompting alone – such as booking flights with changing prices, debugging code by running tests, or negotiating with other agents via A2A.

---

# **Persistent Challenges in Agentic AI**

Despite rapid progress, major challenges remain.

---

## **Reliability**

Agents still fail in unpredictable ways.

Common failure modes include:

* hallucinated tool usage,  
* invalid API calls,  
* infinite reasoning loops,  
* context corruption,  
* planning instability,  
* instruction drift,  
* unsafe execution,  
* over-delegation, and  
* brittle coordination.

Because agent workflows are multi-step and partially nondeterministic, even small intermediate errors can propagate into catastrophic downstream failures.

Improving reliability requires:

* verification layers,  
* execution constraints,  
* robust evaluation,  
* guardrails,  
* fallback strategies,  
* structured traces, and  
* human oversight.

---

## **Evaluation**

Evaluating agents is substantially harder than evaluating standard LLM outputs.

The final answer alone is insufficient. We must also assess:

* reasoning trajectories,  
* planning quality,  
* tool selection,  
* memory usage,  
* safety compliance,  
* cost efficiency,  
* latency,  
* recovery behavior,  
* robustness under failure.

This has led to growing interest in trajectory-based evaluation and agent benchmarking systems.

Modern evaluation increasingly combines:

* automated testing,  
* LLM-as-judge frameworks,  
* human review,  
* execution validation,  
* simulation environments,  
* adversarial testing.

However, standardized evaluation methodologies remain immature.

---

## **Cost and Latency**

Agentic systems are expensive.

A single task may involve:

* multiple reasoning steps,  
* numerous tool calls,  
* retrieval operations,  
* long context windows,  
* repeated reflection loops.

This creates substantial computational cost and latency overhead.

As a result, practical deployment increasingly depends on:

* model routing,  
* caching,  
* context compression,  
* smaller specialized models,  
* parallel execution,  
* efficient orchestration.

Balancing capability with operational efficiency remains a major engineering challenge.

---

## **Observability and AgentOps**

As agents become more complex, observability becomes essential.

Traditional DevOps tooling was not designed for systems whose internal state is partially expressed through natural language reasoning.

This has given rise to a new operational discipline often referred to as **AgentOps**.

AgentOps platforms provide:

* execution tracing,  
* prompt logging,  
* tool-call monitoring,  
* token analytics,  
* replay systems,  
* failure diagnostics,  
* safety auditing,  
* cost monitoring.

These systems transform agents from opaque black boxes into inspectable software systems.

Observability is especially important for:

* debugging failures,  
* improving reliability,  
* governance,  
* compliance,  
* reproducibility,  
* optimization.

As agentic systems move into enterprise and high-stakes environments, AgentOps infrastructure will likely become as important as traditional software observability stacks.

---

# **Conclusion**

ConnectED demonstrates that the future of AI applications lies not in isolated model outputs, but in carefully engineered intelligent systems that combine:

* orchestration,  
* pedagogy,  
* structured workflows,  
* localization,  
* memory,  
* tools,  
* and human collaboration.

The broader evolution toward agentic AI reflects a similar transition across the industry. Large language models are no longer merely text generators; they are becoming reasoning engines embedded within larger computational ecosystems.

However, building reliable agentic systems remains difficult. Success increasingly depends not only on model capability, but also on:

* orchestration quality,  
* evaluation rigor,  
* observability,  
* memory design,  
* tool integration,  
* and domain-specific engineering.

The next generation of AI innovation will likely be defined by how effectively we design these surrounding systems — the infrastructure that transforms raw intelligence into dependable, scalable, real-world capability.

