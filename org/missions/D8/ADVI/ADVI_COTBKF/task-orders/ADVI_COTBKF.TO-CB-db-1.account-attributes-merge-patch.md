# TO ADVI_COTBKF.TO-CB-db-1.account-attributes-merge-patch -- round 105 CB-db-1: write the one-line ssm.tf patch that makes Cottonwood's silver run merge account_attributes (not applied anywhere), prove its shape and its Terraform plan, and measure the drift and the readers it will release

<to_id>ADVI_COTBKF.TO-CB-db-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~195</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>105</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-db-1` (`decompositions/ADVI_COTBKF_DECOMP.round105.md`) |
**outcome_ref:** S59 (CTO msg 6923; FIRMBKTS row `ADVI_FIRMBKTS-D1-S59`) | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Cottonwood's daily silver run (SSM document `opal-cot-silver-run`) never merges the `account_attributes` table, although its bronze file lands every day. Silver holds one partition (2026-08-19), and the gold accounts dimension joins that stale snapshot. The fix is one non-gating step in the document. It moves served output once applied, so it is applied later by another seat under a sign-off pair. **You write the patch and the evidence for that sign-off. You apply nothing, edit no committed file, and write nothing to AWS.**

**Facts (read by the issuer; check, do not assume).**
- `infra/aws/terraform/cot-pipeline/ssm.tf`, resource `aws_ssm_document.cot_silver_run`, the `runCommand` list: `--table transactions`, `allocations`, `realized`, `unrealized`, then `holdings` as a NON-GATING brace group (`{ python3.11 /tmp/cot_silver_merge.py --table holdings $DATE_ARG || echo 'WARN: ...'; } &&`), then a comment block starting `# ADVI_COTETL.CHAIN-FIX: LAST step`, then `--finalize`.
- `data/cot/scripts/silver/cot_silver_merge.py` already has `TABLE_CONFIG['account_attributes']` (forwardfill prefix `forwardfill_v2/account_attributes`, silver prefix `silver/account_attributes`, bucket `opal-data-cot`). `_SILVER_STAGE_TABLES` (the four gated tables) must NOT gain `account_attributes`.
- Gold `data/cot/scripts/gold/A_00.accounts_dimension.py` `load_account_attributes()` reads the sorted-last `silver/account_attributes/*.parquet`.

