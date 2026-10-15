# TO IRPT_BCKEND.TO-IB-pr-550 -- READ the Orion Inflection gap (2026-07-01 and 2026-09-28): the pull path stage by stage, why the scheduled pull skipped the two days, and the re-pull method that writes only those days' keys; READ ONLY (CTO ruling, msg 7914, row IRPT_DASHBD-D2-W302-S2)

<to_id>IRPT_BCKEND.TO-IB-pr-550</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~394</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>199</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `msg 7914` (the Orion pull and its sweep belong to IRPT_BCKEND under the 6 AM ET fold; re-pull both days under a never-widen pair; ask why the scheduled pull skipped them) | **Decomp cell:** `IB-pr-550` (decomposition section 191) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-394`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~394 <0.9.0_WK_IRPT_BCKEND~394@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.** AWS CLI goes through the `.tools/aws` shim.

**Client data rule:** counts, dates, hashes, commit ids, object-key prefixes, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch394/`).

**Cell `IB-pr-550` (inlined).** The channel row `IRPT_DASHBD-D2-W302-S2` (in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`) and the record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~302/DATE_GAP_READ_R114.json` (READ BOTH FIRST) measured that the two NYSE trading days **2026-07-01 and 2026-09-28 are absent** from the Orion Inflection silver tables `fact_positions`, `fact_performance` and `fact_transactions` and from the bronze feeds `positions`, `performance` and `transactions` under `s3://opal-data-assets/orion/inflection/bronze/`, while `fact_assets` and the bronze `assets` feed hold both days. The CTO ruled the pull is IRPT_BCKEND's, and that a later order will re-pull exactly those two days under a never-widen pair. **This order is the READ that pair needs. It re-pulls and writes NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Census the target partitions, EMPTY beforehand.** For each of the two dates, by LIST (paginated to the end, counts printed beside the denominator): the three bronze feed prefixes `s3://opal-data-assets/orion/inflection/bronze/{positions,performance,transactions}/` (count the keys carrying the ISO date, with and without dashes) and the three silver tables `fact_positions`, `fact_performance`, `fact_transactions` (the partition for the date). Each of the six counts per date must read 0 (else STOP: a non-empty partition is not a gap). Record `trading_day` true for both dates from `lib/trading_calendar.py`.
3. **Name the pull path stage by stage.** Find, by READING the repository (Glob and Grep on named directories; start at `infra/aws/lambda/opal-assets/opal-assets-silver-orion/` (`lambda_function.py`, `mirror_conversion.py`, `backfill_status.py`), `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/`, `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/`, and the catalog entry `workflows/atom_decomposition/catalog_entries/opal_data_assets_silver_orion_inflection_fact_positions.yaml`) and by LIVE DESCRIBE reads of the schedule objects (EventBridge rules and SSM schedules naming Orion, `describe` and `list` only): (i) what pulls from the vendor into bronze (`vendor_pull`), (ii) what writes the bronze keys (`bronze_write`), (iii) what converts bronze to silver (`silver_convert`) and what fires it, (iv) what triggers each of those (`trigger`), including the 6 AM ET fold (rulings @23eff24d0c) if it covers this feed. Each stage is `{"kind":"vendor_pull|bronze_write|silver_convert|trigger","claim":"measured|inferred|absent","producer":"<repo path>:<line>","identifier":"<a name appearing ON that line>","trigger":"<words: what fires it and when>"}`; a `measured` stage must cite a path:line that exists at HEAD with the identifier on the line (the check reads it); a stage you could not find is `absent` or `inferred`, never guessed. If no repository code pulls the Orion bronze feeds (they arrive by an external delivery), say so as an `absent` `vendor_pull` stage with the evidence.
4. **Why the scheduled pull skipped the two days.** Read the evidence that exists without writing: the meta layer (`s3://opal-data-assets/orion/inflection/meta/` conversion records and the backfill status object, GET only), the lambda's CloudWatch log groups for the two dates and the days around them (`logs filter-log-events`/`get-log-events`, read only, counts and error class names only), the catalog entry, and the converter header. Record `skip_cause` = `{"claim":"measured|inferred|absent","statement":"<what happened and why, 40+ characters>","evidence":["<line naming a source and a count or class name>", ...]}` with at least two evidence lines unless the claim is `absent` (no cause found; say what you looked at). A cause is `measured` only if an artifact states it; otherwise `inferred`.
5. **The re-pull method (PROPOSED, NOT EXECUTED).** Record `repull_method` = `{"writes":["s3://opal-data-assets/orion/inflection/<bronze or silver prefix>/<one of the two dates, in the key form the feed uses>/", ...],"writes_only_the_two_dates":true,"executed":false,"read_back":"<how each written key is read back and compared before the silver conversion runs, 30+ characters>","rollback_per_key":"<how each created key is removed, by version id, 30+ characters>","vendor_calls_needed":<count of Orion API requests the re-pull would make>}`. Every write prefix sits under `s3://opal-data-assets/orion/inflection/` and names one of the two dates; nothing else is written. State in `notes` which seat could run it (the converter fires on an object-created event: say whether re-pulled bronze keys would also trigger conversion of other dates), what sign-in or secret the vendor call needs by NAME only, and what you did NOT read.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~394/IB199-1_orion_gap_read.json`: `{"base_commit":"<40hex>","dates":{"2026-07-01":{"trading_day":true,"claim":"measured","empty_beforehand":{"bronze_positions":0,"bronze_performance":0,"bronze_transactions":0,"silver_fact_positions":0,"silver_fact_performance":0,"silver_fact_transactions":0}},"2026-09-28":{...}},"pull_path":{"stages":[...]},"skip_cause":{...},"repull_method":{...},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB199-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB199-1-AC1" cell_refs="IB-pr-550"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-1-AC1</invocation><expect>IB199-1-AC1 PASS</expect></criterion>
<criterion id="IB199-1-AC2" cell_refs="IB-pr-550"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-1-AC2</invocation><expect>IB199-1-AC2 PASS</expect></criterion>
<criterion id="IB199-1-AC3" cell_refs="IB-pr-550"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-1-AC3</invocation><expect>IB199-1-AC3 PASS</expect></criterion>

<expected_criteria>IB199-1-AC1, IB199-1-AC2, IB199-1-AC3</expected_criteria>

What the checks grade: AC1 both dates trading days and all six target partitions per date reading 0, each as a measured claim; AC2 the pull path stage by stage (a `silver_convert` stage required; every `measured` stage a path:line at HEAD holding its identifier) and the skip cause carrying its claim and at least two evidence lines unless absent; AC3 the proposed method writes only keys under the Orion Inflection prefix naming one of the two dates, executed false, read-back and per-key rollback stated, notes present, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY. **Nothing is pulled, re-pulled, invoked, written to AWS, uploaded, converted, deleted, signed or sent, and no Orion API request is made:** the only AWS calls are `list`, `get`, `describe` and `filter-log-events` reads with your identity on the Orion Inflection prefixes, the converter lambda's log groups and the schedule objects. A denial is recorded, never worked around or widened. No secret value is read (the secret's NAME only).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes, pulls or sends; a non-empty target partition; a client identifier in a tracked file; a need to read a secret value. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W394-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~394/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 191 (round 199, workstream ~P), cell `IB-pr-550`.
<owned_cells>IB-pr-550</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB199-1-AC1, IB199-1-AC2, IB199-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~394/IRPT_BCKEND.TO-IB-pr-550.read-orion-inflection-gap-days-pull-path-and-repull-method.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order lists S3 prefixes, reads the meta objects and the converter lambda's log groups, and describes schedule objects with the worker's own identity; it writes only the worker's records; nothing is pulled or converted, so no served byte moves; the re-pull this READ prepares is a later order under a never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity (a denial is recorded, not widened).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: schedule objects are described (read), never created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p199_cells.py IB199-1 dry-run at base on dell2 2026-10-15 ~02:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp git root the run created itself (synthetic records and a stub producer; removed): all three PASS; thirteen negatives across IB199-1, each failing its own arm: a gap date not a trading day, a target partition not empty, one date only, a measured stage with a wrong identifier, a line past the file, no silver_convert stage, an unknown cause claim, an inferred cause with one evidence line, a re-pull writing another date, a write outside the prefix, a method marked executed, a vendor request already sent, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~394` (worktree `C:/dev/wk-IRPT_BCKEND-394`). Class SERVED (reads served prefixes and live schedule objects; writes only the worker's records).
</preflight>
