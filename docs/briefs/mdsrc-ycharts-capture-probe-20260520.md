# YALP_MDSRC.A1 -- YCharts Headless-Capture WAF Probe (Result Brief)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` (PRD v0.3) -- Phase 2A / TO-A1 |
| Task Order | `YALP_MDSRC.A1.ae-ycharts-capture-probe` |
| Author | `0.7.0_AE_CloudOps` |
| Date | 2026-05-20 (probe run 2026-05-21T01:0xZ UTC) |
| Type | Empirical probe-result brief. Throwaway probe; no integration build (that is TO-C1). |
| Feeds | WS-4 design doc `docs/briefs/mdsrc-ws4-ycharts-operational-pattern-20260520.md` (Branch A/B + cron); TO-C1 (YCharts credential pipeline) if Q1 resolves to session-scrape. |

---

## 0. Verdict

**AC1 -- Branch A (headless capture) is VIABLE.** Headless Chromium clears the AWS WAF
JS-challenge: on a YCharts app page that loads the awswaf SDK, headless Chromium executed the
challenge and acquired a valid `aws-waf-token` cookie -- no challenge interstitial, no block,
the page rendered normally. Attended capture (Branch B) is **not** required for the WAF step.

**AC2 -- session-cookie TTLs measured.** `aws-waf-token` TTL ~96h (4 days); `ycsessionid` is a
pure session cookie with no client-readable expiry; `csrftoken` ~1 year. The WS-4 daily
pre-emptive capture cron sits comfortably inside the binding measurable TTL.

---

## 1. Method

Throwaway probe, pre-auth (no credentials -- the WAF challenge fires independent of login).

Playwright's own browser transports both **hang under `bun`** on this host -- `chromium.launch()`
(pipe transport) timed out at 180s, and `chromium.connectOverCDP()` got the WebSocket URL then
hung on the `ws connecting` handshake. Root cause: there is no real Node runtime on this host
(`which node` resolves to a `bun`-node shim); Playwright's bundled `ws` client is not completing
the CDP handshake under bun's node-compat. **The probe succeeded via raw Chrome DevTools
Protocol over `bun`'s native `WebSocket`** -- chrome.exe was launched separately with
`--headless=new --remote-debugging-port=9222 --no-sandbox`, and the probe drove it with raw CDP
(`Page.enable` / `Network.enable` / `Runtime.evaluate` / `Network.getAllCookies`).

This transport finding is itself a carry-forward for TO-C1 (Section 4).

Three URLs were probed headless: `https://ycharts.com/account/login/`, `https://ycharts.com/`,
and `https://ycharts.com/dashboard/`.

## 2. AC1 -- does headless clear the AWS WAF challenge?

| Probed URL (headless) | awswaf SDK in DOM | `aws-waf-token` acquired | Challenge interstitial / block | Page rendered |
|---|---|---|---|---|
| `/account/login/` | no | no | no | yes -- real login form (1 password field, "YCharts Admin Login / Enter your credentials") |
| `/` (homepage) | no | no | no | yes -- marketing homepage, full content |
| `/dashboard/` | **yes** | **yes** | **no** | yes -- "Dashboard" page |

**Finding.** The AWS WAF JS-challenge SDK does **not** load on every page -- the login-page GET
and the homepage GET were not WAF-challenge-gated (no awswaf SDK, no token). The awswaf SDK
engages on YCharts **app pages** (`/dashboard/`). On that page, **headless Chromium ran the
challenge JS and acquired a valid `aws-waf-token` cookie** -- with no challenge interstitial, no
"verify you are human" page, no block, and the page rendered normally.

**=> Branch A is viable.** The AWS WAF challenge is solvable by headless Chromium executing the
challenge JS -- it does not fingerprint-block the headless browser at the challenge step. The
WS-4 capture mechanism can be the automated headless-Playwright path (Branch A); the attended
fallback (Branch B) is held in reserve but is not the required path on this evidence.

**Caveat -- scope of this verdict.** This probe proves the **WAF challenge** clears headless.
It does **not** exercise the **login POST** (credential submission) headless -- that step needs
credentials and is a separate question (a login form rendering + accepting input is a normal
form, not a WAF concern). The `ycharts/credentials` secret (YALP_MDSRC.006) currently holds a
cookie bundle, not a username/password, so a fresh headless login was out of scope here. The
WAF-clear result -- the de-risking purpose of A1 -- stands on its own: the capture sequence
"headless browser loads a YCharts app page -> awswaf SDK runs -> `aws-waf-token` acquired" is
empirically confirmed to work headless.

## 3. AC2 -- session-cookie TTLs + cron-cadence implication

Measured from the live probe (`Network.getAllCookies`) and the captured login-flow HAR
(`ycharts.com3.har`, Set-Cookie response headers; cookie values redacted, attributes only):

