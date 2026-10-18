# AMGT_HARVST task order -- `HVST-cm-2` -- ROUND 98, workstream PULLENQ-MAP: THE `opal-research-pull-enqueue` LAMBDA HAS A SOURCE-MAP ROW THAT MAPS ITS DEPLOYED BYTES TO ITS SOURCE (row `D1-S62`; CTO round-97 analysis item 2; the deploy-integrity rule)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cm-2.the-pull-enqueue-lambda-has-a-source-map-row-that-maps-its-deployed-bytes-to-its-source</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~176</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY AWS reads ONLY: `lambda get-function-configuration` (or `get-function`) of `opal-research-pull-enqueue`, through the `.tools/aws` shim (never a bare `aws`); never `update-function-code`, `invoke`, `put`, `delete`, `terraform` or any write; NO edit outside `<paths>`; NO build, upload or deploy; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a row whose `deployed_code_sha256` was copied from this order instead of read from the live function, a row that maps a hash to a source file that has since changed (the source md5 is printed from the file at HEAD, not typed), a check that cannot see a wrong hash (it has a negative control), a row written for a different function name or file name, a change to any other function's row, a run of `record-terraform-deploy.sh` or any apply (not yours), a `last_deployed_commit` that is HEAD or the merge instead of the commit the recorder's own rule picks, and a commit that the naming gate refuses and that is then forced.
</preflight>

## 0. THE CELL

The Lambda `opal-research-pull-enqueue` was redeployed by Terraform at 2026-10-18 15:24:23Z (`HVST-cl-2`; live `CodeSha256` `7c4gYrZHxrNDhf2bqv3wo2JTUWdUxt/BeDFQsp33fx4=`; the one-file zip `research/opal-research-pull-enqueue.zip` in the bucket `opal-313476888478-lambda-artifacts`; its source `infra/aws/lambda/research/pull_enqueue/lambda_function.py`, md5 `45c83ddf74640e90368e8bebf712b52c` at the merge `349e7ee0da`). The deploy-integrity rule maps every Lambda to its build input in `infra/aws/lambda/ci/function-map/<function-name>.json`; this function HAS NO ROW, so `infra/aws/lambda/ci/record-terraform-deploy.sh` refused to stamp its deploy (row `D1-S62`). **This cell adds the row, so that the deployed bytes can be diffed against the source.** It changes no code and deploys nothing.

