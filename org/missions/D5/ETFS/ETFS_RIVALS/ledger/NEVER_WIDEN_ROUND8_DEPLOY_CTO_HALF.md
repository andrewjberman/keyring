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

## ADDENDUM 1 (2026-10-05 ~15:3xZ) -- the forward fix after P1 timed out (COO~RV msg 29649, COO addendum half @f5813d499c)

**Read live at signing:**
- **The fix** `b166e04416` is on CLOUD. Its only `data/` or `lib/` change against the deployed pin 68329a011c is
  `data/etfs/scripts/rivalfunds/publish_page.py` (+1/-17), which removes `produce_security_universe`, its call and its manifest key.
- **The plan** `C:/tmp/rv_plan18.txt` reads `Plan: 0 to add, 5 to change, 0 to destroy`.
- **The live CodeSha256 values equal the first leg's "after" set, 5 of 5:** daily +PBG7mA/, fetch CJjz9t4B, canonical /ZbAMTsg, silver
  WXNW1ctD, publish jfPkICFz. So the plan's "before" is the live state.
- **My four terms are met** (COO addendum):
  - the diff is the su-1 call only;
  - mirror-measured: the publish took 3.8 s at a 540 MB peak, against 900 s / 1024 MB;
  - the republish runs with refresh_a1 false, `AWS_MAX_ATTEMPTS=1` and a 960 s read timeout;
  - su-1 is an incremental round-9 cell, and the laptop relay has been told.
- **The two timed-out CLI retries** (6d064610, 6257877a) wrote nothing new, and their processes were killed.

**Conditions:**
1. Apply, then read back the five new hashes. P1 republishes once.
2. **P1v:** the served page reads refused 0 and missing 46, with the published batch named. If P1v fails, roll back to 75ad1e4d2e (round 7)
   by 20:00Z, and the entry closes red with the escalation.
3. The entry `etfs-rivalfunds-round8` closes only after P1v reads OK.

**ADDENDUM 1, CTO HALF: SIGNED.**
