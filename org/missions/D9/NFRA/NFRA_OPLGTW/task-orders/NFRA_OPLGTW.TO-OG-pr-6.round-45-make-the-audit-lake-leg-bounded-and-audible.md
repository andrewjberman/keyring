# NFRA_OPLGTW task order -- `OG-pr-6` -- make the audit lake leg BOUNDED and AUDIBLE: one file, `app/audit.py` (round 45; round-44 analysis item 2; row `Z-S402`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-6</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pr-6</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~161</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the change adds no AWS call (it bounds the existing S3 put). No AWS call is needed to build or test it.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-44 analysis, list item 2 (a counted, rate-bounded failure line in `_emit`, plus an explicit botocore Config; one file, by the build ladder).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-pr-6` (decomposition addendum R3-T.122, round 45, workstream ENRICH-R45-A)

WHY. `infra/aws/ec2/opal-gateway/app/audit.py` `_emit` writes each audit record to the local floor file, then ships the same record to the S3 audit lake with `_s3_client.put_object(...)` inside `try:`/`except Exception: pass`. Two defects (row `Z-S402`, cell `OG-ev-11`): (1) a failed lake put is SILENT for every audit record: nothing counts it and nothing prints a line; (2) the S3 client is built with botocore's DEFAULTS (60 s connect, 60 s read, 5 attempts) and 80 of the gateway's 81 audit-write sites run on the event loop, so one stalled put can hold the loop for minutes. Read `app/audit.py` lines 1 to 70 first.

DO, in `infra/aws/ec2/opal-gateway/app/audit.py` ONLY (plus the new test file), by the smallest change that works (native botocore setting plus a counter; NO new module, NO new dependency):
1. **A counter and an audible, rate-bounded line.** Add `import sys` and `import time` at the top with the other imports. After the `_s3_client = None` line add module state: `_lake_put_failures = 0`, `_lake_last_warn = None` (the `time.monotonic()` of the last stderr line; None before the first), `_lake_fail_lock = threading.Lock()` and `_LAKE_WARN_EVERY_S = 60.0`. Add `def lake_put_failure_count() -> int:` returning `_lake_put_failures`. Add `def _note_lake_failure(exc: Exception) -> None:` that, under `_lake_fail_lock`, adds 1 to `_lake_put_failures` and then, ONLY if `_lake_last_warn is None or time.monotonic() - _lake_last_warn >= _LAKE_WARN_EVERY_S`, sets `_lake_last_warn = time.monotonic()` and prints exactly ONE line to `sys.stderr` (`flush=True`): `SCTY_PREMCP audit-lake WARN: lake put failed (<the exception CLASS NAME only, type(exc).__name__>) count=<the running count> -- the local floor line is written`. The line never carries the exception message, the bucket, the key or any record content. `_note_lake_failure` must never raise (wrap its body in `try`/`except Exception: pass`). In `_emit`, change the last `except Exception:` branch from `pass` to call `_note_lake_failure(exc)` (write `except Exception as exc:`). The `time.monotonic()` call must be written exactly as `time.monotonic()` (the tests replace `audit.time.monotonic`).
2. **An explicit bounded botocore Config.** Where `_emit` builds the client (`boto3.client("s3", region_name=_cfg.AWS_REGION)`), import `from botocore.config import Config` inside that same lazy block and build it as `boto3.client("s3", region_name=_cfg.AWS_REGION, config=Config(connect_timeout=2, read_timeout=3, retries={"max_attempts": 1, "mode": "standard"}))`. Add a comment above it that states the justification in two or three lines: a healthy put takes well under a second; a stalled put now costs at most 2 s to connect plus 3 s to read on the event loop, where the botocore default is 60 s plus 60 s and 5 attempts; one attempt, no retry, because the lake write is a best-effort sink and the floor already holds the record (round-44 `OG-ev-11`: 80 of 81 sites on the loop, about 9,800 lake records a day).
3. **The local floor write is NOT touched.** The lines of `_emit` from `def _emit(record: dict) -> None:` through `fh.write(line + "\n")` stay byte-for-byte as they are (the check compares them to the base).
4. **The new test file `infra/aws/ec2/opal-gateway/tests/test_og_pr6.py`** with EXACTLY these three tests (names fixed): first READ `tests/test_audit_lake_key_stamp.py` and copy the way it turns on `AUDIT_S3_BUCKET` and replaces `audit._s3_client` with a stub, and the way it points `AUDIT_PATH` at a temporary file. Use a stub client whose `put_object` raises `RuntimeError("boom")`.
   - `test_failed_put_increments_counter_and_writes_one_line`: reset `audit._lake_put_failures = 0` and `audit._lake_last_warn = None`; call `audit._emit(<a small dict record with a ts>)` five times; assert `audit.lake_put_failure_count() == 5`, and that the captured stderr holds exactly ONE line containing `audit-lake WARN` and `count=1`, and does NOT contain `boom`.
   - `test_second_line_after_60s_carries_the_running_count`: monkeypatch `audit.time.monotonic` to return, in order, controlled values so that three failures happen at t=1000, t=1010 and t=1061 (reset the state first); assert two warning lines in all, the first with `count=1` and the second with `count=3`.
   - `test_floor_line_written_when_the_put_fails`: with the failing stub and a temporary `AUDIT_PATH`, one `_emit` leaves exactly one line in the floor file and `lake_put_failure_count() == 1`.
   Restore every patched module value after each test (use `monkeypatch`).

