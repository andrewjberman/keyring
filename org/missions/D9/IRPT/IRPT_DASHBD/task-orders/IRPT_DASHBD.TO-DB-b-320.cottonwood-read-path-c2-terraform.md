# TO IRPT_DASHBD.TO-DB-b-320 -- C2 of the Cottonwood Performance read path: the TERRAFORM. A new root `reporting-read-iso` with the Cottonwood read function and its `-cot-` role, and in the `reporting-read` root the forward target's name and ONE `lambda:InvokeFunction` statement; no route, no S3 widening, nothing planned or applied (CTO ruling A, msg 10134) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-320</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~254</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTTF</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/RULING_COTTONWOOD_READ_PATH_OPTION_A_20261017.md` @6bfcbcf2cc (A ruled; the Cottonwood function has its own `-cot-` role, so the Cottonwood bucket fence `DenyForeignFirmPrincipals` is untouched; the 49F role gains `lambda:InvokeFunction` on that ONE function and no S3; the API route is unchanged) and the plan `COTTONWOOD_READ_PATH_PLAN_20261017.md` (cell C2) | **Decomp cell:** `DB-b-320` (decomposition section 180).

**Risk class WORLD** is the floor of the path (`infra/`): Terraform files in a branch. The box has no terraform binary: nothing is validated by the tool, planned, applied or pushed. The apply is the pair (C4). The function-map entry of the new function is the NEXT cell's (C3, after C1 lands): the new root reads it by the builder-derived name, so the root cannot plan until it exists, and this order does not create it.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-254` (branch `wk-IRPT_DASHBD-254`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~254/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the facts record and the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**The cell (`DB-b-320`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p186_cot_read_terraform.py` (your three criteria) and the issuer's REFERENCE DIFF `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/DB320_REFERENCE.patch` (six files, already green against the checker); the existing roots `infra/aws/terraform/investor-reporting/reporting-read/` (`locals.tf`, `lambda.tf`, `iam.tf`) and `reporting-publish-iso/` (`locals.tf`, `lambda.tf`), the two templates the reference follows.
2. **Apply the reference diff** (`git apply` from your worktree root, then read every hunk): it creates `infra/aws/terraform/investor-reporting/reporting-read-iso/` (`main.tf`, `locals.tf`, `lambda.tf`, `iam.tf`), creates `infra/aws/terraform/investor-reporting/reporting-read/forward.tf`, and adds ONE environment variable (with its comment) to `reporting-read/lambda.tf`. What it means: (a) the iso root derives the firm, both buckets, the directory map and the artifact key; names every resource through `opal_name` (the role name carries the firm's scope token, which is what the bucket fence admits); the function has only `IRPT_DIRECTORY_BUCKET_MAP` and `IRPT_FIRM_REGISTRY` in its environment and NEVER the forward variable; its role reads and lists only the platinum reporting prefix and reads the directory and ownership-map objects (an absent map reads as an empty map), plus the service-profile read of the shared guard; there is no route, schedule, topic, mail or permission resource; (b) `forward.tf` names the forward target by the same derivation and gives the 49 Financial role exactly one statement, `lambda:InvokeFunction` on that one function's ARN, and no S3 action; (c) `lambda.tf` of the 49 Financial root gains the single line `IRPT_FORWARD_COTTONWOOD_FUNCTION = module.irpt_reporting_read_forward_target_name.name`. If a hunk does not apply, or you think the reference is wrong, file a BLOCKING row and stop on it.
3. **Nothing else changes:** no other file under `infra/`, no function-map file, no Python, no registry row, no portal file.
4. **Run the checks yourself before the record**, from the MAIN tree's copy of the checker, by absolute path, against your worktree as the root: `python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p186_cot_read_terraform.py" C:/dev/wk-irpt-dashbd-254 DB186-1-AC1`, then AC2, then AC3. (AC2 and AC3 read your commits: commit the artifact files first, then run AC2; AC3 needs the record, so run it after the record is written.)
5. **Record** `RD_COT_READ_ISO_FACTS_R150.json` in your folder with EXACTLY these fields: `iso_root` (the root path, with its trailing slash); `names` (the five builder names, in this order: the iso function, the iso role, the iso policy, the iso service-profile policy, the 49 Financial forward policy); `iso_resources` (the five addresses the iso plan will add: the function and the log group inside the module, the role, and the two role policies); `iso_plan` (`{"add": 5, "change": 0, "destroy": 0, "claim": "inferred"}`); `read_root_plan` (`{"add": 1, "change": 1, "destroy": 0, "claim": "inferred", "change_is": "<words: what the one in-place change is>"}`); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was validated by terraform or planned, the iso root cannot plan until the function-map entry of the new function exists (the next cell), the artifact differs only when the pinned served.py moves, and the claims are inferred).

