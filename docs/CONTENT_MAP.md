# Content Map — Parthiv Patel's Portfolio

This document inventories every page, its sections, the content required for each, and current availability. It is the source of truth for what goes where.

---

## Navigation Structure

### Launch Navigation (v1)

```
HOME
WORK
ABOUT
```

NOTEBOOK is added to primary navigation only when at least one genuine entry exists. See the Notebook section below.

### Full Navigation (when Notebook is ready)

```
HOME
WORK
NOTEBOOK
ABOUT
```

### Page Hierarchy

```
HOME
WORK
  ├─ JARVIS          (flagship case study)
  ├─ USC SERC        (flagship case study)
  ├─ FRC             (flagship case study, if enough media/content)
  └─ (future projects added as material exists)
NOTEBOOK             (deferred — see below)
  └─ (entries)
ABOUT
```

Contact and résumé are accessible from the footer and/or About page — not top-level nav items.

> **Streamlit implementation:** Use `st.navigation` with `st.Page` (Streamlit ≥ 1.36) for multi-page routing. Avoid the legacy `pages/` directory convention. The site's custom navigation should replace Streamlit's default sidebar nav — the sidebar should be hidden unless there is a very strong reason to expose it.

---

## Page: HOME

The homepage serves Depth 1 — a 30-second read that communicates who Parthiv is and where to go next.

| Section | Content | Status |
|---|---|---|
| **Hero / Introduction** | Name, one-liner or short paragraph that captures Parthiv's curiosity-driven approach. NOT a corporate tagline. Conceptual direction: *"I ask 'what if?' a little too often. Sometimes I build the answer."* Final copy TBD. | Copy: needs writing |
| **Selected Work** | 2–3 project highlights (likely JARVIS + USC SERC + FRC). Each: title, one sentence, status tag, link to full page. | Content: available. Layout: needs design. |
| **Current Activities** | Brief list or sentence about what Parthiv is currently working on or preparing for (e.g., FRC season, Caltech EWB prep, SAT prep). Keeps the site feeling alive. | Content: available. Copy: needs writing. |
| **About Preview** | 2–3 sentences + link to full About page. Should hint at breadth of interests beyond engineering. | Copy: needs writing |
| **Footer** | Contact email (public-facing, TBD), links to relevant profiles (GitHub, etc.), copyright. | Email: TBD. Links: TBD. |

---

## Page: WORK

An index page listing projects and experiences, with dedicated detail pages only for flagship work that has enough depth to justify a full page.

### Work Hierarchy

Not every activity needs a dedicated detail page. The number of pages follows the amount of meaningful material, not résumé category count.

| Tier | Examples | Treatment |
|---|---|---|
| **Flagship case study** | JARVIS, USC SERC, FRC (if enough media/content) | Full dedicated page with narrative, media, technical detail |
| **Supporting entry** | Computer Science Club, tutoring, academic activities, community work | Shorter editorial entries on the Work index or integrated into the About page — no dedicated page unless depth grows |
| **Future / placeholder** | Caltech EWB, new projects | Mentioned on homepage under "Current Activities" only — no Work entry until meaningful material exists |

### Work Index

| Content | Notes |
|---|---|
| Page introduction | One or two sentences. Not a grand statement — just orientation. |
| Flagship entries | Editorial-style entry for each: title, status tag, short description, link to detail page. Ordered by significance or recency — not alphabetically. |
| Supporting entries | Shorter entries below flagships: title, brief description. These do NOT link to separate pages — the entry itself is the content. |

### Work → JARVIS

| Section | Content | Status |
|---|---|---|
| **Overview** | What JARVIS is, when it started (late 2024), current status (on hold). The "what if I built my own AI assistant?" origin. | Available |
| **Origin Story** | Started as a type-and-speak TTS script. The gap between the initial idea and the ambition. | Available |
| **Technical Evolution** | The progression of technologies and architecture changes: Faster-Whisper, Llama 3 / Ollama, TTS systems, OpenCV, YOLOv8, webcam vision, web-search integration. This should read as a development history, not a feature list. | Available — needs narrative writing |
| **What Broke / What Changed** | Honest account of architecture changes, things that didn't work, technologies swapped. | Available conceptually — specific anecdotes needed from Parthiv |
| **Current State & Future** | Where the project stands now. Potential next steps: web-search improvements, visual capabilities. Clearly marked as on hold. | Available |
| **Media** | Screenshots, architecture diagrams, code snippets if appropriate. | Needs gathering from Parthiv |

**Narrative emphasis:** The story is the learning process — starting with no knowledge, learning individual systems, connecting them, breaking things, iterating. NOT "Parthiv built an amazing AI assistant."

### Work → USC SERC / ISI

| Section | Content | Status |
|---|---|---|
| **Overview** | What the internship was, where (USC Space Engineering Research Center / ISI), when (Summer 2026, ~6 weeks), general scope. | Available |
| **Lab Work** | PCB soldering, CAD / Siemens NX, pneumatic thrust-test-stand assembly, Starfish project clearance experiments. | Available — needs detail from Parthiv |
| **Digital Twin Project** | Origin: heard about digital twins in a meeting, asked to work on one. Research: ROS/Gazebo combinations, discussed architecture with PhD researcher. Implementation: ROS 2 Jazzy + Gazebo Ignition, Floatbot simulation. | Available |
| **Self-Direction** | Emphasize that the digital-twin project was largely self-initiated and self-directed. | Available |
| **Collaboration & Environment** | Starfish involved frequent communication and iteration. The research environment was collaborative, not intimidating. Weekly tag-ups, significant independence. | Available |
| **What Changed** | Parthiv's perception of research shifted from expecting something extremely formal to discovering a collaborative engineering environment. | Available |
| **Media** | Screenshots of simulation, photos (if allowed — see PRIVACY.md), diagrams. | Needs gathering. Must check disclosure permissions. |

