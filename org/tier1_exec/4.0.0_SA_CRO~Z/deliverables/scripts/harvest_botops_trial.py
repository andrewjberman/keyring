"""HARVST bot-operations trial: does a real-browser warm-up clear the cold-start challenge, and how long does it last?

Andrew-direct 2026-09-30 ("Yes do it"), after HARVST_BOT_OPS_STUDY_20260930.md. One publisher per process:

  t0      warm-up: headed Google Chrome on this box's own connection, the stored session's cookies and
          user agent loaded, the homepage opened and left 20 s for the site's own scripts. A challenge
          on the page is RECORDED and the publisher stops -- nothing is clicked, held or solved.
  t0+     REST phase 1 with the production client (curl_cffi, Chrome impersonation, same user agent)
          and the cookies exported from the warm browser: auth check (if the publisher has one),
          one search, one article. ~20 s apart.
  t0+6m   trust window: the same search twice -- once with the t0 cookies (stale arm), once with
          cookies re-exported from the still-open tab (live arm).
  t0+12m  re-warm: one ordinary reload of the homepage, then the search with fresh cookies.

Records statuses, content types, byte counts, challenge signatures, hit counts and trust-cookie expiry
per step. Stores no article text, prints no cookie or credential value, and never writes the stored
session back (read-only trial). Output: .runtime/harvest-botops-trial-20260930/<pub>.jsonl

Usage (workspace root): python harvest_botops_trial.py bbg|wsj|barrons|ft
"""
import datetime
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
from curl_cffi import requests as creq  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

from lib.opal_data_harvest.auth import SessionManager  # noqa: E402
from lib.opal_data_harvest.sessions import TokenFirstSessions  # noqa: E402

PUB = sys.argv[1]
OUT = Path(".runtime/harvest-botops-trial-20260930")
OUT.mkdir(parents=True, exist_ok=True)
LOG = OUT / f"{PUB}.jsonl"
PACE = 20
QUERY = "Apple"

CONF = {
    "bbg": {"home": "https://www.bloomberg.com/",
            "auth": "https://login.bloomberg.com/user-info?withSubscriberData=true&activeSubscriptionsOnly=false",
            "search": f"https://www.bloomberg.com/nemo-next/api/search/query?query=%22{QUERY}%22&page=1",
            "hit": r'"(?:resourceId|id)"\s*:\s*"([A-Z0-9]{12,20})"',
            "article": "https://www.bloomberg.com/article/api/story/id/{hit}?languagePreference=en",
            "domain": ".bloomberg.com"},
    "wsj": {"home": "https://www.wsj.com/", "auth": "https://www.wsj.com/client?legacy=false",
            "search": f"https://www.wsj.com/search?query={QUERY}",
            "hit": r'"articleUrl"\s*:\s*"(https://www\.wsj\.com/[^"]+)"', "article": "{hit}", "domain": ".wsj.com"},
    "barrons": {"home": "https://www.barrons.com/", "auth": "https://www.barrons.com/client?legacy=false",
                "search": f"https://www.barrons.com/search?query={QUERY}",
                "hit": r'"url"\s*:\s*"https://www\.barrons\.com/articles/([a-z0-9-]+-[0-9a-f]{8})"',
                "article": "https://www.barrons.com/articles/api/articles/{hit}", "domain": ".barrons.com"},
    "ft": {"home": "https://www.ft.com/", "auth": None, "search": f"https://www.ft.com/search?q={QUERY}",
           "hit": r'href="/content/([0-9a-f-]{36})"', "article": "https://www.ft.com/content/{hit}", "domain": ".ft.com"},
}[PUB]

CHALLENGE = {"perimeterx": ("px-captcha", "press &amp; hold", "press & hold", "human-challenge"),
             "datadome": ("captcha-delivery.com", "geo.captcha-delivery", "ct.captcha-delivery"),
             "cloudflare": ("challenges.cloudflare.com", "cf-chl", "just a moment", "cf_chl_opt"),
             "security_verification": ("security verification", "verify you are human", "are you a robot")}
TRUST_PREFIX = ("_px", "pxcts", "datadome", "__cf_bm", "cf_clearance")


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def log(**row):
    row["at"] = now().isoformat()
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
    print(json.dumps(row)[:400], flush=True)


def signatures(text):
    low = (text or "").lower()
    return sorted(kind for kind, marks in CHALLENGE.items() if any(m in low for m in marks))


def trust_state(cookies):
    t = now().timestamp()
    out = {}
    for c in cookies:
        name = c.get("name", "")
        if name.startswith(TRUST_PREFIX):
            exp = c.get("expires")
            out[name] = "session" if not exp or float(exp) <= 0 else round((float(exp) - t) / 60, 1)
    return out  # minutes to expiry (negative = expired); never a value


