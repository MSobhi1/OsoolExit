from sitelib import *


def calculator():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('حاسبة الخروج','Exit calculator')}</span>
  <h1>{B('اعرف موقفك في دقيقة','Know your position in a minute')}</h1>
  <p class="lead">{B('أدخل قيمة العقد وما دفعته، وشاهد الإلغاء والتنازل جنبًا إلى جنب، مع النقد المطلوب من المشتري عند التنازل.','Enter the contract value and what you paid, and see cancellation next to transfer, plus the cash a buyer needs at transfer.')}</p>
</section>
<section class="container">{calc_box('c')}</section>
<section class="container section">
  <div class="grid-2">
    <div class="card"><h3>{B('كيف نحسب','How we calculate')}</h3>
      {checks([('المسترد عند الإلغاء = المدفوع − (قيمة العقد × نسبة الخصم)، ولا يقل عن صفر.','Refund on cancel = paid − (contract value × deduction %), never below zero.'),
               ('المسترد عبر التنازل = المدفوع، لأن الأوفر برايس غير مسموح.','Recovered by transfer = paid, because overprice is not allowed.'),
               ('عمولة المشتري = قيمة العقد × النسبة، وتُستحق بعد إتمام التنازل.','Buyer commission = contract value × rate, due after the transfer completes.'),
               ('النقد المطلوب من المشتري = المدفوع + العمولة + رسوم نقل المطوّر.','Buyer cash needed = paid + commission + developer transfer fee.')])}</div>
    <div class="card"><h3>{B('تنبيهات','Caveats')}</h3>
      <p class="muted">{B('الأرقام استرشادية. نسب الخصم وشروط الاسترداد ورسوم النقل تختلف من عقد لآخر ومن مطوّر لآخر، والتنازل يحتاج موافقة المطوّر. نتحقق من أرقامك الفعلية على عقدك قبل أي خطوة.','Figures are indicative. Deduction rates, refund terms and transfer fees differ by contract and developer, and a transfer needs developer approval. We check your actual numbers against your contract before any step.')}</p>
      <a class="btn btn-accent" href="sellers.html">{B('قيّم عقدي مجانًا','Assess my contract free')}{arrow()}</a></div>
  </div>
