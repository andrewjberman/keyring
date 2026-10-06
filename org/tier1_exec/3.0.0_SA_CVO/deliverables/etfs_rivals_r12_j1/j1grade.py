"""J1 grade, ETFS_RIVALS round 12 RIV-au-1, on the served 2026-10-06 index.html (S3 bytes).
Limbs: (a) every data-sec button resolves, in-document, to a popover that carries a section for the fund the button sits under;
(b) real mouse clicks per fund across periods open the right modal; (c) plain-text ticker census of VISIBLE text outside
buttons; (d) page reads whole: 13 panels each with head, AI card, rankings; no audit block, no audit-trail link."""
import json
import re
import sys
import pathlib
from playwright.sync_api import sync_playwright

P = pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2])
html = P.read_text(encoding="utf-8")
keys = sorted(set(re.findall(r'data-sec-dialog="([^"]+)"', html)))
res = {"page": str(P), "bytes": len(html.encode("utf-8")), "dialog_keys": len(keys)}

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 1400, "height": 1000})
    pg.goto(P.as_uri())
    funds = pg.eval_on_selector_all("[data-fund-panel]", "e => e.map(x => x.dataset.fundPanel)")
    res["funds"] = funds
    # (a) static resolution + fund-section check over every button
    a = pg.evaluate("""() => {
      const out = {buttons:0, unresolved:[], no_fund_section:[], outside_panel:0, per_fund:{}};
      for (const btn of document.querySelectorAll('button[data-sec]')) {
        out.buttons++;
        const tgt = document.getElementById(btn.getAttribute('popovertarget'));
        const panel = btn.closest('[data-fund-panel]');
        const f = panel ? panel.dataset.fundPanel : null;
        if (!f) out.outside_panel++;
        out.per_fund[f] = (out.per_fund[f]||0)+1;
        if (!tgt || tgt.dataset.secDialog !== btn.dataset.sec) { out.unresolved.push(btn.dataset.sec); continue; }
        if (f && !tgt.querySelector('section[data-fund="'+f+'"]')) out.no_fund_section.push(f+':'+btn.dataset.sec+':'+btn.textContent.slice(0,40));
      }
      return out;}""")
    a["no_fund_section_n"] = len(a["no_fund_section"])
    a["no_fund_section"] = a["no_fund_section"][:40]
    res["a_static"] = a
    # (b) real clicks: per fund, every period, up to 6 visible buttons spread across the panel
    periods = list(dict.fromkeys(pg.eval_on_selector_all("label[for^=rf-period-]", "e => e.map(x => x.getAttribute('for'))")))
    clicks, fails, firsts = 0, [], []
    for f in funds:
        pg.click(f"label[for=rf-fund-{f}]")
        print("clicks", f, clicks, len(fails), flush=True)
        for per in periods:
            lab = pg.locator(f"label[for={per}]")
            try:
                lab.click(timeout=800)
            except Exception:
                pass
            vis = pg.locator(f"[data-fund-panel={f}] button[data-sec]:visible")
            n = vis.count()
            idx = sorted(set([0, n // 5, 2 * n // 5, 3 * n // 5, 4 * n // 5, n - 1])) if n else []
            print("  per", per, n, flush=True)
            for i in idx:
                btn = vis.nth(i)
                key = btn.get_attribute("data-sec")
                txt = btn.inner_text()[:50]
                try:
                    btn.scroll_into_view_if_needed(timeout=1500)
                    btn.click(timeout=1500)
                    tid = btn.get_attribute("popovertarget")
                    ok = pg.evaluate("t => { const d=document.getElementById(t); return !!d && d.matches(':popover-open'); }", tid)
                    has_f = pg.evaluate("([t,f]) => !!document.getElementById(t).querySelector('section[data-fund=\"'+f+'\"]')", [tid, f])
                    first = pg.evaluate("t => (document.getElementById(t).querySelector('section[data-fund]')||{dataset:{}}).dataset.fund", tid)
                    firsts.append(first == f)
                    h3 = pg.evaluate("t => (document.getElementById(t).querySelector('h3')||{}).textContent", tid)
                    clicks += 1
                    if not (ok and has_f):
                        fails.append({"fund": f, "period": per, "key": key, "text": txt, "open": ok, "fund_section": has_f, "h3": h3})
                    if clicks == 1:
                        pg.screenshot(path=str(OUT.parent / "j1_first_click.png"))
                    pg.keyboard.press("Escape")
                except Exception as e:
                    fails.append({"fund": f, "period": per, "key": key, "text": txt, "err": str(e)[:160]})
                    pg.keyboard.press("Escape")
    res["b_clicks"] = {"periods": periods, "clicks": clicks, "fails_n": len(fails), "clicking_fund_section_first": sum(firsts), "fails": fails[:30]}
    # nested: a security button inside an AI modal
    pg.click("label[for=rf-fund-IDVZ]")
    pg.click("[data-fund-panel=IDVZ] button.rf-open >> nth=0")
    nb = pg.locator("[data-fund-panel=IDVZ] [data-ai-dialog]:popover-open button[data-sec]").first
    nkey = nb.get_attribute("data-sec")
    nb.click()
    res["b_nested_ai_modal"] = {"key": nkey, "open": pg.evaluate("k => document.querySelector('[data-sec-dialog=\"'+k+'\"]').matches(':popover-open')", nkey)}
    pg.screenshot(path=str(OUT.parent / "j1_nested_click.png"))
    pg.keyboard.press("Escape")
    pg.keyboard.press("Escape")
    # (c) visible-text plain ticker census, per fund panel shown
    tick = sorted({k.split("_")[0] for k in keys if len(k.split("_")[0]) >= 2})
    hits = []
    RX = re.compile(r"(?<![A-Za-z0-9$])(" + "|".join(re.escape(x) for x in sorted(tick, key=len, reverse=True)) + r")(?: [A-Z]{2})?(?![A-Za-z0-9])")
    for f in funds:
        pg.click(f"label[for=rf-fund-{f}]")
        texts = pg.evaluate("""f => { const out=[]; const root=document.querySelector('[data-fund-panel="'+f+'"]');
          const w=document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
          let n; while ((n=w.nextNode())) { const el=n.parentElement; if (!el || el.closest('button[data-sec]')) continue;
            if (el.closest('[popover]') && !el.closest('[popover]').matches(':popover-open')) { /* closed modal: read anyway, it is page text */ }
            const t=n.textContent.trim(); if (t) out.push([t, !!el.closest('[popover]'), el.checkVisibility ? el.checkVisibility() : true]); }
          return out; }""", f)
        for t, in_pop, visible in texts:
            for m in RX.finditer(t):
                hits.append({"fund": f, "ticker": m.group(1), "in_modal": in_pop, "visible": visible, "ctx": t[max(0, m.start() - 50): m.end() + 30]})
        print("census", f, len(texts), len(hits), flush=True)
    # exclude fund codes (the picker/headers use fund tickers by design)
    hits_nf = [h for h in hits if h["ticker"] not in funds]
    res["c_plain_ticker"] = {"ticker_vocab": len(tick), "hits": len(hits_nf), "hits_fund_codes": len(hits) - len(hits_nf),
                             "by_ticker": {}, "sample": hits_nf[:60]}
    for h in hits_nf:
        res["c_plain_ticker"]["by_ticker"][h["ticker"]] = res["c_plain_ticker"]["by_ticker"].get(h["ticker"], 0) + 1
    eq = re.findall(r'[A-Z0-9]{1,6} [A-Z]{2} Equity', pg.evaluate("() => document.body.innerText"))
    res["c_equity_form_visible_text"] = {"n": len(eq), "sample": eq[:20]}
    # (d) reads whole
    res["d_whole"] = pg.evaluate("""() => { const o={}; for (const p of document.querySelectorAll('[data-fund-panel]')) {
        const f=p.dataset.fundPanel; o[f]={head:!!p.querySelector('.rf-fund-head'), ai:p.querySelectorAll('[data-ai-kind]').length,
          rankings:!!p.querySelector('[data-component=rankings]'), text_chars:p.innerText.length, buttons:p.querySelectorAll('button[data-sec]').length}; }
        o._audit_block=!!document.querySelector('details#audit'); o._audit_href=[...document.querySelectorAll('a[href]')].filter(a=>/audit/i.test(a.href)).length;
        o._audit_text=(document.body.innerText.match(/audit trail|audit\\.html/gi)||[]).length; return o; }""")
    pg.click("label[for=rf-fund-IDVZ]")
    pg.screenshot(path=str(OUT.parent / "j1_idvz_top.png"))
    b.close()
OUT.write_text(json.dumps(res, indent=1, ensure_ascii=True))
print(json.dumps({k: (v if k not in ("c_plain_ticker",) else {kk: vv for kk, vv in v.items() if kk != "sample"}) for k, v in res.items()}, indent=1)[:6000])
