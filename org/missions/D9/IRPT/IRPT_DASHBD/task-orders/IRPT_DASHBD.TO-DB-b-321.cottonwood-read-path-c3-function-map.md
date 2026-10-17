# TO IRPT_DASHBD.TO-DB-b-321 -- C3 of the Cottonwood Performance read path: the FUNCTION-MAP. A new entry for `irpt-cot-reporting-read-lambda` that is the twin of the 49 Financial read entry, and the re-pin of `served.py` (which now carries the forward) in BOTH entries; nothing built for upload, nothing deployed (CTO ruling A, msg 10134) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-321</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~255</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTMAP</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/RULING_COTTONWOOD_READ_PATH_OPTION_A_20261017.md` @6bfcbcf2cc and the plan `COTTONWOOD_READ_PATH_PLAN_20261017.md` (cell C3; CTO msg 10176: the function-map is the layout, CLOUD retired the single source map) | **Decomp cell:** `DB-b-321` (decomposition section 181).

**Risk class WORLD** is the floor of the path (`infra/`): two JSON files in a branch. No build for upload, no AWS call, no Terraform command, no push. C1 (`served.py` with the forward) is landed at 3eb27c60c0; C2 (the Terraform root that reads this entry by the builder-derived name) is in flight as order DB-b-320. Nothing is deployed: the apply is the pair (C4).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-255` (branch `wk-IRPT_DASHBD-255`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~255/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the facts record and the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**The cell (`DB-b-321`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p187_cot_read_function_map.py` (your three criteria) and the issuer's REFERENCE DIFF `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/DB321_REFERENCE.patch` (two files, already green against the checker); the existing entry `infra/aws/lambda/ci/function-map/irpt-49f-reporting-read-lambda.json` and the sibling `irpt-cot-reporting-publish-lambda.json`.
2. **Apply the reference diff** (`git apply` from your worktree root, then read every hunk): (a) `irpt-49f-reporting-read-lambda.json` changes in ONE member only: the `served.py` member's `pin` becomes `3eb27c60c02d8900c7e7303453eeb9af328da819` (the trunk commit that carries the forward, DB-b-319) and its `sha256` becomes the sha256 of the file at HEAD; no deploy field moves (`artifact_sha256`, `last_deployed_*`, `recorded_by`, `deploy_ledger`, `deployed_code_sha256` stay); (b) a NEW file `irpt-cot-reporting-read-lambda.json` is the twin: the same `source_dir`, `files`, `pipeline` and the same 31 `staged_from` members (with the same re-pinned `served.py`), its own `tf_file`/`tf_resource` (the iso root's lambda module), `iam_role` `irpt-cot-reporting-read-role` and `artifact_s3_key` `investor-reporting/irpt-cot-reporting-read-lambda.zip`, and NO deploy field (the recorder writes them at the apply). Before you commit, verify the pin yourself: `git show 3eb27c60c02d8900c7e7303453eeb9af328da819:infra/aws/lambda/investor-reporting/_authz/served.py` hashed with sha256 must equal the member's `sha256` and the file at HEAD. If a hunk does not apply, or you think the reference is wrong, file a BLOCKING row and stop on it.
3. **Nothing else changes:** no other function-map file, no source file, no Terraform, no registry row.
4. **Run the checks yourself before the record**, from the MAIN tree's copy of the checker, by absolute path, against your worktree as the root: `python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p187_cot_read_function_map.py" C:/dev/wk-irpt-dashbd-255 DB187-1-AC1`, then AC2 (after the artifact commit), then AC3 (after the record; it runs the real build-only package of both entries, each a few minutes at most).
5. **Record** `RD_COT_READ_FUNCTION_MAP_FACTS_R150.json` in your folder with EXACTLY these fields: `entries` (`["irpt-cot-reporting-read-lambda", "irpt-49f-reporting-read-lambda"]`); `served_pin` (the 40-hex pin); `served_sha256` (the 64-hex sha256 of the file); `build_only_sha256` (the base64 hash the real build-only run printed, the same for both entries); `members` (the integer count of members in the built package); `words` (one paragraph, 80 to 1800 characters, no digit run of 8 or more: what changed and why, and what is NOT proven: nothing was uploaded or deployed, the two entries must move together in any later re-pin, the 49 Financial function's artifact differs from the deployed one only by the forward, and the new function does not exist yet).

<criterion id="DB187-1-AC1" cell_refs="DB-b-321"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p187_cot_read_function_map.py" C:/dev/wk-irpt-dashbd-255 DB187-1-AC1</invocation><expect>DB187-1-AC1 PASS</expect></criterion>
`DB187-1-AC1` -- the new entry: the agreed keys and tf fields and artifact key, no deploy field, and the 49 Financial entry's `source_dir`, `files` and `staged_from` member for member. Base: FAIL.
<criterion id="DB187-1-AC2" cell_refs="DB-b-321"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p187_cot_read_function_map.py" C:/dev/wk-irpt-dashbd-255 DB187-1-AC2</invocation><expect>DB187-1-AC2 PASS</expect></criterion>
`DB187-1-AC2` -- the re-pin: `served.py` in BOTH entries is pinned to an ancestor commit whose bytes equal the file at HEAD; the 49 Financial entry moved in that one member only (pin and sha256) and no other key. Base: FAIL.
<criterion id="DB187-1-AC3" cell_refs="DB-b-321"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p187_cot_read_function_map.py" C:/dev/wk-irpt-dashbd-255 DB187-1-AC3</invocation><expect>DB187-1-AC3 PASS</expect></criterion>
`DB187-1-AC3` -- the real build-only run through the function map for both entries prints ONE hash, each package equals its sources member for member, and the facts record equals it. Base: FAIL.

<expected_criteria>DB187-1-AC1,DB187-1-AC2,DB187-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. The build-only run writes a zip under the system temp folder and uploads nothing. No network, no AWS call, no Terraform command, no push. Writes: the two function-map files and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W255-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
infra/aws/lambda/ci/function-map/irpt-49f-reporting-read-lambda.json
infra/aws/lambda/ci/function-map/irpt-cot-reporting-read-lambda.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~255/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-321.cottonwood-read-path-c3-function-map.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 181 (round 150, workstream COTMAP), cell `DB-b-321`.
<owned_cells>DB-b-321</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB187-1-AC1, DB187-1-AC2, DB187-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~255/IRPT_DASHBD.TO-DB-b-321.cottonwood-read-path-c3-function-map.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB187-1-AC1,DB187-1-AC2,DB187-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the build-only hash and the member count in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two JSON files in a branch; nothing is built for upload, planned, applied or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes; the entry names the role the iso root creates.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green, the reference diff is committed beside the checker) and on single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>
