# Project Brief — Parthiv Patel's Portfolio

## What This Is

A personal portfolio website for Parthiv Patel, built as a Streamlit application and deployed on Streamlit Community Cloud.

Parthiv is a high-school senior whose interests sit at the intersection of software, AI, and physical engineering — robotics, computer vision, mechanical systems, intelligent machines, and the questions that connect them.

He is still exploring his exact career direction. The site should reflect genuine curiosity and range, not a neatly packaged specialty.

---

## Conceptual Direction

> "I ask 'what if?' a little too often. Sometimes I build the answer."

This captures Parthiv's pattern: a question leads to research, which leads to a prototype, which leads to something breaking, which leads to learning. The portfolio should let that process be visible rather than only showing polished outcomes.

---

## Audience

| Visitor | What they need |
|---|---|
| College admissions reader | Quick sense of who Parthiv is, what he's done, that he's genuine — in ≤ 60 seconds |
| Engineer / researcher | Technical depth, architecture decisions, failures, iteration history |
| Peer or friend | Something that feels like *Parthiv*, not a corporate brochure |
| Casual visitor | An interesting, navigable site that doesn't waste their time |

---

## Two-Depth Model

The site must work at two levels of engagement:

### Depth 1 — ~30 seconds
- Who Parthiv is
- What kinds of problems interest him
- What he has actually built or worked on
- That he has both technical and creative sides
- Where to go deeper

### Depth 2 — 5–15+ minutes
- Project development histories with failures and iterations
- Architecture notes and diagrams
- Screenshots and photographs
- Technical explanations
- Research rabbit holes
- Unfinished work acknowledged honestly

---

## Voice & Tone

The site should sound like a thoughtful, technically capable high-school senior writing in his own voice.

**Characteristics:**
- Casual but considered
- Dry humor, used sparingly
- Short sentences mixed with longer ones
- Self-aware — can admit confusion, mistakes, or unfinished work
- Specific rather than impressive

**Never use:**
- "Passionate innovator," "driven student," "cutting-edge," "revolutionary"
- "Leveraging technology," "crafting digital experiences," "building tomorrow"
- "At the intersection of innovation and…"
- "AI enthusiast," "technology enthusiast"
- Corporate résumé phrasing of any kind

**Acceptable to say:**
- Something broke
- Something was confusing
- A project is unfinished or on hold
- Parthiv didn't know how to do something
- An idea changed direction
- The first version was bad

---

## Information Architecture

Three primary navigation items at launch. Contact and résumé are accessible but not top-level sections.

```
HOME
WORK
ABOUT
```

NOTEBOOK is added to navigation only when at least one genuine entry exists. See CONTENT_MAP.md for details.

### Home
- Hero / introduction
- Selected work (2–3 highlights)
- Current activities
- Short About preview
- Contact / footer

### Work
- JARVIS (independent AI assistant — on hold)
- USC SERC / ISI (digital-twin project, lab work — completed, Summer 2026)
- FIRST Robotics Competition (ongoing, Worlds qualifier)
- Computer Science Club (founding board member, hackathons)
- Caltech EWB (when material exists)
- Future experiments / projects

### Notebook
A place for technical rabbit holes, research notes, things currently being learned, and broader thoughts. Not a blog in the influencer sense — more like published pages from a working notebook.

Possible early topics: AI ethics, neuromorphic computing, robotics concepts, computer vision, quantum computing, engineering questions.

### About
Communicates Parthiv as a person — interests, community, leadership, recognition — without becoming a résumé dump.

Interests: engineering, AI, photography, filmmaking, backpacking/hiking, fitness, games, storytelling/worldbuilding, music.

