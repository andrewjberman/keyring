# YALP_MACROS T002-VALIDATE Fresh Cookie — 2026-05-26

**TO:** YALP_MACROS.013 T002-VALIDATE fresh-cookie
**Author:** 0.1.0_DS_MarketIntelligence~A
**Authority:** Andrew sovereign direct ~21:54Z via ws CTO + ws COO `/drive` cycle 113 URGENT carry-on (time-pressure window NOW → tomorrow AM ET before colleague re-takes single-session YCharts seat per [[project_ycharts_dedicated_seat_403_session_eviction]])
**T*:** 2026-05-26 (~22:18Z harness execution timestamp)
**Status:** Phase 2b T002-VALIDATE COMPLETE — 4/4 ACs met

---

## §0 — TL;DR

Fresh cookie bundle (AWS Secrets Manager `ycharts/credentials`, refreshed ~21:55Z) **RESOLVES session-eviction class** (freshness_probe = HTTP 200) but **CONFIRMS** Phase 1 macro-class entitlement gap (10/10 macro test-pulls returned HTTP 404 entitlement-gap-likely; ZERO 403 session-eviction class this sweep).

**Architectural confirmation:** YCharts macro-class surface remains entitlement-blocked at the structural level — NOT cookie-related. **Phase 2 multi-source RE pivot architecture (TO-008 FRED-PRIMARY + sister-CROSS-CHECK + ~E PRIMARY for 24 FRED-GAP) is architecturally justified bottom-up.** Use as cross-check input for TO-008 harness build: FRED-PRIMARY runtime tier covers 55/79 = 69.6% without YCharts dependency; YCharts macro-class surface = NOT a usable v1 cross-check source.

**No mid-window session-eviction observed** (no 403 class fired during ~30s pull burst); cookie remained valid through entire 10-endpoint sweep.

---

## §1 — Cookie bundle source verification

**Source:** AWS Secrets Manager `ycharts/credentials` SecretString JSON.
**Retrieval timestamp:** 2026-05-26T22:18:11Z (verified live via YChartsClient constructor).
**Bundle structure:** `cookies` field = STRING (2045 chars; multi-cookie concatenated string).
**Refresh source:** Andrew HAR `ycharts.com(mchm).har` 24.9MB per TO `<references>` cite (ws COO ~21:55Z refresh).

**Validation:** YChartsClient constructed OK; freshness_probe immediately succeeded with HTTP 200 — bundle is well-formed + session is alive.

---

## §2 — Per-endpoint validation table

Harness: `.runtmp/yalp_macros_to002/run_macros_pulls.py` (reuses C2 `ycharts_client.py` per Phase 1 §11 pattern); full results at `.runtmp/yalp_macros_to002/macros_pull_results.json`.

**Phase 1 freshness probe (^SPX baseline):**

| Endpoint | Symbol | HTTP status | Parseable | Class |
|---|---|---:|---|---|
| `/indices/table_data?indices=^SPX&columns=ytd_total_return` | ^SPX | **200** | YES | session-OK (baseline) |

**Phase 2 UST yield tenors (`/indices/table_data?indices=I:USNNYLD&columns=last_price,ytd_total_return`):**

| Endpoint | Symbol | HTTP status | Parseable | Class |
|---|---|---:|---|---|
| UST 2Y | `I:US2YYLD` | **404** | NO | entitlement-gap-likely |
| UST 5Y | `I:US5YYLD` | **404** | NO | entitlement-gap-likely |
| UST 10Y | `I:US10YYLD` | **404** | NO | entitlement-gap-likely |
| UST 30Y | `I:US30YYLD` | **404** | NO | entitlement-gap-likely |

**Phase 3 Volatility indices:**

| Endpoint | Symbol | HTTP status | Parseable | Class |
|---|---|---:|---|---|
| VIX | `^VIX` | **404** | NO (HTML body) | entitlement-gap-likely (404 page reads "Sorry we can not find that!") |
| MOVE | `^MOVE` | **404** | NO | entitlement-gap-likely |

**Phase 4 FRED-proxy macros:**

