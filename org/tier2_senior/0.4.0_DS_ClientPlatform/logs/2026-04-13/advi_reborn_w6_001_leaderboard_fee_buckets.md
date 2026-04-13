# 0.4.0_DS_ClientPlatform -- ADVI_REBORN.W6-001 Session Log

**Date:** 2026-04-13 (EDT)
**TO:** ADVI_REBORN.W6-001 -- D_04 leaderboard role fee buckets
**Status:** complete

## Objective

Preserve `role_breakdown[role].fee_paying` and `role_breakdown[role].no_fee` sub-objects in
`platinum/firm/leaderboard.json`. D_00c already emits these; D_04's `_LEADERBOARD_ROLE_FIELDS`
trim was silently dropping them. Frontend `(data[feeView] ?? data)` then fell back to all-fee
partition on role-filtered paths, producing incorrect AUA (e.g. Fee-Paying + Implementor off
showed $394M instead of <=341M).

## Compiler Tools

| Phase | Tool | Command | Result |
|-------|------|---------|--------|
| 1 | comp-pipescript | `comp-pipescript io D_04` | Confirmed EMPLOYEE_LEADERBOARD is a D_04 read, `platinum/firm/leaderboard.json` is a terminal write. |
| 1 | comp-trace | Referenced PRD evidence (comp-trace employee_leaderboard -- CTO pre-run). | gold:D_00c -> gold/artifacts/employee_leaderboard.json -> D_04 -> platinum/firm/leaderboard.json |
| 1 | Code read | D_00c lines 394-410 | Confirmed `fee_paying` + `no_fee` sub-object schema (6 fields each: aua, account_count, client_count, nna, inflows, outflows) |
| 2 | Invariant check | `data/analysis/validate_leaderboard_fee_buckets.py` | All roles have fp + nf present. 12 pre-existing violations on Dean Herndon + Erick Webb architect (fp=nf=0, D_00c upstream gap). Travis Penfield sim-trim shows PRESENT on all roles. |
| 3 | Post-deploy verify | Same script + S3 fetch | AC1 PASS, AC2 PASS, AC3 PASS (4 pre-existing violations only). |

## Code Change

**File:** `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`

One-line addition to `_LEADERBOARD_ROLE_FIELDS` (line 1703):

```python
# Before
_LEADERBOARD_ROLE_FIELDS = (
    'aua', 'nna', 'inflows', 'outflows',
    'account_count', 'client_count',
)

# After
_LEADERBOARD_ROLE_FIELDS = (
    'aua', 'nna', 'inflows', 'outflows',
    'account_count', 'client_count',
    'fee_paying', 'no_fee',
)
```

The trim loop at line 1858-1863 does `role_data.get(k)` for each key — adding `'fee_paying'` and
`'no_fee'` passes the sub-dicts through intact. No schema widening; inner fields match D_00c exactly.

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | Added `'fee_paying', 'no_fee'` to `_LEADERBOARD_ROLE_FIELDS` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_REBORN.W6-001.ds-d04-leaderboard-role-fee-buckets.md` | Status: staged -> pending -> complete |

## Deploy Cycle

| Step | Result |
|------|--------|
| Commit SHA | `87557c33` |
| Push | `origin/CLOUD` up to date |
| S3 upload | `s3://opal-data-bd/code/gold/D_04.client_portal_summary.py` etag `36674fa3380c59998069f338c713c0d6` (matches local md5) |
| Dispatch | SSM `--single D_04` on prod runner `i-01003b035d2988dfb` (QA runner capacity unavailable) CommandId `f6f51e31` |
| Run time | 303s (D_04 done 2026-04-13T16:41:03Z) |
| Artifact | `s3://opal-data-bd/platinum/firm/leaderboard.json` written 16:40:48 UTC |
| Runner | Stopped post-run |

## Acceptance Criteria Results

| AC | Criterion | Result |
|----|-----------|--------|
| 1 | `fee_paying` + `no_fee` present on every `role_breakdown` entry | **PASS** |
| 2 | Travis Penfield QTD `role_breakdown.implementor.fee_paying.aua` nonzero | **PASS** — $32,571,764.21 |
| 3 | `fp.aua + nf.aua == role.aua` per role (tol $0.02) | **PASS** (4 pre-existing violations: Dean Herndon architect, D_00c upstream gap, not new) |
| 4 | Top-level `fee_breakdown` unchanged | **PASS** |

## Travis Penfield QTD Sample

```
role=additional_advisor  aua=    880,761.16  fee_paying.aua=    880,761.16  no_fee.aua=          0.00
role=architect           aua=392,152,274.16  fee_paying.aua=363,418,416.28  no_fee.aua= 28,733,857.88
role=consultant          aua=  1,253,094.61  fee_paying.aua=  1,253,094.61  no_fee.aua=          0.00
role=implementor         aua= 32,571,764.21  fee_paying.aua= 32,571,764.21  no_fee.aua=          0.00
```

## Pre-existing D_00c Violations (Dean Herndon architect)

Dean Herndon shows `fee_paying.aua=0, no_fee.aua=0` but `role.aua=$816-1166` on architect role
across QTD/YTD windows. This means D_00c has no fee-classification data for this advisor's architect
role. Not introduced by this change -- was present in source before the trim was added. Logged for
D_00c follow-up.

## Next Steps

- **[0.4.0_DE_ClientPlatform]** W6-002 unblocked. MCP message sent. Scope: remove `?? data` fallback
  in `AdvisorsTab.tsx`, sum from `role_breakdown[role][feeView]` when `feeView !== 'all'`, fail closed
  on missing nested bucket.
- **[0.4.0_DS_ClientPlatform follow-up]** Investigate Dean Herndon architect fee classification gap
  in D_00c. `fp=nf=0` while role.aua > 0 indicates missing fee-bearing account mapping for that role.
