# ConnectED & Emerging Agentic AI Stack — Presentation Hub

Welcome to the **Master Workshop Presentation Hub** workspace. This repository contains the source files, content scripts, and compilation tools for an interactive, web-based presentation hub focusing on modern AI adaptation, structured education planning platforms, and the emerging agentic AI stack.

---

## 📖 Table of Contents
1. [Overview / Tổng Quan](#overview--tổng-quan)
2. [Workspace Architecture / Cấu Trúc Thư Mục](#workspace-architecture--cấu-trúc-thư-mục)
3. [Key Concepts / Khái Niệm Cốt Lõi](#key-concepts--khái-niệm-cốt-lõi)
   - [Part I: ConnectED](#part-i-connected)
   - [Part II: The Emerging Agentic AI Stack](#part-ii-the-emerging-agentic-ai-stack)
4. [Compilation & Usage / Hướng Dẫn Biên Dịch & Sử Dụng](#compilation--usage--hướng-dẫn-biên-dịch--sử-dụng)

---

## 🌟 Overview / Tổng Quan

This workspace is designed to build and host an interactive, single-page presentation interface that showcases two main segments:
1. **ConnectED**: A deeply localized, AI-native lesson planning platform designed for Vietnamese K-12 education.
2. **The Emerging Agentic AI Stack**: A technical decomposition of modern agent architectures, execution loops, orchestration frameworks, MCP protocols, and deployment checklists.

*Dự án này là trung tâm tài liệu và giao diện trình chiếu tương tác cho Workshop Master về nền tảng ConnectED và Hệ sinh thái Tác nhân AI mới nổi.*

---

## 📂 Workspace Architecture / Cấu Trúc Thư Mục

The repository is organized as follows:

```text
.
├── build_ui.py              # Python script to compile template + markdown into index.html
├── template.html            # Main HTML/CSS/JS frontend shell for the presentation hub
├── index.html               # Compiled production-ready presentation website (auto-generated)
├── presentation_doc/        # Vietnamese workshop presentation source documents
│   ├── 01_connected_platform/    # Part I: ConnectED Platform materials
│   ├── 02_agentic_stack/         # Part II: Emerging Agentic Stack concepts
│   ├── 03_challenges_ops/        # Part III: AgentOps & production challenges
│   ├── 04_deployment_handouts/   # Part IV: Handout checklists
│   └── WS-Converged.md           # Unified master Vietnamese document
└── ref_doc/                 # English reference materials (identical structure)
    ├── 01_connected_platform/
    ├── 02_agentic_stack/
    ├── 03_challenges_ops/
    ├── 04_deployment_handouts/
    └── WS-Converged.md           # Unified master English document
```

### File Breakdown:
- **`presentation_doc/` & `ref_doc/`**: Contain Markdown files (`reference.md`, `detailed_notes.md`, `presentation_script.md`, and `handout_checklists.md`) representing slide content, transcripts, and speaker notes.
- **`template.html`**: A highly interactive UI that supports dark mode, slide-by-slide navigation, search, and rendering markdown files dynamically.
- **`build_ui.py`**: Reads files under `presentation_doc/`, parses them into a JS global object, and embeds them into `template.html` in place of the `/* CONTENT_PLACEHOLDER */` comment.

---

## 💡 Key Concepts / Khái Niệm Cốt Lõi

### Part I: ConnectED
ConnectED solves the 3–4 hour lesson preparation challenge for Vietnamese K-12 teachers by replacing generic monolithic prompts with a structured pedagogy-first pipeline:
- **Pedagogical Backbone**: Built on the **ADDIE** (Analyze, Design, Develop, Implement, Evaluate) model.
- **Script-First Workflow**: Narratives are generated and verified before assets/visuals are produced.
- **Hierarchical Agent Pipeline**: Splits monolithic generation into specialized micro-steps (Concept Extraction, Objective Gen, Activity Design, Content Dev, Visuals).
- **Localization**: Local curriculums, cultural context, and terminology are treated as core infrastructure, not translation wrappers.

### Part II: The Emerging Agentic AI Stack
From reactive generative prompts to agentic reasoning-execution loops:
1. **Orchestration Layer**: Manages execution state, retries, and plans (e.g., CrewAI, AutoGen).
2. **Reasoning Core**: Leverages frontier models (GPT-4o, Claude Sonnet) or reasoning-specific models (o1, DeepSeek-R1) and routes tasks to optimize costs.
3. **Skills**: Modular, versioned business logic prompts loaded dynamically.
4. **Tools & Protocols**: Interfaces like MCP (Model Context Protocol) and Agent Payments Protocol (AP2) that act as the standard connectors.
5. **Memory Systems**: Short-term context buffers coupled with long-term semantic retrieval.

---

## 🛠️ Compilation & Usage / Hướng Dẫn Biên Dịch & Sử Dụng

### How to Compile the UI / Cách biên dịch giao diện:
If you modify any content inside `presentation_doc/` or the layout inside `template.html`, compile the final `index.html` by running:

```bash
python3 build_ui.py
```

Upon execution, it will read all categories from `presentation_doc/`, package them into a JSON representation, insert it into `template.html`, and write the output to `index.html`.

### How to Run and View / Cách xem slide tương tác:
Since `index.html` compiles into a standalone static web application, you can view it directly by:
1. Double-clicking `index.html` to open it in your browser, or
2. Running a local HTTP server inside the root directory:

```bash
# Python 3
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your web browser.
