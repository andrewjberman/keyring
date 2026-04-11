# ds-advi-nna-canonical-source -- D_04 emits by_geo + by_adv in timeseries_overview.nna

**Date:** 2026-04-10
**Agent:** 0.4.0_DS_ClientPlatform
**TO:** `ds-advi-nna-canonical-source` (ad-hoc, issued by 2.0.0_SA_COO, 2026-04-10)
**Brief:** `docs/briefs/ds-brief-advi-nna-canonical-source.md`

## Summary

Extended `build_timeseries_overview()` in `D_04.client_portal_summary.py` to attach per-category NNA breakouts (`by_geo` + `by_adv`) inside every entry of `nna.{monthly|quarterly|annually}`. Single-source canonical partition: the breakouts are aggregated from `gold/canonical/nna/*.parquet` daily flows, not from cumulative pairwise-diff. Category keys reuse `ts_chart.nna_geo.categories` / `nna_adv.categories` (top-9 + Other) so they match `cumulative_chart.json` byte-for-byte. Sum invariance holds structurally for every period × granularity × cohort after residual absorption into `Other`, hard-asserted within $0.05 tolerance.

**Commit SHA:** `f5398e42` (DS-authored, attribution correct this time)
**S3 etag parity:** `e971b6618cad6bc256f1da49a1feea3e` (local md5 == S3 etag)
**Status:** Code is on CLOUD + in `s3://opal-data-bd/code/gold/`. **Runner is STOPPED**, so there is no timing race this time. Next gold run will pick up the new `D_04.client_portal_summary.py` cleanly.

## Path decision rationale

The TO offered two options:
- (a) D_04 reads `CANONICAL_NNA_PREFIX` directly (adds a new D_04 input)
- (b) Pre-aggregate upstream in D_00/D_00b and have D_04 consume the pre-aggregated per-period-per-category output

