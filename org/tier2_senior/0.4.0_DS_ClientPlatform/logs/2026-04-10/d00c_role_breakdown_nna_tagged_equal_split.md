# D_00c role_breakdown NNA -- tagged canonical equal-split

**Date:** 2026-04-10
**Agent:** 0.4.0_DS_ClientPlatform
**Trigger:** Andrew ad-hoc. Advisor Profile -> Role Composition donut showing -$16.9K total NNA for Chase Bertrand QTD while Summary Flows panel shows +$1.20M. Individual role slices also failing to reconcile.

## Summary

Fixed a two-source divergence in `D_00c.portal_leaderboard.py` where `entry.nna` (advisor top-level) was migrated to the tagged canonical-NNA path but `entry.role_breakdown[r].nna` was left on the legacy C_08 `advisor_fee_detail` path. Additionally, the tagged per-role helper was double-attributing full account NNA to every role an advisor held on an overlapping account (no equal-split analogue to the existing `_weighted_aua` treatment), which would have caused sum-of-slices to exceed the advisor-level total even after the data-source fix.

Resolution: teach `_compute_tagged_window_metrics_by_role` to honor an optional `weight` column on `advisor_role_pairs`, compute `_split_weight = 1 / n_roles_per_pair` inside `build_employee_leaderboard` (mirroring the existing `_weighted_aua` computation), and attach it to `advisor_role_pairs_fee` / `_nofee`. Replace `rd.nna / inflows / outflows` with `twm_fee + twm_nofee` (tagged canonical, equal-split) when the tagged-by-role partitions are populated; fall back to `rr.nna` (C_08) only when `fee_rate_history` is missing at build time.

Post-fix invariants (after the next gold run):

1. `entry.nna == sum(role_breakdown[r].nna for r in roles)` -- exact within rounding
2. `role_breakdown[r].nna == role_breakdown[r].fee_paying.nna + role_breakdown[r].no_fee.nna` -- exact within rounding
3. `entry.inflows == sum(role_breakdown[r].inflows)` and same for `outflows`
4. AUA treatment unchanged (already equal-split via `_weighted_aua`)
5. Top-level `entry.nna/inflows/outflows` values unchanged (additive fix, changes only the role breakdown attribution)

## Root Cause

Two separate NNA sources were in play inside `_employee_entries_for_window`:

| Field | Source | Code path |
|---|---|---|
| `entry.nna` (top-level) | `tagged_window_metrics[advisor]` | `_compute_tagged_window_metrics` joins `canonical_nna` with `advisor_account_pairs` (deduped to (advisor, account)) |
| `entry.role_breakdown[r].nna` (stale) | `window.groupby(['advisor','role'])['nna_daily'].sum()` from `detail` | C_08 `advisor_fee_detail` parquet -- fee-paying slice only, partial coverage |
| `entry.role_breakdown[r].fee_paying.nna` / `no_fee.nna` | `tagged_window_metrics_by_role_fee` / `_nofee` | Tagged canonical partitioned, but WITHOUT equal-split |

The code comment at lines 362-364 (pre-fix) described the inverted architecture: "top-level nna/inflows/outflows which are sourced from C_08 advisor_fee_detail -- the sub-buckets use the clean tagged path." An earlier migration flipped the top-level to the tagged path but did not propagate the same fix to `role_breakdown[r].*`. Comment also removed in this fix.

Secondary issue: `_compute_tagged_window_metrics_by_role` was used to populate the fee_paying/no_fee sub-buckets correctly (they sum to the full advisor-level tagged total at the ADVISOR level because `advisor_account_pairs` is deduped), but for PER-ROLE attribution it used `advisor_role_pairs_fee/nofee` which is (advisor, role, account_id) -- non-deduped on (advisor, account). Consequence: when an advisor holds two roles on the same account (~3.7% of accounts per the existing `_weighted_aua` code comment), that account's NNA was attributed in full to each role, so `sum(fee_paying.nna across roles) > fee_paying_total_for_advisor`. The new `weight` column closes this.

