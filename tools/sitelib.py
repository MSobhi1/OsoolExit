"""Shared layout + helpers for the OsoolExit static site generator.
Every page carries both languages in the DOM; <html lang> picks which one shows."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = ROOT

EMAIL = "hello@osoolexit.com"            # placeholder address
PHONE_DISPLAY = "+20 1XX XXX XXXX"       # placeholder number


def B(ar, en):
    """Inline bilingual text."""
    return f'<span lang="ar">{ar}</span><span lang="en">{en}</span>'


def T(tag, ar, en, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<{tag}{c}>{B(ar, en)}</{tag}>"


ICONS = {
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L16 9.5"/>',
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "coins": '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>',
    "eyeoff": '<path d="M3 3l18 18M10.6 10.6a2 2 0 0 0 2.8 2.8M9.9 5.1A9.8 9.8 0 0 1 12 5c5 0 9 4.5 10 7-.4 1-1.2 2.3-2.4 3.5M6.2 6.2C4.1 7.6 2.6 9.8 2 12c1 2.5 5 7 10 7 1.6 0 3-.4 4.3-1"/>',
    "heart": '<path d="M12 20s-7-4.4-9-9.2C1.8 7.5 3.6 4.5 6.7 4.5c1.9 0 3.3 1 4.3 2.4 1-1.4 2.4-2.4 4.3-2.4 3.1 0 4.9 3 3.7 6.3C19 15.6 12 20 12 20z"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "home": '<path d="M3 11l9-8 9 8v10H3z"/>',
    "list": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    "calc": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M14 12h2M8 16h2M14 16h2"/>',
    "upload": '<path d="M12 16V4M7 9l5-5 5 5M4 20h16"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "scale": '<path d="M12 3v18M5 7h14M5 7l-3 7a3.5 3.5 0 0 0 6 0zM19 7l-3 7a3.5 3.5 0 0 0 6 0z"/>',
    "building": '<path d="M5 21V5l9-2v18M14 9h5v12M8 9h2M8 13h2M8 17h2"/>',
    "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/>',
}


def icon(name, size=22, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def arrow():
    return icon("arrow", 18, "icon-dir")


def fmt(n):
    return f"{int(round(n)):,}"


# ---- inline, theme-aware logo built from the generated horizontal.svg ----
def inline_logo():
    svg = open(f"{ROOT}/logo/horizontal.svg", encoding="utf-8").read()
    svg = re.sub(r'\swidth="\d+"\sheight="\d+"', "", svg, count=1)
    svg = svg.replace("#3D1F56", "var(--logo-main)").replace("#BD7A00", "var(--logo-accent)")
    return svg.replace("<svg ", '<svg focusable="false" ', 1).strip()


# ---- form helpers ----
def field(fid, ar, en, typ="text", ph=("", ""), required=False, hint=None, cls="", full=False, value=None, extra=""):
    req = " required" if required else ""
    star = " *" if required else ""
    val = f' value="{value}"' if value is not None else ""
    h = f'<span class="hint">{B(*hint)}</span>' if hint else ""
    num = typ == "money"
    t = "text" if num else typ
    mode = ' inputmode="numeric"' if num else ""
    klass = f'input {"input-num" if num else ""} {cls}'.strip()
    return (f'<div class="field{" full" if full else ""}"><label for="{fid}">{B(ar, en)}{star}</label>'
            f'<input class="{klass}" id="{fid}" name="{fid}" type="{t}"{mode}{req}{val} data-ph-ar="{ph[0]}" data-ph-en="{ph[1]}" {extra}>{h}</div>')


def select(fid, ar, en, options, required=False, full=False, data_filter=None):
    """options: [(value, ar, en)]"""
    req = " required" if required else ""
    df = f' data-filter="{data_filter}"' if data_filter else ""
    opts = "".join(f'<option value="{v}" data-ar="{a}" data-en="{e}">{a}</option>' for v, a, e in options)
    return (f'<div class="field{" full" if full else ""}"><label for="{fid}">{B(ar, en)}</label>'
            f'<select class="input" id="{fid}" name="{fid}"{req}{df}>{opts}</select></div>')


def textarea(fid, ar, en, ph=("", ""), full=True, required=False):
    req = " required" if required else ""
    ph = ph or ("", "")
    return (f'<div class="field{" full" if full else ""}"><label for="{fid}">{B(ar, en)}</label>'
            f'<textarea class="input" id="{fid}" name="{fid}"{req} data-ph-ar="{ph[0]}" data-ph-en="{ph[1]}"></textarea></div>')


def consent(fid, ar, en, required=True):
    req = " required" if required else ""
    return f'<label class="check full" for="{fid}"><input type="checkbox" id="{fid}"{req}><span>{B(ar, en)}</span></label>'


def ok_msg(ar="هذا نموذج تجريبي ولم يُرسل أي شيء.", en="This is a demo form. Nothing was sent."):
    return f'<div class="form-ok" role="status">{B(ar, en)}</div>'


def stepper(items, current=0):
    out = []
    for i, (ar, en) in enumerate(items):
        cls = ' class="todo"' if i > current else ""
        cur = ' aria-current="step"' if i == current else ""
        out.append(f"<li{cls}{cur}><h3>{B(ar, en)}</h3></li>")
    return '<ol class="stepper">' + "".join(out) + "</ol>"


def feature(ico, ar_t, en_t, ar_p, en_p):
    return (f'<div class="card feature"><div class="ico">{icon(ico)}</div>'
            f'<h3>{B(ar_t, en_t)}</h3><p>{B(ar_p, en_p)}</p></div>')


def checks(items):
    return '<ul class="checks">' + "".join(f"<li><span>{B(a, e)}</span></li>" for a, e in items) + "</ul>"


def trust_strip():
    return f"""<div class="trust">
  <div><div class="k">{B('عمولة البائع','Seller commission')}</div><div class="v num">0%</div></div>
  <div><div class="k">{B('عمولة المشتري','Buyer commission')}</div><div class="v num">0.5%</div></div>
  <div><div class="k">{B('موعد الاستحقاق','Due')}</div><div class="v">{B('بعد إتمام التنازل','After transfer completes')}</div></div>
  <div><div class="k">{B('قبل النشر','Before publishing')}</div><div class="v">{B('مراجعة بشرية','Human review')}</div></div>
