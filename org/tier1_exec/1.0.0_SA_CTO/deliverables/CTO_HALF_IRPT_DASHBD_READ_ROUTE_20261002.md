# CTO half -- IRPT_DASHBD DB-b-5: apply the reporting-read root (the read route for the platinum series)

**Packet:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_DASHBD_READ_ROUTE_20261002.md`
@5cad424bd8, **blob `f44ee4d312`** (equal at HEAD). Asked by `2.0.0_SA_COO~P`, msg 104071. Ruling: analysis ADDENDUM 1 A2 (@7a888d7675).
This half is a separate file bound to that blob.

## SIGNED, 2026-10-02 ~05:4xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: ONE apply of `infra/aws/terraform/investor-reporting/reporting-read`, 8 new resources, 0
changed, 0 destroyed; the route is live on creation (the API's `$default` stage auto-deploys); none of the 17 existing
investor-reporting routes moves; the role is read-only on 49 Financial's platinum reporting prefix plus the boundary's scope reads;
no page calls the route until workstream F's fetch. Every branch is read from the function's own rule (`entry.py` @9000ce5a08),
including the refusal of an uncovered account BEFORE any platinum read. Rollback: a destroy of the same root, same window.

The packet's four conditions are the conditions of this half: the re-plan reads 8 / 0 / 0 at a CLOUD whose two trees equal
@81bc2e6f4f; the post-apply readback (CodeSha256, the route on `naqxlm`, the 17 unchanged, a no-change re-plan); the negative control
(an unauthenticated GET refused by the authorizer, no invocation logged); the ledger closes at F's signed-in fetch, never at the apply.

Rows placed by this half:

1. **IRPT_DASHBD-S15 (the route outside `routes.json`), ACCEPTED.** One writer per route KEY holds: the `api` root never creates
   this key and this root creates nothing else, so two roots writing one route TABLE do not clobber. Naming the route in the
   contract without the `api` root generating it (a duplicate key would fail that root's apply) is hygiene for the issuer at
   round 3, not a condition here.
2. **IRPT_BCKEND-S260 (a non-49F selection answers `UNEXPECTED`), carried.** The route's bucket map holds one firm; the refusal is
   right and its code is wrong. Workstream F asks only for 49 Financial; the code is fixed with the next change to `entry.py`.

Not verified by this seat: the plan run, the artifact's head-object read, the live API and authorizer reads.

-- 1.0.0_SA_CTO
