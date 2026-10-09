# R2-1 landed, refused once on its own statement text, and a verify leg this box cannot close -- 0.7.0_AE_CloudOps~DELL1

**Session:** 2026-10-09 07:10Z - 07:5xZ (the delta since
`four_orders_three_clock_gated_and_a_blocking_finding_measured_closed.md`, whose Next Step 1 this log closes)
**Branch:** box/dell1

## Objective

Execute `ADHOC.healgap-r2-1-runner-reads-own-result` from 07:10Z, the clock its own scope 1 sets, and land it before
~20:00Z.

## Compiler Tools

- `comp-find --files 'cottonwood' infra/aws/terraform/opal-assets` -- denominator 34 hits / 21 files, bands DEF=1
  SURFACED=25 CONFIG=8. Established that the refused literal is pervasive across the root and that
  `cot_rebalancer_runner.tf` is its DEF site, which is what made the gate's NEW-vs-EXISTING discriminator legible.
- `comp-find 'permitted context|...|LGIC_ENFORCE' .tools` -- denominator 33 hits / 499 files, bands HEAD=11
  SURFACED=22. Located `naming-gate.py:1737/:1738` (the REFUSE/WARN split) and `:1721-1731` (the R20 declared
  exception, "THE ONE CONSUMPTION POINT"), which is what established that no escape existed at this seat's authority.
  Both searches were RAIL DENIALS first: a blind recursive grep was refused twice and the rail printed the comp-find
  that answers. Running what it named cost one round-trip each and produced the denominators above.
- `naming-gate.py --diff --enforce` -- the C8 instrument, run three times: REFUSE on the typed cut, PASS on the
  one() cut, PASS again on the committed diff.
- `hg_t8_iam.py` / `hg_tf_fmt.py` -- C1 and C2, each with its base arm run by this seat.
- `terraform show -json` -- C3, graded per attribute rather than from the summary line.
- `deploy_ledger.py open / close-leg / hold / check` -- the NEVER-2 entry.
- `proof-of-spec-check.py` -- the instance, INVALID then VALID (see Decisions 3).
- `comp-iam` -- DECLARED-NOT-APPLICABLE and recorded as such: it models `(action)` and never `(action, resource)`, so
  it cannot grade a key-pattern-scoped grant; cloud-ops states it is a FLOOR and fails green. The live
  `get-role-policy` read is the stronger instrument and was run instead.

## Work Completed

### 1. The order's own verbatim statement text was refused by a commit gate

**archetype:** DIAGNOSE

Scope 2 gave the statement to insert. It went in exactly -- 7 lines added, 0 removed, between the two named Sids --
and both criteria passed with their controls moving (C1 `IAM-BAD 0 (want 1)` -> `IAM-OK statements=4`; C2 `FMT-OK`).
`safe-commit` then REFUSED at the naming limb: the added `Resource` literal is a NEW hand-kept carrier of the firm
token `cottonwood`, which must "be read through `lookup('cottonwood')`" -- a form a `.tf` file cannot express.

What made this decidable rather than a judgment call: `naming-gate.py:1737` REFUSES a NEW carrier while `:1738` only
WARNs an EXISTING one, and the identical literal already sits at `:85`, `:86` and `:102` of the same resource. The
refusal turned on the line being new, not the name being wrong. The order's condition anticipated "a missing registry
row to report" -- but no row was missing: `cottonwood` is already a known firm segment, which is precisely why
`carrier()` flags it.

I did not work around it. `--force` covers contamination only, never a limb refusal; `safe-apply` carries the same
limb at `:183/:262/:321`, so no bypass of the commit would have landed it either; and the gate's one sanctioned
admission is an R20 declared exception whose `authority_ok()` at `:1295` demands a record at a full 40-hex pin whose
blob carries the ruling id -- which CLAUDE.md rule 30 puts under Andrew's word.

Filed row `MDPF_HEALGAP-D1-S9` @20ec950171 (BLOCKING, INERT), reverted the edit, and asked `COO~G1` + `CTO~DELL1` for
one of three dispositions. The revert mattered for a reason beyond tidiness: two other seats are live in this shared
worktree, and a stray uncommitted IAM widening would ride the next apply of that root by anyone.

### 2. Ruling H, and the act landed

**archetype:** DEPLOY

`CTO~DELL1` ruling H @1af255b7da, carried as issuer amendment A1 @83028dca8a, took option (c): read the firm from the
grammar. The Resource became
`"arn:aws:s3:::${local.monolith_bucket}/blackdiamond/${one(local.monolith_source_scopes.blackdiamond)}/meta/*-result.json"`.
`monolith.tf:89` reads `blackdiamond = ["cottonwood"]`, so `one()` resolves to the single element and the rendered ARN
is byte-identical to the refused form -- which is why A1 added a C3 clause requiring the plan to print that identical
ARN, and a new C8 requiring the gate to PASS.

The amendment was read VERBATIM at its own pin before acting (`git show 83028dca8a:<order>`, 8,722 B as the positive
control that the pin-and-path read resolves at all), not grepped from the worktree.

Landed: commit ba88934f7b, ledger `20261009T0732Z_healgap-r2-1-runner-reads-own-result-dell1-20261009`, targeted plan
graded per attribute, `safe-apply` on the SAVED plan so the applied bytes were the graded bytes. Live read-back: 4
statements, `ReadOwnRunResult` Allow `s3:GetObject` on the exact key pattern, `DenyBlackdiamond49fFirmSep`
byte-identical, re-plan `No changes` with `-detailed-exitcode` rc=0.

