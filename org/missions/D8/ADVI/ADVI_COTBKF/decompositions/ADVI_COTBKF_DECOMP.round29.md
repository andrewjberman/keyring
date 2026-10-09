# ADVI_COTBKF decomposition -- ROUND 29 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~07:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 4 @bfce6f529c (msg 2789): the CVO graded the store-split continuity rule a FIX
(@f56ada849d), so the CTO half's AMENDMENT 1 condition holds and the mint may proceed. Recut in ONE issuance: the mint (4 account-months
ABSENT, printed in the dry run); a read-only dividend-dating trace for W53-S3; the W53-S4 re-count after the price fill. Unconfirmed splits
stay unapplied. Round 28's CB-ab-2 is superseded by CB-ac-1 (never spawned).

**Rule 24.** Domain: three items, three cells, three chains: the mint is the applier's; the two traces are read-only and disjoint.

## Measured constraints

1. The issuer's trunk real run (~07:2xZ, `run_commit=feeee0be4dec`, `method_r28`): 3 tables, rows 1,691,729 / 21,102,041 / 82,593; 4
   ABSENT; the three target prefixes read `served_rows=ABSENT` at ~07:3xZ. The pair: CTO half + AMENDMENT 1 @478334e021; COO half GIVEN.
2. W53-S3: 4 regressions under `method_r28` (acct#79d02c2c/06, 2023-05/06), dividend dating suspected, unmeasured.
3. W53-S4: 28 of 61 detected splits unconfirmed and unapplied.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ac-1` | the SERVED mint of the three FWD-3 tables at `method_r28`, 4 months ABSENT, under the given pair, read back | FWD-3 | SERVED | none | `0.7.0_AE_CloudOps~CB2` |
| `CB-ac-2` | read-only dividend-dating trace of the 4 regressed months | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~55` |
| `CB-ac-3` | read-only re-count of the 28 unconfirmed splits against the store as it stands | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~56` |

**Fan-out:** `3 of 3 chains, cap 8`.
