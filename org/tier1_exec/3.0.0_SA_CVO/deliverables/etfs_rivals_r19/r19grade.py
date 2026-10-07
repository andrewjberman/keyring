"""CVO~RV browser grade, ETFS_RIVALS rounds 15-19, on a real-run page layer (not the served page).

Usage: python r19grade.py <layer dir holding index.html and charts/> <out.json>

Every .rf-chart frame is loaded by the page's own script: each security dialog is opened, the chart route
/rivalfunds/<day>/chart/<FUND> is stood in by request interception from charts/<FUND>.json, and each frame is read back.
"""
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

LAYER = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
DAY = "2026-10-06"
HTML = (LAYER / "index.html").read_bytes()
FUNDS = {p.stem for p in (LAYER / "charts").glob("*.json")}

OPEN_ALL = """async () => {
  for (const d of document.querySelectorAll('[data-sec-dialog]')) {
    try { d.showPopover(); } catch (e) {}
    await new Promise(r => setTimeout(r, 2));
    try { d.hidePopover(); } catch (e) {}
  }
}"""

SETTLED = "[...document.querySelectorAll('.rf-chart')].every(f => f._o !== undefined && !f._busy)"

READ_FRAMES = """() => [...document.querySelectorAll('.rf-chart')].map(f => {
  const sec = f.closest('section');
  const dlg = f.closest('[data-sec-dialog]');
  const tile = [...sec.querySelectorAll('p')].map(p => p.textContent).find(t => /across [0-9]+ trade/.test(t)) || '';
  const strip = sec.querySelector('[data-month-chart]');
  const tr = f.querySelector('[data-chart-trades]');
  const out = f.querySelector('.rf-ch-out');
  return {
    fund: f.dataset.chartFund, key: f.dataset.chartKey, dlg: dlg.dataset.secDialog,
    status: f.querySelector('[data-chart-status]').textContent,
    svg: f.querySelectorAll('svg').length,
    text: out ? out.textContent : '',
    trades: tr ? [tr.textContent] : null,
    tile: tile,
    strip: strip ? [...strip.children].map(c => [c.dataset.m, c.className]) : null,
    periods: [...sec.querySelectorAll('table tr td:first-child')].map(t => t.textContent),
    buttons: [...f.querySelectorAll('[data-chart-range]')].map(
      x => x.textContent + (x.getAttribute('aria-current') ? '*' : ''))
  };
})"""

SAMPLES = (("IDVZ", "PBR_US_Equity"), ("CGIC", "2454_TT_Equity"), ("BASG", "482480100"), ("IDVZ", "AZN_LN_Equity"))


def handle(route):
    url = route.request.url
    m = re.search(r"/rivalfunds/" + DAY + r"/chart/([A-Z0-9]+)$", url)
    if m and m.group(1) in FUNDS:
        body = (LAYER / "charts" / (m.group(1) + ".json")).read_bytes()
        route.fulfill(status=200, content_type="application/json", body=body)
    elif url.rstrip("/").endswith("/rivalfunds/" + DAY):
        route.fulfill(status=200, content_type="text/html; charset=utf-8", body=HTML)
    else:
        route.fulfill(status=404, body="{}")


def sample(pg, fund, key):
    sel = '.rf-chart[data-chart-fund="%s"][data-chart-key="%s"]' % (fund, key)
    rec = {"fund": fund, "key": key, "ranges": {}}
    if not pg.query_selector(sel):
        rec["absent"] = True
        return rec
    pg.evaluate("s => document.querySelector(s).closest('[data-sec-dialog]').showPopover()", sel)
    for rg in ("R30", "R90", "R365"):
        pg.click('%s [data-chart-range="%s"]' % (sel, rg))
        pg.wait_for_timeout(120)
        rec["ranges"][rg] = {
            "status": pg.inner_text(sel + " [data-chart-status]"),
            "svg": pg.evaluate("s => document.querySelector(s).querySelectorAll('svg').length", sel),
            "circles": pg.evaluate("s => document.querySelector(s).querySelectorAll('svg circle').length", sel),
        }
    svg = pg.query_selector(sel + " svg")
    if svg:
        box = svg.bounding_box()
        before = pg.inner_text(sel).split("\n")
        pg.mouse.move(box["x"] + box["width"] * 0.6, box["y"] + box["height"] * 0.5)
        pg.wait_for_timeout(150)
        rec["hover_text"] = [ln for ln in pg.inner_text(sel).split("\n") if ln not in before][:4]
        rec["axis"] = pg.evaluate("s => [...document.querySelector(s).querySelectorAll('svg text')].map(t => t.textContent)", sel)
        pg.screenshot(path=str(OUT.parent / ("shot_%s_%s.png" % (fund, key))))
    pg.evaluate("s => document.querySelector(s).closest('[data-sec-dialog]').hidePopover()", sel)
    return rec


def main():
    errors = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        pg = browser.new_page(viewport={"width": 1400, "height": 1000})
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.route("**/*", handle)
        pg.goto("http://standin.local/rivalfunds/" + DAY)
        pre = pg.evaluate(
            "[...document.querySelectorAll('[data-chart-trades]')].filter("
            "e => /load with the chart/.test(e.textContent)).length")
        pg.evaluate(OPEN_ALL)
        pg.wait_for_function(SETTLED, timeout=120000)
        frames = pg.evaluate(READ_FRAMES)
        samples = [sample(pg, fund, key) for fund, key in SAMPLES]
        browser.close()
    result = {"frames_n": len(frames), "static_load_lines": pre, "frames": frames, "samples": samples, "pageerrors": errors}
    with OUT.open("w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1)
    print("frames", len(frames), "static load lines", pre, "page errors", len(errors))


if __name__ == "__main__":
    main()
