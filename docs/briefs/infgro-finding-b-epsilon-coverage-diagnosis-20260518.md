# INFGRO Finding B — Epsilon-Coverage Diagnosis Brief

**TO:** ADVI_INFGRO.008 (dsc-infc02-epsilon-coverage-diagnosis)
**Author:** 0.4.0_DS_ClientPlatform (DS~C)
**Date:** 2026-05-18
**Status:** Phase 0 diagnosis COMPLETE — escalation to CTO for the reconciliation-method ruling
**Scope:** Read-only diagnosis. No script modified.

---

## TL;DR

Finding B (firm_epsilon_$ = 71.6% of the AUA-growth decomposition) is **not** a
coverage gap and **not** staleness. Candidates (i) and (ii) are ruled OUT with
evidence. The root cause is candidate (iii) — a grain/units error — and it is
precisely characterized:

> **`silver/performance_dim.twr_factor_period` is an inception-to-date
> ANNUALIZED TWR rate (`1 + annualized_return`), NOT a cumulative-growth factor.
> `INF_C_02._build_daily_factor_table` treats it as a cumulative-growth factor
> and takes consecutive ratios (`f_curr / f_prior`) as per-period returns. The
> ratio of two consecutive annualized rates is ~1.0, so `return_pct_twr` and
> `return_$` come out ~6-10x too small; `epsilon_$` absorbs the unexplained
> ~90% of real market AUA movement.**

This is the **shared upstream root** the CTO ruling (PRD section 8.4) predicted:
"the two can only share a root upstream in INF_C_02 ... if INF_C_02's per-row
decomposition is itself driven by a mis-scaled per-row return." It is. The same
defect understates Finding A's `*_return_pct_twr` in absolute scale (INFGRO.007's
aggregation fix is correct but sits on a ~6x-understated input).

The TO's A/B/C reconciliation menu is coverage-framed and does not fit the
diagnosed root. A corrected option set (reconstruct-from-annualized vs
obtain-a-better-Orion-source) is in section 6 — the choice is the CTO escalation.

---

## 1 — How INF_C_02 derives return_$ and epsilon_$ (code trace)

`INF_C_02.client_performance.py`, household grain (one row per household_id,date):

- `total_aua`, `aua_change`, `net_nna` — aggregated (`.sum()`) from the
  account-level `gold/canonical/canonical_performance_{date}.parquet`. `aua_change`
  is canonical_performance's own per-account field, summed to household.
- `return_pct_twr = daily_factor - 1`, where `daily_factor` comes from
  `_build_daily_factor_table(perf_dim)` reading `silver/performance_dim/`.
- `return_$ = prior_total_aua * return_pct_twr`, `prior_total_aua = total_aua.shift(1)`.
- `epsilon_$ = aua_change - net_nna - return_$` (the residual; PRD section 2.4 — epsilon
  is MEASURED, not assumed).

`_build_daily_factor_table` (INF_C_02.py:106-160): groups `performance_dim` by
`client_id`, sorts by `period_end_date`, and for each consecutive pair computes
`weekly_relative = twr_factor_period[curr] / twr_factor_period[prior]`, then
`daily_factor = weekly_relative ** (1/n_days)`. **Its docstring states the
assumption explicitly: "Sort weekly CUMULATIVE TWR factors ... Identity preserved:
PI(daily_factors) = period_TWR_factor."** That assumption — that
`twr_factor_period` is a cumulative-growth factor — is the defect.

`epsilon_$` ranges over the SAME household set as `return_$` — both are computed
on the same `hh_perf` rows. There is no entity-set asymmetry between the terms.

## 2 — Set P vs Set A (AC1) — coverage is NOT the issue

Account/household coverage measured against live artifacts (YTD,
2026-01-01..2026-05-17):

| Set | Definition | Count |
|-----|-----------|-------|
| Set A | all (household,date) rows feeding `aua_change` | 38,840 rows / 296 households |
| Set P | rows with non-null `return_pct_twr` feeding `return_$` | 37,656 rows (97.0%) / 295 households |
| A − P | rows with no return coverage | 1,184 rows / 1 never-covered household |

**The 1,184 A−P rows are exactly the 4-day stale tail** (05-14..05-17 x 296
households) — see section 4. Only **1** household is never covered.

`is_managed` split (accounts_dimension, 862 accounts): 848 managed / 14
non-managed. **Non-managed accounts hold $0.13M of $202.6M = 0.1% of AUA.** The
managed/unmanaged split cannot explain a 71.6% epsilon.

AUA-weighted: `aua_change` sitting in non-covered rows = -$1.59M = 7.2% of firm
`aua_change` — and all of it is the stale tail.

