# TO IRPT_BCKEND.TO-IB-pr-571 -- READ the Cottonwood validator OFFLINE on the dropped account's source rows and name the failing condition in cot_screen_accounts; the fix options in the code; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-571</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~414</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PC</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8248 ("cut both READs now, 49 Financial's refusal FIRST") on the S158 READ (IB-pr-569, row D2-S192) | **Decomp cell:** `IB-pr-571` (decomposition section 206) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-414`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~414 <0.9.0_WK_IRPT_BCKEND~414@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (a local setting, never committed, nothing wider), so the publisher, its tests and the checks' file reads resolve under the worktree root.

**Client data rule:** counts, dates, hashes, commit ids, condition names, class names and file paths only in any tracked file; **no account id, household id, client id, name, quantity, value or holding name; accounts are described by class and count, never by id.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch414/`); delete any downloaded refusal record or source rows from scratch after you read them.

**Cell `IB-pr-571` (inlined) -- the Cottonwood validator, offline.** The S158 READ (`deliverables/0.9.0_WK_IRPT_BCKEND~412/IB209-1_s158_read.json`, rows `D2-W412-S1` to `S4`, `D2-S192`; READ THEM FIRST) found Cottonwood's one residual lost account (the latest refusals, `account_lost` count 1) is LISTED in the custodian `fact_holdings` source on every date read, has no directory entry, and is dropped by the COT account screen: `cot_screen_accounts` (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` lines 2266 to 2294), which refuses each source account that fails `validate_cot_actual_positions` (build_cot applies it when no account list is passed, near line 2328). **The failing validator condition is not measured.** The CTO (msg 8248) wants it named: run the validator OFFLINE on the dropped account's source rows and name the condition. **Offline means: the source rows are read (GET of the existing partition objects to scratch), the validator function is imported from the repository file and called on those rows in a scratch script outside the repository; nothing is published, no producer is run, no served prefix is written.** Ids private.

**Do, in this order:**
0. `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (local, never committed). **AMENDMENT 1 (issuer, on your row W414-S1): the validator's import chain sits outside that directory.** Read the validator's `import` lines and add, with the same local command, EXACTLY the directories they need and nothing else (the row names `infra/aws/lambda/investor-reporting`; add it, plus any other directory a import in the chain resolves to; read-only use, never committed, no wider than the chain). The offline run MUST be performed: a record that did not run the validator is not graded (`offline_run.performed` true; the check refuses a record without it). `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
1. **Find the dropped account without recording it.** From the S158 record and the refusal record's `listed` block (Cottonwood, the latest candidate, `account_lost` count 1), identify the one account that is in the served snapshot and absent from the latest candidate; keep its id in memory/scratch only. Read its rows from the `fact_holdings` source partition for the latest candidate date (count them: `source_rows` = `{"count":<n>,"distinct_dates":<n>}`; if the account has rows on more dates in the partitions you read, count them).
2. **Read the code.** `validator_site` = `{"file":"<repo path>","line":<n>,"identifier":"<text on that line, holding validate_cot_actual_positions>"}`; `screen_site` likewise for `cot_screen_accounts`. Read the validator in full: its conditions (each refusal reason the function can raise or return, with the name the code gives it).
3. **Run it offline.** In a scratch script OUTSIDE the repository, import the validator from the repository file (read-only), call it on the account's rows exactly as `cot_screen_accounts` calls it, and record `offline_run` = `{"performed":true,"read_only":true,"writes":0,"published":false,"invocation":"30+ characters: the command, WITHOUT any account id","outcome":"refused|accepted"}`. If the validator REFUSES, `failing_condition` = `{"name":"<the condition name the code gives>","claim":"measured","site":{"file":"..","line":<n>,"identifier":"<the line that raises it>"},"explanation":"60+ characters: what it checks, in words, no value"}`. If it ACCEPTS the rows (so the screen drops the account for another reason, such as a different input shape in `cot_screen_accounts`), say so: `failing_condition` = `{"name":"","claim":"inferred|absent","statement":"60+ characters","explanation":"60+ characters"}` and name in `statement` what you read instead (the screen's own code path).
4. **The fix options, read in the code.** `fix_options` = `[{"option":"20+ characters","site":{"file":"..","line":<n>,"identifier":".."},"effect":"30+ characters"},...]`, at least two (for example a correction in the screen or the validator at the line you named, and a custodian-confirmed TERMINATED mark through the directory exclusion at `closed_accounts` near line 3051); each `site` a line you read at HEAD. Do not propose a guard bypass. `ids_private` is true.
5. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~414/IB210-2_cot_validator_read.json` with exactly: `base_commit`, `read_date`, `validator_site`, `screen_site`, `source_rows`, `offline_run`, `failing_condition`, `fix_options`, `ids_private`, `notes` (at least three lines of 30+ characters), and the six counters at 0 (`functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`).

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB210-2_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`, as the proof instance of `IB-pr-567` does**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB210-2-AC1" cell_refs="IB-pr-571"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py" . IB210-2-AC1</invocation><expect>IB210-2-AC1 PASS</expect></criterion>
<criterion id="IB210-2-AC2" cell_refs="IB-pr-571"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py" . IB210-2-AC2</invocation><expect>IB210-2-AC2 PASS</expect></criterion>
<criterion id="IB210-2-AC3" cell_refs="IB-pr-571"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py" . IB210-2-AC3</invocation><expect>IB210-2-AC3 PASS</expect></criterion>

<expected_criteria>IB210-2-AC1, IB210-2-AC2, IB210-2-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects under the firms' IRPT prefixes (publication, refusal records, manifests, the custodian source partitions, the directory), `list`, `describe`. **Nothing is published, bypassed, re-run against a served prefix, invoked, written to AWS, signed or sent. The producer is NOT run against a served prefix; no bypass is widened (the guard stays).**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to run the producer against a served prefix; an account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W414-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~414/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 206 (round 2, workstream ~PC), cell `IB-pr-571`.
<owned_cells>IB-pr-571</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB210-2-AC1, IB210-2-AC2, IB210-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~414/IRPT_BCKEND.TO-IB-pr-571.run-the-cottonwood-validator-offline-on-the-dropped-accounts-rows-and-name-the-failing-condition.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing objects and the publisher's code with the worker's own identity and writes one record; nothing is published, bypassed or invoked against a served prefix, so no served byte moves; the fix (a screen correction or a custodian TERMINATED mark) is the CTO's ruling and a later act under its own signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p210_cells.py IB210-2 dry-run at base on dell2 2026-10-15 ~11:4xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub publisher file with the guard, screen and validator lines, synthetic records; removed): all three PASS; eleven negatives on this cell, each failing its own arm: a wrong validator line, a wrong screen identifier, no source rows, an offline run that wrote, an offline run that published, a refused run claimed inferred, a wrong condition line, one fix option, ids not private, short notes, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~414` (worktree `C:/dev/wk-IRPT_BCKEND-414`). Class SERVED (reads a served surface and writes only the worker's records).
</preflight>