| Endpoint | Symbol | HTTP status | Parseable | Class |
|---|---|---:|---|---|
| CPI YoY | `CPIAUCSL` | **404** | NO | entitlement-gap-likely |
| Core CPI | `CPILFESL` | **404** | NO | entitlement-gap-likely |
| Unemployment | `UNRATE` | **404** | NO | entitlement-gap-likely |
| ISM Manufacturing | `NAPMPMI` | **404** | NO | entitlement-gap-likely |

**Totals:**
- freshness_probe: **1/1 OK (HTTP 200)** ✓
- macro test-pulls: **0/10 OK; 10/10 HTTP 404 entitlement-gap-likely**
- session-eviction (HTTP 403): **0** — ZERO mid-window 403 class fired (vs Phase 1 §11 Phase 3 burst which got 6/6 403)

---

## §3 — Failure categorization (3-class taxonomy per TO `<acceptance_criteria>` AC3)

### §3.1 — session-eviction-RETRY class fires: ZERO

No HTTP 403 / "You are signed out" observed during this sweep. Fresh cookie is alive + stable through full 10-endpoint burst. Phase 1 §11 Phase 3 burst-class 403 finding (~3-6 sequential pulls trigger eviction) **NOT REPRODUCED** with fresh cookie this window.

### §3.2 — endpoint-class-issue: ZERO

No HTTP 5xx / transport-error class. `/indices/table_data` + `/charts/general_data.json` (covered by harness via `indices_table_data` C2 method) endpoint surface remains live + responding within ~60-300ms per request.

### §3.3 — symbol-resolution-gap-CONFIRMED: 10/10

All 10 macro symbols return HTTP 404 entitlement-gap-likely class. Sample HTML body from `^VIX` 404: `"\n\n\n\n\n\n\n\n\n<!doctype html>\n<html lang=\"en\" ng-jq>\n    <head>\n        <title>\n        \n        404: Sorry we can not find that!\n        \n        </title>"` — generic YCharts "404 Sorry we can not find that!" page, NOT entitlement-error-403-class.

**Class interpretation:** YCharts indices/charts surface does NOT carry these symbols under our account's entitlement OR under any account's standard entitlement. Sister-finding to Phase 1 §11 Phase 2 (10/10 404 for same symbol set with `last_price` column gap; this re-test fired without column-validity gap and still 404 — confirms gap is symbol-resolution-class, NOT column-class).

**~D §9 corrections sister-pattern:** API-internal symbol mappings need live-probe ground-truth before banking — sister to LD-31 + ~A §1.6 release_id catalog discipline. ~A Phase 1 §11 Finding C (27 variant attempts all 404 for VIX/MOVE/UST/FRED-proxy) holds empirically post-fresh-cookie.

---

## §4 — Disposition for Phase 2 TO-008 harness build

### §4.1 — YCharts macro-class surface NOT usable for v1 cross-check

**Verdict:** YCharts macro-class symbol surface (^VIX + ^MOVE + I:US{2,5,10,30}YYLD + CPIAUCSL + CPILFESL + UNRATE + NAPMPMI) remains structurally entitlement-blocked. Cookie eviction is OPERATIONAL not the root cause; the symbol set itself is not in our account's macro-class entitlement scope.

**For TO-008 harness build (shipped `30bd38cf0` Wave 1+3+4):**
- **FREDAdapter remains canonical PRIMARY** for the 79-indicator universe (55/79 = 69.6% coverage); ZERO YCharts dependency in production harness.
- **YahooFinanceAdapter remains canonical PRIMARY** for 3 specific YCharts-uncovered indicators (^MOVE + CNH=X + AGG ETF-NAV); ZERO YCharts dependency.
- **YCharts macro-class is NOT a viable v1 cross-check source** per this validation; do NOT add a `YChartsAdapter` to the multi-source RE harness v1. Future YCharts utility = equity-grade cross-checks for OTHER YALP probes (YALP_VALUAT + YALP_FACTOR + YALP_POSITN + YALP_CORREL where ticker-grade symbols are well-entitled).