<criterion id="DB186-1-AC1" cell_refs="DB-b-320"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p186_cot_read_terraform.py" C:/dev/wk-irpt-dashbd-254 DB186-1-AC1</invocation><expect>DB186-1-AC1 PASS</expect></criterion>
`DB186-1-AC1` -- the iso root's HCL: exactly the four files; one role and two role policies and no other resource type; one yang-lambda module (29 s, 512 MB, no layer, no reserved concurrency) reading its artifact key from the function map; exactly the two environment keys and never the forward variable; four builder-named resources with the derived scope; exactly the expected statement ids and explicit allowed actions, no write; no typed firm token or bucket; the right state key. Base: FAIL.
<criterion id="DB186-1-AC2" cell_refs="DB-b-320"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p186_cot_read_terraform.py" C:/dev/wk-irpt-dashbd-254 DB186-1-AC2</invocation><expect>DB186-1-AC2 PASS</expect></criterion>
`DB186-1-AC2` -- the forward half: the change touches only the iso root, `forward.tf`, `lambda.tf` and the worker's own folder; `forward.tf` holds one role policy with one `lambda:InvokeFunction` statement on the one builder-named target (no S3, no wildcard); `lambda.tf` of the 49 Financial root only gained the forward variable line. Base: FAIL.
<criterion id="DB186-1-AC3" cell_refs="DB-b-320"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p186_cot_read_terraform.py" C:/dev/wk-irpt-dashbd-254 DB186-1-AC3</invocation><expect>DB186-1-AC3 PASS</expect></criterion>
`DB186-1-AC3` -- the five names equal the builder recount; the REAL naming gate (plan mode) grades the four iso resources and the forward policy CONFORMANT; the facts record is complete. Base: FAIL.

<expected_criteria>DB186-1-AC1,DB186-1-AC2,DB186-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the iso root, `forward.tf`, `lambda.tf` of the 49 Financial root and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W254-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
infra/aws/terraform/investor-reporting/reporting-read-iso/main.tf
infra/aws/terraform/investor-reporting/reporting-read-iso/locals.tf
infra/aws/terraform/investor-reporting/reporting-read-iso/lambda.tf
infra/aws/terraform/investor-reporting/reporting-read-iso/iam.tf
infra/aws/terraform/investor-reporting/reporting-read/forward.tf
infra/aws/terraform/investor-reporting/reporting-read/lambda.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~254/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-320.cottonwood-read-path-c2-terraform.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 180 (round 150, workstream COTTF), cell `DB-b-320`.
<owned_cells>DB-b-320</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB186-1-AC1, DB186-1-AC2, DB186-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~254/IRPT_DASHBD.TO-DB-b-320.cottonwood-read-path-c2-terraform.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB186-1-AC1,DB186-1-AC2,DB186-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the number of resources the iso root adds and the one change the 49 Financial root makes, in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: Terraform files in a branch; nothing is planned, applied, uploaded, scheduled or deployed (the box has no terraform binary).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied and no grant changes in AWS; the statements are new and explicit (listed in the checker); the Cottonwood bucket fence admits the new execution role by its `-cot-` token and the 49 Financial role gains no S3 action, only lambda:InvokeFunction on one function.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the API wiring is untouched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green, the reference diff is committed beside the checker) and on thirty single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>
