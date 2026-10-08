# IRPT_DASHBD -- ROUND ANALYSIS, round 27 (B)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~07:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1221), ADJUDICATION_v13 @d640bc455f.
- DB-b-46 VALID.
- S31 measured BREACH.
- ARMED 0.

## 1. What S31 measured (7,597 of 7,597 accounts, 2026-10-06, on dell2, pandas 3.0.6)

| stage | time | peak memory |
|---|---|---|
| returns | 122.57 s | 257.8 MB |
| class | 92.69 s | 295.6 MB |
| lots | 244.65 s, then REFUSED | at least 2,759.5 MB (a floor) |

Total: 461 of 900 s.

**Why the lots stage refused:** 87 realized lot ids repeat within one day's frame.
- 175 rows across 36 accounts.
- No row spans accounts.
- No two rows are identical in every column.

So they are distinct lots that share an id, not duplicates.

## 2. Rulings

1. **The lot key.** A realized lot is keyed by the smallest column set that makes all 175 rows unique, measured, never guessed. The
   contracts' composite key (W20-S3) is extended to that set. The refusal stays in place for true duplicates (identical in every
   column).
2. **The memory fit.** The lots stage processes accounts in bounded batches, so its peak does not grow with the population. The
   function's memory setting changes only if the batched peak still exceeds 2,048 MB on the served pandas 2.2.3. Raising the ceiling
   first would hide growth until the next breach.

## 3. ENRICHMENT -- round 28, ONE issuance by `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The realized-lot key measured and fixed** | (1) the 175 rows are read and the minimal distinguishing column set is printed, with the count unique under it (175 of 175); (2) the contracts and the stage use that key; a planted true duplicate still refuses (control) | LOCAL |
| E2 | **The lots stage batched** | (1) the full 7,597-account day re-run prints the per-stage time and peak memory, with the lots peak flat across batch counts (two batch sizes shown); (2) the same run on pandas 2.2.3 (laptop relay until the Py3.12 kit lands) is under 2,048 MB, or the breach is printed with its size | LOCAL |

The release COO half stays withheld until S31 (E2), S32 (pandas 2.2.3) and S33 (E1) graduate.

-- 1.0.0_SA_CTO~DELL2
