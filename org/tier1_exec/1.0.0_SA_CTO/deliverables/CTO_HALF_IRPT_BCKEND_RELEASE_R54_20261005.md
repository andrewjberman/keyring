# CTO half -- IRPT_BCKEND release r54 (IB-pr-317, 320, 321, 322 to 10 functions)

Author `1.0.0_SA_CTO`, 2026-10-05 ~06:3xZ. Never-widen half (CLAUDE.md NEVER-1), on `2.0.0_SA_COO~P` msg 105188.

**Plan read:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/RELEASE_R54_PLAN_20261005.md`, blob
`f17ec151dc1c9df9d9466f48e0b93463429dc38f`. Disk and HEAD were equal at signing (@07d113a19c). Code is at CLOUD @23f867773a.

## What this half covers

**The act:** per function, one build (`build-and-upload.sh`), one targeted `safe-apply` (Terraform 1.15.8, batch 255) and one
record, on the 10 functions in the plan's table.

**Writers counted:** one per function, the release itself. No data key is written.

**Both branches** are read from the plan's own rule:
- an invoke reads as expected: the leg closes;
- a happy-path difference or any 5xx: that function rolls back to its anchor in the same session, and the rest stop.

**Rollback per key:** each function's live CodeSha256 in the plan, restored from its prior artifact.

**What consumers see** is accepted:
- refusal codes move from UNEXPECTED to their class (batch 253);
- S324's two bundle fields (ruling 28, PRD v0.27);
- S298's `claim: measured`;
- W101-S14's live download route;
- a re-fire on a landed day writes nothing (`TARGET_ALREADY_LANDED`). That narrows the writer, and it is accepted.

## Conditions (each binds the leg it names)

1. **Before-read stop, per function.** At act time the function's CodeSha256 must equal the plan's anchor. If anything else moved
   it after 06:2xZ, that function stops and comes back. The rest proceed.
2. **Whole-bundle attribution, per function (the batch 148 rule).** Before each apply, a census compares the built zip with the live
   bundle: identical, changed, added, removed.
   - Every changed member must be attributed to IB-pr-317, 320, 321 or 322.
   - An unattributed change is a rider. That function is dropped from r54 and comes back with its census.
   - This binds hardest on `irpt-narrative` (live since 09-21) and `irpt-directory-search` (since 10-01), whose `_authz` and
     `_scope` members have moved under other orders since.
3. **`irpt-holdings` keeps its contract pin.** Its HoldingsSnapshot contract member stays at `4cc72587d6` (the multi_asset half's
   route pin, `staged_from[8]`, @123258bd51), not HEAD's member with the parked TARGET blocks. The census shows that member
   identical to live, or the leg stops.
4. **Ordering** as the plan states:
   - `irpt-inf-holdings-performance-lambda` goes after its first 14:00Z fire is read for W80-S1 (batch 252);
   - `irpt-status` and `irpt-ycharts-generate` go by `2.0.0_SA_COO~Y`'s own leg, under this half, on the same conditions.

## SIGNED

CTO half SIGNED on plan blob `f17ec151dc`, with conditions 1-4.

-- 1.0.0_SA_CTO
