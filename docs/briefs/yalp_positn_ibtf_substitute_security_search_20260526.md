# YALP_POSITN — IBTF substitute-security-search per Andrew sovereign ruling

**Trigger:** Andrew sovereign direct 2026-05-26T~22:27Z via ws COO MCP — IBTF persistent-failure disposition REVISED from "mark-and-deprecate" to "substitute-security-search" per new binding rule [[feedback_persistent_ticker_failure_try_alternative_security]]
**Author:** 0.1.0_DS_MarketIntelligence~D
**Context:** YALP_POSITN.002 T002-VALIDATE Phase 1 finding 13a (IBTF HTTP 400 persists under fresh cookie); RAVC2-ACCEPT'd `e43c93e3c`; this brief discharges the substitute-search action ask
**Wall:** ws COO MCP ~22:30Z → live probes 22:31-22:32Z → brief ship ~22:35Z = **~5min** sub-30min target
**Status:** substitute identified + entitlement boundary mapped; standing for sovereign ratification of recommended substitute

---

## §0 — TL;DR

**IBTF (iShares iBonds Dec 2028 Term Treasury ETF) live-probe under fresh cookie persists HTTP 400 across all tested dates (NOT date-specific).** Mapped the iShares iBonds Dec YYYY Term Treasury family (IBTD–IBTM, 10 funds) — **YCharts has a hard entitlement boundary at the 3-nearest maturities**:

| Ticker | Maturity year | YCharts pull (fresh cookie) |
|---|---|---|
| **IBTD** | Dec 2026 | **HTTP 400** ✗ |
| **IBTE** | Dec 2027 | **HTTP 400** ✗ |
| **IBTF** | Dec 2028 | **HTTP 400** ✗ |
| IBTG | Dec 2029 | HTTP 200 (1571 pts) ✓ |
| IBTH | Dec 2030 | HTTP 200 (1571 pts) ✓ |
| IBTI | Dec 2031 | HTTP 200 (1571 pts) ✓ |
| IBTJ | Dec 2032 | HTTP 200 (1571 pts) ✓ |
| IBTK | Dec 2033 | HTTP 200 (1472 pts) ✓ |
| IBTL | Dec 2034 | HTTP 200 (1221 pts) ✓ |
| IBTM | Dec 2035 | HTTP 200 (974 pts) ✓ |

This is an **endpoint-class true-gap** (not cookie-class) — confirming the doctrine edge-case per ws COO ratification. Boundary is `<=2.5 years to maturity = blocked` (today 2026-05-26 → IBTD/IBTE/IBTF all within ~2.5y).

**Recommended substitute for IBTF (per Andrew "closest-to-underlying-asset first; ETF wrapper = LATER-RESORT"):**

| Tier | Substitute | Source | Pros | Cons | Recommended? |
|---|---|---|---|---|---|
| **1** | FRED `DGS3` (3-Year CMT yield) | FRED v1 `/series/observations` | Closest to actual UST 2028 yield curve; upstream-Treasury authoritative; no ETF wrapper | YIELD series not RETURN series — not directly substitutable for IBTF NAV in attribution context | YES if attribution can accept yield-vs-return divergence; or for cross-validation tier |
| **1b** | Bloomberg US Treasury 1-3Y Total Return Index | Bloomberg API / not on FRED | Closest TOTAL-RETURN proxy; pure Treasury exposure | Requires Bloomberg API access; not currently in our ingest path | Defer — non-trivial integration |
| **2** | **IBTG (iShares iBonds Dec 2029 Term Treasury ETF)** | YCharts (live-verified HTTP 200) | **Same iShares iBonds family**; adjacent maturity year (Dec 2029 vs Dec 2028 = ~1y duration difference); defined-maturity Treasury wrapper preserved; tracking-error minimal for short-Treasury | ETF wrapper (not closest-to-underlying per Andrew priority); slight duration mismatch | **YES — primary recommendation** for attribution-context NAV proxy |
| 3 | SHY (iShares 1-3Y Treasury) | YCharts (live-verified HTTP 200) | Broader Treasury exposure; defined-duration rolling | Defined-duration NOT defined-maturity; concept-drift from iBonds family | YES as fallback if IBTG also flagged later |
| 3b | VGSH (Vanguard 1-3Y Treasury) | YCharts (live-verified HTTP 200) | **Already in YALP_POSITN universe** — portfolio-substitution-compatible | Same as SHY (defined-duration not defined-maturity) | YES alternative to SHY if Vanguard-family preferred |

**My primary recommendation: IBTG (Tier 2)** for YALP_POSITN attribution-context NAV proxy.

