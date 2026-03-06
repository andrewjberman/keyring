# ADVI_NNAVAR: Phase 1 Results Through Phase 3 Structural Scoping — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 11:15
**End Time:** 17:30

## Objective

Following the Phase 1 gap decomposition results returned by DT (ADVI_NNAVAR.002-DT complete),
analyze findings, design and implement the Phase 2 cap tuning diagnostic, analyze those results,
ideate on structural explanations for the residual gap, and implement the Phase 3 structural
diagnostic suite. This log covers the full analytical arc from Phase 1 result interpretation
through Phase 3 script delivery.

---

## Work Completed

### 1. Phase 1 Gap Decomposition Results — Analysis

DT returned results for all 6 suites of `diag_nnavar_gap_decomposition.py` (commit `61fab0a9`).
Key findings from the 14-variant result table:

**Baseline:** pearson_r=0.175, sign_agr=10/13, total_gap=-$119.8M (gold parquet, production caps)

**Dominant finding — velocity cap:**

| Variant | pearson_r | sign_agr | total_gap |
|---------|-----------|----------|-----------|
| cap_event_only (no AUA, no vel) | 0.128 | 10/13 | -$484.1M |
| cap_event_plus_aua (no vel) | **0.203** | **12/13** | -$117.0M |
| cap_event_plus_aua_plus_velocity | -0.219 | 13/13 | +$34.2M |

Removing the velocity cap while keeping the AUA cap moves pearson from 0.175 → 0.203 and
sign agreement from 10/13 → 12/13. Adding the velocity cap back (with my diagnostic's
simplified implementation) flipped to r=-0.219, which indicated an implementation issue.

**Exclusions, dedup, timing, coverage** — all suites collapsed to +$34.2M / r=-0.219
because my velocity cap implementation (integer-count rolling + zero-out) was too aggressive,
dominating all other signals. Could not cleanly read those levers.

**Root cause of implementation divergence:** Read production script 05 (lines 566–622) and
confirmed the production velocity cap uses:
- DatetimeIndex calendar-day rolling window (`f'{VELOCITY_WINDOW_DAYS}D'`)
- Budget room-clipping: `room = (allowed - trailing_out_excl).clip(min=0)`, then
  `daily_outflow = min(daily_outflow, room)` — partial suppression, not zeroing

My Phase 1 diagnostic used integer-count rolling and zeroed the entire outflow when budget
exceeded, producing over-suppression of ~$154M.

**Decision:** Write a corrected Phase 2 cap tuning script with production-accurate velocity cap
before any production parameter recommendation.

---

### 2. Phase 2 Cap Tuning Script — Implementation

**Script:** `data/black_diamond/scripts/diagnostics/diag_nnavar_cap_tuning.py`
**Commits:** `1d9b2e8d` (script), `e6e6cdd1` (DT brief)

Three suites:
- **`aua`:** AUA threshold isolation (velocity cap OFF) — 6 variants: aua_none, t0p50, t1p00
  (prod), t1p50, t2p00, t3p00
- **`vel`:** Velocity cap isolation (AUA at 1.0×, production) — 10 variants: vel_none, then
  all combinations of window {60, 90, 120} × threshold {1.0, 1.5, 2.0}
- **`combo`:** Cross-product AUA {1.0, 1.5, 2.0} × velocity {none, w90_t1p50, w90_t2p00,
  w120_t1p50, w120_t2p00} = 15 variants

Key architectural corrections from Phase 1:
- Production-accurate velocity cap: DatetimeIndex calendar-day rolling + room-budget clipping,
  matching script 05:566–622 exactly
- Flows separated into `daily_inflow` / `daily_outflow` (both positive) matching script 05:283–319
- Shared `build_flow_spine_base()`: all 31 variants share one transaction load and one
  preprocessing pass; only cap parameters vary per variant

**DT brief:** `docs/briefs/devops-brief-nnavar-cap-tuning-ec2-run.md`
Specified suite-per-invocation, SSM params file pattern, runtime estimates (~25-40 min / aua,
~50-80 min / vel, ~60-90 min / combo), sequential execution default with parallel option noted.

---

### 3. Phase 2 Results — Analysis

DT returned aua + vel + combo results (all 31 variants, commit `207416d1` from DT).

**AUA suite (velocity OFF):**

| Variant | AUA thresh | pearson_r | sign_agr | total_gap |
|---------|-----------|-----------|----------|-----------|
| aua_none | off | 0.134 | 9/13 | -$540.4M |
| aua_t0p50 | 0.5× | 0.109 | 13/13 | -$82.3M |
| aua_t1p00 (prod) | 1.0× | 0.253 | 10/13 | -$168.6M |
| **aua_t1p50** | **1.5×** | **0.263** | **9/13** | -$184.1M |
| aua_t2p00 | 2.0× | 0.261 | 9/13 | -$189.2M |
| aua_t3p00 | 3.0× | 0.261 | 9/13 | -$196.2M |