</section>"""
    return layout("calculator", "calculator", "حاسبة الخروج", "Exit calculator", body)


def how():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('كيف تعمل','How it works')}</span>
  <h1>{B('من التقييم إلى التنازل الرسمي','From assessment to the official transfer')}</h1>
  <p class="lead">{B('خطوات واضحة للبائع وللمشتري، ومعك مدير حالة في كل مرحلة.','Clear steps for the seller and the buyer, with a case manager at every stage.')}</p>
</section>

<section class="container">
  <div class="grid-2">
    <div class="card"><h2 style="font-size:1.3rem">{B('للبائع','For the seller')}</h2>
      <ol class="stack" style="padding-inline-start:20px;margin:0">
        <li><b>{B('قيّم عقدك','Assess your contract')}</b><br><span class="muted">{B('أدخل بيانات العقد وشاهد الإلغاء مقابل التنازل.','Enter the contract facts and see cancellation versus transfer.')}</span></li>
        <li><b>{B('ارفع المستندات','Upload documents')}</b><br><span class="muted">{B('العقد وإيصالات الدفع، وتبقى خاصة بك.','The contract and payment receipts, kept private to you.')}</span></li>
        <li><b>{B('مراجعة بشرية','Human review')}</b><br><span class="muted">{B('نطابق الأرقام مع كشف المطوّر ونطلب أي نقص.','We reconcile the numbers with the developer statement and ask for anything missing.')}</span></li>
        <li><b>{B('نجد المشتري','We find the buyer')}</b><br><span class="muted">{B('إعلان عام أو بيع خاص لمشترين محددين.','A public listing or a private sale to chosen buyers.')}</span></li>
        <li><b>{B('التنازل الرسمي','The official transfer')}</b><br><span class="muted">{B('عرض ثم اتفاق ثم إجراءات المطوّر، وتستلم أموالك عند الإتمام.','Offer, agreement, then developer procedures; you are paid when it completes.')}</span></li>
      </ol></div>
    <div class="card"><h2 style="font-size:1.3rem">{B('للمشتري','For the buyer')}</h2>
      <ol class="stack" style="padding-inline-start:20px;margin:0">
        <li><b>{B('سجّل ميزانيتك','Register your budget')}</b><br><span class="muted">{B('النقد المتاح والقسط المريح والمناطق المفضلة.','Available cash, comfortable installment and preferred areas.')}</span></li>
        <li><b>{B('تصلك الفرص المناسبة','Matching opportunities reach you')}</b><br><span class="muted">{B('كل فرصة بأرقام موثقة وحالة تحقق واضحة.','Each with verified numbers and a clear verification state.')}</span></li>
        <li><b>{B('احجز وحدتك','Reserve your unit')}</b><br><span class="muted">{B('اسأل البائع عبر المنصة وحدد جاهزيتك.','Ask the seller through the platform and state your readiness.')}</span></li>
        <li><b>{B('التنازل الرسمي والدفع','Official transfer and payment')}</b><br><span class="muted">{B('نرافقك حتى موافقة المطوّر، وتُستحق العمولة بعد الإتمام فقط.','We stay with you through developer approval; the commission is due after completion only.')}</span></li>
      </ol></div>
  </div>
</section>

<section class="band section">
  <div class="container grid-2">
    <div><h2>{B('ما الذي تحتاجه؟','What will you need?')}</h2>
      {checks([('نسخة من عقد الحجز أو التعاقد','A copy of the reservation or purchase contract'),('إيصالات كل الدفعات','Receipts for every payment'),('كشف حساب المطوّر إن توفر','The developer statement, if available'),('بطاقة الهوية لإتمام التنازل','ID for the transfer itself')])}</div>
    <div><h2>{B('كم يكلّف؟','What does it cost?')}</h2>
      <table class="compare"><tbody>
        <tr><th scope="row">{B('البائع','Seller')}</th><td class="num">0%</td></tr>
        <tr><th scope="row">{B('المشتري (قيمة تجريبية)','Buyer (demo value)')}</th><td class="num">0.5%</td></tr>
        <tr><th scope="row">{B('رسوم نقل المطوّر','Developer transfer fees')}</th><td>{B('تُعرض منفصلة، وتختلف من مطوّر لآخر','Shown separately; differ by developer')}</td></tr>
      </tbody></table>
      <p class="muted" style="font-size:.85rem;margin-top:var(--space-2)">{B('المدة تختلف حسب المطوّر واكتمال المستندات، ولا نعد بمدة محددة.','Timing depends on the developer and on complete documents; we do not promise a fixed duration.')}</p></div>
  </div>
</section>
<section class="container section">
  <div class="cta-row" style="margin-top:0"><a class="btn btn-accent" href="sellers.html">{B('أريد أن أبيع','I want to sell')}{arrow()}</a><a class="btn btn-secondary" href="buyers.html">{B('أريد أن أشتري','I want to buy')}</a></div>
</section>"""
    return layout("how-it-works", "how", "كيف تعمل", "How it works", body)


def story():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('قصتنا','Our story')}</span>
  <h1>{B('لأن الخروج من عقد لا يجب أن يعني خسارة جزء من أموالك','Because leaving a contract should not mean losing part of your money')}</h1>
  <p class="notice">{B('نص مبدئي: استبدله بقصتكم الحقيقية وأسماء الفريق.','Draft copy: replace with your real story and team names.')}</p>
</section>
<section class="container">
  <div class="grid-3">
    {feature('clock','المشكلة','The problem','كثيرون يشترون على الأقساط ثم تتغير ظروفهم. الإلغاء يعني خصمًا وانتظارًا، وإعادة البيع المعتادة تعني أوفر برايس وسماسرة.','Many buy on installments and then their circumstances change. Cancelling means a deduction and a wait, and normal resale means overprice and brokers.')}
    {feature('shield','ما نفعله','What we do','نجمع بين من يريد الخروج بما دفعه ومن يريد وحدة بسعر العقد القديم، بأرقام موثقة وإجراءات رسمية.','We connect someone who wants out at what they paid with someone who wants a unit at the older price, with verified numbers and official procedures.')}
    {feature('scale','وعدنا','Our commitment','لا ننشر قبل المراجعة، ولا نسمّي رقمًا موثقًا بدون دليل، ولا نضغط على أحد.','We do not publish before review, call a number verified without evidence, or pressure anyone.')}
  </div>
