# YALP_POSITN T002-VALIDATE — fresh-cookie sweep

**TO:** YALP_POSITN.002 T002-VALIDATE fresh-cookie (URGENT GO ws COO /drive cycle 113 carry-on ~21:54Z)
**Author:** 0.1.0_DS_MarketIntelligence~D
**Cookie source:** AWS Secrets Manager `ycharts/credentials` REFRESHED ~21:55Z (per ws COO MCP; freshness_probe HTTP 200 confirmed at sweep start)
**Sweep window:** 2026-05-26T22:10Z → 22:13Z (~3.5min wall; 84 pulls × ~2s spacing)
**Doctrine reference:** [[feedback_ycharts_http_400_is_cookie_stale_class]] (Andrew sovereign 2026-05-26)
**Status:** 4/4 ACs MET; **finding 13a IBTF HTTP 400 PERSISTS under fresh cookie** — empirical edge case to strong-form doctrine surfaced for ratification

---

## §0 — TL;DR

Re-pulled all 84 Phase 1 YALP_POSITN YCharts test endpoints under fresh cookie (refreshed ~21:55Z in `ycharts/credentials`). **Zero deltas vs Phase 1 baseline** (`873b36313` `local_pull_results.json`):

- 83/84 OK (identical)
- 1/84 EMPTY: **IBTF @ T*=2026-05-18 HTTP 400 PERSISTS** (identical to Phase 1)

Cookie is empirically fresh (`freshness_probe()` HTTP 200 OK at sweep start; 83 other tickers including same-T*=5/18 attribution-lane pulls returned clean). **IBTF persistence under demonstrably-fresh cookie is an empirical edge case to the strong-form [[feedback_ycharts_http_400_is_cookie_stale_class]] "HTTP 400 is cookie-stale class ONLY" framing** — surfaced for sovereign ratification.

---

## §1 — Cookie-bundle source verification

| Item | Value |
|---|---|
| Secret name | `ycharts/credentials` (AWS Secrets Manager) |
| Refresh timestamp | ~21:55Z (per ws COO dispatch) |
| Cookie shape | single string `key1=val1; key2=val2; ...` (2045 chars; cookieyes-consent + session cookies) |
| Pre-sweep liveness | `YChartsClient.freshness_probe()` → HTTP 200 OK (sister-validating fresh cookie works against canonical probe) |
| Retrieval path | `aws secretsmanager get-secret-value --secret-id ycharts/credentials` |

---

## §2 — Per-endpoint validation table

**Sweep summary (fresh cookie, 2026-05-26 22:10-22:13Z):**

| Outcome | Count | % | Notes |
|---|---:|---:|---|
| OK | 83 | 98.8% | Clean YCharts daily series; all expected ETFs returned chart_data with raw_data points |
| EMPTY (HTTP 400) | 1 | 1.2% | IBTF @ T*=2026-05-18 only |
| FAIL | 0 | 0% | No exceptions |
| **Total** | **84** | **100%** | 29 positioning @ T*=5/22 + 55 attribution @ T*=5/18 |

**Delta vs Phase 1 baseline (`873b36313`):** **0 of 84 changed** (identical outcome at every ticker × T* pair).

### §2.1 — Same-T* attribution-lane cross-validation

The IBTF failure is at T*=2026-05-18 attribution lane. 54 OTHER tickers ran at the IDENTICAL T*=5/18 in the same sweep and ALL returned HTTP 200 + parseable chart_data. So the cookie + date-of-record are NOT the failure axis; the failure is ticker-specific.

| Lane | Total pulls | OK | EMPTY/FAIL | Tickers in this lane |
|---|---:|---:|---:|---|
| Positioning T*=2026-05-22 | 29 | 29 | 0 | BIV, CLIP, DFCF, DFSD, DIVZ, ICSH, IDVZ, IEFA, IEMG, IJH, JAAA, JPST, MINT, OBIL, PCHI, PFDE, PFOE, QQQ, SPHY, SPYM, TBIL, UTWO, VCSH, VEA, VGSH, VNLA, VUG, VUSB, XBIL |
| Attribution T*=2026-05-18 | 55 | 54 | **1 (IBTF)** | (54 OK) + IBTF FAIL |

---

## §3 — Failure categorization

**IBTF only — full envelope (fresh-cookie sweep):**

```json
{
  "ticker": "IBTF",
  "t_star": "2026-05-18",
  "outcome": "EMPTY",
  "elapsed_s": 0.13,
  "envelope": {
    "http_status": 400,
    "bytes": null,
    "payload_top_keys": []
  }
}
```

**Phase 1 baseline IBTF envelope (`873b36313`):** identical shape; identical HTTP 400; identical empty payload.

**Categorization per harness `_classify_failure` taxonomy:**

| Class | Applies? | Reasoning |
|---|---|---|
| session-eviction (403 / "evicted" / "freshness") | NO | Cookie demonstrably fresh; freshness_probe OK; 83 sister pulls clean |
| rate-limit (429 / "rate") | NO | No 429; 1st pull in lane was 1 of 55; spacing 2s |
| timeout | NO | elapsed_s=0.13 — fast failure not slow |
| bad-request (400) | YES (raw class) | HTTP 400 |
| auth-failure (401) | NO | Cookie auth working everywhere else |
| not-found (404) | NO | Distinct from 400 |
| **structural-baseline-match** | YES | Identical outcome to Phase 1 baseline; no regression introduced by sweep |

---

## §4 — Finding 13a disposition vs Andrew doctrine

