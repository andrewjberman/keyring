# Seeking Alpha / Financial Times / WSJ / Bloomberg -- endpoint reference for future agents

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-11 | **For:** any agent consuming these four platforms
**Mechanism briefs (read these for the full "how we got here" story, real bugs, and root causes):**
`SEEKING_ALPHA_AUTOMATED_AUTH_MECHANISM_20260911.md`, `FT_AUTOMATED_AUTH_MECHANISM_20260911.md`,
`WSJ_DATA_ACCESS_MECHANISM_20260911.md`, `BLOOMBERG_AUTOMATED_AUTH_MECHANISM_20260911.md` (all in
this same `deliverables/` directory).

**This document's job is different from the briefs above: it is a practical lookup table** -- every
known endpoint, its exact shape, and what a future agent should and shouldn't do, with no narrative.
Every fact below traces to a brief cited next to it; this file adds nothing new, it only re-shapes
what is already proven into a form meant for fast lookup and machine parsing.

---

## 0. Read this before calling anything

1. **Never log in inline.** Every REST consumer below rides a PARKED session from Secrets Manager. If
   a call comes back unauthorized, the fix is re-running the matching `*_harvest_session.py`, not
   hand-rolling a login inside a REST script.
2. **Never print or log a credential, cookie, or token VALUE.** Every script referenced here follows
   this; keep following it in anything new built on top of them.
3. **A vendor call (Bright Data, NopeCHA, the sites themselves) needs Andrew's per-use word.**
   Availability of a working script is not standing authorization to run it on a schedule.
4. **A `403`/`404` is not automatically "broken."** Read the matching brief's own findings before
   concluding an endpoint has changed -- e.g. Seeking Alpha's 403-with-`blockScript` is a re-harvest
   signal, not an auth failure; several endpoints below are explicitly marked NOT PROVEN rather than
   guessed at.
5. **Egress requirements differ per platform** -- Seeking Alpha and FT need the Bright Data
   residential proxy; WSJ needs the Bright Data Web Unlocker; Bloomberg needs neither (native IP
   works). Check the `"egress"` field per platform below before assuming one recipe fits all four.

---

## 1. Seeking Alpha

```json
{
  "platform": "seeking-alpha",
  "auth_mechanism": "PerimeterX Press & Hold + email/password login",
  "harvester": "org/tier1_exec/4.0.0_SA_CRO/scripts/sa_harvest_session.py",
  "rest_client": "org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py",
  "session_secret": "seeking-alpha/session",
  "credential_secret": "seeking-alpha/credentials",
  "egress": "Bright Data residential proxy (astn/brightdata/residential-proxy) -- required for REST reads; native IP gets PerimeterX-blocked after ~10 calls",
  "identity_cookies_minimum": ["user_id", "session_id", "user_remember_token", "user_cookie_key"],
  "identity_cookies_full_pass_set": ["user_id", "session_id", "user_remember_token", "user_cookie_key", "_px3", "_pxvid", "pxcts", "_pxde"],
  "required_headers": {"Referer": "must be a real per-page Referer -- omitting it returns HTTP 200 with a 2-byte body, a silent-empty trap"},
  "endpoints": [
    {"name": "check", "method": "GET", "path": "/api/v3/account/{userId}/info", "params": {"include": "proSubscription"}, "proven": true, "returns": "account + subscription status"},
    {"name": "symbol", "method": "GET", "path": "/api/v3/symbols/{ticker}", "params": {}, "proven": true, "returns": "symbol record; carries the internal sa_id used by report"},
    {"name": "report", "method": "GET", "path": "/api/v3/virtual_analysts/{sa_id}", "params": {}, "proven": true, "returns": "the virtual_analyst_report modal's actual data: responseContent (markdown analysis), ratingsResponse, createdAt, previousReportDate"},
    {"name": "article", "method": "GET", "path": "/api/v3/articles/{id}", "params": {"include": "author"}, "proven": true, "returns": "full article body for a paying user"},
    {"name": "analysis_list", "method": "GET", "path": "/api/v3/symbols/{ticker}/analysis (or similar listing)", "params": {"limit": "N"}, "proven": "partially -- see sa_rest_fetch.py usage line", "returns": "recent analysis list"}
  ],
  "known_not_found": ["a stable news-tab-style endpoint distinct from articles was not separately confirmed"],
  "re_harvest_signal": "HTTP 403 with 'blockScript' in the body means the PX cookies aged out -- re-run sa_harvest_session.py. A 403 WITHOUT that string is a real auth failure, not a re-harvest case."
}
```