</section>
<section class="container section">
  <h2>{B('مبادئ نلتزم بها','Principles we hold ourselves to')}</h2>
  {checks([('البائع لا يدفع عمولة، والمشتري يدفع بعد إتمام التنازل فقط.','The seller pays no commission; the buyer pays only after the transfer completes.'),
           ('لكل رقم حالة: معلن، قيد المراجعة، موثق، أو غير معروف. رفع ملف لا يعني توثيقه.','Every number has a state: declared, in review, verified or unknown. Uploading a file is not verification.'),
           ('المستندات خاصة، ولا تُشارك إلا بإذن محدد.','Documents are private and shared only with a specific permission.'),
           ('نعرض لك كل الخيارات، حتى لو كان الأفضل ألا تتنازل.','We show every option, even when not transferring is best.')])}
  <div class="cta-row"><a class="btn btn-primary" href="how-it-works.html">{B('كيف تعمل','How it works')}{arrow()}</a><a class="btn btn-secondary" href="contact.html">{B('تواصل معنا','Contact us')}</a></div>
</section>"""
    return layout("story", "story", "قصتنا", "Our story", body)


FAQ = [
    (("عام", "General"), [
        (("ما هو التنازل عن وحدة؟", "What is a unit transfer (tanazol)?"), ("هو نقل حقوقك والتزاماتك في عقد الوحدة إلى مشترٍ آخر بموافقة المطوّر، فيكمل المشتري الأقساط.", "It moves your rights and obligations under the unit contract to another buyer with the developer’s approval, and the buyer continues the installments.")),
        (("ما الفرق بينه وبين الإلغاء؟", "How is it different from cancelling?"), ("عند الإلغاء قد يخصم المطوّر نسبة من المبلغ ويرد الباقي وفق العقد. في التنازل قد تسترد ما دفعته إن وُجد مشترٍ ووافق المطوّر. الأرقام تختلف من عقد لآخر.", "On cancellation the developer may deduct a percentage and refund the rest under the contract. With a transfer you may recover what you paid if a buyer is found and the developer approves. Numbers differ by contract.")),
        (("ما معنى بدون أوفر برايس؟", "What does no overprice mean?"), ("لا يزيد المبلغ المطلوب من البائع عن المبلغ الموثق الذي دفعه فعلًا. للبائع أن يقبل أقل بإرادته.", "The amount the seller asks never exceeds the verified amount they actually paid. A seller may voluntarily accept less.")),
    ]),
    (("للبائعين", "Sellers"), [
        (("هل أدفع أي رسوم؟", "Do I pay any fees?"), ("لا عمولة على البائع. قد توجد رسوم من المطوّر على النقل، وتُعرض منفصلة.", "There is no seller commission. The developer may charge transfer fees, shown separately.")),
        (("هل سيُعلن عن وحدتي علنًا؟", "Will my unit be advertised publicly?"), ("فقط إن اخترت الإعلان العام. يمكنك اختيار البيع الخاص لمشترين محددين.", "Only if you choose a public listing. You can choose a private sale to chosen buyers.")),
        (("ماذا لو رفض المطوّر التنازل؟", "What if the developer refuses the transfer?"), ("موافقة المطوّر شرط للتنازل الرسمي. نراجع عقدك مبكرًا لنخبرك بما هو متوقع، ونعرض عليك البدائل.", "Developer approval is required for an official transfer. We review your contract early to tell you what to expect, and we show you the alternatives.")),
        (("كم تستغرق العملية؟", "How long does it take?"), ("تعتمد على المطوّر واكتمال المستندات ووجود المشتري المناسب، ولا نعد بمدة محددة.", "It depends on the developer, complete documents and finding the right buyer; we do not promise a fixed time.")),
    ]),
    (("للمشترين", "Buyers"), [
        (("متى أدفع العمولة؟", "When do I pay the commission?"), ("بعد إتمام التنازل فقط. النسبة المعروضة حاليًا تجريبية.", "Only after the transfer completes. The rate shown is currently a demo value.")),
        (("ماذا يعني موثّق وقيد المراجعة؟", "What do Verified and In review mean?"), ("موثّق: راجعنا الرقم مع المستندات. قيد المراجعة: لم تكتمل المراجعة بعد. معلن: ذكره البائع ولم نتحقق منه.", "Verified: we checked the number against documents. In review: not yet complete. Declared: stated by the seller and not yet checked.")),
        (("هل سعر السوق المعروض تقييم منكم؟", "Is the market price shown a valuation by you?"), ("لا. هو تقدير المالك، وعليك التحقق منه قبل القرار.", "No. It is the owner’s estimate, and you should check it before deciding.")),
    ]),
    (("الخصوصية", "Privacy"), [
        (("من يرى مستنداتي؟", "Who sees my documents?"), ("أنت وفريق المراجعة فقط. لا يراها مشترٍ إلا بإذن محدد منك.", "You and the review team only. No buyer sees them without a specific permission from you.")),
    ]),
]


def faq():
    groups = ""
    for (ga, ge), items in FAQ:
        qs = "".join(f"<details><summary><span>{B(*q)}</span></summary><div>{B(*a)}</div></details>" for q, a in items)
        groups += f'<div class="faq-group"><h2 style="font-size:1.25rem">{B(ga, ge)}</h2>{qs}</div>'
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('الأسئلة الشائعة','FAQ')}</span>
  <h1>{B('أسئلة يسألها الناس قبل أن يبدأوا','Questions people ask before they start')}</h1>
  <p class="notice">{B('إجابات مبدئية بانتظار المراجعة القانونية.','Draft answers pending legal review.')}</p>
</section>
<section class="container faq">{groups}
  <div class="panel-cta" style="margin-top:var(--space-5)"><h3>{B('لم تجد سؤالك؟','Did not find your question?')}</h3>
    <a class="btn btn-accent" href="contact.html#form">{B('اسألنا','Ask us')}{arrow()}</a></div>
</section>"""
    return layout("faq", "faq", "الأسئلة الشائعة", "FAQ", body)