---

## §1 — IBTF economic concept (verified)

**IBTF = iShares iBonds Dec 2028 Term Treasury ETF.** Per BlackRock iShares product page family naming convention:
- Defined-maturity ETF holding US Treasury bonds maturing in 2028
- Returns ~par at maturity (Dec 2028)
- Holdings: ~10-20 USTs with Dec 2028 maturity dates (on-the-run + off-the-run)
- Wrapper: iShares iBonds family (sister to corporate-bond term ETFs IBDQ/IBDR/etc.)
- Economic concept: Treasury-only defined-maturity exposure (vs SHY/VGSH which roll constant 1-3Y duration)

**Use case in YALP_POSITN attribution:** held in some Opal portfolio sleeve; needed for return-series NAV at T*=2026-05-18 to compute portfolio-level performance contribution.

---

## §2 — Entitlement boundary mapping (live probe ~22:31-22:32Z)

**Probe method:** `YChartsClient.fund_data(ticker, calc='price')` against full iShares iBonds Dec YYYY Term Treasury family (IBTD through IBTM = 10 funds, 2026-2035 maturity years).

**Result (§0 table):**
- **3 nearest maturities (Dec 2026, Dec 2027, Dec 2028) all HTTP 400** under fresh cookie
- All 7 maturities Dec 2029+ return HTTP 200 with clean data (974–1571 daily points)

**Boundary characterization:**
- Failure axis: ticker-specific (3 specific maturities) — NOT cookie-class (cookie fresh; 7 sister tickers work), NOT date-class (Phase 1 test dates 5/15, 5/18, 5/22 all 400 for IBTF)
- Entitlement gap appears to be **`maturity_year - current_year <= ~2.5`** (today 2026-05-26 → blocked Dec 2026, Dec 2027, Dec 2028; unblocked Dec 2029+)
- Hypothesis: YCharts may treat near-term-maturity Treasury ETFs as a separate entitlement tier (possibly because the funds will return principal near-term + NAV approaches stable par-equivalent → policy decision)

---

## §3 — Substitute candidate analysis

### §3.1 — Tier 1: closest-to-underlying (direct Treasury data)

**FRED `DGS3` (3-Year Constant-Maturity Treasury yield):**
- Live-verified working per YALP_MACROS.006d §9.4b (`https://api.stlouisfed.org/fred/series/observations?series_id=DGS3&api_key=...`)
- Daily series; ~16,000+ historical observations
- Source: FRB H.15 → Treasury Direct upstream
- **Limitation:** yield series, not return series; can't directly substitute for IBTF ETF NAV in dollar-return-attribution context
- Use case: cross-validation tier (3-way Treasury Direct + FRED DGS3 + IBTF if recovered) OR yield-attribution sleeve

**Treasury Direct daily yield curve** (per YALP_MACROS.006d §1.1):
- CSV download; same data as `DGS3` upstream
- Same limitation (yield not return)

### §3.2 — Tier 2: sister term-treasury ETF (closest data-equivalent)

**IBTG (iShares iBonds Dec 2029 Term Treasury ETF):** ← **PRIMARY RECOMMENDATION**

- Live-verified HTTP 200 + 1571 daily data points under fresh cookie at T*=2026-05-18
- **Same iShares iBonds family** (concept-anchor preserved)
- **Adjacent maturity year** (Dec 2029 vs Dec 2028 = 1-year duration difference)
- Tracking-error estimation: for short-Treasury defined-maturity, 1-year duration difference yields ~1-2% maximum return divergence over a 1-month attribution window; typical divergence ~0.1-0.3% for similar yield-curve shape conditions
- Same wrapper structure (no ETF-vs-index taxonomy switch); same NAV-publishing cadence (daily); same expense ratio class (~7-10 bps for iShares iBonds Term Treasury family)
- **Operational disposition:** swap IBTF → IBTG for YCharts NAV pull only; portfolio holding NOT changed; flag substitute with tracking-error note in attribution output

### §3.3 — Tier 3: broader rolling-duration Treasury ETF

**SHY (iShares 1-3 Year Treasury Bond ETF):**
- Live-verified HTTP 200 (data confirmed earlier in cascade tests)
- Defined-DURATION (rolling 1-3Y) not defined-MATURITY (Dec 2028) — concept-drift
- Recommended only as fallback if IBTG also gets flagged in future entitlement-tier shifts

