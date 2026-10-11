# ADVI_COTBKF decomposition -- ROUND 58 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~05:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 4131, answering round 57 (CB-be-1, drained @e54f2086f5; packet @6edfe081c7).
- Round 57 read the stored bond close as DIRTY on the coupon-date fall, so method row 3's income basis is false for a bond priced
  from that store. 0 of 107,316 measured account-days hold a Fixed Income CUSIP (the worker's count; CB57be1-AC2 is with the CVO).
- The CTO: the CB-al-2 pair may stamp `method_version` 3 on the measured rows, on two conditions.
  1. The count is re-read AT THE MINT on the exact files minted, denominator printed. 0 mints; anything else stops.
  2. "Never measured from this store" needs a GUARD, not a sentence: a cell that refuses a measured row on a bond-holding day under
     `method_version` 3, with a test. Until the guard is in the tree the pair says "no minted row", not "never".

**Rule 24.** Domain: the two conditions -> one cell, both in the one adapter this project owns.

## Measured constraints (issuer)

1. **The adapter is `data/assets/scripts/silver/commonwealth_account_return_daily.py`** (618 lines): `build` makes the day files,
   `apply_days` is the guarded mint, `verify_served` reads back. The local day files live under the BASE checkout's
   `.scratch/advi_cotbkf/ard_cottonwood_r47` (3,325 day directories), not in a worker worktree.
2. **The bond rule is round 57's:** silver transactions `Asset_Type == 'Fixed Income'` (`commonwealth_transactions.py:53`).
3. **No S3 write, no deploy.** The mint itself stays HELD on its pair. The apply path gains a refusal; it is not run.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bf-1` | the adapter counts measured rows on bond-holding days over the exact files of a manifest (0 or it stops, at the mint too), and its build refuses to measure a bond-holding day under `method_version` 3 | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~85` |

**Fan-out:** `1 of 1 chains, cap 8`. DIRECT-ACT cell (one cell, under 300 product lines, LOCAL): its close is the one real run by
the issuer.
