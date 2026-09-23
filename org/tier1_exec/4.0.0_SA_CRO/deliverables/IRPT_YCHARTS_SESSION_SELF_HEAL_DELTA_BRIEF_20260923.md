# IRPT YCharts session: credential store, stale-cookie EC2 re-run, self-healing retry -- what exists and the delta

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-23 ~18:5xZ.

**For:** `1.0.0_SA_CTO` (Codex, IRPT governor).

**Scope:** read-only assessment. Nothing was deployed, started, stopped or changed. The one exception is the runner
host start recorded in `ANDREW_DIRECT_20260923_YCHARTS_TICKER_LOOKUP_TEST_PER_USE_AUTHORIZATION.md`.

**Companion:** `IRPT_ANALYSIS_UPLOAD_AND_TICKER_RESOLUTION_BRIEF_20260923.md`, section 5.4, which depends on this.

**This brief deliberately does NOT restate the design.** The design exists: `docs/briefs/investor-reporting-ycharts-session-recovery-brief-20260910.md`
@`9a71ef7626`, sections IV.1 and IV.5-IV.7. This brief measures what of it is built and names only the delta.

## 0. Andrew's words, verbatim (2026-09-23, at the `4.0.0_SA_CRO` terminal)

> The runner host needs to be set up with the same pattern as we do elsewhere with ec2 rerun on stale cookie, followed by
> self-healing retry. THat should be featured potentially in a second brief if that framework is not already worked into
> the YCharts workflow here (which it may very well already be done, so be careful to not duplicate if so).

> I would give IRPT it's own credentials lib store, same pattern with however we do it for Black Diamond, Orion, etc.,
> however again that may already be implemented properly, so take care to note that.

> staleness detection is if a pull fails, need to see what error messages they send in failed pull if its 401 403 etc.

## 1. Answer

- **The credential store: ALREADY IMPLEMENTED, in the estate's pattern. No new store is needed.**
- **The stale-cookie framework: DESIGNED, and its parts BUILT (library, broker, SSM documents, host, IAM). Two things
  are missing:**
  1. **the deploy has never run**, so the runner code is not on the host;
  2. **the controller that turns "cookie stale" into "start EC2 -> run -> verify -> stop -> retry" was never
     built.**

  Those two are the whole delta.

## 2. What exists (measured 2026-09-23)

| Piece | State | Evidence |
|---|---|---|
| Login secret | EXISTS | `ycharts/login/credentials`, with a current version, last changed 2026-09-11 |
| Session secret | EXISTS, EMPTY | `ycharts/session/current`: no `AWSCURRENT` version today, last changed 2026-05-21 |
| Research session (proof of a live K3 login) | EXISTS | `ycharts/session/research-20260911`, with a current version (09-10 brief VI.4-VI.5) |
| Legacy shared cookie | EXISTS, LIVE | `ycharts/credentials` (2026-07-01); consumers are the gateway `ycharts_*` tools and the market-data pull. 09-10 brief IV.6: *"Preserve `ycharts/credentials` for legacy consumers"* |
| Runner library | BUILT, offline-proven | `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js`: `getSession`, `probeSession`, `acquireSession`, `persistSession` and `withAuthenticatedPage`; a DynamoDB lease on `irpt-jobs`; a monotonic fence checked at the write; bounded reacquisition (`YC_MAX_REACQUISITIONS`, default 1); no OTP branch; a Kimi vision fallback |
| Resume after an eviction | BUILT | `infra/aws/lambda/investor-reporting/ycharts/session/broker.py`: exactly ONE recovery per evicted job, verified three ways. It *"never logs in, never captures"* (`:19`), so it needs a fresh session to be put there by something else |
| SSM documents | BUILT, NEVER RUN | `irpt-ycharts-deploy` (artifact to host, installs Playwright/Chromium) and `irpt-ycharts-run` (`Task=probe` only). `ssm list-commands` shows 0 runs of either within SSM's retention |
| Host | BUILT, NOT DEPLOYED | `irpt-ycharts-runner` `i-0167fd745ad906a66` (t3.medium). The bootstrap installs OS dependencies, node and the secret-id pointers; *"runner code and browsers land at deploy"* (`infra/aws/terraform/investor-reporting/ycharts/instance.tf:110`). The run on 2026-09-23 failed rc 127 because `/opt/investor-reporting-ycharts/run-ycharts-session.sh` is absent |
| Host IAM | BUILT, exact | `irpt-ycharts-runner-role`: *"Get on three exact secret names, Put on ycharts/session/current ONLY, lease on irpt-jobs, artifact-prefix S3. No ec2 control plane"* (`infra/aws/lambda/investor-reporting/PATH_MANIFEST.json:3447`) |
| Controller: stale -> start -> run -> stop -> continue | **NOT BUILT** | no YCharts code calls `start_instances` or `send_command`. The only IRPT callers are `directory/refresh.py:678,699` (the directory builder) and `export/dispatch.py:195` (the render host) |
| Callers retrying through a refresh | **NOT WIRED** | the generation worker is not constructed live (companion brief section 3, hop 7), and the `/securities/*` lookups (companion section 5.4) do not exist yet |

