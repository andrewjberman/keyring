# TO IRPT_BCKEND.TO-IB-pn-5 -- The Scope account feed writes the raw Orion replies ONCE per run, not into every day's bronze envelope (CTO ruling @2f780e14a6, option B)

<to_id>IRPT_BCKEND.TO-IB-pn-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~490</issued_to>
<issued_by>2.0.0_SA_COO~N2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` ruling `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/RULING_IB_PN5_BRONZE_ENVELOPE_FIX_WRITER_FIRST_20261019.md` (@2f780e14a6) | **Decomp cell:** `IB-pn-5` (`IRPT_BCKEND_DECOMP_R6_N.md`) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-490`, cut from the current branch by the issuer (sparse: `data/inf/manual_api/`, `data/inf/scripts/gold/`, `data/inf/scripts/silver/`, `data/inf/scripts/bronze/`, `lib/`, `.tools/` and the project folder are present; if a test import fails for a missing directory, run `git sparse-checkout add <that directory>` locally and never commit it). Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~490 <0.9.0_WK_IRPT_BCKEND~490@opal.agent>" -F <msgfile> -- <explicit paths>` (message file written by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit (the runner runs Python 3.9, so no `X | Y` type unions and no `match`). No typed bucket name, `s3://` address or key prefix in a product file: every S3 address comes from `lib/opal_naming.address()` (CLAUDE.md rule 30) or, on the runner where `lib/` is absent, from the sidecar exactly as `feed_addresses()` does.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array. Row ids are `IRPT_BCKEND-D2-W490-S<k>` (start at 1); `surfaced_at` = `date -u +%FT%TZ` at filing.

**Cell `IB-pn-5` (inlined).** `data/inf/manual_api/pull_inflection_scope_account_returns.py` is the Scope account feed. It makes one Orion call per household over the whole window `window_start..pull_date` and keeps each reply whole (`record["response"] = reply.body`). Then, for EACH complete day, it builds that day's bronze envelope with a `"responses"` member holding EVERY household's raw reply for the WHOLE window, gzips it and writes it as that day's bronze object. For the scheduled one-day run that is small; for a history backfill of N days it writes N copies of the full reply set (bytes grow with N squared) and repeats the serialize-and-compress N times. The CTO has ruled the fix: **the raw replies are written ONCE per run, unchanged and not sliced; each day's envelope keeps its metadata and names that one object by key and sha256; silver does not change.**

The script holds three nested blocks, `SCOPE-FEED-A` (begins line 17), `SCOPE-FEED-B` (592) and `SCOPE-FEED-C` (787), each redefining `run`; the one in block C (lines 798-889) is the live one. The envelope with `"responses"` is built in all three (lines 555, 771, 871). **No code path may embed replies in a day's envelope after your change**: put the new helper functions in block A (so B and C can call them) and make all three `run` definitions use them.

