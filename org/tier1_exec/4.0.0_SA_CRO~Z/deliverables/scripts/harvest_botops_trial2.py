"""HARVST bot-operations trial 2: WHICH client can make the REST pull once the browser is warm?

Trial 1 (harvest_botops_trial.py) showed that a real-browser warm-up loads every homepage unchallenged and mints
fresh trust cookies, and that FT's REST pull then succeeds, but bbg's search (PerimeterX 403) and wsj/barrons'
search (DataDome 401) still refuse the curl_cffi client even with seconds-old cookies. That client impersonates
Chrome 146 (macOS) while trial 1 sent the browser's Chrome 154 (Windows) user agent. This trial separates the
causes, all inside one warm session per publisher:

  A  in-page fetch: the REST call issued by the warm tab itself (same TLS, headers, cookies): search, then article
  C  a browser navigation to the search URL (how a person searches) -- run before B
  B  curl_cffi with a self-consistent identity (impersonation's own user agent, no override) + the warm cookies
  C  a browser navigation to the search URL (how a person searches)

A challenge is RECORDED, never interacted with. No article text is stored; no cookie or credential value is
printed; the stored session is never written back. Output: .runtime/harvest-botops-trial-20260930/<pub>-t2.jsonl

Usage (workspace root): python harvest_botops_trial2.py bbg|wsj|barrons|ft
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from curl_cffi import requests as creq  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

import harvest_botops_trial as t1  # noqa: E402  (reuses CONF, signatures, trust_state, stored_envelope, to_playwright)

PUB = t1.PUB
CONF = t1.CONF
LOG = t1.OUT / f"{PUB}-t2.jsonl"
PACE = 20

FETCH_JS = """async ([url, headers]) => {
  try {
    const r = await fetch(url, {credentials: 'include', headers: headers || {}});
    const text = await r.text();
    return {status: r.status, type: r.headers.get('content-type') || '', text: text};
  } catch (e) { return {status: null, type: '', text: '', error: String(e)}; }
}"""


def log(**row):
    row["at"] = t1.now().isoformat()
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
    print(json.dumps(row)[:400], flush=True)


def summarize(step, url, status, ctype, text, error=None):
    hits = re.findall(CONF["hit"], text or "")
    log(step=step, path=re.sub(r"https?://[^/]+", "", url)[:90], status=status, content_type=(ctype or "")[:40],
        bytes=len(text or ""), challenge=t1.signatures(text), hits=len(set(hits)), error=error)
    return hits[0] if hits else None


def article_headers(hit):
    if PUB == "barrons":
        return {"Accept": "application/json", "x-nextjs-data": "1", "Referer": "https://www.barrons.com/articles/" + hit}
    return {}


def main():
    stored, ua, source = t1.stored_envelope()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        ctx = browser.new_context(user_agent=ua) if ua else browser.new_context()
        ctx.add_cookies(t1.to_playwright(stored))
        page = ctx.new_page()
        page.goto(CONF["home"], wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(20000)
        sig = t1.signatures(page.content())
        log(step="warmup", title=(page.title() or "")[:80], challenge=sig,
            trust_cookies_minutes_left=t1.trust_state(ctx.cookies()))
        if sig:
            log(step="stop", reason="challenge on warm-up page; not interacted with")
            browser.close()
            return
        # A: in-page fetch, search then article
        res = page.evaluate(FETCH_JS, [CONF["search"], {}])
        hit = summarize("A_inpage_search", CONF["search"], res.get("status"), res.get("type"), res.get("text"), res.get("error"))
        page.wait_for_timeout(PACE * 1000)
        if hit:
            url = CONF["article"].format(hit=hit)
            res = page.evaluate(FETCH_JS, [url, article_headers(hit)])
            summarize("A_inpage_article", url, res.get("status"), res.get("type"), res.get("text"), res.get("error"))
            page.wait_for_timeout(PACE * 1000)
        else:
            log(step="A_inpage_article", skipped="no hit parsed from in-page search")
        # C: browser navigation to the search page (before B: trial 1 showed a refused outside client
        # poisons the browser session that follows it)
        resp = page.goto(CONF["search"], wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(8000)
        summarize("C_navigate_search", CONF["search"], resp.status if resp else None, "", page.content())
        page.screenshot(path=str(t1.OUT / f"{PUB}-t2-search.png"))
        page.wait_for_timeout(PACE * 1000)
        # B: curl_cffi, self-consistent identity (no user-agent override), warm cookies -- LAST, so a
        # refusal here cannot contaminate A or C
        s = creq.Session(impersonate="chrome", timeout=45)
        for c in ctx.cookies():
            s.cookies.set(c["name"], c["value"], domain=c["domain"], path=c.get("path") or "/")
        try:
            r = s.get(CONF["search"])
            summarize("B_curl_consistent_search", CONF["search"], r.status_code, r.headers.get("content-type"), r.text)
        except Exception as exc:  # noqa: BLE001
            log(step="B_curl_consistent_search", error=type(exc).__name__, detail=str(exc)[:160])
        browser.close()
    log(step="done")


if __name__ == "__main__":
    main()