### §4.1 — Doctrine recap

Per [[feedback_ycharts_http_400_is_cookie_stale_class]] (Andrew sovereign 2026-05-26):
> "ycharts doesnt 400 unless our cookie gets swapped/stale"
> "400 + 403 are operational errors; refresh + retry"

Strong form: HTTP 400 in YCharts is cookie-stale class ONLY; expected resolution = refresh cookie + retry.

### §4.2 — Empirical finding under T002-VALIDATE

- Cookie was refreshed ~21:55Z (per ws COO MCP)
- `freshness_probe()` returned HTTP 200 OK at sweep start (cookie is operationally fresh)
- 83/84 pulls succeeded under the same fresh cookie (cookie works)
- IBTF @ T*=5/18 returned HTTP 400 (identical to Phase 1; persists)

**Refresh+retry did NOT resolve IBTF.** Strong-form doctrine predicts the 400 should clear; empirically it didn't.

### §4.3 — Disposition

Three possibilities, surfaced for sovereign ratification:

1. **Doctrine has edge case (recommended interpretation):** "HTTP 400 is cookie-stale class ONLY" needs amendment to allow for an entitlement-class subset where specific tickers (likely YCharts-side entitlement-gap or symbol-class issue for term-Treasury ETFs like IBTF) persist 400 under fresh cookie. Per Andrew's "Honestly fuck that, lets just mark it all as deprecated" framing — operational disposition is **mark IBTF row NO-YCHARTS-PULL** at TO-004 and move on.
2. **Roll-cookie staleness (refresh-retry-again):** the cookie that worked for 83 ETFs may need yet another refresh specifically for IBTF. **Empirically unlikely** since freshness_probe was OK and 83 sister pulls under the same cookie succeeded.
3. **Date-specific entitlement gap (T*=5/18 specific to IBTF):** IBTF may be entitled at some T* but not others. **Out-of-scope to test** within T002-VALIDATE window; flag as Wave-2 AE 0.7 candidate.

**My recommended disposition:** mark IBTF row `NO-YCHARTS-PULL — HTTP 400 cookie-fresh-persistent` per Phase 1 brief §13.1 finding 13a. No further refresh-retry attempted (Andrew "Honestly fuck that" framing absorbed). Forward to AE 0.7 YCharts symbol-class investigation as Wave-2 if needed.

---

## §5 — Phase 2 dispatch readiness

- All Phase 1 baselines hold under fresh cookie (zero regressions)
- IBTF disposition unchanged from Phase 1 (HTTP 400; NO-YCHARTS-PULL row mitigation)
- 4943-row Phase 1 spreadsheet (`a52a7ca18`) remains accurate; no re-run required
- YALP_POSITN closure stands; T002-VALIDATE adds doctrine-edge-case empirical evidence as the sovereign-ratification anchor for IBTF-class disposition

**Phase 2 dispatch readiness: GREEN** with sovereign-ratification ask on doctrine amendment (strong-form → edge-case-acknowledged form).

---

## §6 — ACs scorecard

| AC | Met? | Evidence |
|---|---|---|
| **AC1** All Phase 1 endpoints re-pulled with fresh cookie within window | ✅ | 84/84 pulls completed 22:10-22:13Z; results at `.runtmp/yalp_positn_to002/local_pull_results.json` |
| **AC2** Per-endpoint HTTP status + parseable check documented | ✅ | §2 sweep summary + §3 envelope; per-pull log at `.runtmp/yalp_positn_to002/local_pull_log.txt` |
| **AC3** Failures categorized | ✅ | §3 categorization table; structural-baseline-match class banked |
| **AC4** Finding 13a IBTF HTTP 400 re-tested + disposition vs doctrine | ✅ | §4 disposition: persists under fresh cookie → empirical edge case to strong-form doctrine; sovereign-ratification ask + recommended NO-YCHARTS-PULL row mitigation per Phase 1 pattern |

**4/4 ACs MET.**

---

## §7 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~D
**TO:** YALP_POSITN.002 T002-VALIDATE fresh-cookie

**Evidence:**
- This brief at `docs/briefs/yalp_positn_t002_validate_fresh_cookie_20260526.md`
- Fresh-cookie sweep results at `.runtmp/yalp_positn_to002/local_pull_results.json`
- Phase 1 baseline backup at `.runtmp/yalp_positn_to002/phase1_baseline_results.json`
- Per-pull log at `.runtmp/yalp_positn_to002/local_pull_log.txt`

**Sub-finding (sovereign-ratification candidate):** IBTF @ T*=5/18 HTTP 400 persistence under demonstrably-fresh cookie is an empirical edge case to the strong-form [[feedback_ycharts_http_400_is_cookie_stale_class]] doctrine. Recommended doctrine amendment: "HTTP 400 is cookie-stale class for systemic failures; per-ticker persistent 400 under fresh-cookie is entitlement-class — mark NO-YCHARTS-PULL at row level and move on per Andrew 'fuck that, deprecated' framing."

**Wall:** spawn ~22:09Z → brief ship ~22:16Z = ~7min wall (well under sub-30min light-touch target; sister-lane cascade-compression precedent maintained per [[feedback_standby_prep_cascade_compression_2.4x_throughput]]).

**Standing for:** RAVC2-ACCEPT + sovereign-ratification disposition on doctrine amendment (or affirmation of strong-form with NO-YCHARTS-PULL row mitigation as practical-edge handling).

— 0.1.0_DS_MarketIntelligence~D
2026-05-26