**Ticker -> data flow:** `symbol {ticker}` -> `data.id` (the `sa_id`) -> `report {sa_id}` (the actual
analysis content). This two-step resolution is required; there is no single per-ticker report endpoint.

## 2. Financial Times

```json
{
  "platform": "financial-times",
  "auth_mechanism": "hCaptcha + email/password login (solved via NopeCHA Token API)",
  "harvester": "org/tier1_exec/4.0.0_SA_CRO/scripts/ft_harvest_session.py",
  "rest_client": "org/tier1_exec/4.0.0_SA_CRO/scripts/ft_rest_fetch.py",
  "session_secret": "astn/ft/session",
  "credential_secret": "astn/ft/credentials",
  "captcha_solver_secret": "nopecha/api-key",
  "captcha_solver_module": "org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py",
  "egress": "Bright Data residential proxy (astn/brightdata/residential-proxy) for READS; the harvester login step itself runs on native IP (the residential zone refuses ALL POST requests -- policy_20130, no-KYC restriction)",
  "identity_cookies": ["FTSession", "FTSession_s"],
  "endpoints": [
    {"name": "listing", "method": "GET", "path": "https://www.ft.com/{section}", "params": {"sections_proven": ["companies", "markets", "global-economy"]}, "proven": true, "returns": "article links"},
    {"name": "article", "method": "GET", "path": "<any FT article URL>", "params": {}, "proven": true, "returns": "full paywalled article body in raw server-rendered HTML -- measured 36,237 chars, no paywall marker, works both through the proxy and on native IP"},
    {"name": "quote_summary", "method": "GET", "path": "https://markets.ft.com/data/equities/tearsheet/summary", "params": {"s": "{TICKER}:{EXCHANGE}"}, "proven": true, "returns": "equity tearsheet summary"},
    {"name": "quote_profile", "method": "GET", "path": "https://markets.ft.com/data/equities/tearsheet/profile", "params": {"s": "{TICKER}:{EXCHANGE}"}, "proven": true, "returns": "equity tearsheet profile"}
  ],
  "known_not_found": [
    {"endpoint": "markets.ft.com/data/equities/tearsheet/news", "status": "every URL shape tried returned an FT-side error page -- a NOT-FOUND, not proof it doesn't exist"},
    {"endpoint": "ft.com/search", "status": "REFUSED at the proxy (policy-shaped block, not merely empty) -- do not treat a 402 here as 'no results'"}
  ],
  "hcaptcha_fix_history": "nopecha.api_key = ... is a DEAD ASSIGNMENT against installed nopecha>=2.0 (module __getattr__ never fires on writes) -- use os.environ['NOPECHA_API_KEY'] instead. Token.solve() returns the raw {\"data\": \"<token>\"} dict, not a bare string. FT's hCaptcha reads completion via a registered data-callback ('onSocialSubmit'), not the response textarea alone -- invoke it directly. Full history in FT_AUTOMATED_AUTH_MECHANISM_20260911.md."
}
```

## 3. Wall Street Journal

```json
{
  "platform": "wsj",
  "auth_mechanism": "NONE -- cookieless, public content only",
  "harvester": null,
  "rest_client": "org/tier1_exec/4.0.0_SA_CRO/scripts/wsj_rest_fetch.py",
  "session_secret": null,
  "credential_secret": null,
  "egress": "Bright Data Web Unlocker (zone=one_shotter), key at brightdata-api-key",
  "note": "Every page fetched via WSJ is tagged \"user_type\": \"nonsubscriber\" in its own embedded state -- this path never reaches paywalled content. That is correct scope, not a limitation to route around; see WSJ_DATA_ACCESS_MECHANISM_20260911.md s.3.",
  "endpoints": [
    {"name": "listing", "method": "GET", "path": "https://www.wsj.com/news/{section}", "params": {"sections_proven": ["home", "markets", "economy", "business", "finance"]}, "proven": true, "returns": "article links"},
    {"name": "article", "method": "GET", "path": "<any WSJ article URL>", "params": {}, "proven": true, "returns": "full public article text"},
    {"name": "quote", "method": "GET", "path": "https://www.wsj.com/market-data/quotes/{TICKER}", "params": {}, "proven": true, "returns": "public per-ticker quote page"},
    {"name": "quote_news", "method": "extraction from quote page's window.__STATE__", "path": "key shaped quotes_latestNews_{\"ticker\":\"{TICKER}\",...}.data.data.news", "params": {}, "proven": "intermittent -- present on one fetch, absent on an immediate repeat of the identical URL (a Bright Data snapshot timing/hydration race, not a stable feature)", "returns": "per-ticker news array when present"}
  ],
  "known_not_found": [{"endpoint": "wsj.com/search", "status": "252-byte near-empty client-rendered shell over plain REST -- needs a real browser, do not build on it"}]
}
```

