#!/usr/bin/env python3
"""Generates the OsoolExit logo set (English-only wordmark, outlined in Cairo 800).
Every variant shares identical geometry; the wordmark is converted to vector paths
with fontTools, so the SVGs need no installed fonts."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "logo")
FONT = os.path.join(BASE, "fonts", "cairo-latin-800-normal.woff2")
os.makedirs(OUT, exist_ok=True)

AUBERGINE = "#3D1F56"
SAFFRON = "#E09F1F"
SAFFRON_DEEP = "#BD7A00"   # arrow/"Exit" on light backgrounds (>= 3:1 on cream)
SAFFRON_LIGHT = "#F2B33D"
CREAM = "#F6EFE3"
BLACK = "#111111"
WHITE = "#FFFFFF"

# "O" ring open on the right, with an exit arrow passing through the opening.
RING = "M40.856 47.32 A20 20 0 1 1 40.856 16.68"
ARROW = "M32 32 H56 M50 24 L58 32 L50 40"


def symbol(ring, arrow):
    return (
        f'<path d="{RING}" fill="none" stroke="{ring}" stroke-width="9" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
        f'<path d="{ARROW}" fill="none" stroke="{arrow}" stroke-width="8" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )


def symbol_svg(ring, arrow, title="OsoolExit symbol"):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="256" height="256" '
        f'role="img" aria-label="{title}"><title>{title}</title>{symbol(ring, arrow)}</svg>\n'
    )


# ---- outlined wordmark -------------------------------------------------------
font = TTFont(FONT)
gs = font.getGlyphSet()
cmap = font.getBestCmap()
hmtx = font["hmtx"]
UPEM = font["head"].unitsPerEm
CAP = font["OS/2"].sCapHeight or 700


def outline(text, size, x0, baseline, tracking=0.0):
    """Returns (svg path data, x after last glyph). tracking is in px."""
    scale = size / UPEM
    x = x0
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for ch in text:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (scale, 0, 0, -scale, x, baseline))
        gs[g].draw(tp)
        x += hmtx[g][0] * scale + tracking
    return pen.getCommands(), x - tracking


SIZE = 46
TRACK = -0.6
SYMBOL_TOP = 8                      # symbol (64 box) sits at y=8 in an 80px-high canvas
CENTER_Y = SYMBOL_TOP + 32          # optical center of the ring
BASELINE = CENTER_Y + (CAP * SIZE / UPEM) / 2
TEXT_X = 80

osool_d, x_mid = outline("Osool", SIZE, TEXT_X, BASELINE, TRACK)
exit_d, x_end = outline("Exit", SIZE, x_mid + TRACK, BASELINE, TRACK)
VB_W = int(x_end + 6 + 0.999)


def horizontal_svg(ring, arrow, osool, exit_, title="OsoolExit"):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W} 80" width="{VB_W * 2}" height="160" '
        f'role="img" aria-label="{title}"><title>{title}</title>'
        f'<g transform="translate(0,{SYMBOL_TOP})">{symbol(ring, arrow)}</g>'
        f'<path d="{osool_d}" fill="{osool}"/><path d="{exit_d}" fill="{exit_}"/>'
        '</svg>\n'
    )


def app_icon_svg():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" '
        'role="img" aria-label="OsoolExit app icon"><title>OsoolExit app icon</title>'
        f'<rect width="512" height="512" rx="112" fill="{AUBERGINE}"/>'
        f'<g transform="translate(85.7 89.6) scale(5.2)">{symbol(CREAM, SAFFRON)}</g>'
        '</svg>\n'
    )


files = {
    "symbol.svg": symbol_svg(AUBERGINE, SAFFRON_DEEP),
    "symbol-on-dark.svg": symbol_svg(CREAM, SAFFRON_LIGHT),
    "symbol-mono-black.svg": symbol_svg(BLACK, BLACK),
    "symbol-mono-white.svg": symbol_svg(WHITE, WHITE),
    "horizontal.svg": horizontal_svg(AUBERGINE, SAFFRON_DEEP, AUBERGINE, SAFFRON_DEEP),
    "horizontal-on-dark.svg": horizontal_svg(CREAM, SAFFRON_LIGHT, CREAM, SAFFRON_LIGHT),
    "horizontal-mono-black.svg": horizontal_svg(BLACK, BLACK, BLACK, BLACK),
    "horizontal-mono-white.svg": horizontal_svg(WHITE, WHITE, WHITE, WHITE),
    "app-icon.svg": app_icon_svg(),
}

for name, svg in files.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name)
print("viewBox width", VB_W, "baseline", round(BASELINE, 1))
