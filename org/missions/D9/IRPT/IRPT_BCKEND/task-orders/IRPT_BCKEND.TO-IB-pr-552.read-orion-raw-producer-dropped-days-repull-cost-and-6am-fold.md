# TO IRPT_BCKEND.TO-IB-pr-552 -- READ the Orion Inflection raw producer: where the flat .jsonl.gz feeds come from, every day the mirror silently dropped, what the re-pull costs per feed, and the 6 AM ET fold design; READ ONLY (CTO msg 7980 on row D2-S180: "locate the raw producer, then cost the re-pull per feed, then the pair")

<to_id>IRPT_BCKEND.TO-IB-pr-552</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~396</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 7980 (egress is open, so no per-use word is needed; pace the re-pull) and msg 7914 | **Decomp cell:** `IB-pr-552` (decomposition section 193) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-396`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~396 <0.9.0_WK_IRPT_BCKEND~396@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named directories). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.** AWS CLI goes through the `.tools/aws` shim.

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function and schedule names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch396/`).

**Cell `IB-pr-552` (inlined).** The previous READ (IB-pr-550, record `deliverables/0.9.0_WK_IRPT_BCKEND~394/IB199-1_orion_gap_read.json` and rows `IRPT_BCKEND-D2-W394-S1` to `S5` and `D2-S180` in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, READ ALL FIRST) found: the Orion Inflection source bucket `opal-data-inf` holds, for 2026-07-01 and 2026-09-28, only a `.parquet` positions object (written by `infra/aws/lambda/inf-pipeline/inf-api-positions/pull_inflection_positions_daily.py`) and no transactions or performance object; the mirror `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py` copies only flat `.jsonl.gz` keys (line 77 `COERCED_SUFFIXES = (".parquet",)`, line 493); the repo holds no writer of the flat `.jsonl.gz` positions key (row W394-S3) although the source holds about 2,358 such objects; and the 06:00 ET fold (ruling @23eff24d0c, S2) covers none of the 155 live rules for this feed. The CTO asks, in order: (1) locate the raw producer; (2) read whether ANY other day landed raw as `.parquet` and was silently dropped (a format the mirror ignores is a defect to fix at the mirror, not per day); (3) cost the re-pull per feed (requests, pacing, time); (4) design the Orion raw producer's place in the 6 AM ET fold (S2: one schedule, builder names, trading-day frontier; also P1's input); (5) fold in the feed `2.0.0_SA_COO~I2`'s account-performance read (B-IN round 116) may add. **This order READS. It pulls, re-pulls and writes NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Locate the raw producer (CTO point 1).** Search named places only: `infra/aws/lambda/inf-pipeline/` subdirectories (Glob the directory list first, then Read the entry files and Grep the named directories for `.jsonl.gz`, `jsonl`, `gzip`, `orion`), `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py` (its header names a raw producer that stopped on 2026-07-10), `workflows/atom_decomposition/catalog_entries/` entries for the Orion feeds, and live reads (Lambda `list-functions` with names or tags matching inf/orion, EventBridge `list-rules`, `describe` only; the write timestamps and object metadata of a few existing `.jsonl.gz` keys via `head-object`, which may name the writer role or user). Record `raw_producer` = `{"claim":"measured|inferred|absent","statement":"<who writes the flat .jsonl.gz keys, where it runs, since when and whether it still runs, 40+ characters>","site":{"path":"<repo path>","line":<n>,"identifier":"<a name ON that line>"},"evidence":["<line naming a source and a count>", ...]}` (at least two evidence lines; for `absent`, say exactly which places were searched; a `measured` claim needs a `site` the check reads at HEAD). If the producer is outside the repository, say where it runs (name only) and `claim` `inferred`.
3. **The dropped-day census (CTO point 2).** For EACH of the three feeds (positions, transactions, performance) over the FULL history in `opal-data-inf`: LIST the feed's prefix paginated to the end (print the denominator), then count `source_keys_total`, `jsonl_gz_days` (days with a flat `.jsonl.gz` key), `parquet_only_days` (days with a `.parquet` key and NO `.jsonl.gz`), and `silently_dropped_days` (the parquet-only days that have no bronze key at `s3://opal-data-assets/orion/inflection/bronze/<feed>/` either, by LIST). Record `parquet_census` = `{"feeds":{"positions":{"source_keys_total":n,"jsonl_gz_days":n,"parquet_only_days":n,"silently_dropped_days":n,"denominator_note":"<what was listed, how, 20+ characters>"},"transactions":{...},"performance":{...}}}` (the check requires dropped <= parquet-only <= total keys, and positions parquet-only >= 2 because 2026-07-01 and 2026-09-28 are known). Record `mirror_defect` = `{"claim":"measured|inferred|absent","statement":"<is a format the mirror ignores a defect to fix at the mirror: which line, which rule, and the days it affects, 40+ characters>"}`. Counts and ISO dates only; never list a day by a client.
4. **Cost the re-pull per feed (CTO point 3).** Record `cost` = `{"positions":{"requests":n,"pacing":"<the vendor's pacing or rate limit as the code or docs state it, and what the pull code does about it, 15+ characters>","hours":x,"claim":"measured|inferred|absent"},"transactions":{...},"performance":{...}}`: the number of Orion API requests for the dropped days of that feed (read the three pull handlers in `infra/aws/lambda/inf-pipeline/inf-api-positions/`, `inf-api-txn/` and the performance puller if one exists: how many requests per household per date, and the household count as a COUNT read from the newest `household_rep_mapping` silver partition, never the ids), and an honest wall-clock estimate in hours from the code's own pacing (state the arithmetic in `notes`). No request is made.
5. **The 6 AM ET fold design (CTO point 4).** READ `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DAILY_6AM_PULLS_FOLD_20261014.md` and the S2 ruling it cites (@23eff24d0c). Record `fold_design` = `{"schedule":"<one 06:00 America/New_York schedule for the Orion raw producer: what fires it and how it replaces or joins the live rules, 20+ characters>","builder_names":"<the schedule and function names are the OUTPUT of lib/opal_naming.py name() (say which builder call and which registry row, or that a row is missing); this text must contain the word opal_naming, 20+ characters>","trading_day_frontier":"<how the producer stamps the previous trading day by lib/trading_calendar.py and what it does on a non-trading day, 20+ characters>","covers_feeds":["positions","transactions","performance"]}`.
6. **The ~I2 feed (CTO point 5).** READ `org/missions/D9/IRPT/IRPT_DASHBD/` for B-IN round 116 (the account-performance read of `2.0.0_SA_COO~I2`: Glob its deliverables folder `deliverables/2.0.0_SA_COO~I2/` newest drain-end packet and the round-116 order or read file, if any exists yet). Record `i2_feed` = `{"claim":"measured|inferred|absent","statement":"<which Orion feed that read may add, or that it is not yet written, 30+ characters>"}`.
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~396/IB199-4_orion_raw_producer_read.json`: `{"base_commit":"<40hex>","raw_producer":{..},"parquet_census":{..},"mirror_defect":{..},"cost":{..},"fold_design":{..},"i2_feed":{..},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB199-4_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB199-4-AC1" cell_refs="IB-pr-552"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-4-AC1</invocation><expect>IB199-4-AC1 PASS</expect></criterion>
<criterion id="IB199-4-AC2" cell_refs="IB-pr-552"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-4-AC2</invocation><expect>IB199-4-AC2 PASS</expect></criterion>
<criterion id="IB199-4-AC3" cell_refs="IB-pr-552"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-4-AC3</invocation><expect>IB199-4-AC3 PASS</expect></criterion>

<expected_criteria>IB199-4-AC1, IB199-4-AC2, IB199-4-AC3</expected_criteria>

What the checks grade: AC1 the raw producer with a claim, a statement and two evidence lines (a `measured` one with a site read at HEAD) and the dropped-day census for the three feeds as counts with a denominator note (dropped <= parquet-only <= total, positions parquet-only >= 2); AC2 the re-pull cost per feed (requests, pacing words, hours, claim), the fold design (schedule, builder names containing `opal_naming`, trading-day frontier, all three feeds), and the ~I2 feed statement; AC3 the mirror defect with a claim, notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY. **Nothing is pulled, re-pulled, invoked, written to AWS, uploaded, converted, deleted, signed or sent, and no Orion API request is made:** the only AWS calls are `list`, `get`, `head`, `describe` and `filter-log-events` reads with your identity. A denial is recorded, never worked around or widened. No secret value is read (names only).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes, pulls or sends; a client identifier in a tracked file; a need to read a secret value. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W396-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~396/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 193 (round 1, workstream ~PO), cell `IB-pr-552`.
<owned_cells>IB-pr-552</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB199-4-AC1, IB199-4-AC2, IB199-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~396/IRPT_BCKEND.TO-IB-pr-552.read-orion-raw-producer-dropped-days-repull-cost-and-6am-fold.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order lists S3 prefixes and reads object metadata, describes Lambda and EventBridge objects and reads repository files with the worker's own identity; it writes only the worker's records; nothing is pulled, mirrored or converted, so no served byte moves; the pair the READ prepares is a later act.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity (a denial is recorded, not widened).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: schedule objects are described (read), never created or changed; the fold design is a proposal in the record.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p199_cells.py IB199-4 dry-run at base on dell2 2026-10-15 ~04:2xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp git root the run created itself (a synthetic record and a stub producer file; removed): all three PASS; thirteen negatives across IB199-4, each failing its own arm: a measured producer with the wrong identifier, one evidence line, dropped above parquet-only, a feed missing from the census, positions with fewer than two parquet-only days, a cost with no pacing, a cost feed missing, builder names typed by hand, a fold that omits a feed, no ~I2 statement, no mirror defect statement, a long digit run, a vendor request already sent.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~396` (worktree `C:/dev/wk-IRPT_BCKEND-396`). Class SERVED (reads served prefixes and live schedule objects; writes only the worker's records).
</preflight>