## 4. Bloomberg

```json
{
  "platform": "bloomberg",
  "auth_mechanism": "PerimeterX Press & Hold + Google OAuth sign-in (via an iframe-hosted method chooser)",
  "harvester": "org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_harvest_session.py",
  "rest_client": "org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py",
  "session_secret": "bloomberg/session",
  "credential_secret": null,
  "google_credential_secret": "google/andrew-goldengate/credentials",
  "google_oauth_handler": "org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py",
  "captcha_press_hold_module": "org/tier1_exec/4.0.0_SA_CRO/scripts/press_and_hold_lib.py",
  "captcha_hcaptcha_module": "org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py",
  "egress": "native IP -- no proxy required, measured clean on every call so far",
  "identity_cookies": ["_user-id", "_user-token", "_user-jwt", "_user-role", "_breg-uid", "_breg-user", "_last-refresh", "session_id", "session_key", "agent_id", "gatehouse_id"],
  "sign_in_iframe_selector": "#reg-ui-client__iframe (src=https://www.bloomberg.com/account/iframe/login) -- the ENTIRE sign-in-method chooser lives inside this iframe, not the top-level page. Any future selector work on Bloomberg's login MUST use page.frame_locator(), not page.locator().",
  "endpoints": [
    {"name": "check", "method": "GET", "path": "https://login.bloomberg.com/user-info", "params": {"withSubscriberData": "true", "activeSubscriptionsOnly": "false"}, "proven": true, "returns": "userId, email, name, sessionId, subscriptionType (e.g. 'BBG'), subscriptions[]"},
    {"name": "ticker", "method": "GET", "path": "https://www.bloomberg.com/nemo-next/api/tickers", "params": {"ids": "{TICKER}:{EXCHANGE}"}, "proven": true, "returns": "id, name, longName, price, percentChange1Day, type, realTimeTickerDescription"},
    {"name": "news", "method": "GET", "path": "https://www.bloomberg.com/bazaar/api/chart-news/{TICKER}:{EXCHANGE}", "params": {"targetDate": "ISO8601 UTC", "dateRange": "1D (observed enum value)", "endDate": "ISO8601 UTC with .000 millis", "name": "'+'-joined display name, e.g. RTX+CORP", "unresolved_param": "at least one further parameter was truncated in the discovery sniff log ('sta...') and never fully captured"}, "proven": false, "returns": "per-ticker news tied to the chart widget -- a hand-built call 404'd; the real request's exact trigger and full parameter set need a CDP/HAR capture, not another response-log sniff"}
  ],
  "known_not_found": [],
  "exchange_suffixes_observed_for_RTX": ["US", "CI", "SW", "AV", "DC"]
}
```

---

## 5. For the next agent who needs to extend or repair any of this

- **A login flow breaking is very likely a selector/DOM-shape change, not a fundamentally new
  obstacle.** Before rewriting logic, dump the actual DOM (`page.evaluate("() => document.body.outerHTML")`
  or the `dump_modal_html` pattern in `bloomberg_harvest_session.py`) rather than guessing from a
  screenshot -- the single biggest time cost in this investigation was assuming DOM structure that
  turned out to be wrong (an iframe nobody suspected).
- **The press-and-hold and hCaptcha mechanisms are shared modules on purpose.** If you find a new
  behavior of either captcha type on a fifth platform, fix it in `press_and_hold_lib.py` or
  `nopecha_hcaptcha_lib.py`, not in a site-specific copy -- every consumer benefits immediately.
- **The network-level completion oracle (a real `Set-Cookie` event, not a cookie-jar snapshot) is the
  bar for "done."** Extend `TRACKED_COOKIE_NAMES`-style lists with real, measured cookie names as soon
  as a platform's identity cookies are known -- recording every cookie (the necessary first-pass
  approach on a brand-new platform) both floods logs and can overflow Secrets Manager's size limit.
- **A defense that keeps re-challenging after a mechanically correct solve is escalation, not a bug.**
  Both Seeking Alpha and Bloomberg showed this after roughly 7-8 live attempts within an hour. Space
  out live testing rather than retrying immediately when this happens.