def stored_envelope():
    tf = TokenFirstSessions(SessionManager(".runtime/opal-data-harvest", lambda v: None), lambda v: None)
    env, source = tf._stored_envelope(PUB)
    if env is None:
        raise SystemExit("no stored session for " + PUB)
    bundle = env.get("bundle") or {}
    raw = bundle.get("all_cookies")
    if raw is None:  # FT's flat name->value shape
        raw = [{"name": k, "value": v, "domain": CONF["domain"], "path": "/"} for k, v in bundle.items()
               if isinstance(v, str) and k not in ("captured_at", "user_agent")]
    return raw, bundle.get("user_agent"), source.split(":")[0]


def to_playwright(cookies):
    out = []
    for c in cookies:
        if not c.get("name") or c.get("value") is None or not c.get("domain"):
            continue
        item = {"name": c["name"], "value": c["value"], "domain": c["domain"], "path": c.get("path") or "/"}
        exp = c.get("expires")
        if exp and float(exp) > 0:
            item["expires"] = float(exp)
        if c.get("secure") is not None:
            item["secure"] = bool(c["secure"])
        if c.get("httpOnly") is not None:
            item["httpOnly"] = bool(c["httpOnly"])
        if c.get("sameSite") in ("Strict", "Lax", "None"):
            item["sameSite"] = c["sameSite"]
        out.append(item)
    return out


def rest(step, url, cookies, ua, extra=None):
    headers = {"User-Agent": ua} if ua else {}
    headers.update(extra or {})
    s = creq.Session(impersonate="chrome", timeout=45, headers=headers)
    for c in cookies:
        if c.get("name") and c.get("value") is not None:
            s.cookies.set(c["name"], c["value"], domain=c.get("domain") or CONF["domain"], path=c.get("path") or "/")
    try:
        r = s.get(url)
        body = r.text or ""
        hits = re.findall(CONF["hit"], body)
        log(step=step, path=re.sub(r"https?://[^/]+", "", url)[:90], status=r.status_code,
            content_type=(r.headers.get("content-type") or "")[:40], bytes=len(r.content or b""),
            challenge=signatures(body), hits=len(set(hits)))
        return r.status_code, (hits[0] if hits else None)
    except Exception as exc:  # noqa: BLE001 -- a trial records a failed call as a result
        log(step=step, path=url[:90], error=type(exc).__name__, detail=str(exc)[:160])
        return None, None


def main():
    stored, ua, source = stored_envelope()
    log(step="stored_session", source=source, n_cookies=len(stored), user_agent_present=bool(ua),
        trust_cookies_minutes_left=trust_state(stored))
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        ctx = browser.new_context(user_agent=ua) if ua else browser.new_context()
        ctx.add_cookies(to_playwright(stored))
        page = ctx.new_page()
        t0 = time.monotonic()
        page.goto(CONF["home"], wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(20000)
        html = page.content()
        sig = signatures(html)
        page.screenshot(path=str(OUT / f"{PUB}-warmup.png"))
        warm = ctx.cookies()
        log(step="warmup", url=page.url[:90], title=(page.title() or "")[:80], challenge=sig,
            trust_cookies_minutes_left=trust_state(warm))
        if sig:
            log(step="stop", reason="challenge on warm-up page; not interacted with")
            browser.close()
            return
        ua_live = page.evaluate("navigator.userAgent")
        if CONF["auth"]:
            rest("rest1_auth", CONF["auth"], warm, ua_live)
            time.sleep(PACE)
        status, hit = rest("rest1_search", CONF["search"], warm, ua_live)
        time.sleep(PACE)
        if hit:
            extra = {"Accept": "application/json", "x-nextjs-data": "1",
                     "Referer": "https://www.barrons.com/articles/" + hit} if PUB == "barrons" else None
            rest("rest1_article", CONF["article"].format(hit=hit), warm, ua_live, extra)
        else:
            log(step="rest1_article", skipped="no hit parsed from search")
        while time.monotonic() - t0 < 360:
            page.wait_for_timeout(15000)
        rest("t6_stale_cookies", CONF["search"], warm, ua_live)
        time.sleep(PACE)
        live = ctx.cookies()
        log(step="t6_live_cookie_state", trust_cookies_minutes_left=trust_state(live))
        rest("t6_live_cookies", CONF["search"], live, ua_live)
        while time.monotonic() - t0 < 720:
            page.wait_for_timeout(15000)
        page.reload(wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(10000)
        sig2 = signatures(page.content())
        rewarm = ctx.cookies()
        log(step="t12_reload", challenge=sig2, trust_cookies_minutes_left=trust_state(rewarm))
        if not sig2:
            rest("t12_after_reload", CONF["search"], rewarm, ua_live)
        browser.close()
    log(step="done")


if __name__ == "__main__":
    main()