## 2. BOUNDS

- Write only `infra/aws/ec2/opal-gateway/app/audit.py`, `infra/aws/ec2/opal-gateway/tests/test_og_pr6.py`, `W/` and, if a row is needed, the channel. NO other product file, no other test, no release, no deploy, no Terraform, no AWS call. No new module and no new dependency.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/tests/test_og_pr6.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~161/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W161-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/pr6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)the three named tests: passed 3 of 3; failed 0; pytest rc=0.*floor lines of _emit equal to the base blob: yes \(\d+ lines\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/pr6.AC2.sh; echo "exit=$?"</invocation><expect>(?s)boto3\.client call with an explicit botocore Config: yes; Config imported from botocore: yes; connect_timeout [0-9.]+ \(want a number in \(0, 5\]\); read_timeout [0-9.]+ \(want a number in \(0, 10\]\); retries max_attempts [12] \(want 1 or 2\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/pr6.AC3.sh; echo "exit=$?"</invocation><expect>(?s)pr6set forward: passed (\d+); failed 0.*pr6set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a failed lake put is counted and writes ONE rate-bounded line (and a second only after 60 s, with the running count), the floor line is still written, and the floor-write lines of `_emit` equal the base. `AC2`: the audit S3 client is built with an explicit `Config` of bounded connect and read timeouts and a retry cap. `AC3`: the existing audit tests (`test_audit_bytes_principal.py`, `test_audit_lake_key_stamp.py`, `test_audit_rivalfunds_args.py`, `test_og_en10.py`) and your new file pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pr-6.round-45-make-the-audit-lake-leg-bounded-and-audible.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: only `python3 -I` sees `jsonschema` on this box, ruling msg 35901), flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines, the three Config values you set, the exact stderr line your failure path prints).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 45, workstream ENRICH-R45-A. Source: the CTO's round-44 analysis (`ledger/ROUND_ANALYSIS.round44.md` @ebefeda213, msg 35898), item 2: "ONE file, `app/audit.py`, by the build ladder: a native botocore setting plus a counter, no new module. Criterion 1: a failed `put_object` increments a module counter and writes ONE stderr line, rate-bounded to the first failure and then at most one line per 60 s with the running count. The floor write is unchanged. Criterion 2: the audit S3 client is built with an explicit `botocore.config.Config`, with bounded `connect_timeout` and `read_timeout` and a retry cap. Values set in the cell and justified from OG-ev-11's table. Criterion 3: the existing audit tests pass, plus a test that a raising client increments the counter and emits one line, not one per failure. The ask must name the process-wide state it touches: stderr volume, bounded."
- READINGS DISCLOSED TO THE CTO: (1) the new tests live in a NEW file `tests/test_og_pr6.py` (the analysis says "one file" for the product change; a test needs a home, and the release takes the two files). (2) the Config values, `connect_timeout` 2, `read_timeout` 3, one attempt, are the issuer's, justified in the order from `OG-ev-11` (a healthy put is far under a second; the worst case on the loop falls from minutes to 5 s); the check accepts connect up to 5 s, read up to 10 s and at most 2 attempts so a worker's reasoned variation inside that is not refused. (3) the stderr line carries the exception class name only, never its message (it can carry a bucket or key).
- Base blob of `app/audit.py` at the issuance: `b40d48c1be77731dac4a0a45fb359bb1eee5b0c0`. Pre-cut: `AC1` base FAIL as expected (no test file; 0 of 3 pass); `AC2` base FAIL as expected (no Config); `AC3` base FAIL as expected (the new file is absent). Arms fed to the checks: a file with a good Config passes `AC2`, `read_timeout=60`, 5 attempts and no Config each fail it; a changed floor line fails `AC1(b)`, the real file's floor lines equal the base.
- Risk `WORLD` is the gateway-path floor.

<status>pending</status>
<status>complete</status>
<round>45</round>
<workstream>ENRICH-R45-A</workstream>
<slot>~161</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
