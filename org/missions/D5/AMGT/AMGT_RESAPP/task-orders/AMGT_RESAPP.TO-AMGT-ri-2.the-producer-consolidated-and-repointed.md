# AMGT_RESAPP task order -- `AMGT-ri-2` -- THE PRODUCER, CONSOLIDATED AND REPOINTED -- the chatter axis writes again

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ri-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~17</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~17`.** Work ONLY in the worktree whose absolute path is given to you in your
spawn prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/` and `.tools/` exist;
if either is absent, STOP with a BLOCKING row. **YOU HOLD A QUEUE OF TWO ORDERS (`ri-2`, then `ri-4`); this is the
first.** Both act on ONE terraform root (`infra/aws/terraform/harvest/`) and ONE remote state (`harvest/tfstate`),
which is why they are one worker's queue. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~17;`.

⛔ **THIS CELL CHANGES THE WORLD (an IAM policy, a Lambda's code, six resources' state ownership). It is ORDERED:
open the deploy-completion entry AND COMMIT ITS SENTINEL, act, close the entry, COMMIT the close, THEN take the
grading reads.** A death after the act and before the commit leaves the world changed and the record silent.
Before your FIRST `safe-apply`, write your serial into the halt gate's session file:
`printf '%s' 0.9.0_WK_AMGT_RESAPP~17 > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"` (that path is in your
grant; the gate reads it; it is last-writer-wins across this session's workers, so write it right before the
apply). Run the apply with `HALT_ACK=1`.

## 1. THE CELL, inlined in full -- `AMGT-ri-2` (row `Z-S88`; an EXISTING-cell recut of `AMGT-rd-5`; cites `C-S49`, `Z-S12`)

**THE PRODUCER FIRES EVERY DAY AND FAILS EVERY FIRE.** `1.0.0_SA_CTO~W` measured it on the live plane
(2026-09-14 ~23:2xZ, row `AMGT_RESAPP-Z-S88`): Lambda `amgt-resapp-chatter-axis` is Active, its EventBridge
Scheduler schedule `amgt-resapp-chatter-axis-daily` (`cron(0 10 * * ? *)` UTC, group `default`) is ENABLED, and
3 of 3 invocations on 2026-09-14 end in `[ERROR] ResourceNotFoundException ... Query ... Requested resource not
found` at `lib/research/metrics/chatter_axis.py:153 default_article_count`. The metrics table
`opal-harvest-security-metrics` holds 52 rows on three axis_dates (`CHATTER#2026-09-11` 10, `PRICE#2026-09-10` 32,
`TRENDING_CHATTER#2026-09-12` 10) and NOTHING after 09-12. **The Lead Panel reads today's partition and finds
nothing, for a reason that is neither the frontend nor the day.**

**THE CAUSE, MEASURED AT THIS CUT (2026-09-15 00:0x-00:1xZ), so you re-ground rather than re-derive:**
- The live role policy `amgt-resapp-chatter-axis-lambda-policy` still names
  `arn:...:table/opal-amgt-articles` (+ its `ticker_date_index`) and `arn:...:table/opal-amgt-security-metrics`.
  BOTH TABLES WERE DELETED in the 2026-09-11 harvest migration; the live tables are `opal-harvest-articles` and
  `opal-harvest-security-metrics` (`infra/aws/terraform/harvest/dynamodb.tf`).
- HEAD's `lib/research/metrics/chatter_axis.py` ALREADY defaults to the harvest names (`:109` `HARVEST_ARTICLES_TABLE`,
  `:111` `HARVEST_METRICS_TABLE`). The traceback's line numbers (153/168/304) do not exist at HEAD (235/243/403):
  the DEPLOYED ZIP predates the code flip. Live: `CodeSha256 TtTSpotkwWuVuMFbPv0RWTv2zqqifa/xfHQtBtuo924=`, 13572 B,
  `LastModified 2026-09-11T18:13:38Z`, `Environment null`.
