# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-pp-6: applied, found a unit error, rolled back in 13 minutes

**Date:** 2026-10-11 (GO 07:24Z; apply 07:37:03Z; CTO [STOP] 07:47Z; rollback 07:50:33Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-pp-6.redeploy-the-scoped-api-carrying-the-rounds-served-cells
**Status:** NOT COMPLETE -- applied, then ROLLED BACK on the CTO's STOP and the issuer's order; live is the pre-pp-6 package

## Objective

One code redeploy of `opal-amgt-scoped-api` at pin 62c242efc4 carrying pp-1's exact-name identity arm (24 members),
oo-5's inert `price_currency.py` and nn-5's `crosswalk.py` by blob.

## The act
**archetype:** DEPLOY

1. Read both halves with addenda, the order and the producer; verified the pin (ancestry, 4 of 4 blobs, pp-4 absent),
   the live peers partition (still `2026-10-11T0707Z`) and the base: AC3 NO with 24 candidates and 0 served.
2. Captured the rollback package from the live function (hash equal) and the `/peers` response of all 243 subjects.
3. Built at the pin (the first attempt stopped on an unset `AMGT_DEPLOYED_ZIP`; the second ran offline with
   `PIP_NO_INDEX=1`). Whole diff: CHANGED 7, ADDED 0. 4 by blob; 3 (`opal_naming.py` and two registries) admitted by the
   table's "other projects" row with the closure reason printed. Uploaded, graded the plan from JSON (1 of 53), applied.
4. AC1-AC3 PASS. The 243-subject compare then showed the 24 members ALSO moved `price_currency`, which the signed text
   did not predict. Reported (msg 3620); the CTO ruled KEEP (msg 3622) on the exchange currency.
5. The issuer read the live routes and found 12 UK members served `GBp` beside prices in pounds, a 100x unit error. The
   CTO withdrew KEEP with a [STOP] (msg 3628) and the issuer ordered the rollback (msg 3630).
6. Rolled back with the kept zip: upload, one `safe-apply`, CodeSha256 `l8egBo/rf..`, re-plan rc=0, compare 0 of 2230
   members changed, AC2's arm YES, record step committed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | two entries: pp6 (11 legs), pp6-rollback (4 legs) | PASS | a closed entry is not reopened; the rollback has its own |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | needs AMGT_DEPLOYED_ZIP; PIP_NO_INDEX for an offline build |
| terraform show -json / safe-apply.sh | both applies | PASS | 1 of 53 moving each time |
| 243-subject /peers compare | base vs post, twice | PASS | found the currency move; proved the rollback |
| r89 / r91 checks | AC2, AC3 | PASS | AC3 reads YES only while pp-6 is live |

**What worked:** a member-by-member baseline of every subject's response, which found what three PASSing criteria did
not; a named, kept, hash-checked rollback that ran in minutes.
**What failed:** my read of the currency. I compared served values with the record and called them consistent with the
156 base members; I did not check the unit against the price. Exchange right, unit wrong is still wrong, and the CTO's
ADDENDUM 2 says the same of its own read. A criterion of "the label matches the figure's unit" was in no one's checks.
**Gap found:** the GBp unit error already exists on about 5 UK base members (CTO). Round 92's cell covers it.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not roll back on my own at 07:50Z when I found the currency move | the pair's expected outcome was wrong, not the code; I judged KEEP and asked. That judgment was incomplete (no unit check); the ask is what let the CTO and issuer correct it inside the hour |
| Opened a second ledger entry for the rollback | the first was closed on the KEEP ruling; closed entries are not reopened |
| Wrote no proof instance and did not flip the order | the end state does not satisfy AC1 or AC3; the disposition is the issuer's |

## Files Modified

- `org/critical_paths/change_management/20261011T0729Z_amgt-resapp-r91-pp6-scoped-api-dell1_deploy_completion.md` (CLOSED)
- `org/critical_paths/change_management/20261011T0749Z_amgt-resapp-r91-pp6-rollback-scoped-api-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the currency finding and the 24-row compare
- the order's `<status>` (rolled back, not complete)

## Next Steps

1. `[2.0.0_SA_COO~R1]` Disposition of pp-6; round 92's one cell is pp-1 plus the unit-aware currency guard, measured
member by member before the pair is signed. 2. `[1.0.0_SA_CTO~DELL1]` The same cell fixes the base's UK members and the stale
reason text. 3. `[box-sync / MSTR]` Push the local commits.