## 1. THE BUILD (one new JSON file and one read-only check script)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `infra/aws/lambda/ci/function-map/README.md`, `infra/aws/lambda/ci/function-map/opal-ticket-api.json` (a Terraform-managed one-file Lambda built by the same `build-and-upload.sh` family: your MODEL for the fields), `lib/opal_lambda_map.py` (`load_entry`, `load_all` and what it requires of a row), `infra/aws/lambda/ci/record-terraform-deploy.sh` (how it picks a row by `pipeline` and sets `last_deployed_commit`: the last commit touching the row's `source_dir`, NOT HEAD), `infra/aws/terraform/harvest/api-gateway.tf` (the module block `harvest_enqueue`) and `infra/aws/terraform/harvest/build-and-upload.sh`. Print what you learned about the `pipeline` value the recorder expects for a harvest-folder function (the Terraform folder is `infra/aws/terraform/harvest`).
b. **Write `infra/aws/lambda/ci/function-map/opal-research-pull-enqueue.json`** (the file name IS the function name; the object has no wrapper) with: `source_dir` `infra/aws/lambda/research/pull_enqueue`; `files` `["lambda_function.py"]` (the zip holds that one file); `pipeline` the value you printed in step a (if the recorder's selection cannot name this function by any `pipeline` value, STOP, file a row and report); `tf_file` `infra/aws/terraform/harvest/api-gateway.tf`; `tf_resource` `module.harvest_enqueue.aws_lambda_function.this`; `artifact_s3_key` `research/opal-research-pull-enqueue.zip`; `artifact_sha256` and `deployed_code_sha256` both READ FROM THE LIVE FUNCTION (the `CodeSha256` that `lambda get-function-configuration` prints, which the issuer read as `7c4gYrZHxrNDhf2bqv3wo2JTUWdUxt/BeDFQsp33fx4=`; if it reads differently, use what you read and say so in a row); `last_deployed_commit` computed with the recorder's own rule (the last commit touching `source_dir` on the branch you are on: print the command and its output); `last_deployed_at` the function's `LastModified` as UTC (issuer's read: 2026-10-18T15:24:23Z); `deploy_ledger` `harvst-cl2-pull-enqueue-canonical-status`; `recorded_by` a short string saying the row was hand-written by `HVST-cm-2` from a read of the live function and that the recorder updates it at the next apply. Add a short `_note` (the deploy, the ledger, what was verified: the deployed entry's sha256 `ad395e19c80e801a91042b550299866c2a86301f268846e7cf274f0d347ef2f3` equals the source file's, per the seat's read). Match the other rows' formatting (key order, indent) so the diff is only the new file. **Do not edit any other function's row.**
c. **Write `cm2_row_check.py`** in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `cm2_row_check.out` (open it with `newline="\n"`): (1) load the row with `lib.opal_lambda_map.load_entry("opal-research-pull-enqueue")`; (2) compute the md5 of `<source_dir>/lambda_function.py` at HEAD, and the sha256 of the same file; (3) read the LIVE `CodeSha256` (read-only, through the `.tools/aws` shim); (4) print exactly `ROW-MAPS function=opal-research-pull-enqueue deployed_code_sha256=<the row's> source_md5=<the md5> live_code_sha256=<the live one> equal=<yes if the row's value equals the live value, else no>`; (5) **the negative control:** run the SAME comparison on an in-memory copy of the row with one character of `deployed_code_sha256` changed and print `CONTROL-NEGATIVE planted_wrong_sha equal=no` (the word `no` is the comparator's output); (6) run `comp-lambdamap check` and `comp-lambdamap sha` (both read-only; `| grep opal-research-pull-enqueue` is allowed as a pipe receiver) and print each as `LAMBDAMAP-CHECK <tool output lines for this function, or none>` and `LAMBDAMAP-SHA <the same>`; print `LAMBDAMAP-DRIFT function=opal-research-pull-enqueue drift=<none if neither tool names this function as drifting, else the text>` (read the tools' output format first; if a tool cannot be run read-only, say why in the line and do not guess).
d. Do not run `record-terraform-deploy.sh`, `terraform`, any build, upload or deploy. A surprise is a row; keep working.

<paths>
infra/aws/lambda/ci/function-map/opal-research-pull-enqueue.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~176/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cm-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~176/cm2_row_check.out</invocation><expect>(?m)^ROW-MAPS function=opal-research-pull-enqueue deployed_code_sha256=(\S+) source_md5=45c83ddf74640e90368e8bebf712b52c live_code_sha256=\1 equal=yes$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cm-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~176/cm2_row_check.out</invocation><expect>(?m)^CONTROL-NEGATIVE planted_wrong_sha equal=no$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cm-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~176/cm2_row_check.out</invocation><expect>(?m)^LAMBDAMAP-DRIFT function=opal-research-pull-enqueue drift=none$</expect></criterion>
</proof_of_spec>

- AC1 is the CTO's grade (`CodeSha256` maps to the source md5): the `\1` makes the row's hash equal the live hash, and the source md5 is the merged one. AC2 is the control (the comparator sees a planted wrong hash). AC3 is the repository's own drift tools reading no drift for this function. **If a line reads otherwise, DO NOT edit the expectation, the row or the script to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~16:3xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W176-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for your row id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~176/AMGT_HARVST.TO-HVST-cm-2.the-pull-enqueue-lambda-has-a-source-map-row-that-maps-its-deployed-bytes-to-its-source.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cm-2.the-pull-enqueue-lambda-has-a-source-map-row-that-maps-its-deployed-bytes-to-its-source` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cm-2.the-pull-enqueue-lambda-has-a-source-map-row-that-maps-its-deployed-bytes-to-its-source.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- **LINE ENDINGS:** edit so `git diff --stat` reads only what you changed; check it before you commit. The naming gate may refuse a commit in a sparse tree; if it does, report the refusal and the exact text, do NOT force it.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-97 analysis (`ledger/ROUND_ANALYSIS.round97.md` @ea9f1e5ef6, msg 8125) item 2 ("add the `pull_enqueue` Lambda's source-map row, so its deployed bytes diff against its build input (the deploy-integrity rule); grade: `CodeSha256` `7c4gYrZH..` maps to the source md5 `45c83ddf..`").
- **Class `WORLD` is the L6 gate's floor for an `infra/` path, not a deploy.** The row is hand-written once from a read of the live function; the recorder updates it at the next apply.
- Chain B of round 98, slot ~176, worktree `C:/dev/wk-harvst-176`, branch `wk-AMGT_HARVST-176`. **Sparse set at provision (each named file CHECKED BY NAME after the add, not counted):** `.claude/agents`, `lib` (`opal_lambda_map.py`, `trading_calendar.py` and the naming files the commit gate reads), `infra/aws/lambda/ci`, `infra/aws/lambda/research/pull_enqueue`, `infra/aws/terraform/harvest`, `infra/logic`, `org/standards`.
- **SENT:** with the round-98 issuance.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>98</round>
<workstream>PULLENQ-MAP</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
