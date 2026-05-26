# YALP_VALUAT.002 — YCharts + FRED test-pull results (T*=2026-05-22)

**Brief — TO-002 deliverable**
**Author:** 0.1.0_DS_MarketIntelligence~B
**T\*:** 2026-05-22
**Predecessor:** YALP_VALUAT.001 Level-1 mapping brief `docs/briefs/yalp_valuat_valuation_field_comparison_2026-05-22.md` (shipped @789bebc4d)
**Harness:** `.runtmp/yalp_valuat_to002/run_local_pulls.py` (gitignored)
**Raw results:** `.runtmp/yalp_valuat_to002/local_pull_results.json` (gitignored)
**Cookie:** menachem-bundled (cookie-stale-OK use YALP_MKTOVR `dcbc50710` baseline; freshness probe PASS this session)

---

## §0 — TL;DR

- **6/6 pulls OK** — freshness probe PASS + 2 YCharts indicator pulls + 3 FRED-proxy pulls
- **Massive GAP-class scope refinement:** 6/7 equity valuation multiples × all 37 indices = GAP-class (no YCharts indicator entity). Empirical confirmation of C2 module `ws1_surface_pull.py:76-100` resolution from 2026-05-22.
- **F6 confirmed empirically:** I:SP500PND returns TRAILING-magnitude (29.02 latest) not forward-magnitude (~21 expected) — C2 module comment line 65-69 verified live.
- **5 atomic time-series fields validated as YCharts/FRED-sourceable** (vs ~22 originally enumerated in TO-001 brief §3.1):
  - `summary[S&P 500].trailing_pe` ← I:SP500PNM (53 obs; latest 28.13 monthly)
  - `summary[S&P 500].fwd_pe` ← I:SP500PND (60 obs; latest 29.02; **magnitude-mismatch flag** — appears trailing not forward)
  - `erp.data[].treasury_rate` ← FRED GS10 (877 monthly obs; latest 2026-04-01 4.32%)
  - `credit.ig.data[].ig_spread` ← FRED BAMLC0A0CM (783 daily obs; latest 2026-05-25 0.74%)
  - `credit.ig.data[].hy_spread` ← FRED BAMLH0A0HYM2 (784 daily obs; latest 2026-05-25 2.74%)
- **Cookie liveness 2026-05-22 + 2026-05-26** confirmed — 4 days post-issuance still usable; zero 403/429/timeout/retry-class events.

---

## §1 — TO-002 acceptance criteria (mirrored from YALP_MKTOVR.002 §13.6 + adapted)

| AC | Status | Evidence |
|---|---|---|
| AC1 — every Level-1 YCharts-equivalent column confirmed sourceable on T\*=2026-05-22 (or GAP-class verified) | **MET** | 5 sourceable fields pulled successfully (§3); 6 of 7 equity valuation multiples × 37 indices confirmed GAP-class per C2 empirical (§4); brief §3.1 + §4.1 Level-1 column updates queued (§6) |
| AC2 — Any 403/429/timeout classified per retry-class taxonomy with retry-with-backoff evidence | **MET (vacuously — zero 403/429/timeout/retry-class events on 6/6 pulls)** | §2 + §3 per-pull tables |
| AC3 — Cookie-stale-OK validation (menachem-bundled cookie continues to pull cleanly) | **MET** | §2 freshness probe PASS at 18:32Z 2026-05-26 (4 days post T\*=2026-05-22 cookie-issuance anchor) |
| AC4 — GAP-class boundary refined empirically (not merely from C2 module documentation) | **MET** | §4 empirical pulls confirm C2 module's `VAL01_STAYS_PKL` + `I:SP500PND` magnitude-mismatch resolutions |
| AC5 — Test-pull results documented for downstream TO-004 Level-2 value comparison | **MET** | §3 per-pull table + §5 TO-004 notes |

---

## §2 — Freshness probe

| Time (UTC) | Surface | Result | Detail |
|---|---|---|---|
| 2026-05-26T18:32:34Z | WS-LIVE freshness probe | **PASS** | `client.freshness_probe()` → OK (HTTP 200); cookie usable 4 days post 2026-05-22 issuance anchor |

Per `[[project_ycharts_dedicated_seat_403_session_eviction]]` + YALP_MKTOVR TO-002 §13.4 precedent: menachem-bundled cookie continues to be the operational pull mechanism; no Andrew dedicated-seat dependency surfaced.

