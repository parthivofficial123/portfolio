"""
content/serc.py
---------------
USC SERC detail page content — Phase 3.

Privacy note: No other researchers named. No internal methods described in
detail. No unpublished research described. Media placeholders note that
disclosure review is required before adding real media.
"""

meta = {
    "folio": "02 / Engineering Internship",
    "title": "USC SERC / ISI",
    "meta_line": "Summer 2026 \u00b7 ~6 weeks \u00b7 Completed",
    "tech": "ROS\u00a02 Jazzy / Gazebo Ignition / Siemens NX / CAD",
}

sections = [
    {
        "id": "opening",
        "type": "prose",
        "content": [
            "For about six weeks in the summer of 2026, I worked at the USC Space Engineering Research Center.",
            "I went in not knowing exactly what to expect. I came out with a different picture of what a research environment actually looks like.",
        ],
    },
    {
        "id": "the-lab",
        "label": "The lab work",
        "type": "prose",
        "content": [
            "Day to day, I was doing a mix of things: PCB soldering, CAD work in Siemens NX, assembly and testing on a pneumatic thrust stand, and clearance experiments on the Starfish project.",
            "It wasn\u2019t one focused track. I moved between things depending on what was needed. That turned out to be a good way to learn fast.",
        ],
        "media": "Lab work \u2014 disclosure review required before adding real media",
    },
    {
        "id": "digital-twin",
        "label": "The digital twin",
        "type": "prose",
        "content": [
            "Partway through, I heard someone mention digital twins in a meeting. I didn\u2019t fully know what that meant, so I looked it up.",
            "I asked if I could try building one. The answer was yes.",
            "I spent time researching the options \u2014 different ROS and Gazebo combinations, how digital twins are typically architected, what would actually make sense for a spacecraft simulation. I talked through the approach with a researcher on the team.",
            "I ended up using ROS\u00a02 Jazzy and Gazebo Ignition. The result was a controllable simulation of Floatbot, one of the lab\u2019s spacecraft platforms.",
        ],
        "media": "Simulation screenshot or diagram \u2014 disclosure review required before adding real media",
    },
    {
        "id": "what-changed",
        "label": "What this changed",
        "type": "prose",
        "content": [
            "I expected a research lab to be extremely formal and a little intimidating. It wasn\u2019t.",
            "People were collaborative. There was real independence, but also regular check-ins and people who were willing to talk through problems. The digital twin project was largely self-directed, and that was fine \u2014 nobody needed to hand me a step-by-step plan.",
            "That\u2019s probably the part that stuck most. Research felt a lot more like building things with smart people than sitting alone in a serious room.",
        ],
    },
]