## 3 — Epsilon attribution (AC2) — candidate (i) RULED OUT

Firm YTD decomposition (`client_performance.parquet`):

| Term | YTD sum |
|------|--------:|
| SUM aua_change | $22,094,046 |
| SUM net_nna | $4,327,985 |
| SUM return_$ | $2,206,325 |
| SUM epsilon_$ | $16,496,355 |
| **epsilon share** | **71.6%** |

Epsilon attribution by coverage:

- epsilon in COVERED rows (Set P) = **$16,496,355 (100.0%)**
- epsilon in UNCOVERED rows (A − P) = **$0**

**100% of firm epsilon is in return-COVERED households.** Candidate (i)
incomplete-perf-coverage explains **0%** of the dominance — the epsilon is not
coming from uncovered accounts; it is coming from covered households whose
modeled `return_$` is far too small. **Candidate (i): RULED OUT.**

Per-advisor epsilon share (YTD): inflection_wealth_management 44.9%,
joe_brandenburg 63.5%, patrick_scanlan 61.0%, peter_lee 73.7% — firm-wide and
systematic, not a per-advisor coverage artifact.

## 4 — Candidate (ii) staleness — RULED OUT (as the cause of dominance)

`silver/performance_dim` latest partition = `2026-05-13.parquet`;
`canonical_performance` latest = `2026-05-17`. 4-day staleness. The 4 stale dates
(05-14..05-17) carry NaN `return_pct_twr` -> NaN `return_$`/`epsilon_$`;
INF_D_00c's `_aggregate_gro_*` apply `.fillna(0)`, so the stale-tail rows
contribute **0** to epsilon. **Staleness does not inflate epsilon** — it drops 4
of ~137 YTD days from the decomposition. Candidate (ii): RULED OUT as the cause
of the 71.6% dominance.

It is a real freshness gap — `performance_dim` not advancing past 05-13 links to
the bronze/performance `--run-date` catalog item (ADVI_INFETL lane,
RUNDATE-DISPATCH-IMPL in flight under AE 0.7.0). **Surfaced as a linkage, not
absorbed into this TO** (per TO out_of_scope).

## 5 — Candidate (iii) — RULED IN, precisely characterized

### 5.1 The grain of `twr_factor_period`

`silver/performance_dim` is built by `INF_C_03.performance_canonical.py`, which
passes `bronze.factor -> twr_factor_period` unchanged. Its header (lines 10-12)
states the empirical TO-INFGRO.002 finding: **"the client-level Orion endpoint
exposes annualized TWR % only."**

`twr_factor_period` trajectory at year boundaries (client 167) confirms it is an
inception-to-date ANNUALIZED rate, not a cumulative-growth factor:

| Date | twr_factor_period |
|------|------------------:|
| inception 2020-06-03 | 1.000000 |
| 2021-01 | 1.139762 |
| 2022-01 | 1.146270 |
| 2023-01 | **1.031057** (drops — 2022 drags the inception-annualized rate down) |
| 2024-01 | 1.040722 |
| 2025-01 | 1.044114 |
| 2026-05-13 | 1.057426 |

A cumulative-growth factor monotonically climbs; this one drops 1.146 -> 1.031
across 2022. That is the signature of an **inception-to-date annualized return**
(a bad year drags the annualized figure down). A 6-year cumulative growth factor
of 1.057 (+5.7% total) would also be absurd; +5.7% *annualized* is sensible.

### 5.2 The decomposition error

`_build_daily_factor_table` computes `weekly_relative = f_curr / f_prior`. For an
annualized-rate series, two consecutive values are ~equal, so `f_curr/f_prior` is
~1.0 +/- a tiny amount unrelated to the period's actual return. Result:
`return_pct_twr` ~ 0, `return_$` ~ 0, `epsilon_$` absorbs the real AUA movement.

Weekly TWR-implied vs AUA-implied return (`f_curr/f_prior - 1` vs the household's
own `(delta total_aua - net_nna)/aua_start`), 3 households, big-move weeks:

| Week | TWR f_curr/f_prior-1 | AUA-implied | ratio |
|------|---------------------:|------------:|------:|
| 04-01->04-08 (HH 167) | +0.245% | +1.551% | 6.3x |
| 04-01->04-08 (HH 68)  | +0.394% | +2.478% | 6.3x |
| 04-01->04-08 (HH 388) | +0.384% | +2.419% | 6.3x |
| 04-08->04-15 (3 HHs)  | ~+0.10-0.19% | ~+0.70-1.26% | 6.6-6.9x |

The ratio is **identical across households on the same week** (6.3x on
04-01->04-08 for all three) — a firm-wide systematic understatement, not
household-specific noise. The clean-week ratio is ~6x; flat weeks are noisier
(small/small).

