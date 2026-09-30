"""HARVST first light: does the box IP pass again, and does collection work through a real browser tab?

Playbook `HARVST_BOT_OPS_PLAYBOOK_20260930.md` step 1, with the residential arm from
`HARVST_CRO_COO_H_SYNC_20260930.md` item 2. Per publisher, in order, stopping each ARM at its first challenge (a
challenge is recorded and NEVER interacted with):

  BOX-ANON   this box's own IP, a fresh anonymous browser: homepage (20 s)
  BOX-WARM   this box's IP, the stored session's cookies and user agent: homepage (20 s), then one search and one
             article issued FROM INSIDE the tab (fetch, credentials included)   -- only if BOX-ANON was clean
  RES-ANON   the Bright Data residential IP (Secrets astn/brightdata/residential-proxy, sticky US session, ASTN's
             pattern), a fresh anonymous browser: homepage (20 s), then one in-tab search. No login cookies travel over
             the residential route.

Publishers default to ft (positive control), bbg, wsj, barrons, ~60 s apart; steps ~20 s apart. Records statuses,
byte counts, challenge signatures and hit counts only -- no article text, no cookie or credential value, and the stored
session is never written back. Output: .runtime/harvest-first-light/<run_id>/<pub>.jsonl plus summary.json.

  --dry-run      every URL becomes https://example.com/ (mechanics only: browser, proxy wiring, logging)
  --publishers   comma list (default ft,bbg,wsj,barrons)
  --no-residential / --headless

Usage (workspace root, Python with playwright): python harvest_first_light.py [--dry-run] [--publishers ft]
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from playwright.sync_api import sync_playwright  # noqa: E402

AWS = r"C:\Users\Opal Bloomberg\AppData\Local\Programs\AWSCLIV2\Amazon\AWSCLIV2\aws.exe"
PUBLISHERS = {
    "ft": {"home": "https://www.ft.com/", "search": "https://www.ft.com/search?q=Apple",
           "hit": r'href="/content/([0-9a-f-]{36})"', "article": "https://www.ft.com/content/{hit}"},
    "bbg": {"home": "https://www.bloomberg.com/",
            "search": "https://www.bloomberg.com/nemo-next/api/search/query?query=%22Apple%22&page=1",
            "hit": r'"(?:resourceId|id)"\s*:\s*"([A-Z0-9]{12,20})"',
            "article": "https://www.bloomberg.com/article/api/story/id/{hit}?languagePreference=en"},
    "wsj": {"home": "https://www.wsj.com/", "search": "https://www.wsj.com/search?query=Apple",
            "hit": r'"articleUrl"\s*:\s*"(https://www\.wsj\.com/[^"]+)"', "article": "{hit}"},
    "barrons": {"home": "https://www.barrons.com/", "search": "https://www.barrons.com/search?query=Apple",
                "hit": r'"url"\s*:\s*"https://www\.barrons\.com/articles/([a-z0-9-]+-[0-9a-f]{8})"',
                "article": "https://www.barrons.com/articles/api/articles/{hit}"},
}
DRY = {"home": "https://example.com/", "search": "https://example.com/?q=Apple", "hit": r"(Example)",
       "article": "https://example.com/?a={hit}"}
CHALLENGE = {"perimeterx": ("px-captcha", "press &amp; hold", "press & hold", "human-challenge"),
             "datadome": ("captcha-delivery.com", "geo.captcha-delivery", "ct.captcha-delivery"),
             "cloudflare": ("challenges.cloudflare.com", "cf-chl", "just a moment", "cf_chl_opt"),
             "security_verification": ("security verification", "verify you are human", "are you a robot")}
FETCH_JS = """async ([url, headers]) => {
  try {
    const r = await fetch(url, {credentials: 'include', headers: headers || {}});
    const text = await r.text();
    return {status: r.status, text: text};
  } catch (e) { return {status: null, text: '', error: String(e)}; }
}"""


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def signatures(text):
    low = (text or "").lower()
    return sorted(k for k, marks in CHALLENGE.items() if any(m in low for m in marks))


class Run:
    def __init__(self, out):
        self.out = out
        self.out.mkdir(parents=True, exist_ok=True)
        self.summary = {}

    def log(self, pub, **row):
        row.update(publisher=pub, at=now().isoformat())
        with (self.out / f"{pub}.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
        print(json.dumps(row)[:300], flush=True)


def residential_proxy(session_id):
    raw = subprocess.run([AWS, "secretsmanager", "get-secret-value", "--secret-id", "astn/brightdata/residential-proxy",
                          "--query", "SecretString", "--output", "text"], capture_output=True, text=True, timeout=60)
    if raw.returncode != 0:
        return None
    s = json.loads(raw.stdout)
    return {"server": f"http://{s['host']}:{s['port']}",
            "username": f"{s['username']}-country-{s.get('country') or 'us'}-session-{session_id}",
            "password": s["password"]}


def stored_session(pub):
    from lib.opal_data_harvest.auth import SessionManager
    from lib.opal_data_harvest.sessions import TokenFirstSessions
    tf = TokenFirstSessions(SessionManager(".runtime/opal-data-harvest", lambda v: None), lambda v: None)
    env, _source = tf._stored_envelope(pub)
    if env is None:
        return [], None
    bundle = env.get("bundle") or {}
    raw = bundle.get("all_cookies")
    domain = "." + PUBLISHERS[pub]["home"].split("//")[1].strip("/").replace("www.", "")
    if raw is None:
        raw = [{"name": k, "value": v, "domain": domain, "path": "/"} for k, v in bundle.items()
               if isinstance(v, str) and k not in ("captured_at", "user_agent")]
    cookies = []
    for c in raw:
        if not c.get("name") or c.get("value") is None or not c.get("domain"):
            continue
        item = {"name": c["name"], "value": c["value"], "domain": c["domain"], "path": c.get("path") or "/"}
        exp = c.get("expires")
        if exp and float(exp) > 0:
            item["expires"] = float(exp)
        # __Secure-/__Host- cookies are refused without secure=True (rehearsal 2, bbg: "Invalid cookie fields").
        if c.get("secure") is not None or c["name"].startswith(("__Secure-", "__Host-")):
            item["secure"] = bool(c.get("secure", True))
        if c.get("httpOnly") is not None:
            item["httpOnly"] = bool(c["httpOnly"])
        if c.get("sameSite") in ("Strict", "Lax", "None"):
            item["sameSite"] = c["sameSite"]
        cookies.append(item)
    return cookies, bundle.get("user_agent")


def add_cookies(ctx, cookies):
    """Bulk add; on a refusal, add one by one and return how many were skipped (never a silent partial)."""
    try:
        ctx.add_cookies(cookies)
        return 0
    except Exception:  # noqa: BLE001 -- fall back to per-cookie adds so one bad cookie cannot void the session
        skipped = 0
        for item in cookies:
            try:
                ctx.add_cookies([item])
            except Exception:  # noqa: BLE001
                skipped += 1
        return skipped


def homepage(run, pub, arm, page, conf):
    resp = page.goto(conf["home"], wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(20000)
    sig = signatures(page.content())
    run.log(pub, arm=arm, step="homepage", status=resp.status if resp else None, title=(page.title() or "")[:70],
            challenge=sig)
    return not sig


def inpage(run, pub, arm, page, step, url, conf, headers=None):
    res = page.evaluate(FETCH_JS, [url, headers or {}])
    if res.get("status") is None and res.get("error"):
        # A NETWORK-level failure (no HTTP response at all, e.g. an idle proxy connection dropped) is retried once;
        # an HTTP answer -- including any challenge -- never is.
        run.log(pub, arm=arm, step=step + "_network_retry", error=res.get("error"))
        page.wait_for_timeout(2000)
        res = page.evaluate(FETCH_JS, [url, headers or {}])
    text = res.get("text") or ""
    hits = re.findall(conf["hit"], text)
    sig = signatures(text)
    run.log(pub, arm=arm, step=step, path=re.sub(r"https?://[^/]+", "", url)[:80], status=res.get("status"),
            bytes=len(text), challenge=sig, hits=len(set(hits)), error=res.get("error"))
    ok = res.get("status") == 200 and not sig
    return ok, (hits[0] if hits else None)


def publisher(run, p, pub, conf, args, dry):
    result = {}
    # BOX-ANON
    browser = p.chromium.launch(channel="chrome", headless=args.headless)
    try:
        page = browser.new_context().new_page()
        result["box_anon_home"] = homepage(run, pub, "BOX-ANON", page, conf)
    finally:
        browser.close()
    # BOX-WARM (only on a clean box IP)
    if result["box_anon_home"]:
        time.sleep(20)
        # The dry run still loads and injects the real stored session (exercising the loader), but only visits
        # example.com, so no publisher is contacted.
        cookies, ua = stored_session(pub) if pub in PUBLISHERS else ([], None)
        browser = p.chromium.launch(channel="chrome", headless=args.headless)
        try:
            ctx = browser.new_context(user_agent=ua) if ua else browser.new_context()
            skipped = add_cookies(ctx, cookies) if cookies else 0
            run.log(pub, arm="BOX-WARM", step="session", stored_cookies=len(cookies), cookies_skipped=skipped,
                    user_agent_present=bool(ua))
            page = ctx.new_page()
            result["box_warm_home"] = homepage(run, pub, "BOX-WARM", page, conf)
            if result["box_warm_home"]:
                page.wait_for_timeout(20000)
                ok, hit = inpage(run, pub, "BOX-WARM", page, "inpage_search", conf["search"], conf)
                result["box_inpage_search"] = ok
                if ok and hit:
                    page.wait_for_timeout(20000)
                    headers = ({"Accept": "application/json", "x-nextjs-data": "1",
                                "Referer": "https://www.barrons.com/articles/" + hit} if pub == "barrons" and not dry else None)
                    ok2, _ = inpage(run, pub, "BOX-WARM", page, "inpage_article", conf["article"].format(hit=hit), conf, headers)
                    result["box_inpage_article"] = ok2
        finally:
            browser.close()
    # RES-ANON
    if not args.no_residential:
        time.sleep(20)
        proxy = residential_proxy("firstlight" + now().strftime("%H%M"))
        if proxy is None:
            run.log(pub, arm="RES-ANON", step="proxy", error="residential proxy credential unavailable")
        else:
            browser = p.chromium.launch(channel="chrome", headless=args.headless, proxy=proxy)
            try:
                ctx = browser.new_context(ignore_https_errors=True)
                page = ctx.new_page()
                result["res_anon_home"] = homepage(run, pub, "RES-ANON", page, conf)
                if result["res_anon_home"]:
                    page.wait_for_timeout(20000)
                    ok, _ = inpage(run, pub, "RES-ANON", page, "inpage_search", conf["search"], conf)
                    result["res_inpage_search"] = ok
            except Exception as exc:  # noqa: BLE001 -- a failed proxy leg is a recorded result
                run.log(pub, arm="RES-ANON", step="error", error=type(exc).__name__, detail=str(exc)[:160])
            finally:
                browser.close()
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--publishers", default="ft,bbg,wsj,barrons")
    ap.add_argument("--no-residential", action="store_true",
                    help="omit the Bright Data residential arm (held by 2.0.0_SA_COO~H pending a CTO ruling, msg 27390)")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--out", default=".runtime/harvest-first-light")
    args = ap.parse_args()
    run_id = now().strftime("%Y%m%dT%H%M%SZ") + ("-dry" if args.dry_run else "")
    run = Run(Path(args.out) / run_id)
    pubs = [x for x in args.publishers.split(",") if x]
    with sync_playwright() as p:
        for i, pub in enumerate(pubs):
            if i:
                time.sleep(60)
            conf = DRY if args.dry_run else PUBLISHERS[pub]
            try:
                run.summary[pub] = publisher(run, p, pub, conf, args, args.dry_run)
            except Exception as exc:  # noqa: BLE001 -- one publisher's failure never stops the next
                run.log(pub, arm="RUN", step="error", error=type(exc).__name__, detail=str(exc)[:200])
                run.summary[pub] = {"error": type(exc).__name__}
    (run.out / "summary.json").write_text(json.dumps({"run_id": run_id, "results": run.summary}, indent=1), encoding="utf-8")
    print("SUMMARY", json.dumps(run.summary), flush=True)


if __name__ == "__main__":
    main()
