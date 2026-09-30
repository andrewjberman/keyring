# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 07Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 07:0xZ | L10/L6 | 22->23 | round-22 analysis `a940eb6813` (msg 27004) READ |
| 07:1xZ-07:2xZ | L5/L6 | 23 | L5 measurement: the unmeasured share is **42.5%**, not 25% (LABEL 21,694; UNRESOLVED 9,595; POINTER 6,457 of 37,746; this seat's round-22 census missed the pointer class). The store holds no TWD line and no FX for TSM. ONE issuance `bbf33b05b4` (merged `46540fd5f6`): y-1 families to `~1`, y-2 `--no-sa-fallback` to `~2`, y-3 the anchor module to `~3`; y-4 is the issuer's ordered WORLD act. |
| 07:31Z | L7 | 23 | NO-OP: workers in flight |
| 07:4xZ-07:5xZ | L7 | 23 | y-2 merged `e727eaf6aa`; y-3 merged `9d4d373916`; y-1 merged `988d0ecfc7` (projected UNRESOLVED 9,595 -> 622; no_family 0; crncy 0); the anchor hookup `a3c4775d7c`, fail-closed; 168 passed |

## Rulings at L5

- The anchor module is its own file, so the write sets stay disjoint; its hookup is the issuer's at the merge.
- y-4's order is written into the decomposition (ruling 1): map, then re-derive, then dossiers.

## Compiler Tools

- The y1 census (issuer): before / after over the same 100 blocks, with the POINTER class added after the base run exposed it.
- `safe-merge.sh`: 4 merges. The peer-staged index held twice; waited, never touched.
- Gap: `safe-commit`'s refusal on a peer's staged index printed nothing my grep matched. Read the full tail before retrying.
