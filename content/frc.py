"""
content/frc.py
--------------
FRC detail page content — Phase 3.
"""

meta = {
    "folio": "03 / FIRST Robotics Competition",
    "title": "FRC",
    "meta_line": "Ongoing \u00b7 CAD + Manufacturing",
    "tech": "CAD / CNC / Fabrication / Mechanical Assembly",
}

sections = [
    {
        "id": "opening",
        "type": "wide-media",
        "media": "Robot / build / competition photo",
    },
    {
        "id": "what-frc-is",
        "type": "prose",
        "content": [
            "FRC is a high-school robotics competition where teams design, build, and compete with robots over a six-week build season.",
            "I\u2019ve been on the team for a few years now. My work has been mostly on the manufacturing and CAD side.",
        ],
    },
    {
        "id": "the-work",
        "label": "The work",
        "type": "prose",
        "content": [
            "CAD, drivetrain design, component assembly. CNC machines, saws, drills, and most of the other tools in a fabrication shop.",
            "There\u2019s a specific kind of satisfaction that comes from building something physical. You design a mechanism on a screen, and then it exists. It either works or it doesn\u2019t, and you can tell immediately.",
            "That feedback loop is different from software. I didn\u2019t fully appreciate how different until I was doing both.",
        ],
        "media": "Build process / fabrication",
    },
    {
        "id": "worlds",
        "label": "Worlds",
        "type": "prose",
        "content": [
            "Our team qualified for the FIRST World Championship.",
            "That\u2019s a good outcome. Getting there took the whole team.",
        ],
        "media": "Competition photo",
    },
]