</div>
<p class="muted" style="margin-top:var(--space-2);font-size:.85rem">{B('أرقام تجريبية للتصميم. نسبة عمولة المشتري لم تُحسم بعد.','Demo figures for design. The buyer commission rate is not final.')}</p>"""


def calc_box(prefix="c", compact=False):
    """Calculator component. Outputs are filled by site.js via data-in / data-out."""
    def inp(k, ar, en, val, hint=None, dec=False):
        mode = "decimal" if dec else "numeric"
        h = f'<span class="hint">{B(*hint)}</span>' if hint else ""
        return (f'<div class="field"><label for="{prefix}-{k}">{B(ar, en)}</label>'
                f'<input class="input input-num" id="{prefix}-{k}" data-in="{k}" inputmode="{mode}" value="{val}">{h}</div>')
    fee = "" if compact else inp("fee", "رسوم نقل المطوّر (جنيه)", "Developer transfer fee (EGP)", "0",
                                  ("تختلف من مطوّر لآخر. اسأل المطوّر.", "Differs by developer. Ask the developer."))
    rows = f"""
      <div class="row"><span>{B('المسترد عند الإلغاء','Refund if you cancel')}</span><b class="num" data-out="refund"></b></div>
      <div class="row"><span>{B('المسترد عبر التنازل','Recovered by transfer')}</span><b class="num" data-out="transfer"></b></div>
      <div class="row"><span>{B('الفرق لصالحك','Difference in your favor')}</span><b class="num big gain" data-out="gain"></b></div>
      <div class="row"><span>{B('عمولة المشتري','Buyer commission')}</span><b class="num" data-out="commission"></b></div>"""
    if not compact:
        rows += f"""
      <div class="row"><span>{B('النقد المطلوب من المشتري عند التنازل','Buyer cash needed at transfer')}</span><b class="num" data-out="buyerCash"></b></div>
      <div class="row"><span>{B('المتبقي على المشتري للمطوّر','Remaining owed to the developer')}</span><b class="num" data-out="remaining"></b></div>"""
    return f"""<div class="calc" data-calc>
  <form class="card" onsubmit="return false" aria-label="Calculator">
    {inp('value','قيمة العقد (جنيه)','Contract value (EGP)','6000000')}
    {inp('paid','المدفوع حتى الآن (جنيه)','Paid so far (EGP)','1200000')}
    {inp('ded','خصم الإلغاء (%)','Cancellation deduction (%)','15',('راجع بند الإلغاء في عقدك.','Check the cancellation clause in your contract.'),True)}
    {inp('com','عمولة المشتري (%)','Buyer commission (%)','0.5',('من قيمة العقد بعد إتمام التنازل. قيمة تجريبية.','Of contract value, after the transfer completes. Demo value.'),True)}
    {fee}
  </form>
  <div class="calc-result" aria-live="polite">{rows}
  </div>
