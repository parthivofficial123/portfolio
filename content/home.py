"""
content/home.py
---------------
Copy and data specific to the Home page.

Separated from views/home.py so that text can be updated without
touching layout or rendering logic.
"""

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
hero = {
    "name": "Parthiv Patel",
    "body": [
        "I build things, take them apart, abandon some of them, come back to "
        "others, and usually learn something in the process.",
        "Most of the time that means code, AI, robots, or something mechanical. "
        "Sometimes it has absolutely nothing to do with any of those.",
        "Currently a high-school senior in Southern California.",
    ],
    "scroll_cue": "Selected work \u2193",
}

# ---------------------------------------------------------------------------
# Right Now
# ---------------------------------------------------------------------------
# Each entry: (category, text)
# category is rendered in mono/uppercase; text is the actual item.
right_now = [
    ("Building",       "This website, apparently."),
    ("Preparing",      "Caltech EWB Science & Engineering Competition"),
    ("Preparing",      "SAT"),
    ("Writing",        "A few game bibles and worlds that may or may not ever "
                       "become actual games."),
    ("Watching",       "Working my way through Marvel again. Also rewatching "
                       "House\u00a0M.D."),
    ("Looking forward to", "December.\nCollege applications will finally be over."),
]

# ---------------------------------------------------------------------------
# Away from the computer
# ---------------------------------------------------------------------------
away = {
    "body": [
        "I take photos. I hike and backpack. I go to the gym. I play games, "
        "listen to a frankly unreasonable range of music, watch movies, and "
        "spend a lot of time making up things that don\u2019t exist.",
        "I like documenting places too. Sometimes I\u2019ll be somewhere new and "
        "already be thinking about the shots I\u2019d use if I turned the trip "
        "into a little film later.",
        "There\u2019s more to me than the engineering stuff. This page would get "
        "ridiculously long if I tried putting all of it here.",
    ],
    "cta_label": "More about me \u2192",
}
