#!/usr/bin/env python3
"""Generate the SVG assets used by README.md (banner and project cards).

Run from anywhere: python3 scripts/build-assets.py
Output goes to assets/ next to this scripts/ directory.
"""

import math
import random
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
CARDS = OUT / "cards"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

ACCENT = "#f2a65a"

# ---------------------------------------------------------------- banner

BANNER_W, BANNER_H = 900, 300

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
    while len(stars) < 38:
        x, y = rng.uniform(8, BANNER_W - 8), rng.uniform(8, 150)
        if x < 430 and 60 < y < 210:  # keep the text area calm
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

    length = route_length(ROUTE)
    route_d = "M" + " L".join(f"{x},{y}" for x, y in ROUTE)
    dur = "14s"
    key_times = "0;0.75;1"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{BANNER_W}" height="{BANNER_H}" viewBox="0 0 {BANNER_W} {BANNER_H}" role="img" aria-labelledby="t d">
  <title id="t">Ehouarn Duriaux</title>
  <desc id="d">Apprentice IT specialist at EPFL. A climber follows a ridge up the Weisshorn: one contribution, one metre.</desc>
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
    <path d="M0,240 L90,214 L170,226 L260,192 L350,214 L430,170 L500,196 L580,150 L660,190 L740,160 L820,190 L900,170 L900,300 L0,300 Z" fill="#1a2550"/>
    <path d="M0,262 L120,240 L230,252 L330,222 L420,238 L500,190 L560,200 L610,120 L650,52 L690,118 L735,100 L790,160 L850,140 L900,170 L900,300 L0,300 Z" fill="#0e1633"/>
    <path d="M650,52 L690,118 L668,150 L650,108 Z" fill="#9fb4ff" opacity="0.10"/>
    <path d="M650,52 L624,98 L640,92 L652,106 L668,90 L690,118 Z" fill="#dfe8ff" opacity="0.22"/>
    <path d="{route_d}" fill="none" stroke="url(#trail)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{length:.0f}" stroke-dashoffset="{length:.0f}">
      <animate attributeName="stroke-dashoffset" values="{length:.0f};0;0" keyTimes="{key_times}" dur="{dur}" repeatCount="indefinite"/>
    </path>
    <g>
      <circle r="9" fill="{ACCENT}" opacity="0.28"><animate attributeName="r" values="7;11;7" dur="2.4s" repeatCount="indefinite"/></circle>
      <circle r="3.4" fill="#fff"/>
      <animateMotion path="{route_d}" keyPoints="0;1;1" keyTimes="{key_times}" calcMode="linear" dur="{dur}" repeatCount="indefinite"/>
    </g>
    <path d="M0,300 L0,272 L110,262 L240,274 L380,258 L520,272 L660,260 L800,274 L900,264 L900,300 Z" fill="#080d1f"/>
    <g font-family="{SANS}">
      <text x="44" y="112" font-size="46" font-weight="700" fill="#f4f6ff" letter-spacing="-0.5">Ehouarn Duriaux</text>
      <text x="46" y="148" font-size="19" fill="#a9b6d9">Apprentice IT specialist · EPFL</text>
      <text x="46" y="190" font-size="17" font-style="italic" fill="{ACCENT}">Une contribution, un mètre.
        <animate attributeName="opacity" values="0;0;1" keyTimes="0;0.3;1" dur="1.8s" begin="0s" fill="freeze"/>
      </text>
    </g>
  </g>
  <rect x="0.5" y="0.5" width="{BANNER_W - 1}" height="{BANNER_H - 1}" rx="13.5" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>
</svg>
"""


# ----------------------------------------------------------------- cards

CARD_W, CARD_H = 400, 96

EPFL_RED = "#e2001a"
PROJECTS = [
    # slug, name, description, tag, colour, url
    ("wordpress-kubernetes", "WordPress on Kubernetes", "DevOps for EPFL's WordPress sites",
     "EPFL · internal", EPFL_RED, "https://duriaux.dev/projets/wordpress-kubernetes"),
    ("wp-veritas", "wp-veritas", "Tracks every EPFL WordPress site",
     "EPFL · lead contributor, 1,000+ commits", EPFL_RED, "https://duriaux.dev/projets/wp-veritas"),
    ("capi-ui", "capi-ui", "Cluster API console for OpenStack",
     "TypeScript", "#3178c6", "https://github.com/dwesh163/capi-ui"),
    ("create-stack", "create-stack", "Scaffold Next.js and Expo apps",
     "TypeScript", "#3178c6", "https://github.com/dwesh163/create-stack"),
    ("spotosh", "spotosh", "Navidrome player with Last.fm",
     "TypeScript", "#3178c6", "https://github.com/dwesh163/spotosh"),
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


def card(name, desc, tag, colour):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W}" height="{CARD_H}" viewBox="0 0 {CARD_W} {CARD_H}" role="img" aria-label="{escape(name)}: {escape(desc)}">
  <style>
    .bg {{ fill: #ffffff; }}
    .bd {{ stroke: #d0d7de; }}
    .name {{ fill: #1f2328; }}
    .desc {{ fill: #59636e; }}
    .tag {{ fill: #59636e; }}
    .arrow {{ stroke: #8c959f; }}
    @media (prefers-color-scheme: dark) {{
      .bg {{ fill: #0d1117; }}
      .bd {{ stroke: #30363d; }}
      .name {{ fill: #f0f6fc; }}
      .desc {{ fill: #9198a1; }}
      .tag {{ fill: #9198a1; }}
      .arrow {{ stroke: #6e7681; }}
    }}
  </style>
  <defs><clipPath id="c"><rect width="{CARD_W}" height="{CARD_H}" rx="12"/></clipPath></defs>
  <rect class="bg" width="{CARD_W}" height="{CARD_H}" rx="12"/>
  <g clip-path="url(#c)">
    <rect width="5" height="{CARD_H}" fill="{colour}"/>
    <rect x="5" width="120" height="{CARD_H}" fill="{colour}" opacity="0.06"/>
  </g>
  <rect class="bd" x="0.5" y="0.5" width="{CARD_W - 1}" height="{CARD_H - 1}" rx="11.5" fill="none"/>
  <text class="name" x="26" y="38" font-family="{SANS}" font-size="18" font-weight="650">{escape(name)}</text>
  <text class="desc" x="26" y="61" font-family="{SANS}" font-size="14">{escape(desc)}</text>
  <circle cx="30" cy="79" r="4" fill="{colour}"/>
  <text class="tag" x="40" y="83" font-family="{MONO}" font-size="11.5">{escape(tag)}</text>
  <path class="arrow" d="M368,30 L378,30 L378,40 M378,30 L366,42" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def main():
    OUT.mkdir(exist_ok=True)
    CARDS.mkdir(exist_ok=True)
    (OUT / "banner.svg").write_text(banner(), encoding="utf-8")
    for slug, name, desc, tag, colour, _ in PROJECTS:
        (CARDS / f"{slug}.svg").write_text(card(name, desc, tag, colour), encoding="utf-8")
    print(f"wrote banner.svg and {len(PROJECTS)} cards to {OUT}")


if __name__ == "__main__":
    main()
