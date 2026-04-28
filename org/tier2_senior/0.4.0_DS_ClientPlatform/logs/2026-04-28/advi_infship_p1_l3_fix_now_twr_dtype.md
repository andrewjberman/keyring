# Session Log -- 0.4.0_DS_ClientPlatform~C -- 2026-04-28 (FIX-NOW addendum)

**Lane:** ~C
**Project:** ADVI_INFSHIP P1.L3
**Session span:** ~12:35Z -- 12:53Z
**Trigger:** CTO+COO joint FIX-NOW dispatch 06:25Z (re-dispatched 12:35Z) — DS~B's L1 close-out flagged 2 alpha-shipped bugs
**Predecessor log:** `advi_infship_p1_l3_geo_emitter_and_max_twr.md` (alpha-ship 04:05Z)

---

## Bugs fixed

### Bug 1 — GRO TWR (MAX) emitted $72.9 TRILLION

**Symptom:** `platinum/firm/timeseries_overview.json#growth_decomposition_max_twr.total_market_twr = $72,915,791,421,110.89`. Would surface in DE B5/B6 panel reads; Andrew would see during V1 RD smoke. Ship-blocker.

**Initial root-cause hypothesis (WRONG):** Silver `twr_value` stores percent, not decimal as schema docs claim. Detect-and-convert proposed.

**Actual root cause:** Silver `twr_value` IS decimal as DS~A's schema docs correctly state (median 0.1151 = 11.51% verified empirically). The runaway came from BAD-DATA OUTLIERS — 4 accounts with malformed Orion API output:

```
acct 1416: twr=730.4259 (73,000% annualized) — closed account, ending_mv=$0 from beginning_mv=$188K
acct 674:  twr=-6.3062  — tiny acct, beginning_mv=$603, ending_mv=$904 (acct GREW but TWR is -630% — vendor data bug)
acct 517:  twr=-5.2135  — same pattern as 674
acct 184:  twr=3.4792   — tiny new acct, $0.02 -> $1.81, internally consistent but extreme
```

For acct 1416: `(1 + 730.4259)^3 ≈ 391,000,000` per-account multiplier × $188,882 beginning_mv = $73T pollution from one bad row.