One hazard was read before relying on the carrier rather than after: `monolith.tf:79-81` records that
`aws_iam_policy.description` is ForceNew and this root's write-policy DESCRIPTIONS interpolate the very scope list the
new statement now reads. A policy document is not a description -- but that was put under test, not assumed: the plan
shows `actions ['update']`, differing attributes exactly `['policy']`, and `name`/`role` before == after.

### 3. A verify leg this box cannot close

**archetype:** DIAGNOSE

C5 asks for three live simulations. The first returned `AccessDenied`: this box's principal
`cloudops-dell1-agent-user` is not authorized for `iam:SimulatePrincipalPolicy` on
`arn:aws:iam::313476888478:role/cot-rebalancer-runner-role`.

A deny is where an instrument is most likely to be lying, so it got a control. The SAME action against the caller's
OWN user ARN returns `allowed` -- the API works, and the grant is RESOURCE-SCOPED to self rather than absent
wholesale. `iam:SimulateCustomPolicy` is denied too, so there is no substitute instrument on this box. C5 is therefore
reported as neither a pass nor a failure, and C6 follows it.

The ledger went to `hold` rather than `close`: `HELD-SOVEREIGN-GATED`, L1 and L2 closed with proof, L3 open on C5
alone, with the gate naming the exact action and resource and a re-read EVENT. deploy_ledger renders that "apply legs
proven, only verify open; tracked-not-stranded". Closing it would have been the DRIFT-DANGEROUS shape I surfaced on
two laptop entries three hours earlier in this same session -- an entry reading terminal over an unproven leg.

Row `MDPF_HEALGAP-D1-S10`. Deliberately NOT self-remedied: granting this seat the permission it needs to verify its
own work is outside the order's `<paths>` and is the wrong shape regardless.

## Verification

- Proof-of-spec instance: **VALID rc=0**, controls 4 of 4 named discriminate, 0 DID-NOT-DISCRIMINATE, rollback named.
  It graded INVALID first, on five real schema violations (an over-short `criterion_verbatim`, two `kind` values
  outside the enum, a `deployed_state` of `N/A`, and an `artifacts_produced` row naming a live AWS principal at a
  commit pin that git correctly refutes). Fixed by naming the repo path at its commit and describing the live grant in
  the evidence field, which is what that row is actually for.
- C8's invocation could NOT be run literally. The criterion says `git diff HEAD~1`, but this is a shared worktree and
  other seats committed on top of mine (HEAD read e21ce491ca while ba88934f7b stayed an ancestor), so `HEAD~1` names
  another seat's commit. Run with `HEAD~1` resolved to the actual commit, and SAID SO in the instance rather than
  letting the recorded invocation drift from what was executed.
- CloudOps conditions (ADDENDUM 3 @947dd446e5): none fires. No SSM send, no firm data bucket written, no 49F principal
  assumed. The firm-sep Deny is byte-identical before and after, so condition 3 holds structurally.

## Decisions Made

1. **No workaround on the naming limb, and no R20 entry minted at this seat.** The mechanism is fail-closed and its
   one admission is explicitly Andrew's to acknowledge.
2. **Revert the refused edit instead of parking it in the tree.** Shared worktree, live peers, an IAM widening nobody
   approved.
3. **`hold`, not `close`.** The act is complete in the world; one verification arm is not runnable here. Those are
   different facts and the ledger has a state for exactly this.
4. **The order stays `pending`.** It says to flip complete "if every criterion passes". Two do not.

## Files Modified

- `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` -- the ReadOwnRunResult statement @ba88934f7b
- `org/critical_paths/change_management/20261009T0732Z_healgap-r2-1-...-dell1-20261009_deploy_completion.md` + its
  sentinel -- @2dc50a181e
- `.../deliverables/ADHOC.healgap-r2-1-runner-reads-own-result_PROOF_OF_SPEC.json` -- @2dc50a181e
- `org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md` -- rows D1-S9 @20ec950171
  and D1-S10 @2dc50a181e
- `.../deliverables/healgap_r2_1_ReadOwnRunResult_REFUSED_BY_NAMING_GATE.patch` -- the refused cut, kept @20ec950171

## Blockers

1. **C5/C6** -- `iam:SimulatePrincipalPolicy` on the runner role for this box's principal, or the issuer grading the
   three arms (SEPARATE invocations) from a box that holds it. Owner: `1.0.0_SA_CTO~DELL1` with `2.0.0_SA_COO~G1`.
   This is a standing hole in dell1's ability to close the verify leg of ANY IAM deploy it is given, not a quirk of
   this order.

## Current State

The grant is live and verified. Ledger HELD on L3 alone. Order `pending`, 6 of 8 criteria PASS. Two clock-held orders
remain with timers armed: aw-1 steps 4-6 in the 11:15Z-12:50Z window (tree `C:/tmp/rv-r28-dell1` and plan
`C:/tmp/rv_apply28_dell1.tfplan` left in place per AMENDMENT 3), and partner-roster B4 after the 17:15Z emitter fire.

## Next Steps

1. `[0.7.0_AE_CloudOps~DELL1]` 11:15Z-12:50Z: aw-1 steps 4-6 -- read AMENDMENT 1 (a)-(d) FIRST, apply nothing and
   name the failing condition if any does not hold, never apply after 12:50Z.
2. `[0.7.0_AE_CloudOps~DELL1]` After 17:15Z: partner-roster B4/C7, then close that ledger.
3. `[1.0.0_SA_CTO~DELL1` / `2.0.0_SA_COO~G1]` Clear C5 by either route in blocker 1; this seat then closes L3 and the
   order in one pass.
