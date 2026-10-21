# TO NFRA_FIDUPL.TO-FT-s-6 -- seed-and-schedule-on -- run the seed once, name the secret version, turn the three rules ON

<to_id>NFRA_FIDUPL.TO-FT-s-6</to_id>
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

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-6` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 2) | **outcome_ref:** FWD-2 |
**depends_on:** FT-s-1, FT-s-2 and FT-s-5 (delivered to the box and applied)

---

## WORKER FACE

### THE CELL

**FT-s-6** -- Close the loop the CTO named: the schedule is enabled against a NAMED version of the per-G list secret. After FT-s-1 and FT-s-2 are delivered to the box (TO-FU-s-10) and FT-s-5 is applied, run `perg_seed.py` once on the box through SSM, read which version of the secret is now current (a version id, never the value), then turn the three schedule rules ON by setting the root's `schedule_enabled` variable and applying the root under `safe-apply`.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules), 7 (box layout), 9 to 12 (interfaces; section 12 is this round's); `infra/aws/terraform/canonical-fidelity-ec2/` (`schedule.tf`, `variables.tf`), your own ledgers, and `C:/Dev/ajb_workspace/org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 0.

### WHAT TO BUILD

**HOLD: do nothing until the issuer's message says GO** (the seed signs in to Fidelity; one sign-in at a time, and only after the code is on the box).
1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-schedule-on-<date> ...`; legs: seed, schedule).
2. Run `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/perg_seed.py` once through SSM. Its single stdout line is counts only: record it verbatim. Do not retry on a refusal: report it.
3. Read the secret's current version id with `describe-secret` (never `get-secret-value`) and write `NFRA_FIDUPL.TO-FT-s-6.schedule_version.md` in your deliverables folder with the version id, the read time, and the counts line. Run `fidupl_round_checks.py ft6v`.
4. **HOLD again (CTO 8919): this step runs ONLY after the issuer's message says ENABLE.** That message follows the CTO's countersign of the never-widen addendum that names the secret version, the seed run's keys, the rule expressions and the first fire read; no enable before the countersign is on file. Then set `schedule_enabled = true` in the root's tfvars default or the variable default as the root's convention is, plan (exactly the three schedule rules change State to ENABLED, nothing else), and apply with `safe-apply`, no `-target`. Run `fidupl_round_checks.py ft6r`. Close the ledger. Do not start the automation by hand.


### ACCEPTANCE

<criterion id="FT-s-6-AC1" cell_refs="FT-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft6v</invocation><expect>R1-FT6V-OK the per-G list secret has a current version</expect></criterion>
`FT-s-6-AC1` -- after the seed: the secret has a current version.

<criterion id="FT-s-6-AC2" cell_refs="FT-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft6r</invocation><expect>R1-FT6R-OK the three schedule rules are ENABLED</expect></criterion>
`FT-s-6-AC2` -- after the apply: the three schedule rules read ENABLED.

<expected_criteria>FT-s-6-AC1,FT-s-6-AC2</expected_criteria>

Dry-run at the base: `FT-s-6-AC1` base: FAIL as expected; `FT-s-6-AC2` base: FAIL as expected

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD.** A real sign-in at Fidelity (the seed, once), a secret write by the box, and a schedule turned ON. Ledger first, closed last; `safe-apply` only; no alert; no value in any record.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/terraform/canonical-fidelity-ec2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3), cell `FT-s-6`.
<owned_cells>FT-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-6-AC1,FT-s-6-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-6.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-6-AC1,FT-s-6-AC2` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criteria with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- three EventBridge rules change State from DISABLED to ENABLED through the `schedule_enabled` variable; denominator 3 rules changed, 0 created.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes in this order (FT-s-5 owns the grant); denominator 0 IAM statements changed.
comp-adversary: RUN -- the schedule is the first standing automated sign-in; the issuer's seed GO and the CTO's Track A rulings (8875, 8891) are the record.
lane: the paths block.
</preflight>

Source: CTO msgs 8891 and 8909; PRD v0.5 @c4f8dc3d51; the first landed day (run record run-20261021T012004Z).
