# ANDREW-DIRECT 2026-09-18 ~17:3xZ at the `2.0.0_SA_COO~B` terminal -- two `/open-calls` cards APPROVED

**Verbatim, in full:** *"Approved"* -- in response to the `/open-calls` queue printed at this lane (2 calls, 2026-09-18 ~17:3xZ).
The word answers the queue as presented; both cards carried a single (a)/yes recommendation, and "Approved" adopts each REC as
written. Nothing wider is read into it: no directive, no money, no vendor, no standing hold is touched.

## CALL 1 (was BLOCKING) -- APPROVED

**The call:** may the two missing firm buckets (`opal-data-inflection`, `opal-data-cottonwood`) be provisioned NOW, ahead of D14's
full migration?
**The REC adopted:** (a) yes -- provision the two buckets now through the LGIC builders (D14's own names, empty, no data moves), so
IB-rtd-7's port can be re-cut in round 5 while the legacy prefixes stay live until the readers cut over in one window.
**Scope, stated narrowly:** bucket CREATION only, at the builders' names (`lib/opal_naming.py name()` / the registry under
`infra/logic/registry/`), applied through `.tools/safe-apply.sh` under a change-management entry; NO object moves, NO reader
cut-over, NO retirement of a legacy prefix -- those stay IB-rtd-7's port under both never-widen halves and the IRPT_FNTEND
reader cell, in one window. The prior word *"legacy bd/inf/cot buckets are the ACTIVE channels until D14"* is not reversed:
the legacy channels stay active; two empty LGIC buckets exist beside them.

## CALL 2 (was CARRIED) -- APPROVED

**The call:** may a bounded TEST PRINCIPAL be created so FWD-1/2/5/11 can be exercised at a live session?
**The REC adopted:** (a) yes -- one firm-scoped test advisor identity with terminated-client visibility, created under a never-widen
sign-off (CTO+COO) and deleted at round close.
**Scope, stated narrowly:** ONE identity, ONE firm scope, created and deleted inside the round that exercises it; both halves name
its blast radius (which routes it can reach, which firm's data, and the deletion as rollback) before it exists; every exercise
against it is recorded by artifact hash (R-40). It is never a standing account.

## Execution route (the L10 order binds: slug -> the CTO's round-4 analysis -> the COO's recut)

Round 4's L8 packet is at `3.0.0_SA_CVO` (98015, 17:18Z); its slug and the CTO's round-4 analysis have not landed. A round-5
issuance cut before round 4's slug deadlocks round 4's L10 (LD-0521), so neither approval is CUT tonight by this seat. Both are
ROUTED the same turn:
- to `1.0.0_SA_CTO` -- to carry into the round-4 analysis as owed items (the bucket provisioning as a D14/LGIC-shaped cell or as
  the D14 owner's own act, the CTO's placement; the test principal as a round-5 cell gated on both halves), so this seat's recut
  serves them in ONE issuance;
- to `0.0.0_AB_MSTR` -- the reserved test-principal card it held for Andrew is ANSWERED; nothing further waits there;
- to `3.0.0_SA_CVO` and `2.0.0_SA_COO~F` -- for the record (the FNTEND reader cut-over is the same window as the port).

**Push state:** this record LOCAL; origin/CLOUD `ec5a7afd2b` (the CTO's 14:48Z ls-remote; not re-read here).