### 5.3 Reconstruction proof

If `twr_factor_period = 1 + annualized_return`, then cumulative growth =
`twr_factor_period ** years_since_inception`, and the YTD return reconstructs as
`cum(2026-05-13) / cum(2026-01) - 1`:

| Client | RECONSTRUCTED YTD (factor^yrs) | AUA-implied YTD | CURRENT INF_C_02 |
|--------|------------------------------:|----------------:|-----------------:|
| 167 | +3.23% | +3.46% | +0.36% |
| 68  | +5.14% | +5.41% | +0.61% |
| 388 | +4.97% | +5.56% | +0.61% |
| 260 | +8.37% | +6.35% | +1.56% |
| 201 | -1.53% | +0.69% | -0.95% |

For the established households (167/68/388) the annualized-rate reconstruction
recovers the AUA-implied return to within 0.2-0.6pp; the current INF_C_02
arithmetic is ~9-10x too small. (Clients 260/201 — short history / near-zero
return — reconstruct more roughly: `factor ** years` is numerically sensitive
when the history is short, which is why the precise reconciliation method is a
CTO call, section 6, not a unilateral DS fix.)

**Candidate (iii): RULED IN.** It is the sole cause of the 71.6% epsilon
dominance. It is a cumulative-vs-annualized grain error at the
INF_C_02 <-> silver/performance_dim boundary — `_build_daily_factor_table`
misinterprets an annualized-rate source.

### 5.4 Bearing on Finding A / INFGRO.007

The same defect understates Finding A. INFGRO.007's Axis-2 chain-link
*aggregation* fix is correct, but it compounds `return_pct_twr` values that are
themselves ~6-10x too small — so the shipped firm window TWRs (MAX 12.38%) are
~6x understated in absolute scale (true MAX likely ~50-75%). INFGRO.007's
relative tells (monotonic, %-consistent) hold; the absolute scale does not.
**INFGRO.005 criterion (a) "plausible window TWRs" should be read as
relatively-plausible-only until this is fixed.** This confirms PRD section 8.4's
predicted shared-root case.

## 6 — Reconciliation methods — for the CTO ruling

**The TO's A/B/C menu is coverage-framed; Phase 0 ruled coverage OUT, so A/B/C
do not address the diagnosed root.** Restated for completeness:
- TO-A (restrict aua_change to Set P): N/A — Set P is already 97% / 100% of epsilon.
- TO-B (derive TWR for uncovered accounts): N/A — uncovered accounts hold ~0 epsilon.
- TO-C (reclassify uncovered return out of epsilon): rejected per section 2.4; also moot.

The actual reconciliation choice, framed against the section 5 diagnosis:

- **Method X — reconstruct cumulative growth from the annualized rate.** In
  INF_C_02, compute `cumulative_growth_t = twr_factor_period_t ** years_since_inception_t`,
  then derive per-period returns from the reconstructed cumulative series before
  the daily decomposition. Pro: uses data already in hand. Con: requires a
  reliable per-client inception date; `**years` is numerically sensitive for
  short-history / near-zero-return clients (260/201 evidence) and may need
  guard-railing.
- **Method Y — obtain a true cumulative or per-period TWR from Orion.** Replace
  the annualized-% field with a cumulative-growth or periodic-return field/endpoint
  (the PERF Pattern-E / INFINC.006 work touched `/Clients/{id}/Performance` — it
  may expose period returns directly). Pro: authoritative, no reconstruction
  numerics. Con: new bronze ingestion work; depends on what Orion exposes.
- **Method Z — leave epsilon dominant / assume the return.** Rejected — violates
  the PRD section 2.4 "epsilon MEASURED, not assumed" invariant. Listed for
  completeness only.

The choice (X vs Y) touches section 2.4 and the section 3 / 8.3 grain branches — it is a
CTO architectural call. The fix TO is authored after the ruling.

## 7 — Compiler tools

| Run | Result vs expect |
|-----|------------------|
| `comp-pipescript io INF_C_02.client_performance` | READS `accounts_dimension_latest.parquet` + `client_performance.parquet` (append-mode self-read); WRITES `gold/timeseries/client_performance.parquet` -> INF_C_04, INF_C_06, INF_D_00, INF_D_00b, INF_D_00d, INF_D_04, INF_D_05a. No COLUMN GAPS. Matches PRD section 8.4. The dynamic paginated reads (`canonical_performance_*`, `silver/performance_dim/*`) are not statically traced — documented from source instead. Not a STOP condition (the I/O model holds). |
| `comp-pipescript feeds INF_C_02.client_performance` | "no upstream pipeline dependencies (reads from silver or external)" — matches expect (Set P / Set A sources are silver/external). |
