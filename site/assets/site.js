/* OsoolExit site behavior: language + theme, calculators, filters, favorites, seller wizard, demo forms. No dependencies. */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const nf = new Intl.NumberFormat('en-US');
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  const root = document.documentElement;
  const q = new URLSearchParams(location.search);

  /* ---------- language ---------- */
  function applyLang(l) {
    root.lang = l; root.dir = l === 'ar' ? 'rtl' : 'ltr';
    $$('[data-ph-ar]').forEach(el => { el.placeholder = el.getAttribute('data-ph-' + l) || ''; });
    $$('[data-aria-ar]').forEach(el => { el.setAttribute('aria-label', el.getAttribute('data-aria-' + l)); });
    $$('option[data-ar]').forEach(o => { o.textContent = o.getAttribute('data-' + l); });
    const t = window.PAGE || {};
    document.title = (l === 'ar' ? t.ar : t.en) || document.title;
    const b = $('#langBtn'); if (b) b.textContent = l === 'ar' ? 'English' : 'العربية';
    store.set('osool-lang', l);
    $$('[data-calc]').forEach(calc);
  }
  const startLang = q.get('lang') || store.get('osool-lang', 'ar');
  const langBtn = $('#langBtn');
  if (langBtn) langBtn.addEventListener('click', () => applyLang(root.lang === 'ar' ? 'en' : 'ar'));

  /* ---------- theme ---------- */
  const themeBtn = $('#themeBtn');
  function setTheme(t) { root.dataset.theme = t; if (themeBtn) themeBtn.setAttribute('aria-pressed', String(t === 'dark')); store.set('osool-theme', t); }
  const startTheme = q.get('theme') || store.get('osool-theme', '');
  if (startTheme === 'dark' || startTheme === 'light') setTheme(startTheme);
  if (themeBtn) themeBtn.addEventListener('click', () => setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark'));

  /* ---------- calculators ---------- */
  function num(el) { return parseFloat(String(el.value).replace(/[^\d.]/g, '')) || 0; }
  function calc(box) {
    const g = k => { const el = $('[data-in="' + k + '"]', box); return el ? num(el) : 0; };
    const v = g('value'), p = g('paid'), d = g('ded'), c = g('com'), f = g('fee');
    const deduction = v * d / 100;
    const refund = Math.max(0, p - deduction);
    const commission = v * c / 100;
    const out = {
      refund, deduction, transfer: p, gain: p - refund, commission,
      buyerCash: p + commission + f, remaining: Math.max(0, v - p)
    };
    Object.keys(out).forEach(k => $$('[data-out="' + k + '"]', box).forEach(el => { el.textContent = nf.format(Math.round(out[k])); }));
  }
  $$('[data-calc]').forEach(box => { $$('input', box).forEach(i => i.addEventListener('input', () => calc(box))); calc(box); });

  /* ---------- favorites ---------- */
  function favs() { try { return JSON.parse(store.get('osool-favs', '[]')); } catch (e) { return []; } }
  function paintFavs() { const f = favs(); $$('.fav').forEach(b => b.setAttribute('aria-pressed', String(f.includes(b.dataset.id)))); }
  $$('.fav').forEach(b => b.addEventListener('click', () => {
    let f = favs(); f = f.includes(b.dataset.id) ? f.filter(x => x !== b.dataset.id) : f.concat(b.dataset.id);
    store.set('osool-favs', JSON.stringify(f)); paintFavs(); filter();
  }));

  /* ---------- opportunity filters ---------- */
  const fbox = $('[data-filters]');
  function filter() {
    if (!fbox) return;
    const val = k => { const el = $('[data-filter="' + k + '"]', fbox); return el ? el.value : ''; };
    const type = val('type'), area = val('area'), state = val('state');
    const budget = parseFloat(val('budget')) || Infinity;
    const onlyFav = $('[data-filter="fav"]', fbox).checked; const f = favs();
    let shown = 0;
    $$('.opps > [data-id]').forEach(card => {
      const ok = (!type || card.dataset.type === type) && (!area || card.dataset.area === area) &&
        (!state || card.dataset.state === state) && (+card.dataset.cash <= budget) && (!onlyFav || f.includes(card.dataset.id));
      card.style.display = ok ? '' : 'none'; if (ok) shown++;
    });
    const n = $('[data-count]'); if (n) n.textContent = shown;
    const e = $('.empty'); if (e) e.classList.toggle('show', shown === 0);
  }
  if (fbox) $$('select, input', fbox).forEach(i => i.addEventListener('input', filter));

  /* ---------- seller wizard ---------- */
  $$('[data-wizard]').forEach(w => {
    const panels = $$('.wizard-panel', w), steps = $$('.stepper li', w); let i = 0;
    function show(n, scroll) {
      i = n;
      panels.forEach((p, k) => p.classList.toggle('active', k === n));
      steps.forEach((s, k) => { s.classList.toggle('todo', k > n); if (k === n) s.setAttribute('aria-current', 'step'); else s.removeAttribute('aria-current'); });
      $$('[data-prev]', w).forEach(b => { b.style.visibility = n === 0 ? 'hidden' : 'visible'; });
      $$('[data-next]', w).forEach(b => { b.style.display = n === panels.length - 1 ? 'none' : ''; });
      $$('[data-finish]', w).forEach(b => { b.style.display = n === panels.length - 1 ? '' : 'none'; });
      if (scroll) w.scrollIntoView({ block: 'start', behavior: 'smooth' });
    }
    $$('[data-next]', w).forEach(b => b.addEventListener('click', () => {
      const bad = $$('input[required], select[required]', panels[i]).find(el => !el.checkValidity());
      if (bad) { bad.reportValidity(); return; } show(Math.min(i + 1, panels.length - 1), true);
    }));
    $$('[data-prev]', w).forEach(b => b.addEventListener('click', () => show(Math.max(i - 1, 0), true)));
    show(0);
  });

  /* ---------- demo forms (nothing is sent) ---------- */
  $$('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault(); if (!f.checkValidity()) { f.reportValidity(); return; }
    const ok = $('.form-ok', f.closest('section, .card, main') || document); if (ok) ok.classList.add('show');
  }));
  $$('input[type=file]').forEach(i => i.addEventListener('change', () => {
    const n = i.closest('.upload-row') && $('.fname', i.closest('.upload-row'));
    if (n) n.textContent = i.files.length ? i.files[0].name : '';
  }));

  paintFavs(); filter(); applyLang(startLang === 'en' ? 'en' : 'ar');
})();
