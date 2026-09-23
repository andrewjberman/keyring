# Andrew-direct 2026-09-23 ~18:2xZ -- per-use authorization: a small YCharts ticker-lookup test, and Kimi K3

Recorded by `4.0.0_SA_CRO` at its own terminal, BEFORE any vendor call. This is the per-use word the 2026-07-09
prohibition requires (`org/tier1_exec/2.0.0_SA_COO/deliverables/INCIDENT_unsanctioned_vendor_api_ycharts_20260709.md:13-17`).

## VERBATIM

> Yes do a small ycharts test now, may need to run the ec2 browser run if the cookie is stale

The same turn, on the Kimi design in `IRPT_ANALYSIS_UPLOAD_AND_TICKER_RESOLUTION_BRIEF_20260923.md` @`fa42eb206f`:

> Kimi should work fine, just model structure from the Kimi Estate Pipeline as we discussed regarding to how the json is
> set up/api call format

> K3 is the model we want to use

It answers the brief's section 7/8 open item, the capture of what YCharts returns for known, typo and unknown symbols.

## Bound this seat applies

- **Endpoints:** READ-ONLY lookups only: `GET /securities/securities_info` (one batch) and
  `GET /search/suggest/main` (typeahead).
- **Not called:**
  - no holdings upload;
  - no portfolio create;
  - no report generation;
  - no mutation of anything on YCharts.
- **Volume:** 5 symbols or fewer, about 3 requests, 2.0 s apart, plus the session's own liveness probe.
- **What leaves the estate:** the ticker symbols and the session credential. No client data, amounts, firm identifiers
  or holdings.
- **Session:** the IRPT session, `ycharts/session/current`. If it is stale or absent, the EC2 browser run
  (`irpt-ycharts-runner` via the SSM document `irpt-ycharts-run`) refreshes it, per Andrew's word above.
- **Calls made:** the call inventory is appended below once it is made, with each call's HTTP status.

## Second per-use authorization (~19:0xZ): the 2-call failed-pull capture

Andrew, VERBATIM, at this terminal: *"With that said, proceed through the 2-call testing"*. The two calls answer the
open item in `IRPT_YCHARTS_SESSION_SELF_HEAL_DELTA_BRIEF_20260923.md` section 4 W1: what YCharts sends on a failed pull.

**Bound:**
- EXACTLY two `GET /securities/securities_info?securities=AAPL` calls:
  - (a) with NO cookie at all;
  - (b) with a deliberately INVALID session cookie (`ycsessionid` and `csrftoken` set to junk values; no real credential
    read or sent).
- Redirects are NOT followed; the first response is recorded (status, `Location`, `content-type`,
  `x-amzn-waf-action`, body head).
- Nothing else is sent.
- The inventory is appended below.

## Call inventory (complete; UTC 2026-09-23)

**Session refresh attempt, with NO vendor contact:**
- **What was run:** `irpt-ycharts-runner` (`i-0167fd745ad906a66`) was started (stopped -> running, SSM online 18:21:33Z), and
  SSM command `05309085-4a7a-41d4-b070-b8d1b76832cf` was sent (`irpt-ycharts-run`, `Task=probe`, `MaxReacquisitions=1`).
- **Result:** **Failed, rc 127**: `/opt/investor-reporting-ycharts/run-ycharts-session.sh: No such file or directory`.
  The runner application is NOT deployed on the host, so nothing reached ycharts.com.
- **The IRPT session secret:** `ycharts/session/current` has no `AWSCURRENT` version (`VersionIdsToStages` null; last
  changed 2026-05-21T14:47Z). So it holds no current session today. That does NOT show it was never populated: an earlier
  version could have existed and been deprecated. (Corrected per `1.0.0_SA_CTO`, msg of 18:31Z.)

**The vendor calls: exactly FOUR, all HTTP 200.** Session: `ycharts/credentials` (last changed 2026-07-01T22:14Z,
84 days old, still live).

