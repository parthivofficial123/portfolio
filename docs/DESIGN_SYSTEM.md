# Design System — Parthiv Patel's Portfolio

This document defines the visual language for the portfolio. It is a reference for implementation, not a CSS file — actual tokens will live in the codebase.

---

## Design Philosophy

The visual identity draws from three overlapping traditions:

1. **Editorial publication** — strong type hierarchy, whitespace, asymmetric layouts, deliberate pacing
2. **Engineering notebook** — monospace metadata, diagrams, annotations, structured data, thin rules
3. **Personal archive** — real photography, project artifacts, honest documentation

The result should feel contemporary, technically sophisticated, and distinctly personal — not templated.

---

## What We Are NOT

| Avoid | Why |
|---|---|
| Cyberpunk / neon UI | Looks like every "developer portfolio" template |
| Iron Man HUD | Thematically adjacent to JARVIS but visually cliché |
| SaaS landing page | Wrong audience, wrong tone |
| Space-themed | Aerospace is one interest, not the identity |
| Glassmorphism everywhere | Overused, ages poorly |
| Purple/blue gradient backgrounds | The single most common AI-portfolio cliché |
| Particle effects / cursor followers | Performance cost for zero information |

---

## Typography

### Type Scale

Use a modular scale (roughly 1.25 ratio) anchored to a 16–18 px body size. Exact values will be set in CSS.

### Font Qualities

The typography should not be final yet, but we know what we're looking for:

| Role | Desired qualities |
|---|---|
| **Display / headings** | Editorial personality. Strong at large sizes. Not overly geometric or futuristic. Should feel like a magazine or independent publication, not a startup landing page or SaaS dashboard. Variable-weight families are preferred for flexibility. |
| **Body** | Highly readable at 16–18 px. Comfortable for long-form reading. Can be the same family as headings if it performs well at text sizes, or a complementary workhorse sans-serif. |
| **Mono / metadata** | Clean, legible monospace for dates, tags, technical labels, code snippets. Should feel intentional and well-paired with the display face — not decorative or overly stylized. |

**Avoid:** Inter, system-default sans-serifs, or any typeface whose primary association is with SaaS/startup/developer-template websites. The font choice should not make the site immediately resemble an AI-generated portfolio.

Load fonts from Google Fonts to keep deployment simple. Limit to **two families maximum** (one sans, one mono) to control page weight.

### Candidate Pairings

These are **candidates for evaluation, not final decisions.** The final pairing will be chosen during implementation after testing in the actual Streamlit layout.

| # | Display / Body | Mono | Character | Notes |
|---|---|---|---|---|
| 1 | **Sora** | JetBrains Mono | Geometric but warm, slightly rounded — editorial without being stiff | Good weight range, reads well at display and body sizes |
| 2 | **Outfit** | IBM Plex Mono | Clean, modern, slightly friendly — avoids the generic geometric feel | Variable font, excellent weight flexibility |
| 3 | **General Sans** (via Fontshare) or **DM Sans** (Google Fonts) | DM Mono | Neutral with personality — sits between geometric and humanist | DM Sans/DM Mono are a natural pairing; General Sans has stronger editorial character but requires Fontshare |
| 4 | **Space Grotesk** | Space Mono | Technical and distinctive — slightly unusual letterforms give it identity | The "Space" family is a matched set; has enough character to feel editorial without being distracting |
| 5 | **Instrument Sans** | Source Code Pro | Contemporary editorial feel, slightly condensed at heavier weights | Newer face, less likely to be recognized as a template default |

**Selection criteria for final decision:**
- Does it look editorial at display sizes (32 px+)?
- Is it comfortable to read at body sizes (16–18 px) for multiple paragraphs?
- Does the mono pairing feel cohesive?
- Does it load quickly on Streamlit Community Cloud (≤ 2 font files)?
- Does it avoid immediate association with AI/SaaS/startup templates?

### Type Principles

