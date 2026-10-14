# TO IRPT_BCKEND.TO-IB-pr-522 -- CENSUS the `account_activity_daily` backfill, READ ONLY: the table, its writers, its sources and the days a 2012-floor backfill would fill; write the plan packet (CTO round-186 analysis item 3; row D2-S153, D2's row IRPT_DASHBD-W141-S3)

<to_id>IRPT_BCKEND.TO-IB-pr-522</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~369</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>186</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-186 analysis (msg 7355: "census and pair first, under the 2012 floor") | **Decomp cell:** `IB-pr-522` (decomposition section 178) | **outcome_ref:** FWD-3 (the default report's contributions, withdrawals and income per window; the dashboard's FWD-21)

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-369` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~369 <0.9.0_WK_IRPT_BCKEND~369@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool; end it with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates can take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-522` (inlined).** The default Investor Reporting report needs contributions, withdrawals and income per window, read from the gold table `account_activity_daily` (one table per firm: `s3://opal-data-<firm bucket>/irpt/<firm>/gold/account_activity_daily/date=<day>/`). Today the 49 Financial table holds 4 daily partitions (2026-10-07, 10-08, 10-09, 10-12; the CTO's relay of D2's read; **verify it**), so those figures read ABSENT for any longer window. **Andrew's rule (2026-10-07, relayed): "we don't need anything prior to the earliest record of a client ... any backfill is thereby cut at 2012"**, so the history goes back to each account's earliest record and never earlier than 2012-01-01 (non-client needs take 365 days; the activity table is for clients). The writer is the Lambda `irpt-reporting-gold` (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`), which emits `account_activity_daily`, `account_lot_realized` and `account_lot_unrealized_daily` through `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py` (`compute_local`, `emit_day`); its explicit backfill event is `{"backfill": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}, "accounts": "population" | [ids], "dry_run": true (optional)}`, bounded by `MAX_BACKFILL_DAYS` per invocation and REFUSING when the range reaches past the newest landed day, holds no trading day, or exceeds the bound (`handler.py` lines 20-40, 118-119, 519-600). **This order MEASURES what a backfill would take and writes a plan packet. It writes NOTHING and invokes NOTHING.**

**Client data rule:** counts, dates, sha256 and reason codes only in any tracked file; no account id, client id or firm bucket key value; extracted data and scratch stay OUTSIDE the worktree (`C:/dev/_scratch369/`), deleted file by file at the end with a short bounded script.

