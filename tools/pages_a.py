from sitelib import *


def home():
    units = "".join(opp_card(u) for u in UNITS[:3])
    body = f"""
<section class="container hero">
  <div>
    <span class="eyebrow">{B('منصة التنازل عن وحدات التقسيط في مصر','Egypt’s installment-unit assignment platform')}</span>
    <h1>{B('اخرج بما دفعته فعلًا. واشترِ بسعر العقد الأصلي.','Exit with what you paid. Buy at the original price.')}</h1>
    <p class="lead">{B('إن لم تعد قادرًا على الاستمرار في الأقساط، انقل وحدتك إلى مشترٍ جاد بدون أوفر برايس بدل أن تخسر جزءًا من أموالك عند الإلغاء. وإن كنت تبحث عن وحدة، تعاقد بسعر قديم وأكمل الأقساط. كل رقم موثق من المستندات، ونرافقك حتى التنازل الرسمي.','If you can no longer keep up with installments, transfer your unit to a serious buyer with no overprice instead of losing part of your money on cancellation. If you are looking for a unit, take over at an older price and continue the installments. Every figure is checked against documents, and we stay with you until the official transfer.')}</p>
    <div class="cta-row">
      <a class="btn btn-accent" href="sellers.html">{B('بيع وحدتك','Sell your unit')}{arrow()}</a>
      <a class="btn btn-secondary" href="opportunities.html">{B('تصفح الفرص','Browse opportunities')}</a>
    </div>
    <p class="muted" style="margin-top:var(--space-3)">{B('للبائع: بدون عمولة. للمشتري: أرقام موثقة قبل أن تدفع أي مبلغ.','Sellers: no commission. Buyers: verified numbers before you pay anything.')}</p>
  </div>
  <aside class="hero-card" aria-label="Example">
    <h3>{B('الإلغاء مقابل التنازل','Cancel vs. transfer')}</h3>
    <div class="row"><span>{B('إجمالي العقد','Contract total')}</span><b class="num">6,000,000</b></div>
    <div class="row"><span>{B('المدفوع حتى الآن','Paid so far')}</span><b class="num">1,200,000</b></div>
    <div class="row"><span>{B('المسترد عند الإلغاء (خصم 15%)','Refund on cancel (15% deduction)')}</span><b class="num">300,000</b></div>
    <div class="row"><span>{B('المسترد عبر التنازل','Recovered by transfer')}</span><b class="num gain">1,200,000</b></div>
    <small>{B('مثال توضيحي. نسب الخصم وشروط الاسترداد تختلف من عقد لآخر.','Illustrative example. Deduction rates and refund terms differ by contract.')}</small>
  </aside>
</section>

<section class="container" aria-label="Fees at a glance">{trust_strip()}</section>

<section class="container section">
  <h2>{B('طرف يريد الخروج وطرف يبحث عن فرصة. نحن نجمع بينهما.','One side needs out, the other wants in. We connect them.')}</h2>
  <p class="lead">{B('هذا ليس إعادة بيع عادية: الأوفر برايس ممنوع. يسترد البائع ما دفعه، ويحصل المشتري على سعر العقد القديم.','This is not normal resale: overprice is not allowed. The seller recovers what they paid, and the buyer gets the older contract price.')}</p>
  <div class="grid-2" style="margin-top:var(--space-4)">
    <div class="card"><h3>{B('للبائع صاحب الوحدة','For the unit owner')}</h3>
      {checks([('استرد ما دفعته نقدًا عند إتمام التنازل','Recover what you paid, in cash, when the transfer completes'),
               ('بلا إعلان عام ولا اتصالات سماسرة إن اخترت البيع الخاص','No public listing or broker calls if you choose a private sale'),
               ('نجهّز ملف التنازل معك ونتابع حتى التوقيع','We prepare the file with you and follow through to signing')])}
      <p class="muted" style="margin-top:var(--space-3)">{B('مجاني للبائع: لا نأخذ منه أي عمولة.','Free for the seller: we take no commission from you.')}</p>
      <a class="btn btn-primary" href="sellers.html">{B('أدرج وحدتك للتنازل','List your unit for transfer')}{arrow()}</a></div>
    <div class="card"><h3>{B('للمشتري','For the buyer')}</h3>
      {checks([('سعر العقد القديم كما هو، بلا أوفر برايس','The older contract price as it is, with no overprice'),
               ('العقد والمدفوعات والمتبقي موثقة قبل أن ترى الفرصة','Contract, payments and balance checked before you see the opportunity'),
               ('تنازل رسمي بموافقة المطوّر، لا توكيلات ولا وعود','An official, developer-approved transfer, not powers of attorney and promises')])}
      <p class="muted" style="margin-top:var(--space-3)">{B('عمولة المشتري تُستحق فقط بعد إتمام التنازل.','The buyer commission is due only after the transfer completes.')}</p>
      <a class="btn btn-primary" href="opportunities.html">{B('اطّلع على الفرص','See opportunities')}{arrow()}</a></div>
  </div>
</section>

<section class="band section">
  <div class="container">
    <h2>{B('كيف نختلف عن إعادة البيع المعتادة؟','How are we different from normal resale?')}</h2>
    <table class="compare">
      <thead><tr><th></th><th>{B('إعادة البيع المعتادة','Normal resale')}</th><th class="col-win">OsoolExit</th></tr></thead>
      <tbody>
        <tr><th scope="row">{B('السعر','Price')}</th><td>{B('أوفر برايس فوق السعر، مضخّم للمساومة','Overprice on top, inflated for haggling')}</td><td class="col-win">{B('بلا أوفر: السعر هو ما دُفع فعلًا، بإيصالات','No overprice: the price is what was actually paid, with receipts')}</td></tr>
        <tr><th scope="row">{B('الأرقام','The numbers')}</th><td>{B('كلام بائع أو سمسار بلا إثبات','Seller or broker claims with no evidence')}</td><td class="col-win">{B('العقد والمدفوعات والرصيد تُراجع مع المستندات','Contract, payments and balance reconciled against documents')}</td></tr>
        <tr><th scope="row">{B('الإجراءات','The process')}</th><td>{B('يعرّفك السمسار ثم تُترك وحدك','A broker introduces you, then you are on your own')}</td><td class="col-win">{B('نرافقك في كل خطوة حتى التوقيع والدفع','We walk each step with you until signing and payment')}</td></tr>
        <tr><th scope="row">{B('الرسوم','Fees')}</th><td>{B('عمولات من الطرفين وتكاليف مفاجئة','Commissions from both sides and surprises')}</td><td class="col-win">{B('مجاني للبائع، والمشتري يدفع بعد إتمام التنازل فقط','Free for the seller; the buyer pays only after the transfer completes')}</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="container section">
  <h2>{B('مثال بأرقام حقيقية الشكل','An example with real-looking numbers')}</h2>
  <p class="muted">{B('عقد بقيمة 10 ملايين جنيه، دفع المالك منها 2 مليون على 3 سنوات ولم يعد قادرًا على الاستمرار.','A 10M EGP contract. The owner paid 2M over 3 years and can no longer continue.')}</p>
  <div class="grid-2">
    <div class="card"><h3>{B('إعادة الوحدة للمطوّر','Returning the unit to the developer')}</h3>
      <table class="pay-table"><tr><td>{B('خصم الإلغاء (15% من إجمالي العقد)','Cancellation deduction (15% of total)')}</td><td class="num" style="color:var(--danger-fg)">1,500,000</td></tr>
      <tr><td>{B('ما يعود للمالك','What returns to the owner')}</td><td class="num">500,000</td></tr>
      <tr><td>{B('موعد الاسترداد','When')}</td><td>{B('حسب العقد، قد يمتد لسنوات','Per contract, may take years')}</td></tr></table></div>
    <div class="card" style="border-color:var(--primary)"><h3>{B('التنازل عبر OsoolExit','Transferring through OsoolExit')}</h3>
      <table class="pay-table"><tr><td>{B('يسترد المالك ما دفعه','Owner recovers what they paid')}</td><td class="num" style="color:var(--verified-fg)">2,000,000</td></tr>
      <tr><td>{B('عمولة المنصة على البائع','Platform fee for the seller')}</td><td class="num">0</td></tr>
      <tr><td>{B('موعد الاسترداد','When')}</td><td>{B('نقدًا عند إتمام التنازل','Cash when the transfer completes')}</td></tr></table></div>
  </div>
  <p class="muted" style="font-size:.85rem;margin-top:var(--space-2)">{B('مثال توضيحي. تختلف نسب الخصم وشروط الاسترداد من عقد لآخر، وهذا ما يفحصه تقرير الخروج المجاني.','Illustrative example. Deduction rates and refund terms differ by contract; that is what the free exit report checks.')}</p>
</section>

<section class="band section">
  <div class="container">
    <h2>{B('خمس خطوات واضحة','Five clear steps')}</h2>
    {stepper([('قيّم عقدك','Assess your contract'),('ارفع مستنداتك','Upload documents'),('نجهّز فرصتك','We prepare your listing'),('نجد المشتري','We find your buyer'),('التنازل الرسمي','The official transfer')])}
    <a class="btn btn-secondary" href="how-it-works.html">{B('التفاصيل الكاملة','Full details')}{arrow()}</a>
  </div>
</section>

<section class="container section">
  <h2>{B('معيارنا للخروج العادل','Our fair-exit standard')}</h2>
  <div class="grid-4">
    {feature('doc','لكل رقم مصدر','Every number has a source','نوضح ما هو موثق من المستندات وما هو تقديري.','We show what is document-verified and what is estimated.')}
    {feature('coins','مجاني للبائع','Free for sellers','بلا عمولة على البائع. المشتري يدفع بعد إتمام التنازل فقط.','No commission on the seller. The buyer pays only after the transfer completes.')}
    {feature('lock','خصوصيتك محفوظة','Your privacy is protected','اختر البيع الخاص: بلا إعلان عام ولا اتصالات غير مرغوبة.','Choose a private sale: no public listing, no unwanted calls.')}
    {feature('scale','بلا ضغط','No pressure','نعرض لك كل الخيارات، حتى لو كان الأفضل أن تحتفظ بعقدك.','We show you every option, even when keeping your contract is best.')}
  </div>
</section>

<section class="band section">
  <div class="container">
    <h2>{B('اعرف موقفك في دقيقة','Know your position in a minute')}</h2>
    <p class="muted">{B('أدخل قيمة العقد وما دفعته، وشاهد الإلغاء والتنازل جنبًا إلى جنب.','Enter the contract value and what you paid, and see cancellation next to transfer.')}</p>
    {calc_box('h', compact=True)}
    <a class="btn btn-secondary" href="calculator.html" style="margin-top:var(--space-3)">{B('الحاسبة الكاملة','Full calculator')}{arrow()}</a>
  </div>
</section>

<section class="container section">
  <h2>{B('فرص منشورة','Published opportunities')} <span class="tag-demo">{B('(بيانات تجريبية)','(demo data)')}</span></h2>
  <div class="opps">{units}</div>
  <p style="margin-top:var(--space-3)"><a class="btn btn-secondary" href="opportunities.html">{B('كل الفرص','All opportunities')}{arrow()}</a></p>
</section>

<section class="container section">
  <div class="grid-2">
    <div class="panel-cta"><h3>{B('تتعثر في الأقساط؟','Struggling with installments?')}</h3>
      <p>{B('لا تتعجل الإلغاء. اعرف موقفك أولًا. التقييم مجاني وبلا التزام.','Do not rush into cancellation. Know your position first. The assessment is free with no obligation.')}</p>
      <a class="btn btn-accent" href="sellers.html">{B('قيّم عقدي','Assess my contract')}{arrow()}</a></div>
    <div class="panel-cta"><h3>{B('تبحث عن فرصة حقيقية؟','Looking for a genuine opportunity?')}</h3>
      <p>{B('سجّل ميزانيتك وسنرسل لك الفرص التي تناسب النقد المتاح لديك والقسط المريح.','Register your budget and we will send opportunities that fit your available cash and comfortable installment.')}</p>
      <a class="btn btn-secondary" href="buyers.html">{B('سجّل كمشترٍ','Register as a buyer')}{arrow()}</a></div>
  </div>
</section>"""
    return layout("index", "home", "الرئيسية", "Home", body)


