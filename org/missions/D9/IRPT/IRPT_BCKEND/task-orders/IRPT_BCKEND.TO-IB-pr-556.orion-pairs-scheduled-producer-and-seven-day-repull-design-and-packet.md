# TO IRPT_BCKEND.TO-IB-pr-556 -- WRITE the design and the never-widen packet for the Orion pairs: (b) the producer PORTED into the 6 AM ET fold with no second producer, and (a) the seven-day positions re-pull through its path; both halves UNSIGNED, READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-556</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~400</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8014 (cut both pairs as packets, three conditions) on the READ `IB-pr-552` (row D2-S182) | **Decomp cell:** `IB-pr-556` (decomposition section 195) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-400`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~400 <0.9.0_WK_IRPT_BCKEND~400@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch400/`).

**Cell `IB-pr-556` (inlined).** The CTO ruled (msg 8014) on the Orion READ (`deliverables/0.9.0_WK_IRPT_BCKEND~396/IB199-4_orion_raw_producer_read.json`, rows `D2-W396-S1` to `S7` and `D2-S182`; READ ALL FIRST): cut BOTH pairs as packets, with three conditions. **(b)** the scheduled producer in the 6 AM New York fold (ruling @23eff24d0c, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DAILY_6AM_PULLS_FOLD_20261014.md`) PORTS `data/inf/manual_api/pull_inflection_positions_daily.py` into the scheduled function (`infra/aws/lambda/inf-pipeline/inf-api-positions/pull_inflection_positions_daily.py`): NO second producer beside it (no shadow pipeline); the manual CLI is retired or repointed in the same pair. **(a)** the one-time re-pull of the seven dropped positions days (2026-07-01, 2026-07-03, 2026-07-04, 2026-07-05, 2026-08-06, 2026-09-28, 2026-09-29) writes THROUGH (b)'s code path to the flat key the mirror reads (`s3://opal-data-inf/bronze/positions/<date>.jsonl.gz`), reads the seven keys ABSENT before writing, and paces the 2,240 requests. Names and addresses come from `lib/opal_naming.py` `address()`/`name()` output, the producer stamps the previous trading day (`lib/trading_calendar.py`). If `2.0.0_SA_COO~I2`'s Scope probe (B-IN round 117) passes, the account feed joins (b) by addendum, not a third pair. **This order WRITES THE DESIGN AND ONE PACKET covering both pairs. It builds, changes, pulls and deploys NOTHING, and makes no Orion request.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Read** the READ record and its rows; both `pull_inflection_positions_daily.py` files at HEAD (the manual one under `data/inf/manual_api/` and the deployed one under `infra/aws/lambda/inf-pipeline/inf-api-positions/`: what the deployed one writes today, what the manual one adds, the flat-key writer near line 445 of the manual one); `data/inf/scripts/bronze/rate_limiter.py`; the schedule declarations for `inf-api-positions-daily` and the bronze-runner (Terraform under `infra/aws/terraform/`: Glob the directory list first); the mirror `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py` (what it reads and when); `lib/opal_naming.py` (is there a SCHEDULE kind in `name()`, and is a registry row needed for the new schedule?) and `lib/trading_calendar.py`. **Locate the live daily writer** of the flat positions key (the READ found 94 flat keys dated on or after 2026-07-10, the newest 2026-10-14 ~11:51Z, written by a writer the repository does not hold): with describe/list/head reads only (EventBridge, Lambda, SSM, the object metadata of a few flat keys), say what writes them; `absent` with the search stated is an allowed answer.
3. **Write the design** `deliverables/0.9.0_WK_IRPT_BCKEND~400/IB200-4_orion_pairs_design.json`: `{"base_commit":"<40hex>","live_writer":{"claim":"measured|inferred|absent","statement":"<40+ characters>","evidence":["<line naming a source>","<second line>"]},"pair_b":{"files":[{"path":"<repo path>","line":<n>,"identifier":"<a name ON that line>"},...],"port":"<what moves from the manual CLI into the scheduled function, 40+ characters>","cli_disposition":"<the CLI is retired or repointed in the same pair: say which and how, 30+ characters>","no_second_producer":true,"schedule_builder_output":"<the schedule and function names as the OUTPUT of lib/opal_naming.py name(), and any registry row needed; must contain the word opal_naming, 20+ characters>","trading_day_frontier":"<how the producer stamps the previous trading day and what it does on a non-trading day, 20+ characters>"},"pair_a":{"days":[{"date":"2026-07-01","trading_day":true|false},... the seven days in this order],"keys":["s3://opal-data-inf/bronze/positions/2026-07-01.jsonl.gz",... the seven flat keys in the same order],"absent_beforehand_read_at_act":true,"through_b_code_path":true,"requests":<n>,"pacing":"<20+ characters>","read_back":"<30+ characters>","rollback_per_key":"<30+ characters>","non_trading_policy":"<what the re-pull does for a day that is not a trading day, 30+ characters>"},"blast_radius":{"writes":["<each key or resource the pairs create>"],"reads":["<what they read>"],"new_iam":true|false,"served_values_changed":false,"other_dates_touched":false},"build_slices":[{"cell":"<name>","risk":"LOCAL","files":["<paths the slice writes>"],"depends_on":["<cell>"]},...],"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. Every `pair_b.files` entry is a site the check reads at HEAD. At least two LOCAL build slices (for example the port with its tests, the schedule declaration), each naming the files it writes.
4. **Write the packet** `deliverables/0.9.0_WK_IRPT_BCKEND~400/ORION_PAIRS_PACKET_V1.md`, at least 6,000 characters, in the shape of `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md` (READ IT for the sections: change set, blast radius, rollback per key, stop rule, the releasing seat's NEVER-2 ledger, what the packet does not measure, signatures). It must carry these phrases (case-insensitive): "never-widen", "pair (a)", "pair (b)", "blast radius", "rollback", "stop rule", "opal_naming", "trading-day frontier", "no shadow", "COO half", "CTO half"; the order of the acts (b built and deployed first; (a) runs through (b)'s path after); and **both halves UNSIGNED**, the packet's sha256 LEFT for the signers (do not compute it).

5. **Notes and counters:** `notes` say what each fact rests on and what was not read (no Orion request is made; the live deployment is read by describe/list/head only).

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB200-4_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, packet and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or packet (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB200-4-AC1" cell_refs="IB-pr-556"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-4-AC1</invocation><expect>IB200-4-AC1 PASS</expect></criterion>
<criterion id="IB200-4-AC2" cell_refs="IB-pr-556"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-4-AC2</invocation><expect>IB200-4-AC2 PASS</expect></criterion>
<criterion id="IB200-4-AC3" cell_refs="IB-pr-556"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py" . IB200-4-AC3</invocation><expect>IB200-4-AC3 PASS</expect></criterion>

<expected_criteria>IB200-4-AC1, IB200-4-AC2, IB200-4-AC3</expected_criteria>

What the checks grade: AC1 the live daily writer with a claim and two evidence lines; pair (b): its files each read at HEAD, the port, the manual CLI retired or repointed in the same pair, no second producer, the schedule and function names as the naming builder's output, the trading-day frontier; AC2 pair (a): the seven days (each with its trading-day flag) and their seven flat keys in order, read ABSENT before writing, written through (b)'s path, the request count, pacing, read-back, rollback per key, the non-trading policy, and the blast radius with served values and other dates unchanged; AC3 the packet at least 6,000 characters with the phrases and both halves UNSIGNED, at least two LOCAL build slices naming files, notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY. **Nothing is built, changed, pulled, re-pulled, deployed, written to AWS, invoked, signed or sent, and no Orion request is made:** the only AWS calls are `list`, `get`, `head` and `describe` reads with your identity. A denial is recorded, never worked around.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes, pulls or sends; a need to read a secret value; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W400-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~400/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 195 (round 2, workstream ~PO), cell `IB-pr-556`.
<owned_cells>IB-pr-556</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB200-4-AC1, IB200-4-AC2, IB200-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~400/IRPT_BCKEND.TO-IB-pr-556.orion-pairs-scheduled-producer-and-seven-day-repull-design-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads repository files and describes live schedule and function objects with the worker's own identity; it writes one design record and one packet in the worker's deliverables; nothing is built, pulled or deployed, so no served byte moves; the pairs the packet describes (a Lambda port, a schedule, a seven-key re-pull) are later acts under two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed by this order; whether the later pairs need one is a question the design answers with a file and line.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB200-4 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; thirteen negatives on this cell, each failing its own arm: a CLI not retired, a second producer, schedule names typed, a wrong file identifier, thin live-writer evidence, six days only, a key for another date, not through (b)'s path, other dates touched, a packet too short, one half signed, one build slice, a vendor request already sent.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~400` (worktree `C:/dev/wk-IRPT_BCKEND-400`). Class SERVED (a design for a scheduled producer and a vendor write; the order reads and writes only the worker's records).
</preflight>