| # | Endpoint | Arguments | HTTP | Bytes |
|---|---|---|---|---|
| 1 | `GET /indices/table_data` (liveness probe) | `indices=^SPX, columns=ytd_total_return` | 200 | 1024 |
| 2 | `GET /securities/securities_info` | `securities=AAPL,ALPPL,VNQ,BREIT,$:CASH` | 200 | 1003 |
| 3 | `GET /search/suggest/main` | `q=ALPPL` | 200 | 103 |
| 4 | `GET /search/suggest/main` | `q=BREIT` | 200 | 3527 |

- **Spacing:** 2.0 s between calls.
- **What left the estate:** the five symbols, `^SPX` and the column name, with the shared session cookie. No client
  data, amounts, firm identifiers or holdings.
- **Where the responses are:** `IRPT_YCHARTS_LOOKUP_CAPTURE_20260923/` beside this file. They are public security
  metadata only; a scan for cookie and session markers found none.
- **Not called:** no upload, no portfolio create, no report generation, no mutation.

## What the capture measured

1. **An unknown symbol is SILENTLY OMITTED by `securities_info`.** 5 symbols were sent and 3 returned (AAPL `stock`,
   VNQ `etf`, `$:CASH` `cash`). `ALPPL` and `BREIT` are simply absent, with no error entry and no null row. "Not
   found" must therefore be computed as the set difference between what was sent and what came back.
2. **For `ALPPL`, YCharts' typeahead returned NO candidates.** `suggest?q=ALPPL` returned all ten category lists empty
   (`alt, r, cs, mp, pmp, sa, co, ind, idx, mf`). That is ONE probe. It shows the typeahead did not rescue this typo; it
   does NOT establish that the typeahead has no typo tolerance in general. (Corrected per `1.0.0_SA_CTO`, msg of 18:31Z;
   this seat's first draft said "NO typo tolerance".) For the design it is enough that YCharts cannot be relied on for
   the suggestion, so the Kimi check call stays.
3. **A private REIT is KNOWN but gated.** `suggest?q=BREIT` returned 9 mutual-fund share classes (`M:BREIT.S`,
   `M:BREIT.L`, ... `M:BREIT.I`). All 9 carry `features_needed: ["evergreenFundData"]` with `all_features_required:
   true`, and the bare `BREIT` is not found by exact lookup. Whether this seat has that feature is unmeasured; if it does
   not, the swap path applies to private REITs too.
4. **Fund identifiers are namespaced.** Mutual funds appear as `M:<ticker>` in the search results. Whether
   `securities_info` resolves a bare mutual-fund ticker without the `M:` prefix is unmeasured; this capture stayed
   inside its 5-symbol bound.
5. **The session:** the 84-day-old `ycharts/credentials` session is live. The IRPT session path cannot run today: its
   secret has no current version and the runner application is not deployed.
6. **The 2-call failed-pull capture (second authorization, ~19:0xZ). Exactly two calls, both HTTP 200:**

   | # | Call | HTTP | Result |
   |---|---|---|---|
   | 5 | `GET /securities/securities_info?securities=AAPL` with NO cookie | 200 `application/json`, 338 B, 0.11 s | the full AAPL row, identical to the authenticated call |
   | 6 | the same with a junk `ycsessionid`/`csrftoken` | 200 `application/json`, 338 B, 0.07 s | the same AAPL row; the response set a fresh `csrftoken` cookie (name recorded, not the value) |

   Neither response had a redirect or a WAF action header. Fixtures: `05_no_cookie.json`, `06_invalid_session.json`.

   **Finding: `securities_info` does not require a session.** An exact-symbol lookup works without authentication,
   so:
   - (a) the `/securities/check` endpoint needs NO YCharts session: no seat, no lease, no eviction risk, no refresh;
   - (b) **this endpoint cannot detect staleness**, because it succeeds regardless.

   The failed-pull shape for AUTHENTICATED endpoints (the `/indices/table_data` probe, report generation) is still
   uncaptured. The May bodies in the self-heal brief (403 "signed out ...") remain the best evidence there. The two calls
   stayed inside their bound; no further call was made.
7. **Exact-lookup absence is a different fact from a namespaced or gated identity.** `BREIT` is absent from the exact
   lookup (item 1), while `M:BREIT.*` exists behind a feature gate (item 3). A resolver treats these as two different
   states, not one.
