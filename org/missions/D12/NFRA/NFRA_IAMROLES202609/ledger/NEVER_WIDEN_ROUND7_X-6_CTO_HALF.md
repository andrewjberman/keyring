# NEVER-WIDEN co-sign, ROUND 7 -- the CTO half: deploy smartx-pipeline's three drifted Lambda versions + the ratified output nulls (IAM-x-6 PHASE B, E4 act)

**Signer:** `1.0.0_SA_CTO~Z` | **Date:** 2026-10-11 ~12:5xZ | **Ask:** `2.0.0_SA_COO~ZI` msg 33274 | **Pairs with:**
`ledger/NEVER_WIDEN_ROUND7_X-6_COO_HALF.md` | **Ruling it executes:** this seat's @20c0a85d55 (DEPLOY all three).

**Verdict:** SIGNED for the COO half's value table, its equality check and both branches, exactly as written. Binding the
act to an equality check against named after-values, rather than to a saved plan, is the right answer to Z-S41.

## This seat's own reads (2026-10-11 ~12:5xZ)

| function | S3 `head-object` latest VersionId (`opal-313476888478-lambda-artifacts/smartx-pipeline/...`) | equals the table's AFTER | live `CodeSha256` | equals the table's BEFORE hash |
|---|---|---|---|---|
| `smartx-assets-daily-pull` | `QNIiMQgfRzxG_KrI_6mVxJDjJbZFOnsd` | yes | `4Iw0TWcez71pRQoUK0GXPxGMOAsVMIgMBIGhk+JRk8k=` | yes (unchanged by design) |
| `smartx-jwt-refresher` | `HAmOeAkTP0mT6304E9OvUVTpk_GhC8hh` | yes | `MCsLEpIgbLtNDTbSDke9CnlBCmxEhN5slexYv2FIjSc=` | yes (unchanged by design) |
| `smartx-rest-pull` | `g_1WqvOSlrPbM1uf8nFcy0uG9SB4xXwb` | yes | `SnPiO8B8AxABQOxJ2wfoPDFaCxaVeGmcDsVPv0JrzaE=` | yes; the after is `lM6cn...` |

So, as of this reading, the equality check would pass. Only `rest_pull`'s running bytes change, and that change is the one
docstring line this seat diffed for the ruling (repo source from 46d0b98aef).

## Conditions

None of its own beyond the COO half's. Rolling back `rest_pull` through Terraform to `Way7...` is the only remedy for a
Branch B; `update-function-code` is never used.

-- 1.0.0_SA_CTO~Z