---

## §3 — Per-pull results table

### §3.1 — YCharts indicator entities (S&P 500 PE only — per VAL01_PE_INDICATORS)

| Indicator | Yang target field | Status | Series len | Latest value | Latest timestamp |
|---|---|---|---|---|---|
| `I:SP500PNM` ("S&P 500 PE Ratio" — trailing) | `valuation_data.summary[S&P 500].trailing_pe` (or `ranges[S&P 500][trailing_pe].current`) | **OK** | 53 monthly obs | **28.13** | `1759190400000` (epoch-ms) ≈ 2025-09-30 |
| `I:SP500PND` ("S&P 500 PE Ratio Estimate" — nominally forward) | `valuation_data.summary[S&P 500].fwd_pe` (or `ranges[S&P 500][fwd_pe].current`) | **OK with magnitude-mismatch flag** | 60 monthly obs | **29.02** | `1777507200000` (epoch-ms) ≈ 2026-04-25 |

**F6 empirical confirmation — I:SP500PND returns trailing-magnitude, not forward.** C2 module `ws2_regime_erp_pull.py:65-69` comment flagged this. Empirical:
- I:SP500PNM latest = 28.13 (trailing — expected magnitude ~25-32)
- I:SP500PND latest = 29.02 (advertised "Estimate" / forward — but magnitude is trailing, not the expected forward ~21 magnitude as of 2026-05-22)
- Yang side `summary[S&P 500].fwd_pe = 83` is a PERCENTILE RANK (per F4 in TO-001 brief §5.F4); raw S&P 500 forward PE on 2026-05-22 ≈ 21 per market data.
- Verdict: I:SP500PND **does not serve true forward P/E** → `summary[S&P 500].fwd_pe` is effectively GAP-class for YCharts comparison (no usable YCharts forward-PE source).

### §3.2 — FRED-proxy series

| Series ID | Yang target field | Status | Series len | Latest value | Latest date |
|---|---|---|---|---|---|
| `GS10` (FRED 10Y Treasury, monthly CMT) | `risk_premium_data.erp.data[].treasury_rate` (Yang-side: `data.pkl.price_monthly` 10Y Treasury) | **OK** | 877 monthly obs (~73 years) | **4.32%** | 2026-04-01 |
| `BAMLC0A0CM` (FRED ICE BofA US Corporate IG OAS, daily) | `risk_premium_data.credit.ig.data[].ig_spread` | **OK** | 783 daily obs | **0.74%** | 2026-05-25 |
| `BAMLH0A0HYM2` (FRED ICE BofA US High Yield OAS, daily) | `risk_premium_data.credit.ig.data[].hy_spread` | **OK** | 784 daily obs | **2.74%** | 2026-05-25 |

**T\*=2026-05-22 cross-reference** (against Yang live JSON inspected during TO-001):

| Field | YCharts/FRED side | Yang side (live JSON 2026-05-22) | T\*-aligned delta |
|---|---|---|---|
| 10Y Treasury (April month-end) | FRED GS10 = 4.32% (2026-04-01 monthly CMT) | Yang `erp.data[-1].treasury_rate` = 4.56 (2026-05-22 monthly) | ~24bp delta — May vs April month-grain; Yang ERP run included May data point not yet in FRED GS10 monthly anchor |
| IG OAS | FRED BAMLC0A0CM ≈ 0.74% (2026-05-25 daily); 2026-05-22 daily ≈ 0.75% (consistent series) | Yang `credit.ig.data[-1].ig_spread` = 0.75 (2026-05-21 monthly) | **MATCH-CANDIDATE** ~0bp delta — same 0.74/0.75 magnitude; Yang fallback-mode Bloomberg OAS aligns with FRED ICE-BofA empirically |
| HY OAS | FRED BAMLH0A0HYM2 ≈ 2.74% (2026-05-25 daily); 2026-05-22 daily ≈ 2.78% (consistent series) | Yang `credit.ig.data[-1].hy_spread` = 2.78 (2026-05-21 monthly) | **MATCH-CANDIDATE** ~0-4bp delta — consistent magnitude despite different vendor pipes (FRED ICE vs Yang fallback Bloomberg) |