Finding: 1.5× is the pearson-optimal AUA threshold but costs sign agreement (9/13 vs 10/13).
Diminishing returns above 1.5×. aua_none causes data-quality collapse (-$540.4M), confirming
the AUA cap is doing essential work on BD phantom withdrawals.

**Velocity suite (AUA fixed at 1.0×):**

| Variant | Window | Thresh | pearson_r | sign_agr | total_gap |
|---------|--------|--------|-----------|----------|-----------|
| vel_none | — | — | 0.253 | 10/13 | -$168.6M |
| vel_w90_t1p00 (prod) | 90d | 1.0× | 0.157 | 11/13 | -$124.7M |
| vel_w120_t1p00 | 120d | 1.0× | 0.111 | 13/13 | -$107.1M |
| vel_w60_t1p50 | 60d | 1.5× | 0.254 | 10/13 | -$163.0M |
| vel_w90_t1p50 | 90d | 1.5× | 0.251 | 10/13 | -$160.6M |
| **vel_w120_t2p00** | **120d** | **2.0×** | **0.260** | **10/13** | **-$163.0M** |

Key tension confirmed: tight threshold (1.0×) maximizes gap closure and sign agreement but
destroys pearson. At 2.0× the cap is nearly inert vs vel_none (+0.007 pearson gain over
vel_none). Production velocity cap at 90d/1.0× is demonstrably too tight — suppresses $44M
of real NNA and drops pearson from 0.253 to 0.157.

**Combo suite (15 variants):**

| Variant | AUA | Vel | pearson_r | sign_agr | total_gap |
|---------|-----|-----|-----------|----------|-----------|
| **comb_aua1p5_w120t2p00** | 1.5× | 120d/2.0× | **0.271** | **10/13** | -$174.9M |
| comb_aua2p0_w120t2p00 | 2.0× | 120d/2.0× | 0.269 | 9/13 | -$177.4M |
| comb_aua1p5_w90t2p00 | 1.5× | 90d/2.0× | 0.264 | 10/13 | -$176.8M |
| comb_aua1p5_velnone | 1.5× | off | 0.263 | 9/13 | -$184.1M |
| comb_aua1p0_w120t2p00 | 1.0× | 120d/2.0× | 0.260 | 10/13 | -$163.0M |

**Ceiling across all 31 variants: pearson_r = 0.271.** PRD target is r≥0.50.

Best production-compatible config for eventual deployment: `aua_t1p50 + vel_w120_t2p00`
(r=0.271, sign_agr=10/13, gap=-$174.9M). The sign agreement parity with production (10/13)
is maintained while gaining +0.096 in pearson. Not integrated yet — awaiting structural
diagnostic results before scheduling the rebuild to minimize rebuild count.

**Decision:** Cap tuning has a hard ceiling far below PRD targets. The gap is structural.
Three hypotheses generated for Phase 3 investigation.

---

### 4. Phase 3 Structural Hypothesis Generation — Research

Reviewed 6 archive documents to understand what the silver transaction data actually contains
vs what production script 05 currently uses:

| Document | Finding |
|----------|---------|
| `data/black_diamond/archive/docs/FIELD_MAPPINGS.md` | Confirms `external_flow` column: values Contribution / Withdrawal / blank. Also `Settle Date` field maps to `settle_date`. BI export has `Net Additions excl Fees`, `Contributions excl Acct Transfers`. |
| `data/black_diamond/archive/docs/NNA_CALCULATION.md` | Explicitly states: "Transfer In with External Flow = Contribution → Include in NNA" vs "Internal transfers → May double-count; verify External Flow field" |
| `data/black_diamond/archive/BD_TRANSACTIONS_DATA_SUMMARY.md` | Original silver NNA_INFLOW_TYPES included `Wire In` and `Transfer` plus `external_flow CONTAINS 'In'` — this logic was later dropped when switching to partitioned silver |
| `data/black_diamond/scripts/silver/merge-daily-incremental.py` | Line 168 DATE_COLS confirms `settle_date` IS parsed and preserved in silver/transactions/ partitions |
| `data/black_diamond/archive/docs/SILVER_LAYER_ARCHITECTURE.md` | Confirms `External Flow` listed as key field for transaction NNA classification alongside `Market Value` |
| `data/black_diamond/scripts/gold/05_build_client_performance.py` | Confirmed: production script uses neither `external_flow` nor `settle_date`. NNA classified solely on transaction_type. |

