#!/usr/bin/env python3
"""Generate the SVG assets used by README.md (banner and project cards).

Run from anywhere: python3 scripts/build-assets.py
Output goes to assets/ next to this scripts/ directory.
"""

import math
import random
import re
import textwrap
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
CARDS = OUT / "cards"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

ACCENT = "#f2a65a"

# ---------------------------------------------------------------- banner

BANNER_W, BANNER_H = 900, 250
K = BANNER_H / 300  # the scenery was drawn for a 300px tall banner


def sy(path):
    """Scale the y coordinate of every 'x,y' pair in a path string."""
    return re.sub(
        r"(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)",
        lambda m: f"{m.group(1)},{float(m.group(2)) * K:.1f}",
        path,
    )


# The climbing route follows the main ridge up to the summit.
ROUTE = [
    (0, 262), (120, 240), (230, 252), (330, 222), (420, 238),
    (500, 190), (560, 200), (610, 120), (650, 52),
]


def route_length(points):
    return sum(math.dist(a, b) for a, b in zip(points, points[1:]))


def banner():
    rng = random.Random(7)
    stars = []
    twinkle = 0
    while len(stars) < 36:
        x, y = rng.uniform(8, BANNER_W - 8), rng.uniform(8, 130)
        if x < 430 and 60 < y < 170:  # keep the text area calm
            continue
        r = rng.uniform(0.6, 1.5)
        o = rng.uniform(0.3, 0.85)
        anim = ""
        if twinkle < 9:
            anim = (
                f'<animate attributeName="opacity" values="{o:.2f};{o * 0.25:.2f};{o:.2f}" '
                f'dur="{rng.uniform(3, 6):.1f}s" begin="{rng.uniform(0, 4):.1f}s" repeatCount="indefinite"/>'
            )
            twinkle += 1
        stars.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fff" opacity="{o:.2f}">{anim}</circle>')

    route = [(x, y * K) for x, y in ROUTE]
    length = route_length(route)
    route_d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in route)
    dur = "14s"
    key_times = "0;0.75;1"

    far = sy("M0,240 L90,214 L170,226 L260,192 L350,214 L430,170 L500,196 L580,150 L660,190 L740,160 L820,190 L900,170 L900,300 L0,300 Z")
    main = sy("M0,262 L120,240 L230,252 L330,222 L420,238 L500,190 L560,200 L610,120 L650,52 L690,118 L735,100 L790,160 L850,140 L900,170 L900,300 L0,300 Z")
    lit = sy("M650,52 L690,118 L668,150 L650,108 Z")
    snow = sy("M650,52 L624,98 L640,92 L652,106 L668,90 L690,118 Z")
    front = sy("M0,300 L0,272 L110,262 L240,274 L380,258 L520,272 L660,260 L800,274 L900,264 L900,300 Z")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{BANNER_W}" height="{BANNER_H}" viewBox="0 0 {BANNER_W} {BANNER_H}" role="img" aria-labelledby="t d">
  <title id="t">Ehouarn Duriaux</title>
  <desc id="d">Apprentice IT specialist at EPFL. A climber follows a ridge up the Weisshorn.</desc>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#070b18"/>
      <stop offset="0.55" stop-color="#141f3d"/>
      <stop offset="1" stop-color="#2a2f5a"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.72" cy="0.86" r="0.55">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity="0.38"/>
      <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="trail" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity="0.15"/>
      <stop offset="1" stop-color="#ffd9a0"/>
    </linearGradient>
    <clipPath id="round"><rect width="{BANNER_W}" height="{BANNER_H}" rx="14"/></clipPath>
  </defs>
  <g clip-path="url(#round)">
    <rect width="{BANNER_W}" height="{BANNER_H}" fill="url(#sky)"/>
    <rect width="{BANNER_W}" height="{BANNER_H}" fill="url(#glow)"/>
    {"".join(stars)}
    <path d="{far}" fill="#1a2550"/>
    <path d="{main}" fill="#0e1633"/>
    <path d="{lit}" fill="#9fb4ff" opacity="0.10"/>
    <path d="{snow}" fill="#dfe8ff" opacity="0.22"/>
    <path d="{route_d}" fill="none" stroke="url(#trail)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{length:.0f}" stroke-dashoffset="{length:.0f}">
      <animate attributeName="stroke-dashoffset" values="{length:.0f};0;0" keyTimes="{key_times}" dur="{dur}" repeatCount="indefinite"/>
    </path>
    <g>
      <circle r="9" fill="{ACCENT}" opacity="0.28"><animate attributeName="r" values="7;11;7" dur="2.4s" repeatCount="indefinite"/></circle>
      <circle r="3.4" fill="#fff"/>
      <animateMotion path="{route_d}" keyPoints="0;1;1" keyTimes="{key_times}" calcMode="linear" dur="{dur}" repeatCount="indefinite"/>
    </g>
    <path d="{front}" fill="#080d1f"/>
    <g font-family="{SANS}">
      <text x="44" y="121" font-size="46" font-weight="700" fill="#f4f6ff" letter-spacing="-0.5">Ehouarn Duriaux</text>
      <text x="46" y="157" font-size="19" fill="#a9b6d9">Apprentice IT specialist · EPFL</text>
    </g>
  </g>
  <rect x="0.5" y="0.5" width="{BANNER_W - 1}" height="{BANNER_H - 1}" rx="13.5" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