**Read first:** `handler.py` (the module docstring, `backfill_days`, `run_backfill`, `select_days`), `account_activity_lots.py` (its docstring, `compute_local`, `emit_day`, what it READS and WRITES), `infra/aws/terraform/investor-reporting/reporting-gold/locals.tf` and `iam.tf` (the schedule, the role's write set, the table address), and `docs/deployment/MDPF_RUNNER_CODE_SYNC.md` only if a named gate points there.

**Do, in this order (every number is a MEASUREMENT with its source named in `notes`, never an estimate presented as a count):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it).
2. **The writers.** Name EVERY writer of `account_activity_daily`: every file under `infra/` and `data/` that writes the table's keys (start from the handler, `account_activity_lots.py` and the Terraform; use the Grep tool with the table name over `infra/` and `data/`; a zero is NOT an absence: print what the search covered). Record `writers.list` (each `{"file": "<repo path>", "how": "scheduled|backfill|scheduled_and_backfill|other"}`) and `writers.count` (equal to the list length): N writers means N write rules read, and N is printed. Note whether any other path (a manual script, a second Lambda) can write the same keys.
3. **The tables, per firm** (`49financial`, `cottonwood`, `inflection`; READ-ONLY S3 lists with your own identity: list the partitions under the activity table's prefix and under the upstream RETURNS table's prefix (find its name in the handler: the table the activity days follow); count partitions and read the earliest and latest `date=` values; counts and dates only). Record `firms.<firm>.activity_table` and `returns_table` as `{"partitions": n, "earliest": "YYYY-MM-DD", "latest": "YYYY-MM-DD"}` (omit earliest and latest only when `partitions` is 0). If your identity cannot list a bucket, say so in `notes` and in a row, and record what the listing allowed; do not widen.
4. **The demand, per firm.** From the producer's own SOURCES (the producer reads its sources; find what `compute_local` reads: the source tables or objects and their date ranges), determine each firm's earliest activity record date (`earliest_record`, a measured date) and apply the floor: `start_day` = the later of `earliest_record` and 2012-01-01, `floor_applied` the literal `2012-01-01`. `trading_days_to_fill` = the count of trading days from `start_day` to the day BEFORE the activity table's earliest existing partition (use the repository's trading calendar `lib/trading_calendar.py`, never a weekday count); `invocations_needed` = ceil(`trading_days_to_fill` / `chunk_bound_days`), where `chunk_bound_days` is `MAX_BACKFILL_DAYS` read from the handler. Record under `firms.<firm>.demand` as `{"floor_applied":"2012-01-01","earliest_record":"YYYY-MM-DD","start_day":"YYYY-MM-DD","trading_days_to_fill":n,"invocations_needed":n}`. If the producer cannot reach back to a day because its SOURCE does not hold it, `start_day` is the earliest day the source holds and `notes` says so.
5. **The rate.** From the function's CloudWatch log group (`/aws/lambda/irpt-reporting-gold`, READ ONLY), the observed wall seconds per trading day of a recent scheduled or backfill run (`observed_seconds_per_day`, a positive number; cite the run's day count and duration in `notes`); if no log line gives it, record `null` and `observed_seconds_per_day_absence` stating why.
6. **The plan (design only; nothing runs).** Record `plan`: `mechanism` (one line: the handler's explicit backfill event, oldest-first in chunks of `chunk_bound_days`, per firm, `accounts` `"population"`), `event_keys` (the key NAMES only), `idempotent` (true only if re-running a day rewrites the same bytes: read `emit_day`), `overwrites_existing_partitions` (does a backfill over days that already exist overwrite them: read `run_backfill`; the four existing 49 Financial partitions are inside no chunk if the range stops before them), `rollback_possible` (true only if the activity table's bucket has versioning so a rewritten or newly written partition can be undone: read `s3api get-bucket-versioning`, record only the status), `batches` (total invocations across firms), `write_set` (the key SHAPES the backfill writes, no firm or account value: for example `irpt/<firm>/gold/account_activity_daily/date=<day>/...`, and the two lot tables), and, in `notes`, who may run it (the function's role, the invoker's identity class), the dry-run you recommend first, and any chunk that would touch the returns or class tables (a backfill rewrites returns days too: say whether the range this plan needs is inside already-landed returns days).
7. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~369/BACKFILL_PLAN_PACKET_IB-pr-522.md`: the purpose in words; the writers (count and list); the three firms' table state and demand (the numbers of steps 3 and 4); the rate and the time the whole backfill would take; **Branch A** (run order: per firm, oldest-first chunks, a `dry_run` chunk first, the invoker and the identity, the verification after each chunk: the new partitions' count and the returns tables untouched); **Branch B** (rollback: what undoes a chunk, from step 6's versioning read; what cannot be undone, stated); the **blast radius** (the write set, the tables, the firms; what a mis-run can overwrite); **the red list** (`deliverables/0.9.0_WK_IRPT_BCKEND~278/IB117-1_red_list.json`: say whether any path the backfill writes or any file it changes intersects its target prefixes; the backfill changes no repository file); the 2012 floor and Andrew's words as the source of it; the after-read (the default report shows contributions, withdrawals and income for a window longer than 4 days: a person's read on DEV); the pair: the COO half (`2.0.0_SA_COO~P2`) and the CTO half (`1.0.0_SA_CTO~DELL2`), both UNSIGNED; and a section "What this census did not measure".
8. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~369/IB186-2_activity_backfill_census.json`: `{"base_commit":"<40hex>","chunk_bound_days":<n>,"observed_seconds_per_day":<n|null>,"writers":{"count":<n>,"list":[...]},"firms":{"49financial":{"activity_table":{...},"returns_table":{...},"demand":{...}},"cottonwood":{...},"inflection":{...}},"plan":{"mechanism":"...","event_keys":[...],"idempotent":true|false,"overwrites_existing_partitions":true|false,"rollback_possible":true|false,"batches":<n>,"write_set":[...]},"notes":["..."],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
9. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB186-2_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the deliverables FIRST, then the instance with the pins), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check) and run again.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB186-2-AC1" cell_refs="IB-pr-522"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py" . IB186-2-AC1</invocation><expect>IB186-2-AC1 PASS</expect></criterion>
<criterion id="IB186-2-AC2" cell_refs="IB-pr-522"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py" . IB186-2-AC2</invocation><expect>IB186-2-AC2 PASS</expect></criterion>
<criterion id="IB186-2-AC3" cell_refs="IB-pr-522"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py" . IB186-2-AC3</invocation><expect>IB186-2-AC3 PASS</expect></criterion>

<expected_criteria>IB186-2-AC1, IB186-2-AC2, IB186-2-AC3</expected_criteria>

What the checks grade: AC1 the writers counted and named, and for the three firms the partition counts of the activity table and of the upstream returns table with earliest and latest dates; AC2 the per-firm demand with the literal 2012 floor, trading days to fill, and invocations needed equal to ceil(days / chunk bound), the chunk bound, and the observed rate or its stated absence; AC3 the plan (mechanism, event keys, idempotence, overwrite and rollback as booleans, batches, write set), the packet's sections (Branch A, Branch B, writers, 2012, both halves, blast radius, red list, rollback, at least 3000 characters), no long digit run, and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the scratch directory. READ ONLY and DESIGN ONLY. **Nothing is invoked, written, uploaded, applied or deployed:** no Lambda invoke (not even `dry_run: true`: a dry-run invoke is still an invoke), no `aws s3 cp`/`put-object`/`rm`, no `terraform`, no source-map write, no change-management entry, no sign-in, no vendor call. Allowed AWS calls (READ): `s3api list-objects-v2` and `head-object` on the activity and returns table prefixes (counts and dates only, never object bodies), `s3api get-bucket-versioning`, `logs filter-log-events` and `describe-log-streams` on `/aws/lambda/irpt-reporting-gold`, `lambda get-function-configuration` of `irpt-reporting-gold`, `events list-rules` for its schedule, `iam get-role-policy` of its role. Reading an object BODY is allowed ONLY for a SOURCE table's metadata or a single partition's key listing; open no client record.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: any call that writes or invokes; an identity that reads an object body of client data; a figure you cannot source (say so, do not estimate). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W369-S<k>` (start at 1). Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~369/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 178 (round 186, workstream ~P), cell `IB-pr-522`.
<owned_cells>IB-pr-522</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB186-2-AC1, IB186-2-AC2, IB186-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~369/IRPT_BCKEND.TO-IB-pr-522.activity-backfill-census-and-plan.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the census reads the gold tables' partition listings of three firms, the function's configuration and log group, and the repository; it writes nothing and invokes nothing; the backfill's own blast radius (the write set, the tables, the firms) is the plan packet's, for a later pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the census reads with the worker's own identity and records a denial as a count, never widened.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created; the order reads the function's existing schedule only.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p186_cells.py IB186-2 dry-run at base on dell2 2026-10-13 ~23:5xZ: AC1, AC2, AC3 FAIL (no records). Positive control in a temp root the run created itself (synthetic records and a synthetic packet; removed): all three PASS; negatives, each failing its own arm: a writers count that does not equal the list, an earliest date after the latest, a floor other than 2012-01-01, invocations that do not equal ceil(days / bound), an idempotence value that is not a boolean, a write counter above 0, a packet without the 2012 floor.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~369` (worktree `C:/dev/wk-IRPT_BCKEND-369`). Class SERVED (reads S3 listings, logs and the repository; writes only the worker's own records). The premises (the table's 4 partitions, the handler's backfill event and bounds) are the CTO's relay of D2's read and my read of the handler (lines 20-40, 118-119, 519-600); the census verifies them.
</preflight>