## 3. The credential store, against the estate's pattern

| Vendor | Login secret | Session secret | Scope |
|---|---|---|---|
| Black Diamond | `blackdiamond/49f/credentials`, `blackdiamond/cot/credentials` | `blackdiamond/49f/session`, `blackdiamond/cot/session` | per firm (one BD login per firm) |
| Orion | `orion/credentials` | `orion/jwt/current` (+ `orion/eclipse_jwt/current`) | one login |
| **YCharts for IRPT** | **`ycharts/login/credentials`** | **`ycharts/session/current`** | **one Opal-wide seat** |

The IRPT store already has the Orion shape: one login secret plus one current-session secret, each under the vendor's
own prefix. It is not per firm, because the YCharts seat is Opal's rather than a firm's. Its runner role reads only its
named secrets and writes only the session. **Recommendation: keep it. Do not re-home it under an `irpt/` prefix.** A
rename would have to move three IAM grants, the runner's `secret-ids.env` pointers and the broker constant, for no
change in isolation.

The one real gap is **usage, not storage**. Today's live lookups had to use the legacy `ycharts/credentials`, because
`ycharts/session/current` is empty. Once the runner is deployed and has run once, IRPT lookups move to
`ycharts/session/current` (companion brief 5.4). The gateway and market-data pull stay on the legacy secret, as the
09-10 brief IV.6 already says.

