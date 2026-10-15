# TO IRPT_BCKEND.TO-IB-pr-560 -- WRITE the design and the never-widen packet v2 for the Orion pairs RE-CUT: (b) re-time the existing inf-gold-trigger chain into the 06:00 New York fold (no new function, no port), (a) re-run the 36 absent trading days through the chain's own pull steps; both halves UNSIGNED, READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-560</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~404</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8127 (re-cut, consolidate never build alongside) on the READ `IB-pr-559` (row D2-S186) | **Decomp cell:** `IB-pr-560` (decomposition section 198) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-404`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~404 <0.9.0_WK_IRPT_BCKEND~404@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name; tests use synthetic ids. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch404/`).

**Cell `IB-pr-560` (inlined).** The CTO voided the Orion pairs packet's design of pair (b) (msg 8127) after the READ `IB-pr-559` located the writer (record `deliverables/0.9.0_WK_IRPT_BCKEND~403/IB202-1_flat_key_writer_read.json`, rows `IRPT_BCKEND-D2-W403-S1` to `S4`, `D2-S186`; READ ALL FIRST): the daily flat Orion keys are written by the three Orion pull steps (`INF_API_PULL_TXN`, `INF_API_PULL_PERF`, `INF_API_PULL_POSITIONS_DAILY`) of the gold chain (`orion-gold-dispatch.sh`, `chain:full`) on the `inf-gold-layer-runner` EC2, started by the `inf-gold-trigger` Lambda at about 11:32Z, which `inf-silver-aggregator` fires; the same pulls feed the silver transactions and performance steps. The CTO's ruling: **consolidate, never build alongside.** (b) = MOVE `inf-gold-trigger` into the 06:00 America/New_York fold (ruling @23eff24d0c, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DAILY_6AM_PULLS_FOLD_20261014.md`): no new function, no port, the silver steps stay chained; BEFORE it lands, the design reads whether Orion's T-1 is complete by 06:00 NY, and if it is not, names the earliest measured-complete time with that reason. (a) = re-run the 36 absent trading days (positions 7: 2026-07-01, 07-03, 07-04, 07-05, 08-06, 09-28, 09-29; transactions 7: 2026-07-01, 07-13, 07-14, 07-15, 08-06, 09-28, 09-29; performance 22 between 2026-05-03 and 2026-10-14 including 2026-07-01 and 2026-09-28, computed by `lib/trading_calendar.py` `trading_days_between` minus the days that hold a key in either format) THROUGH the chain's own pull steps, each key read ABSENT first; where the vendor returns nothing record ABSENT-AT-SOURCE with the response status and never write an empty key. The manual CLIs' bronze writes are retired in the same pair, each exiting with a message that names the chain; a delete stays Andrew's act. The Scope account feed joins by a later addendum (not this packet). **This order WRITES THE DESIGN AND ONE PACKET (v2, which SUPERSEDES the IB-pr-556 packet). It builds, changes, pulls and deploys NOTHING and makes no Orion request.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Read** the READ record and its rows; CTO msg 8127 as quoted above; the chain from its HEAD: what starts `inf-silver-aggregator` and so `inf-gold-trigger` each day (the scheduled rule or rules of the bronze runner and the aggregator: `events list-rules` / `describe-rule` / `list-targets-by-rule`, the Lambda sources under `infra/aws/lambda/inf-pipeline/` (Glob the directory list first: `inf-gold-trigger`, `inf-silver-aggregator`, `inf-bronze-trigger`) and their Terraform under `infra/aws/terraform/` (Glob first)); the dispatch script `code/gold/orion-gold-dispatch.sh` (repository copy if there is one, else the S3 object by GET); the three manual CLIs (`data/inf/manual_api/pull_inflection_{positions,transactions,performance}_*.py`) and which of their bronze writes the chain's copies make; `lib/opal_naming.py` (any NEW name) and `lib/trading_calendar.py`.
3. **What exactly moves (CTO: "move inf-gold-trigger into the 06:00 NY fold").** The trigger is fired by an event chain, not a schedule of its own: find the FIRST scheduled link of that chain and state which rule's cron changes (or which new schedule replaces it) so that the gold chain's Orion pulls run in the 06:00 New York fold, in EDT and EST, with the silver steps still chained after them. Name every resource that changes (rule or schedule, Lambda environment, the auto-shutdown) and every resource that does not.
4. **T-1 completeness by 06:00 NY (READ, no Orion request).** Record `pair_b.t1_completeness` = `{"claim":"measured|inferred|absent","statement":"<is Orion's T-1 complete by 06:00 NY; if not, the earliest measured-complete time and why; must contain a clock time, 40+ characters>","evidence":["<line naming a source and a time>", ...]}` from what exists without a vendor call: the landing times of the pull outputs against the as-of timestamps inside a few recent pulls' bronze objects (a field in the record, read by GET of a small object; counts and timestamps only), the chain logs `diagnostic/chain_logs`, the 6AM-fold ruling and the vendor documentation or code comments. If the evidence cannot show completeness at 06:00, propose in `pair_b.measurement_plan` the one-time probe that would (the earliest hour, how many requests, read-only) and mark the claim `inferred`.
5. **Write the design** `deliverables/0.9.0_WK_IRPT_BCKEND~404/IB203-1_orion_recut_design.json`: `{"base_commit":"<40hex>","pair_b":{"files":[{"path":"<repo path>","line":<n>,"identifier":"<a name ON that line>"},...],"retiming":"<40+ characters; must name inf-gold-trigger and the 06:00 fold>","new_function":false,"port":false,"silver_steps_chained":true,"t1_completeness":{..},"measurement_plan":"<30+ characters or 'not needed: ..'>","cli_retirement":"<40+ characters; each manual CLI's bronze writes removed and it exits with a message that names the chain>","schedule_builder_output":"<any NEW schedule name as the OUTPUT of lib/opal_naming.py name(), or that none is new; contains the word opal_naming, 20+ characters>","trading_day_frontier":"<20+ characters>"},"pair_a":{"feeds":{"positions":{"days":[7 ISO dates],"keys":["s3://opal-data-inf/bronze/positions/<date>.jsonl.gz",...],"requests":<n>,"chain_step":"INF_API_PULL_POSITIONS_DAILY"},"transactions":{"days":[7],"keys":[..],"requests":<n>,"chain_step":"INF_API_PULL_TXN"},"performance":{"days":[22],"keys":[..],"requests":<n>,"chain_step":"INF_API_PULL_PERF"}},"absent_beforehand_read_at_act":true,"through_chain_steps":true,"read_back":"<30+ characters>","rollback_per_key":"<30+ characters; a delete is Andrew's act>","absent_at_source_policy":"<40+ characters; must say ABSENT-AT-SOURCE is recorded with the response status and an empty key is never written>"},"blast_radius":{"writes":[..],"reads":[..],"new_iam":true|false,"served_values_changed":false,"other_dates_touched":false},"build_slices":[{"cell":"<name>","risk":"LOCAL","files":["<paths the slice writes>"],"depends_on":["<cell>"]},...],"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. Every `pair_b.files` entry is a site the check reads at HEAD. The key days for the three feeds must be the exact days above (the check lists them).
6. **Write the packet** `deliverables/0.9.0_WK_IRPT_BCKEND~404/ORION_RECUT_PAIRS_PACKET_V2.md`, at least 6,000 characters, in the shape of `deliverables/0.9.0_WK_IRPT_BCKEND~400/ORION_PAIRS_PACKET_V1.md` (READ IT for the sections), saying plainly that it SUPERSEDES the V1 packet for pair (b)'s design and re-states pair (a); it must carry these phrases (case-insensitive): "never-widen", "pair (a)", "pair (b)", "blast radius", "rollback", "stop rule", "re-timing", "inf-gold-trigger", "no shadow", "supersede", "COO half", "CTO half"; the order of the acts ((b)'s landing and one clean scheduled day, then (a)); the T-1 completeness result; and **both halves UNSIGNED**, the sha256 LEFT for the signers (do not compute it).

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB203-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, packet and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or packet (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB203-1-AC1" cell_refs="IB-pr-560"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py" . IB203-1-AC1</invocation><expect>IB203-1-AC1 PASS</expect></criterion>
<criterion id="IB203-1-AC2" cell_refs="IB-pr-560"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py" . IB203-1-AC2</invocation><expect>IB203-1-AC2 PASS</expect></criterion>
<criterion id="IB203-1-AC3" cell_refs="IB-pr-560"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py" . IB203-1-AC3</invocation><expect>IB203-1-AC3 PASS</expect></criterion>

<expected_criteria>IB203-1-AC1, IB203-1-AC2, IB203-1-AC3</expected_criteria>

What the checks grade: AC1 pair (b): its files each read at HEAD, a re-timing that names inf-gold-trigger and the 06:00 fold, no new function and no port, the silver steps chained, the T-1 completeness read with a clock time and two evidence lines, the manual CLIs retired with a message naming the chain, any new name from the builder; AC2 pair (a): every absent trading day of the three feeds (7, 7 and 22) with its flat key and the chain's own pull step, read ABSENT first, ABSENT-AT-SOURCE and never an empty key, read-back, rollback, and the blast radius; AC3 the packet at least 6,000 characters with the phrases, saying it supersedes V1, both halves UNSIGNED, a LOCAL build slice, notes, counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY. **Nothing is built, changed, stopped, started, pulled, re-pulled, deployed, written to AWS, invoked, signed or sent, and no Orion request is made:** the only AWS calls are `describe`, `list`, `get`, `head` and `lookup` reads with your identity.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, starts, stops, invokes, pulls or sends; a need to read a secret value; an account number, ARN with an account number or IP address in a tracked file; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W404-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~404/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 198 (round 4, workstream ~PO), cell `IB-pr-560`.
<owned_cells>IB-pr-560</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB203-1-AC1, IB203-1-AC2, IB203-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~404/IRPT_BCKEND.TO-IB-pr-560.orion-recut-gold-chain-retiming-and-36-day-rerun-design-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads repository files and describes live schedule and function objects with the worker's own identity; it writes one design record and one packet in the worker's deliverables; nothing is built, pulled, stopped or deployed, so no served byte moves; the pairs the packet describes (a re-timing of an existing trigger, a 36-key re-run through the chain) are later acts under two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed by this order.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p200_cells.py IB203-1 dry-run at base on dell2 2026-10-15 ~05:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub packages at the real relative paths, a worker commit, synthetic records; removed): all three PASS; seventeen negatives on IB203-1, each failing its own arm: a new function built alongside, a port, silver steps not chained, a re-timing that names no trigger, no clock time in the completeness read, a CLI not naming the chain, a wrong file identifier, performance at 21 days, a feed missing, not through the chain's steps, no chain step name, no ABSENT-AT-SOURCE policy, other dates touched, a packet too short, a packet that does not supersede, one half signed, a vendor request already sent.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~404` (worktree `C:/dev/wk-IRPT_BCKEND-404`). Class SERVED (a design over a scheduled chain and a vendor write; the order reads and writes only the worker's records).
</preflight>
