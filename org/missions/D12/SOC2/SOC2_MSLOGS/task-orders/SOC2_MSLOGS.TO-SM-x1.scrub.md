# TO SOC2_MSLOGS.TO-SM-x1 -- the cosmetic scrub: the Ticket Center name out of the Terraform, the app registration script, the README and the RUNBOOK

<to_id>SOC2_MSLOGS.TO-SM-x1</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~5</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Risk note:** WORLD only by the gate's path floor (an infrastructure path is in `<paths>`); the cell calls nothing live.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-x-1` (`decompositions/SOC2_MSLOGS_DECOMP.md`) |
**outcome_ref:** cosmetic (Andrew's scrub word) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-x-1`. Andrew-direct 2026-10-16 ~16:1xZ, VERBATIM: "We should scrub all ticket center frameworks from this schema." The system under `data/m365_metadata/` and `infra/aws/terraform/trino/` was built under the project
TCKT_MTADTA (Ticket Center metadata), which is closed; it now belongs to the project SOC2_MSLOGS (an audit store to know the exposure of a hacked account). This cell is a word change in six places and changes NO behaviour.
Other cells own the other files that mention the old name (the collector package, the door, the silver builder, the registry) and scrub their own. Tests and tools run nothing live.

### THE FILES (read each; change only words)

1. `infra/aws/terraform/trino/main.tf` -- header and comments; the `Project` tag value `"TCKT_MTADTA"` becomes `"SOC2_MSLOGS"`; the KMS key `description` string `"... (TCKT_MTADTA). ..."` becomes `"... (SOC2_MSLOGS). ..."`.
   Those two strings are the only non-comment changes in the Terraform; keep every other word of each string.
2. `infra/aws/terraform/trino/identity.tf` -- comments only (the header names the old project and a cell id: say the same thing about SOC2_MSLOGS, or drop the sentence).
3. `infra/aws/terraform/trino/collector.tf` -- comments only (same).
4. `data/m365_metadata/scripts/app/register_app.py` -- the module docstring and comments only. Change no code line.
5. `data/m365_metadata/README.md` -- rewrite the opening and the spec pointers so they describe the SOC2_MSLOGS purpose in two or three plain sentences (store the raw Microsoft 365 audit records of every account so that, if an account is
   hacked, the exposure can be read back: what was seen and for how long) and point to `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md`. Delete every reference to `org/missions/D7/TCKT/...` and to "eight accounts".
6. `data/m365_metadata/scripts/app/RUNBOOK.md` -- replace the project name and cell id in the opening lines; leave every step as written (the release lane edits it later).

Behaviour is graded by fingerprint: Python files by their syntax tree without docstrings; Terraform by its non-comment lines with `TCKT_MTADTA` read as `SOC2_MSLOGS`. So do NOT rewrap or reorder any code or any non-comment Terraform line.
`start_subscriptions.py` and `test_app.py` are NOT yours (the collector cell owns them).

### ACCEPTANCE

<criterion id="SM1-x1-AC1" cell_refs="SM-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_x1.py scrub</invocation><expect>X1-SCRUB-OK</expect></criterion>
`SM1-x1-AC1` -- none of the eight listed files mentions the Ticket Center, and the three Terraform files and the app registration script behave exactly as before (fingerprints equal).

<expected_criteria>SM1-x1-AC1</expected_criteria>

Dry-run at the base 2026-10-16 ~17:0xZ: AC1 `X1-SCRUB-REFUSED infra/aws/terraform/trino/main.tf still mentions TCKT; ...` -- FAIL as expected. It was driven GREEN against a sed-scrubbed scratch copy outside the repository.
Run from the repository (worktree) root. The check imports `fp_lib.py` beside it.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL; NOTHING is called live.** No AWS call, no Terraform init or apply; `terraform fmt -check` (no network) is welcome.
- **Refusal clause.** If the check refuses and you cannot see why, stop, write the reason and the check line in your report and a surprise row (id `SOC2_MSLOGS-D1-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing, in the investigation file below); do not touch the check.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~5 <0.9.0_WK_SOC2_MSLOGS~5@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/terraform/trino/main.tf
infra/aws/terraform/trino/identity.tf
infra/aws/terraform/trino/collector.tf
data/m365_metadata/scripts/app/register_app.py
data/m365_metadata/README.md
data/m365_metadata/scripts/app/RUNBOOK.md
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md</decomp_doc> (round 1), cell `SM-x-1`.
<owned_cells>SM-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SM1-x1-AC1. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~5/SOC2_MSLOGS.TO-SM-x1.scrub.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SM1-x1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the check line, `git diff --stat` of your commit, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- words only.
lane: the <paths> block IS the grant.
</preflight>

Source: Andrew-direct 2026-10-16 ~16:1xZ (record `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md`); PRD v0.2 C-HOMES; decomposition round 1 cell SM-x-1.
Risk note: the Terraform tag and key description strings change, so the release's plan will show an in-place tag update on the bucket and key; the release seat reads it as expected (decomposition ruling 9 admits tag-only updates).
