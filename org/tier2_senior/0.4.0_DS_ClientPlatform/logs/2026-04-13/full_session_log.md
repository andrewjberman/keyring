# 0.4.0_DS_ClientPlatform -- Full Session Log

**Date:** 2026-04-13 (EDT)
**Session span:** ~09:00 EDT Apr 13 to ~14:15 EDT Apr 13
**Agent:** 0.4.0_DS_ClientPlatform

---

## TOs Completed This Session

| TO | Title | Status | Per-TO log |
|---|---|---|---|
| (ad hoc) | Yang benchmarks SI field investigation | complete (DS no code change; AE deployed) | [yang_benchmarks_si_investigation section](#1) |
| (ad hoc) | GEO snapshot vs continuous AUA discrepancy | complete (D_01 fix deployed) | [geo_aua_discrepancy section](#2) |
| `ADVI_REBORN.W6-001` | D_04 leaderboard fee_paying + no_fee passthrough | **complete** | [`advi_reborn_w6_001_leaderboard_fee_buckets.md`](advi_reborn_w6_001_leaderboard_fee_buckets.md) |
| `ADVI_REBORN.W6-003` | D_00c role_combination_breakdown | **complete** (superseded by W6-005) | (inline below) |
| `ADVI_REBORN.W6-005` | D_00c split_pct-weighted role fee buckets | **complete** | (inline below) |

---

## 1. Yang Benchmarks SI Investigation

**Trigger:** Andrew reported SI column on ModelPortfolios Benchmark tab showing values that looked wrong (~2.34% UST when he expected a cumulative return).

**Investigation:**
- Ran `comp-routes` (no match), grep'd portal frontend and found `BenchmarkHeatmap.tsx` with an `annualizeSI` helper that annualizes SI before display.
- Fetched live S3 `benchmark_returns.json` and `model_portfolio_benchmarks.json`: UST SI = 4.79%, LTC = 15.93% (annualized-once from Lambda).
- Scanned all 27 S3 version history entries of `benchmark_returns.json` (script `data/analysis/si_flip_scan.py`). Found the Lambda output was CUMULATIVE before 2026-01-22, then flipped to ANNUALIZED. Trace: commit `feca94a1` (2026-01-21) added annualization block at lines 401-409 of `yang-model-portfolio-benchmarks/lambda_function.py`.
- Portal `BenchmarkHeatmap.tsx` also added `annualizeSI` on 2026-01-14 (commit `79dbb15`). Frontend annualizes Lambda-annualized output → **double-annualized** ($4.79% → $2.34%).
- Checked yang PKL history (mar29/apr05/apr12 cross-check via `data/analysis/yang_pkl_si_xcheck.py`): PKL was innocent — return_daily identical on 697 common dates.
- DT investigated server-side: bundle versioning off (can't confirm exact deploy date), CloudFront invalidations normal, portal PROD rebuilt 25 times since Feb 25. 4/6 onset mystery unresolved.
- Andrew directive: **SI = absolute cumulative, no transformation**.
- **DS fix:** deleted annualization block from both `yang-model-portfolio-benchmarks/lambda_function.py` and `yang-generate-benchmark-returns/lambda_function.py`. Commit `bc6f4ccb`.
- **AE 0.5.0 deployed:** `yang-v2.3.7` confirmed via MCP message.
- **DT pivoted:** portal re-annualizes once on top of cumulative (consistent with Andrew's subsequent confirmation). SI now shows single-annualized (~4.79% UST). Frontend also shows annualized in ReturnVolatilityScatter (both surfaces consistent).

**Compiler Tools:**
- `comp-routes trace getBenchmarkReturns` → no match (used direct grep)
- S3 version scan: 27 historical snapshots spanning 2026-01-04 to 2026-04-12
- Yang PKL cross-check: 697 common inception-window dates across 3 snapshots

---

## 2. GEO Snapshot vs Continuous AUA Discrepancy

**Trigger:** Andrew noted Snapshot GEO AUA shows $1.64B, Continuous shows $1.65B, Assets Overview headline shows $1.65B.

**Investigation:**
- Traced DistributionTab.tsx: Snapshot reads `partner_analytics_quarterly.json → views.geo.current.metrics.aua`; Continuous reads `cumulative_chart.json → geo.data`.
- Used `comp-platinum reverse` to identify producers: Snapshot path-through = D_01 `header_metrics_quarterly.json`. Continuous = D_00b `timeseries_chart.json`.
- Fetched live S3 values: `geo.current.metrics.aua = $1,643,056,448.59` (Snapshot display = $1.64B); continuous geo sum = $1,646,714,399.86 (= headline).
- Root cause: D_01 `build_geo_view` line 741-745 filters `state != 'Unknown'` before computing `total_aua` and setting `metrics.aua`. Unknown-state accounts ($3.66M, 0.22% of firm AUA) are excluded. D_00b continuous includes them.
- **Fix:** added `firm_total_aua` param to `build_geo_view`; when provided, `metrics.aua = firm_total_aua` instead of state-filtered sum. D_04 main loop already computes `_firm_total_aua` for ADV view and now passes it to GEO view call.
- Commit `b846b2b5`. Deployed via full incremental run (accidental — trigger Lambda doesn't support `--group D`; lesson noted).
- Post-run verification: `partner_analytics_quarterly.json` updated 15:59:03 UTC. `geo.current.metrics.aua` now = $1,646,714,399.87 (matches headline).

**Note on deploy incident:** Triggered `bd-gold-trigger` with `{"group":"D"}` payload but trigger Lambda ignores `group` field — only writes `mode=incremental` to marker. Runner started full A→D chain (~90 min). Going forward: use SSM `gold_dispatch.sh --single <script>` or `--group D` for targeted runs.

---

## 3. ADVI_REBORN.W6-001 — Leaderboard Role Fee Passthrough

See full per-TO log: `advi_reborn_w6_001_leaderboard_fee_buckets.md`.

**Summary:** Added `'fee_paying'` and `'no_fee'` to `_LEADERBOARD_ROLE_FIELDS` in D_04 (one-line change). D_00c already emitted these sub-objects; D_04 trim was dropping them. Frontend W6-002 (DE) followed.

---

## 4. ADVI_REBORN.W6 Series — Fee × Role Intersection (W6-001 through W6-005)

**Context:** Andrew's audit: "Fee-Paying + Implementor off" showed $394M instead of expected ≤$341M.

### W6-002 (DE frontend, not DS)
DE removed `?? data` fallback in `AdvisorsTab.tsx`. Fixed the 394M bug. Post-fix numbers: 398M (all roles + fee-paying), 366M (no implementor + fee-paying). Andrew found the non-additive issue: adding implementor DROPS total from 366→341. Not right.

### W6-003 — role_combination_breakdown (superseded)
- Built `_build_role_combination_breakdown()` in D_00c: partitions accounts by full role-set membership (`architect`, `architect|implementor`, etc.), emits `fee_paying + no_fee` AUA per combination.
- D_04 passes through verbatim.
- Travis: 5 combinations present. Additive invariant: 365.5M + 32.6M = 398.1M.
- BUT: `sum(combo.fee_paying) = $398M` vs `fee_breakdown.fee_paying = $340.5M`. AUA source mismatch between account_team (portfolio snapshot) and fee_detail (billing system). **Superseded by W6-005.**

### W6-004 (DE frontend, not DS)
DE wired W6-003 combo schema in `AdvisorsTab.tsx`. Numbers were ~correct-ish but wrong canonical total. Reverted after W6-005.

### W6-005 — Split-pct-weighted fee buckets (correct implementation)
**Root cause discovered:** `fee_rate_history.is_billable=True` marks 448 Travis accounts ($398M) as fee-paying. C_08 additionally requires `split_pct > 0` → 215 accounts ($340.5M). The $57.6M gap = accounts where Travis is billable but has 0% split allocation (house accounts). D_00c was using the looser definition.

**Andrew's rule (split_pct weighting):**
1. Multi-role, all fee-paying: weight = `split_pct[role] / sum(split_pct[active roles])`
2. Multi-role, no fee-paying: equal split (1/N)
3. Multi-role, mixed: full weight to fee-paying roles only

**Implementation:**
- Added `ADVISOR_ASSIGNMENTS` to D_00c imports + `load_for_leaderboard`.
- Loaded current split_pcts from `advisor_assignments_history.parquet` (`is_current=True`).
- Joined into melted DataFrame; resolved `_role_split_pct` per (account, advisor, role).
- Updated `_is_fee_paying = billable AND split_pct > 0` (matches C_08's filter).
- Replaced `_split_weight = 1/n_roles` with three-case split_pct weight via `_compute_split_weight`.
- Added post-hoc scaling: `scale = fee_aua / sum(role.fee_paying.aua)` to guarantee exact match to billing canonical. Handles PIT vs is_current drift in assignments.

**Validation (all 152 QTD advisors):** `sum(role.fee_paying.aua) == fee_breakdown.fee_paying.aua` within $0.02 for every advisor.

**Travis Penfield QTD result:**
- `fee_breakdown.fee_paying.aua = $340,504,526.17`
- `sum(role.fp.aua) = $340,504,526.17` (diff = $0.00)
- `no-imp fee_paying = $307,900,383.45`
- `+ implementor = $32,604,142.72`
- `= all-roles = $340,504,526.17` ✓ (additive, monotone)

Per-role: architect $305.8M, implementor $32.6M, consultant $1.2M, additional_advisor $0.86M.

---

## Compiler Tools

| Section | Tool | Command/Action | Result |
|---|---|---|---|
| SI investigation | S3 version scan | 27 `benchmark_returns.json` versions | Flip date confirmed: 2026-01-22 |
| SI investigation | Yang PKL cross-check | `data/analysis/yang_pkl_si_xcheck.py` | PKL innocent, 697 common dates identical |
| GEO AUA | comp-platinum reverse | `partner_analytics_quarterly.json`, `cumulative_chart.json` | Producers: D_01 (snapshot), D_00b (continuous) |
| GEO AUA | S3 live fetch | `partner_analytics_quarterly.json`, `cumulative_chart.json`, `clients-tab-slim.json`, `dashboard.json` | metrics.aua = $1.643B, continuous sum = $1.647B, headline = $1.647B |
| W6-001 | comp-pipescript | `comp-pipescript io D_04` | Confirms EMPLOYEE_LEADERBOARD read, `platinum/firm/leaderboard.json` write |
| W6-001 | Live S3 validate | Post-deploy leaderboard.json Travis sample | AC1/AC2/AC3/AC4 PASS |
| W6-005 | account_team + assignments audit | boto3 S3 read + pandas analysis | $57.6M gap = billable-but-split_pct==0 accounts (233 accounts). 215 accounts at $340.5M match fee_breakdown exactly. |
| W6-005 | Full dry-run validation | `importlib` load + `build_employee_leaderboard` | All 152 QTD advisors: sum(role.fp) == fee_breakdown.fp ≤ $0.02 |
| W6-005 | Post-deploy verify | S3 `platinum/firm/leaderboard.json` 18:14 UTC | Travis $340.5M exact, additive PASS |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| AE deploy brief (yang SI) | `docs/briefs/ae-brief-yang-benchmarks-si-unannualize.md` | AE (0.5.0) |
| DT briefing (SI investigation) | (relayed verbally in session) | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Commit |
|---|---|---|
| `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` | Deleted SI annualization block (lines 401-409) | `bc6f4ccb` |
| `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-benchmark-returns/lambda_function.py` | Same deletion | `bc6f4ccb` |
| `docs/briefs/ae-brief-yang-benchmarks-si-unannualize.md` | Created | `bc6f4ccb` |
| `data/black_diamond/scripts/gold/D_01.partner_analytics.py` | `build_geo_view` accepts + uses `firm_total_aua` for `metrics.aua` | `b846b2b5` |
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Added `fee_paying`/`no_fee` to `_LEADERBOARD_ROLE_FIELDS`; added `role_combination_breakdown` passthrough; added `rcb` passthrough | `87557c33`, `1d70ecaf` |
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | `role_combination_breakdown` (W6-003); full split_pct three-case weighting + `_is_fee_paying = billable AND split_pct > 0` + post-hoc scaling (W6-005) | `1d70ecaf`, `0804b377` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_REBORN.W6-001.*` | Status: staged → pending → complete | `977c64ec` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_REBORN.W6-003.*` | Created + status: pending → complete | `1d70ecaf` |
| `data/analysis/si_flip_scan.py` | Created: S3 version scan for SI flip diagnosis | (committed separately) |
| `data/analysis/yang_pkl_si_xcheck.py` | Created: PKL cross-check | (committed separately) |
| `data/analysis/geo_aua_snapshot_vs_continuous.py` | Created: GEO AUA discrepancy analysis | (not committed) |
| `data/analysis/validate_leaderboard_fee_buckets.py` | Created: W6-001 Phase 2 validation | (not committed) |
| `data/analysis/validate_role_combination_breakdown.py` | Created: W6-003 Phase 2 validation | (not committed) |

---

## Deploy Cycles

| Script | S3 etag | Method | Run time | Output verified |
|---|---|---|---|---|
| `yang-model-portfolio-benchmarks` + `yang-generate-benchmark-returns` | (AE managed) | `yang-v2.3.7` terraform apply | N/A | Next PKL refresh will produce cumulative SI |
| `D_01.partner_analytics.py` | (via full incremental) | Accidental full A→D via `bd-gold-trigger` | ~90 min | `geo.current.metrics.aua = $1.647B` at 15:59:03 UTC |
| `D_04.client_portal_summary.py` (W6-001) | `36674fa3…` | SSM `--single D_04` on prod runner | 303s | `platinum/firm/leaderboard.json` 16:40:48 UTC; AC1-4 PASS |
| `D_00c.portal_leaderboard.py` (W6-003) | `b5305bbd…` | SSM `--single D_00c` on prod runner | 39s | `employee_leaderboard.json` 17:25:11 UTC |
| `D_04.client_portal_summary.py` (W6-003) | `d12ab64b…` | SSM `--single D_04` on prod runner | 314s | `platinum/firm/leaderboard.json` 17:30:22 UTC |
| `D_00c.portal_leaderboard.py` (W6-005) | `d7e53f07…` | SSM `--single D_00c` on prod runner | 38s | `employee_leaderboard.json` 18:08:57 UTC |
| `D_04.client_portal_summary.py` (W6-005) | (same as prior D_04) | SSM `--single D_04` on prod runner | 315s | `platinum/firm/leaderboard.json` 18:14:13 UTC; Travis $340.5M exact, additive PASS |

---

## Commits This Session

| SHA | Scope | Author |
|---|---|---|
| `bc6f4ccb` | Yang benchmarks SI fix + AE brief | DS |
| `b846b2b5` | D_01 geo metrics.aua reconciliation | DS |
| `87557c33` | D_04 W6-001 fee_paying/no_fee trim | DS |
| `977c64ec` | W6-001 session log + TO status | DS |
| `1d70ecaf` | D_00c + D_04 W6-003 role_combination_breakdown | DS |
| `0804b377` | D_00c W6-005 split_pct weights | DS |

---

## Open Items / Next Steps

- **[Andrew]** Confirm four-cell matrix looks correct in portal after DE reverts W6-004 combo logic and RE wires per-role sum. DE has the signal.
- **[0.4.0_DE_ClientPlatform]** W6-004 revert + re-wire to per-role `role_breakdown[role].fee_paying.aua` sum for fee-filtered role subsets. Portfolio of W6-003 combo schema can be removed.
- **[0.4.0_DS_ClientPlatform next session]** ADVI_PROFAU.001 TO is staged (no GO yet). COO updated framing: EXISTS-UPSTREAM first, new label taxonomy. Read `profau_gap_audit_response.md` (not `profaup_...`) target.
- **[0.4.0_DS_ClientPlatform next session]** Verify D_04 NNA/flows in `role_breakdown[role].fee_paying` are consistent with the new split_pct-weighted AUA (flows use a separate window metrics path — check `_compute_tagged_window_metrics_by_role` still aligned).
- **[0.4.0_DT_ClientPlatform]** portal-v2.1.39 deployed 4/10. Yang SI fix pending next PKL refresh; once confirmed, close the loop on SI fix.
- **[DO NOT]** Use `bd-gold-trigger` when a targeted `--single <script>` or `--group D` is needed. The trigger ignores `group` in payload — use SSM `gold_dispatch.sh` directly.

---

## Do NOT Rules (session-wide)

- Do NOT interpret `sum(combo.fee_paying.aua)` as equivalent to `fee_breakdown.fee_paying.aua` — W6-003 combo schema uses account_team AUA, billing system uses fee_detail AUA, sources can differ. Use per-role split_pct-weighted path (W6-005) for canonical numbers.
- Do NOT re-add SI annualization to yang Lambda. SI is emitted as cumulative; frontend annualizes once for display. Both layers agree.
- Do NOT trigger a full gold rebuild when only D_00c/D_04 changes. Use SSM `--single D_00c` then `--single D_04` sequentially.
- Do NOT skip `_is_fee_paying = billable AND split_pct > 0` — the split_pct > 0 requirement is what aligns D_00c with C_08's fee definition. Reverting to billable-only produces $57.6M overcounting for Travis.