"""


# ----------------------------------------------------------------- cards

# The card body is CARD_H tall; CARD_GAP is a little transparent room under it
# that separates the rows, since the README cannot use CSS margins.
CARD_W, CARD_H, CARD_GAP = 200, 82, 6

EPFL_RED = "#e2001a"
PLATFORM = "#2dd4bf"
SOON = "#8b949e"

PROJECTS = [
    # slug, name, description, language or label, dot colour, url
    ("wordpress-kubernetes", "WordPress EPFL", "DevOps for EPFL's WordPress sites",
     "EPFL", EPFL_RED, "https://duriaux.dev/projets/wordpress-kubernetes"),
    ("wp-veritas", "wp-veritas", "Source of truth for every EPFL WordPress site",
     "EPFL", EPFL_RED, "https://duriaux.dev/projets/wp-veritas"),
    ("xdew-cloud", "xdew.cloud", "Managed cloud: projects, storage and identity",
     "Platform", PLATFORM, "https://xdew.cloud"),
    ("xdew-studio", "xdew.studio", "Under construction",
     "Soon", SOON, "https://xdew.studio"),
    ("kooked", "kooked.ch", "Self-hosted apps for our own needs",
     "Platform", PLATFORM, "https://kooked.ch"),
    ("capi-ui", "capi-ui", "Cluster API console for OpenStack",
     "TypeScript", "#3178c6", "https://github.com/dwesh163/capi-ui"),
    ("create-stack", "create-stack", "Scaffold Next.js and Expo apps",
     "TypeScript", "#3178c6", "https://github.com/dwesh163/create-stack"),
    ("shed", "shed", "Kubernetes and OpenShift ops toolkit",
     "Shell", "#89e051", "https://github.com/dwesh163/shed"),
    ("BONDS", "BONDS", "Namespace backups to S3 with restic",
     "Shell", "#89e051", "https://github.com/dwesh163/BONDS"),
    ("outlinewiki-exporter", "outlinewiki-exporter", "Prometheus exporter for Outline Wiki",
     "Go", "#00add8", "https://github.com/dwesh163/outlinewiki-exporter"),
    ("skills", "skills", "Skills for coding agents",
     "Markdown", "#3d6fd8", "https://github.com/dwesh163/skills"),
    ("actions", "actions", "Reusable GitHub Actions for CI/CD",
     "GitHub Actions", "#2088ff", "https://github.com/dwesh163/actions"),
]


def card(name, desc, label, colour):
    total_h = CARD_H + CARD_GAP
    name_size = 12.5 if len(name) > 17 else 14
    # One line when it fits, otherwise the narrowest wrap that stays on two
    # lines, so the second line is never a lone word.
    if len(desc) <= 27:
        lines = [desc]
    else:
        width = next(w for w in range(14, 28) if len(textwrap.wrap(desc, width=w)) <= 2)
        lines = textwrap.wrap(desc, width=width)
    desc_svg = "\n  ".join(
        f'<text class="desc" x="16" y="{43 + 14 * i}" font-family="{SANS}" font-size="11.5">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W}" height="{total_h}" viewBox="0 0 {CARD_W} {total_h}" role="img" aria-label="{escape(name)}: {escape(desc)}">
  <style>
    .s1 {{ stop-color: #ffffff; }}
    .s2 {{ stop-color: #f5f7fb; }}
    .bd {{ stroke: #d0d7e2; }}
    .name {{ fill: #1b2233; }}
    .desc {{ fill: #535d78; }}
    .lang {{ fill: #5a6480; }}
    .arrow {{ stroke: #7d88a6; }}
    @media (prefers-color-scheme: dark) {{
      .s1 {{ stop-color: #151b27; }}
      .s2 {{ stop-color: #0f141d; }}
      .bd {{ stroke: #2a3345; }}
      .name {{ fill: #f1f4ff; }}
      .desc {{ fill: #a3aed0; }}
      .lang {{ fill: #9aa6c8; }}
      .arrow {{ stroke: #7080a8; }}
    }}
  </style>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop class="s1" offset="0"/><stop class="s2" offset="1"/></linearGradient>
  </defs>
  <rect class="bd" x="0.5" y="0.5" width="{CARD_W - 1}" height="{CARD_H - 1}" rx="11" fill="url(#g)"/>
  <path class="arrow" d="M180,19 L187,12 M181,12 L187,12 L187,18" fill="none" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="name" x="16" y="26" font-family="{SANS}" font-size="{name_size}" font-weight="650">{escape(name)}</text>
  {desc_svg}
  <circle cx="19" cy="71" r="3" fill="{colour}"/>
  <text class="lang" x="27" y="74.5" font-family="{SANS}" font-size="11">{escape(label)}</text>
</svg>
"""


def main():
    OUT.mkdir(exist_ok=True)
    CARDS.mkdir(exist_ok=True)
    (OUT / "banner.svg").write_text(banner(), encoding="utf-8")
    keep = {f"{p[0]}.svg" for p in PROJECTS}
    for old in CARDS.glob("*.svg"):
        if old.name not in keep:
            old.unlink()
    for slug, name, desc, label, colour, _ in PROJECTS:
        (CARDS / f"{slug}.svg").write_text(card(name, desc, label, colour), encoding="utf-8")
    print(f"wrote banner.svg and {len(PROJECTS)} cards to {OUT}")


if __name__ == "__main__":
    main()
