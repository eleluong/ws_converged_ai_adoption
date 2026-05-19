# Workshop Presentation Script
## ConnectED & the Emerging Agentic AI Stack

> **Format:** 2-part workshop | ~90 minutes total  
> **Audience:** Developers, product managers, researchers, educators  
> **Style:** Conversational + technical deep-dives with live examples  

---

## PRE-TALK CHECKLIST
- [ ] Slides loaded and screen mirrored
- [ ] Demo environment live (ConnectED UI / agent trace viewer)
- [ ] Timer visible to presenter
- [ ] Audience poll tool ready (Mentimeter / Slido)

---

## OPENING — Hook the Audience (3 min)

### Slide 1: Title Slide
**Visual:** Full-bleed image of a Vietnamese classroom, overlay with title text

**Script:**
> "How long do you think it takes a teacher to prepare a single lesson? Not a perfect one — just a decent one."
> *(pause for audience responses)*
> "Three to four hours. Every single lesson. Multiply that by 30 lessons a semester. That's the hidden workload nobody talks about."
> "Today we'll look at what happens when you take that burden seriously — and use AI to actually solve it. Then we'll explore the architecture making all of this possible."

**Transition:** "Let's start with the platform."

---

## PART I — ConnectED (35 min)

### Slide 2: What is ConnectED?
**Visual:** Platform logo + 3-icon row: Lesson Plans | Animations | Virtual Labs

**Key talking points:**
- AI-powered lesson planning platform for Vietnamese K-12
- Generates curriculum-aligned lessons, animations, virtual labs
- Preserves pedagogical quality + local standards
- Goal: reduce lesson prep from hours to minutes

**Script:**
> "ConnectED is not just a generate-text button. It's a structured intelligent system that understands how lessons are actually built and mirrors that process. Three core outputs: lesson plans, teaching animations, and virtual laboratory experiences. All aligned to Vietnam's national curriculum."

---

### Slide 3: The Problem — Teacher Reality
**Visual:** Timeline graphic showing 3-4 hour lesson prep breakdown

| Task | Typical Time |
|------|-------------|
| Define learning objectives | ~30 min |
| Extract concepts from textbooks | ~45 min |
| Design classroom activities | ~40 min |
| Create visual materials | ~45 min |
| Prepare assessments | ~30 min |
| Adapt for student needs | ~30 min |
| Total | ~3-4 hrs |

**Script:**
> "When we handed this problem to generic LLMs, they failed. Generic prompts default to Western curricula, use unfamiliar terminology, and produce lessons that feel foreign."
> "That observation became our north star: AI for education must be deeply localized and pedagogically grounded. Not just translated — re-rooted."

---

### Slide 4: Why Generic LLMs Fall Short
**Visual:** Side-by-side comparison — Generic AI output vs. ConnectED output

**6 failure modes:**
1. Weak curriculum alignment
2. Inaccurate pedagogical sequencing
3. Inconsistent terminology
4. Lack of cultural localization
5. Vague activity design
6. Hallucinated educational content

**Script:**
> "The models weren't broken — they were just uninformed about the local context. That's a design problem, not a model problem."

---

### Slide 5: ADDIE — The Instructional Design Backbone
**Visual:** Circular ADDIE diagram

```
[Analyze] -> [Design] -> [Develop] -> [Implement] -> [Evaluate]
    ^                                                     |
    +-------------------- Feedback Loop ------------------+
```

**Script:**
> "The key architectural decision: don't generate a lesson in one shot. Instead, embed the proven ADDIE instructional design model. ConnectED mirrors this structure — each phase becomes a stage in the AI pipeline."

---

### Slide 6: ADDIE — Phase Deep Dive

**Analyze:** Ingests textbooks and curriculum docs, extracts core concepts, learning outcomes, prerequisites, competency targets

**Design:** Generates lesson structures, activities, timing, assessment strategies; focus on pedagogical coherence

**Develop:** Creates slides, animation scripts, virtual lab instructions, quizzes
- Key innovation: Script-First Workflow — narrative before visuals

**Implement and Evaluate:** Teacher review, refinement, adaptation — human-in-the-loop by design

**Script on Develop:**
> "One subtle but important choice: we generate the instructional script before visual assets. Counterintuitive — but generating the narrative first dramatically improves consistency and accuracy of downstream media."

---

### Slide 7: Hierarchical Agent Pipeline
**Visual:** Horizontal flow diagram

```
Concept     -> Objective  -> Activity   -> Content    -> Visual     -> Evaluation
Extraction    Generation   Design       Development   Materials    Review
[Stage 1]     [Stage 2]   [Stage 3]    [Stage 4]    [Stage 5]   [Stage 6]
```

**Why this matters:**
- Reduced prompt complexity per stage
- Easier verification of intermediate outputs
- Modular debugging
- Lower hallucination rates
- Stronger pedagogical consistency

**Script:**
> "This is a preview of a broader pattern we'll explore in Part II: hierarchical agent systems."

---

### Slide 8: Virtual Labs and Interactive Learning
**Visual:** Screenshots of virtual lab simulations

**Coverage:** Physics simulations, chemistry demonstrations, biology explorations, interactive diagrams

**Script:**
> "Virtual labs are especially valuable in Vietnam where many schools — particularly rural — lack physical equipment. ConnectED generates lab experiences embedded directly into lesson objectives."

---

### Slide 9: Localization as Core Infrastructure
**Visual:** Layered architecture diagram showing localization at every level

**Where localization is embedded:**
- Prompts and system instructions
- Instructional templates
- Terminology and vocabulary
- Assessment structures
- Example scenarios and cultural references
- Curriculum sequence mappings

**Script:**
> "Localization isn't a post-processing step. It needs to be infrastructure — embedded at every layer."

---

### Slide 10: Impact and Results
**Visual:** Big number callout — 15-20 minutes vs 3-4 hours

**Key outcomes:**
- Lesson prep time: 3-4 hours to 15-20 minutes
- Maintained high instructional quality
- Teacher adoption and positive feedback

**4 principles validated:**
1. Pedagogy embedded into architecture
2. Hierarchical workflow decomposition
3. Teachers remain in the loop
4. Localization as foundational infrastructure

**Script:**
> "ConnectED is a proof-of-concept for something much larger — which brings us to Part II."