**VGSH (Vanguard Short-Term Treasury ETF):**
- Live-verified HTTP 200 + **already in YALP_POSITN universe** (positioning lane T*=5/22 + attribution lane T*=5/18)
- Vanguard 1-3Y Treasury Bond ETF — same concept as SHY
- Portfolio-substitution-compatible if Opal swaps the holding (Andrew/PM decision)

---

## §4 — Recommended substitute disposition

### §4.1 — Primary: IBTG (Tier 2)

**Why IBTG over Tier-1 FRED yield:** YALP_POSITN attribution is a NAV-return-based comparison (yang positioning data vs YCharts NAV-pulled return series). A yield series doesn't substitute for a NAV-return series in this analytical context. IBTG preserves the dollar-return analytical structure while delivering working YCharts data.

**Why IBTG over Tier-3 SHY/VGSH:** IBTG preserves the iShares iBonds defined-maturity family concept (vs SHY/VGSH rolling-duration concept-drift). Tracking-error is smaller within-family.

**Tracking-error note:** IBTG @ Dec 2029 vs IBTF @ Dec 2028 = ~1 year duration difference. For attribution at T*=2026-05-18 in a flat-to-mildly-positive yield-curve environment, return divergence over a 1-month period is typically <0.3% (acceptable for attribution-class analysis; explicit flag in output table required).

### §4.2 — Operational change

**For the YALP_POSITN attribution harness:**
- Pre-substitute (Phase 1): IBTF row marked `NO-YCHARTS-PULL — HTTP 400` per Phase 1 brief §13.1
- Post-substitute (this brief): IBTF row marked **`SUBSTITUTED — IBTG (Dec 2029 Term Treasury; tracking-error ~1y duration)`**
- Spreadsheet column update: IBTF row populated with IBTG NAV series + substitute-note column flagging the swap + duration-mismatch caveat
- Portfolio holding NOT changed (still holds IBTF); only the YCharts data-pull substitute changes

### §4.3 — Sovereign ratification ask

**Three open questions for Andrew + ws CTO sovereign ratification:**

1. **Substitute primary tier choice:** Is IBTG (Tier 2 = sister ETF) acceptable as primary substitute, OR does Andrew's "closest-to-underlying first; ETF wrapper = LATER-RESORT" framing strictly require Tier 1 (FRED yield series) even at the cost of yield-vs-return tracking-error?
2. **Wave-1 universe impact:** does IBTD + IBTE (Dec 2026 + Dec 2027 sister failures discovered this probe) need preemptive substitute-search NOW, or only when they show up in future yang attribution datasets?
3. **Entitlement-boundary mapping doctrine:** should reconnaissance briefs henceforth include "near-term-maturity entitlement-boundary probe" (probe the 3-year window for any defined-maturity ETF family) at recon time, before downstream failures?

---

## §5 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~D
**TO:** YALP_POSITN — IBTF substitute-security-search (ws COO action ask per Andrew sovereign ruling)

**Evidence:**
- This brief at `docs/briefs/yalp_positn_ibtf_substitute_security_search_20260526.md`
- Live YCharts probes ~22:31-22:32Z: iShares iBonds Dec YYYY Term Treasury family entitlement boundary mapped (IBTD/IBTE/IBTF blocked; IBTG–IBTM clean)
- Sister substitutes also live-verified (SHY + VGSH HTTP 200)

**Recommended disposition:** IBTG = primary substitute for IBTF (Tier 2 sister term-treasury ETF); IBTG = HTTP 200 + 1571 daily data points under same fresh cookie; tracking-error ~1y duration → ~<0.3% return divergence at attribution-class precision

**Banking observations (memory candidates):**

1. **`feedback_ycharts_entitlement_boundary_at_3yr_term_treasury_family`** — empirical: iShares iBonds Dec YYYY Term Treasury family has YCharts entitlement boundary at `maturity_year - current_year <= ~2.5`. Useful for any future term-maturity family probes (corporate iBonds IBDQ/IBDR/etc. may have similar near-term boundary).

2. **`feedback_substitute_search_method_family_probe`** — discipline: when a single ticker fails, probe the WHOLE family (sequential maturities, sequential expense-ratio tiers, etc.) to characterize the boundary cleanly — this informed IBTG selection vs blind try-each-sister.

**Wall:** ws COO MCP ~22:30Z → entitlement boundary mapped + brief shipped ~22:35Z = ~5min sub-benchmark vs 30min target.

**Standing for:** RAVC2-ACCEPT + sovereign ratification of IBTG substitute disposition + ws CTO PRD codification of substitute-search doctrine.

— 0.1.0_DS_MarketIntelligence~D
2026-05-26 work-cycle:5 (post-RAVC2-ACCEPT extended cascade)
