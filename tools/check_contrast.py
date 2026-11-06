#!/usr/bin/env python3
"""Reads theme.css and checks every foreground/background pair the components use.
Text pairs need 4.5:1, graphics / input outlines need 3:1 (WCAG 2.x AA)."""
import re, sys, os

css = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "theme.css"), encoding="utf-8").read()


def block(selector):
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\n\}", css, re.S)
    return {k: v for k, v in re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", m.group(1))} if m else {}


light = block(":root")
dark = {**light, **block(':root[data-theme="dark"]')}


def lum(h):
    h = h.lstrip("#")
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def mix(a, b, pct):  # pct of a over b, like color-mix(in srgb)
    a, b = a.lstrip("#"), b.lstrip("#")
    out = [round(int(a[i:i + 2], 16) * pct + int(b[i:i + 2], 16) * (1 - pct)) for i in (0, 2, 4)]
    return "#" + "".join(f"{v:02x}" for v in out)


# (label, fg var, bg var or ("mix", a, b, pct), minimum ratio)
PAIRS = [
    ("body text on page", "ink", "bg", 4.5),
    ("body text on card", "ink", "surface", 4.5),
    ("muted text on page", "ink-muted", "bg", 4.5),
    ("muted text on card", "ink-muted", "surface", 4.5),
    ("muted text on sunken band", "ink-muted", "surface-sunken", 4.5),
    ("body text on sunken band", "ink", "surface-sunken", 4.5),
    ("primary button label", "on-primary", "primary", 4.5),
    ("primary button hover", "on-primary", "primary-hover", 4.5),
    ("accent button label", "on-accent", "accent", 4.5),
    ("accent button hover", "on-accent", "accent-hover", 4.5),
    ("link / secondary button on page", "primary", "bg", 4.5),
    ("link on sunken band", "primary", "surface-sunken", 4.5),
    ("accent small text on page", "accent-text", "bg", 4.5),
    ("accent large text/graphic on page", "accent-deep", "bg", 3.0),
    ("input outline vs card", "border-strong", "surface", 3.0),
    ("input outline vs page", "border-strong", "bg", 3.0),
    ("focus ring vs page", "focus", "bg", 3.0),
    ("focus ring vs card", "focus", "surface", 3.0),
    ("gain figure on primary panel", "gain-on-primary", "primary", 4.5),
    ("verified badge", "verified-fg", "verified-bg", 4.5),
    ("review badge", "review-fg", "review-bg", 4.5),
    ("declared badge", "declared-fg", "declared-bg", 4.5),
    ("unknown badge", "unknown-fg", "unknown-bg", 4.5),
    ("danger text", "danger-fg", "danger-bg", 4.5),
    ("loss figure on card", "danger-fg", "surface", 4.5),
    ("win figure on highlighted column", "verified-fg", ("mix", "accent", "surface", 0.12), 4.5),
    ("body text on highlighted column", "ink", ("mix", "accent", "surface", 0.12), 4.5),
]

fails = 0
for name, theme in (("LIGHT", light), ("DARK", dark)):
    print(f"== {name} ==")
    for label, fg, bg, need in PAIRS:
        if fg not in theme:
            print(f"MISSING  --{fg} ({label})"); fails += 1; continue
        bgc = mix(theme[bg[1]], theme[bg[2]], bg[3]) if isinstance(bg, tuple) else theme[bg]
        r = ratio(theme[fg], bgc)
        ok = r >= need
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'} {r:5.2f} (min {need}) {label}: {theme[fg]} on {bgc}")
print("\nfailures:", fails)
sys.exit(1 if fails else 0)