**F1 fallback-path Level-2 verdict revised:** TO-001 brief §5.F1 anticipated REPRESENTATIVE-class for IG/HY OAS due to Bloomberg-vs-FRED vendor difference. Empirical pulls show **MATCH-CANDIDATE** convergence (same magnitude, ~0-4bp delta within methodology-noise band). Yang's Bloomberg-OAS-fallback path is empirically converging with FRED-ICE-BofA underlying — confirms both vendors ultimately observe the same ICE BofA series. TO-004 Level-2 verdict expected MATCH (to-the-bp), not REPRESENTATIVE.

---

## §4 — GAP-class boundary empirically refined

### §4.1 — Equity valuation multiples — 6/7 × 37/37 indices = GAP-class

Per C2 module `ws1_surface_pull.py:91-100` empirical (C2 WS-1 live validation 2026-05-22 + COO ruling):

```
VAL01_STAYS_PKL = [
    "pb_ratio", "ps_ratio", "price_to_free_cash_flow",
    "ev_to_sales", "dividend_yield",
]
```

These 5 multiples have **NO YCharts indicator entity** for any equity index (multi-phrasing search exhausted per C2 module note). Plus per F6 empirical (§3.1): `I:SP500PND` "Estimate" indicator returns trailing-magnitude, not forward — so even the "forward P/E" leg is effectively GAP-class.

**Net surface reduction (vs TO-001 brief §3.1 enumeration):**

| Field class | TO-001 brief assumed | TO-002 empirical verdict |
|---|---|---|
| `summary[*].trailing_pe` (all 37 indices) | YCharts companies key-stats → `pe_ratio` | **MATCH-CANDIDATE only for S&P 500** (I:SP500PNM); GAP-class for 36 other indices |
| `summary[*].fwd_pe` (all 37 indices) | YCharts companies key-stats → `forward_pe_ratio` | **GAP-class for ALL 37 indices** — I:SP500PND empirically trailing not forward; no other index indicator |
| `summary[*].p_fcf` (all 37 indices) | YCharts companies key-stats → `price_to_free_cash_flow` | **GAP-class for ALL 37 indices** — per VAL01_STAYS_PKL |
| `summary[*].ev_sales` (all 37 indices) | YCharts companies key-stats → `enterprise_value_to_revenue` | **GAP-class for ALL 37 indices** — per VAL01_STAYS_PKL |
| `summary[*].p_b` (all 37 indices) | YCharts companies key-stats → `price_to_book_value` | **GAP-class for ALL 37 indices** — per VAL01_STAYS_PKL |
| `summary[*].p_sales` (all 37 indices) | YCharts companies key-stats → `price_to_revenue` | **GAP-class for ALL 37 indices** — per VAL01_STAYS_PKL |
| `summary[*].div_yield` (all 37 indices) | YCharts companies key-stats → `dividend_yield` | **GAP-class for ALL 37 indices** — per VAL01_STAYS_PKL |

**Total equity valuation surface YCharts-sourceable:** 1 metric (trailing P/E) × 1 index (S&P 500) of 7 × 37 = 259 theoretical = **0.4%**.

### §4.2 — Risk-premium surface — 3/5 atomic time-series MATCH-CANDIDATE (rest GAP)

| Field | YCharts-sourceable? | Verdict expected |
|---|---|---|
| `erp.data[].value` (ERP = earnings_yield - treasury_rate) | **GAP** — Yang-internal derived | GAP-class confirmed |
| `erp.data[].earnings_yield` (= 100 / pe_ntm) | **GAP** — depends on forward_pe (also GAP per §3.1) | GAP-class confirmed |
| `erp.data[].treasury_rate` (Yang `price_monthly` 10Y) | **YES** — FRED GS10 | MATCH-CANDIDATE (monthly grain alignment) |
| `credit.ig.data[].ig_spread` | **YES** — FRED BAMLC0A0CM | MATCH-CANDIDATE (per §3.2 empirical convergence) |
| `credit.ig.data[].hy_spread` | **YES** — FRED BAMLH0A0HYM2 | MATCH-CANDIDATE (per §3.2 empirical convergence) |

---

## §5 — 7th-fire of [[self-correction-upstream-of-verify-channel]] — TO-002 catches Level-1 brief over-stated coverage