def sellers():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('للبائعين','For sellers')}</span>
  <h1>{B('لا تخسر جزءًا من أموالك بالإلغاء','Do not lose part of your money to cancellation')}</h1>
  <p class="lead">{B('قيّم عقدك مجانًا، وشاهد ما ستسترده عند الإلغاء وما ستسترده عند التنازل. نجهّز لك الملف ونتابع حتى استلام أموالك.','Assess your contract for free and see what you would get back by cancelling versus transferring. We prepare the file and follow through until you are paid.')}</p>
</section>

<section class="container">
  <div class="grid-3">
    {feature('coins','استرد ما دفعته','Recover what you paid','السعر هو المبلغ المدفوع فعلًا، بلا أوفر برايس، وهذا ما يجعل وحدتك أسرع عرض في السوق.','The price is the amount actually paid, with no overprice, which makes your unit the most attractive offer.')}
    {feature('eyeoff','بيع خاص إن أردت','Private sale if you prefer','بلا إعلان عام وبلا اتصالات. نعرض الوحدة على مشترين محددين فقط.','No public listing and no calls. We show the unit only to chosen buyers.')}
    {feature('shield','مجاني بلا ضغط','Free, no pressure','لا عمولة على البائع. ونخبرك إن كان الأفضل أن تحتفظ بعقدك.','No seller commission. And we tell you if keeping your contract is the better option.')}
  </div>