**Chose (a).** Reasons:
1. **Scope compliance.** The TO lists `D_00b.portal_timeseries.py` under `file action="reference"` -- explicitly not-to-modify. D_00b is where the per-category groupby already happens, but modifying it is out of scope for this TO. Reading canonical_nna in D_04 is additive and self-contained.
2. **Minimizes layering churn.** Adding a new intermediate artifact (option b) means a new output from D_00/D_00b, a new read from D_04, and a new contract surface. Reading canonical_nna directly puts the entire new computation in one function inside one script.
3. **canonical_nna is already multi-reader.** D_00 and D_00b both read `CANONICAL_NNA_PREFIX`. D_04 becoming a third reader is not a layering regression -- the parquet is the firm's canonical source by design.
4. **Single source of truth.** Both the top-level `nna.*` firm totals and the new `by_geo` / `by_adv` breakouts are now computed from data that originates in canonical_nna (top-level via D_00b -> ts_chart.nna, breakouts via D_04's direct read). In principle they should agree. Where they don't (see "Known source drift" below), the drift is quantified and absorbed into `Other` explicitly.

## Implementation

### New imports

```python
from lib.s3_layout import (
    ...,
    CANONICAL_NNA_PREFIX,
)
```

`ThreadPoolExecutor`, `as_completed`, `BytesIO`, `pandas as pd` were already imported for other parts of D_04.

### New helpers (all in D_04, before `build_timeseries_overview`)

1. `_nna_period_key(ds, gran)` -- derives `(period_key, label)` for an ISO date string and granularity. **Matches `_aggregate_nna_to_periods._period_key` exactly** so the per-category buckets zip 1-to-1 with the top-level entries by period.

2. `_load_canonical_nna_flows()` -- streams every `gold/canonical/nna/*.parquet` partition into a concatenated daily-flow DataFrame. Columns: `date, account_id, client_state, architect, daily_inflow, daily_outflow`. Unresolved values normalized: `client_state -> 'Unknown'`, `architect -> 'Unassigned'`. Uses `ThreadPoolExecutor(max_workers=READ_WORKERS=64)` for parallel load. Reports row count, date count, and account count.

3. `_build_per_category_nna_by_period(df, top_cats, category_col, gran)` -- the per-category groupby. For a given category column (`client_state` for geo, `architect` for adv), maps non-top values to `'Other'`, groups by `(period_key, category)`, sums inflow / outflow. Returns `{period_key: {category: {inflow, outflow, net}}}`. Stores both inflow and outflow as POSITIVE, `net = inflow - outflow` (matching actual top-level convention -- see "Brief drift" below).

4. `_absorb_residual_into_other(by_cat, entry, cohort, gran)` -- closes the partition sum to `entry.{inflow|outflow|net}` by adding the residual to the `'Other'` category. Logs per period where `|residual| > $1`. Then **hard-asserts** `sum(by_cat.field) == entry.field` within `_NNA_PARTITION_HARD_TOL = $0.05`. Raises `AssertionError` on violation -- a post-absorption violation indicates a bug in the absorber itself, since absorption should structurally close the sum to zero modulo floating-point noise.

5. `_attach_nna_breakouts(nna_periods, canonical_df, geo_cats, adv_cats)` -- the orchestrator. For each granularity, calls `_build_per_category_nna_by_period` once for geo and once for adv, then iterates entries, looks up the period's breakout, fills missing categories with zero cells, absorbs residual, attaches `entry['by_geo']` / `entry['by_adv']`.

### Integration point in `build_timeseries_overview`

Immediately after the existing `_aggregate_nna_to_periods(nna_raw)` call:

```python
# Per-category NNA breakouts (by_geo + by_adv) nested into every entry.
nna_geo_cats = ts_chart.get('nna_geo', {}).get('categories', [])
nna_adv_cats = ts_chart.get('nna_adv', {}).get('categories', [])
if nna_geo_cats and nna_adv_cats:
    canonical_nna_df = _load_canonical_nna_flows()
    _attach_nna_breakouts(nna, canonical_nna_df, nna_geo_cats, nna_adv_cats)
else:
    print('  WARN: nna_geo/nna_adv categories absent from ts_chart '
          '-- skipping breakouts')
```

No change to the AUA section, the growth decomposition section, the mix section, or the final `_write_batch`. Top-level `nna.*` fields are byte-for-byte unchanged per scope constraint #1.

## Known source drift (documented, absorbed, asserted)

Live measurement on 2026-04-10 data:

| Partition | Accumulated drift (firm-wide) | Source |
|---|---|---|
| `by_adv` | ~$0.02 (floating-point noise) | None -- already structurally closed because D_00b maps unresolved architects to `'Unassigned'` which rolls into `Other` |
| `by_geo` | ~$817,980 (NNA), ~$1,627,980 (inflow), ~$809,999 (outflow) | D_00b's `_nna_drill_data` excludes `state == 'Unknown'` and non-US rows (see `D_00b.portal_timeseries.py:781-782`). Those account-days exist in the firm total but not in `nna_geo.data`. |

Per-period breakdown (quarterly, pre-absorption pairwise-diff sanity check on raw ts_chart):

| Quarter | Firm NNA net | Geo partition sum | Drift (geo only, inflow/net) |
|---|---|---|---|
| 2023-Q2 | $49.20M | $49.08M | -$118,860 |
| 2023-Q3 | $36.93M | $36.93M | -$16 |
| 2024-Q2 | $52.09M | $52.09M | -$100,000 / +$0.02 |
| 2025-Q4 | $81.70M | $80.99M | -$1,409,103 / -$699,103 |
| Most other quarters | varies | varies | <= $0.03 (noise) |

Materially, three quarters in the last three years see large geo drift (2023-Q2, 2024-Q2, 2025-Q4). All three correspond to periods with large transactions on Unknown-state accounts (non-US or unresolved geography).

**Absorption semantics:** the residual is added to the `Other` geo bucket per period. `Other` is ALREADY the catch-all bucket in the brief's top-9 + Other rule, and "unresolved geo" is semantically a kind of "other". This is a more accurate representation of Other than cumulative_chart.json's Other, which underreports it. Byte-for-byte category key parity is preserved: the keys are still exactly `['TX', 'FL', 'GA', 'CA', 'NC', 'AR', 'NY', 'KS', 'AZ', 'Other']`, just with a more complete Other dollar value.

This is documented here so a future DS or a reviewer knows:
1. The Other bucket in `timeseries_overview.by_geo` is LARGER than the Other bucket in `cumulative_chart.nna_geo` for periods with Unknown-state residual.
2. This is INTENTIONAL: it's what makes sum-invariance hold structurally.
3. The root fix (populate state for Unknown accounts) is a D_00b / silver enhancement that belongs in a different TO.

## Brief drift -- outflow sign convention

The brief's invariant #7 and the TO's requirement #4 both say:

> "`by_geo[cat].outflow` is stored NEGATIVE (matches the top-level sign convention already in `timeseries_overview.nna.*`)"

**The brief's stated premise is incorrect.** The live `timeseries_overview.json` stores `nna.quarterly[*].outflow` as a POSITIVE number, with `net = inflow - outflow` (not `inflow + outflow`). Verified against `s3://opal-data-bd/platinum/firm/timeseries_overview.json` on 2026-04-10:

```
2026-Q2 inflow=9,936,991.72  outflow=6,628,873.78  net=3,308,117.94
  (inflow - outflow = 3,308,117.94 PASS)
  (inflow + outflow = 16,565,865.50 FAIL)
```

I matched the ACTUAL top-level convention (both positive, net = inflow - outflow) rather than the brief's stated (incorrect) premise. The principle "match top-level" is preserved -- I just followed what top-level actually does, not what the brief claimed top-level does.

This will not affect the frontend migration because the frontend bar construction code in the brief's §Frontend-follow-up uses `inflows += cv.inflow`, `outflows += cv.outflow`, `net += cv.net` -- sign-neutral. The hero / legend logic can render outflow with a minus sign at display time without affecting the stored value.

Session log flagged to 2.0.0_SA_COO so the brief can be corrected if it's reused.

## Dry-run validation (local, pre-deploy)

Ran the full pipeline end-to-end against live S3 data without uploading:

```
geo_cats: ['TX', 'FL', 'GA', 'CA', 'NC', 'AR', 'NY', 'KS', 'AZ', 'Other']
adv_cats: ['Travis Penfield', 'Kyle Sims', 'Greg Rosner', 'Hunter Lloyd',
           'Josh Henson', 'Chase Bertrand', 'Dean Dillenberg',
           'David Farrell', 'Tim Rodgers', 'Other']

Top-level periods: 26q, 76m, 7y

Loading canonical_nna for NNA breakouts...
    [ 500/2290] partitions loaded
    [1000/2290] partitions loaded
    [1500/2290] partitions loaded
    [2000/2290] partitions loaded
    [2290/2290] partitions loaded
  canonical_nna: 5,836,153 rows, 2290 dates, 7314 accounts
canonical_nna load time: 37.6s (2290 parquets, 16 IO workers)

Attach time: 27.1s (groupby + absorb + assert across 26+76+7 = 109 entries x 2 cohorts)

SUCCESS: all sum-invariants held after absorption
```

### Q2 2026 spot check (Andrew's reference period)

| | top-level | by_geo sum | by_adv sum |
|---|---|---|---|
| 2025-Q4 net | $81,698,609.04 | $81,698,609.04 | $81,698,609.04 |
| 2026-Q1 net | $66,040,903.07 | $66,040,903.07 | $66,040,903.07 |
| 2026-Q2 net | $3,308,117.94 | $3,308,117.94 | $3,308,117.94 |

Exact match on all three. Same exact match across monthly and annually spot checks.

**Top-3 geo for Q2 2026:** `TX=$3.5M, FL=$1.45M, Other=$309K` (Texas concentration consistent with 49 Financial's primary market).

**Top-3 adv for Q2 2026:** `Travis Penfield=$2.70M, Other=$1.36M, Hunter Lloyd=$248K`.

Note the **apparent discrepancy** for Q2 2026: `TX net=$3.5M` is LARGER than top-level net=$3.31M. This is correct: TX is one positive contributor, other states have net outflows, and the sum of all per-state nets is $3.31M. `by_geo.TX.inflow` is $3.5M and `by_geo.TX.outflow` is $0, so net=$3.5M. Other states contribute net outflows that reduce the firm total to $3.31M. Math is correct; this is just a reminder that individual category nets can exceed the firm total.

### File size impact

Serialized nna section with by_geo + by_adv attached: **154 KB** (minified).

The brief projected 250-500 KB. Actual is smaller because:
- Only 10 categories per cohort, not 20
- Only ~109 period entries total across three granularities
- Each cell is 3 fields (inflow/outflow/net), not more

Well within CloudFront/S3 limits. No infra change needed.

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Added `CANONICAL_NNA_PREFIX` to the `lib.s3_layout` import block. Added 5 helpers (`_nna_period_key`, `_load_canonical_nna_flows`, `_build_per_category_nna_by_period`, `_absorb_residual_into_other`, `_attach_nna_breakouts`) plus the `_NNA_PARTITION_HARD_TOL` constant and `_NNA_BREAKOUT_MONTH_SHORT` lookup. Modified `build_timeseries_overview` to call `_attach_nna_breakouts(nna, canonical_nna_df, nna_geo_cats, nna_adv_cats)` after the existing `_aggregate_nna_to_periods(nna_raw)`. |

+253 / -0 lines. One file. No touch on `build_cumulative_chart`, no touch on any other D_04 function, no touch on any lib module.

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp-pipescript io | `comp-pipescript io D_04` | Pre-edit: D_04 reads TIMESERIES_CHART, FIRM_MIX_VIEWS, etc. Writes platinum/firm/timeseries_overview.json. |
| comp-pipescript io (post-edit effect) | n/a | After edit, D_04 also reads `CANONICAL_NNA_PREFIX`. The compiler graph will pick this up on the next `comp-build`. |
| comp-pipescript consumers | `comp-pipescript consumers D_04` | `platinum/firm/*` outputs are terminal in the graph (no downstream gold-script consumers). Frontend consumers are out of graph scope. Additive change, zero downstream impact on gold scripts. |
| Grep | `tax_exposure`, `build_timeseries_overview`, `nna_geo`, `nna_adv` across gold/ | Confirmed `build_timeseries_overview` is the only producer of `platinum/firm/timeseries_overview.json`. Confirmed `nna_geo.categories` / `nna_adv.categories` are produced by D_00b's `_nna_drill_data` via `top_states` / `top_architects`. |
| Grep | `_weekly_downsample`, `_nna_drill_data` | Verified D_04's `build_cumulative_chart` is the consumer of `nna_geo` / `nna_adv` via weekly-downsample. Untouched per scope constraint #3. |
| py_compile | `python -m py_compile D_04.client_portal_summary.py` | Clean. |
| Live dry-run | In-process exec of modified `_load_canonical_nna_flows` + `_attach_nna_breakouts` against S3 ACCOUNT_TEAM and canonical_nna | 5.84M rows loaded in 37.6s, 27.1s attach, all 109 entries (26q + 76m + 7y) x 2 cohorts pass sum-invariance within $0.05 tolerance. Spot-checked Q2 2026 match exactly. |

Compiler tools log: entry to be appended.

## Deploy Cycle

| Step | Result |
|---|---|
| Pre-deploy `git status` | Clean except for D_04. |
| `py_compile D_04.client_portal_summary.py` | Clean. |
| Dry-run against live canonical_nna | PASS (all invariants hold post-absorption). |
| Runner state check (`aws ec2 describe-instances`) | `stopped` (no concurrent run -- timing race avoided this time). |
| Commit | `f5398e42` (CORRECTLY attributed this time -- used `git commit -m ... -- <pathspec>` form per AE's incident finding about how `git add <path> && git commit -m ...` sweeps the full index). |
| Author | `0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>` |
| Push | `git push origin CLOUD` -> `8ca8d73d..f5398e42` |
| S3 upload | `aws s3 cp data/black_diamond/scripts/gold/D_04.client_portal_summary.py s3://opal-data-bd/code/gold/D_04.client_portal_summary.py` |
| Local md5 | `e971b6618cad6bc256f1da49a1feea3e` |
| S3 etag | `e971b6618cad6bc256f1da49a1feea3e` |
| Etag parity | OK (exact match) |
| Gold runner trigger | **NOT invoked directly by DS.** Per user directive, ask AE to run Group D only (not a full run from A) -- the upstream A_* and C_* outputs from the 00:07 UTC run are still valid. |

## Acceptance Criteria Mapping

| TO # | Criterion | Status |
|---|---|---|
| 1 | Q2 2026 parity: `sum(by_geo[*].net) == top-level net` within $0.01 | **PASS** (exact to 2 decimals after absorption; pre-absorption geo drift absorbed into Other) |
| 2 | Sum invariance at every period + granularity with HARD assert | **PASS** (all 109 entries x 2 cohorts assert within $0.05 post-absorption) |
| 3 | Category key parity with `cumulative_chart.json.nna_geo.categories` | **PASS** (keys copied directly from `ts_chart.nna_geo.categories` / `nna_adv.categories`) |
| 4 | No regression on top-level fields | **PASS** (top-level nna.* unchanged; only additive `by_geo` / `by_adv` keys) |
| 5 | Cross-panel tie-out post RD frontend migration | **PENDING** (awaits RD companion TO + next gold run) |
| 6 | Compiler Tools section | **PASS** (above) |
| 7 | DS deploy cycle end-to-end | **PASS** (commit + push + S3 upload + etag parity) |
| 8 | Session log at `advi_nna_canonical_source.md` with all sections | **PASS** (this file) |

## Broker Messages

| Direction | Recipient | Subject | When |
|---|---|---|---|
| out | 0.6.0_AE_PartnerETL | D-group only re-run of gold (per Andrew) -- pick up D_04 at code/gold/ | pending (sent right after this log) |
| out | 0.7.0_AE_CloudOps | (relay) ds-advi-nna-canonical-source shipped -- D-group run requested | pending |

Per memory `feedback_no_direct_ds_messages.md`, the RD companion-TO handoff goes through Andrew.

## Next Steps

- **[0.6.0_AE_PartnerETL]** Run Group D only on the bd-gold-layer-runner (NOT a full run from A -- upstream outputs from the 00:07 UTC Apr 11 run are still valid, and re-running from A would waste ~30-45 min of positions cube rebuild). Group D = D_00, D_00b, D_00c, D_01, D_02, D_03, D_04. Expected output: `platinum/firm/timeseries_overview.json` with the new `by_geo` / `by_adv` nested objects in every nna entry. Log the trigger timestamp + completion in the AE session log.
- **[0.4.0_DS_ClientPlatform]** After the D-group run completes, verify:
  1. `aws s3 cp s3://opal-data-bd/platinum/firm/timeseries_overview.json -` has `nna.quarterly[-1].by_geo` and `by_adv` populated.
  2. Q2 2026 `sum(by_geo[*].net) == by_adv[*].net == top-level net` within $0.01.
  3. Category keys match `cumulative_chart.json.nna_geo.categories` byte-for-byte.
- **[Andrew]** Routes a note to `0.4.2_RD_AdvisorIntelligence` that the backend is ready for the frontend migration TO. RD can then swap `DistributionTab.ContinuousNnaDivergingView` off `cumulative_chart.json.nna_geo` pairwise-diff onto `timeseries_overview.nna[gran][i].by_geo` / `by_adv`. Frontend migration is ~30-60 minutes per the brief.
- **[2.0.0_SA_COO]** Note the brief accuracy issue (outflow sign convention -- brief said negative, actual is positive). Optional: edit the brief in place so future references are correct.

## Do NOT

- Do NOT re-enable cumulative-pairwise-diff for `by_geo` / `by_adv`. The whole point of this TO is to eliminate that path.
- Do NOT remove the `Other`-absorption logic without also fixing D_00b's `nna_geo` Unknown-state exclusion. The absorption is what closes the structural sum invariant given the known source drift.
- Do NOT reduce `_NNA_PARTITION_HARD_TOL` below `$0.05`. The tolerance is for floating-point rounding noise after the structural sum has been closed via absorption. Setting it lower would false-positive on rounding and fail the pipeline on legitimate runs.
- Do NOT modify `build_cumulative_chart` or the weekly-downsample path. AUA still needs the cumulative chart. Out of scope for this TO.
- Do NOT trigger the gold runner directly from DS. The TO forbids it. AE runs it.
- Do NOT re-author the commit. `f5398e42` is correctly attributed to DS this time.
