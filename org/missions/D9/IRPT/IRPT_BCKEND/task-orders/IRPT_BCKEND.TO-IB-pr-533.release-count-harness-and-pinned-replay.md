# TO IRPT_BCKEND.TO-IB-pr-533 -- COMMIT the release re-measure HARNESS and REPLAY it on pinned inputs, so the signed packet's stop rule is a deterministic comparison, READ ONLY (CTO round-192 analysis item 1 @296869062d; packet IB-pr-532 sha256 4129abf31f3d; COO half condition 2; CTO half conditions 4 and 8; rows D2-S166, D2-S167)

<to_id>IRPT_BCKEND.TO-IB-pr-533</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~380</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>192</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-192 analysis (item 1: the releasing seat "re-measures the per-firm movers, the lost-account count and the gate outcomes against the packet (the stop rule)" and "states each firm's business date for the first fire") | **Decomp cell:** `IB-pr-533` (decomposition section 184) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-380` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~380 <0.9.0_WK_IRPT_BCKEND~380@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, object names and PUBLIC security symbols only in any tracked file; **no account id, client id, position value, quantity or holding name**; candidates and scratch live OUTSIDE the worktree (`C:/dev/_scratch380/`) and are deleted at the end with a short bounded script.

**Cell `IB-pr-533` (inlined).** The signed packet for ONE holdings-producer release (`deliverables/0.9.0_WK_IRPT_BCKEND~379/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532.md`, sha256 `4129abf31f3d402d72de9778c0cc32d7114fd414105cc24ac169893696e28504`; read it and `IB191-1_release_counts.json` beside it first) says the release STOPS unless, at the release, the per-firm canonical and fallback movers, the lost-account count and the gate outcome and conditions equal the packet. The worker that measured those numbers (IB-pr-532) ran a scratch harness that was deleted, and its candidates were not pinned, so a re-measure on a LATER candidate (the 2026-10-13 sources land overnight) would differ for reasons that have nothing to do with the code. **This order commits the harness and proves the comparison is deterministic: the harness takes a firm's source date as an input and replays the build on exactly that date, twice, and the two runs must agree.** The releasing seat will run this committed harness at the release (a later order), and separately reads each firm's newest candidate date for the CTO's business-date condition.

**The harness (`deliverables/0.9.0_WK_IRPT_BCKEND~380/release_count_harness.py`, committed):**
1. Usage: `python release_count_harness.py <repo_root> --as-of <YYYY-MM-DD>[,<firm>=<YYYY-MM-DD>...] --firms <all|firm,...> --out <json path outside the repo> [--date-check <fire date>]`. It puts `<repo_root>/data/assets/scripts/gold/investor_reporting` on `sys.path` and imports `holdings_snapshot` and `source_inputs`; it uses boto3 with the caller's own identity for READ calls only.
2. For each firm it replays `holdings_snapshot.build_snapshot(firm, inputs, as_of)` where `inputs` is a `VersionedInputs` over the read client and `as_of` is the pinned source date (never `select_business_date()`), TWICE over the same inputs: once as the code stands and once with `holdings_snapshot.apply_cash_rule` replaced by an identity function (a monkeypatch inside the harness only). A mover is a SECURITY node whose `asset_class` differs between the two builds, matched by `node_id`; the layer of a mover is read by re-running the producer's `classify_security` on its display symbol, description and security id, as IB-pr-532 did (the node carries no per-node layer).
3. For each firm it then reads the served publication as `run_firm` does (`HoldingsPublication(read_client, firm).begin()` and `served_publication`; `begin()` only reads) and evaluates `evaluate_publish_gate` on the with-rule candidate TWICE: **before** with the pre-repair marks rule (every landed-directory entry's `termination.indicator`, a missing one counting UNKNOWN, all UNKNOWN and the directory non-empty; write it in the harness) and **after** with `holdings_snapshot.directory_marks_no_closures(...)` and the producer's own `closed_account_ids(...)`.
4. It writes a JSON with per firm: the pinned `as_of`, `movers_canonical`, `movers_fallback`, the DISTINCT public ticker-shaped canonical movers, `gate_before`, `gate_after`, `conditions_before`, `conditions_after`, `lost_accounts_listed_after` (a COUNT, never an id), and `receipts_digest` = sha256 over the canonical JSON of `inputs.receipts()` (the source objects and versions the build read). With `--date-check <fire date>` it also prints, per firm, the NEWEST candidate's `clocks.business_date` (built with `as_of` = `select_business_date()` of that fire date, no replay) beside `lib/trading_calendar.prev_trading_day(<fire date>)`.
5. **Read-only by construction:** no `put_`, `copy_`, `delete_`, upload, `send_command`, invoke, `publish_client`, `land` or `run_firm` call anywhere in the file (the check reads the text for them). 49financial is the largest book (about 156,000 SECURITY nodes, minutes per build): if a firm's build cannot finish in 25 minutes, stop it and record why.

**Do, in this order (every number is a MEASUREMENT with its source named in `notes`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it). Read `IB191-1_release_counts.json`, the packet, `holdings_snapshot.py` `run_firm`, `build_snapshot`, `evaluate_publish_gate`, `served_publication`, `directory_marks_no_closures`, `classify_security`, and `source_inputs.py`.
2. Write the harness, run it as RUN A for each firm on that firm's source date `2026-10-12` (the date the packet's candidates carried; if a firm's newest source partition is earlier or later, use `2026-10-12` anyway: the pin is an input), and immediately as RUN B with the same arguments. If you can pre-seed `VersionedInputs._refs` from RUN A's receipts so RUN B reads exactly RUN A's object versions, do so and say so; if not, RUN B pins only the date and `notes` says so.
3. Compare each firm's RUN A with the signed packet's numbers: 49financial 32 canonical + 0 fallback, gate PUBLISHED before and after, 0 listed; Cottonwood 38 + 211, REFUSED before (`account_lost`), PUBLISHED after, 1 listed; Inflection 774 + 67, PUBLISHED before and after, 0 listed. Record `matches_packet` and name every differing field in `deviations_from_packet` (`canonical`, `fallback`, `gate_before`, `gate_after`, `listed`). A deviation is a MEASUREMENT, not a failure: record it and explain in `notes`.
4. Run the harness with `--date-check 2026-10-14` and record `first_fire_check` = `{"fire_date":"2026-10-14","t_minus_1":"<calendar prev_trading_day>","newest_candidate_dates":{"49financial":"..","cottonwood":"..","inflection":".."},"all_equal_to_t_minus_1":bool}` as measured now (the check recomputes `t_minus_1`).
5. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~380/IB192-1_replay_record.json`: `{"base_commit":"<40hex>","harness":"release_count_harness.py","firms":{"49financial":{"pinned_source_date":"2026-10-12","run_a":{"movers_canonical","movers_fallback","canonical_tickers","gate_before","gate_after","conditions_before","conditions_after","lost_accounts_listed_after"},"run_b":{same},"receipts_digest":"<64hex>","matches_packet":bool,"deviations_from_packet":[..],"note":".."},"cottonwood":{...},"inflection":{...}},"first_fire_check":{...},"notes":["what each fact rests on and what was not read"],"uploaded":false,"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
6. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB192-1_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the harness, the record and the criteria output FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR harness or record (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB192-1-AC1" cell_refs="IB-pr-533"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py" . IB192-1-AC1</invocation><expect>IB192-1-AC1 PASS</expect></criterion>
<criterion id="IB192-1-AC2" cell_refs="IB-pr-533"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py" . IB192-1-AC2</invocation><expect>IB192-1-AC2 PASS</expect></criterion>
<criterion id="IB192-1-AC3" cell_refs="IB-pr-533"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py" . IB192-1-AC3</invocation><expect>IB192-1-AC3 PASS</expect></criterion>

<expected_criteria>IB192-1-AC1, IB192-1-AC2, IB192-1-AC3</expected_criteria>

What the checks grade: AC1 the harness file exists, compiles, contains none of the write, publish or invoke calls named above, and uses `build_snapshot`, `apply_cash_rule`, `evaluate_publish_gate`, `directory_marks_no_closures`, `VersionedInputs` and `as_of`; AC2 per firm the two runs agree EXACTLY (movers by layer, gate outcomes and conditions, lost accounts listed), a 64-hex `receipts_digest`, `matches_packet` and `deviations_from_packet` consistent with the signed packet's numbers, and the `first_fire_check` recomputed (t_minus_1 against the trading calendar, the equality flag against the three dates); AC3 a note per firm, no long digit run, `uploaded` false and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. READ ONLY. **Nothing is invoked, written, uploaded, applied, deployed or sent:** no Lambda invoke, no SSM `send-command`, no S3 put/copy/delete, no terraform, no sign-in, no vendor call; the harness makes only get/list/head/scan calls with your own identity. A denial is recorded, never worked around or widened.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a value, name or identifier of a client or account in a tracked file; a figure you cannot source (say so; do not estimate); two runs that disagree after you have ruled out a harness defect (a nondeterministic build is a finding to report, not to hide). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W380-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~380/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 184 (round 192, workstream ~P), cell `IB-pr-533`.
<owned_cells>IB-pr-533</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB192-1-AC1, IB192-1-AC2, IB192-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~380/IRPT_BCKEND.TO-IB-pr-533.release-count-harness-and-pinned-replay.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order builds each firm's candidate in memory from versioned source reads (twice per firm, pinned to a source date), reads each firm's served publication and directory; it writes and invokes nothing, and commits only a read-only Python file and records; the release and its re-measure are the next round's order.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity (IB-pr-526, -528 and -532 read the same sources).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p192_cells.py IB192-1 dry-run at base on dell2 2026-10-14 ~06:1xZ: AC1, AC2, AC3 FAIL (no harness, no record). Positive control in a temp root the run created itself (a synthetic harness, record and a copy of lib/trading_calendar.py; removed): all three PASS, and a record naming a real deviation passes; negatives, each failing its own arm: a put_object call, run_firm used, no gate, a syntax error, no VersionedInputs, runs that disagree, an unnamed deviation, matches_packet false with no deviation, no digest, a wrong t_minus_1, a wrong equality flag, a write counter above 0, uploaded true, a long digit run, a missing note.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~380` (worktree `C:/dev/wk-IRPT_BCKEND-380`). Class SERVED (builds candidates from served sources and reads served publications; writes only the worker's records). The premises are the signed packet and its record, the merged builds, and my read of the producer's date rule (row D2-S167).
</preflight>
