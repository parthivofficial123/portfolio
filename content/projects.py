"""
content/projects.py
-------------------
Flagship project data for the portfolio.

Each dict is the single source of truth for a project's metadata and
home-page copy. Detail page content will be added here or in separate
files during Phase 4.

Fields used on Home:
  slug          str   — URL-safe identifier
  index         str   — editorial number label, e.g. "01"
  title         str   — display title
  meta          str   — one-line metadata shown in mono above the title
  status        str   — "On Hold" | "Completed" | "Ongoing"
  status_slug   str   — CSS class modifier
  body          list  — paragraphs as strings (rendered in order)
  tech          str   — comma-separated tech stack
  cta_label     str   — text for the detail-page link
  media_label   str   — label shown inside the placeholder block
  detail_page   str   — path to the detail view file (None until Phase 4)
"""

projects = [
    {
        "slug": "jarvis",
        "index": "01",
        "title": "JARVIS",
        "meta": "Independent project · 2024— · On hold",
        "status": "On Hold",
        "status_slug": "on-hold",
        "body": [
            "It started as a program that said whatever I typed.",
            "That was supposed to be the project.",
            "Instead, I kept adding things: speech recognition, a local LLM, "
            "computer vision, object detection, web search. I rebuilt parts of it "
            "more than once and changed direction whenever I found a better "
            "way\u2014or realized the previous way wasn\u2019t very good.",
            "Eventually I put it on hold. It\u2019s still probably the project that "
            "taught me the most about figuring things out without already knowing "
            "how to build them.",
        ],
        "tech": "Faster-Whisper / Llama\u00a03 / Ollama / OpenCV / YOLOv8",
        "cta_label": "View JARVIS \u2192",
        "detail_page": "views/work/jarvis.py",
        "media_label": "MEDIA NEEDED\nJARVIS UI / Screenshot",
    },
    {
        "slug": "serc",
        "index": "02",
        "title": "USC SERC",
        "meta": "Engineering internship · Summer 2026",
        "status": "Completed",
        "status_slug": "completed",
        "body": [
            "For about six weeks, I got to bounce between CAD, PCB soldering, "
            "testing, simulation, and whatever else was happening around the lab.",
            "The part I ended up owning started because I heard someone mention "
            "digital twins in a meeting and wanted to know more. I asked if I "
            "could try building one, researched the options, settled on ROS\u00a02 "
            "Jazzy and Gazebo, and built a controllable simulation of Floatbot.",
            "I went in expecting a research lab to be extremely serious and "
            "slightly terrifying.",
            "It wasn\u2019t.",
        ],
        "tech": "ROS\u00a02 Jazzy / Gazebo / Siemens NX / CAD",
        "cta_label": "View SERC \u2192",
        "detail_page": "views/work/serc.py",
        "media_label": "MEDIA NEEDED\nSimulation Screenshot / Diagram",
    },
    {
        "slug": "frc",
        "index": "03",
        "title": "FIRST Robotics",
        "meta": "CAD + Manufacturing · Ongoing",
        "status": "Ongoing",
        "status_slug": "ongoing",
        "body": [
            "FRC gave me the side of engineering that you can\u2019t really get "
            "from sitting behind a laptop.",
            "I\u2019ve worked on CAD, drivetrain and component assembly, CNC "
            "machines, saws, drills, and fabrication while helping build "
            "competition robots.",
            "There is something very satisfying about watching something that "
            "existed on a screen become an actual mechanism in front of you.",
            "Our team eventually made it to the FIRST World Championship.",
        ],
        "tech": "CAD / CNC / Fabrication / Mechanical Assembly",
        "cta_label": "View FRC \u2192",
        "detail_page": "views/work/frc.py",
        "media_label": "MEDIA NEEDED\nRobot / Build / Competition Photo",
    },
]