- `infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf` (the declaration) grants the two old ARNs and
  references `aws_dynamodb_table.security_metrics.arn`, a resource declared ZERO times in the estate -- the module
  cannot plan (row `C-S49`, `4.0.0_SA_CRO~Z`'s, OPEN since round 5; decomposition s.14d). Its sibling `main.tf`
  carries backend key `amgt-resapp/tfstate`, whose state (serial 1) tracks ONE resource, the DELETED
  `opal-amgt-articles` -- a plan there would RECREATE that table under the old name.
- The six live producer resources (function, two roles, two role policies, the schedule) are tracked in a THIRD
  state, `amgt-resapp/rd-2-security-metrics/tfstate` (serial 3), beside the deleted metrics table, and in NEITHER
  `harvest/tfstate` (serial 25) nor `amgt-resapp/tfstate`. No root at HEAD points at that third key.

**AMENDED 2026-09-15 ~02:0xZ ON ROW `AMGT_RESAPP-Z-W17-S2` (the worker's refusal, correct): THIS ROOT CANNOT IMPORT OR PLAN
UNTIL THE MOUNT'S ARTIFACT EXISTS.** `module.scoped_amgt_api.data.aws_s3_object.artifact` (scoped-amgt-api.tf) reads
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` at EVALUATION time, and that key is a 404 until
it is uploaded -- so `terraform import` and `terraform plan` both fail before touching anything. The issuer sequenced ri-2
before ri-4 in one root and that was backwards for this one step. **So this order now carries two preconditions of its
own, AC11 and AC12 (the never-widen co-sign gate and the artifact build+upload, verbatim ri-4's AC1 and AC2; both inside
the signed act -- the COO half names the artifact as the one S3 write outside terraform), and its plan (AC6) is a
TARGETED plan over the six producer resources so the mount's not-yet-applied resources are not counted against it.**
EXECUTION ORDER: AC1, AC2, AC3, AC4, then AC11, AC12, then AC5, AC6, AC7, AC8, AC9, AC10. ri-4's whole-root plan runs
only after this order is terminal.

**DELIVER -- the consolidation Andrew ordered for this estate (`harvest/main.tf` header, verbatim: "ALL worker
terraform consolidates into this one harvester tf"), done as a NON-DESTRUCTIVE import:**
1. **THE s3.tf GUARD FIRST (AC1).** `infra/aws/terraform/harvest/s3.tf` at HEAD names `opal-data-research`, a bucket
   DELETED on 2026-09-11 (404 live); the harvest STATE tracks `aws_s3_bucket.harvest -> opal-data-harvest`, and
   `bucket` is ForceNew, so a plan against HEAD's file proposes DESTROYING the live harvest bucket (53 objects, this
   project's `derived/model_block/`). The two-line fix is the migration ledger's own uncommitted step 2 (row
   `AMGT_RESAPP-Z-S89`; ledger `org/critical_paths/change_management/20260911T1915Z_harvest-opal-data-harvest-migration_deploy_completion.md`).
   If your worktree's `s3.tf` reads `opal-data-research`, apply the saved patch
   `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/UNFINISHED_EDIT_harvest_s3_tf_20260914.patch` with
   `git apply` (it is in your grant) and carry those two lines in your commit citing the ledger and `Z-S89`.
   ⛔ **NO PLAN RUNS WHILE `s3.tf` NAMES `opal-data-research`, AND NO APPLY RUNS ON A PLAN THAT DESTROYS ANYTHING.**
2. `git mv infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf infra/aws/terraform/harvest/chatter-axis-schedule.tf`
   and `git mv infra/aws/terraform/amgt-resapp/lambda_src infra/aws/terraform/harvest/lambda_src`; `git rm`
   `infra/aws/terraform/amgt-resapp/main.tf` (precedent `dc868af89c`: a root whose state tracks a deleted resource
   would recreate it; the stale state objects stay in S3, inert, and are named in your ledger entry as the CRO's
   clean-up, not touched by you).
3. In the moved `chatter-axis-schedule.tf`: point `ReadArticlesTickerDateIndex` at
   `aws_dynamodb_table.harvest_articles.arn` and `"${aws_dynamodb_table.harvest_articles.arn}/index/ticker_date_index"`,
   and `WriteSecurityMetrics` at `aws_dynamodb_table.harvest_security_metrics.arn` -- RESOURCE REFERENCES, never a
   retyped ARN; delete the `data "aws_caller_identity"` only if nothing else in the file uses it (the log-group ARN
   does -- keep it, or use `local.account_id`). Update the file's header comments so no line still names an
   `opal-amgt-*` table or `security-metrics-table.tf` as if they existed. Fix `build_zip.py`'s and
   `lambda_function.py`'s docstring paths to the new home; their LOGIC is unchanged (`_REPO_ROOT = parents[4]` still
   resolves from `harvest/lambda_src/`).
4. Build the zip from HEAD's sources (`python infra/aws/terraform/harvest/lambda_src/build_zip.py` writes
   `infra/aws/terraform/harvest/.build/chatter-axis-producer.zip`, gitignored) -- BEFORE `terraform init`, because
   `filebase64sha256()` reads the file during evaluation.
5. `terraform init` in the harvest root (its lock file pins aws 5.100.0; the provider download is the standard
   toolchain act, not a vendor call), then `terraform import` the SIX live resources into `harvest/tfstate`:
   `aws_iam_role.chatter_axis_lambda` <- `amgt-resapp-chatter-axis-lambda-role`;
   `aws_iam_role_policy.chatter_axis_lambda` <- `amgt-resapp-chatter-axis-lambda-role:amgt-resapp-chatter-axis-lambda-policy`;
   `aws_iam_role.chatter_axis_scheduler` <- `amgt-resapp-chatter-axis-scheduler-role`;
   `aws_iam_role_policy.chatter_axis_scheduler` <- `amgt-resapp-chatter-axis-scheduler-role:amgt-resapp-chatter-axis-scheduler-invoke`;
   `aws_lambda_function.chatter_axis_producer` <- `amgt-resapp-chatter-axis`;
   `aws_scheduler_schedule.chatter_axis_daily` <- `default/amgt-resapp-chatter-axis-daily`.
6. `terraform validate`, then a TARGETED `terraform plan -out` over the six producer addresses (AC6): **`0 to add,
   N to change, 0 to destroy`**, every change in place (the policy's resources, the function's code hash and filename,
   default-tag adds); terraform prints that resource targeting is in effect, and that line is recorded. The mount's
   resources are deliberately outside this plan (they are ri-4's, in the same root, after this order). A `-/+` or a
   destroy anywhere means STOP and a row.
7. Open the deploy-completion entry (`python .tools/deploy_ledger.py open --slug
   amgt-chatter-axis-consolidation-and-repoint --author 0.9.0_WK_AMGT_RESAPP~17 ...` with legs: L1 git, L2
   activation = the apply, L3 verify = the live function/policy read, L4 verify = the QA invoke and today's rows),
   COMMIT the entry and its sentinel `org/critical_paths/.open_deploys/amgt-chatter-axis-consolidation-and-repoint.json`,
   then `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply ../../../../.scratch/ri2.tfplan`
   (AC7). Close each leg with its proof, `close` the entry (the tool unlinks the sentinel), commit the close.
8. QA-INVOKE ONCE (AC9) -- ad-hoc runs are permitted for QA; the 10:00Z scheduled fire stays the acceptance and is
   read from its own log by the CTO at L10. You do not wait for it.

**BOUND: a SCHEDULED PRODUCER is required and a MONITOR is forbidden** (standing moratorium; `comp-schedule` C3
= 12 NEVER clauses). You add no alarm, SNS topic, SES send, freshness checker or log subscription. You rename no
function (`function_name` is ForceNew and a rename is a destroy). You touch no table. You do not `state rm` from
any state.

## 2. WHERE THIS CAME FROM

**ROUND 10**, cut by `2.0.0_SA_COO~W` from `1.0.0_SA_CTO~Z`'s L10 round-9 analysis @`e9d1c6e6a5`, decomposition
s.18 (v1.1). The analysis named the page's "claimed daily-job cause" as UNMEASURED; `1.0.0_SA_CTO~W` measured it
(`Z-S88`) and REC'd this recut (hand-over s.3); the round-10 issuer re-measured the cause on the live plane and
found the three states above. `C-S49` (the CRO's harvest-migration consolidation row) is CITED here and stays
at `4.0.0_SA_CRO~Z`; the CVO adjudicates it against your outcome.

## 3. SURFACES -- what you may read and write

<paths>
infra/aws/terraform/amgt-resapp/
infra/aws/terraform/harvest/
lib/research/metrics/chatter_axis.py
lib/research/metrics/chatter_gate.py
lib/research/metrics/movement_gate.py
infra/aws/lambda/research/scoped_amgt_api/
lib/research/
lib/__init__.py
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_COO_HALF.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_CTO_HALF.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json
org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/UNFINISHED_EDIT_harvest_s3_tf_20260914.patch
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/mcp/sessions/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-2.the-producer-consolidated-and-repointed.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/research/` (the whole tree, for AC12's import closure),
  `lib/research/metrics/*.py` and `universe.json` are READ-ONLY inputs to the two zips; the patch file is READ-ONLY. Your `deliverables/0.9.0_WK_AMGT_RESAPP~17/` home needs
  no entry. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~17 <0.9.0_WK_AMGT_RESAPP~17@opal.agent>" -F <msgfile> -- <paths>`,
  the message file written with the Write tool, ASCII only. Several commits are expected (the move + edits; the
  ledger open with its sentinel; the close). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

No vendor call. No non-ASCII in any file you write or in anything that reaches AWS (tags, names, logs). No
monitor. No promote and nothing touching `portal/`. This cell makes FWD-15 REACHABLE and grades nothing
REALIZED. **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a
row; never repaired, widened or satisfied by a route this order did not name. **SURPRISE ROWS**, quoted from the
channel's own header: *"a seat's row is `AMGT_RESAPP-Z-S<k>`; a worker's row is `AMGT_RESAPP-Z-W<n>-S<k>` with
`<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every
new row."* Your coordinate is `W17`; your first row is `AMGT_RESAPP-Z-W17-S1`; append inside the one fenced JSON
array; never edit an existing row; keep working.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ri-2"><invocation>python -c "t=open('infra/aws/terraform/harvest/s3.tf',encoding='utf-8').read(); i=t.find('resource \"aws_s3_bucket\" \"harvest\"'); print(t[i:i+110].replace(chr(10),' | ')); print('harvest', t.count('bucket = \"opal-data-harvest\"'), 'research', t.count('bucket = \"opal-data-research\"'))"</invocation><expect>harvest 1 research 0, run BEFORE any terraform plan. STOP: if it prints research 1, do NOT plan -- git apply the saved patch named in your paths, re-run this criterion, and carry the two lines in your commit citing the 1915Z ledger and row AMGT_RESAPP-Z-S89. A plan taken while this reads research 1 proposes destroying the live harvest bucket</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ri-2"><invocation>git status --porcelain -- infra/aws/terraform/; python -c "t=open('infra/aws/terraform/harvest/chatter-axis-schedule.tf',encoding='utf-8').read(); print('old-names', t.count('opal-amgt-'), 'dangling', t.count('aws_dynamodb_table.security_metrics'), 'articles-ref', t.count('aws_dynamodb_table.harvest_articles'), 'metrics-ref', t.count('aws_dynamodb_table.harvest_security_metrics'), 'nonascii', sum(1 for b in open('infra/aws/terraform/harvest/chatter-axis-schedule.tf','rb').read() if b>127))"</invocation><expect>the status lines show the two renames INTO infra/aws/terraform/harvest/ (the schedule file and lambda_src/), the deletion of infra/aws/terraform/amgt-resapp/main.tf, and s3.tf modified only if AC1 required the patch; then old-names 0, dangling 0, articles-ref at least 2, metrics-ref at least 1, nonascii 0. A retyped literal ARN in a Resource list is NOT met; any surviving opal-amgt- token is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ri-2"><invocation>python infra/aws/terraform/harvest/lambda_src/build_zip.py && python -c "import zipfile,hashlib; z=zipfile.ZipFile('infra/aws/terraform/harvest/.build/chatter-axis-producer.zip'); a=hashlib.sha256(z.read('lib/research/metrics/chatter_axis.py')).hexdigest(); b=hashlib.sha256(open('lib/research/metrics/chatter_axis.py','rb').read()).hexdigest(); print('zip-member-equals-HEAD-source', a==b, a[:16]); print('entries', len(z.namelist())); print('defaults-in-member', z.read('lib/research/metrics/chatter_axis.py').decode('utf-8').count('opal-harvest-'))"</invocation><expect>two OK: lines from build_zip (built, and N producer imports verified), zip-member-equals-HEAD-source True, entries 6, defaults-in-member at least 2 -- the packaged producer is HEAD's, which already defaults to the harvest tables. A False, a missing universe_snapshot.json, or a FATAL from verify() is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ri-2"><invocation>cd infra/aws/terraform/harvest && timeout 115 terraform init -input=false -no-color > ../../../../.scratch/ri2.init.txt 2>&1; echo init-rc=$?; tail -4 ../../../../.scratch/ri2.init.txt; terraform version | head -1</invocation><expect>init-rc=0 and a line saying Terraform has been successfully initialized, provider hashicorp/aws v5.100.0 per the lock file, backend s3 key harvest/tfstate. A backend-init failure, a lock-file mismatch, or a timeout (rc 124, retried once) is NOT met and is a BLOCKING row</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-ri-2"><invocation>cd infra/aws/terraform/harvest && for pair in "aws_iam_role.chatter_axis_lambda amgt-resapp-chatter-axis-lambda-role" "aws_iam_role_policy.chatter_axis_lambda amgt-resapp-chatter-axis-lambda-role:amgt-resapp-chatter-axis-lambda-policy" "aws_iam_role.chatter_axis_scheduler amgt-resapp-chatter-axis-scheduler-role" "aws_iam_role_policy.chatter_axis_scheduler amgt-resapp-chatter-axis-scheduler-role:amgt-resapp-chatter-axis-scheduler-invoke" "aws_lambda_function.chatter_axis_producer amgt-resapp-chatter-axis" "aws_scheduler_schedule.chatter_axis_daily default/amgt-resapp-chatter-axis-daily"; do set -- $pair; printf "IMPORT %s <- %s: " "$1" "$2"; timeout 100 terraform import -input=false -no-color "$1" "$2" 2>&1 | tail -1; done; terraform state list | python -c "import sys; t=sys.stdin.read().split(); print('state-resources', len(t), 'chatter', sum(1 for x in t if 'chatter_axis' in x))"</invocation><expect>six lines each ending Import successful! (an already-managed resource on a re-run prints an error naming it as already managed -- record it and do not import twice), then state-resources 22 and chatter 6 (the 16 resources harvest/tfstate carried at this cut plus the six). Fewer than six imported, or a chatter count under 6, is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-ri-2"><invocation>cd infra/aws/terraform/harvest && timeout 60 terraform validate -no-color && timeout 115 terraform plan -input=false -no-color -detailed-exitcode -target=aws_iam_role.chatter_axis_lambda -target=aws_iam_role_policy.chatter_axis_lambda -target=aws_iam_role.chatter_axis_scheduler -target=aws_iam_role_policy.chatter_axis_scheduler -target=aws_lambda_function.chatter_axis_producer -target=aws_scheduler_schedule.chatter_axis_daily -out=../../../../.scratch/ri2.tfplan > ../../../../.scratch/ri2.plan.txt 2>&1; echo plan-rc=$?; python -c "import re; t=open('../../../../.scratch/ri2.plan.txt',encoding='utf-8',errors='replace').read(); m=re.search(r'Plan: (\d+) to add, (\d+) to change, (\d+) to destroy',t); print('PLAN', m.group(0) if m else 'NO-PLAN-LINE'); print('replace-marks', t.count('must be replaced'), 'destroy-marks', t.count('will be destroyed'), 'create-marks', t.count('will be created'), 'targeting-note', t.count('targeting is in effect')); [print(' ', l.strip()[:110]) for l in t.splitlines() if l.strip().startswith('#') and ('will be' in l or 'must be' in l)]"</invocation><expect>Success! The configuration is valid, then PLAN Plan: 0 to add, N to change, 0 to destroy with N between 2 and 6, replace-marks 0, destroy-marks 0, create-marks 0, targeting-note at least 1 (the plan is TARGETED to the six producer addresses; terraform says so and the line is recorded), plan-rc=2, and every listed address a chatter_axis resource being updated in-place (the policy's resources, the function's filename/source_code_hash, default-tag adds). STOP: aws_s3_bucket.harvest appearing at all is AC1 unmet; any add, replace or destroy is NOT met and no apply runs. AMENDED on row W17-S2: the committed version was a whole-root plan, which counts the mount's unapplied resources as adds in this same root</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-ri-2"><invocation>printf '%s' 0.9.0_WK_AMGT_RESAPP~17 > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"; test -f org/critical_paths/.open_deploys/amgt-chatter-axis-consolidation-and-repoint.json && git log -1 --format=%h -- org/critical_paths/.open_deploys/amgt-chatter-axis-consolidation-and-repoint.json; HALT_ACK=1 timeout 115 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -no-color ../../../../.scratch/ri2.tfplan > .scratch/ri2.apply.txt 2>&1; echo apply-rc=$?; tail -6 .scratch/ri2.apply.txt</invocation><expect>a commit hash printed for the COMMITTED sentinel (a staged-only sentinel is destroyed by a forced teardown -- commit it BEFORE this criterion), then apply-rc=0 and the line Apply complete! Resources: 0 added, N changed, 0 destroyed. with N equal to AC6's change count. A halt-gate BLOCK is recorded verbatim and is NOT met until its named cause is read; a non-zero destroyed count is a hard stop and a BLOCKING row</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-ri-2"><invocation>.tools/aws lambda get-function-configuration --function-name amgt-resapp-chatter-axis --query "[CodeSha256,LastModified,CodeSize]" --output text; python -c "import hashlib,base64; print('LOCAL-ZIP-SHA256-B64', base64.b64encode(hashlib.sha256(open('infra/aws/terraform/harvest/.build/chatter-axis-producer.zip','rb').read()).digest()).decode())"; .tools/aws iam get-role-policy --role-name amgt-resapp-chatter-axis-lambda-role --policy-name amgt-resapp-chatter-axis-lambda-policy --query "PolicyDocument.Statement[].Resource" --output text | python -c "import sys; t=sys.stdin.read(); print('harvest-articles', t.count('table/opal-harvest-articles'), 'harvest-metrics', t.count('table/opal-harvest-security-metrics'), 'old-amgt', t.count('opal-amgt-'))"</invocation><expect>the live CodeSha256 EQUAL to LOCAL-ZIP-SHA256-B64 and NOT TtTSpotkwWuVuMFbPv0RWTv2zqqifa/xfHQtBtuo924=, LastModified dated today, then harvest-articles 2, harvest-metrics 1, old-amgt 0 -- read from the LIVE role policy, never from the .tf. An unchanged CodeSha256 means the apply did not move the function and is NOT met</expect></criterion>
  <criterion id="AC9" cell_refs="AMGT-ri-2"><invocation>.tools/aws lambda invoke --function-name amgt-resapp-chatter-axis --cli-binary-format raw-in-base64-out --payload "{}" .scratch/ri2.invoke.json --query "[StatusCode,FunctionError]" --output text; cat .scratch/ri2.invoke.json; echo; TODAY=$(date -u +%F); for d in "$TODAY" 2026-09-13; do printf "COUNT TRENDING_CHATTER#%s: " "$d"; .tools/aws dynamodb query --table-name opal-harvest-security-metrics --key-condition-expression "axis_date = :ad" --expression-attribute-values "{\":ad\":{\"S\":\"TRENDING_CHATTER#$d\"}}" --select COUNT --query Count --output text; done</invocation><expect>200 None, a JSON payload with rows_written strictly greater than 0 and tickers_considered greater than 0, COUNT for today at least 1 and at most 10, and COUNT for 2026-09-13 exactly 0 (the day the deployed producer failed -- the control that shows the query discriminates). A FunctionError, a rows_written of 0, or a today count of 0 is NOT met. Copy .scratch/ri2.invoke.json into your deliverables folder as chatter-axis.qa-invoke.json</expect></criterion>
  <criterion id="AC10" cell_refs="AMGT-ri-2"><invocation>python -c "import glob,os; fs=glob.glob('org/critical_paths/change_management/*amgt-chatter-axis-consolidation-and-repoint*.md'); print('entries', len(fs)); [print(f, 'CLOSED-in-head', 'CLOSED' in open(f,encoding='utf-8').read()[:800]) for f in fs]; print('sentinel-present', os.path.exists('org/critical_paths/.open_deploys/amgt-chatter-axis-consolidation-and-repoint.json'))"; git log -1 --format="%h %s" -- org/critical_paths/change_management/</invocation><expect>entries 1, CLOSED-in-head True, sentinel-present False (the tool unlinks the sentinel on close, so ABSENT is the closed state and PRESENT means a leg is unproven), and the close COMMITTED (a hash whose subject names the close). Run this LAST, after the close commit</expect></criterion>
  <criterion id="AC11" cell_refs="AMGT-ri-2"><invocation>MAIN="$(dirname "$(git rev-parse --git-common-dir)")"; for h in COO CTO; do f="$MAIN/org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_${h}_HALF.md"; printf "%s_HALF %s\n" "$h" "$(test -f "$f" && echo PRESENT || echo ABSENT)"; test -f "$f" && sed -n '1,5p' "$f"; done; printf "NEG %s\n" "$(test -f "$MAIN/org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_ZZZ_NOPE.md" && echo PRESENT || echo ABSENT)"</invocation><expect>COO_HALF PRESENT and CTO_HALF PRESENT, each with its first lines printed and the CTO half carrying a Verdict line that reads SIGNED, and NEG ABSENT -- the never-widen co-sign that covers the artifact upload AC12 makes (the COO half names it as the one S3 write outside terraform). Read from the MAIN tree because both halves landed after this worktree was cut. STOP: either half ABSENT means AC12 does not run and this order stops on a BLOCKING row</expect></criterion>
  <criterion id="AC12" cell_refs="AMGT-ri-2"><invocation>timeout 115 bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh > .scratch/ri2.artifact.txt 2>&1; echo build-rc=$?; tail -12 .scratch/ri2.artifact.txt</invocation><expect>build-rc=0; a zipped: line with a non-zero byte count and an entry count above 20; a VERIFY line reporting every lib.research import it found is packaged with a missing list of []; a head-object JSON for research/opal-amgt-scoped-api.zip whose Meta.content-sha256 EQUALS the printed local sha256 (b64) line and whose Size is non-zero; and OK: uploaded s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip. THE SCRIPT IS YOURS TO WRITE under infra/aws/terraform/harvest/ (in your grant), exactly as ri-4 specifies it: zip lambda_function.py from infra/aws/lambda/research/scoped_amgt_api/ at the root plus the TRANSITIVE IMPORT CLOSURE of lib.research modules reachable from it -- start from lambda_function.py and the five packages lib/research/api/, lib/research/metrics/, lib/research/checkface/, lib/research/rules/, lib/research/watchlist/, walk every packaged .py by AST (module-scope AND function-scope imports), add every lib.research module it names from lib/research/ (the whole tree is in your grant, read-only), and repeat to a fixed point; the __init__.py of lib/ and lib/research/ and of every packaged package; preserving the lib/ prefix, EXCLUDING tests/ and __pycache__; deterministic entries (fixed date_time); the AST verify printing the closure it computed and its missing list; upload with --metadata content-sha256 (base64 sha256) mirroring build-and-upload.sh; head-object the key back. AMENDED on row W17-S3: the committed version enumerated five directories and the adapter's own closure reaches lib.research.price.axis, lib.research.print.render_pack and lib.research.provenance.render_print from function scope -- an enumeration lapses silently; a closure cannot. This deploys NOTHING (the Lambda does not exist yet); it makes the root's data source resolve. A missing-module list that is not empty, or a head-object without content-sha256, is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** There is no judgment criterion
on this order; every bar is an instrument's.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~17/AMGT_RESAPP.TO-AMGT-ri-2.the-producer-consolidated-and-repointed.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8,AC9,AC10,AC11,AC12` (rc 0 is the verdict);
save the plan text, the apply text and the QA payload beside it; flip `<status>` to `complete`; commit with
`--only -- <paths>`. Report once in your final message. **If a criterion cannot be met, leave the order OPEN and
file a row** -- and if that criterion is AC6 or AC7, say so as BLOCKING, because the world may be half-moved.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>10</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-9 analysis @`e9d1c6e6a5` (NO PRD ADDENDUM; round 10 on the COO's recut, one issuance), the slug REMEDIATION_v9 @`1ae76e9c83` (the empty page's "claimed daily-job cause was not measured"), row `AMGT_RESAPP-Z-S88` @`a325badef6` (`1.0.0_SA_CTO~W`: the cause measured; disarm_owner `2.0.0_SA_COO~W`; REC: an existing-cell recut of AMGT-rd-5 with C-S49 cited), hand-over s.3 @`c595aaec87`, and the round-10 issuer's re-measurement of the three terraform states and the live policy (decomposition s.18a/s.18d). The s3.tf guard: rows `Z-S12`, `C-S49`, `Z-S89`; the 1915Z migration ledger; CTO walk-back 22942 and CRO confirmation 22945 (2026-09-15 00:2xZ). Andrew-direct 2026-09-11 ~17:3xZ (harvest consolidation, record @`bb1800ec4d`). Cell set: s.18a; fan-out: s.18e.</authority>

<preflight>
ALL RUN 2026-09-15 00:3x-00:4xZ at this cut (decomposition s.18g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (15.2 s of 90); REACHED-DENOMINATORS C1=23, C2=9, C3=12, C4=21, C5=334; C2 = 9 OPEN deploy-ledger entries (9 ARMED gates, none this project's; this cell opens one and closes it inside the round); C3 = 12 standing NEVER clauses, the source of the producer-not-monitor bound; BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s); 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED; 15 missing, 291 deny-present across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The chatter-axis role is NOT in this lens's denominator (its package is not in the source map), so the repoint is verified on the LIVE policy (AC8), not by the lens.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 32 commit pins, 9 repo paths, 6 file:line cites; 15 hex runs not parsed (named); T11 NOT RESOLVED (236 uncited siblings, CAP 25 declared); stage 4 disabled by the caller.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE with the reason: six resources move state ownership and update in place; no shared served artifact moves; the plan's 0-destroy line is the blast control and it is a criterion.
</preflight>