**The change (the pinned shapes; the check reads these exact names):**
1. `run_object_address(pull_date, window_start, digest)` returns the `s3://` address of the run object: with `lib/opal_naming` importable, `builder.address(SOURCE, SCOPE, "bronze", TABLE, "run=%s" % pull_date, "%s_%s.json.gz" % (window_start, digest[:12]))`; otherwise (the runner) the same partition and object name under the sidecar's bronze prefix, built the way `feed_addresses()` builds its fallback. A builder `ValueError` is a `_Refused` with the message, as in `feed_addresses()`. The partition is `run=<pull_date>` (never `date=`).
2. The run object is gzip JSON: `{"schema": "orion-scope-raw-replies-v1", "source": SOURCE, "scope": SCOPE, "table": TABLE, "pull_date": <str>, "window": {"start": <str>, "end": <str>}, "responses": [{"household_token": <token>, "body": <the reply exactly as received>}, ...]}`, serialized with `sort_keys=True` and compressed with `gzip.compress(data, mtime=0)` so equal replies give equal bytes. `digest` is the sha256 hex of the stored (gzip) bytes. The object name is therefore content-addressed.
3. Write order and rules: build and write the run object ONCE, FIRST, only when at least one day is complete (a run with no complete day writes NOTHING, as today); read it ABSENT first and SKIP an existing key, never overwrite (the existing `write_day` rule and its `exists`/`put_bytes` ports); if writing the run object raises, no day is written. Then the days, as today.
4. Each day's bronze envelope: `"schema": "orion-scope-account-returns-bronze-v2"`; every other metadata member stays exactly as today (`source`, `scope`, `table`, `day`, `pull_date`, `window`, `fee_basis`, `calc_gross_of_fees`, `calls`, `households_failed`, `universe_rows`, `households_without_id`); the `responses` member is REMOVED; a new member `"raw_object": {"key": <the run object's address>, "sha256": <digest>}`.
5. Silver is untouched: for the same inputs the silver bytes of every day equal what the current writer produces (the check holds the pre-change sha256 values). Do not change `_day_rows`, `_silver_frame` or any silver column.
6. Memory: the run still holds the parsed replies once (as today) and builds the run object once; it must not serialize the reply set once per day.

**READ FIRST (named files only):** the feed script (whole), the five test files in `data/inf/manual_api/` (`test_pull_inflection_scope_account_returns.py`, `test_scope_feed_daily_factor.py`, `test_scope_feed_day_complete.py`, `test_scope_feed_region.py`, `test_scope_feed_runner_layout.py`; how the fake transport and fake S3 are built), `lib/opal_naming.py` (`address()`, lines 2517-2530), and the check `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r6/pn5_cells.py` (read it; do not edit it). **The check imports the helpers `_fixture_s3`, `_run`, `_point`, `_group`, `_response` from `test_scope_feed_day_complete.py`: do not rename, remove or change those helpers.**

**Write the tests** `data/inf/manual_api/test_scope_feed_run_object.py` (at least 3 tests; no network; synthetic values; reuse the existing fakes by importing them from `test_scope_feed_day_complete`):
1. A 3-day window (`from_date` 2026-10-12, pull date 2026-10-14): exactly ONE object is written outside the three days' keys; it is not under a `date=` partition; its stored bytes hash to the sha256 each day's envelope carries; each envelope has the v2 schema, no `responses` member, and the metadata members above.
2. The run object holds every household's reply unchanged (equal to the fixture reply), and a re-run with the same fixture replies writes nothing new (same key, SKIP).
3. A run with no complete day writes no run object; and `run_object_address` falls back to the sidecar when the builder is hidden (point `SIDECAR_PATH` at a temp sidecar and make `_builder()` return None), giving an address under the sidecar's bronze prefix with the same partition and object name.

**Existing tests:** you MAY edit an existing assertion ONLY where it counts or enumerates S3 puts and must now include the one run object (for example `len(s3.puts) == 2` becomes 3, or the exact put-set comparison in `test_from_date_window_writes_only_complete_days`); never delete or weaken a test; list every edit in the record. No test asserts the `responses` member today (read).

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~490/IBN5-1_record.json`: `{"base_commit":"<40hex, git rev-parse HEAD at your start>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"tests_total":<n>,"tests_passed":<n>,"existing_assertions_edited":[{"file":"<path>","test":"<name>","why":"<one line>"}],"peak_memory_bytes_3day_fixture":<int, from tracemalloc around the 3-day run>,"script_sha256":"<64 hex of the script as committed>","notes":["what each fact rests on and what you did not read; the sparse directories you added"],"aws_writes_made":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~490/IBN5-1_criteria_output.txt`, write the proof instance named under proof_of_spec (it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R6_N.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`) and validate it with `python .tools/proof-of-spec-check.py <instance>`. Commit with explicit paths (script, tests, record and criteria output first; then set the instance's artifact rows to that commit and commit the instance alone in a second commit, flipping the order `complete` only when every criterion passes). Report once, in your final message: the commit ids, the three outputs (AC2 prints `PEAK_MEMORY_BYTES=`), the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IBN5-1-AC1" cell_refs="IB-pn-5"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r6/pn5_cells.py" . IBN5-AC1</invocation><expect>IBN5-AC1 PASS</expect></criterion>
<criterion id="IBN5-1-AC2" cell_refs="IB-pn-5"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r6/pn5_cells.py" . IBN5-AC2</invocation><expect>IBN5-AC2 PASS</expect></criterion>
<criterion id="IBN5-1-AC3" cell_refs="IB-pn-5"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r6/pn5_cells.py" . IBN5-AC3</invocation><expect>IBN5-AC3 PASS</expect></criterion>

<expected_criteria>IBN5-1-AC1, IBN5-1-AC2, IBN5-1-AC3</expected_criteria>

What the checks grade: AC1 on a 3-day fixture exactly one raw object outside the date= keys, each day's envelope v2 with no `responses`, its metadata kept, and a `raw_object` key and sha256 that name that object, whose body equals the fixture replies; AC2 (a difference control, PASS at the base) the silver bytes of a 1-day run and of each day of the 3-day run hash to the pre-change writer's values, and the 3-day peak memory is printed; AC3 `run_object_address` returns builder output under the bronze table home carrying the digest, the script holds no `s3://` or `orion/inflection` literal, the new test file has at least 3 tests, and the tests of `data/inf/manual_api` pass. AC1 and AC3 fail at the base; do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and a scratch directory outside the repository. LOCAL build: you write the feed script, the new test file, the assertions named above and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent; no Orion request is made.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails for a reason other than an S3-put count or put-set; a typed object address in product code; a builder refusal of the run address (the missing registry row is the issuer's to route, never a typed workaround); silver bytes that change; a real account id or security identifier in a tracked file. Never weaken a check.

<paths>
data/inf/manual_api/pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_run_object.py
data/inf/manual_api/test_pull_inflection_scope_account_returns.py
data/inf/manual_api/test_scope_feed_daily_factor.py
data/inf/manual_api/test_scope_feed_day_complete.py
data/inf/manual_api/test_scope_feed_region.py
data/inf/manual_api/test_scope_feed_runner_layout.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pn-5.scope-feed-raw-replies-once-per-run.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~490/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R6_N.md</decomp_doc> round 6, workstream ~PN, cell `IB-pn-5`.
<owned_cells>IB-pn-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBN5-1-AC1, IBN5-1-AC2, IBN5-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~490/IRPT_BCKEND.TO-IB-pn-5.scope-feed-raw-replies-once-per-run.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one repository script (the bronze envelope and one new run-level object) and adds one test file plus put-count assertions in the existing tests; nothing is deployed or run against Orion or S3, so no served byte moves. The runner's copy changes only at a later WORLD apply under ADDENDUM 5; the first one-day scheduled run after that apply writes one extra small run object under `run=<day>` in the feed's bronze table prefix.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- pn5_cells.py dry-run at base on dell2 2026-10-19 ~13:5xZ: AC1 FAIL (expected exactly ONE raw object besides the 3 days' keys, found 0), AC2 PASS (the silver sha256 values equal the pre-change writer's; peak memory 3613193 bytes on the 3-day fixture; the control), AC3 FAIL (run_object_address absent). control_pn5.py patches the script IN MEMORY to the ruled shape: AC1 and AC2 PASS; six variants (responses still embedded, schema not bumped, sha256 of the wrong bytes, a reply sliced, a second object written, silver changed) each fail only their own arm; run_object_address absent fails AC3; unexpected 0. Not exercised by the control: AC3's new-test-file count and pytest of the manual_api folder (they need the worker's tests); silver is deterministic across runs (two runs, equal sha256).
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~490` (worktree `C:/dev/wk-IRPT_BCKEND-490`). Class LOCAL.
authority: workstream ~PN is this seat's under the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1; write surface `data/inf/manual_api/` is named there; the shape is the CTO ruling above.
</preflight>
