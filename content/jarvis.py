"""
content/jarvis.py
-----------------
JARVIS detail page content — Phase 3.
"""

meta = {
    "folio": "01 / Independent Project",
    "title": "JARVIS",
    "meta_line": "2024\u2014 \u00b7 On hold",
    "tech": "Faster-Whisper / Llama\u00a03 / Ollama / OpenCV / YOLOv8",
}

sections = [
    {
        "id": "opening",
        "type": "prose",
        "content": [
            "JARVIS is on hold. It\u2019s been on hold for a while, and I\u2019m not sure when I\u2019ll pick it back up.",
            "It started in late 2024 as a program that said whatever I typed out loud. That was the whole thing. Then I kept going.",
        ],
    },
    {
        "id": "how-it-started",
        "label": "How it started",
        "type": "prose",
        "content": [
            "The original idea was simple: text in, speech out. A glorified text-to-speech wrapper.",
            "I got that working, and then immediately started wondering what else I could connect to it. That question is basically the entire history of this project.",
        ],
        "media": "JARVIS / Early version screenshot or architecture sketch",
    },
    {
        "id": "what-got-added",
        "label": "What got added",
        "type": "prose",
        "content": [
            "Speech recognition came first \u2014 Faster-Whisper, because it ran locally and was fast enough to feel responsive.",
            "Then a local language model. I used Llama\u00a03 through Ollama because I wanted it to run on my own machine. Using an API felt like cheating, and I also didn\u2019t want to pay for tokens while I was figuring things out.",
            "Computer vision came later. First OpenCV for basic processing, then YOLOv8 for object detection. I hooked up a webcam so the system could see what was in front of it.",
            "At some point I added web search so it could pull in information it didn\u2019t have. Each of these additions worked, more or less. Getting them to all work together cleanly was a different problem.",
        ],
        "media": "Architecture diagram / component overview",
    },
    {
        "id": "what-changed",
        "label": "What changed along the way",
        "type": "prose",
        "content": [
            "I rebuilt parts of the architecture more than once. The first version of the voice pipeline wasn\u2019t structured well and got messy fast. I pulled it apart and redid it.",
            "Some things I tried didn\u2019t work the way I expected. Some worked fine but turned out to be the wrong approach. A few things I built I later removed entirely.",
            "The project changed direction several times. That\u2019s probably the most accurate way to describe it.",
        ],
        "media": "Current state screenshot",
    },
    {
        "id": "where-it-is",
        "label": "Where it is now",
        "type": "prose",
        "content": [
            "On hold. I put it down when other things took priority and haven\u2019t come back to it yet.",
            "The areas I\u2019d want to improve if I picked it up again: better web search integration, more capable visual processing. The foundation is there.",
        ],
    },
]
