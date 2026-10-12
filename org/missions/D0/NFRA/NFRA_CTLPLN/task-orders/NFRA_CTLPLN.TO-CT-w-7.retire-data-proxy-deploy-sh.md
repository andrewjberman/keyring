# TO NFRA_CTLPLN.TO-CT-w-7 -- workstream HYGIENE round 1 (cell CT-w-7 of the round-8 decomposition): retire the data proxy's legacy deploy.sh

<to_id>NFRA_CTLPLN.TO-CT-w-7</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~69</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>HYGIENE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-7` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`, the added row) | **outcome_ref:** FWD-28 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/portal_data_proxy/deploy.sh` is a legacy hand-deploy script: it copies only `lambda_function.py` and `session_tracker.py` into a zip and calls `aws lambda update-function-code`, which CLAUDE.md forbids (Lambda code moves by Terraform only). Since the data proxy now imports `firm_page_access.py` at load, a zip built by that script cannot import. The CTO has ruled (msg 108501): RETIRE it. This is a repo delete (recoverable from git) and needs no other word.

### DO

1. Delete `infra/aws/lambda/portal_data_proxy/deploy.sh` (`git rm` through your commit).
2. Read `infra/aws/lambda/portal_data_proxy/README.md` (57 lines; it tells a reader to run `./deploy.sh` through `safe-lambda-deploy.sh`). Replace its deploy instructions with ONE line: `Deploy: Lambda code moves by Terraform only. Build the code-only zip from the entry for opal-portal-data-proxy in infra/aws/lambda/ci/lambda-source-map.json (its files list is the zip's member list), then safe-apply infra/aws/terraform/market-overview/. deploy.sh was retired 2026-10-12 (CTO msg 108501).` Keep any line of the README that is NOT about deploying (a description of what the function serves), and say in your report which lines you kept and which you removed.
3. Search the repo ONLY by the comp-tools or native Grep for any other reference to `portal_data_proxy/deploy.sh` or `./deploy.sh` for this function (the README has some; `safe-lambda-deploy.sh` may name the path). Report every hit with file and line. Do NOT edit any file other than the two above; if another file names the script, file ONE surprise row naming it and keep working.

### RULES

Write surface is exactly the `<paths>`. No aws call, no terraform, no deploy, no push. Use `.tools/safe-commit.sh`. No non-ASCII added. Do NOT commit the `portal` gitlink. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to the surprise-channel file (id `NFRA_CTLPLN-W69-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw7-AC1" cell_refs="CT-w-7"><invocation>test -e infra/aws/lambda/portal_data_proxy/deploy.sh; echo exists=$?</invocation><expect>exists=1</expect></criterion>
`CTw7-AC1` -- the script is gone (exit 1 from `test -e`).

<criterion id="CTw7-AC2" cell_refs="CT-w-7"><invocation>grep -c "safe-apply" infra/aws/lambda/portal_data_proxy/README.md</invocation><expect>1</expect></criterion>
`CTw7-AC2` -- the README carries the pointer exactly once.
</proof_of_spec>

<expected_criteria>CTw7-AC1,CTw7-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~69/NFRA_CTLPLN.TO-CT-w-7.retire-data-proxy-deploy-sh.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTw7-AC1,CTw7-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-7</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/portal_data_proxy/deploy.sh
infra/aws/lambda/portal_data_proxy/README.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- another script or doc still pointing at the deleted file (step 3 reports every hit; a hit outside the two files is a surprise row, not an edit); a README that loses a non-deploy fact (the worker keeps those lines and reports); BLIND: operators who run the script from memory.
risk: WORLD is declared because the L6 gate derives a floor from the infra paths; this cell deletes one script and edits one README.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 108501 (retire deploy.sh by a hygiene cell); row NFRA_CTLPLN-W65-S4.