def contact():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('تواصل معنا','Contact')}</span>
  <h1>{B('نرد عليك بسرعة','We reply quickly')}</h1>
  <p class="notice">{B('بيانات التواصل أدناه أمثلة مؤقتة.','The contact details below are temporary placeholders.')}</p>
</section>
<section class="container detail" id="form">
  <div class="card">
    <form data-demo class="form-grid">
      {field('c-name','الاسم','Full name','text',('','') ,True)}
      {field('c-wa','رقم واتساب','WhatsApp number','tel',('+20 …','+20 …') ,True,None,'ltr')}
      {select('c-topic','الموضوع','Topic',[('sell','أريد أن أبيع','I want to sell'),('buy','أريد أن أشتري','I want to buy'),('dev','أنا مطوّر','I am a developer'),('inv','استثمار','Investment'),('other','آخر','Other')],False,True)}
      {textarea('c-msg','رسالتك','Your message','', required=True)}
      {consent('c-ok','أوافق على التواصل معي بخصوص رسالتي.','I agree to be contacted about my message.')}
      <div class="full"><button class="btn btn-primary" type="submit">{B('إرسال','Send')}</button></div>
    </form>
    {ok_msg()}
  </div>
  <aside class="card stack">
    <h3>{B('قنوات أخرى','Other channels')}</h3>
    <p style="margin:0"><b>{B('واتساب','WhatsApp')}</b><br><span class="num" dir="ltr">{PHONE_DISPLAY}</span></p>
    <p style="margin:0"><b>{B('البريد','Email')}</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p style="margin:0"><b>{B('مواعيد الرد','Reply hours')}</b><br><span class="muted">{B('يحدد لاحقًا','To be set')}</span></p>
  </aside>