**Your items.**
1. **The patch.** Write `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/SSM_ACCOUNT_ATTRIBUTES.patch`, a unified diff of `infra/aws/terraform/cot-pipeline/ssm.tf` with header paths `a/infra/aws/terraform/cot-pipeline/ssm.tf` and `b/infra/aws/terraform/cot-pipeline/ssm.tf`, containing exactly ONE added line and no removed line: a NON-GATING step for `account_attributes`, in the holdings step's own shape, placed immediately after the holdings step and before the `# ADVI_COTETL.CHAIN-FIX: LAST step` comment: `          "  { python3.11 /tmp/cot_silver_merge.py --table account_attributes $DATE_ARG || echo 'WARN: account_attributes refresh failed -- NON-GATING'; } &&",` (keep the file's own line ending). Do NOT edit `ssm.tf` in your worktree or anywhere in the repo: copy the file to your scratch folder `C:/Dev/ajb_workspace/.scratch/cotbkf_r105/`, add the line there, and produce the diff with Python `difflib.unified_diff(old_lines, new_lines, 'a/<path>', 'b/<path>', n=3)` over the lines read with `splitlines(keepends=True)`, written with `newline=''` so line endings survive.
2. **The shape and plan evidence.** Run the issuer's two checks (AC1 and AC2 below) and fix the patch until both pass. The checks apply the patch to a throwaway copy that they delete; they never touch the real file.
3. **The drift record.** Measure, with your own code written from the facts above (do NOT run or read `deliverables/2.0.0_SA_COO~C1/db1_attr_drift_recompute.py`; an independent measurement is the point), how far the stale silver partition has drifted from the newest bronze pull, reading these two objects read-only with the `.tools/aws.cmd` shim (never `.tools/aws` from Python): `s3://opal-data-cot/silver/account_attributes/2026-08-19.parquet` and `s3://opal-data-cot/forwardfill_v2/account_attributes/ACCOUNT_ATTRIBUTES_DAILY_2026-10-15.xlsx` (sheet `Sheet1`; columns `Portfolio Group, AccountID, Position Only, Account Supervised, Account Billable`; silver columns `portfolio_group, account_id, position_only, account_supervised, account_billable`). Compare by distinct `AccountID` with each value stripped and a blank as the empty string; for an account with two rows compare its set of values. Report: `old_rows, new_rows, old_accounts, new_accounts, added, removed, both, multibook_old, multibook_new, changed_supervised, changed_billable, changed_position_only, changed_portfolio_group, changed_any, multibook_flag_disagree_new` (the number of accounts with more than one row in the bronze whose `supervised`, `billable` or `position_only` values are not all equal).
4. **The readers and the rule.** Read, without editing: (a) `A_00.accounts_dimension.py` `load_account_attributes()` and `join_account_attributes()`, and say in the record in words what it does at a multi-book account (the flag-agreement assert and the portfolio_group it keeps); (b) which gold scripts under `data/cot/scripts/gold/` READ the dimension's four attribute columns (`account_supervised`, `account_billable`, `position_only`, `portfolio_group`) and which WRITE them, by file basename, using the `Grep` tool restricted to that folder with the four names (print the denominator: how many gold scripts exist and how many matched); (c) whether the choice of `portfolio_group` at a multi-book account depends on the row order of the silver partition, by reading how `cot_silver_merge.py` orders and writes the `account_attributes` partition, and say yes, no or cannot tell with the line you read; (d) how a silver partition for `account_attributes` is named and what one run reads (one bronze day, or all), by reading `cot_silver_merge.py`.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/ACCOUNT_ATTRIBUTES_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `silver_object`, `bronze_object` (the two object keys above), `drift` (the fifteen counts of item 3), `multibook_rule` (item 4a, words), `gold_readers` (`{"scripts_scanned","readers":[basenames],"writers":[basenames]}`), `partition_order_dependence` (`{"answer":"yes|no|cannot tell","evidence":"<file:line and a one-line paraphrase>"}`), `partition_naming` (item 4d), `what_this_shows` (two sentences in counts), `not_established`; and a short `.md` beside it. COUNTS, FILE NAMES AND ROLES ONLY: no account id, advisor, client or portfolio-group name, and no dollar value anywhere in the record, the `.md` or your report.

### ACCEPTANCE

<criterion id="CB105db1-AC1" cell_refs="CB-db-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/db1_patch_check.py shape org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/SSM_ACCOUNT_ATTRIBUTES.patch</invocation><expect>^PATCH-SHAPE files=1 removed=0 added=1 table_line=True nongating=True before_finalize=True applies=True$</expect></criterion>
`CB105db1-AC1` -- the patch is one added line in `ssm.tf`: the `account_attributes` step in the non-gating brace-group shape, before `--finalize`, and it applies to the tree at HEAD.

<criterion id="CB105db1-AC2" cell_refs="CB-db-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/db1_patch_check.py plan org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/SSM_ACCOUNT_ATTRIBUTES.patch</invocation><expect>^PATCH-PLAN add=0 change=1 destroy=0 address=aws_ssm_document\.cot_silver_run$</expect></criterion>
`CB105db1-AC2` -- a read-only `terraform plan` of the cot-pipeline root with the patch applied to a throwaway copy reads one in-place change, to `aws_ssm_document.cot_silver_run`, and nothing else.

<criterion id="CB105db1-AC3" cell_refs="CB-db-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/ACCOUNT_ATTRIBUTES_RECORD.json',encoding='utf-8'));m=d['measured'];r=d.get('drift') or {};print('DRIFT-RECORD measured=%s' % m + ((' bronze=%s added=%d removed=%d changed_billable=%d changed_portfolio_group=%d changed_any=%d multibook_new=%d flag_disagree=%d' % (d['bronze_object'].rsplit('_',1)[-1],r['added'],r['removed'],r['changed_billable'],r['changed_portfolio_group'],r['changed_any'],r['multibook_new'],r['multibook_flag_disagree_new'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^DRIFT-RECORD measured=True bronze=2026-10-15\.xlsx added=62 removed=0 changed_billable=45 changed_portfolio_group=130 changed_any=171 multibook_new=122 flag_disagree=0$</expect></criterion>
`CB105db1-AC3` -- your own measurement of the drift between the stale silver partition and the 2026-10-15 bronze pull states the same counts the issuer measured (62 accounts added, none removed, 45 billable changes, 130 portfolio-group changes, 171 accounts changed in any column, 122 multi-book accounts, none whose flags disagree). A different number is not a failure to hide: if your measurement differs, write what you measured and why in the record and the report, and file a surprise row; the criterion will then read as not met and the issuer will reconcile the two.