**Disclosure note:** Content is limited to material Parthiv is authorized to share publicly. See PRIVACY.md.

### Work → FIRST Robotics Competition

| Section | Content | Status |
|---|---|---|
| **Overview** | FRC, ongoing, team qualified for FIRST World Championship. | Available |
| **Contributions** | Manufacturing, CAD, drivetrain/component assembly, CNC machines, saws, drills, fabrication tools. | Available |
| **Why It Matters** | Gave Parthiv hands-on exposure to physical engineering — not everything is software on a screen. | Available |
| **Media** | Robot photos, build photos, competition photos. | Needs gathering from Parthiv |

### Supporting Entries (on the Work index, not separate pages)

These appear as shorter editorial entries directly on the Work index page. They do not have dedicated detail pages unless the available material grows significantly.

**Computer Science Club**
- Founding board member. School lacked a dedicated CS club.
- Organized two hackathons, beginner-oriented CS activities/lessons.
- Additional technical clubs later emerged at the school.
- Status: available. Photos: needs gathering.

**Other supporting material** (tutoring, academic activities, community work) may appear here or be integrated into the About page — placement depends on what reads most naturally. See the About page section for detail.

### Future / Caltech EWB

No Work entry until meaningful material (project progress, results, documentation) exists. Currently in preparation — mentioned on the homepage under "Current Activities" only.

---

## Page: NOTEBOOK

> **Launch rule:** The Notebook section is **hidden from primary navigation** until at least one genuine entry exists. Do not launch an empty Notebook. Do not populate it with fake or sample content to fill space.

When ready, it is a collection of technical and exploratory writing. Not a polished blog — more like published pages from a working notebook.

### Launch Options

| Option | When to use |
|---|---|
| **A. Defer entirely** | Notebook stays hidden from nav. Add it when Parthiv writes a real entry. |
| **B. Launch with one real entry** | Parthiv writes at least one genuine notebook entry before launch (e.g., ROS 2 / Gazebo learnings from SERC, or a "what if?" question he's explored). The section goes live with that entry. |

Option A is the default. Option B requires Parthiv to write the entry — we do not write it for him.

### Notebook Index (when active)

| Content | Notes |
|---|---|
| Entry list | Title, date, optional tags, one-line summary. Reverse chronological or loosely categorized. |
| Introduction | Very brief — what this section is. "Things I'm reading, learning, or thinking about." |

### Possible Future Topics

These are ideas for entries — none have been written yet.

| Topic | Category | Notes |
|---|---|---|
| AI ethics | AI | Parthiv's actual thoughts, not a textbook summary |
| Neuromorphic computing | Engineering / AI | A "what is this and why is it interesting?" exploration |
| Computer vision concepts | AI / Engineering | Could tie into JARVIS or SERC work |
| Quantum computing | Physics / CS | Curiosity-driven — what is he actually trying to understand? |
| ROS 2 / Gazebo learnings | Robotics | Could be technical notes from the SERC project |
| Engineering concepts | Engineering | Broad — narrow based on what Parthiv actually wants to write about |
| "What if?" questions | General | The questions that start projects or rabbit holes |

**Content status:** All entries need to be written by Parthiv. This section will grow over time.

---

## Page: ABOUT

Communicates Parthiv as a person. NOT a résumé.

| Section | Content | Status |
|---|---|---|
| **Personal Introduction** | Who Parthiv is beyond project titles. Interests, what drives him, how he thinks. Written in his voice. | Needs writing |
| **Interests & Hobbies** | Engineering, AI, photography, filmmaking, backpacking/hiking, fitness, games, storytelling/worldbuilding, music, learning random things. Presented naturally — not as an icon grid or bulleted skills list. | Available — needs narrative writing |
| **Community & Leadership** | Boy Scouts / Troop 378 (Patrol Leader, mentoring, EDGE method, fundraising — $43k+ popcorn campaign / top-selling unit in GLAC, Top Sellers celebration, 5-day ~20-mile Sierra backpacking trip with ~45 lb pack). BAPS volunteering (food service, events, MC'd youth assemblies, performed in Janmashtami program, Walkathons). Tutoring (private word-of-mouth tutoring, peer tutoring, AP Calc help, learning how differently people need concepts explained). Present as ongoing parts of his life, not performative service hours. | Available — needs narrative writing |
| **Academic Recognition** | AP Scholar, Principal's Honor Roll, Science Olympiad, AMC 10/12, dual enrollment (El Camino College — CSCI 8 data science, HIST 102). Mentioned without inflation — these are real but should not each be a separate section. | Available |
| **Creative Side** | Game concept design / game bibles, worldbuilding. This is part of who Parthiv is — not a footnote. | Available — needs writing |
| **Contact** | Public-facing email (TBD), relevant profile links. | TBD |
| **Résumé** | Downloadable PDF link or equivalent. | Needs creation |

---

## Content Dependencies & Open Items

| Item | Owner | Status |
|---|---|---|
| Public-facing contact email | Parthiv | Not yet set up |
| JARVIS screenshots / diagrams | Parthiv | Needs gathering |
| USC SERC media (check disclosure) | Parthiv | Needs gathering + permission check |
| FRC photos | Parthiv | Needs gathering |
| CS Club photos | Parthiv | Needs gathering |
| Personal photography for About | Parthiv | Needs gathering |
| Profile links (GitHub, etc.) | Parthiv | Needs confirmation |
| Résumé PDF | Parthiv | Needs creation |
| All page copy | Collaborative | Needs writing during implementation |
| Notebook entries | Parthiv | Needs writing — future, ongoing |
| Caltech EWB content | Parthiv | Future — when material exists |