</section>"""
    return layout("contact", "contact", "تواصل معنا", "Contact", body)


def developers():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('للمطوّرين','For developers')}</span>
  <h1>{B('بديل منظّم للإلغاء داخل مشروعك','An organized alternative to cancellation inside your project')}</h1>
  <p class="lead">{B('حين يريد عميل الخروج، ننقل عقده إلى مشترٍ جاد وفق إجراءات شركتك، بدل أن تعود الوحدة وتبدأ الدورة من جديد.','When a customer wants out, we move the contract to a serious buyer following your company’s procedures, instead of the unit coming back and the cycle starting over.')}</p>
  <p class="notice">{B('نص مبدئي بانتظار مراجعتكم.','Draft copy pending your review.')}</p>
</section>
<section class="container">
  <div class="grid-3">
    {feature('doc','ملفات منظمة','Organized files','نسلّم لك ملف تنازل مراجَعًا بالمستندات والأرقام.','We hand you a reviewed transfer file with documents and figures.')}
    {feature('shield','مشترون جادون','Serious buyers','نعرّف مشترين ببياناتهم وجاهزيتهم قبل الوصول إليك.','We introduce buyers with their details and readiness before they reach you.')}
    {feature('building','وفق إجراءاتك','Your procedures','نلتزم بنموذج التنازل ورسومه كما تحددها شركتك.','We follow your transfer form and fees as your company defines them.')}
  </div>
</section>
<section class="container section" id="form">
  <h2>{B('ابدأ شراكة','Start a partnership')}</h2>
  <div class="card"><form data-demo class="form-grid">
    {field('d-co','اسم الشركة','Company name','text',('','') ,True)}
    {field('d-name','اسم المسؤول','Contact person','text',('','') ,True)}
    {field('d-mail','البريد الإلكتروني','Email','email',('','') ,True,None,'ltr')}
    {field('d-wa','الهاتف','Phone','tel',('+20 …','+20 …'),False,None,'ltr')}
    {textarea('d-msg','عن مشروعاتكم وإجراءات التنازل','About your projects and transfer procedures')}
    <div class="full"><button class="btn btn-primary" type="submit">{B('إرسال','Send')}</button></div>
  </form>{ok_msg()}</div>
</section>"""
    return layout("developers", "developers", "للمطوّرين", "For developers", body)


def investors():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('علاقات المستثمرين','Investor relations')}</span>
  <h1>{B('سوق ثانوي منظّم لعقود التقسيط','An organized secondary market for installment contracts')}</h1>
  <p class="notice">{B('نص مبدئي بلا أرقام: أضف المؤشرات الحقيقية قبل النشر.','Draft copy with no figures: add real metrics before publishing.')}</p>
</section>
<section class="container">
  <div class="grid-3">
    {feature('coins','نموذج الإيراد','Revenue model','البائع مجانًا، وعمولة على المشتري عند إتمام كل تنازل.','Free for the seller, with a buyer commission on each completed transfer.')}
    {feature('shield','قيمة التحقق','The value of verification','مراجعة بشرية وحالات تحقق لكل رقم تبني الثقة.','Human review and a verification state for every number build trust.')}
    {feature('building','شراكات المطوّرين','Developer partnerships','مسارات تنازل جاهزة مع المطوّرين تقلل الاحتكاك.','Ready transfer paths with developers reduce friction.')}
  </div>
</section>
<section class="container section" id="form">
  <h2>{B('تحدث معنا','Talk to us')}</h2>
  <div class="card"><form data-demo class="form-grid">
    {field('i-name','الاسم','Full name','text',('','') ,True)}
    {field('i-mail','البريد الإلكتروني','Email','email',('','') ,True,None,'ltr')}
    {textarea('i-msg','نبذة عن اهتمامك','About your interest')}
    <div class="full"><button class="btn btn-primary" type="submit">{B('إرسال','Send')}</button></div>
  </form>{ok_msg()}</div>