<expected_criteria>CB105db1-AC1,CB105db1-AC2,CB105db1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder, your own NEW channel row, and this order's own file (for the one `<status>` flip). You change no code, test, Terraform or other committed file. Scratch stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r105/` (gitignored); a small measuring script of yours may be committed in your deliverables folder as evidence provided it carries no account id or name. Your instance rows for artifacts that already exist in a commit are pinned to that commit's FULL hash.
- **AWS: READ-ONLY** (`s3 cp` / `get-object` / `ls` of the two named objects and the listing of `silver/account_attributes/` and `forwardfill_v2/account_attributes/` in `opal-data-cot`); no write, no `terraform apply`, no `terraform init`, no SSM call, no vendor call. You contact no one.
- **NEVER** apply the patch to the real `ssm.tf`, edit any module, serve, push, override a gate or `--force`; never write an account id, a name or a dollar value into a record, a row, a commit message or a message.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W195-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'ab')` writing LF bytes only (the file holds CRLF lines from earlier rows: never read and rewrite it); `git diff --numstat` must show added lines only; the row carries no id or name.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-db-1.account-attributes-merge-patch.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one write to this order is the `<status>` flip.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round105.md</decomp_doc> (round 105), cell `CB-db-1`.
<owned_cells>CB-db-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB105db1-AC1, CB105db1-AC2, CB105db1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/ADVI_COTBKF.TO-CB-db-1.account-attributes-merge-patch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB105db1-AC1,CB105db1-AC2,CB105db1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the order file is in your `<paths>` for this flip).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: the patch's one line as written (it carries no id); the drift counts; what `A_00` does at a multi-book account; the gold readers and writers (basenames and the denominator); the partition-order answer with its line; the partition naming and what one run reads; any step you could not run and why; commits; every gate refusal and hook denial, verbatim. No account id, name or dollar value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a patch file and a counts record; nothing is scheduled, served or deployed by this order.
comp-iam: DECLARED-NOT-APPLICABLE read-only reads of two objects and two listings in opal-data-cot under the existing role; no new permission; no vendor access.
comp-adversary: RUN -- the patch is checked by an issuer script on a good patch and three mutants (gating form, a removed line, the line after --finalize: each reads a different PATCH-SHAPE field), and a non-applying patch (applies=False; plan reads patch-did-not-apply); the plan mode on the good patch reads add=0 change=1 destroy=0 address=aws_ssm_document.cot_silver_run, and the root's own plan at HEAD reads "No changes" (baseline). BLIND: the plan cannot say whether the live SSM document equals the one Terraform holds (a drift in the live document would show as an in-place change on its own, which the baseline "No changes" excludes today); the shape check cannot judge that the step is the right one for the data (the worker's measurement and the sign-off pair do); the drift counts are the issuer's own recompute and the worker's own, from one bronze file named in the record, not a standing measure of later days.
lane: the <paths> block IS the grant (worker RULING 1) and names the order file for the status flip.
</preflight>

**ISSUER NOTES:** Source: CTO msg 6923 and 6946. Mechanical checks dry-run at the base (patch and record absent): AC1, AC2 and AC3 FAIL as expected. `db1_patch_check.py` ran on a good patch (AC1 line reads exactly the expected output; AC2 reads add=0 change=1 destroy=0 address=aws_ssm_document.cot_silver_run in 7 s), and on three mutants and a non-applying patch (each AC1 field reads False where it should). The issuer's drift recompute reads the 2026-10-15 bronze file; a later bronze file would move the numbers, which is why the criterion pins the bronze object name in the record. Round 106 (the never-widen pair, the CloudOps apply, and a read of the first partition newer than 2026-08-20) waits on this record: the pair's expected outcome is read from `A_00`'s own rule and from this measurement, never from the shape of the input.
