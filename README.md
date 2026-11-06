# OsoolExit — brand kit + demo site (draft v3)

**The repo root IS the website.** Hostinger serves this folder as `public_html`, so `index.html` sits at the top level and every path is relative to it. No build step is needed to publish.

Palette: aubergine `#3D1F56` + saffron `#E09F1F` on cream `#FBF7F0`. Font: Cairo (self-hosted, `fonts/`).

## Layout
- `*.html` — 15 static pages (Arabic RTL default, English LTR, light/dark).
- `assets/` — `site.css`, `site.js`.
- `theme.css`, `fonts/`, `logo/` — tokens, Cairo woff2, English-only logo set.
- `.htaccess` — index file, no directory listing, hides `tools/` and this README from the public.
- `tools/` — Python generators + contrast checker (not needed on the server).

## Regenerate pages (optional)
`pip install fonttools brotli`, then from `tools/`: `python3 build_logos.py && python3 build_site.py`. `python3 check_contrast.py` re-checks WCAG AA.

## Preview locally
`python3 -m http.server 8000` in this folder → http://localhost:8000/

## Before real launch
1. Pages carry `<meta name="robots" content="noindex, nofollow">` because content is demo. **Remove it in `tools/sitelib.py` and rebuild at launch.**
2. Placeholders: 0.5% buyer commission, all listings, `hello@osoolexit.com`, phone number.
3. Story, investors, developers, FAQ, privacy, terms are drafts; get legal review.
4. Forms send nothing (demo confirmation only).
5. Not checked: trademark, Egyptian brokerage / developer-approval requirements.

## Domain shows NXDOMAIN?
That is DNS, not these files. Test: `nslookup osoolexit.com 8.8.8.8`. If it answers, flush your cache (`ipconfig /flushdns`). If it also says NXDOMAIN, the nameservers/DNS zone at the registrar are not pointing to Hostinger.