</section>"""
    return layout("investors", "investors", "المستثمرون", "Investors", body)


def reports():
    by_area = {}
    for u in UNITS:
        by_area[u["area"]] = by_area.get(u["area"], 0) + 1
    top = max(by_area.values())
    bars = "".join(f'<div class="bar-row"><span>{B(*AREAS[k])}</span><div class="track"><div class="fill" style="width:{100 * n // top}%"></div></div><b>{n}</b></div>'
                   for k, n in sorted(by_area.items(), key=lambda x: -x[1]))
    states = {s: sum(1 for u in UNITS if u["state"] == s) for s in STATES}
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('التقارير والمؤشر','Reports & index')}</span>
  <h1>{B('صورة السوق من بيانات المنصة','A market view from platform data')}</h1>
  <p class="notice">{B('بيانات تجريبية: الأعداد أدناه محسوبة من الوحدات الخيالية في الصفحة التجريبية فقط.','Demo data: the counts below are computed from the fictional demo units only.')}</p>
</section>
<section class="container"><div class="grid-2">
  <div class="card"><h3>{B('الوحدات حسب المنطقة','Units by area')}</h3>{bars}</div>
  <div class="card"><h3>{B('الوحدات حسب حالة التحقق','Units by verification state')}</h3>
    <table class="pay-table">{''.join(f'<tr><td>{badge(s)}</td><td>{n}</td></tr>' for s, n in states.items())}</table></div>
</div></section>"""
    return layout("reports", "reports", "التقارير والمؤشر", "Reports & index", body)


def _legal(slug, ar, en, items):
    secs = "".join(f"<h2 style='font-size:1.2rem;margin-top:var(--space-4)'>{B(*h)}</h2><p>{B(*p)}</p>" for h, p in items)
    body = f"""
<section class="container page-hero"><h1>{B(ar, en)}</h1>
  <p class="notice">{B('مسودة بانتظار المراجعة القانونية. لا تُعد نصًا نهائيًا.','Draft pending legal review. Not final text.')}</p></section>
<section class="container section" style="max-width:820px;padding-top:0">{secs}</section>"""
    return layout(slug, "legal", ar, en, body)


def privacy():
    return _legal("privacy", "سياسة الخصوصية", "Privacy policy", [
        (("ما نجمعه", "What we collect"), ("بيانات الاتصال وبيانات العقد والمستندات التي ترفعها بنفسك.", "Contact details, contract data and the documents you upload yourself.")),
        (("كيف نستخدمه", "How we use it"), ("لمراجعة طلبك والتواصل معك ومطابقتك بالمشترين أو الوحدات المناسبة.", "To review your request, contact you and match you with suitable buyers or units.")),
        (("المشاركة", "Sharing"), ("لا تُشارك مستنداتك مع أي مشترٍ إلا بإذن محدد منك.", "Your documents are not shared with any buyer without a specific permission from you.")),
        (("حقوقك", "Your rights"), ("يمكنك طلب الاطلاع على بياناتك أو تصحيحها أو حذفها عبر التواصل معنا.", "You can ask to access, correct or delete your data by contacting us.")),
    ])


def terms():
    return _legal("terms", "شروط الاستخدام", "Terms of use", [
        (("طبيعة الخدمة", "Nature of the service"), ("OsoolExit وسيط لنقل العقود وليست المطوّر الأصلي ولا طرفًا في عقده.", "OsoolExit is a contract-transfer intermediary, not the original developer and not a party to its contract.")),
        (("الأرقام", "Figures"), ("الأرقام والتقديرات استرشادية وتعتمد على بنود كل عقد، ولا تُعد استشارة قانونية.", "Figures and estimates are indicative, depend on each contract’s clauses, and are not legal advice.")),
        (("موافقة المطوّر", "Developer approval"), ("إتمام التنازل مشروط بموافقة المطوّر وإجراءاته.", "Completing a transfer is subject to the developer’s approval and procedures.")),
        (("الرسوم", "Fees"), ("لا عمولة على البائع. تُستحق عمولة المشتري بعد إتمام التنازل، والرسوم الأخرى تُعرض منفصلة.", "No seller commission. The buyer commission is due after the transfer completes; other fees are shown separately.")),
    ])
