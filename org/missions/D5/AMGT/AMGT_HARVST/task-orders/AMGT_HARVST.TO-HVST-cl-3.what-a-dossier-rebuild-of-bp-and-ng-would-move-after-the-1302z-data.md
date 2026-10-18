# AMGT_HARVST task order -- `HVST-cl-3` -- ROUND 97, workstream DOSSIER-CENSUS-BP: A NO-WRITE CENSUS OF EVERY SERVED FIELD THAT A DOSSIER REBUILD OF `BP/_LN_Equity` AND `NG/_LN_Equity` WOULD MOVE AFTER THE 13:02Z DATA, WITH EACH CAUSE AND THE MODEL-BLOCK GUARD (CTO round-96 analysis item 2: "cut only if a census shows a served field would move")

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cl-3.what-a-dossier-rebuild-of-bp-and-ng-would-move-after-the-1302z-data</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cl-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~175</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` ONLY: list and get under `amgt/harvest/gold/research_dossier/`, `amgt/harvest/gold/research-continuation/`, `amgt/harvest/gold/research-fund-form/`, `derived/model_block/` and the silver and bronze objects a dossier build reads, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 6000 requests and 700 MiB in all, counted in the census's last line (the round-94 census of 95 names read about 1,700 requests and 280 MiB per 10 names after memoising). NO gold or silver writer is RUN: `dossier.write_one`, `continuation.write_one`, `gold_put` and every `--write` are NEVER run; only `dossier.build` (in memory). NO Bloomberg, NO model call, NO network beyond the S3 client: if `dossier.build` tries one, STOP, file a row and report. NO deploy, NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a comparator that cannot see a changed field (it has a negative control), a comparator that reports a move where only key order or whitespace differs (compare parsed values, not bytes), a census that compares the build with an object that is NOT the one the gateway serves (use the gateway's `_pick_dossier` rule), a `write_one` that slips in beside `build`, a cause assigned from the field's name instead of from the inputs that differ, a guard read from the stored dossier instead of from the build, a slash key looked up under its raw spelling (the stored partition is `security_key=BP-SLASH-_LN_Equity/`: use `crosswalk.security_key_partition`, never type the encoding), and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

At 13:02Z on 2026-10-18 a harvest cycle wrote a new Bloomberg pull, a new model block (`derived/model_block/BP-SLASH-_LN_Equity/20261018T130249Z/model_block.json`, written 13:02:51Z) and a new input ledger for `BP/_LN_Equity`. The BP dossier the gateway serves (`as_of=2026-10-18.2d0238f7570cff0e.json`) was written at 11:30Z, BEFORE that data; the NG dossier (`as_of=2026-10-18.1af6506669c49a8a.json`, written 11:34Z) may or may not predate NG's own new data. **The CTO wants the facts before deciding a rebuild (the cj-5 shape): for `BP/_LN_Equity` and `NG/_LN_Equity`, build the dossier IN MEMORY and list every served field that would move against the stored dossier the gateway serves, with the cause, and evaluate the model-block guard.** This cell writes nothing and changes no source file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `lib/research/corpus/dossier.py` (`current_inputs`, `build`, what `inputs` of a stored dossier list), `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~170/ci3_census.py` and its `ci3_census.out` (a read-only census of 95 names that builds each dossier in memory and compares it with the served one; START FROM IT; copy its `_pick_dossier` use, its comparator, its cause rule and its memo of immutable reads), `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/cj5_issuer_verify.py` (how a stored dossier's `inputs_sha16` and the model-block record are read) and `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CJ5_DOSSIERS_SLASH_CTO_HALF.md` (the CTO's MODEL-BLOCK GUARD, verbatim: per name that moves `model_rows`: the build's model-block record status is `SERVED`, its stamp is later than the stored dossier's, and the count of valued rows is not lower, else STOP).
b. Write `cl3_census.py` in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `cl3_census.out` (open it with `newline="\n"`). Names: `BP/_LN_Equity`, `NG/_LN_Equity` and the control `UNH_US_Equity`. If it would not finish inside the tool's ten-minute limit, slice it by name into a parts file and merge with `--final`, as `ci3_census.py` does.
c. Per name: the SERVED dossier = the object of `research_dossier/security_key=<partition>/` chosen by the gateway's `_pick_dossier` rule (`infra/aws/ec2/opal-gateway/app/harvest_research.py` lines 239-255; read them; do not call the gateway); the BUILT dossier = `dossier.build(security_key)` in memory (NEVER `write_one`). Compare the two `fields` objects FIELD BY FIELD over the union of the two key sets as parsed values with `==`, and `as_of` and the `inputs` lists. Print `NAME <security_key> served=<the full object name>/<method_version integer> as_of_served=<date> as_of_built=<date> fields_moved=<n> list=<comma-separated field names or none> input_kinds_differ=<comma-separated kinds or none>` and, per moved field, `DIFF <security_key> <field> cause=<cause> served=<first 70 characters or absent> built=<first 70 characters or absent>`. **The cause** is decided from the INPUTS that differ, never from the field's name: `inputs_continuation`, `inputs_fund_form`, `model_block` (the dossier's own name for the model-block input; the round-94 census assigned `other:model_block` and this cell names it as `model_block`), `as_of` when only the stamp differs, a comma-joined set when several kinds differ, and `other` when a field moves and no input kind differs (every `other` is a surprise row).
d. **The guard (print one line per name that moves `model_rows`, and one for every name):** `GUARD <security_key> model_block_status=<the build's model-block record status> built_stamp=<stamp> stored_stamp=<stamp of the model block the STORED dossier cites> valued_rows_built=<n> valued_rows_stored=<n> verdict=<PASS|STOP>` where PASS needs status `SERVED`, a later built stamp and a built count not lower than the stored count (read how `cj5_issuer_verify.py` counts valued rows; if the build exposes no such record, print `model_block_status=NOT_EXPOSED` and `verdict=STOP`). Do not change the guard to make it pass.
e. **The controls (rule 22):** POSITIVE: `CONTROL-POSITIVE UNH_US_Equity stored_vs_stored fields_moved=0` after comparing UNH's served dossier with a deep copy of itself by the SAME comparator. NEGATIVE: copy it, change ONE field's value, compare by the same comparator and print `CONTROL-NEGATIVE UNH_US_Equity planted fields_moved=1`.
f. The LAST line, exactly: `CENSUS-DOSSIER-MOVE-97 names=2 no_stored_dossier=<n> unchanged=<names with fields_moved=0> moved=<names with fields_moved>0> fields_moved=<total> cause_other=<count of DIFF lines with cause=other> guard_pass=<n> guard_stop=<n> gets=<requests> bytes=<bytes>` (UNH is a control and is not counted in `names`). **The issuer expects `names=2`.** The counts are the FINDING: do NOT change anything to make them read 0; print every moved name and field plainly. If the total would exceed the budget, STOP at the budget, print `BUDGET-EXCEEDED gets=<n>` and file a row.
g. Rows: ONE surprise row summarising the result (per name: moved fields, causes, the guard line); ONE row per `cause=other`. Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~175/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cl-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~175/cl3_census.out</invocation><expect>(?m)^CENSUS-DOSSIER-MOVE-97 names=2 no_stored_dossier=\d+ unchanged=\d+ moved=\d+ fields_moved=\d+ cause_other=\d+ guard_pass=\d+ guard_stop=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cl-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~175/cl3_census.out</invocation><expect>(?m)^CONTROL-POSITIVE UNH_US_Equity stored_vs_stored fields_moved=0$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cl-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~175/cl3_census.out</invocation><expect>(?m)^CONTROL-NEGATIVE UNH_US_Equity planted fields_moved=1$</expect></criterion>
</proof_of_spec>