</section>

<section class="container section" id="assess">
  <h2>{B('قيّم عقدك','Assess your contract')}</h2>
  <p class="muted">{B('خمس خطوات قصيرة. هذا نموذج تجريبي لا يرسل بيانات.','Five short steps. This is a demo form that sends no data.')}</p>
  <div class="card wizard" data-wizard>
    {stepper([('الأهلية','Eligibility'),('بيانات الوحدة','Unit details'),('العقد والدفعات','Contract & payments'),('المستندات والخصوصية','Documents & privacy'),('المراجعة','Review')])}
    <form data-demo>
      <section class="wizard-panel form-grid">
        {select('s-contract','حالة العقد','Contract status',[('active','ساري ومنتظم','Active and up to date'),('late','متأخر في بعض الأقساط','Behind on some installments'),('notice','وصلني إنذار من المطوّر','I received a developer notice')],True,True)}
        {field('s-dev','اسم المطوّر','Developer name','text',('مثال: اسم الشركة','e.g. company name'),True)}
        {select('s-why','سبب الرغبة في الخروج','Why do you want to exit',[('cash','ضغط مالي','Financial pressure'),('change','تغيّرت خططي','My plans changed'),('other','سبب آخر','Something else')])}
      </section>
      <section class="wizard-panel form-grid">
        {field('s-proj','اسم المشروع','Project name','text',('','') ,True)}
        {select('s-type','نوع الوحدة','Unit type',[('apartment','شقة','Apartment'),('villa','فيلا','Villa'),('shop','محل','Shop')])}
        {field('s-size','المساحة (م²)','Area (m²)','money',('','') ,True)}
        {select('s-area','المنطقة','Area',[(k, a, e) for k, (a, e) in AREAS.items()])}
      </section>
      <section class="wizard-panel form-grid">
        {field('s-value','قيمة العقد (جنيه)','Contract value (EGP)','money',('','') ,True)}
        {field('s-paid','المدفوع حتى الآن (جنيه)','Paid so far (EGP)','money',('','') ,True)}
        {field('s-next','القسط القادم (جنيه)','Next installment (EGP)','money')}
        {field('s-date','موعد القسط القادم','Next installment date','date')}
      </section>
      <section class="wizard-panel">
        <div class="upload-row"><span><b>{B('العقد','Contract')}</b><br><span class="muted fname"></span></span><input type="file"></div>
        <div class="upload-row"><span><b>{B('إيصالات الدفع','Payment receipts')}</b><br><span class="muted fname"></span></span><input type="file" multiple></div>
        <div class="upload-row"><span><b>{B('كشف حساب المطوّر (إن وُجد)','Developer statement (if any)')}</b><br><span class="muted fname"></span></span><input type="file"></div>
        <p class="privacy-note">{icon('lock', 20)}<span>{B('ملفاتك تظهر لك ولفريق المراجعة فقط، ولا يراها أي مشترٍ إلا بإذن محدد منك.','Your files are visible only to you and our reviewers, and no buyer sees them without a specific permission from you.')}</span></p>
        <h3 style="margin-top:var(--space-4)">{B('كيف تريد العرض؟','How should we present it?')}</h3>
        <div class="stack">
          <label class="mode-opt"><input type="radio" name="mode" checked><span><b>{B('بيع خاص','Private sale')}</b><br><span class="muted">{B('بلا إعلان عام. نعرضها على مشترين محددين فقط.','No public listing. We show it only to chosen buyers.')}</span></span></label>
          <label class="mode-opt"><input type="radio" name="mode"><span><b>{B('إعلان عام','Public listing')}</b><br><span class="muted">{B('تظهر في صفحة الفرص بعد المراجعة البشرية.','Appears on the opportunities page after human review.')}</span></span></label>
        </div>
      </section>
      <section class="wizard-panel form-grid">
        {field('s-name','الاسم','Full name','text',('','') ,True)}
        {field('s-wa','رقم واتساب','WhatsApp number','tel',('+20 …','+20 …') ,True,None,'ltr')}
        {consent('s-ok','أوافق على أن تراجع OsoolExit مستنداتي وتتواصل معي بخصوص طلبي.','I agree that OsoolExit may review my documents and contact me about my request.')}
      </section>
      <div class="wizard-nav">
        <button class="btn btn-secondary" type="button" data-prev>{B('السابق','Back')}</button>
        <button class="btn btn-primary" type="button" data-next>{B('التالي','Next')}</button>
        <button class="btn btn-accent" type="submit" data-finish>{B('إرسال للمراجعة','Submit for review')}</button>
      </div>
    </form>
    {ok_msg()}
  </div>