**Three confirmed structural hypotheses:**

1. **`external_flow` filter** — `silver/transactions/` partitions have an `external_flow` column
   (values: Contribution / Withdrawal / blank) that BD uses to distinguish external client money
   movements from internal account-to-account transfers. Production script 05 ignores this column
   and includes ALL Transfer In/Out regardless. Internal transfers counted as NNA inflate both
   inflows and outflows incorrectly.

2. **Settlement date timing** — `settle_date` is present in silver partitions but production
   uses `trade_date` exclusively. Schwab's institutional NNA reporting almost certainly uses
   settlement date. Month-boundary crossings (T+2 to T+5 for large institutional transfers)
   could explain sign disagreements in specific months.

3. **BI cross-validation** — BD's own BI export pre-computes `Net Additions excl Fees` and
   `Contributions excl Acct Transfers`. If these fields exist in S3, direct comparison would
   quantify the definitional gap between our transaction-derived NNA and BD's own calculation.

---

### 5. Phase 3 Structural Script — Implementation

**Script:** `data/black_diamond/scripts/diagnostics/diag_nnavar_structural.py`
**Commits:** `defdf684` (script, 963 lines), `5e24913e` (DT brief)

Four suites in one script:

**Suite `schema` (~5-10 min, fast, gates all others):**
- Audit A: Full transaction type taxonomy — every type, dollar volume, sign distribution
- Audit B: `external_flow` distribution by flow type — what fraction of Transfer In/Out have
  external_flow=Contribution vs blank vs null
- Audit C: `settle_date` vs `trade_date` gap — cross-month boundary counts by Schwab month
- Audit D: Account coverage gaps — accounts active in Schwab window but absent from dimension
- Audit E: Partition completeness — partition count per month, coverage flags for gaps
- Outputs `schema_summary.json` with gating flags (`external_flow_present`, `settle_date_present`)

