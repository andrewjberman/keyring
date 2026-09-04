# TO NFRA_OPSEC202609.TO-OP-S-22 -- A PER-ROLE IAM VERDICT ON THE APPLIED PLANE BEFORE ANY SENTINEL-CHAIN CODE IS DEPLOYED: `simulate-principal-policy` per role, ONE `--resource-arns` per call, the positive control as a SEPARATE invocation -- and silence from a DESIRED-plane lens is NEVER an ALLOW (OP-s-22)

<to_id>NFRA_OPSEC202609.TO-OP-S-22</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

<!-- 0.7.0_AE_CloudOps~W 2026-09-04T02:1xZ: COMPLETE. Proof-of-spec VALID rc=0, 5 of 5 criteria PASS.
     THE VERDICT: all three roles PASS on the APPLIED plane. 45 simulations, ONE --resource-arns per
     call, 28 allowed / 17 denied / 0 mismatches, stable across two runs. Applied-plane existence
     confirmed at this seat (all three CreateDate 2026-09-04T01:51:56Z) with a fabricated-name
     negative control returning NoSuchEntity.
     C-2 AND C-11 VERDICTED ACROSS ALL FOUR IP SETS, not the two the criterion originally said:
     reconciler allowed x4, sentinel explicitDeny x4, CLI explicitDeny x4. The four-set correction was
     this face's own finding, adopted by the issuer at 7669a062e6 BEFORE the roles landed -- without it
     this verdict would have certified the chain's founding invariant with half the population
     unguarded and every simulation in it passing.
     S22-AC2's GATE HELD: 17 denies of 45, so the instrument demonstrably says no.
     THE ses:FromAddress TRAP WAS DEMONSTRATED IN BOTH DIRECTIONS -- allowed WITH the context entry,
     implicitDeny WITHOUT it, same call otherwise. Without it this face would have filed a FALSE DENY
     on a correctly-granted permission. The warning came from iam_sentinel.tf, written by
     0.7.0_AE_CloudOps~S addressed to this face.
     VERDICT DELIVERED: msg 20115 (~T, reconciler + CLI), 20116 (~S, sentinel), 20117 (COO~Z), all
     preceding any function deployment -- no code for any of the three roles exists yet.
     ZERO IAM POLICY EDITS by this face, with a positive control proving the census sees .tf files.
     WHAT THIS VERDICT DOES NOT ESTABLISH, and it is in the instance rather than left to inference:
     C-2's EXCLUSIVITY over the account. This face verdicted THREE principals; C-2 claims nothing else
     in 221 roles ever calls UpdateIPSet, and a fourth holder would leave all 45 results unchanged.
     That enumeration is S15-AC3's. Nor does it cover resource policies, SCPs, or whether the code
     makes the calls -- an allowed pair is not an exercised pair.
     ARTIFACTS: phase1-permission-pairs.md @a63dc951ec, simulation-log.txt @4d31522182.

     Prior note, kept for the record -- 2026-09-04T01:1xZ, staged -> pending on the re-address
     (Msg-ID 20078), when the verdict was correctly unstartable and all three roles filed UNCOMPUTABLE:
     aws iam list-roles over a TRUE denominator of 221 (counted client-side; --query length() returns
     the PAGE count and read 100) returns ZERO for ipset / reconcil / sentinel / unblock, positive
     control passing on two known roles.
     PHASE-1 ARTIFACT: ../deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-22.phase1-permission-pairs.md
     -- the MUST-HAVE / MUST-NOT action-resource pairs per role with every resource ARN pre-resolved,
     so each verdict is a mechanical run the moment an ARN lands. It is SPEC-derived, not code-derived,
     and says so: no implementation exists for any of the three roles (11 hits, all spec, over 51,747
     files; positive control 474 on 'def lambda_handler'). It MUST be re-derived against source before
     any verdict is filed -- a spec list cannot see a helper call the design never mentioned, and those
     are exactly the pairs an over-permissioned role gets padded with.
     ONE FINDING ALREADY: S22-AC3 says "both sets" but the applied plane carries FOUR IP sets
     (cloudfront, cloudfront-ipv6, regional, regional-ipv6). A verdict written to "both" covers 2 of 4
     and reads as complete. This face verdicts all four, denominator printed. -->