**Fix:** Bounds guard `abs(twr_decimal) > 1.0 → exclude from $-weighted aggregate, emit in `_meta.bounded_out`. NO unit conversion (initial divide-by-100 attempt was wrong; reverted).

**Math sanity (post-fix, live silver):**
- total_market_twr: **$59,038,256** (vs residual $54,310,576, 8.7% methodology variance — plausible geometric vs arithmetic gap)
- 848 accts kept, 4 bounded out (0.1152% of beginning_mv excluded — negligible)
- twr_unit_handling = 'decimal'

### Bug 2 — Lifecycle merge dtype WARN (object vs float64)

**Symptom:** Pandas WARN on `_compute_hh_lifecycle` line 818 merge. Indicates dtype mismatch that could bite edge inputs.

**Root cause:** `_compute_hh_lifecycle` builds `adim` from either:
- `accounts_dim` (household_id is float64 — `pd.to_numeric` in INF_A_00 to handle SCOPEFIX 'unknown' string-coerce)
- `accounts_v2_dim` (household_id is str per DS~A schema)

Downstream `hh.household_id` was cast to str via astype, but `win_inflows.household_id` (built from `acct_to_hh = adim[['account_id','household_id']]`) carried the source dtype unchanged → merge mismatch.

**Fix:** Cast `adim['household_id'] = adim['household_id'].astype(str)` immediately after the if/elif build branch. Propagates str dtype through `acct_to_hh` → `win_inflows.household_id` → merge → WARN eliminated.

---

## Implementation

### File changed
`data/orion/scripts/gold/INF_D_04.client_portal_summary.py` (+64 / -32)

### Diff highlights
- `_compute_max_twr_market`: removed unit-conversion (initial misdiagnosis); added bounds guard at `abs(twr) > 1.0`; restructured aggregate computation to use `j_bounded` (post-guard); added `account_count_input`, `account_count_bounded_out`, `twr_unit_handling` fields; replaced `_meta.outliers` with `_meta.bounded_out` to reflect new "excluded from aggregate" semantic vs prior "included with diagnostic" semantic.
- `_compute_hh_lifecycle`: one-line cast `adim['household_id'] = adim['household_id'].astype(str)` after if/elif.

### Compiler tools
| Phase | Tool | Result |
|---|---|---|
| Pre-commit | `.tools/ds-commit-gate.sh` | OK clean (py_compile + AST + ruff) |
| Local validation | `python data/orion/scripts/gold/INF_D_04.client_portal_summary.py --upload` | Runs against live silver; 4 accts bounded out; market_twr=$59.0M sane |
| Post-publish | manual S3 fetch + JSON inspect | growth_decomposition_max_twr live and matches local computation |

---

## Commits

| SHA | Subject | When |
|---|---|---|
| `5293e48c` | fix(ADVI_INFSHIP.P1.L3): TWR $72.9T runaway + lifecycle dtype WARN — CTO+COO FIX 06:25Z | 12:43Z |

Pushed to origin/CLOUD via `git push origin CLOUD` (df4b3f86..5293e48c).

## S3 deploys

| File | S3 key | When |
|---|---|---|
| INF_D_04.client_portal_summary.py | `s3://opal-data-inf/code/gold/` | 12:44Z (85.9 KB) |
| timeseries_overview.json | `s3://opal-data-inf/platinum/firm/` | 12:46:17Z (54.5 KB) |
| partner_analytics_monthly.json | `s3://opal-data-inf/platinum/firm/` | 12:46:17Z (14.2 KB) |
| partner_analytics_quarterly.json | `s3://opal-data-inf/platinum/firm/` | 12:46:17Z (10.2 KB) |
| partner_analytics_annual.json | `s3://opal-data-inf/platinum/firm/` | 12:46:17Z (8.6 KB) |

Re-publish via local `python --upload` (COO authorized "Local exec or QA-runner once primitive lands" in fix-now dispatch).

---

## RAVCs Sent

| When | To | Subject |
|------|----|---------|
| 12:36Z | 2.0.0_SA_COO | RAVC2 ACK PICKUP — root cause analysis (initial: percent-vs-decimal hypothesis) |
| 12:47Z | 2.0.0_SA_COO | RAVC4 SHIP — corrected root cause (bad-data outliers, NOT percent drift); live metrics + bounded_out diag |

COO RAVC ACK 12:53Z accepts: root cause correction, live metrics, DE B5/B6 unblock confirmed.

---

## Operational flags surfaced (NOT in fix scope)

1. **Live canonical_holdings appears stale.** Live geo view total = $91.8M / 295 HH / 781 accts. My local mock-test against unified_account_dim gave $199.4M / 308 HH / 852 accts. Likely cause: `B_00.canonical_holdings.py` not yet re-run post-SCOPEFIX. Routed to DS~A as canonical owner per COO's MCP.

2. **`_meta.outliers` → `_meta.bounded_out` semantic shift:** prior alpha-ship had outliers diagnostic-only (included in aggregate per DS~A's policy). FIX-NOW changes to bounded-out (excluded from aggregate). DS~A's policy was correct for normal-distribution outliers but didn't account for malformed-source-data outliers. Worth surfacing to ~A as a policy refinement: "outliers from data quality issues should be EXCLUDED, outliers from real but extreme data can be INCLUDED with diagnostic". Current implementation conservatively excludes all `abs(twr) > 1.0` — won't materially distort firm aggregate at 0.115% beginning_mv share.

---

## Pending / Next

| Item | State | Owner |
|---|---|---|
| AE chain re-dispatch (production rebuild after canonical_holdings refresh) | Pending | AE 0.6.1 / DS~A coordination |
| DS~B vs ~A vs ~C lane re-validation post canonical refresh | Pending | depends on chain |
| Live RD smoke (V1) | Pending | RD 0.4.2 |
| Andrew sign-off (V2) | Pending | Andrew |

Watcher: `bedo22lgc`. Idle.
