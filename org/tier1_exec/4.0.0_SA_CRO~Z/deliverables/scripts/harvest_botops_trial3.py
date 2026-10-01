"""HARVST bot-operations trial 3: is the flag on the replayed bot-visitor cookies or on this box's IP?

Trial 2 showed bbg and wsj search refused even from inside a warm browser tab, and barrons' homepage now
challenged, so something persistent is flagged. The stored sessions replay the same bot-visitor identity
(`_pxvid`/`_px*`, `datadome`, `cf_clearance`) on every run. This trial keeps everything else identical (same box,
same IP, same login cookies, same headed Chrome) and STRIPS those bot-manager cookies before the warm-up, so each
site mints a fresh visitor. Then: warm-up, one in-page search, and (if it passes) one in-page article.

  pass -> the replayed visitor cookies carried the flag (fix: never persist bot-manager cookies)
  fail -> the IP carries it (fix: cool-down / a different egress)

A challenge is RECORDED, never interacted with. No article text stored; no cookie or credential value printed;
the stored session is never written back. Output: .runtime/harvest-botops-trial-20260930/<pub>-t3.jsonl

Usage (workspace root): python harvest_botops_trial3.py bbg|wsj|barrons
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from playwright.sync_api import sync_playwright  # noqa: E402

import harvest_botops_trial as t1  # noqa: E402
import harvest_botops_trial2 as t2  # noqa: E402

PUB = t1.PUB
CONF = t1.CONF
LOG = t1.OUT / f"{PUB}-t3.jsonl"
BOT_COOKIES = ("_px", "pxcts", "datadome", "__cf_bm", "cf_clearance")


def log(**row):
    row["at"] = t1.now().isoformat()
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
    print(json.dumps(row)[:400], flush=True)


def main():
    stored, ua, source = t1.stored_envelope()
    kept = [c for c in stored if not str(c.get("name", "")).startswith(BOT_COOKIES)]
    log(step="strip", stored=len(stored), kept=len(kept), removed=len(stored) - len(kept))
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        ctx = browser.new_context(user_agent=ua) if ua else browser.new_context()
        ctx.add_cookies(t1.to_playwright(kept))
        page = ctx.new_page()
        page.goto(CONF["home"], wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(20000)
        sig = t1.signatures(page.content())
        log(step="warmup", title=(page.title() or "")[:80], challenge=sig,
            trust_cookies_minutes_left=t1.trust_state(ctx.cookies()))
        if sig:
            log(step="stop", reason="challenge on warm-up page with fresh visitor; not interacted with")
            browser.close()
            return
        res = page.evaluate(t2.FETCH_JS, [CONF["search"], {}])
        text = res.get("text") or ""
        hits = re.findall(CONF["hit"], text)
        log(step="inpage_search", status=res.get("status"), bytes=len(text), challenge=t1.signatures(text),
            hits=len(set(hits)))
        if hits and not t1.signatures(text):
            page.wait_for_timeout(20000)
            url = CONF["article"].format(hit=hits[0])
            res = page.evaluate(t2.FETCH_JS, [url, t2.article_headers(hits[0])])
            atext = res.get("text") or ""
            log(step="inpage_article", status=res.get("status"), bytes=len(atext), challenge=t1.signatures(atext))
        browser.close()
    log(step="done")


if __name__ == "__main__":
    main()
