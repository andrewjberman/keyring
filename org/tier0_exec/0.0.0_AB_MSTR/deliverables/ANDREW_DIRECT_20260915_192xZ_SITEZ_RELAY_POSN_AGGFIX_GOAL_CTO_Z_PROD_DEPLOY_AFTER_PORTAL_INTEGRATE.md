# RELAY 2026-09-15 ~19:2xZ (site Z) -- POSN_AGGFIX goal: validated completion, then a portal /integrate across both fabrics, then 1.0.0_SA_CTO~Z may run /prod-deploy

**Seat:** `0.0.0_AB_MSTR` (laptop), recording a SITE-Z Andrew-direct on this fabric at `0.0.0_AB_MSTR~Z`'s request
(agentbus 58740afd, 19:33Z). This is a RELAY record. The canonical record is site Z's:
org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_192xZ_POSN_AGGFIX_GOAL_VALIDATED_COMPLETION_THEN_PORTAL_INTEGRATE_THEN_PROD_DEPLOY.md
@15827b3991 (LOCAL on SITEZ at relay time).

## VERBATIM AND ENTIRE (given as a /goal at the 1.0.0_SA_CTO~Z terminal, as relayed)

> "see POSN_AGGFIX through to validated completion. At that point, have MSTR~Z coordinate on a portal repo /integrate
> merge so the repo updates are included on both fabrics. | Once this is done, you may run a /prod-deploy."

## WHY IT IS RECORDED HERE

- **A /prod-deploy by a CTO lane is not the normal route.** The skill is written for the DT seat, and on this fabric
  `1.0.0_SA_CTO~A` ran today's promote. His word authorizes `1.0.0_SA_CTO~Z` for this ONE deploy, at step 3 only, after
  steps 1 and 2. It authorizes no other seat and no other deploy.
- **Step 2 is a two-fabric act.** It needs this seat, as the laptop MSTR, as the other party. The portal /integrate
  runs the standard protocol: one resolution agreed on the bus first, per-hunk base ranges before any pick-versus-union
  call, named non-trunk branches on origin so both sides read the same bytes, and a loser-content audit on any pick.

## THE SEQUENCING, AGREED ON THE BUS (as 1.0.0_SA_CTO~Z recorded it and 0.0.0_AB_MSTR~Z reads it)

"Validated completion" resolves as follows:
1. Every outcome is graded before the promote.
2. The portal changes are built, verified locally and drained.
3. The page outcomes (FWD-1, FWD-2, FWD-3, FWD-9) are read on the SERVED page immediately after /prod-deploy.
4. The project closes on those reads.

## WHAT IT DOES NOT CHANGE

- The site-Z WORKSPACE push hold stands, and so does this fabric's CLOUD push hold. Both wait on Andrew's word.
- Portal non-trunk branches are a separate matter.
- The CLOUD<->SITEZ workspace merge still waits on his "yes, merge".
