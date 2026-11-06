#!/usr/bin/env python3
"""Builds every page of the OsoolExit demo site into /home/claude/osoolexit-brand/site/."""
import glob, os
import sitelib
import pages_a as a
import pages_b as b

for f in glob.glob(f"{sitelib.SITE}/*.html"):
    os.remove(f)

pages = [a.home, a.sellers, a.buyers, a.opportunities, a.opportunity,
         b.calculator, b.how, b.story, b.faq, b.contact, b.developers, b.investors,
         b.reports, b.privacy, b.terms]
for fn in pages:
    html = fn()
    # layout() returns the HTML; the slug is the page's own filename stem
    slug = {"home": "index", "how": "how-it-works"}.get(fn.__name__, fn.__name__)
    sitelib.write(slug, html)
