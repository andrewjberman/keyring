# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M` until 21:13:40Z (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-24T18:4xZ. Full history:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/STATUS.md` on the M branch.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` @ebd3f237c5 (LOCAL; its base da6d4e9365 is on origin via N1) |
| Served holdings | 49F 5a25ae76 (index QC.bs6a5w); INF d32e50c6 (k9U4ucuT); COT dec293d6 (mSFR0vat) |
| Deployed reader | irpt-holdings; served code in opal-data-mdpf moved by the N1 push, origin 8a29069dea (MSTR 100810) |
| Push state | LOCAL @ebd3f237c5; shared pushes are 0.0.0_AB_MSTR's |

## Live thread

LIVE END TO END at COT and 49F (signed-in HAR 14:17Z, READY on the served revisions). INF: the signed-in hop is not
exercised. Andrew is walking the remaining firms now and will return a HAR.

## Goal criteria (verify addendum 18:4xZ @ebd3f237c5)

| Criterion | State | Evidence |
|---|---|---|
| (1) signed-in journey, 49F / INF / COT | COT EXERCISED; 49F EXERCISED on a Client-only account; INF NOT EXERCISED | VERIFY_HOLDINGS_GOAL_20260924.md addendum |
| (2) every active 49F/INF account resolvable, or refused explicitly | 49F 5,908 with a model + 1,509 Client only + 37 refused (NOT_READY), 0 empty of 7,454; INF 624 + 251, 0 refused, 0 empty of 875 | HOLDINGS_ACCOUNT_CENSUS_49F_INF_20260924.json @acaa51635d |
| (3) COT soundness + window disclosed | disclosed in the receipts | COT_LABELLED_PUBLICATION_RECEIPT_20260924.json |

## Write claims

`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*` on the M branch. No holdings code edit is open.

## Next proof

Andrew's returning HAR, read in place: one INF client READY on d32e50c6 with a model leaf, and one 49F account that
carries a model. Then /verify on all three criteria.

## Next list (enrichment, in order)

1. A refused 49F account shows NOT_READY. It should name "not covered": OBJECT_NOT_COVERED from the named vocabulary,
   at `holdings/snapshot.py` + `entry.py`. It is a served-code change: ledger entry + never-widen.
2. The 49F publication header discloses its directory-active refused population (37) with reasons. That needs a
   republish under a CTO GO.
3. Characterize the 11 refused accounts that the Black Diamond cross-reference places in the 0833 universe (custody
   present at 09-22, or not).

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Served directory as_of_business_date reads 2026-09-17 at 49F and INF, 3 trading days behind the 09-22 publication, with the refresh schedule ENABLED | 2.0.0_SA_COO~P (directory surface) | ~P reads the refresh's _refresh manifests |
| The FULL -> FAST line to the CVO ("FAST from 18:1xZ; pins graded after the fact") | 2.0.0_SA_COO~M | 3.0.0_SA_CVO registers live |
| IRPT_BCKEND-S124: the bundle mint reads working-tree bytes | owner of .tools/safe_deploy_core.py | next bundle re-mint |

## Limits

The INF signed-in read is not exercised. The screen render (taxonomy + drill) is the portal's (2.0.0_SA_COO~D). No
CVO verdict on any criterion. No deploy by this seat this session.
