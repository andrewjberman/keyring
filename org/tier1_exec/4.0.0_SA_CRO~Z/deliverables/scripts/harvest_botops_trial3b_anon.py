"""HARVST bot-operations trial 3b: a completely fresh anonymous browser (no cookies at all), same box and IP.

Homepage load (20 s), then one in-page search if the homepage is not challenged. Separates an IP-level flag from a
cookie- or account-level one (trial 3 already stripped the bot-manager cookies). Records only; a challenge is never
interacted with. Output: .runtime/harvest-botops-trial-20260930/<pub>-t3b.jsonl

Usage (workspace root): python harvest_botops_trial3b_anon.py bbg|wsj|barrons|ft
"""
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from playwright.sync_api import sync_playwright  # noqa: E402

import harvest_botops_trial as t1  # noqa: E402
import harvest_botops_trial2 as t2  # noqa: E402

LOG = t1.OUT / f"{t1.PUB}-t3b.jsonl"


def log(**row):
    row["at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
    print(json.dumps(row)[:300], flush=True)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_context().new_page()
        page.goto(t1.CONF["home"], wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(20000)
        sig = t1.signatures(page.content())
        log(step="anon_warmup", challenge=sig)
        if not sig:
            res = page.evaluate(t2.FETCH_JS, [t1.CONF["search"], {}])
            text = res.get("text") or ""
            log(step="anon_inpage_search", status=res.get("status"), bytes=len(text),
                challenge=t1.signatures(text), hits=len(set(re.findall(t1.CONF["hit"], text))))
        browser.close()


if __name__ == "__main__":
    main()
