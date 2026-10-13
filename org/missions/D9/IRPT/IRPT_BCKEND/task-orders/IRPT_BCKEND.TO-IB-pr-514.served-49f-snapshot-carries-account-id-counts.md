# TO IRPT_BCKEND.TO-IB-pr-514 -- READ-ONLY, COUNTS ONLY: the latest served 49 Financial HoldingsSnapshot built on the new package carries `account_id` on its ACCOUNT nodes (CTO RE 7016, round 180 item 1)

<to_id>IRPT_BCKEND.TO-IB-pr-514</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~364</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>180</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's RE 7016 ("Round 180, item 1 (read-only, counts only): read the latest served 49F HoldingsSnapshot built on UHOCIkWj. Report ACCOUNT nodes total; those with account_id; those whose account_id is in the landed directory population; those without, by reason. The negative arm is the pre-release snapshot reading 0 with account_id.") | **Decomp cell:** `IB-pr-514` (decomposition section 172) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-514` (inlined):** the 49 Financial builder's host package (VersionId `UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD`, put 2026-10-13T13:35:24Z) carries the additive `account_id` member on each 49F ACCOUNT node (merged IB-pr-493). The holdings refresh ran on it at 14:15:25 to 14:20:49Z (SSM invocation `4f958436`). **Nobody has read the snapshot it published.** READ it and report COUNTS ONLY. **READ ONLY: no write to any AWS service, no host start, no deploy. Client data: the snapshot holds account ids; they stay IN MEMORY of your script. You print and record counts and revision names ONLY; no id, mask, name, balance or figure, and no scratch file or copy of the snapshot (the prior art, `deliverables/0.9.0_WK_IRPT_BCKEND~345/mismatch_count.py`, does this with boto3 GET/HEAD/LIST: copy its habits and the builder's own helpers).**

**Do:**
1. **Find the served snapshots.** Read `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` `land()` and `infra/aws/lambda/investor-reporting/holdings/publication.py` for the publication layout (the firm's bucket, `platinum/holdings/date=<as_of>/<revision>.json` and its `.manifest.json`, the `current` pointer). With `s3 list/head` only, list the 49financial publication objects and record for each candidate its `LastModified`. The POSITIVE snapshot is the latest served one whose `LastModified` falls in the 14:15Z build's window (2026-10-13T14:15:25Z to 14:30:00Z); the NEGATIVE ARM is the latest served snapshot written BEFORE 2026-10-13T13:35:24Z (the pre-release builder). If no snapshot falls in the window, STOP and report (the build may not have published).
2. **Count the positive snapshot** (GET into memory only): `account_nodes_total` (nodes with `node_kind` ACCOUNT), `with_account_id` (those carrying the `account_id` member), `in_directory_population` (those whose `account_id` is in the landed directory's account-id population for 49financial, loaded with the builder's own `holdings_snapshot._directory_account_ids(s3, bucket, firm_id)` or the same read), and `without_account_id` `{total, by_reason}` where the reasons come from the builder's own census if the snapshot or its manifest records them (`account_id_member_omitted`, with its reason keys), else computed by the builder's rule (neither candidate key is in the directory; both candidate keys are: ambiguous; no directory landed). Name each reason by the builder's own word.
3. **Count the negative arm** the same way: `account_nodes_total` and `with_account_id` (expected 0).
4. **Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~364/IB180-1_served_account_id_read.json`: `{"positive":{"revision":"<the object name, a hash>","last_modified_utc":"...","built_in_invocation":"4f958436 (by window)","account_nodes_total":N,"with_account_id":a,"in_directory_population":b,"without_account_id":{"total":c,"by_reason":{"<reason>":n}}},"negative_arm":{"revision":"...","last_modified_utc":"...","account_nodes_total":M,"with_account_id":0},"directory":{"object_last_modified_utc":"...","population":D},"reading":"two sentences","aws_writes_made":0,"objects_uploaded":0,"functions_invoked":0,"hosts_started":0,"accounts_written":0,"figures_written":0,"files_deleted":0}`. The record carries no key beyond the two revision names, no id, no digit run of 9 or more digits.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB180-1-AC1" cell_refs="IB-pr-514"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r180/p180_cells.py" . IB180-1-AC1</invocation><expect>IB180-1-AC1 PASS</expect></criterion>
<criterion id="IB180-1-AC2" cell_refs="IB-pr-514"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r180/p180_cells.py" . IB180-1-AC2</invocation><expect>IB180-1-AC2 PASS</expect></criterion>
<criterion id="IB180-1-AC3" cell_refs="IB-pr-514"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r180/p180_cells.py" . IB180-1-AC3</invocation><expect>IB180-1-AC3 PASS</expect></criterion>

<expected_criteria>IB180-1-AC1, IB180-1-AC2, IB180-1-AC3</expected_criteria>

What the checks grade: AC1 the arithmetic (`with_account_id` + `without_account_id.total` = `account_nodes_total`; `in_directory_population` no more than `with_account_id`; the reasons sum to the total), the positive snapshot written in the build window, the negative arm written before the package was put; AC2 no account content (no id, no `account_number`, `masks`, `node_id`, no digit run of 9 or more); AC3 the CTO's reading: `with_account_id` above 0, `in_directory_population` equal to `with_account_id`, the negative arm reading 0, the seven bound counters 0. **If AC3 fails because the release wrote NO `account_id` (or one outside the directory), that is the FINDING: record it as it reads, file a row, and report; do not edit a record to pass.** Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and read-only AWS calls (`s3api list-objects-v2`, `head-object`, `get-object` into memory, `s3 ls`). No write, no copy of a snapshot to disk, no host start, no deploy, no Lambda invoke.
- **Refusal clause:** STOP, file a row, change nothing more, if no snapshot falls in the build window, if your script would need to print or store an id or any account content, or the directory cannot be read.
- **Row ids** are `IRPT_BCKEND-D2-W364-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~364/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-514.served-49f-snapshot-carries-account-id-counts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 172 (round 180, workstream ~P), cell `IB-pr-514`.
<owned_cells>IB-pr-514</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB180-1-AC1, IB180-1-AC2, IB180-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~364/IRPT_BCKEND.TO-IB-pr-514.served-49f-snapshot-carries-account-id-counts.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read-only: the order reads one served snapshot and one directory object of the 49financial bucket in memory and records counts; nothing is written or copied.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; read calls under the session's existing principal.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched and the host is not started.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p180_cells.py dry-run at base on dell2 2026-10-13 ~15:3xZ: IB180-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic record (10 nodes, 8 with account_id, all in the directory, a pre-release arm reading 0) in a path the run itself created passes all three, and the path was removed.
lane: the paths block IS the grant; worker slot ~364 of IRPT_BCKEND. Class SERVED.
</preflight>