⚠ Both secrets sign in the SAME shared seat (Alyssa, the automation, and the gateway's users). One automation drives it
at a time (the `irpt-jobs` lease), and a person signing in can evict it. The library's bounded reacquisition exists
for exactly this case.

## 4. The delta: two builds and one wiring

**D1 -- Deploy the runner (an operations act, under change management).**
- Send `irpt-ycharts-deploy` to `irpt-ycharts-runner`. That is the artifact plus Playwright/Chromium: egress to the
  browser mirror, which the README flags.
- Then send `irpt-ycharts-run Task=probe` once. That populates `ycharts/session/current` through `acquireSession` ->
  `persistSession` and proves the sign-in on the real page. The sign-in DOM is still a MODEL (README, "What the offline
  proof cannot show").
- Stop the host after, as the host is designed to be held stopped.
- **Gates:**
  - a YCharts sign-in by the automation is a live vendor call and needs Andrew's per-use word (README "Bounds";
    `run-ycharts-session.sh` header);
  - a person signed in at that moment may be evicted.
- **Cost:** one deploy plus one run; minutes of t3.medium.

**D2 -- Build the session controller: the BD pattern, as the 09-10 design specifies.**
- **Model on:** `infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py` (*"Probe, start host, wait for
  Running and SSM Online, send a command, process completion, stop host and invoke the intended continuation"*, 09-10
  brief IV.1). The same shape is in `cot-bd-session-trigger` and, for Orion, `inf-jwt-trigger` with
  `jwt_freshness.recover_or_exit()` (IV.2).
- **Interfaces, already specified in IV.5:** `probeSession`, `ensureSession`, `captureSession`, `completeRefresh`,
  `resumeRequest`.
- **Decision table, already specified in IV.7:**
  - an authenticated response continues with no EC2;
  - a 401 or a verified eviction refreshes once and requires a new verified generation;
  - a WAF interstitial is browser work, never a login loop;
  - a 429 backs off;
  - an ambiguous mutation reconciles before any replay;
  - a repeat eviction goes to attention, never to an endless contest.
- **Owned by the lease and fence** that the library and `irpt-jobs` already provide. A durable job wait and completion
  event is used rather than a Lambda held busy through browser start-up (IV.5), and continuations are idempotent.
- **What is new here:** only the Lambda that composes the pieces. Every rule it follows is written in IV.5-IV.7 and
  every lower-level piece exists.

**W1 -- Self-healing retry at every YCharts caller (wiring).**
- Each caller routes a stale-session signal to `ensureSession` and retries its read once, under the broker's one-refresh
  rule. The callers are the `/securities/check` lookups (companion 5.4) and the generation worker (companion 5.6).
- Reads (`securities_info`, typeahead) are safe to retry after a refresh. Mutations follow IV.7's reconcile-first row.

**Staleness is detected from a FAILED PULL, classified by status AND body** (Andrew, verbatim: *"staleness detection is if
a pull fails, need to see what error messages they send in failed pull if its 401 403 etc."*).

- **A separate liveness probe is not enough.** Measured 2026-05-20, a disturbed session failed `/model_portfolios/*`
  with 403 while `/indices/table_data`, the probe endpoint, returned 200 in the same second
  (`docs/briefs/mdsrc-ycharts-live-session-test-20260520.md:67`). So every pull classifies its own failure.
- **The classification the estate has already measured** (`docs/briefs/mdsrc-ws4-ycharts-operational-pattern-20260520.md:260-263`,
  bodies verbatim from live runs):

| Failed pull | Class | Action |
|---|---|---|
| HTTP 403, body contains `"You have been signed out due to a concurrent sign in using your credentials"` | **EVICTED** (another login took the seat) | refresh once (D2), retry the read. A repeat goes to attention (IV.7), never a login contest with a person |
| HTTP 403, body contains `"You are signed out. Please sign in again."` | **SIGNED OUT / disturbed** | refresh once (D2), retry |
| HTTP 403, body contains `"don't have access to this feature"` | **ENTITLEMENT**, not staleness | no refresh. For the lookup it counts as not available, the same as BREIT's `features_needed` gate (Andrew's paywall rule) |
| HTTP 200 whose body is HTML or a login page instead of the expected JSON | **NOT AUTHENTICATED** (the 09-10 brief IV.4 measured the legacy probe calling this healthy) | treat as signed out: refresh once, retry |
| HTTP 405 or 202 with an `x-amzn-waf-action` header | **WAF challenge** (09-10 brief IV.3, from AWS documentation) | browser work in D1/D2, never a password loop |
| HTTP 404 on a data endpoint | **bad symbol or route** (measured 05-26: `/indices/table_data` 404 on unresolved symbols, `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-26/yalp_macros_002_ycharts_test_pulls.md:98`) | not staleness; for the lookup it is NOT_FOUND |
| HTTP 429 or a timeout | transient | back off with jitter; no refresh |

- **Measured 2026-09-23 (the 2-call capture, on Andrew's word): `securities_info` succeeds with NO session.** With no
  cookie and with a junk session cookie it returned HTTP 200 and the full row. So:
  - (a) the ticker lookup needs no session at all and is outside this controller's scope;
  - (b) **a lookup success says nothing about session freshness.** Staleness is only observable on AUTHENTICATED pulls
    (the `/indices/table_data` probe, portfolio and report calls), and W1's classifier applies to those only.
- **Still UNCAPTURED, so the classifier's defaults must be conservative:**
  - the body when a cookie simply expires with age (today's 84-day-old cookie was still live);
  - the response to a request with no cookie or an invalid one ON AN AUTHENTICATED endpoint (the 2-call capture hit
    `securities_info`, which turned out to be open);
  - whether YCharts ever sends 401, since every observed auth failure so far was 403.
- **Unknown-body default:** a 401 or 403 whose body matches no row is treated as SIGNED OUT, refreshed once, then sent
  to attention.
- **The capture that would settle it:** two read-only calls, one with no cookie and one with a deliberately invalid
  session cookie, against `securities_info`. They carry no credential and no client data, but they are still vendor
  calls, so they **need Andrew's per-use word**.

## 5. Order, and what not to do

1. D1 first. Without a populated `ycharts/session/current`, D2 has nothing to verify against and W1 nothing to resume on.
2. D2 next.
3. Then W1 in the lookup endpoints and the worker.

**Do NOT:**
- build a second runner or a Lambda-container login (`infra/aws/lambda/ycharts-session-capture/` is the older
  Puppeteer design the 09-10 brief IV.4 rejected);
- create an `irpt/` secret namespace beside the existing store;
- point IRPT at `ycharts/credentials` permanently. That is a stopgap until D1.

## 6. Open with Andrew

1. **The per-use word for D1's sign-in run.** This is the automation's first real sign-in to YCharts.
2. **The per-use word for the two-call failed-pull capture** (no cookie, invalid cookie) in section 4 W1.
3. **The runner host `i-0167fd745ad906a66` is RUNNING,** started for today's lookup test. Stop it now, or keep it
   running for D1 if D1 is approved immediately.

## 7. What this brief does not claim

- SSM command history is only as long as SSM's retention. "Never run" means "no run within retention", and the
  missing file on the host corroborates it.
- "Session secret empty" is about today. Whether it held a version earlier is not established.
- The live K3 login proof (the research session of 09-11) is taken from the 09-10 brief's status section and the
  secret's existence. It was not re-run here.
