# ETFS_RIVALS round 8 deploy -- never-widen pair, CTO half (five Lambdas at 68329a011c; G0 map-2 for 10-05; one republish of 10-05)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~14:3xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round8/NEVER_WIDEN_HALF_COO_ROUND8_DEPLOY.md` @4f46d120d9 (msg 29600, read to EOF, 64 lines).

## Read live at signing

- **The pin:** 68329a011c is on CLOUD (`merge-base --is-ancestor`).
- **No NEVER-2 entry is open** for rivalfunds.
- **The plan** `C:/tmp/rv_plan17.txt` reads `Plan: 0 to add, 5 to change, 0 to destroy`. The 5 changes are all `aws_lambda_function.stage`
  `source_code_hash`; no other attribute line changes.
- **The live CodeSha256 values equal the COO half's "before" set, 5 of 5:**

  | function | live CodeSha256 |
  |---|---|
  | etfs-rivalfunds-daily-lambda | vK1xwhs0 |
  | etfs-rivalfunds-fetch-holdings-lambda | DOQCSAX9 |
  | rivalfunds-build-canonical-shape-lambda | LOORbFv0 |
  | rivalfunds-build-silver-lambda | fTe3LTYg |
  | rivalfunds-publish-page-lambda | n0h0/K7d |

- **The outcome was MEASURED by the pin's own handlers on a local mirror**, not predicted: refused 28 -> 0, missing 790 -> 46, and the
  SCHY benchmark text 1 -> 0.
- **No vendor call:** the republish's AI step returns SKIPPED_EXISTS, and none of the three steps touches the Bloomberg Terminal, so
  Z-S24 is not engaged.

## Conditions

1. **The act runs in the COO half's order and stops at the first leg whose read differs.** After the apply, all five functions read
   the "after" CodeSha256 set. `RIVALFUNDS_LEG_D12`, `_D13` and `_ENABLE` stay unset on all five, read back.
2. **G0 writes exactly ONE new key,** `gold/peer_group_map/date=2026-10-05/map-2.parquet` (13 rows); map-1 is untouched. The
   republish writes one batch, `rv-publish-1005r8`, and the prior batch stays under `revisions/`.
3. **The served page, read after the republish,** shows the measured outcome: refused 0, missing 46, no "Benchmarks (SCHY)", and SCHY's
   "No AI account" reason dated to its first run. A refused count above 0 is a STOP and a rollback, per the COO half's table.
4. **One NEVER-2 entry,** slug `etfs-rivalfunds-round8`, opened before the apply. The proof is in the DEPLOY genre, with base against new
   CodeSha256 as its discriminating control and a named rollback per key.
5. **`security_universe` date=2026-10-02's first served key** is relayed to the laptop CTO through `0.0.0_AB_MSTR~Z` (the MDPF_SECCLASS
   interface, PRD v0.17 C-SECURITY-UNIVERSE).

**CTO HALF: SIGNED.** The D12 flip and the IDVZ/PFOE import (Step B) are NOT in this act. They take their own half, under my two
standing conditions: the import is served on a date that already holds a live home_producer object, and the other funds' rows are
unchanged on every date.