</div>"""


# ---- demo listings (fictional) ----
TYPES = {"apartment": ("شقة", "Apartment"), "villa": ("فيلا", "Villa"), "shop": ("محل", "Shop")}
AREAS = {
    "newcairo": ("القاهرة الجديدة", "New Cairo"), "zayed": ("الشيخ زايد", "Sheikh Zayed"),
    "capital": ("العاصمة الإدارية", "New Capital"), "shorouk": ("الشروق", "Shorouk"),
    "mostakbal": ("مستقبل سيتي", "Mostakbal City"), "northcoast": ("الساحل الشمالي", "North Coast"),
}
STATES = {"verified": ("موثّق", "Verified"), "review": ("قيد المراجعة", "In review"), "declared": ("معلن", "Declared")}
UNITS = [
    dict(id="u101", type="apartment", area="newcairo", proj=("مشروع أ", "Project A"), size=148, beds=3, value=6200000, paid=1240000, year=2028, state="verified"),
    dict(id="u102", type="apartment", area="zayed", proj=("مشروع ب", "Project B"), size=110, beds=2, value=3400000, paid=680000, year=2027, state="review"),
    dict(id="u103", type="villa", area="northcoast", proj=("مشروع ج", "Project C"), size=260, beds=4, value=8100000, paid=1620000, year=2029, state="declared"),
    dict(id="u104", type="apartment", area="capital", proj=("مشروع د", "Project D"), size=120, beds=2, value=3000000, paid=600000, year=2027, state="verified"),
    dict(id="u105", type="shop", area="capital", proj=("مشروع هـ", "Project E"), size=40, beds=0, value=4200000, paid=840000, year=2028, state="verified"),
    dict(id="u106", type="apartment", area="shorouk", proj=("مشروع و", "Project F"), size=169, beds=3, value=2900000, paid=580000, year=2026, state="review"),
    dict(id="u107", type="apartment", area="mostakbal", proj=("مشروع ز", "Project G"), size=113, beds=3, value=2400000, paid=480000, year=2028, state="verified"),
    dict(id="u108", type="villa", area="newcairo", proj=("مشروع ح", "Project H"), size=300, beds=5, value=12500000, paid=2500000, year=2029, state="declared"),
]


def badge(state):
    a, e = STATES[state]
    return f'<span class="badge badge-{state}">{B(a, e)}</span>'


def opp_card(u, href="opportunity.html"):
    ta, te = TYPES[u["type"]]
    aa, ae = AREAS[u["area"]]
    beds = "" if not u["beds"] else f'<span>{B(str(u["beds"]) + " غرف", str(u["beds"]) + " BR")}</span>'
    return f"""<article class="card card-hover opp" data-id="{u['id']}" data-type="{u['type']}" data-area="{u['area']}" data-state="{u['state']}" data-cash="{u['paid']}">
  <div class="opp-photo" role="img" aria-label="Photo placeholder">{B(u['proj'][0], u['proj'][1])}</div>
  <div class="opp-head"><div><h3>{B(f'{ta} {u["size"]} م² · {aa}', f'{u["size"]} m² {te} · {ae}')}</h3>
    <div class="opp-meta">{beds}<span>{B('التسليم ' + str(u['year']), 'Delivery ' + str(u['year']))}</span></div></div>{badge(u['state'])}</div>
  <div class="opp-cash"><span class="muted">{B('النقد المطلوب الآن','Cash due now')}</span><b class="num">{fmt(u['paid'])}</b></div>
  <dl class="opp-grid" style="margin:0">
    <div class="opp-stat"><dt>{B('قيمة العقد','Contract value')}</dt><dd class="num">{fmt(u['value'])}</dd></div>
    <div class="opp-stat"><dt>{B('المتبقي للمطوّر','Remaining')}</dt><dd class="num">{fmt(u['value'] - u['paid'])}</dd></div>
  </dl>
  <div class="opp-actions"><a class="btn btn-secondary" href="{href}">{B('عرض التفاصيل','View details')}</a>
    <button class="fav" type="button" data-id="{u['id']}" aria-pressed="false" data-aria-ar="إضافة للمفضلة" data-aria-en="Save to favorites">{icon('heart', 20)}</button></div>