- Headings should carry real weight — large enough to anchor a section, not just slightly bigger body text.
- Body text: minimum 16 px, comfortable line-height (~1.5–1.6), max line-length ~65–75 characters.
- Use weight and size for hierarchy, not color alone.
- Monospace is for metadata, labels, dates, code — not for entire paragraphs.

---

## Color

### Palette Strategy

A restrained, intentional palette — not a rainbow.

| Token | Purpose | Direction |
|---|---|---|
| `--color-bg` | Page background | Near-white or very light warm neutral (light mode); deep charcoal or warm near-black (dark mode) |
| `--color-surface` | Cards, raised elements | Slight shift from bg — enough to separate, not enough to distract |
| `--color-text` | Primary body text | High contrast against bg, but not pure #000 or #FFF — use a tinted near-black / near-white |
| `--color-text-secondary` | Captions, metadata, labels | Reduced contrast, still legible (minimum 4.5:1 against surface) |
| `--color-accent` | Links, interactive elements, key highlights | A single confident hue — warm amber, muted teal, or earthy terracotta. NOT neon, NOT gradient. |
| `--color-accent-hover` | Hover/focus state for accent | Slightly shifted (darker or lighter) variant of accent |
| `--color-rule` | Thin dividers, borders | Very subtle — low-opacity text color or distinct neutral |
| `--color-code-bg` | Code block backgrounds | Slightly tinted neutral |

### Color Principles

