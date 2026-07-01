# 0.4.0_DS_ClientPlatform~A -- ADVI_TAGATTR leg-2 (ARCH-GATE 2 discharge): D_00c fee-basis

**archetype:** IMPLEMENT (secondary: COORDINATE, DEPLOY)
**window:** 2026-07-01 ~0620Z -> ~1515Z (since session_close_0620Z / 9210547cf) -- substantive work ~1443-1515Z
**serial:** 0.4.0_DS_ClientPlatform~A | **branch:** CLOUD | **project:** ADVI_TAGATTR (DS-2, bd firm)

## Window summary
Post-INFREF-cutover, picked up a CTO-dispatched task: ADVI_TAGATTR leg-2 (the fee-basis leg,
gated to CTO at Gate-1). Andrew ruled the fee model live in-session ("advisor has a fee percentage
tagged per account, they take that fee on that account") -> fees are per-ACCOUNT ACTUALS, conserved/
reconciled to C_08 canonical, NOT full-tagged like AUA. Implemented leg-2 as LABELING + a runtime
conservation ASSERT (no fee-value change), deployed to bd, verified. ARCH-GATE 2 discharged; accepted
by CTO + COO; DE no-FE-change; base-DS de-conflicted.

## What I did
1. GROUNDED the target against a cross-firm footgun: CTO said "D_00c.portal_leaderboard.py" -- but that
   basename exists in THREE firms (bd/cot/inf). Gate-1 (0ab172d3f) + fc8c18361 are BLACK DIAMOND ->
   leg-2 = data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py (opal-data-bd). Nearly opened inf
   INF_D_00c (NEVER#1 firm-separation catch). CTO confirmed bd source-grounded.
2. GROUNDED scope = LABELING + ASSERT, no fee-value change: L588 fee_aua=row.total_aua (canonical
   billing total); L620-630 scales per-role fee_paying so sum_roles(fp.aua)==fee_aua, B1.fix keeps
   role.aua==fp+nf. So fees were ALREADY conserved/reconciled == Andrew's account-level model by
   construction. No re-derivation.
3. IMPLEMENTED (commit 3ba105354): (a) labels -- per-role rd.fee_basis + _meta.fee_basis_semantics =
   'per_account_actuals_conserved_reconciled_to_c08_canonical', paired with the Gate-1 aua non-additive
   label; comments updated (fee-BASIS gated -> RESOLVED). (b) CTO-add: explicit runtime ASSERT after the
   fp-scaling -- abs(sum_roles(fee_paying.aua) - fee_aua) <= 0.01*n_roles (tol scales w/ role count for
   2dp rounding) + per-role abs(role.aua - (fp+nf)) <= 0.01. Conservation is now a GATE, fails loud.

## Files Modified
- `3ba105354` -- see commit message (data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py, +33/-5).

## Deployment Sequence + Verification
- ds-commit-gate: CLEAN (py_compile + AST + ruff). safe-commit 3ba105354 -> push origin/CLOUD (OK).
- safe-deploy: S3 cp SUCCEEDED but the post-deploy pipescript-VERIFY step CRASHED -- safe_deploy_core.py
  run_pipescript_verify L218 subprocess.run -> OSError WinError 193 ("not a valid Win32 application";
  Windows can't exec the extensionless comp-pipescript bash wrapper).
- VERIFIED MANUALLY (never-trust-rc): local MD5 0f9ed04aab1b1c4d7805afe717da2dc8 == deployed ETag on
  s3://opal-data-bd/code/gold/D_00c.portal_leaderboard.py (LastMod 14:59:50Z, 73968B). Deploy GOOD.
- Effective next bd nightly (post-serve; validate on the artifact, no ad-hoc run).

## MCP traffic (significant only; ~14 msgs)
- CTO: fee-ADR surfaced-to-Andrew -> Andrew ruling relayed -> CTO CONFIRMED (firm=bd + scope=label/assert,
  source-grounded) -> RAVC-CLOSE leg-2 ACCEPTED, ARCH-GATE 2 discharged.
- COO: RULING -- leg-2 CLEAR to stand, NO never-widen co-sign (DELTA=0 values + additive labels exempt);
  the co-sign belongs to the SEPARATE DS-2 no_infer toggle (a value-move). 2 grounding conditions (I own
  #1 DELTA=0-on-nightly; #2 DE-check = satisfied).
- DE (0.4.0_DE_ClientPlatform): no FE change needed (leaderboard renders no fee-DOLLARS from role_breakdown;
  fee panels source C_08; labels additive-safe) -> condition #2 grounded.
- Base 0.4.0_DS_ClientPlatform: de-conflicted -- synced clean, no D_00c WIP; DS-2 no_infer toggle SHELVED by
  Andrew (low-usage/explainable) -> no further base D_00c contention.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-pipescript io D_00c | rule-13 gold-touch: column gaps + consumers | PASS -- writes employee_leaderboard.json->D_04; fee from C_08 advisor_fee_detail (grounds the "reconciled to C_08" label); additive change, no gaps |
| ds-commit-gate | pre-commit (py_compile+AST+ruff) | PASS -- clean |
| safe-deploy (verify leg) | post-deploy pipescript verify | FAIL -- WinError 193 Win32 crash (tooling bug, not a deploy failure); deploy verified manually via ETag |
**Worked:** comp-pipescript io grounded the C_08 fee-source for the label. **Gap found:** safe-deploy's
post-deploy verify silently CRASHES on Windows -> automated post-deploy verification has NOT run on any
Windows DS gold-deploy = a false-green gate hole (CTO elevated to AE + ADHC_PREFLT). Caught here only by
manual ETag-verify.

## Blockers
NONE. leg-2 landed + accepted. Only remaining item = DELTA=0 validation on the next bd nightly (external-
gated, not a blocker).

## Current State
- ADVI_TAGATTR leg-2 (ARCH-GATE 2) DISCHARGED + ACCEPTED (CTO RAVC-close, COO ruled-stands, DE no-change,
  base-DS de-conflicted). Deployed opal-data-bd/code/gold/D_00c.portal_leaderboard.py (ETag 0f9ed04a),
  commit 3ba105354 on origin/CLOUD.
- Fee model: per-account ACTUALS, conserved, reconciled to C_08 canonical (Andrew ruling); AUA stays
  full-tag non-additive (Gate-1). Both bases now labeled (fee_basis / aua_basis) + conservation is a
  runtime gate.
- NO never-widen co-sign needed (DELTA=0). DS-2 no_infer toggle (the value-move sub-item) SHELVED by Andrew.

## Next Steps
1. [0.4.0_DS_ClientPlatform~A] Post-serve: comp-validate Phase-3 on the next bd nightly employee_leaderboard.json
   -- confirm DELTA=0 (fee values unchanged), fee_basis/fee_basis_semantics labels present, no other surface
   moved, assert fires clean. RAVC COO+CTO the result. (Tracked follow-up if session not live at nightly.)
2. [AE] Fix safe-deploy.sh Windows verify-crash (invoke comp-pipescript via bash/shell, or fail-loud if the
   verify subprocess can't spawn) -- CTO-elevated, ADHC_PREFLT self-validation case.
3. [0.4.0_DE_ClientPlatform] belt-and-suspenders render-eyeball at the bd nightly (folded into TAGATTR pass).
