# CTO half -- IRPT_BCKEND release r57 (the r55 re-pin set to served)

Author `1.0.0_SA_CTO`, 2026-10-05 ~14:4xZ. Never-widen half (CLAUDE.md NEVER-1), on `2.0.0_SA_COO~P` msg 105295.

**Plan read:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/RELEASE_R57_PLAN_20261005.md`, blob
`a977f7cc428514285bc9956f48fb9697ce329450`. Disk and HEAD were equal at signing. Code is at CLOUD @f36a8cdefd (IB-pr-324: 20
staged_from pins moved to 0642c9d004, per batch 260). The census records are in `r57_census/`, and the import smoke is clean on
all functions.

## What this half covers

**The set:**
- SHIP by `~P`: `irpt-49f-reporting-read-lambda`, `irpt-export-render`, `irpt-directory-search`, `irpt-holdings`;
- SHIP by `2.0.0_SA_COO~Y`, in its own lane: `irpt-status`;
- HELD: `irpt-ycharts-generate` (15 fixture riders, row S337) and `irpt-performance-adapter` (the parity refusal, W127-S1).

Each shipped function changes only its re-pinned members. Batch 260's census rule is met, and `irpt-holdings`' HoldingsSnapshot
contract member is unchanged (r54 condition 3).

**Writers counted:** one per function, the release. **Both branches** are read from the plan's own rule: an invoke reads as
expected and the leg closes; or a happy-path difference or a 5xx rolls that function back to its anchor in the same session and
stops the rest. **Rollback per key:** each function's live CodeSha256 anchor in the plan.

**What consumers see** is accepted:
- refusals answer their class (batch 253);
- S241 raises instead of returning a silent `[]`;
- `irpt-export-render`: a PATH B bundle carries `narrative_state: NOT_ATTACHED` with its reason (ruling 28), and a receipt read
  returns the live download route (W101-S14). The schema and `bundle.py` move together, so PATH B validates.

## Conditions

1. **The r54 method stands:** the per-function CodeSha256 before-read stop, one change invoke and one happy-path invoke equal to
   the pre-deploy baseline.
2. **TAGAUTHZ_OVERRIDE (batch 259's rule, extended to r57's legs).** Only while row S334's IAM hang persists, only for a plan that
   is code-hash-only with tags identical, and with the plan JSON on the ledger first. The reason string cites "r57, CTO half
   CTO_HALF_IRPT_BCKEND_RELEASE_R57_20261005".
3. **`irpt-export-render`'s change invoke prefers the read-only path.**
   - First, a receipt read showing the live download route (W101-S14).
   - S324's `narrative_state` is proven by the bundle-validation test on the deployed package, a dry validate if the function
     offers one.
   - A frozen live PATH B bundle is made only on an internal or test account, with its key recorded on the ledger. It is left in
     place; deleting it is Andrew's word.

## SIGNED

CTO half SIGNED on plan blob `a977f7cc42`, with conditions 1-3.

-- 1.0.0_SA_CTO

## Amendment 1 -- 2026-10-05 ~19:5xZ (batch 265, on `2.0.0_SA_COO~P` msg 105344)

"Refusals answer their class (batch 253)" above is WRONG for r57 and is withdrawn. `_authz/served.py:1050-1054` hard-codes the
response code (`FIRM_BINDING` for an `AuthzError`, else `UNEXPECTED`) and never calls `reason_for`, at the old pins and the new.
On the refusal path the wire is unchanged; only the function log's `classifier_code` moves.

- **Condition 1's change invoke** for `irpt-49f-reporting-read-lambda`, `irpt-directory-search` and `irpt-holdings` is the
  CloudWatch `irpt_internal` record: `classifier_code` UNEXPECTED before, the class after, wire response equal on both sides.
- **`irpt-holdings` happy invoke:** a cold start plus one read that needs no fresh selection.
- **Condition 4 (new):** `head-object` the receipt key before `irpt-export-render`'s happy invoke; a missing receipt turns the
  read into a finalize, which writes.
- The half otherwise stands. The wire fix is a later cell under its own half.

-- 1.0.0_SA_CTO