</section>

<section class="container section">
  <div class="panel-cta"><h3>{B('تريد أن تعرف الأرقام أولًا؟','Want the numbers first?')}</h3>
    <p>{B('قارن الإلغاء بالتنازل بحاسبة سريعة قبل أن ترفع أي مستند.','Compare cancellation with transfer using a quick calculator before uploading any document.')}</p>
    <a class="btn btn-accent" href="calculator.html">{B('افتح الحاسبة','Open the calculator')}{arrow()}</a></div>
</section>"""
    return layout("sellers", "sellers", "للبائعين", "For sellers", body)


def buyers():
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('للمشترين','For buyers')}</span>
  <h1>{B('وحدة تقسيط بسعر قديم، بلا أوفر برايس','An installment unit at an older price, with no overprice')}</h1>
  <p class="lead">{B('تتعاقد على الوحدة بسعر العقد القديم الذي أقل من سعر المطوّر الحالي، وتكمل الأقساط المعتادة. الفرق مكسب لك من أول يوم.','You take the unit at the older contract price, below the developer’s current price, and continue the regular installments. The difference is your gain from day one.')}</p>
</section>

<section class="container">
  <div class="grid-3">
    {feature('coins','سعر العقد القديم','The older contract price','بلا أوفر برايس. السعر هو ما دفعه المالك فعلًا.','No overprice. The price is what the owner actually paid.')}
    {feature('doc','أرقام موثقة','Verified numbers','نراجع العقد والمدفوعات والمتبقي قبل أن تظهر لك الفرصة.','We check the contract, payments and balance before an opportunity reaches you.')}
    {feature('building','تنازل رسمي','Official transfer','بموافقة المطوّر وإجراءاته، لا توكيلات ولا وعود.','With developer approval and procedures, not powers of attorney and promises.')}
  </div>
</section>

<section class="container section" id="register">
  <h2>{B('سجّل ميزانيتك','Register your budget')}</h2>
  <p class="muted">{B('نرسل لك الفرص التي تناسب النقد المتاح والقسط المريح. هذا نموذج تجريبي لا يرسل بيانات.','We send opportunities that fit your available cash and comfortable installment. This is a demo form that sends no data.')}</p>
  <div class="card">
    <form data-demo class="form-grid">
      {field('b-name','الاسم','Full name','text',('','') ,True)}
      {field('b-wa','رقم واتساب','WhatsApp number','tel',('+20 …','+20 …') ,True,None,'ltr')}
      {field('b-cash','النقد المتاح عند التنازل (جنيه)','Cash available at transfer (EGP)','money',('','') ,True)}
      {field('b-inst','القسط السنوي المريح (جنيه)','Comfortable yearly installment (EGP)','money')}
      {select('b-type','نوع الوحدة','Unit type',[('','أي نوع','Any type')]+[(k, a, e) for k, (a, e) in TYPES.items()])}
      {select('b-when','موعد التسليم المفضل','Preferred delivery',[('','أي موعد','Any time'),('now','قريبًا (حتى 2027)','Soon (up to 2027)'),('later','بعد 2027','After 2027')])}
      <div class="field full"><label>{B('المناطق المفضلة','Preferred areas')}</label>
        <div class="chips">{''.join(f'<label class="chip"><input type="checkbox" name="areas" value="{k}"><span>{B(a, e)}</span></label>' for k, (a, e) in AREAS.items())}</div></div>
      {consent('b-ok','أوافق على أن تتواصل معي OsoolExit بخصوص الفرص المناسبة.','I agree that OsoolExit may contact me about matching opportunities.')}
      <div class="full"><button class="btn btn-primary" type="submit">{B('سجّل كمشترٍ','Register as a buyer')}</button></div>
    </form>
    {ok_msg()}
  </div>
</section>

<section class="band section">
  <div class="container">
    <h2>{B('كيف يتم الشراء','How buying works')}</h2>
    {stepper([('تسجّل ميزانيتك','Register your budget'),('نرسل الفرص المناسبة','We send matches'),('تحجز وحدتك','You reserve a unit'),('التنازل الرسمي والدفع','Official transfer and payment')])}
    <p class="muted">{B('عمولة المشتري (قيمة تجريبية 0.5% من قيمة العقد) تُستحق فقط بعد إتمام التنازل.','The buyer commission (demo value 0.5% of contract value) is due only after the transfer completes.')}</p>
  </div>
</section>"""
    return layout("buyers", "buyers", "للمشترين", "For buyers", body)