⛔ **BLOCKER, NAMED: the three roles must EXIST ON THE APPLIED PLANE first.** The cell's `depends_on` is `OP-s-14`, `OP-s-15`, `OP-s-19` -- *"their roles must exist in Terraform first; the verdict is on the APPLIED role."* **GO CONDITION: `TO-OP-S-15-19` has applied its two roles, and `TO-OP-S-14-21` has applied the sentinel's.** **The verdict may run per role as each becomes available; it does NOT wait for all three.**

> **THIS IS NOT A CIRCULAR DEPENDENCY AND IT IS WORTH SAYING WHY**, because it looks like one. PRD s.9 item 7 says this cell *"runs before any of OP-s-14 / 15 / 19 is DEPLOYED"* -- not before they are declared. The sequence is: **declare and apply the ROLE, verdict the role, then deploy the CODE that assumes it.** Those faces carry that ordering in their own deliverables.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (s.9 item 7; s.4 on the DESIRED-plane lens's blindness; brief F7 the cross-firm-secret-deny belt) - **Decomp cell:** `OP-s-22` (v0.1.11, s.1a) - **Lane:** AE lane - **Round:** 3.

---

## WHY THIS CELL EXISTS SEPARATELY FROM THE THINGS IT VERDICTS

A role that is under-permissioned fails loudly at first invocation. **A role that is OVER-permissioned fails never, and nothing in the build would show it.** This cell is the only place the chain's permissions are examined as their own object rather than as a side effect of the code working.

**The cell's own binding clause: NEVER SIGNAL `ALLOWED` FROM `comp-iam` SILENCE.** `comp-iam` is a DESIRED-plane lens over policy documents; the PRD records at s.4 that it does not parse the Deny statements it reports. **An absence in that tool is an absence of PARSING, not an absence of permission.** The verdict here is `simulate-principal-policy` against the APPLIED role, or it is not a verdict.

## THE INSTRUMENT, AND ITS TRAPS ARE NAMED BECAUSE THEY ARE NOT RE-DERIVABLE AT THE CALL SITE

- **ONE `--resource-arns` PER CALL.** Batching resources into a single simulation collapses per-resource outcomes and yields an answer that is true of the batch and false of a member.
- **THE POSITIVE CONTROL IS A SEPARATE INVOCATION.** Simulate an action the role must NOT have and confirm `implicitDeny` or `explicitDeny`. **A simulation run that returns `allowed` for everything you asked is indistinguishable from a broken query until a control fires.**
- **`--context-entries` FOR ANY CONDITIONED STATEMENT.** A condition that is not supplied a context value evaluates in a way that will not match production. State which context keys you supplied and why.
- **The cross-firm-secret-deny belt (brief F7) is EXTENDED, never re-invented.** If a new deny is needed it takes the existing shape; a parallel belt with different wording is a second enumeration to drift.

## DELIVERABLE

1. **A per-role verdict for each of the three roles** -- sentinel, reconciler, unblock CLI -- on the APPLIED plane.
2. **For each role, the enumerated action/resource pairs it MUST have** (from what its code actually does, read at source) **and the ones it MUST NOT** -- at minimum: the reconciler is the ONLY principal with `wafv2:UpdateIPSet` on ALL FOUR sets (C-2), the CLI can write the table row and **cannot** touch the IP sets (C-11), and the sentinel can write rows and case files and **cannot** write the IP sets.
3. **The verdict RETURNED to the owning faces in writing**, so their deployment step can cite it. **A verdict nobody receives has not gated anything.**
4. **Any gap is a ROW and a recommendation, not a silent widening or narrowing.** ⛔ **Do not edit a role's policy inside this face** -- the roles belong to the faces that declare them. This cell produces a VERDICT.
5. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-22.sentinel-chain-iam-verdict.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S22-AC1" cell_refs="OP-s-22"/> `S22-AC1` -- EVERY ROLE VERDICTED ON THE APPLIED PLANE, ONE RESOURCE PER CALL: for each role, the `simulate-principal-policy` invocations pasted with their `--resource-arns` (one each) and their decisions. **Denominator: roles verdicted of roles existing, and pairs simulated of pairs enumerated, both printed.** A role that does not yet exist files `UNCOMPUTABLE` naming it, never a skipped row.
<criterion id="S22-AC2" cell_refs="OP-s-22"/> `S22-AC2` -- THE POSITIVE CONTROL FIRED, AS A SEPARATE INVOCATION: for each role, at least one action it must NOT have, simulated separately, returning a deny. **If every simulation in the instance returns `allowed`, this criterion FAILS regardless of the other results** -- an instrument that cannot say no has not said yes.
<criterion id="S22-AC3" cell_refs="OP-s-22"/> `S22-AC3` -- C-2 AND C-11 ARE VERDICTED EXPLICITLY, NOT INFERRED: the reconciler ALLOWED `wafv2:UpdateIPSet` on ALL FOUR SETS, one simulation per set; the CLI and the sentinel DENIED the same action on the same resources, each as its own simulation. **This is the invariant the whole chain rests on and it gets its own named result. ⛔ **CORRECTED 2026-09-04 01:4xZ BY THE ISSUER: THE IP SETS ARE **FOUR**, NOT TWO** -- `opal-blocked-ips-cloudfront` (b2e008a6-40d9-4d07-bef5-1caa8b682bb3) and `opal-blocked-ips-cloudfront-ipv6` (eb1a0caa-60a0-492e-a685-e5456cea8b7d) at scope CLOUDFRONT, plus `opal-blocked-ips-regional` (f073f448-eb85-4d23-9306-0cadf4573331) and `opal-blocked-ips-regional-ipv6` (85f90377-7cba-45dd-baca-397310d61f8e) at scope REGIONAL, all us-east-1. Surfaced by `0.7.0_AE_CloudOps~W` in msg 20088 and confirmed by the issuer on the live plane. **THE DENOMINATOR IS 4 OF 4 AND IT IS PRINTED, OR THIS CRITERION FAILS.** A check scoped to two of four would certify C-2 while two sets stand unguarded, and every arm of that check would pass -- the third instance of that shape on this project tonight.**
<criterion id="S22-AC4" cell_refs="OP-s-22"/> `S22-AC4` -- CONDITIONS WERE EVALUATED WITH CONTEXT, AND THE LENS'S LIMITS ARE STATED: for any conditioned statement, the `--context-entries` supplied and why. Plus an explicit sentence naming what this verdict does NOT cover -- resource policies, SCPs, permission boundaries -- so a later reader does not read it as wider than it is. **`comp-iam` output, if run, is labelled DESIRED-plane and is never cited as an ALLOW.**
<criterion id="S22-AC5" cell_refs="OP-s-22"/> `S22-AC5` -- THE VERDICT WAS DELIVERED AND NO POLICY WAS EDITED: the message ids in which each owning face received its verdict, with timestamps preceding that face's code deployment; and a diff census showing **zero IAM policy changes** made by this task order.

<expected_criteria>S22-AC1, S22-AC2, S22-AC3, S22-AC4, S22-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cell `OP-s-22` (no manifest FWD of its own; it is the gate on FWD-14 / FWD-17's deployment); value: a per-role VERDICT on the live plane.
<owned_cells>OP-s-22</owned_cells>
Read-dependencies, NOT claimed: `OP-s-14`, `OP-s-15`, `OP-s-19` (whose roles this verdicts -- their policies are theirs to edit, never this face's).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0).
comp-iam: RUN FOR ORIENTATION ONLY, and its status in this face is explicit -- it is a DESIRED-plane lens, the PRD records at s.4 that it does not parse the Deny statements it reports, and **its silence is NEVER an ALLOW signal** (the cell's own binding clause). Run it, print its denominators, and cite it only as context beside the applied-plane simulations.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; its evidence is live simulation output taken at the assignee's own vintage.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S22-AC1`, `S22-AC2`, `S22-AC3`, `S22-AC4`, `S22-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-22.sentinel-chain-iam-verdict.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S22-AC1,S22-AC2,S22-AC3,S22-AC4,S22-AC5"` BEFORE the complete flip. **`S22-AC2` IS the control that must be able to fail, and it is written so that an all-allowed instance fails on its face.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any simulation">Read each role's ACTUAL code to derive the action/resource pairs it needs. A verdict against a guessed permission list verdicts the guess.</phase>
  <phase id="2" when="during">One resource per call; the control as its own invocation; context entries stated.</phase>
  <phase id="3" when="after">Deliver each verdict in writing to the owning face BEFORE its deployment, and record the message id.</phase>
</compiler_tools_mandate>