## Changes

### 1. `_compute_tagged_window_metrics_by_role` (D_00c.portal_leaderboard.py)

Added optional `weight` column support. After the `advisor_role_pairs.merge(acct_sum)` step, if a `weight` column exists on the joined frame, scale `nna/inflows/outflows` by it before the `(advisor, role)` groupby. Backwards compatible: when the column is absent the function behaves identically to before.

### 2. `build_employee_leaderboard`

Hoisted `n_roles_per_pair` computation out of the `if has_aua:` block so it is always computed. Added `melted['_split_weight'] = 1.0 / n_roles_per_pair`. When building `pairs_dedup`, carried `_split_weight` through and renamed to `weight` on both `advisor_role_pairs_fee` and `advisor_role_pairs_nofee`. The existing `_weighted_aua` line is preserved (now an explicit `if has_aua:` branch that reuses the same `n_roles_per_pair` variable).

### 3. `_employee_entries_for_window`

Reordered the per-role block so `at_role_fee / at_role_nofee / twm_fee / twm_nofee` are pulled from the dicts BEFORE the `rd = {...}` literal is constructed (they were previously pulled after). Added a `tagged_by_role_available` sentinel (computed once per call) and the new `rd.nna / inflows / outflows` path:

```python
if tagged_by_role_available:
    role_nna      = float(twm_fee.get('nna', 0.0))      + float(twm_nofee.get('nna', 0.0))
    role_inflows  = float(twm_fee.get('inflows', 0.0))  + float(twm_nofee.get('inflows', 0.0))
    role_outflows = float(twm_fee.get('outflows', 0.0)) + float(twm_nofee.get('outflows', 0.0))
else:
    role_nna      = float(rr.nna)
    role_inflows  = float(rr.inflows)
    role_outflows = float(rr.outflows)
```

Stale comment at lines 360-364 (describing the pre-migration inversion) removed.

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | `_compute_tagged_window_metrics_by_role` weight support; `_split_weight` in `melted`; `weight` column on `advisor_role_pairs_fee/_nofee`; `_employee_entries_for_window` rd.nna/inflows/outflows use tagged-by-role sum; stale comment removed. |

No schema change. `employee_leaderboard.json` field set is byte-identical (same keys, same order); only `role_breakdown[r].nna / inflows / outflows` values change and only for advisors where the current value is non-zero.

Also co-committed (pre-commit hook auto-staged previously-untracked analysis artifacts, unrelated to this fix): `data/analysis/nna_suppression_accounting_residual/*` (NNA suppression audit CSVs, parquets, scripts). Not part of the functional change; noted here for traceability.

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| RD frontend -- Role Composition reconciliation | `docs/briefs/rd-brief-role-composition-nna-tagged-split.md` | 0.4.2_RD_AdvisorIntelligence |

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript io | `comp-pipescript io D_00c` | Confirmed READS: CANONICAL_NNA_PREFIX, ADVISOR_FEE_DETAIL_PREFIX, ACCOUNT_TEAM, FEE_RATE_HISTORY, ACCOUNT_PERFORMANCE, CLIENT_DIMENSION, REL_ARCHITECT_LOOKUP. WRITES: EMPLOYEE_LEADERBOARD -> D_04. | No I/O change from this edit. Verified both sources the fix is reconciling (canonical_nna and advisor_fee_detail) are already in the READS set. |
| Grep | `role_breakdown` across `data/black_diamond/scripts/gold/` | Hit D_00c, D_02, D_04. D_00c is the only producer of the leaderboard role_breakdown; D_02 and D_04 consume/restructure different views. | Scope verified as D_00c-only for this fix. |
| Grep | `role_breakdown` across `portal/src` | Single consumer path: `AdvisorPublicProfile.tsx` RoleDonut component reads `entry.role_breakdown[r].{aua,nna,client_count,account_count}`; `AdvisorsTab.tsx` also reads `role_breakdown` for leaderboard filtering. | Used to size the frontend brief; RoleDonut is the only place displaying the NNA value today. |

