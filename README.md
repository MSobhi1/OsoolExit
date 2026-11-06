# OsoolExit brand kit + demo site (draft v2)

Palette: aubergine `#3D1F56` + saffron `#E09F1F` on warm cream `#FBF7F0`.
Chosen to stay away from the competitors' navy / teal / blue (measured live: Aqar Exit `#0f172a` `#0d9488` `#1e3a8a`, Aqar Out slate-navy + teal).
Font: Cairo (Arabic + Latin), self-hosted in `fonts/`.

## What's inside
- `site/index.html` — start here. 15 static pages, Arabic RTL (default) and English LTR, light/dark.
  Home, For sellers (5-step assessment wizard), For buyers (registration), Opportunities (filters + favorites),
  Opportunity details, Calculator, How it works, Our story, FAQ, Contact, For developers, Investors,
  Reports & index, Privacy, Terms.
- `logo/` — English-only logo: symbol, horizontal lockup (light, on-dark, mono black, mono white), app icon.
  The wordmark is outlined from Cairo ExtraBold, so the SVGs need no installed fonts.
- `theme.css` — design tokens (light + dark), RTL-first components, verification-state badges.
- `tailwind.preset.js` — the same tokens for Tailwind.
- `fonts/` — Cairo woff2 files + `cairo.css` (SIL Open Font License).
- `build/` — Python generators for the logo set and all pages (needs `pip install fonttools brotli`).
  Run `python3 build_logos.py && python3 build_site.py` from inside `build/`.
- `check_contrast.py` — re-checks every text/background pair in `theme.css` against WCAG AA.

## Open it locally
Serve the kit root (fonts need http, not file://):
`python3 -m http.server 8000` then open http://localhost:8000/site/index.html

## Before real use
1. **Placeholders:** the 0.5% buyer commission, all listings and projects, `hello@osoolexit.com` and the phone number are demo values.
2. **Draft copy:** story, investors, developers, FAQ, privacy and terms are first drafts. Replace the story with the real one and have a lawyer review the legal pages.
3. **Forms send nothing.** They show a demo confirmation. Wire them to a backend (e.g. a Frappe web form or API) before launch.
4. **Reports page** is computed from the fictional demo units only.
5. **Not checked:** domain availability for osoolexit.com, trademark search, developer-approval and brokerage licensing requirements in Egypt.
6. Page structure mirrors the navigation of aqarexit.com (read from its home page); wording and visuals are original. Their inner pages could not be fetched, so form fields and page details are my own design, not a copy.
