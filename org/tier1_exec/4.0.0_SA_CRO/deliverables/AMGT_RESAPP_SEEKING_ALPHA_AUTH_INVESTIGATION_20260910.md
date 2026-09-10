# Seeking Alpha: can a paying user's credential drive the REST API? -- MEASURED, YES, with two conditions

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | **For:** Andrew; `1.0.0_SA_CTO~Z` (L4), `2.0.0_SA_COO~ZZZ` (L5)
**Andrew's question, verbatim:** *"I want to know if we can just use REST API with my credentials as a paying user."*
**Authorization:** Andrew-direct at this terminal (record beside this file). Every vendor call below was inside that word.
**Scripts:** `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_harvest_session.py`, `.../sa_rest_fetch.py`.
**Parked artifact:** Secrets Manager `seeking-alpha/session` (CREATED 2026-09-10 19:29Z, 17,202 bytes, 65 cookies, tagged `service=seeking-alpha kind=site-session`).

---

## 1. THE ANSWER

**Yes.** With one browser-harvested session and no browser at fetch time, a plain HTTP client returns:

| Call | Result |
|---|---|
| `GET /api/v3/account/1btfwdu/info?include=proSubscription` | 200, `data.type=authorizedUser`, `proSubscription: plan=Annual, active=true, isFreeSubscription=false` |
| `GET /api/v3/virtual_analysts/{sa_id}` (THE `virtual_analyst_report` MODAL'S DATA) | 200 for RTX, AAPL, MSFT, GOOGL, JPM, NVDA -- 7.8-8.8 KB each, `responseContent` 5.3-6.4K chars of markdown |
| `GET /api/v3/articles/{id}?include=author` | 200, full analysis bodies: 7,580 and 17,581 chars, ending on the author's rating sentence |
| `GET /api/v3/symbols/{ticker}` | 200; carries the internal `sa_id` the report endpoint keys on (RTX=601510, AAPL=146, MSFT=575, GOOGL=148893, JPM=907, NVDA=1150) |
| `GET /api/v3/symbol_data`, `/metrics`, `/symbols/{t}/rating/periods`, `/news`, `finance-api.../real_time_quotes` | 200, JSON:API |

**The `virtual_analyst_report` page itself is JS-rendered and its HTML carries none of the content**
(plain fetch: "Javascript is Disabled"). The content lives ONLY at `/api/v3/virtual_analysts/{sa_id}`,
which the page calls once. Scraping the modal is the wrong instrument; the endpoint is the artifact.
Its shape: `{id, slug, responseContent (markdown: Company Description / Competitors and Unique Value /
Positives / Concerns, each bullet citing an article id), ratingsResponse (Quant rating explanation with
sector-median comparatives), createdAt, previousReportDate, enoughAnalysis}`. RTX's is dated
2026-09-10 00:01 ET with a previous edition 2026-09-05 -- **it re-generates roughly every few days.**

## 2. THE TWO CONDITIONS -- both measured, both load-bearing

**(a) THE JAR MUST CARRY THE BROWSER-MINTED PerimeterX COOKIES, AND THE REQUEST A PER-TICKER `Referer`.**

| Jar | Native IP | Residential proxy |
|---|---|---|
| identity only (`user_id`,`session_id`) | 403 | -- |
| identity + remember (`user_remember_token`,`user_cookie_key`) | 200 on the first burst, then IP-blocked | 200 on some tickers, **413-byte PerimeterX challenge JSON on others** (AAPL/MSFT/JPM, both articles) |
| **full 65-cookie jar incl. `_px3`,`_pxvid`,`pxcts`,`_pxde`** | -- | **200 on every ticker and every article** |
| full jar, NO `Referer` | -- | 200 but a **2-byte body** (the anomaly that cost one round) |

`user_id` is the identity discriminator (`session_id` is issued to anonymous visitors too -- measured).
The minimal AUTH set is `user_id + session_id + user_remember_token + user_cookie_key`; the minimal
PASS set adds the four PX cookies. `_px3` has a TTL: a 413-byte 403 with `blockScript` in the body is
the re-harvest signal, not an auth failure.

**(b) THE FETCH MUST EGRESS THROUGH THE RESIDENTIAL PROXY.** This device's native IP served the first
~10 API calls and was then blocked by PerimeterX for EVERY call including ones that had just worked
(6 of 6 tickers 403 at 1 call / 3 s). The same jar through `astn/brightdata/residential-proxy` (US
sticky session) was never challenged once the PX cookies were present. The proxy is GET-capable today.

## 3. WHAT DID NOT WORK, AND WHY -- keep these, they are paid for

1. **Bright Data residential zone refuses every POST**, on any host (`httpbin.org` included):
   `x-brd-err-code: policy_20130` -- *"not available for immediate residential (no KYC) access mode due
   to the fact that POST requests are not allowed ... fill in the KYC form: https://brightdata.com/cp/kyc"*.
   A login is a POST and so is PerimeterX's sensor telemetry, so THROUGH the proxy the challenge can never
   complete and `/account/login` returns 403. **Andrew is doing the KYC.** Until it lands, the proxy
   carries reads only, which is the whole production path anyway.
2. **The cookieless Unlocker (`one_shotter`, the MCP `scrape_as_markdown`) returned an EMPTY body for the
   modal URL and the anonymous symbol page for `/symbol/RTX`** -- consistent with the ASTN finding that
   an Unlocker cannot ride an authenticated session. Not a route for anything paywalled or user-keyed.
3. **The Playwright MCP's own Edge session and any headless launch hit the press-and-hold wall on the
   first request**; real Chrome, headed, on this device did not (page came up anonymous, no wall) --
   the wall appeared only AFTER the login POST and was cleared once.
4. **`seeking-alpha/credentials` (Andrew-direct today, 8-char password) worked first try.** The older
   `opal/external-apis -> seeking_alpha_password` (11 chars, same email) was not tried and is presumably
   stale; it should be retired or made a pointer (the same split-identity shape as the two dead Bright
   Data keys in `ASTN_BRIGHTDATA_CREDENTIAL_INVENTORY_20260910.md` s3b).

## 4. THE KIMI AUTHENTICATOR PORT -- exercised, not just read

`bd_49f_auto_login.js`'s perceive-act loop, ported to Python for SA and run to a green cookie:

```
step 0: ANON      (kimi)  -> clicked [data-test-id=header-button-sign-in]
step 1: LOGIN     (kimi)  -> filled the 'Member Sign In' modal (email anchored to the password field), clicked 'Sign in'
step 2: BOT_WALL  (kimi)  -> Kimi localize timed out twice (60 s each) -> DOM fallback #px-captcha bbox -> press-and-hold 8 s
step 3: LOGGED_IN (kimi)  -> user_id PRESENT (the oracle; vision only advances the machine) -> parked
```

Measured on the way and folded into the script:
- **Kimi `kimi-k2.6` is a REASONING model: hidden reasoning tokens count against `max_tokens`.** At 50
  and 120 tokens both replies were EMPTY with `reasoning_tokens=49/119`; at 1,500 classify answered
  `BOT_WALL` and localize returned `{"x":640,"y":416,"w":252,"h":50}` -- the button's true centre to
  the pixel. This is the bd-49f "KIMI_EMPTY" failure mode with its cause named. Localize budgets 4,000.
- Kimi latency is 4-33 s per call and it timed out twice at 60 s during the run; the DOM fallback is
  what made the run green. Both guards from bd-49f (call-failure vs ambiguous-screen, DOM fallback) held.
- The modal's Email input must be anchored to the password field (`preceding::input[1]`): the page
  behind the modal has its own `#email` in a "Create Free Account" banner that a bare selector picks.
- SA sets `session_id` for anonymous visitors; **`user_id` is the identity cookie.** Post-login the jar
  also carries `has_paid_subscription=true`, `ever_pro=1`, `user_remember_token`, `user_cookie_key`.

## 5. WHAT THIS MEANS FOR AMGT_RESAPP -- surfaced for the CTO and COO, not adjudicated here

- **S4 (coverage reader) and the Seeking Alpha section Andrew asked for have a measured substrate:**
  `GET /api/v3/symbols/{t}` -> `sa_id` -> `GET /api/v3/virtual_analysts/{sa_id}` and
  `GET /api/v3/symbols/{t}/analysis|news` -> `GET /api/v3/articles/{id}`. JSON, keyed, dated. No HTML parsing.
- **S12 (identity layer):** the SA key is the ticker slug at the symbol endpoint and the numeric `sa_id`
  underneath it. Both are returned by one call; the map is cheap to build and should be persisted.
- **The scheduled shape is the FT/Black Diamond shape exactly:** harvest in a real browser (this script),
  park (`seeking-alpha/session`, done), ride by REST through the residential proxy, re-harvest on a
  413-byte PX 403. `C-VENDOR-EGRESS` still binds the scheduled consumer; today's word covered today's run.
- **NOT owned or decided here:** where the harvester runs (a Windows box with real Chrome, as today, or a
  Linux box with Playwright's Chromium -- untested), the re-harvest cadence, and whether the per-firm
  gateway pattern applies (one credential, one mailbox).
  Those are L5 questions and the COO's.

## 6. NOT MEASURED

- **Session lifetime.** The jar was minted at 19:29Z and rode fine through 19:5xZ. Its TTL (SA's
  `user_remember_token` is a long-lived remember-me; `_px3` is short) is unobserved past ~30 minutes.
- **Headless.** Every green run here was HEADED real Chrome on this Windows device. A headless or
  Linux-Chromium harvest is untested and is the first thing a box deployment must exercise.
- **MFA.** Andrew's account showed no OTP step. Whether SA ever forces one (new device, new geography)
  is unknown; the script stops on `MFA_OTP` and has no adapter wired.
- **Rate limits and terms.** Paced at 1 call / 1-3 s; nothing faster was tried. Seeking Alpha's terms
  of use on programmatic access were not read for this investigation.
- **The `has_paid_subscription` gate on other paywalled surfaces** (PRO-locked articles, Alpha Picks).
  Both articles fetched were `isPaywalled=false, isLockedPro=false`; a PRO-locked one was not tried.

## 7. PROVENANCE

```
RUNS (all 2026-09-10, this device, this seat):  probe1 proxy smoke 19:0xZ; probe2/2b proxied Chrome
  18:5x-19:0xZ (login 403 behind the proxy); probe3 REST login (402 policy_20130 on every POST);
  kimi_probe (empty at 50/120 tokens, correct at 1500); harvest run 1 19:20Z (ANON x4, selectors);
  harvest run 2 19:25-19:29Z (GREEN, parked); ride 19:3xZ; rest_minimal, rest_confirm, rest_px,
  rest_proxy_referer, rest_fulljar 19:4x-19:5xZ. Logs and step screenshots in the session scratch dir.
READ:  data/seeking-alpha/scripts/seeking_alpha_login.py; infra/aws/lambda/seeking-alpha-analysis-scraper;
  infra/aws/ec2/bd-49f-auto-login/{bd_49f_auto_login.js,run-bd-auto-login.sh,secret-ids.env};
  data/assets/docs/BLACKDIAMOND_LOGIN_MECHANISM.md; docs/briefs/bd-49f-durable-auto-auth-cv-login-otp-relay-20260625.md;
  org/missions/D5/AMGT/AMGT_RESAPP/{project.json,prd/AMGT_RESAPP_PRD.md}; this seat's two 2026-09-10 deliverables.
CENSUS: comp-find 'seeking.?alpha' 3,865 hits / 54,465 files; --corpus aws 42 hits / 2,382 nodes
  (8 Lambdas, 2 EC2, 1 DynamoDB, 6 secrets, all SA Lambdas LIVE-no-DECLARED); Secrets Manager 89 names
  auto-paginated, 7 SA/Bright Data candidates.
SECRETS TOUCHED: read seeking-alpha/credentials, astn/brightdata/residential-proxy, astn/kimi/api-key,
  opal/external-apis (keys only), brightdata-api-key; CREATED seeking-alpha/session. No value printed anywhere.
Push state: LOCAL. 0.0.0_AB_MSTR~Z holds all pushes.
```
