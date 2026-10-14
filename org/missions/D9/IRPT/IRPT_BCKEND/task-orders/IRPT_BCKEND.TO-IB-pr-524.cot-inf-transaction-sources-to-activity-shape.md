# TO IRPT_BCKEND.TO-IB-pr-524 -- READ the landed transaction sources of Cottonwood and Inflection and map them to the `account_activity_daily` shape, READ ONLY (CTO round-187 analysis @718356ee39, ruling 2 and item 3: "FWD-21's own clause: the same layout for every firm, whatever vendor fed the data")

<to_id>IRPT_BCKEND.TO-IB-pr-524</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~371</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>187</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-187 analysis (item 3: "One read cell: the landed transaction sources for Cottonwood and Inflection and their mapping to `account_activity_daily`, read only") | **Decomp cell:** `IB-pr-524` (decomposition section 179) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-371` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~371 <0.9.0_WK_IRPT_BCKEND~371@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read; print what a search covered before you read a zero as an absence). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-524` (inlined).** The default Investor Reporting report shows contributions, withdrawals and income per window from the gold table `account_activity_daily`. Only 49 Financial has a producer for it (the Lambda `irpt-49f-reporting-gold-lambda` reads ONE declared custody source, the 49 Financial master: its `dim_balance` and `fact_trn` tables; `handler.py` refuses a second source). The CTO ruled (FWD-21; Andrew's "Opal Shape" word: one simple mechanism regardless of data vendor, a Gold layer that serves one shape) that Cottonwood (Black Diamond) and Inflection (Orion) activity must be produced into the SAME table shape **from their own already-landed transactions, with no new vendor pull**. **This order only READS: which landed transaction source each firm has, and, column by column, how it maps to the shape.** It writes and invokes nothing.

**Client data rule:** counts, dates, column NAMES and sha256 only in any tracked file; no account id, client id, transaction value or bucket key value; scratch stays OUTSIDE the worktree (`C:/dev/_scratch371/`), deleted at the end with a short bounded script.

**Read first:** `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py` (the activity table's schema, its columns and what `compute_local` / `emit_day` read: the 49F source's tables and which of their columns feed each shape column), `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` lines 20-70 and 210-240 (the declared source and the one-source refusal), the producer's source declaration (`ard.load_declaration`: find the `sources.json` it names and read the 49F custody entry), `lib/opal_naming.py` and `infra/logic/registry/` (the tier homes: each firm's bronze/silver/gold bucket and prefix shapes come from `address()` output, rule 30; never type a bucket), and the repository's data scripts for the two vendors (Black Diamond under `data/black_diamond/`, Orion under `data/` wherever the Inflection pipeline lives: find it by the registry, not by guessing).