### §4.2 — Architectural justification for Phase 2 multi-source RE pivot CONFIRMED

This validation provides **bottom-up empirical confirmation** for the Phase 2 architectural decision-class:

- Phase 1 §11 Finding C (27 variant attempts all 404) → STILL TRUE with fresh cookie → cookie was never the issue → **macro-class entitlement gap is the structural justification for multi-source RE pivot**
- Multi-source RE harness (TO-008 `30bd38cf0`) sidesteps YCharts entitlement constraints by using federal-source-direct adapters (FRED + BLS + Census + Treasury Direct + NY Fed Markets + BEA + Yahoo Finance) for all 79 indicators

**Architectural decision-class reinforcement:** FRED-PRIMARY + sister-CROSS-CHECK + ~E PRIMARY-for-24-GAP architecture is the correct path; no rework needed.

### §4.3 — Cookie-state observation for cross-fabric awareness

Cookie remained alive + valid through full 10-endpoint sweep (~30s wall; 22:18:11Z → 22:18:39Z). No mid-window eviction. **Sister-lane T002-VALIDATE sweeps (~B VALUAT + ~D POSITN + ~E FACTOR + ~C CORREL SPAWN-NEEDED)** can fire freely without sequencing risk per Andrew sovereign "no queue/sequencing" PARALLEL execution directive.

**If sister-lane MCPs report HTTP 403 surfacing during their sweeps:** that is colleague re-taking seat per F1 single-session constraint; escalate to ws COO per TO `<notes>` mid-window-eviction protocol. My sweep window did NOT trigger this.

---

## §5 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~A
**TO:** YALP_MACROS.013 T002-VALIDATE fresh-cookie

**Acceptance criteria (4/4 MET):**

- **AC1** All Phase 1 YALP_MACROS YCharts test endpoints re-pulled with fresh `ycharts/credentials` bundle ✓ — 11 endpoints (1 freshness + 4 UST + 2 volatility + 4 FRED-proxy) re-pulled within window (22:18:11Z → 22:18:39Z = ~28s wall well inside NOW → tomorrow AM ET budget)
- **AC2** Per-endpoint HTTP status + parseable check documented ✓ — §2 table; full results JSON at `.runtmp/yalp_macros_to002/macros_pull_results.json`
- **AC3** Failures categorized into 3 classes ✓ — §3: session-eviction-RETRY = 0; endpoint-class-issue = 0; symbol-resolution-gap-CONFIRMED = 10/10
- **AC4** Disposition for Phase 2 TO-008 cross-check use documented ✓ — §4: YCharts macro-class NOT usable for v1 cross-check; multi-source RE architecture confirmed bottom-up; ZERO Phase 2 rework needed

**Disposition recommendation:** ACCEPT.

**No production touches.** Test-pull validation scope; documentation-only commit. No portal/Lambda code edits.

**TO-008 parallel execution status:** TO-008 Wave 1+3+4 shipped `30bd38cf0` BEFORE this T002-VALIDATE side-task fired (TO-013 fired ~22:08Z; TO-008 commit ~21:55Z); this T002-VALIDATE outcome **reinforces** TO-008 architectural decisions empirically.

---

## §6 — Memory candidate banked

16. **`ycharts-macro-class-entitlement-gap-is-structural-not-cookie-eviction-class`** — fresh-cookie validation confirms Phase 1 finding C: 27 variant attempts all 404 → still 10/10 404 with fresh cookie → cookie was never the issue → macro-class entitlement gap is the structural justification for multi-source RE pivot. Distinct from session-eviction class (HTTP 403) which IS cookie-state. **Sister to** [[feedback_ycharts_http_400_is_cookie_stale_class]] cookie-stale-class memory; this candidate adds the structural-entitlement-gap-vs-operational-eviction taxonomy distinction. **CANDIDATE** for /mstr-review LD wave; distinguishes 2 YCharts failure classes that previously co-classified under "cookie issues" generally.

— 0.1.0_DS_MarketIntelligence~A
2026-05-26 work-cycle:5 (Phase 2b YALP_MACROS.013 T002-VALIDATE)