def opportunities():
    cards = "".join(opp_card(u) for u in UNITS)
    body = f"""
<section class="container page-hero">
  <span class="eyebrow">{B('الفرص','Opportunities')}</span>
  <h1>{B('وحدات للتنازل بسعر العقد القديم','Units for transfer at the older contract price')}</h1>
  <p class="notice">{B('بيانات تجريبية: كل الوحدات والأسعار والمشاريع أدناه خيالية لغرض التصميم.','Demo data: every unit, price and project below is fictional, for design only.')}</p>
</section>

<section class="container">
  <div class="card filters" data-filters>
    {select('f-type','النوع','Type',[('','الكل','All')]+[(k, a, e) for k, (a, e) in TYPES.items()],data_filter='type')}
    {select('f-area','المنطقة','Area',[('','الكل','All')]+[(k, a, e) for k, (a, e) in AREAS.items()],data_filter='area')}
    {select('f-state','حالة التحقق','Verification',[('','الكل','All')]+[(k, a, e) for k, (a, e) in STATES.items()],data_filter='state')}
    {select('f-budget','النقد المتاح (حتى)','Cash available (up to)',[('','أي مبلغ','Any amount'),('700000','700,000','700,000'),('1000000','1,000,000','1,000,000'),('1500000','1,500,000','1,500,000')],data_filter='budget')}
    <label class="check" style="padding-bottom:12px"><input type="checkbox" data-filter="fav"><span>{B('المفضلة فقط','Favorites only')}</span></label>
  </div>
  <p class="muted"><span data-count>{len(UNITS)}</span> {B('فرصة','opportunities')}</p>
  <div class="opps">{cards}</div>
  <div class="empty">{B('لا توجد فرص مطابقة. جرّب توسيع الفلاتر أو سجّل ميزانيتك لنرسل لك ما يناسبك.','No matching opportunities. Try widening the filters or register your budget and we will send matches.')}
    <p><a class="btn btn-primary" href="buyers.html">{B('سجّل كمشترٍ','Register as a buyer')}</a></p></div>
</section>"""
    return layout("opportunities", "opportunities", "الفرص", "Opportunities", body)