`py_compile` on `D_00c.portal_leaderboard.py`: **OK** (pre-commit gate).

Compiler tools log: appended entry for this session.

## Deploy Cycle

| Step | Result |
|---|---|
| git status clean (pre-stage) | D_00c dirty as expected; staged explicitly |
| Commit SHA | `4f821b99c9468aeb5a96799e2f24759cae397f17` |
| Author | `0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>` |
| Push | `origin/CLOUD 702fbb91..4f821b99` -- up to date |
| S3 upload | `s3://opal-data-bd/code/gold/D_00c.portal_leaderboard.py` |
| S3 etag | `959dd3a4316815bbd98236ea5e08a7a7` |
| Local md5 | `959dd3a4316815bbd98236ea5e08a7a7` |
| Etag parity | OK (exact match) |
| Size | 40,595 bytes |
| S3 LastModified | 2026-04-10T22:44:30Z (18:44 ET) |
| Gold runner trigger | Not invoked -- Andrew will trigger the next bd-gold-trigger cycle manually |

## Verification Plan (next gold run)

After the next `bd-gold-trigger` cycle writes the updated `employee_leaderboard.json`:

1. **Chase Bertrand QTD reconciliation** -- verify `entry.nna` (-- should remain +$1.20M as before --) and `sum(role_breakdown[r].nna for r in active_roles)` match within rounding.
2. **Firm-wide spot check** -- pick 5 random advisors with multi-role overlap (any advisor with > 1 value in `role_breakdown` and any `fee_paying.nna + no_fee.nna > 0`), assert `entry.nna == sum(role_breakdown[r].nna)` within $0.01.
3. **Per-bucket invariant** -- for each (advisor, role), assert `role_breakdown[r].nna == role_breakdown[r].fee_paying.nna + role_breakdown[r].no_fee.nna` within $0.01.
4. **Non-regression on AUA** -- confirm `sum(role_breakdown[r].aua) == entry.total_aua` (should already hold pre-fix; we did not touch AUA logic, just reused `n_roles_per_pair`).

If any invariant fails, escalate to 0.6.0_AE_PartnerETL for diagnostic and rollback the commit. No rollback-blocker if we need to revert; the change is contained to D_00c and is additive-only from a schema perspective.

## Next Steps

- **[Andrew]** Trigger `bd-gold-trigger` (`mode=incremental` is sufficient; D_00c has order 300 so incremental reruns it after upstreams). Output: `employee_leaderboard.json` in `s3://opal-data-bd/gold/artifacts/`.
- **[0.4.2_RD_AdvisorIntelligence]** Read `docs/briefs/rd-brief-role-composition-nna-tagged-split.md` -- the brief covers the semantic change, the new invariants, a recommended one-line tooltip update for Role Composition, and a "wait for next gold run" activation note. No code changes required on the RD side for basic correctness; the existing `entry.role_breakdown[r].nna` read path auto-picks up the new values. Optional frontend polish items listed in the brief.
- **[0.4.0_DS_ClientPlatform]** On next session, run the verification spot checks above against the refreshed `employee_leaderboard.json` and append results to this log.

## Do NOT

- Do NOT hand-edit the `employee_leaderboard.json` in S3 to patch a stale copy. Re-run D_00c.
- Do NOT re-introduce the dual-source pattern (top-level tagged + role_breakdown from C_08). The single-source-of-truth is the tagged canonical path for both.
- Do NOT remove `_split_weight` equal-split without reverting the role_breakdown data source change simultaneously. Mixing "tagged full attribution" with "sum-reconciles-to-advisor-total" is mathematically impossible when overlap exists.
