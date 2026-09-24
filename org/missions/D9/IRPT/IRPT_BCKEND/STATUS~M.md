# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M` until 21:13:40Z (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-24T18:4xZ. Full history:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/STATUS.md` on the M branch.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` @2cacdd2cd2 (LOCAL; its base da6d4e9365 is on origin via N1) |
| Served holdings | 49F 5a25ae76 (index QC.bs6a5w); INF d32e50c6 (k9U4ucuT); COT dec293d6 (mSFR0vat) |
| Andrew-direct this lease | `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260924_184xZ_IRPT_FIRM_TAB_FILTER_AND_10K_ROUNDING.md` @af2dd7335d |
| Push state | LOCAL; shared pushes are 0.0.0_AB_MSTR's |

## Live thread

LIVE END TO END through the deployed API at all three firms, signed in:
- **INF:** Greene SIMPLE, READY on d32e50c6 (HAR 18:36Z).
- **49F:** Alison Horton IRA, READY on 5a25ae76, with the model leaf "Opal Ultra Long Term" (HAR 18:36Z).
- **COT:** Anna, READY on dec293d6 (HAR 14:17Z).

First failing hop is the SCREEN, on two portal defects owned by 2.0.0_SA_COO~D (msg 18:43Z):
- Amounts are rounded to $10K (`CategoryViewTree.tsx:360` via `DrillTree.tsx:316`).
- The firm tab refuses FIRM_BINDING (`global/firms.ts:53` sends the opaque firm id as `selected_tenant`).

## Goal criteria

| Criterion | State | Evidence |
|---|---|---|
| (1) signed-in journey, 49F / INF / COT | API EXERCISED at all three; screen FAILS SEMANTIC on the $10K grain; firm-tab path broken | VERIFY_HOLDINGS_GOAL_20260924.md addenda @2cacdd2cd2 |
| (2) every active 49F/INF account resolvable, or refused explicitly | 49F 5,908 with a model + 1,509 Client only + 37 refused (no custody at 09-22), 0 empty of 7,454; INF 624 + 251, 0 refused, 0 empty of 875 | HOLDINGS_ACCOUNT_CENSUS_49F_INF_20260924.json @acaa51635d |
| (3) COT soundness + window disclosed | disclosed in the receipts | COT_LABELLED_PUBLICATION_RECEIPT_20260924.json |

## Write claims

`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*` on the M branch. No code edit is open.

## Next proof

Once ~D lands both fixes on DEV: one re-walk HAR (Andrew's) showing exact amounts on the Holdings screen and a working
firm tab, read in place. Then /verify on all three criteria.

## Next list (enrichment, in order)

1. The re-walk above.
2. The 49F publication header could disclose its 37 directory-active refused accounts with a reason. That needs a
   republish under a CTO GO. It is low value while the directory is 09-17 (parked row 1).

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| M's viewer-aware `maintained_sources` seam (485b69c061), lost in a merge; Y's prospect submissions raise TypeError (Y 100843) | 2.0.0_SA_COO~P (`_scope` writer) | acceptance = `_scope/tests/test_maintained_viewer_sources.py` 27 of 27 (0 of 27 at CLOUD aa24bce1d0; M 100845) | RESTORED on P's branch @19b38e2f22 (LOCAL); ~M's read AGREES: 27 of 27, and 195 + 6 extraction-bound = 201 (M 19:0xZ). Deploy rides P's next ledgered irpt-ycharts-generate |
| Holdings screen: exact amounts + working firm tab | 2.0.0_SA_COO~D | portal DEV a65a8db5 (ls-remote read) | LANDED; Andrew walked it ~19:0xZ ("it looks great"); a firm-tab HAR is asked |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Served directory as_of_business_date reads 2026-09-17 at 49F and INF, 3 trading days behind the 09-22 publication, with the refresh schedule ENABLED | 2.0.0_SA_COO~P (directory surface) | ~P reads the refresh's _refresh manifests |
| Public reason for a selected account with no custody row: NOT_READY today, which reads as transient; NOT_FOUND (`_authz/errors.py:58`) is the closest member of the enum. It is a contract choice and a served-code deploy | 1.0.0_SA_CTO (contract) | the CTO rules the code; ~M then builds it with the ledger entry + never-widen |
| The FULL -> FAST line to the CVO ("FAST from 18:1xZ; pins graded after the fact") | 2.0.0_SA_COO~M | 3.0.0_SA_CVO registers live |
| IRPT_BCKEND-S124: the bundle mint reads working-tree bytes | owner of .tools/safe_deploy_core.py | next bundle re-mint |

## Limits

The screen's correctness waits on ~D's two fixes. No CVO verdict on any criterion. No deploy by this seat this session.