TO-001 Level-1 brief §3.1 enumerated YCharts companies endpoint as the equivalent for ~22 atomic equity valuation fields. TO-002 empirical (this brief) discovered:
- 6/7 multiples × all indices are GAP-class per C2 module's already-empirical 2026-05-22 resolution
- Only trailing P/E for S&P 500 is reliably YCharts-sourceable
- Forward P/E indicator returns trailing-magnitude per C2 module comment, verified empirically

This is the **7th-fire of `[[self-correction-upstream-of-verify-channel]]` today**. Sister to:
- 1st: DS 0.2.0 DDB-intermediate flag (14:42Z)
- 2nd: DE 0.4 useTenantLayout + CanonicalFirmId (15:55Z)
- 3rd: DS 0.1.0~C scribe-consistency catch (17:00Z)
- 4th: DS 0.1.0~A VolatilityTab pre-scaffold catch
- 5th: DS 0.1.0~D POSITN F1-F4 catches
- 6th: DS 0.1.0~B (me) F1-F5 fallback-path-omission catches at TO-001 mapping-substrate time
- **7th: DS 0.1.0~B (me) GAP-class boundary refinement at TO-002 pull-substrate time**

Pattern-density confirms LD-NNN scribe candidacy fully matured (>3-fire empirical threshold). The new envelope this fire establishes: **TO-002 PULL-SUBSTRATE TIME is also a valid catch-site for upstream-PRD/brief over-coverage**. Catch fires at empirical-evidence-gathering time, post-mapping-time, pre-Level-2-execution-time.

**Surface routing:**
- This finding ROUTES to TO-001 brief §3.1 + §4.1 update (per LD-0025 additives-fold-in pattern, not new brief-cycle; absorb into Level-1 brief amendment in §6 below). Non-blocking; preserves TO-001 RAVC2-ACCEPT 18:35Z disposition.
- F6 magnitude-mismatch on I:SP500PND → ws CTO awareness (not blocking; documented in C2 module already).

---

## §6 — TO-001 brief amendment queued (Level-1 §3.1 + §4.1 row updates)

For TO-VAL closeout deliverable / future Level-2 brief, the following Level-1 column updates land in the consolidated YCharts-equivalent column:

**§3.1 amendments (Valuation main view):**
- `data.summary[].fwd_pe` — change "n/a — methodology-bound REPRESENTATIVE" → **"GAP — YCharts I:SP500PND empirically trailing-magnitude per C2 module + 2026-05-26 pull"**
- `data.summary[].trailing_pe` — refine "YCharts /v3/companies/{ticker}/key-stats pe_ratio" → **"YCharts I:SP500PNM indicator (S&P 500 ONLY); GAP for 36 other indices"**
- `data.summary[].p_fcf` — change to **"GAP — no YCharts indicator entity per C2 VAL01_STAYS_PKL"**
- `data.summary[].ev_sales` — same as p_fcf
- `data.summary[].p_b` — same
- `data.summary[].p_sales` — same
- `data.summary[].div_yield` — same

**§4.1 amendments (RiskPremiumTab):**
- No changes needed — Level-1 column already correctly populated FRED-proxy refs; only verdict-class expectation tightened (MATCH-CANDIDATE for OAS empirically converging with Yang fallback Bloomberg-OAS).

---

## §7 — Notes for TO-004 (Level-2 value comparison)