Academic recognition (AP Scholar, Principal's Honor Roll, Science Olympiad, AMC 10/12, dual enrollment), Scouting, BAPS community volunteering, tutoring, and leadership can be woven in naturally.

---

## Flagship Projects — Story Notes

### JARVIS — Independent AI Assistant
- Status: **On hold** (started late 2024)
- Began as a type-and-speak text-to-speech script
- Evolved through Faster-Whisper, Llama 3 / Ollama, OpenCV, YOLOv8, webcam vision, web-search integration
- Changed architectures multiple times
- **The story is the learning process**, not the finished product
- Future: improved web search, visual capabilities beyond screen/webcam

### USC SERC / ISI — Summer 2026
- Status: **Completed** (~6 weeks)
- PCB soldering, CAD (Siemens NX), pneumatic thrust-test-stand work, Starfish clearance experiments
- Main independent project: digital-twin simulation using ROS 2 Jazzy + Gazebo Ignition
- Self-directed — Parthiv heard about digital twins, asked to work on one, researched the architecture, built a controllable Floatbot simulation
- Changed his perception of research environments (expected formal/intimidating, found collaborative)

### FIRST Robotics Competition
- Status: **Ongoing**
- Manufacturing, CAD, drivetrain/component assembly, CNC, saws, drills, fabrication
- Team qualified for FIRST World Championship
- Gave Parthiv hands-on exposure to physical engineering

---

## Technical Constraints

| Constraint | Detail |
|---|---|
| Framework | Streamlit (Python) |
| Hosting | Streamlit Community Cloud |
| Navigation | `st.navigation` + `st.Page` (Streamlit ≥ 1.36). Hide the default sidebar. |
| Visual target | Should NOT look like a default Streamlit dashboard |
| Custom styling | Custom CSS, Streamlit layout primitives, careful HTML where needed |
| Dependencies | Minimal — justify any addition. Do not add PyYAML or similar unless strictly necessary. |
| Content storage | Python dictionaries in `.py` files for v1. See Content Model section below. |
| Performance | Fast loads, no unnecessary weight |
| Maintainability | Understandable by a student |
| Responsive | Desktop, laptop, tablet, mobile |
| Accessibility | Readable contrast, keyboard usability, semantic structure, alt text, motion restraint, readable font sizes |
| Privacy | See PRIVACY.md — this is a public site belonging to a minor |

---

## Content Model (v1)

For the first version, project data and page content will be stored as **Python dictionaries in `.py` files.**

### Why Python dicts over alternatives

| Option | Verdict | Reasoning |
|---|---|---|
| **Python dicts / dataclasses** | **Chosen for v1** | Zero dependencies. Editable by anyone who can read Python. Type hints available if desired. IDE support works out of the box. No parsing layer. |
| Markdown files | Deferred | Useful for long-form content (Notebook entries) in the future, but adds complexity for structured project data. Streamlit can render Markdown inline — we don't need a Markdown-to-HTML pipeline. |
| YAML files + PyYAML | Rejected for v1 | Adds a dependency for minimal benefit. YAML syntax errors are harder to debug. Python dicts do the same job without a parser. |
| Hybrid (Python dicts + Markdown) | **Future consideration** | If Notebook entries become substantial, storing them as `.md` files and reading them with `Path.read_text()` makes sense. No additional dependency needed — Python's built-in file I/O is sufficient. |

### Structure

```python
# content/projects.py
projects = [
    {
        "slug": "jarvis",
        "title": "JARVIS",
        "status": "On Hold",
        "summary": "...",
        "tier": "flagship",
        # ... additional fields as needed
    },
    # ...
]
```

Long-form copy (paragraphs, narrative sections) can be stored as multi-line strings within these dicts, or in separate `.py` files organized by page if the content becomes large.

---

## Implementation Phases

These phases define the build order. Do not begin a later phase until the prior phase is functional.

| Phase | Scope | Notes |
|---|---|---|
| **1. Application shell** | `st.navigation` / `st.Page` setup, global CSS injection, typography, color tokens, hidden sidebar, basic responsive behavior | The skeleton — no content yet, but the site loads, navigates, and looks intentional |
| **2. Homepage** | Hero, selected work, current activities, About preview, footer — using real copy, placeholder media if necessary | First real content. Copy should be in Parthiv's voice. |
| **3. Real assets / media** | Gather and integrate Parthiv's photos, screenshots, diagrams. Strip EXIF. Write alt text. | Dependent on Parthiv providing assets. |
| **4. Flagship case studies** | JARVIS, USC SERC, FRC detail pages — each with its own structure, not a shared template | The depth layer. May be built incrementally. |
| **5. About page** | Personal intro, interests, community, recognition, creative side, contact | Should feel like a person, not a résumé. |
| **6. Notebook** | Add to navigation and build the section — only when at least one genuine entry exists | Deferred until Parthiv writes real content. |
| **7. Polish** | Responsive testing, accessibility audit, keyboard navigation, `prefers-reduced-motion`, contrast checks, font loading optimization | Quality pass across everything built so far. |
| **8. Deployment prep** | SEO metadata, favicon, Open Graph tags, final Streamlit Community Cloud config, README updates | Ship it. |

---

## What This Document Does NOT Cover

- Exact copy / final text → will be written during implementation
- Visual design tokens → see DESIGN_SYSTEM.md
- Content inventory and page structure → see CONTENT_MAP.md
- Privacy rules → see PRIVACY.md