</article>"""


# ---- page layout ----
NAV = [("sellers", "sellers.html", "للبائعين", "For sellers"), ("opportunities", "opportunities.html", "الفرص", "Opportunities"),
       ("story", "story.html", "قصتنا", "Our story"), ("how", "how-it-works.html", "كيف تعمل", "How it works"),
       ("contact", "contact.html", "تواصل", "Contact"), ("investors", "investors.html", "المستثمرون", "Investors")]


def layout(slug, key, title_ar, title_en, body, desc_en=""):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if key == k else ""}>{B(a, e)}</a>' for k, h, a, e in NAV)
    bottom = [("home", "index.html", "الرئيسية", "Home", "index"), ("list", "opportunities.html", "الفرص", "Opportunities", "opportunities"),
              ("calc", "calculator.html", "الحاسبة", "Calculator", "calculator"), ("upload", "sellers.html", "بيع وحدتك", "Sell", "sellers")]
    bnav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if key == k else ""}>{icon(i)}<span>{B(a, e)}</span></a>' for i, h, a, e, k in bottom)
    page_js = json.dumps({"ar": f"{title_ar} | OsoolExit", "en": f"{title_en} | OsoolExit"}, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title_en} | OsoolExit</title>
<meta name="description" content="{desc_en or 'Transfer an installment property contract in Egypt with verified numbers and no overprice.'}">
<link rel="icon" href="logo/app-icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="fonts/cairo.css">
<link rel="stylesheet" href="theme.css">
<link rel="stylesheet" href="assets/site.css">
<script>window.PAGE = {page_js};</script>
</head>
<body>
<a class="visually-hidden" href="#main">{B('تخطَّ إلى المحتوى','Skip to content')}</a>
<header class="site-header">
  <div class="container bar">
    <a class="brand" href="index.html" aria-label="OsoolExit">{inline_logo()}</a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="tools">
      <a class="btn btn-secondary hide-md" href="opportunities.html">{B('أريد أن أشتري','I want to buy')}</a>
      <a class="btn btn-accent hide-sm" href="sellers.html">{B('أريد أن أبيع','I want to sell')}</a>
      <button class="btn btn-ghost" id="langBtn" type="button">English</button>
      <button class="btn btn-ghost icon-btn" id="themeBtn" type="button" aria-pressed="false" data-aria-ar="الوضع الداكن" data-aria-en="Dark mode">{icon('moon', 20)}</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div><div class="brand" style="margin-bottom:var(--space-2)">{inline_logo()}</div>
        <p class="muted" style="font-size:.9rem">{B('منصة تنازل عن وحدات التقسيط في مصر، بدون أوفر برايس وبأرقام موثقة.','Egypt’s installment-unit assignment platform: no overprice, verified numbers.')}</p>
        <p style="font-size:.9rem;margin:0"><a href="mailto:{EMAIL}">{EMAIL}</a><br><span class="num" dir="ltr">{PHONE_DISPLAY}</span></p></div>
      <div><h4>{B('المنصة','Platform')}</h4><ul>
        <li><a href="opportunities.html">{B('الفرص','Opportunities')}</a></li><li><a href="calculator.html">{B('حاسبة الخروج','Exit calculator')}</a></li>
        <li><a href="sellers.html">{B('للبائعين','For sellers')}</a></li><li><a href="buyers.html">{B('للمشترين','For buyers')}</a></li></ul></div>
      <div><h4>{B('الشركة','Company')}</h4><ul>
        <li><a href="story.html">{B('قصتنا','Our story')}</a></li><li><a href="reports.html">{B('التقارير والمؤشر','Reports & index')}</a></li>
        <li><a href="how-it-works.html">{B('كيف تعمل','How it works')}</a></li><li><a href="developers.html">{B('للمطوّرين','For developers')}</a></li>
        <li><a href="investors.html">{B('علاقات المستثمرين','Investor relations')}</a></li><li><a href="faq.html">{B('الأسئلة الشائعة','FAQ')}</a></li>
        <li><a href="contact.html">{B('تواصل معنا','Contact')}</a></li></ul></div>
      <div><h4>{B('قانوني','Legal')}</h4><ul>
        <li><a href="privacy.html">{B('سياسة الخصوصية','Privacy policy')}</a></li><li><a href="terms.html">{B('شروط الاستخدام','Terms of use')}</a></li></ul>
        <h4 style="margin-top:var(--space-3)">{B('الدولة','Country')}</h4><ul><li>{B('مصر','Egypt')}</li></ul></div>
    </div>
    <p class="fine">{B('الأرقام والتقديرات المعروضة استرشادية وتعتمد على بنود كل عقد، ولا تُعد استشارة قانونية ولا وعدًا بنتيجة معينة. أصول إكزت وسيط لنقل العقود وليست المطوّر الأصلي ولا طرفًا في عقده. هذه صفحات تجريبية بمحتوى مبدئي وبانتظار المراجعة القانونية.','Figures and estimates are indicative, depend on each contract’s clauses, and are not legal advice or a promise of outcome. OsoolExit is a contract-transfer intermediary, not the original developer and not a party to its contract. These are demo pages with draft copy pending legal review.')}<br>© 2026 OsoolExit</p>
  </div>
</footer>
<div class="help-fab"><a class="btn btn-primary" href="contact.html#form">{icon('chat', 20)}<span>{B('اسألنا','Ask us')}</span></a></div>
<nav class="bottom-nav" aria-label="Mobile">{bnav}</nav>
<script src="assets/site.js"></script>
</body>
</html>
"""


def write(slug, html):
    os.makedirs(SITE, exist_ok=True)
    with open(f"{SITE}/{slug}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug + ".html")
