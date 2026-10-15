# TO IRPT_BCKEND.TO-IB-pr-570 -- READ 49 Financial's holdings refusal: which condition refused it, how many accounts, which class of account or field (ids private), how far behind it is served, and the acceptance path in the code; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-570</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~413</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PC</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8248 ("cut both READs now, 49 Financial's refusal FIRST") on the S158 READ (IB-pr-569, row D2-S192) | **Decomp cell:** `IB-pr-570` (decomposition section 206) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-413`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~413 <0.9.0_WK_IRPT_BCKEND~413@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (a local setting, never committed, nothing wider), so the publisher, its tests and the checks' file reads resolve under the worktree root.

**Client data rule:** counts, dates, hashes, commit ids, condition names, class names and file paths only in any tracked file; **no account id, household id, client id, name, quantity, value or holding name; accounts are described by class and count, never by id.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch413/`); delete any downloaded refusal record or source rows from scratch after you read them.

**Cell `IB-pr-570` (inlined) -- 49 Financial's refusal.** Rows `IRPT_BCKEND-D2-S158` and `D2-S192` (READ BOTH FIRST, in `INVESTIGATION_v1.md`) and the S158 READ record `deliverables/0.9.0_WK_IRPT_BCKEND~412/IB209-1_s158_read.json`: Cottonwood's holdings are refused on `account_lost`, and **49 Financial, the P1 firm, ALSO has a refusal record** and is served at 2026-10-12, two trading days behind T-1 (2026-10-14 at the read). The CTO (msg 8248) wants 49 Financial's refusal read FIRST: **which condition refused it, how many accounts, and which class of account or field (ids private).** The guard is `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the conditions are added near lines 2888 to 3060; read the condition names there and the tests `test_holdings_publish_gate.py`). This order READS; the guard stays and no bypass is widened.

**Do, in this order:**
0. `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (local, never committed). `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
1. **The refusals.** Find 49 Financial's holdings publication prefix and its refusal records with the canonical address (`lib/opal_naming.py` `address()`) and a read-only list (the served-graph route may be blocked; the address and list stand). Read EVERY refusal record version (counts). Record `served` = `{"firm":"49financial","business_date":"<its current manifest's date>","t_minus_1":"<lib/trading_calendar.py prev_trading_day of read_date>","trading_days_behind":<number of trading days from the served date to t_minus_1, counting t_minus_1 and not the served date>}` (the check recomputes both), and `refusals` = `{"refused_dates":[the candidate business dates refused, ISO, sorted, trading days after the served date],"refusal_records_read":<n>,"per_candidate":[{"candidate_date":"<ISO>","conditions":[{"condition":"<the condition name as the record states it>","count":<n>},...]},...]}` (one row per refused date, same order). `guard_site` = `{"file":"<repo path>","line":<n>,"identifier":"<text on that line, the line that adds the first condition named>"}`.
2. **The account or field.** `account_or_field` = `{"claim":"measured|inferred|absent","class":"10+ characters: the KIND of account or field behind the condition, never an id","statement":"60+ characters"}`. Read the refusal record's `listed` block and the code that fills it; count, never name.
3. **The cause and the path.** `cause` = `{"claim":"measured|inferred|absent","statement":"60+ characters","evidence":["30+ characters each, at least two"]}`; `acceptance_path` = `{"mechanisms":[{"name":"..","file":"..","line":<n>,"identifier":".."},...],"recommended_path":"40+ characters"}` (every mechanism a line you read at HEAD; the check reads the line; do not recommend a bypass of the guard). `other_firms` = `{"cottonwood":{"served_business_date":"<ISO>"},"inflection":{"served_business_date":"<ISO>"}}` from their manifests.
4. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~413/IB210-1_49f_refusal_read.json` with exactly: `base_commit`, `read_date`, `served`, `refusals`, `guard_site`, `account_or_field`, `cause`, `acceptance_path`, `other_firms`, `notes` (at least three lines of 30+ characters), and the counters `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`, all 0.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB210-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`, as the proof instance of `IB-pr-567` does**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB210-1-AC1" cell_refs="IB-pr-570"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py" . IB210-1-AC1</invocation><expect>IB210-1-AC1 PASS</expect></criterion>
<criterion id="IB210-1-AC2" cell_refs="IB-pr-570"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py" . IB210-1-AC2</invocation><expect>IB210-1-AC2 PASS</expect></criterion>
<criterion id="IB210-1-AC3" cell_refs="IB-pr-570"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py" . IB210-1-AC3</invocation><expect>IB210-1-AC3 PASS</expect></criterion>

<expected_criteria>IB210-1-AC1, IB210-1-AC2, IB210-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects under the firms' IRPT prefixes (publication, refusal records, manifests, the custodian source partitions, the directory), `list`, `describe`. **Nothing is published, bypassed, re-run against a served prefix, invoked, written to AWS, signed or sent. The producer is NOT run against a served prefix; no bypass is widened (the guard stays).**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to run the producer against a served prefix; an account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W413-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~413/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 206 (round 2, workstream ~PC), cell `IB-pr-570`.
<owned_cells>IB-pr-570</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB210-1-AC1, IB210-1-AC2, IB210-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~413/IRPT_BCKEND.TO-IB-pr-570.read-49-financials-holdings-refusal-which-condition-how-many-accounts-and-which-field.proof_of_spec.json`.
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
comp-adversary: RUN -- p210_cells.py IB210-1 dry-run at base on dell2 2026-10-15 ~11:4xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub publisher file with the guard, screen and validator lines, synthetic records; removed): all three PASS; fourteen negatives on this cell, each failing its own arm: a wrong firm, a wrong behind-count, a wrong T-1, a refused date before the served date, a short per-candidate list, a bad condition row, a wrong guard line, a missing claim, one evidence line, no mechanism, a missing other firm, short notes, a counter above 0, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~413` (worktree `C:/dev/wk-IRPT_BCKEND-413`). Class SERVED (reads a served surface and writes only the worker's records).
</preflight>
