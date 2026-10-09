# TO IRPT_BCKEND.TO-IB-pr-388 -- H1: the analysis READY event to the commentary Lambda as DESIRED Terraform (stream, filtered mapping, exact grant); applied later by IRPT_ANLREQ

<to_id>IRPT_BCKEND.TO-IB-pr-388</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~199</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>97</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msgs 1778, 2192 and 2507 (a); ~T2 READY-event contract v1 @98ca40fd4c | **Decomp cell:** `IB-pr-388` (decomposition section 90) |
**outcome_ref:** NFRA_TRNSPT FWD-10 C-TRIGGER (owned by IRPT_ANLREQ under C-ABSORB (d)) | **depends_on:** the drained code cells named below. Nothing here is applied; the pairs are signed after IB-pr-383 closes.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-199` (branch `wk-IRPT_BCKEND-199`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell (CTO msgs 1778, 2192, 2507).** H1 sends the analysis report's READY event to `outlook-global-commentary-draft-lambda`.
It belongs to IRPT_ANLREQ, which applies it under its own pair. ~P builds it now as DESIRED Terraform: NOTHING is planned against the
live backend, applied or uploaded.
- **Contract:** ~T2's READY-event contract v1 (@98ca40fd4c). Producer facts are in
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/H1_READY_PRODUCER_FACTS_20261008.md`.
- **The consumer:** `infra/aws/terraform/transcripts/commentary.tf` (~T2, d153aeaba0). Its names are in
  `data/transcripts/scripts/commentary/NAMES.json` (lib/opal_naming.py output). It leaves the event-source mapping and the stream grant
  to the stream owner.

**Build:**
1. `infra/aws/terraform/investor-reporting/core/dynamodb.tf`, table `requests`: add `stream_enabled = true` and
   `stream_view_type = "NEW_IMAGE"`, plus an output for its `stream_arn`.
2. A new `core/ready_trigger.tf` holds ONE `aws_lambda_event_source_mapping`:
   - the requests stream to the commentary function;
   - the function's name comes from the builder, never a hand-typed literal (rule 30 REFUSES at commit);
   - `starting_position = "LATEST"`, a bounded `maximum_retry_attempts`, and `bisect_batch_on_function_error`;
   - `destination_config.on_failure` is the commentary DLQ;
   - `filter_criteria`: eventName INSERT, `keys.request_revision.S` prefix `REPORT#`, and `NewImage.ref.M.report_kind.S` = `ANALYSIS`.
3. One `aws_iam_role_policy` on the commentary role, by builder name:
   - `dynamodb:DescribeStream`, `GetRecords`, `GetShardIterator` and `ListStreams` on `aws_dynamodb_table.requests.stream_arn`;
   - `kms:Decrypt` on `aws_kms_key.irpt.arn`;
   - nothing else.
4. `terraform fmt` the files you touch. Do not reformat other core files.

No alarm, SNS, SES or monitor. Note in your report whether the commentary role already has `sqs:SendMessage` on its DLQ
(commentary.tf:78); if not, file a row.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB97-1-AC1" cell_refs="IB-pr-388"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_h1.py" . IB97-1-AC1</invocation><expect>IB97-1-AC1 PASS</expect></criterion>
<criterion id="IB97-1-AC2" cell_refs="IB-pr-388"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_h1.py" . IB97-1-AC2</invocation><expect>IB97-1-AC2 PASS</expect></criterion>
<criterion id="IB97-1-AC3" cell_refs="IB-pr-388"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r97/p97_h1.py" . IB97-1-AC3</invocation><expect>IB97-1-AC3 PASS</expect></criterion>

<expected_criteria>IB97-1-AC1, IB97-1-AC2, IB97-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No upload, apply or deploy; BUILD_ONLY and offline replays only. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W199-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~199" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~199@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~199 <0.9.0_WK_IRPT_BCKEND~199@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/terraform/investor-reporting/core/dynamodb.tf
infra/aws/terraform/investor-reporting/core/ready_trigger.tf
infra/aws/terraform/investor-reporting/core/outputs.tf
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-388.h1-ready-event-trigger-desired-terraform.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~199/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 90 (round 97, workstream ~P), cell `IB-pr-388`.
<owned_cells>IB-pr-388</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB97-1-AC1, IB97-1-AC2, IB97-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~199/IRPT_BCKEND.TO-IB-pr-388.h1-ready-event-trigger-desired-terraform.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msgs 1778, 2192 and 2507 (a); ~T2 READY-event contract v1 @98ca40fd4c; code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p97_h1.py dry-run at base 6dea768ce8 on dell2 2026-10-09 ~05:0xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control, surface file FAIL (absent); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msg 2507); release pairs signed after IB-pr-383 closes.
</preflight>