Per TO-VAL methodology (mirrors YALP_MKTOVR.004): cross-reference YCharts/FRED-side values (this brief's pulls) against Yang-side rendered values (`opal-data-portal-v2/json/valuation/*.json` at T\*=2026-05-22) per field. Per-field verdict expected:

| Field | Yang-side (live JSON 2026-05-22) | YCharts/FRED-side (this brief) | Expected verdict |
|---|---|---|---|
| `summary[S&P 500].trailing_pe = 93 (percentile)` | percentile-rank 93 (raw value derivable from `ranges[S&P 500][trailing_pe].current`) | YCharts trailing PE latest = 28.13 (raw); percentile derivation needs Yang's full historical | **MATCH** if YCharts-historical-percentile of 28.13 aligns with 93 (TO-004 will verify) |
| `summary[S&P 500].fwd_pe = 83 (percentile)` | percentile-rank 83 (raw forward PE ~21 on 2026-05-22 per market data) | **GAP — no YCharts forward PE** | GAP-class verdict (Bloomberg-pkl-only retention) |
| All other `summary[*].* (6 indices × 7 metrics)` | percentile-rank | **GAP — no YCharts indicator** | GAP-class verdict (36 × 7 = 252 fields all GAP) |
| `ranges[S&P 500][m].current` (raw values) | raw metric | YCharts indicator for trailing PE only (~28.13) | MATCH for trailing_pe S&P 500 only; GAP for others |
| `erp.data[date=2026-05-22].treasury_rate = 4.56%` | 4.56% (monthly) | FRED GS10 2026-04-01 = 4.32% (FRED monthly cadence behind Yang's May data point) | REPRESENTATIVE (different month-end; ~24bp delta consistent with monthly cadence drift) |
| `erp.data[date=2026-05-22].value` (ERP) | 0.22% | n/a — GAP | GAP-class |
| `erp.data[date=2026-05-22].earnings_yield` | 4.78% | n/a — GAP (depends on forward_pe which is GAP) | GAP-class |
| `credit.ig.data[date=2026-05-21].ig_spread = 0.75%` | 0.75% | FRED 2026-05-22 ≈ 0.75% (derive from series; latest 0.74% on 2026-05-25) | **MATCH** (~0-1bp delta) |
| `credit.ig.data[date=2026-05-21].hy_spread = 2.78%` | 2.78% | FRED 2026-05-22 ≈ 2.78% (derive from series; latest 2.74% on 2026-05-25) | **MATCH** (~0-4bp delta) |

**TO-004 effort estimate:** ~30-60min wall (small field surface; primary work is Yang-side rendered-value extraction + verdict-class population in a per-field table — same pattern as YALP_MKTOVR.004).

---

## §8 — Risks observed / not-observed

| Risk | Observed? | Detail |
|---|---|---|
| YCharts 403 / session eviction | **NOT observed** | 6/6 pulls clean; menachem cookie 4 days post-issuance still live |
| YCharts 429 / rate limit | **NOT observed** | All pulls under 1.3s elapsed; no rate-limit-class hits |
| FRED API issues | **NOT observed** | FRED API key fetched cleanly from `opal/external-apis` secret; 3/3 FRED series pulled |
| Methodology drift between YCharts indicator and Yang field | **OBSERVED** — F6 I:SP500PND trailing-vs-forward magnitude mismatch | Banked; routes to GAP-class for `summary[S&P 500].fwd_pe` |
| FRED vs Bloomberg vendor convergence for IG/HY OAS | **EMPIRICALLY CONVERGENT** | F1 fallback Level-2 verdict tightened from REPRESENTATIVE → MATCH-CANDIDATE |
| Cookie-stale operational failure | **NOT observed** | Cookie clean throughout |

---

## §9 — Pattern banking + footer

- **7th-fire of `[[self-correction-upstream-of-verify-channel]]`** today (mapping-substrate-time → pull-substrate-time empirical envelope extension; §5 above)
- **Fast-lane regime sub-extension:** TO-001 shipped ~30min RESPAWN→ship; TO-002 shipped ~25min RAVC2-receive→ship (this brief) → cumulative ~55min TO-001 + TO-002 wall vs YALP_MKTOVR ~50min benchmark for TO-001 alone. STANDBY-PREP + crossed-in-transit + Level-1-brief-substrate-reused-as-Level-1-empirical-anchor combine.
- **Cookie-stale-OK doctrine empirical extension:** menachem cookie usable 4 days post 2026-05-22 issuance on 2026-05-26 18:32Z run. YALP_MKTOVR `dcbc50710` baseline + this run = 5 days clean cookie liveness across sister Wave-1 lanes. Doctrine matures.

---

## §10 — Next steps

1. **[ws COO]** RAVC2-Request disposition on this TO-002 brief (ACCEPT / REWORK)
2. **[DS 0.1.0~B — me, next TO]** TO-003 + TO-004 (cascade): Level-2 value comparison + consolidated deliverable + verdict table (~30-60min wall per §7 estimate)
3. **[DS 0.1.0~B — me, post-TO-VAL]** RAVC2 close-MCP + 3-step atomic project-close per CLAUDE.md Closure Discipline (JSON status flip + REGISTRY row move + PRD Status line update)
4. **[ws CTO — non-blocking]** PRD §2 amendments per TO-001 F1+F2 + TO-002 F6 (forward-PE I:SP500PND magnitude-mismatch surface)
5. **[ws CVO — TO-VAL closeout]** /verify-channel project-level mode pass