**Suite `external_flow` (~20-30 min):**
Four variants using production caps (aua_t1p00, vel_w90_t1p00) to isolate the effect:
- `ef_all_transfers` — baseline (current production behavior)
- `ef_contribution_only` — Transfer In/Out only if external_flow=Contribution/Withdrawal;
  Cash Deposit/Withdrawal always included (BD's intended NNA filter)
- `ef_nonempty` — Transfer In/Out where external_flow is not null/blank
- `ef_no_transfers` — Cash Deposit/Withdrawal only; isolation of transfer-type contribution

**Suite `settlement` (~20-25 min):**
Three variants using ef_all_transfers + production caps, varying date column for monthly bucketing:
- `settle_trade_date` — current production (bucket by trade_date)
- `settle_settle_date` — use settle_date where non-null, fall back to trade_date
- `settle_settle_strict` — only rows with non-null settle_date, bucketed by settle_date

**Suite `bi_crossval` (~5-15 min, non-blocking):**
Searches 4 S3 paths for BI parquet data. If found, cross-references BD's pre-computed monthly
NNA against our gold and Schwab for all 13 months. If not found, outputs `not_available.json`
cleanly without error.

**Key architectural decisions:**
- `base_dedup_and_exclude()` preserves ALL columns including `external_flow` and `settle_date`
  — nothing dropped before the suite-specific filter logic runs
- `classify_flows()` accepts `ef_mode` parameter determining which rows become inflows/outflows
- `build_flow_spine()` accepts `date_col` parameter for settlement suite (switches trade_date →
  settle_date or effective_date throughout the aggregation and gold spine join)
- Self-gating: if `external_flow` / `settle_date` absent from data, suites skip with a JSON
  explaining the reason — no crash, no false results

**DT brief:** `docs/briefs/devops-brief-nnavar-structural-ec2-run.md`
Execution order: schema first → read stdout → share gating flags → external_flow → settlement
(parallel if RAM allows, sequential by default) → bi_crossval.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Write Phase 2 cap tuning instead of immediately recommending production changes | Phase 1 velocity cap implementation diverged from production; needed production-accurate implementation before any parameter recommendation |
| Use DatetimeIndex calendar-day rolling for velocity cap | Required to match script 05:566-622 exactly; integer-count rolling gives materially different results on sparse relationship-day data |
| best combo for production deployment: aua_t1p50 + vel_w120_t2p00 | r=0.271 (vs current 0.175), sign_agr=10/13 (maintained), gap=-$174.9M. Only candidate that beats production on pearson without losing sign agreement |
| Do not deploy cap changes yet | Wait for structural diagnostic results — if external_flow fix also improves r, a single gold rebuild captures both changes, avoiding two full rebuilds (each ~145 min) |
| Phase 3 as a single script (4 suites) instead of 4 scripts | Consistent with established diagnostic framework; shared preprocessing; single S3 upload |
| schema suite as gating check before external_flow / settlement | Cannot know if external_flow / settle_date columns are populated in live silver partitions without checking first; documentation confirms presence but not null rates |
| bi_crossval as non-blocking | BI data location in S3 is uncertain; failing fast with a not_available.json is better than a blocking error |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Cap tuning EC2 execution | `docs/briefs/devops-brief-nnavar-cap-tuning-ec2-run.md` | 0.4.0_DT_ClientPlatform |
| Structural diagnostics EC2 execution | `docs/briefs/devops-brief-nnavar-structural-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py` | Phase 1 — 6-suite gap decomposition (suites 0-5) | Yes — `61fab0a9` |
| `docs/briefs/devops-brief-nnavar-gap-decomposition-ec2-run.md` | DT brief for Phase 1 EC2 run | Yes — `e093c2c9` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_NNAVAR.001-DS.write-gap-decomposition-script.md` | Status: pending → complete | Yes — `64cb0913` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-06/nnavar_gap_decomposition_script.md` | Phase 1 session log | Yes — `64cb0913` |
| `data/black_diamond/scripts/diagnostics/diag_nnavar_cap_tuning.py` | Phase 2 — 31-variant cap tuning (aua / vel / combo suites) | Yes — `1d9b2e8d` |
| `docs/briefs/devops-brief-nnavar-cap-tuning-ec2-run.md` | DT brief for Phase 2 EC2 run | Yes — `e6e6cdd1` |
| `data/black_diamond/scripts/diagnostics/diag_nnavar_structural.py` | Phase 3 — structural diagnostics (schema / external_flow / settlement / bi_crossval) | Yes — `defdf684` |
| `docs/briefs/devops-brief-nnavar-structural-ec2-run.md` | DT brief for Phase 3 EC2 run | Yes — `5e24913e` |

---

## Blockers

None. Phase 3 script and brief are committed. DT is unblocked to run `schema` suite.

---

## Current State

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Three diagnostic scripts committed across three phases of ADVI_NNAVAR investigation. Phase 1
(`diag_nnavar_gap_decomposition.py`, `61fab0a9`) ran on EC2 and confirmed velocity cap as the
dominant lever but exposed a velocity cap implementation divergence. Phase 2
(`diag_nnavar_cap_tuning.py`, `1d9b2e8d`) ran with production-accurate velocity cap and
established the hard ceiling at r=0.271 across 31 variants; best config for production is
aua_t1p50 + vel_w120_t2p00. Phase 3 (`diag_nnavar_structural.py`, `defdf684`) is committed and
ready for DT to run. DT runs `schema` suite first (~5-10 min), shares gating flags
(`external_flow_present`, `settle_date_present`) with DS, then proceeds to `external_flow` and
`settlement` suites. The `bi_crossval` suite is non-blocking and can run at any time.

**State of production changes:**
- Cap tuning params (aua_t1p50 + vel_w120_t2p00): validated, NOT yet integrated — awaiting
  structural diagnostic results to bundle into a single gold rebuild
- ACAT integration (+$45.98M): validated, NOT integrated — awaiting CEO go/no-go
- JNL/sweep canonical fix: committed (`9bfb289b` + `b4f2d7a7`), NOT rebuilt — same gate

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Run `schema` suite** per
   `docs/briefs/devops-brief-nnavar-structural-ec2-run.md` — share `schema_summary.json` and
   stdout with DS before proceeding

2. **[0.4.0_DT_ClientPlatform] Run `external_flow` and `settlement` suites** (sequential
   unless RAM allows parallel) — share summary.csv for each with DS/COO

3. **[0.4.0_DT_ClientPlatform] Run `bi_crossval` suite** — share `comparison.csv` or
   `not_available.json`

4. **[DS — this agent] Analyze Phase 3 results** — interpret external_flow and settlement
   suites against the 7-metric grid; determine whether either vector clears the materiality
   threshold (>0.05 pearson improvement) that would warrant a production change

5. **[2.0.0_SA_COO] Production rebuild decision** — after Phase 3 results: authorize a
   single gold rebuild bundling the confirmed structural fixes (cap tuning + external_flow
   filter if confirmed + ACAT if CEO go/no-go received + canonical fix). One rebuild covers
   all pending improvements.

**Files to touch next (DS):**
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-06/` — Phase 3 results analysis
  log (after DT returns results)

**Do NOT:**
- Deploy any cap parameter change to production script 05 before Phase 3 results are analyzed
- Run Phase 3 suites out of order — `schema` must complete first and gate the others
- Push any commits (DT handles all pushes)
- Modify production gold scripts (`05_build_client_performance.py`) without COO authorization
  of a rebuild window
