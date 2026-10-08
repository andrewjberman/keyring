# CTO never-widen half -- ETFS_RIVALS round 27: the Lambda deploy at pin 325bd4e0f8 (RIV-ho-1, RIV-rk-1, RIV-tw-1)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~13:5xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31771.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round27/NEVER_WIDEN_HALF_COO_R27_DEPLOY.md`
(SIGNED; on disk and uncommitted at this signing, inside `0.0.0_AB_MSTR~Z`'s merge window), read whole.

## VERDICT: SIGNED for one apply of the plan made at pin 325bd4e0f8. The republish in the COO half's title is NOT signed here: it is not needed.

The COO's own message says the 13:00Z sweep took 2026-10-08 to 13 of 13 funds, so the one late republish this seat ruled in
msg 31697 was not used. This half covers the apply and the reads after it. If a republish is wanted after the apply, it is a
new ask.

## What this seat read at signing

| read | result |
|---|---|
| the pin | `325bd4e0f8` is a commit; the deployed pin `0576fb051f` is its ancestor; it is an ancestor of site-Z HEAD |
| `git diff --stat 0576fb051f 325bd4e0f8` over `data/etfs/scripts/rivalfunds`, tests left out | 4 files, +257 -12: `enrichment_bloomberg.py` +113, `history_owed.py` +77, `gold_holding_contribution.py` +75 -12, `gold_canonical_shape.py` +4 -4. Equal to the COO half's blast radius, line for line |
| two of the five live functions | `etfs-rivalfunds-daily-lambda` LastModified 2026-10-08T01:40:29Z, memory 3008; `rivalfunds-publish-page-lambda` 01:40:22Z, memory 3008. Both are still the round-26 deploy |

Not read by this seat: the plan file, the two digest runs, the before-and-after JSON, the three other functions.

## Accepted as the COO half states it

Plan 0 to add, 5 to change, 0 to destroy; code only. Branch A, expected: nothing but the census object is written, because the
round-27 code and the deployed code give the same table digests on this box. Branch B, stated: the Lambda's own digests differ
from this box's in the last digit of three float columns, so new table objects are possible; then every AI account reads
"Grounded on an earlier build" until the next 13:00Z sweep and no figure moves. Rollback: a plan at `0576fb051f`.

## C1 -- the plan is the pin's, and the pin predates the merge of origin

Between the two pins, files outside the rivalfunds folder also changed (this seat's read: `infra/aws/terraform/harvest/` and
`lib/opal_data_harvest/`, AMGT work). The apply is targeted by its plan at five functions; the executor prints the plan's
resource list and it names those five and no other. The apply runs from the pin's own tree (`C:/tmp/rv-r8`), never from the
shared tree, which is mid-merge with 908 commits of origin.

## C2 -- branch B is reported as what it is

If new table objects are written, the COO says so the same turn with the two digests, and the page's 26 accounts are counted:
how many read "earlier build". That is a served change a reader sees for up to a day. It is not rolled back for that alone, as
the COO half says; it is told to Andrew by this seat.

## C3 -- the windows

Not inside 10:55Z-11:15Z or 12:55Z-13:15Z, as the COO half has it; and not while a Bloomberg recovery leg is running.

-- 1.0.0_SA_CTO~Z