**Do, in this order (every number is a MEASUREMENT with its source named in `notes`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it).
2. **The shape.** Read the activity table's schema from the producer's own code (`account_activity_lots.py`): record `shape_columns` (the column NAMES, in order, distinct) and `shape_source` (the file and the symbol the columns were read from). Also note in `notes` each column's meaning in one phrase (for example a contribution, a withdrawal, an income amount) as the producer's own comments state it.
3. **The 49F reference.** For each shape column, which 49F source table and column (or rule) feeds it, from `compute_local` (names only). This is the mapping the two firms must meet; keep it in `notes` or `reference_mapping`.
4. **The landed transaction source, per firm** (`cottonwood`, `inflection`): find, from the registry and the data scripts, the firm's LANDED transaction table(s) (the analogue of the 49F `fact_trn`: transactions or activity with dates, accounts, amounts and a type), and its balance or account dimension (the analogue of `dim_balance`) if one exists. List the table prefixes with the READ-ONLY S3 calls `s3api list-objects-v2` (partition counts and `date=` earliest and latest only; **no object body**) using your own identity. Record `firms.<firm>.transaction_source` as `{"vendor": "...", "tables": ["<table names>"], "partitions": n, "earliest": "YYYY-MM-DD", "latest": "YYYY-MM-DD"}` (omit earliest and latest only when `partitions` is 0; if the table exists and your identity cannot list it, say so in `notes`, record `partitions` 0 and stop short of guessing). If NO landed transaction source exists for a firm, record `tables` as `["<none found>"]`, `partitions` 0, and say what you searched in `notes`.
5. **The column schemas, from repository code, never from bodies.** For each landed table of step 4, the column names its writer produces (the vendor's silver schema in the repository's pipeline scripts, a schema JSON or a dataclass): names only. If you cannot find a table's schema in code, say so; do not open data objects to learn it.
6. **The mapping, per firm.** For EVERY shape column of step 2, one row `{"shape_column": "<name>", "status": "MAPPED|DERIVED|ABSENT", "source": "<the firm's table.column, or the derivation rule in one line>" (for MAPPED and DERIVED), "reason": "<why it cannot be produced>" (for ABSENT)}`; `firms.<firm>.mapping` must account for every shape column once, and `firms.<firm>.unmapped_columns` lists the ABSENT ones. MAPPED means a source column carries it directly; DERIVED means it follows from source columns by a rule you state (for example a sign convention or a type filter); ABSENT means the landed source cannot give it, with the reason.
7. **The reading, per firm.** `can_produce_shape`: `YES` only if no shape column is ABSENT; `PARTIAL` if some are; `NO` if the source or its schema was not found. `note`: one or two sentences stating what the reading rests on and what was NOT measured (for example that value semantics and signs were not compared against real rows, that the earliest account record was not read, or that a column's schema was not found in code).
8. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~371/IB187-2_transaction_source_mapping.json`: `{"base_commit":"<40hex>","shape_source":"<file: symbol>","shape_columns":[...],"reference_mapping":[...],"firms":{"cottonwood":{"transaction_source":{...},"mapping":[...],"unmapped_columns":[...],"can_produce_shape":"YES|PARTIAL|NO","note":"..."},"inflection":{...}},"notes":["..."],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}` and a short readable summary `deliverables/0.9.0_WK_IRPT_BCKEND~371/TRANSACTION_SOURCE_MAPPING_SUMMARY.md` (what each firm has, the mapped and absent columns, and the first cell a producer build would need: no more than 60 lines).
9. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB187-2_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the deliverables FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB187-2-AC1" cell_refs="IB-pr-524"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py" . IB187-2-AC1</invocation><expect>IB187-2-AC1 PASS</expect></criterion>
<criterion id="IB187-2-AC2" cell_refs="IB-pr-524"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py" . IB187-2-AC2</invocation><expect>IB187-2-AC2 PASS</expect></criterion>
<criterion id="IB187-2-AC3" cell_refs="IB-pr-524"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py" . IB187-2-AC3</invocation><expect>IB187-2-AC3 PASS</expect></criterion>

<expected_criteria>IB187-2-AC1, IB187-2-AC2, IB187-2-AC3</expected_criteria>

What the checks grade: AC1 the shape columns (at least 3 distinct names with the file and symbol they were read from) and, for each of the two firms, the transaction source (a vendor, a non-empty tables list, an integer partition count, and earliest and latest dates when there are partitions); AC2 for each firm every shape column accounted for exactly once as MAPPED, DERIVED (each with its source) or ABSENT (each with its reason), and `unmapped_columns` equal to the ABSENT columns; AC3 per firm `can_produce_shape` YES, PARTIAL or NO consistent with the ABSENT list (YES if and only if none is ABSENT), a note, no long digit run, and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. READ ONLY. **Nothing is invoked, written, uploaded, applied or deployed:** no Lambda invoke, no S3 write or object-body read of client data, no terraform, no source-map write, no sign-in, no vendor call. Allowed AWS calls (READ): `s3api list-objects-v2` with a delimiter on the transaction and dimension table prefixes (partition names and counts only), `s3api head-object` of a `_SUCCESS` or manifest key if one exists (metadata only), `sts get-caller-identity`.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes or invokes; a read of an object BODY of client data; a column you cannot source (say so; do not estimate). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W371-S<k>` (start at 1); file a row for anything odd and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~371/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 179 (round 187, workstream ~P), cell `IB-pr-524`.
<owned_cells>IB-pr-524</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB187-2-AC1, IB187-2-AC2, IB187-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~371/IRPT_BCKEND.TO-IB-pr-524.cot-inf-transaction-sources-to-activity-shape.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the read lists table prefixes of two firms' landed transaction sources (partition names and counts only) and reads repository code; it writes nothing and invokes nothing; the producer build, its pair and its runs (which would write gold tables for two more firms) are later cells with their own blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the read uses the worker's own identity and records a denial as a statement, never widened.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p187_cells.py IB187-2 dry-run at base on dell2 2026-10-14 ~01:3xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (a synthetic record; removed): all three PASS; negatives, each failing its own arm: a source without tables, a shape column missing from a mapping, an ABSENT column without a reason, an unmapped list that disagrees with the statuses, YES with an absent column, a write counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~371` (worktree `C:/dev/wk-IRPT_BCKEND-371`). Class SERVED (reads listings and the repository; writes only the worker's records). The premises (one declared source for the 49F producer; the CTO's reading of FWD-21) are the census's and the CTO's.
</preflight>
