# Privacy Guidelines — Parthiv Patel's Portfolio

This document defines what personal information may and may not appear on the public website. It applies to all content: text, images, metadata, embedded files, and linked resources.

**Parthiv is a minor. These guidelines are non-negotiable.**

---

## Never Publish

The following must NEVER appear on the site, in source code, in commit messages, in metadata, or in any publicly accessible file:

| Category | Detail |
|---|---|
| **Date of birth / exact age** | Do not state birthday, birth year, or exact age. Use "high-school senior" when context requires it. Do not publish a numeric age. |
| **Home address / city of residence** | No street address, city name, or zip code. Do not publish the exact city where Parthiv lives. General regional references ("Southern California," "Los Angeles area") are the maximum precision — see the Location section below. |
| **Phone number** | No personal or family phone numbers. |
| **Personal email** | No private email addresses. Use only the designated public-facing contact email. |
| **Family information** | No names, occupations, or personal details about family members. |
| **Personal schedules** | No school schedules, class times, daily routines, or travel itineraries. |
| **Real-time location** | No current or recent location sharing. |
| **School schedules** | No bell schedules, class rosters, or teacher names. |
| **Sensitive documents** | No report cards, transcripts, financial documents, or legal documents. |
| **College application info** | No application essays, admission decisions, school lists, or application status. |
| **Private writings** | No content from personal journals, memoirs, private recordings, or private messages — unless Parthiv explicitly approves a specific excerpt for publication. |
| **Private account credentials** | No passwords, API keys, tokens, or private account identifiers. |

---

## Publish With Care

These categories may appear but require intentional decisions:

### Location
- **Maximum precision:** "Southern California" or "Los Angeles area."
- Do not name specific neighborhoods, streets, or precise locations.
- Event locations (e.g., competition venues) may be named if they are already public information.

### School
- School name may be included **only where it adds meaningful value** (e.g., FRC team context).
- Do not include school address, internal systems, or administrative details.
- Default to omitting school name unless there is a clear reason to include it.

### Internship / Lab Content
- Content from USC SERC / ISI is limited to **material Parthiv is authorized to disclose publicly.**
- When in doubt, omit. Ask before including technical details, lab photos, internal project names, or unpublished research.
- Publicly presented or published work (e.g., poster sessions, public demos) is generally safe.
- Internal communications, proprietary methods, or other researchers' unpublished work must not be shared.

### Photography
- Photos of Parthiv himself: allowed, at his discretion.
- Photos of other identifiable individuals: **require their consent** or should have faces obscured.
- Photos of private spaces (homes, non-public areas): do not publish.
- Photos of labs, workshops, or events: check disclosure policies first.

### Social Media / Profile Links
- Only link to profiles Parthiv intentionally maintains as public.
- Do not link to personal/private social media accounts.
- Verify each link is intentional before publishing.

---

## Technical Safeguards

### Source Code & Repository
- The repository is public. **No secrets in code, comments, commit messages, or configuration files.**
- Use environment variables or Streamlit secrets management for any sensitive values.
- Review `.gitignore` to ensure private files are excluded.
- Do not hardcode email addresses in source — load from configuration or secrets.

### Metadata & Assets
- Strip EXIF data (especially GPS coordinates) from images before committing.
- Review filenames — avoid filenames that leak personal information.
- Review alt text and captions for unintended disclosure.

### Analytics & Third-Party Services
- If analytics are added, use privacy-respecting options. No tracking pixels or invasive third-party scripts.
- Streamlit Community Cloud's default behavior should be reviewed for any user-data collection.

### Contact Form
- If a contact form is implemented, it should use the public-facing email only.
- Do not expose the form submission endpoint in a way that enables spam or data harvesting.

---

## Review Process

Before publishing or deploying:

1. **Content review:** Check all visible text, image captions, alt text, and metadata against this document.
2. **Source review:** Check code comments, configuration files, and commit history for leaked information.
3. **Image review:** Verify EXIF data is stripped, no private locations visible, no unauthorized individuals identifiable.
4. **Link review:** Verify all external links point to intentionally public profiles/pages.

---

## Updating This Document

If Parthiv's circumstances change (e.g., turning 18, changing what information he is comfortable sharing), this document should be updated before the site content changes.

Any relaxation of these guidelines requires Parthiv's explicit approval.
