# D8 TO-C -- AUTH-SURFACE RULING, 1.0.0_SA_CTO, 2026-08-19 ~20:59Z (lands ahead of the running build's claim-check finalization)

**Context:** Andrew ranked D8 into the freed sitez slot (@f45e5db124); TO-A is building toward
its claim-check finalization, which this ruling gates (MSTR nudge 205746Z). Editor SET is
already Andrew's word (all-approved ruling 5: ALL-INTERNAL); this ruling settles the CLAIM
SHAPE and its sufficiency.

## RULING

1. **The write-path predicate is the SERVER-SIDE JWT claim `firmId == 'opal-capital'`** --
   the existing internality predicate (AuthContext.tsx:551-553 client-side is ADVISORY ONLY;
   the PUT handler re-derives it from the VALIDATED token, never from any client flag or body
   field). This predicate is exactly coextensive with Andrew's all-internal editor ruling BY
   CONSTRUCTION -- no new claim, no new tier, rung-2 reuse.
2. **Riders, binding on TO-A's claim-check:**
   (a) `updated_by` is stamped FROM THE TOKEN's subject, never from the request body (a
   caller-supplied identity field is the stamps-never-checks class the estate already carries
   as a standing finding);
   (b) token validation rides the EXISTING auth chain for scoped routes -- no bespoke
   verification path;
   (c) the 403 is EXERCISED with a non-employee token in Phase 3 (already on the TO face --
   confirmed as the test that can fail);
   (d) 403 on the API even where the UI hides the affordance (the API never relies on the UI).
3. **Future-narrowing note, so nobody re-opens this:** if the editor set ever narrows to
   admin-only, the check swaps to the admin claim at the same chokepoint -- one predicate
   swap, no schema or table impact (the store's audit fields already carry who).
4. **Scope guard:** this ruling covers the D8 content-store write path ONLY. It is the same
   auth doctrine D6 references (server-side, never model/client-trusted) and changes nothing
   there.

**Effect:** TO-A's claim-check finalization is UNBLOCKED. Ferry via MSTR to the executing
sitez seat. -- 1.0.0_SA_CTO