- **One accent color.** It should feel like a signature, not a theme park.
- Avoid pure black (#000) and pure white (#FFF) — they feel harsh. Tinted neutrals are warmer.
- Avoid gradients as backgrounds or text fills. A gradient is acceptable only if it serves a specific, local purpose.
- Dark mode is desirable but optional for v1. If implemented, it should be a true second palette, not just an inverted version.
- All text/background combinations must meet WCAG AA contrast (4.5:1 for body text, 3:1 for large text).

---

## Spacing

Use a base-4 or base-8 spacing scale. Consistency matters more than the exact base.

```
4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128
```

### Spacing Principles

- **Generous whitespace.** Let content breathe. White space is not wasted space — it creates hierarchy and focus.
- Section gaps should be large enough to clearly separate distinct content areas.
- Tighter spacing within related groups (e.g., a heading + subheading + paragraph).
- Don't fill every empty area with decorative elements.

---

## Layout

### Grid & Structure

- Content width: constrain to ~720–900 px for text-heavy sections (readability).
- Allow wider breakouts for images, diagrams, and featured content (~1100–1200 px max).
- Streamlit's column system can approximate asymmetric layouts — use `st.columns` with unequal ratios.

### Layout Principles

- **Asymmetry is welcome.** Not every section needs to be centered. Text-left / image-right (or vice versa) creates visual interest.
- **Vary the rhythm.** Alternate between full-width sections, constrained text, side-by-side layouts, and featured content. Avoid repeating the same layout pattern for every section.
- Not every piece of content needs a card. Use cards only when content genuinely benefits from containment (e.g., a project summary with a clear boundary).
- Thin horizontal rules (1 px, low opacity) can separate sections without heavy visual weight.

---

## Components

### Core Principle: Content Determines the Component

> Do not create a reusable component simply because multiple pieces of content exist. A project listing can be typography + rules + spacing rather than containers. Repeated visual treatment should only become a reusable component when it genuinely improves consistency and maintainability.

Every component must earn its existence. If the same result can be achieved with a heading, a paragraph, and a divider, do not wrap it in a card.

### Vocabulary

These are conceptual building blocks — implementation details will be determined during development. Not all of these may be needed. Start with the minimum and extract components only when repetition justifies it.

| Component | Purpose | Notes |
|---|---|---|
| **Section header** | Title + optional subtitle + optional metadata line | Strong heading, optional monospace date/tag beneath |
| **Project entry** | Summary of a project on the Work index | Title, status tag, one-line description. Prefer editorial typography (heading + rule + description) over a contained card. Only use a card if the layout genuinely requires visual containment. |
| **Status tag** | Small label: "Completed," "Ongoing," "On Hold" | Monospace, small, muted — not a bright badge |
| **Image / figure** | Photo or diagram with caption | Caption in secondary text or monospace. Alt text required. |
| **Metadata line** | Date, category, reading time, status | Monospace, secondary color, small size |
| **Divider** | Thin horizontal rule | 1 px, `--color-rule`, generous vertical margin |
| **Footer** | Contact links, copyright, minimal info | Simple, not a second navigation bar |
| **Navigation** | Top-level nav: Home, Work, About (+ Notebook when launch-ready) | Minimal, clear, not visually heavy. Consider left-aligned rather than centered for editorial feel. |

---

## Project Detail Pages — Flexible Structure

Flagship case studies (JARVIS, USC SERC, FRC) should NOT be forced into an identical page template.

They share typography, navigation, and spacing primitives, but each case study should have its own pacing and structure dictated by the material:

| Project | Likely structure | Why |
|---|---|---|
| **JARVIS** | Chronological evolution / development timeline | The story *is* the iteration: idea → first attempt → technology changes → current state → future. A linear narrative works best. |
| **USC SERC** | Dual narrative: internship context + digital-twin deep dive | Two interleaved stories: the broader lab experience and the self-directed project. Could use a section break or shift in pacing between them. |
| **FRC** | Visual / manufacturing-focused | More images, less narrative. Emphasis on physical artifacts, build process, tools. Could be shorter and more image-driven than the other two. |

Do not build a single `project_detail` template and force all three through it. Shared elements (nav, footer, section headers, typography) provide cohesion; page-level structure should be flexible.

---

## Motion & Animation

### Principles

- **Restrained.** Motion should clarify state changes, not decorate.
- No scroll-triggered animations on every section.
- No elements fading in from below on every scroll.
- Hover transitions: subtle (opacity, underline, color shift), ~150–250 ms, ease-out.
- Page transitions: if feasible in Streamlit, a simple fade. If not, don't force it.
- Respect `prefers-reduced-motion` — disable non-essential animations for users who request it.

### Acceptable Motion

- Link/button hover states
- Navigation state changes
- Image hover (subtle scale or overlay)
- Expandable sections (smooth height transition)

### Not Acceptable

- Parallax scrolling
- Floating/bouncing elements
- Particle systems
- Typewriter text effects
- Every section sliding in from the side

---

## Imagery

- **Use real photography** where available (Parthiv's own photos, project screenshots, diagrams).
- No stock photography.
- No generic illustration packs.
- No AI-generated decorative images used as if they were real photographs.
- Diagrams and technical illustrations are encouraged — they should look intentional and clear, not decorative.
- All images must have descriptive alt text.

---

## Iconography

- Minimal icon usage. Prefer text labels over icon-only buttons.
- If icons are needed, use a single consistent set (e.g., a simple line-icon set or inline SVGs).
- No emoji as primary UI elements (occasional inline emoji in conversational text is fine).
- No icon grids to represent skills or hobbies.

---

## Anti-Patterns Checklist

Before implementation, verify the design does NOT include:

- [ ] Purple/blue gradient backgrounds
- [ ] Gradient text
- [ ] Glowing blobs
- [ ] Generic dark navy background
- [ ] Neon accents
- [ ] Glassmorphism on more than one element
- [ ] Fake terminal windows
- [ ] Skill progress bars or percentages
- [ ] Star ratings
- [ ] Meaningless dashboards or statistics
- [ ] Giant centered marketing hero with stock imagery
- [ ] Typewriter introduction
- [ ] "Hello World" as a greeting
- [ ] Pill-shaped CTA buttons
- [ ] Large rounded corners on every container
- [ ] 3-column card grids repeated throughout
- [ ] Scroll animations on every section
- [ ] Cursor-following effects
- [ ] Generic illustration packs
- [ ] Fake testimonials
