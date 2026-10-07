"""Plain-ticker census v2 on the served page: visible text outside data-sec buttons, a ticker token from the page's own dialog
keys, not adjacent to '_' (the rf-cite key line), classed by the element it sits in. Also inspects the 15 no-fund-section buttons."""
import collections
import json
import re
import sys
import pathlib
from playwright.sync_api import sync_playwright

P = pathlib.Path(sys.argv[1]).resolve()
html = P.read_text(encoding="utf-8")
keys = sorted(set(re.findall(r'data-sec-dialog="([^"]+)"', html)))
tick = sorted({k.split("_")[0] for k in keys if len(k.split("_")[0]) >= 2}, key=len, reverse=True)
RX = re.compile(r"(?<![A-Za-z0-9$_])(" + "|".join(re.escape(x) for x in tick) + r")(?: [A-Z]{2})?(?![A-Za-z0-9_])")
out = {"vocab": len(tick), "hits": []}
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 1400, "height": 1000})
    pg.goto(P.as_uri())
    funds = pg.eval_on_selector_all("[data-fund-panel]", "e => e.map(x => x.dataset.fundPanel)")
    for f in funds:
        pg.click(f"label[for=rf-fund-{f}]")
        texts = pg.evaluate("""f => { const out=[]; const root=document.querySelector('[data-fund-panel="'+f+'"]');
          const w=document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n;
          while ((n=w.nextNode())) { const el=n.parentElement; if (!el || el.closest('button[data-sec]')) continue;
            const t=n.textContent; if (!t.trim()) continue;
            const pop=el.closest('[popover]');
            out.push({t, tag:el.tagName, cls:el.className||'', pop: pop ? (pop.dataset.secDialog ? 'sec' : (pop.dataset.aiDialog ? 'ai' : 'other')) : '',
                      comp: (el.closest('[data-component]')||{dataset:{}}).dataset.component || (el.closest('[data-ai-kind]') ? 'ai-face' : '')}); }
          return out; }""", f)
        for x in texts:
            for m in RX.finditer(x["t"]):
                out["hits"].append({"fund": f, "tok": m.group(0), "where": f'{x["tag"]}.{x["cls"]}|pop={x["pop"]}|comp={x["comp"]}',
                                    "ctx": x["t"][max(0, m.start() - 60): m.end() + 40]})
    # the 15 no-fund-section buttons: where they sit and what the modal holds
    out["nfs"] = pg.evaluate("""() => { const o=[]; for (const btn of document.querySelectorAll('button[data-sec]')) {
        const f=btn.closest('[data-fund-panel]').dataset.fundPanel; const tgt=document.getElementById(btn.getAttribute('popovertarget'));
        if (tgt.querySelector('section[data-fund="'+f+'"]')) continue;
        const ctxEl = btn.closest('p,td,li,div'); o.push({f, key:btn.dataset.sec, text:btn.textContent,
          modal_funds:[...tgt.querySelectorAll('section[data-fund]')].map(s=>s.dataset.fund),
          where:(btn.closest('[data-component]')||{dataset:{}}).dataset.component || (btn.closest('[data-ai-kind]')||{dataset:{}}).dataset.aiKind || '',
          ctx: ctxEl ? ctxEl.textContent.slice(0,200) : ''}); } return o; }""")
    out["nbis_dialog_exists"] = pg.evaluate("() => !!document.querySelector('[data-sec-dialog=\"NBIS_US_Equity\"]')")
    out["goog_keys"] = pg.evaluate("() => [...document.querySelectorAll('[data-sec-dialog^=\"GOOG\"]')].map(d => [d.dataset.secDialog, [...d.querySelectorAll('section[data-fund]')].map(s=>s.dataset.fund)])")
    b.close()
c = collections.Counter(h["where"] for h in out["hits"])
print("vocab", out["vocab"], "hits", len(out["hits"]))
for w, n in c.most_common(30):
    print(f"{n:5d}  {w}")
pathlib.Path(sys.argv[2]).write_text(json.dumps(out, indent=1, ensure_ascii=True))
print(json.dumps({"nfs": out["nfs"], "nbis": out["nbis_dialog_exists"], "goog": out["goog_keys"]}, indent=1)[:5000])