def opportunity():
    u = UNITS[0]
    others = "".join(opp_card(x) for x in UNITS[3:6])
    remaining = u["value"] - u["paid"]
    body = f"""
<section class="container page-hero" style="padding-bottom:var(--space-3)">
  <p class="muted"><a href="opportunities.html">{B('الفرص','Opportunities')}</a> / {B('مشروع أ','Project A')}</p>
  <div style="display:flex;gap:var(--space-3);align-items:flex-start;flex-wrap:wrap;justify-content:space-between">
    <div><h1 style="margin-bottom:var(--space-1)">{B('شقة 148 م² · 3 غرف · القاهرة الجديدة','148 m² apartment · 3 BR · New Cairo')}</h1>
      <p class="muted">{B('مشروع أ · رقم الوحدة DEMO-0101','Project A · Unit ref DEMO-0101')}</p></div>
    {badge('verified')}
  </div>
  <p class="notice">{B('صفحة تجريبية: بيانات خيالية لغرض التصميم.','Demo page: fictional data, for design only.')}</p>
</section>

<section class="container detail">
  <div class="stack">
    <div class="gallery"><div class="opp-photo">{B('صورة 1','Photo 1')}</div><div class="opp-photo">{B('صورة 2','Photo 2')}</div><div class="opp-photo">{B('صورة 3','Photo 3')}</div></div>
    <div class="card"><h3>{B('المواصفات','Key specs')}</h3>
      <dl class="spec-list">
        <div><dt>{B('النوع','Type')}</dt><dd>{B('شقة','Apartment')}</dd></div><div><dt>{B('المساحة','Area')}</dt><dd class="num">148 m²</dd></div>
        <div><dt>{B('الغرف','Bedrooms')}</dt><dd class="num">3</dd></div><div><dt>{B('الدور','Floor')}</dt><dd class="num">4</dd></div>
        <div><dt>{B('التشطيب','Finishing')}</dt><dd>{B('بدون تشطيب','Core and shell')}</dd></div><div><dt>{B('التسليم المتوقع','Expected delivery')}</dt><dd class="num">{u['year']}</dd></div>
      </dl></div>
    <div class="card"><h3>{B('السعر والدفعات','Price and payments')}</h3>
      <table class="pay-table">
        <tr><td>{B('قيمة العقد','Contract value')}</td><td>{fmt(u['value'])}</td></tr>
        <tr><td>{B('المدفوع للمطوّر (نفس ما دفعه المالك)','Paid to the developer (same as the owner paid)')}</td><td>{fmt(u['paid'])}</td></tr>
        <tr><td>{B('المتبقي للمطوّر على أقساط','Remaining owed to the developer, in installments')}</td><td>{fmt(remaining)}</td></tr>
        <tr><td>{B('عمولة المشتري (0.5%، قيمة تجريبية)','Buyer commission (0.5%, demo value)')}</td><td>{fmt(u['value'] * 0.005)}</td></tr>
        <tr class="total"><td>{B('النقد المطلوب عند التنازل','Cash needed at transfer')}</td><td>{fmt(u['paid'] + u['value'] * 0.005)}</td></tr>
      </table>
      <p class="muted" style="font-size:.85rem;margin-top:var(--space-2)">{B('رسوم نقل المطوّر تُعرض منفصلة وتختلف من مطوّر لآخر.','Developer transfer fees are shown separately and differ by developer.')}</p></div>
    <div class="card"><h3>{B('مقارنة بالسوق','Market comparison')}</h3>
      <p class="muted">{B('تقدير المالك لسعر السوق الحالي لا يمثل تقييمًا من OsoolExit. تحقق بنفسك قبل القرار.','The owner’s estimate of today’s market price is not a valuation by OsoolExit. Check it yourself before deciding.')}</p>
      <span class="badge badge-declared">{B('تقدير المالك','Owner estimate')}</span></div>
  </div>
  <aside class="card">
    <h3>{B('احجز هذه الوحدة','Reserve this unit')}</h3>
    <form data-demo>
      {field('r-name','الاسم','Full name','text',('','') ,True)}
      {field('r-wa','رقم واتساب','WhatsApp number','tel',('+20 …','+20 …') ,True,None,'ltr')}
      {select('r-ready','جاهزيتك للشراء','Your readiness',[('now','جاهز الآن','Ready now'),('soon','خلال شهر','Within a month'),('look','أتفحص فقط','Just looking')])}
      {textarea('r-q','سؤال للبائع (اختياري)','Question for the seller (optional)')}
      {consent('r-ok','أفهم أن عمولة المشتري تُستحق فقط بعد إتمام التنازل.','I understand the buyer commission is due only after the transfer completes.')}
      <button class="btn btn-accent" type="submit" style="width:100%;margin-top:var(--space-2)">{B('احجز','Reserve')}</button>
      <p class="privacy-note">{icon('lock', 20)}<span>{B('نستخدم رقمك للتواصل بخصوص هذه الوحدة فقط.','We use your number only to contact you about this unit.')}</span></p>
    </form>
    {ok_msg()}
  </aside>
</section>

<section class="container section">
  <h2>{B('وحدات مشابهة','Similar units')}</h2>
  <div class="opps">{others}</div>
</section>"""
    return layout("opportunity", "opportunities", "تفاصيل الفرصة", "Opportunity details", body)
