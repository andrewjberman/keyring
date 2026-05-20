# YALP_MDSRC WS-4 -- YCharts Integration Operational-Pattern Design

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` (PRD v0.2) -- WS-4 / TO-4 |
| Task Order | `YALP_MDSRC.004.ae-ws4-ycharts-operational-pattern-declaration` |
| Author | `0.7.0_AE_CloudOps` |
| Date | 2026-05-20 |
| Type | DESIGN DOC -- declares an operational pattern. v0.2 authorizes NO code/Terraform/Lambda. |
| Status | Phase 0 audit deliverable. Implementation = a v0.3 TO. |
| Baselines read | `ADVI_JWTRES` (Orion JWT pattern), `ADVI_ECLDAT` (Eclipse dual-track variant) -- shipped Lambda source, read-only |
| Shared inputs consumed | WS-1 (`0.1.0_DS_MarketIntelligence`) empirical Q3 auth/WAF finding (MCP 2026-05-20 21:1xZ); recon doc-of-record `docs/briefs/ycharts-bloomberg-portal-data-sourcing-audit-20260520.md`; WS-2 brief Section 6 |

---

## 0. Executive summary

Andrew's framing -- "manual jwt refresh and lib/secrets storage like how we do it for Orion,
but for YCharts" -- is correct on the **operational pattern** and wrong on the **credential**.
The Orion pattern (capture -> Secrets Manager -> freshness gate -> refresh Lambda -> CloudWatch
alarms -> daily cron) transfers cleanly. The credential does not: YCharts has **no JWT**. It is
a Django session-cookie web app behind an AWS WAF (PRD Section 3.1). So `jwt_freshness.py`'s
decode-the-`exp`-claim mechanism does **not** port -- there is no `exp` to decode -- and the
freshness gate must be redesigned around a different signal.

This doc declares the YCharts-adapted pattern for all six pattern elements (capture, Secrets
Manager shape, freshness gate, refresh, CloudWatch, cron), grounded in the WS-1 empirical probe.

**Three load-bearing facts shape the design:**

1. **WAF gates capture, not pulls** (WS-1 Finding 1). The AWS WAF challenge must be solved by a
   real browser at credential-*capture* time; once the `aws-waf-token` is captured, plain
   headless GETs pass HTTP 200. This is structurally identical to Orion: browser-capture the
   credential once, then headless requests carry it. The capture step is the only browser-bound
   step.
2. **YCharts enforces a single concurrent session per credential** (WS-1 Finding 2). A
   programmatic pull on a captured session cookie is mutually evicted with any human signed in
   on the same seat (verbatim 403: "You have been signed out due to a concurrent sign in using
   your credentials"). This has **no analogue in the Orion JWT pattern** and is the single
   biggest YCharts-specific divergence. The design mandates a **dedicated YCharts seat** for the
   integration and a dedicated `SessionEvicted` alarm.
3. **No `exp` claim -> freshness must be probed, not decoded** (PRD Q2). Combined with fact 2 --
   the session can die at *any* moment via human collision, not at a predictable expiry -- a
   passive time-to-live is structurally insufficient. The freshness gate is an **active
   lightweight authenticated probe**.

**Primary recommendation:** if the official YCharts Data API (key-auth) is in reach, take it --
it eliminates capture, WAF, the freshness probe, and the single-session constraint outright
(Section 7). That is Andrew's call (Q1). This doc designs the **session-scrape operational
pattern** in full because it is the path that works with what is empirically in hand today; the
official-API delta is documented so v0.3 can choose with both fully specified.

---

## 1. Baseline -- the Orion JWT operational pattern (AC1)

Hardened by `ADVI_JWTRES`. Source read for this doc:
`infra/aws/lambda/inf-pipeline/inf-jwt-trigger/lambda_function.py`,
`infra/aws/lambda/inf-pipeline/*/jwt_freshness.py` (shared lib, copied per consumer),
`infra/aws/terraform/inf-pipeline/{eventbridge,alarms,secrets}.tf`.

| Pattern element | Orion implementation |
|---|---|
| **Credential** | A single ~10h Orion session JWT (`Authorization: Session {jwt}`, not `Bearer`). No long-lived API key exists. |
| **Capture** | Playwright browser automation on the `inf-exporter` EC2. The `inf-jwt-trigger` Lambda starts the EC2, waits for `running`, dispatches SSM document `opal-inf-jwt-fetch` (`_send_ssm_with_retry`, 5x retry to absorb the SSM-agent registration window). Login is OTP-gated -- a human (Andrew) supplies the OTP via the inf-otp-relay; on timeout the SSM doc writes `FAILED_OTP_TIMEOUT`. So Orion capture is itself **semi-attended**. |
| **Storage** | AWS Secrets Manager `orion/jwt/current` (raw JWT string, primary) + S3 `s3://opal-data-inf/orion/jwt/current.json` (JSON wrapper with `jwt` + `issued_at_iso`, fallback). Two-path load: SM first, S3 second; both unreadable -> `JwtUnreadableError`, treated as stale (fail-fast). |
| **Freshness gate** | `jwt_freshness.py` shared lib. `check_jwt_freshness()` base64url-decodes the JWT payload, reads the `exp` claim, computes `seconds_remaining`, compares against a 30-min headroom (`DEFAULT_MIN_REMAINING_SECONDS=1800`; env override `JWT_MIN_REMAINING_SECONDS`). Returns a `JwtFreshnessReport` (`is_fresh`, `seconds_remaining`, `expires_at`, `source`, `raises_on_stale`, `jwt`). `assert_fresh_or_exit()` -- fail-fast wrapper, prints `FATAL [kind]` and `sys.exit(2)` (`EXIT_CODE_STALE_JWT`) on stale. The exp claim is read **unsigned** (signature is Orion's concern). |
| **Refresh / auto-recovery** | `recover_or_exit()` (`ADVI_JWTRES.002`): on stale, async-invokes `inf-jwt-trigger` (`InvocationType='Event'`), then polls S3 `issued_at_iso` every 30s up to a 15-min ceiling for advancement; on advance, reloads + re-checks; on invoke-fail or timeout, `sys.exit(2)`. Latency budget ~13 min (EC2 boot-to-JWT). |
| **Observability** | CloudWatch namespace `Inflection/JwtResilience` -- counter metrics `JwtNearExpiry`, `JwtExpired`, `JwtUnreadable` (dimension `script_name`). Recovery metrics (`JwtAutoRecoveryAttempted/Succeeded/Failed`) land in `Inflection/HistBackfill/RateLimiter`. CW emission is best-effort (failures logged + swallowed -- never double-fail the pull). Alarms in `inf-pipeline/alarms.tf`: `orion-otp-timeout-alert` (OTP timeout), `Inflection-JwtResilience-NearExpirySpike` (`JwtNearExpiry` Sum > 1 / 5 min) -- both -> `inf-otp-alert` SNS. |
| **Cadence** | EventBridge `opal-inf-jwt-fetch`, `cron(13 12 * * ? *)` = 12:13 UTC / 08:13 ET daily -- pre-emptive renewal 30 min before the 12:43 UTC bronze runner. JWT TTL ~10h, so a fresh daily capture comfortably covers the pull window. |

### 1.1 The Eclipse dual-track variant (`ADVI_ECLDAT`)

Eclipse does not have an independent login -- its credential is **derived from** the Orion JWT.
In the same `inf-jwt-trigger` `jwt-extract` run: after the Orion JWT advances in SM, the Lambda
GETs the Eclipse admin Token endpoint (`https://www.orioneclipse.com/v1/admin/Token`) with the
Orion JWT as the `Authorization: Session {orion_jwt}` bearer, receives `eclipse_access_token`,
and writes it to SM `orion/eclipse_jwt/current` as JSON (`jwt`, `eclipse_user_id`,
`orion_user_id`, `expires_at`, `captured_at`). Both tracks are still **JWTs with `exp`** -- the
Eclipse one is HS256 (float `exp`), Orion HS512 (int `exp`); `_decode_jwt_exp_safe` handles both
via `int(float(...))`. "Dual-track" = two JWTs, one a child of the other, both decode-exp.

**Relevance to YCharts:** the dual-track variant shows the pattern already accommodates a
second credential captured in the same run. It does **not** give YCharts a freshness mechanism
-- both Eclipse and Orion still decode an `exp`. YCharts has neither.

---

## 2. The YCharts credential difference -- why `jwt_freshness.py` does not port (AC3)

PRD Section 3.1, corroborated by the WS-1 empirical probe. YCharts authenticated data calls
(`/charts/fund_data.json`, `/indices/table_data`, `/model_portfolios/*`, ...) carry **zero
`Authorization` headers**. Authentication is a **cookie bundle**:

| Component | Role | YCharts | Orion |
|---|---|---|---|
| `ycsessionid` | Django server-side session id -- the actual credential | cookie | -- |
| `csrftoken` | Django CSRF double-submit token | cookie + `x-csrftoken` request header | -- |
| `aws-waf-token` | AWS WAF challenge token (host `fdb400f6cad7.edge.sdk.awswaf.com`) | cookie | -- |
| `x-requested-with` | XHR marker on data calls | request header | -- |
| (the credential as a whole) | -- | ~16-cookie bundle + 2 headers | one ~10h JWT string |

**Why `jwt_freshness.py`'s mechanism does not port -- three structural reasons:**

1. **No `exp` claim.** `_decode_jwt_exp()` base64url-decodes a JWT payload and reads `exp`. A
   Django `ycsessionid` is an **opaque server-side session key** -- it carries no client-readable
   payload, no expiry, nothing to decode. `seconds_remaining` is uncomputable from the
   credential itself. The entire `check_jwt_freshness()` decode-and-compare core is inapplicable.
2. **Multi-field credential.** `jwt_freshness.py` loads and returns a single string (`report.jwt`).
   The YCharts credential is a structured bundle (session cookie + CSRF cookie + WAF token + the
   other ~13 cookies + 2 headers) that must travel together. The storage shape, the load path,
   and the report object all change from "a string" to "a bundle".
3. **Failure is event-driven, not time-driven.** A JWT fails predictably at `exp`. A YCharts
   session fails at `exp` **or** the moment a human signs in on the same seat (WS-1 Finding 2)
   **or** on server-side session rotation. Two of those three are unpredictable. A
   decode-the-expiry check -- even if an expiry existed -- could not catch a mid-window
   eviction. The freshness signal must be **active** (probe the live session), not **passive**
   (read a stored timestamp).

What ports unchanged: the **shape** of the lib -- a `*_freshness.py` module with a
`check_*()` returning a report dataclass, an `assert_fresh_or_exit()` fail-fast wrapper, a
`recover_or_exit()` auto-recovery wrapper, two-path load (SM primary / S3 fallback),
best-effort CW emission, distinguishable stale exit code. WS-4 keeps that skeleton and replaces
only the freshness *mechanism*.

---

## 3. Shared empirical auth/WAF finding (Q3) -- consumed from WS-1

WS-1 (`0.1.0_DS_MarketIntelligence`) reached the YCharts auth layer first and shared the
empirical Q3 result (PRD Section 4 -- recorded once, not triplicated). Method: replayed the
captured HAR cookie bundle (`ycsessionid` + `csrftoken` + `aws-waf-token`, 16 cookies) from
headless `curl`, ~5.5h after HAR capture. Verbatim findings:

- **Finding 1 -- WAF does not block headless replayed-token requests.** `curl` (no browser, no
  JS) with the captured `aws-waf-token` returned HTTP 200 + full JSON on `/indices/table_data`
  and `/indices/asset_class/root/index_list`. The WAF gates the **initial token acquisition**
  (the challenge needs a real browser to solve); once `aws-waf-token` is captured, plain
  headless GETs pass. The WAF is **not** a per-request bot block.
- **Finding 2 -- single concurrent session per credential (CRITICAL).** Mid-probe the session
  was invalidated: HTTP 403, body "You have been signed out due to a concurrent sign in using
  your credentials." A concurrent human sign-in (or YCharts session rotation) kills the session;
  every subsequent call 403s.
- **Finding 3 -- entitlement/tier gating.** `/classifications/sectors.json` returned 403 "You
  don't have access to this feature." YCharts features are subscription-tier gated.

**Q3 verdict for WS-4:** the AWS WAF does **not** defeat headless *pulls*, so the steady-state
pull path is plain headless HTTP (good -- mirrors Orion). The residual WAF question is narrowed
to the **capture** step only: can a headless browser solve the WAF JS challenge during login,
or is an attended capture required? That residual is addressed with both branches in Section
4.1 (AC4). Finding 2 is the dominant design constraint and is threaded through Sections 4.1,
4.3, 4.5.

---

## 4. The YCharts-adapted operational pattern (AC2)

Naming convention mirrors Orion (`inf-jwt-trigger`, `Inflection/JwtResilience`,
`orion/jwt/current`). Proposed YCharts equivalents are prefixed `ycharts-` / `YCharts/` /
`ycharts/`. All resource names below are **design proposals** -- v0.3 finalizes.

### 4.1 Credential-capture mechanism (WAF-challenge-solving)

The capture must (a) log in to YCharts with the dedicated-seat credentials, (b) solve the AWS
WAF JS challenge, (c) harvest the full post-login, post-WAF-clear cookie bundle + the CSRF
header value. WS-1 Finding 1 confirms only this step is browser-bound.

**Tool: Playwright** -- the same tool Orion uses, for the same reason: the WAF challenge is a
JavaScript proof-of-work / device-fingerprint check that only a real browser engine executes.
`curl` cannot solve it; Playwright (Chromium) runs the real JS and can.

**Host: a capture EC2** mirroring `inf-exporter` -- a small instance, stopped between runs,
started by the refresh Lambda, Playwright driven via an SSM document. (Alternative: Playwright
in a Lambda container image. EC2 is recommended for parity with the proven Orion path and
because headed-browser + display dependencies are simpler to host on EC2.)

Per AC4, **both capture branches are designed** -- the residual Q3 question (can headless
Chromium solve the WAF login challenge) is empirically open until a capture probe runs:

- **Branch A -- automated headless capture (target steady state).** Playwright headless
  Chromium with a stealth profile (realistic user-agent, viewport, navigator fingerprint;
  `playwright-stealth`-class hardening) runs on the capture EC2, drives the login form, lets the
  WAF challenge JS execute and settle, and harvests cookies. Fully unattended, daily. This is
  the goal; WS-1 Finding 1 makes it plausible (the WAF is challenge-once, not block-always), but
  whether *headless* Chromium clears the *login* challenge is the open residual.
- **Branch B -- attended / assisted capture (fallback).** If the WAF fingerprints and blocks
  headless Chromium at login, fall back to an attended capture: a human runs a real headed
  browser session (or a headed Playwright on the EC2 via a remote display) periodically -- weekly
  or on-eviction -- and the cookie bundle is exported to Secrets Manager. This is **not
  unprecedented**: Orion's own capture is semi-attended (Andrew supplies the OTP). An
  OTP-relay-style assist (a one-tap human confirm, reusing the inf-otp-relay pattern) is the
  middle ground.

**Recommendation:** implement Branch A; ship Branch B as the documented fallback runbook. v0.3's
first implementation step is a **capture probe** -- run Playwright headless against the YCharts
login once and observe whether the WAF challenge clears. That probe result picks A vs B. Until
then, neither is foreclosed.

A capture run, on success, produces the bundle written per Section 4.2; on failure (WAF block,
bad credentials, login-form change) it emits `CaptureFailed` (Section 4.5) and does **not**
overwrite the existing bundle (last-good is retained, exactly as Orion never overwrites a good
JWT with a failed fetch).

### 4.2 Secrets Manager storage shape -- the cookie bundle

Orion stores a raw JWT string in SM and a thin JSON wrapper in S3. YCharts' credential is
inherently structured, so it is **JSON in both** stores.

Primary: Secrets Manager `ycharts/session/current`
```json
{
  "ycsessionid":    "<opaque django session id>",
  "csrftoken":      "<django csrf token>",
  "aws_waf_token":  "<aws waf challenge token>",
  "cookie_bundle":  { "<name>": "<value>", "...": "all ~16 cookies as captured" },
  "headers":        { "x-csrftoken": "<token>", "x-requested-with": "XMLHttpRequest" },
  "captured_at":    "2026-05-20T21:00:00Z",
  "soft_expires_at":"2026-05-21T21:00:00Z",
  "seat_id":        "ycharts-integration-seat",
  "capture_method": "headless | attended"
}
```
Fallback: S3 `s3://opal-data-inf/ycharts/session/current.json` -- the **same JSON object**.
(`opal-data-inf` reused as the host bucket for parity with `orion/jwt/current.json`; v0.3 may
elect a YCharts-scoped prefix or bucket.)

Contrast with Orion: Orion = one string in SM + a 2-field wrapper in S3. YCharts = one
structured object, identical in SM and S3. The consumer no longer prepends an `Authorization`
header -- it attaches `cookie_bundle` as the request `Cookie` jar plus the two `headers`
entries.

A second secret, `ycharts/login/credentials` (`{username, password, seat_id}`), holds the
**dedicated-seat** login used only by the capture step. Never logged; never leaves the capture
EC2.

`soft_expires_at` is a *capture-time + observed-Django-SESSION_COOKIE_AGE* estimate -- it drives
the **pre-emptive** daily refresh (Section 4.6), but it is explicitly **not** the freshness gate
(Section 4.3 explains why a stored timestamp cannot be the gate).

### 4.3 The freshness gate (Q2) -- an active authenticated probe

There is no `exp` to decode (Section 2) and the session can die mid-window via human collision
(Section 3, Finding 2). Therefore the freshness gate is an **active lightweight authenticated
probe**, not a stored-timestamp read. This is the cookie-world analogue of Orion's
`assert_fresh_or_exit` -- same contract, different signal.

Proposed shared lib `cookie_freshness.py` (mirrors `jwt_freshness.py`'s skeleton):

- `check_session_freshness()` -- loads the bundle (SM primary, S3 fallback; both fail ->
  `SessionUnreadableError`), then issues **one cheap authenticated GET** to a stable, low-cost
  YCharts endpoint (candidate: `/indices/asset_class/root/index_list`, ~41 KB, or a cheaper
  reference endpoint WS-1 identifies) carrying the cookie bundle + CSRF/XHR headers. It
  classifies the response:

  | Response | Classification | Returned state |
  |---|---|---|
  | HTTP 200 + well-formed JSON | FRESH | `is_fresh=True` |
  | HTTP 403, body matches "concurrent sign in" | STALE -- **EVICTED** (Finding 2) | `is_fresh=False`, `reason=evicted` |
  | HTTP 401/403 login-redirect, or session-invalid body | STALE -- EXPIRED | `is_fresh=False`, `reason=expired` |
  | HTTP 403, body matches "don't have access" | ENTITLEMENT (not a freshness fault) | `is_fresh=False`, `reason=entitlement` |
  | SM + S3 both unreadable / transport error | UNREADABLE | `is_fresh=False`, `reason=unreadable` |

  Returns a `SessionFreshnessReport` (`is_fresh`, `reason`, `source`, `probe_status`,
  `raises_on_stale`, `bundle`).

- `assert_fresh_or_exit()` -- fail-fast wrapper; on stale prints `FATAL [reason]` and
  `sys.exit(2)` (`EXIT_CODE_STALE_SESSION`, reusing the distinguishable-exit-code convention).

- `recover_or_exit()` -- auto-recovery; see Section 4.4.

**Why a probe and not a TTL.** Finding 2 makes the credential's death **event-driven**: a TTL
(even a real one) is blind to a 10:00-AM human sign-in that evicts the integration. Only an
active probe -- which tests the exact thing the pull needs, "can this bundle still fetch data"
-- is correct. The `soft_expires_at` TTL is retained but demoted to a *pre-emptive refresh
scheduler input only*, never the gate. This is a deliberate divergence from Orion, forced by
the credential's failure model, and is the central Q2 answer.

**Probe cost.** One ~41 KB GET per pull-start (and optionally once per long pull's mid-point) --
negligible. The probe doubles as the eviction detector that feeds the `SessionEvicted` metric.

### 4.4 Refresh mechanism

`ycharts-session-trigger` Lambda -- the `inf-jwt-trigger` analogue:

- **Scheduled mode** (daily cron, Section 4.6): start the capture EC2, wait for `running`,
  dispatch SSM document `opal-ycharts-session-capture` (with `_send_ssm_with_retry`-style agent-
  registration retry), which runs the Section 4.1 Playwright capture and writes the Section 4.2
  bundle. Stop the EC2 on completion.
- **On-demand / auto-recovery mode:** invoked async by a pull script when
  `check_session_freshness()` returns stale.

Auto-recovery in `cookie_freshness.recover_or_exit()` mirrors `jwt_freshness.recover_or_exit()`
exactly, swapping the advancement sentinel: snapshot SM/S3 `captured_at`, async-invoke
`ycharts-session-trigger` (`InvocationType='Event'`), poll `captured_at` every 30s up to a
15-min ceiling for advancement, reload + re-probe on advance, `sys.exit(2)` on invoke-fail or
timeout. `captured_at` replaces Orion's `issued_at_iso` as the "refresh landed" sentinel.

**Eviction-specific behavior.** When the stale `reason` is `evicted` (Finding 2), recovery
re-captures as normal -- but a re-capture only helps if the colliding human has since left the
seat; if the integration and a human are both active, they will keep evicting each other. The
durable fix is the **dedicated seat** (Section 4.7), not recovery. Recovery handles the
transient collision; the seat handles the structural one.

### 4.5 CloudWatch observability

New namespace `YCharts/SessionResilience` (mirrors `Inflection/JwtResilience`). Best-effort
emission -- failures logged and swallowed, never double-fail the pull (Orion convention).

| Metric | Emitted when | Dimension |
|---|---|---|
| `SessionProbeOk` | freshness probe returns FRESH | `script_name` |
| `SessionExpired` | probe -> EXPIRED | `script_name` |
| `SessionEvicted` | probe -> EVICTED (the Finding-2 concurrent-sign-in 403) | `script_name` |
| `SessionUnreadable` | SM + S3 both unreadable | `script_name` |
| `SessionEntitlementDenied` | probe -> "don't have access" 403 (Finding 3) | `script_name` |
| `CaptureFailed` | a `ycharts-session-trigger` capture run fails (WAF block / bad creds / form change) | `capture_method` |
| `SessionAutoRecoveryAttempted/Succeeded/Failed` | `recover_or_exit` lifecycle | `script_name` |

Proposed alarms (Terraform, v0.3; `inf-pipeline/alarms.tf` or a new `ycharts` module) -- all ->
**`opal-infrastructure-alerts`** SNS (the shared ops topic; **not** `inf-otp-alert`, which is
Orion-OTP-scoped):

| Alarm | Signal | Why distinct |
|---|---|---|
| `ycharts-session-evicted` | `SessionEvicted` Sum >= 1 / period | The Finding-2 failure class. A distinct, named alarm tells Andrew a **human seat collision** happened -- actionable as "stop using that seat" or "the integration needs its own seat". This is the YCharts-specific alarm with no Orion equivalent. |
| `ycharts-session-stale` | `SessionExpired` + `SessionUnreadable` | Generic stale -- recovery should self-heal; a sustained breach means recovery is failing. |
| `ycharts-capture-failed` | `CaptureFailed` Sum >= 1 | The capture step broke (WAF started blocking headless, login form changed, creds rotated). Mirrors `orion-otp-timeout-alert`. |

### 4.6 Daily cron cadence

EventBridge rule `opal-ycharts-session-capture`, daily, pre-emptive, scheduled **before** the
YCharts daily pull -- the exact Orion shape (`opal-inf-jwt-fetch` at 12:13 UTC, 30 min before
the 12:43 UTC bronze runner).

Cadence inputs: the YCharts Django session lifetime is not yet measured (no `exp` to read; the
WS-1 probe survived ~5.5h before a *collision*, not an expiry). v0.3's capture probe should also
record the observed `Set-Cookie` `Max-Age`/`Expires` on `ycsessionid` to size `soft_expires_at`.
**Design default: daily pre-emptive re-capture** -- a fresh bundle each morning, ~30-60 min
before the pull, regardless of measured TTL. Daily is safe (a daily capture cannot under-cover a
multi-hour session) and matches Orion. If v0.3 finds the session lives well beyond 24h, the cron
can stretch; if it finds it shorter, the **active probe (4.3) plus auto-recovery (4.4) already
covers** an intra-day death -- the cron is the pre-emptive layer, the probe is the safety net.

### 4.7 The single-concurrent-session constraint -- dedicated seat (Finding 2)

This is the design's load-bearing non-technical requirement. Because YCharts evicts on
concurrent sign-in, the integration **must run on a YCharts seat that no human uses**:

- **Provision a dedicated YCharts seat / login** for the integration (`seat_id` in the
  Section 4.2 secret). This is a **licensing / procurement ask -- an Andrew business call**, and
  it gates any session-scrape implementation. Without it, every integration pull risks evicting
  an analyst and vice versa.
- The `ycharts-session-evicted` alarm (4.5) is the detection if a collision happens anyway
  (e.g. the dedicated seat is accidentally shared).
- This constraint **does not exist for Orion** (a JWT is not a single-session credential) and
  is the sharpest YCharts-vs-Orion divergence. It is also the strongest operational argument for
  the official API (Section 7) -- an API key has no session and no eviction.

---

## 5. Side-by-side -- Orion JWT vs YCharts session pattern

| Element | Orion (baseline) | YCharts (this design) |
|---|---|---|
| Credential | one ~10h session JWT | ~16-cookie bundle + 2 headers |
| Auth header | `Authorization: Session {jwt}` | `Cookie:` jar + `x-csrftoken` + `x-requested-with`; no `Authorization` |
| Capture | Playwright on `inf-exporter` EC2, OTP-gated (semi-attended) | Playwright on a capture EC2, WAF-challenge-solving; Branch A headless / Branch B attended |
| SM secret | `orion/jwt/current` (raw string) | `ycharts/session/current` (JSON bundle) + `ycharts/login/credentials` |
| S3 fallback | `orion/jwt/current.json` (2-field wrapper) | `ycharts/session/current.json` (same JSON object) |
| Freshness signal | **passive** -- decode `exp`, 30-min headroom | **active** -- authenticated probe, 200-vs-403 classification |
| Freshness lib | `jwt_freshness.py` | `cookie_freshness.py` (same skeleton, probe core) |
| Stale exit code | 2 (`EXIT_CODE_STALE_JWT`) | 2 (`EXIT_CODE_STALE_SESSION`) |
| Refresh Lambda | `inf-jwt-trigger` | `ycharts-session-trigger` |
| Recovery sentinel | S3 `issued_at_iso` advances | SM/S3 `captured_at` advances |
| CW namespace | `Inflection/JwtResilience` | `YCharts/SessionResilience` |
| Distinct failure class | OTP timeout | **session eviction** (concurrent sign-in) -- no Orion analogue |
| Alarm target SNS | `inf-otp-alert` | `opal-infrastructure-alerts` |
| Cron | `cron(13 12 * * ? *)` pre-emptive daily | daily pre-emptive, pre-pull |
| Single-session constraint | none | **yes -- dedicated seat required** |

---

## 6. Open items carried to v0.3

| # | Item | Owner |
|---|---|---|
| 1 | **Capture probe** -- run Playwright headless against the YCharts login once; does the WAF challenge clear headless? Picks Branch A vs B (Section 4.1). | v0.3 impl TO |
| 2 | **Dedicated YCharts seat** -- procure/license a seat reserved for the integration (Section 4.7). | Andrew business call (gates session-scrape impl) |
| 3 | **Q1 -- official YCharts Data API** -- if procured, Section 7 supersedes Sections 4.1-4.7. | Andrew business call |
| 4 | **Q7 -- ToS** -- is programmatic extraction from a YCharts seat contractually permitted? | Andrew business call |
| 5 | Measure the Django `ycsessionid` lifetime (`Set-Cookie Max-Age`) to size `soft_expires_at` + the cron (Section 4.6). | v0.3 capture probe |
| 6 | Pick the cheapest stable authenticated probe endpoint for `check_session_freshness()` (Section 4.3) -- coordinate with WS-1's endpoint inventory. | v0.3 impl TO |

**comp-iam carry-forward (PRD TO-4 mandate).** When this design is implemented in v0.3, the
implementing TO MUST carry `comp-iam service <lambda>` (Phase 1) for the new
`ycharts-session-trigger` Lambda's boto3 surface (`secretsmanager:GetSecretValue` +
`PutSecretValue` on `ycharts/*`, `ec2:StartInstances`/`StopInstances`/`DescribeInstances` on the
capture EC2, `ssm:SendCommand`, `cloudwatch:PutMetricData` namespace-scoped to
`YCharts/SessionResilience`, `s3:GetObject`/`PutObject` on the `ycharts/session/current.json`
fallback) and `comp-iam gaps` (Phase 2) after the `iam.tf` change. The capture EC2 role needs
the symmetric SM read/write + CW + S3 grants. All namespace/prefix-scoped per least-privilege --
mirror the `inf-pipeline` Orion role policies.

---

## 7. The official-API branch (Q1) -- what changes

If Andrew procures the official YCharts Data API (key-authenticated, documented, ToS-permitted),
the operational pattern **collapses dramatically**:

| Element | Session-scrape (Sections 4.x) | Official API |
|---|---|---|
| Credential | 16-cookie bundle | one long-lived API key |
| Capture | Playwright + WAF-challenge solve, EC2, daily | none -- a static key in SM `ycharts/api/key` |
| Freshness gate | active authenticated probe | none -- keys do not expire on a session timer |
| Refresh Lambda | `ycharts-session-trigger` daily | none (only a periodic key rotation, if YCharts rotates) |
| WAF | must be solved at capture | not in the API path |
| Single-session eviction | dedicated seat required | **no session concept -- eviction cannot happen** |
| Observability | `YCharts/SessionResilience` (5 metrics + 3 alarms) | a simple `ApiCallFailed` / `ApiKeyRejected` metric + 1 alarm |
| Fragility | high (WAF, eviction, login-form drift, ToS risk) | low |

The official API removes capture, WAF, the freshness probe, the eviction class, and the
dedicated-seat procurement -- it is by a wide margin the lower-operational-cost path, and it
neutralizes the single worst constraint (Finding 2). **WS-4's recommendation: if the official
API is within reach, take it.** WS-1's recon brief independently reaches the same conclusion
("if Opal's subscription tier includes API access, the entire integration collapses to a clean
key-auth daily pull"). This doc nonetheless specifies the session-scrape pattern in full because
(a) it is the path that works with what is empirically in hand, and (b) v0.3 must be able to
choose with both options completely designed. The choice is Andrew's (Q1) and the CTO's at v0.3
synthesis (WS-5).

---

## 8. Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| 1 (before) | none | Per the TO `<compiler_tools_mandate>` -- WS-4 is a read-only review of shipped Orion/Eclipse Lambda source + a design declaration. No code is authored, so no comp-* tool applies. The YCharts side is an external system with no comp-graph representation. `comp-iam service` is explicitly deferred to the v0.3 implementation TO. |
| 2 (before commit) | none | Design doc, no code -- no `py_compile` / `ruff` / `ds-precommit` gate applies. |
| 3 (after commit) | none | Design completeness is checked by the TO acceptance criteria (AC1-AC5), not a compiler tool. |

**v0.3 carry-forward:** the implementing TO carries `comp-iam service` (Phase 1) + `comp-iam
gaps` (Phase 2) for the new Secrets Manager / Lambda / EC2-role boto3 surface enumerated in
Section 6.

---

## 9. Acceptance-criteria self-check

| AC | Where satisfied |
|---|---|
| AC1 -- Orion + Eclipse JWT patterns documented as the baseline (capture, SM, freshness, refresh, CW, cron) | Section 1 + 1.1 |
| AC2 -- YCharts-adapted pattern declared for ALL of: capture, SM shape, freshness gate (Q2), refresh, CW, cron | Section 4.1-4.6 |
| AC3 -- the JWT-vs-cookie credential difference explicitly addressed | Section 2 (three structural reasons `jwt_freshness.py` does not port) |
| AC4 -- both capture branches designed (headless vs attended) OR cites the shared finding | Section 3 cites the WS-1 Q3 finding; Section 4.1 designs **both** Branch A (headless) and Branch B (attended) -- both, per AC4 |
| AC5 -- committed design doc + session log w/ Compiler Tools section + RAVC2 to COO + CC CTO | This doc (committed); Section 8; session log + RAVC2 on completion |

---

*WS-4 deliverable. Operational pattern declared; no code or Terraform authored (PRD v0.2
design-only). Implementation = a v0.3 TO gated on the WS-5 synthesis and the Andrew Q1/Q7
calls.*