| Cookie | TTL signal | Value |
|---|---|---|
| `aws-waf-token` | CDP cookie `expires` | epoch 1779671348 = **2026-05-25T01:09:08Z**; acquired ~2026-05-21T01:09Z -> **TTL ~96h (4 days)** |
| `ycsessionid` | HAR `Set-Cookie` + CDP `expires` | **NO `Max-Age`, NO `expires`** -- a pure session cookie (`expires: -1`). Client-side lifetime is unbounded; the server-side Django `SESSION_COOKIE_AGE` governs and is not client-visible. |
| `csrftoken` | HAR `Set-Cookie` | `Max-Age=31449600` (~1 year) |
| `page_view_ctr` | HAR `Set-Cookie` | `Max-Age=2592000` (30 days) -- not auth-bearing |
| `multidb_pin_writes` | HAR `Set-Cookie` | `Max-Age=2` (2s DB-replication pin) -- not auth-bearing |

**Cron-cadence implication for WS-4 (Section 4.6 of the WS-4 design doc).**
- The binding **measurable** credential TTL is `aws-waf-token` at ~96h. A daily (24h)
  pre-emptive re-capture is comfortably inside that -- the WS-4 daily-cron default holds, with
  ~4x headroom on the WAF token.
- `ycsessionid` carries **no client-readable expiry at all** -- this empirically confirms and
  hardens the WS-4 Q2 conclusion: the freshness gate cannot be a stored-timestamp/TTL check
  (there is no TTL to read), it must be the **active authenticated probe**. The cron is the
  pre-emptive layer; the probe is the correctness layer. The session's true death is governed
  by the server-side `SESSION_COOKIE_AGE` (unmeasurable from the client) plus the
  single-concurrent-session eviction (WS-1 Finding 2) -- both event-driven, both caught only by
  the active probe.
- **No cadence change to WS-4 is required.** Daily pre-emptive capture + active multi-endpoint
  probe (WS-4 Sections 4.3/4.6) is correct as written; this probe supplies the empirical TTL
  numbers behind it.

## 4. Carry-forward for TO-C1 (YCharts credential pipeline)

1. **Branch A confirmed** -- scope the C1 capture mechanism as automated headless Playwright /
   Chromium; the attended Branch B is the documented fallback, not the primary path.
2. **Runtime gap** -- Playwright's `launch()` and `connectOverCDP()` both hang under `bun` on
   this host (no real Node). The production capture Lambda/EC2 must run Playwright on a **real
   Node runtime** (Lambda Node image, or Node on the capture EC2), OR use the raw-CDP-over-
   native-WebSocket approach this probe used. Do not assume `bun` + Playwright works.
3. **WAF SDK engages on app pages, not the login page** -- the capture script must navigate to
   a YCharts app page (e.g. `/dashboard/`) to trigger the awswaf SDK and acquire the
   `aws-waf-token`, then proceed to login. Loading only `/account/login/` does not yield a
   WAF token.
4. **`ycharts/credentials` holds a cookie bundle, not username/password** (YALP_MDSRC.006,
   Andrew's format pick). A fresh-login capture mechanism needs login credentials; C1 planning
   must reconcile the secret's contents with the capture mechanism's needs.
5. **aws-waf-token ~96h TTL** -- a daily capture cron has ~4x headroom on the WAF token.

## 5. Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| 1 (before) | (none) | Documented-none per the TO mandate + PRD Section 10 honest-scope note -- YCharts is an external system, not in the comp-graph; the probe is throwaway test code, not a pipeline script. Evidence base is the live headless probe + the captured HAR. |
| 2 (before commit) | (none) | Probe-result brief; no production code committed (the probe scripts are throwaway, `.runtmp/`, not committed). |
| 3 (after commit) | (none) | The Branch-A/B verdict + the measured TTLs ARE the deliverable's self-validation (AC1/AC2). |

## 6. Acceptance-criteria self-check

| AC | Where satisfied |
|---|---|
| AC1 -- headless WAF-challenge verdict (Branch A vs B) with evidence | Section 2 -- Branch A viable; headless Chromium acquired a valid `aws-waf-token` on `/dashboard/`, no challenge/block. |
| AC2 -- `ycsessionid` (+ other) Set-Cookie TTL measured; cron cadence stated | Section 3 -- `ycsessionid` = pure session cookie (no client TTL); `aws-waf-token` ~96h; daily WS-4 cron holds with headroom. |
| AC3 -- committed probe brief + session log w/ Compiler Tools section + RAVC2 | This brief (committed); Section 5; session log + RAVC2 on completion. |

---

*A1 probe deliverable. Branch A (headless capture) empirically de-risked. No integration built
(that is TO-C1). Throwaway probe scripts not committed.*
