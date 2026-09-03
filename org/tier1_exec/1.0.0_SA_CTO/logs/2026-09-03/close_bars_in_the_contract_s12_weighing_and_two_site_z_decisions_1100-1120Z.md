# 1.0.0_SA_CTO -- 2026-09-03 11:00-11:20Z -- the close's two grading bars in the contract; S12 weighed; two site-Z decisions

Inputs (READ-acked): 2.0.0_SA_COO~A 93490 (S12's tool half is owned by PRD R11 / cells CG-s-6, CG-s-8 -- no route);
3.0.0_SA_CVO~A 93493 + 93500 (the closing cell tests FWD-2's negative limb vacuously; a REFUSED close, not a false one;
the bar lives in a message); 1.0.0_SA_CTO~A 93503 (the limb-coverage bar relayed to the contract owner); 0.0.0_AB_MSTR
relays 93515 (a pending lifecycle rule in the shared-infra plan) and 93520 (no steward-item carrier on the register);
93519 (the 49F ~09:46Z fire aborted at stage 1 on a missing silver partition -- COO/MSTR's thread).

## Acts
1. R6 STATE BAR, mechanical @105cbe8705: per outcome, the report's done_when_state vs the REALIZED grade's
   state_observed (APPLIED met by APPLIED/EXERCISED; EXERCISED only by EXERCISED; ABSENT meets nothing); refuses a CLOSED
   row citing a state below its card; 4 new arms, battery 38/38, live tree 0 violations.
2. LIMB-COVERAGE BAR in the contract @39c0d295ae: COMPLETION_REPORT.schema.json artifact_ref description + spine v2.5's
   close sentence -- a REALIZED grade cites artifacts covering EVERY limb of the ACCEPT clause; a control window that
   makes a limb true by construction is not evidence; an uncovered limb grades NOT_EVALUATED (R6 refuses). Stated as
   non-mechanical on purpose (judgment over prose). Form check 13/13. Broadcast to six seats.
3. S12 weighed (93484): the class is "a mandated lens with a WRITE side effect outside the face's bounds"; tool half =
   CLDGRPH's own cells (confirmed by COO~A from the record); gate half = a `mutates` field on the tool manifest BEFORE a
   preflight limb can read it -- a plan improvement carried by the round-2 step log, not built.
4. Site Z (93487/93527): the two D0 NFRA register items do not enter CLDGRPH (spine v2.4); (i) homed in the debt
   baseline beside (ii) under the same steward (MSTR's REC adopted); the pending ms-heat-snapshots-expire-60d lifecycle
   rule is NOT shipped as a passenger of an unscoped apply -- an expiry deletes objects, so it is Andrew's card; owner
   opens a change-management entry naming the hold; applies scoped away with an UNSCOPED re-plan as acceptance.

## Open, with owner
- Andrew: the lifecycle-expiry card (apply the 60-day expiry on ms-heat snapshots: yes/no).
- 0.8.0_AE_CloudComp / ~Z: the change-management entry for the pending rule; 0.0.0_AB_MSTR: the baseline entry.
- 2.0.0_SA_COO~A: the provoking-read test for FWD-2's negative limb at L6; 1.0.0_SA_CTO~A grades it.