- AC1 is the shape (and the `names=2` the issuer expects); its counts are the finding. AC2 and AC3 are the controls. **If a control prints another number, DO NOT edit the expectation or the comparator to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~14:5xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W175-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body, AND run the gate against your row WITHOUT the override first (the override must cover the Z-S106 pair only).
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~175/AMGT_HARVST.TO-HVST-cl-3.what-a-dossier-rebuild-of-bp-and-ng-would-move-after-the-1302z-data.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cl-3.what-a-dossier-rebuild-of-bp-and-ng-would-move-after-the-1302z-data` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cl-3.what-a-dossier-rebuild-of-bp-and-ng-would-move-after-the-1302z-data.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line (a commentary on the matched line breaks the `$` anchor).
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-96 analysis (msg 8092) item 2 ("rebuild under the cj-5 shape: the model-block guard, and moved fields within `{fund_form_ref, model_rows}` or a STOP; it is cut only if a census shows a served field would move").
- Chain B of round 97 (its own worker `~175`: no dependency on chain A; disjoint write set). Slot ~175, worktree `C:/dev/wk-harvst-175`, branch `wk-AMGT_HARVST-175`. **Sparse set at provision (checked against `<paths>` and the files the face names):** `.claude/agents`, `lib/research`, `integrations/bloomberg/research` (the `team_sheet` field map the round-94 worker lacked), `infra/aws/ec2/opal-gateway/app`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, and the deliverables folders `0.9.0_WK_AMGT_HARVST~170`, `0.9.0_WK_AMGT_HARVST~168`, `0.9.0_WK_AMGT_HARVST~165` and `2.0.0_SA_COO_W1/round95` plus `ledger/` for the CTO half.
- The rebuild itself is `HVST-cl-4` (seat `0.7.0_AE_CloudOps~SC1`, under a never-widen pair, add-only, the cj-5 shape): DEFINED and held; it is cut only if this census shows a served field would move and the guard passes.
- **SENT:** with the round-97 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>97</round>
<workstream>DOSSIER-CENSUS-BP</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
