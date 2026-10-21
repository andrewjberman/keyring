# TO NFRA_FIDUPL.TO-FT-s-5 -- box-role-put-perg-secret -- one per-secret put grant

<to_id>NFRA_FIDUPL.TO-FT-s-5</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-5` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 2) | **outcome_ref:** FWD-9 |
**depends_on:** FR-s-5 (the secret, applied at 01:0xZ)

---

## WORKER FACE

### THE CELL

**FT-s-5** -- The seed command (`perg_seed.py`, FT-s-1) runs on the box under the box role, which today may only READ the per-G list secret. Add ONE statement to the box role's policy in the Terraform root: `secretsmanager:PutSecretValue` on the ARN of `fidelity/alongside/perg-list` and on nothing else (no wildcard, no other secret, never the Wealthscape credentials). This is the only way the value reaches the secret without a person or a record carrying it.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules), 7 (box layout), 9 to 12 (interfaces; section 12 is this round's); `infra/aws/terraform/canonical-fidelity-ec2/` (`perg.tf`, the box role policy), your FU-s-13 ledger as the pattern.

### WHAT TO BUILD

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-perg-put-<date> ...`, one leg: statement added).
2. In the root, add the statement beside the existing per-secret read grant, referencing the secret resource (not a typed ARN), with the guard-friendly comment if any wildcard appears (none should).
3. Plan: exactly `Plan: 0 to add, 1 to change, 0 to destroy.` and the one change is the box role policy. Apply with `safe-apply` only, no `-target`. Close the ledger. Do not run the seed and do not write the secret's value.
4. Run both criteria and put the lines verbatim in your report.


### ACCEPTANCE

<criterion id="FT-s-5-AC1" cell_refs="FT-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft5i</invocation><expect>R1-FT5I-OK the box role may put the per-G list secret and not the credentials</expect></criterion>
`FT-s-5-AC1` -- the IAM simulator: put allowed on the per-G secret, not allowed on the Wealthscape credentials (a negative control).

<criterion id="FT-s-5-AC2" cell_refs="FT-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu6g</invocation><expect>R1-FU6G-OK</expect></criterion>
`FT-s-5-AC2` -- the root's guard still passes. A second criterion, with its reason: it fails if the new statement is written with a wildcard.

<expected_criteria>FT-s-5-AC1,FT-s-5-AC2</expected_criteria>

Dry-run at the base: `FT-s-5-AC1` base: FAIL as expected; `FT-s-5-AC2` base: FAIL as expected

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD.** This order changes an IAM policy. Ledger first, closed last; the apply is by `safe-apply` only; nothing is stopped, started or deleted; no secret value anywhere; no alert.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/terraform/canonical-fidelity-ec2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3), cell `FT-s-5`.
<owned_cells>FT-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-5-AC1,FT-s-5-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-5.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-5-AC1,FT-s-5-AC2` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criteria with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: RUN -- ONE statement is added to the box role policy (secretsmanager:PutSecretValue on the one per-G secret ARN); denominator 1 IAM statement added, 0 widened. comp-iam is blind to the root's computed names; the live check is the IAM simulator in FT5-AC1, with the Wealthscape credentials secret as the negative control.
comp-adversary: DECLARED-NOT-APPLICABLE -- one narrow put on a list secret the box already reads.
lane: the paths block.
</preflight>

Source: CTO msgs 8891 and 8909; PRD v0.5 @c4f8dc3d51; the first landed day (run record run-20261021T012004Z).
