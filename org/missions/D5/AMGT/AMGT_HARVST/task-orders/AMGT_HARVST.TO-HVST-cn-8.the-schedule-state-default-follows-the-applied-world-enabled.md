# AMGT_HARVST task order -- `HVST-cn-8` -- ROUND 99, workstream SCHEDULE-DEFAULT: THE DEFAULT OF `dossier_refresh_schedule_state` BECOMES `ENABLED`, BECAUSE THE APPLIED WORLD HAS THE SCHEDULE ENABLED (CTO countersign of COO addendum 3, `ledger/NEVER_WIDEN_CN7_ADDENDUM3_FLAG_DEFAULTS_CTO_COUNTERSIGN.md`, section "The schedule default, ruled")

<!-- ===================== WORKER FACE -- the worker's whole context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cn-8.the-schedule-state-default-follows-the-applied-world-enabled</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cn-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~184</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule is created or changed. The schedule already exists and is ENABLED in AWS; you change the DEFAULT of a Terraform variable so that the file equals that world. Nothing is applied.
comp-iam: RUN at L5 -- you create no role, no policy and no AWS resource. Allowed commands: `terraform init`, `terraform validate`, `terraform plan -lock=false` (READ-ONLY against the state in `s3://opal-313476888478-terraform-state/harvest/tfstate`) and `python` on the check file named below. FORBIDDEN: `terraform apply`, `terraform import`, `terraform state`, `safe-apply`, `aws ... create/put/update/delete/run-task/start-build`, `docker`, any S3 `put`, `git push`. NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is an edit that touches a resource line (a changed `description`, `name` or `state` expression would plan an in-place update of the live schedule and break the `No changes.` proof), a plan that was not actually run (the plan output is the program's own file), an expectation edited to match, and an `apply` of any kind.
</preflight>

## 0. THE CELL

The daily dossier-refresh schedule `amgt-dossier-refresh-daily` is ENABLED in AWS (applied 2026-10-19 16:57Z by `0.7.0_AE_CloudOps~SC1`; first scheduled fire Tue 2026-10-20 10:00 America/New_York). The Terraform file `infra/aws/terraform/harvest/dossier-refresh.tf` still defaults the variable `dossier_refresh_schedule_state` to `"DISABLED"`, so a plan of the harvest root WITHOUT `-var` now reads `Plan: 0 to add, 1 to change, 0 to destroy.` (ENABLED to DISABLED), and any seat that applied it would silently switch the standing producer off. **This cell makes the file equal the world: the default becomes `"ENABLED"`.** Nothing is applied; the rollback stays an apply with `-var dossier_refresh_schedule_state=DISABLED`.

## 1. THE BUILD

Work in your worktree; run every command from its repo root. Change ONLY `infra/aws/terraform/harvest/dossier-refresh.tf`, and in it ONLY:
a. In `variable "dossier_refresh_schedule_state"`: `default = "ENABLED"`; the `description` says the schedule is ENABLED in the applied world (stage 5 of `HVST-cn-7`, 2026-10-19 16:57Z), this default keeps it so, and `DISABLED` by an apply with `-var dossier_refresh_schedule_state=DISABLED` is the rollback (never a deletion). The `validation` block stays byte-identical, including its `error_message` (it still says "DISABLED (default) or ENABLED"; leave it: only the description and default change in this block).
b. In the file's header comment (lines 1 to 33), correct only the sentences that became false: line 7 to 8 ("DISABLED by default ... the file never enables the schedule by itself") and line 9 ("A later seat (HVST-cn-7) applies this text") may be reworded to say the default now follows the applied world. Comment lines only (they start with `#`).
c. **Leave the schedule RESOURCE byte-identical, including its `description = "...(DISABLED by default)."` attribute (about line 493).** That string is applied in AWS; editing it would plan an in-place update of the live schedule and the no-`-var` plan would stop reading `No changes.`. Every resource, local, precondition, output and the other variables stay byte-identical.
d. Run `terraform -chdir=infra/aws/terraform/harvest init -input=false` first (print its last line to your report).
e. Write the checks' outputs in your deliverables folder `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~184/` (open every file with `newline="\n"` if you write it from Python; ASCII only):
   - `cn8_diff.out` = the output of `python -I org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/cn8_diff_check.py` (the file exists already, written by the issuer; do NOT edit it; it compares your tf with the base blob `8f7d3651c3`, proves the new default is ENABLED, proves every changed line is a comment or inside the one variable block, and first runs a planted-change negative control);
   - `cn8_plan.out` = TWO labelled plans against the REAL state, full root (no `-target`), each `terraform -chdir=infra/aws/terraform/harvest plan -lock=false -input=false -no-color`, each followed by a line `<LABEL>-EXIT=<the command's exit code>`: first the line `DEFAULT-PLAN (NO -var)` then the plan with NO `-var` (it must read `No changes. Your infrastructure matches the configuration.`); then the line `DISABLE-ROLLBACK-PLAN (-var dossier_refresh_schedule_state=DISABLED)` then the plan with that one `-var` (it must read `Plan: 0 to add, 1 to change, 0 to destroy.` with the schedule `state` ENABLED to DISABLED the only change);
   - `cn8_validate.out` = `terraform -chdir=infra/aws/terraform/harvest validate -no-color`.
f. Do not run `terraform apply`, `import`, `state`; do not commit a `.terraform` directory, a `.tfplan` binary or a lock-file change; check `git status` before every commit. If a plan reads otherwise than stated, DO NOT edit the Terraform, the plan command or an expectation to hide it: print the actual lines, file a row, report. A surprise is a row; keep working.

<paths>
infra/aws/terraform/harvest/dossier-refresh.tf
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~184/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/cn8_diff_check.py
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
# READ ONLY, change nothing: the harvest root loads these at terraform init
infra/aws/terraform/modules/
infra/aws/lambda/ci/
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cn-8"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~184/cn8_diff.out</invocation><expect>(?s)DIFF-CONTROL planted_resource_change_detected=yes\s+DIFF-CHECK schedule_default=ENABLED changed_lines=\d+ outside_allowed=0</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cn-8"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~184/cn8_plan.out</invocation><expect>(?s)DEFAULT-PLAN \(NO -var\)[^\n]*\n.*?No changes\. Your infrastructure matches the configuration\..*?DEFAULT-PLAN-EXIT=0.*?DISABLE-ROLLBACK-PLAN[^\n]*\n.*?Plan: 0 to add, 1 to change, 0 to destroy\.</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cn-8"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~184/cn8_validate.out</invocation><expect>(?m)^Success! The configuration is valid\.$</expect></criterion>
</proof_of_spec>

- AC1 proves the change is the default and comments only, with a negative control. AC2 proves the file equals the world (no-`-var` plan: nothing) and that the rollback still plans exactly one in-place change. AC3 proves the text is valid Terraform. **If a line reads otherwise, DO NOT edit the expectation, the Terraform or the plan command to hide it: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-19 ~18:0xZ):** AC1 FAILS as expected (`schedule_default=DISABLED`; the control fires), AC2 and AC3 FAIL as expected (`cat` of files that do not exist).
- **LINE ENDINGS:** edit so `git diff --stat` reads only what you changed (the tf file: a few insertions and deletions, none in a resource block); check it before you commit. The commit gate (terraform fmt and the naming gate) may refuse a file; fix the file, never force the commit. ASCII only.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W184-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~184/AMGT_HARVST.TO-HVST-cn-8.the-schedule-state-default-follows-the-applied-world-enabled.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cn-8.the-schedule-state-default-follows-the-applied-world-enabled` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cn-8.the-schedule-state-default-follows-the-applied-world-enabled.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's countersign of COO addendum 3 (`ledger/NEVER_WIDEN_CN7_ADDENDUM3_FLAG_DEFAULTS_CTO_COUNTERSIGN.md`, section "The schedule default, ruled: yes, ENABLED right after stage 5, by its own cell and addendum"; proof: a no-`-var` plan reading No changes; rollback stays DISABLED by `-var` apply). Preconditions measured by me before the cut (2026-10-19 ~18:0xZ): stage 5 DONE 16:57Z (SC1 msg 8401, ledger `harvst-cn7-s5-enable` closed `2a4e7e67b1`); I read the live schedule myself: `State ENABLED`, `cron(0 10 ? * MON-FRI *)`, `America/New_York`; `dossier-refresh.tf` sha256 at HEAD `8f7d3651c3` is `f6f72c3a4391eb36d4e1b6f2428600dc8b5b25b2de79458d19e1978a5756bc36` (the bytes bound by addendum 3).
- Decomposition: section 141 (addendum to section 140). Gate limb: the cell is NEWLY ADDED to an EXECUTING round; coverage is NOTED, not graded, at a recut (`/dispatch` Step 2).
- Risk class WORLD by the gate's `infra/` floor, not by effect: the cell applies nothing and calls no AWS write. I re-run the three checks myself at close.
- Known stale text left on purpose: the schedule resource's `description` attribute still says "(DISABLED by default)"; it is applied in AWS, and fixing it is a later in-place update under its own plan, not this cell.
- Needs after the merge: COO addendum 4 to the `cn-7` pair (the tf bytes change; countersign by `1.0.0_SA_CTO~DELL1`) BEFORE any seat plans the root from the merged bytes for an apply; the first scheduled fire (Tue 2026-10-20 14:00Z) does not depend on this file.
- Dry run at the base: all three criteria FAIL as expected.
- **FIRST PASS (issuer, 2026-10-19 ~18:4xZ):** worker `~184` built the edit (`ab70f25bcf`: default ENABLED, description, header comments; AC1 PASS by output, `changed_lines=11 outside_allowed=0`) and filed `D1-W184-S1` (BLOCKING) and `S2`: AC2 and AC3 could not run because MY sparse provisioning left out `infra/aws/terraform/modules/` (the harvest root sources `../modules/yang-lambda`), so `terraform init` failed. The miss is mine (I provisioned from `<paths>` and did not census what `init` loads). Fix: the worktree now holds `infra/aws/terraform/modules/` and `infra/aws/lambda/ci/` (the function-map folder the naming gate wanted); the order's `<paths>` names both read-only; the worker is continued to re-run init, validate and both plans and to regenerate AC2 and AC3 and the proof. `S1` and `S2` are dispositioned here as an issuer miss, not a product defect. Gate limb: none graded this modification (no new order file).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>99</round>
<workstream>SCHEDULE-DEFAULT</workstream>
<slot>184</slot>
<fabric>dell1</fabric>
