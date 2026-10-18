# NFRA_OPLGTW task order -- `OG-pr-2` -- the probe listener's second repair: the audit write leaves the shared event loop, and a refused call reads the request body first so it answers cleanly (round 42; the issuer's review of `OG-pr-1`, rows `Z-W147-S1` and the reset seen in `test_ogpr1_ac02`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pr-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~148</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the issuer's own repair of a cell the CTO ruled (decision msg 35584, option A).
EGRESS CLASS, declared: NONE (the listener binds the loopback interface only).
</preflight>

## 1. THE CELL -- `OG-pr-2` (decomposition addendum R3-T.119 amendment A4, round 42, workstream ENRICH-R42-B, a recut of one repair cell inside round 42)

INHERITED STATE (in your tree, merged, passing; do NOT rebuild or restructure it): `infra/aws/ec2/opal-gateway/app/probe_listener.py` is the loopback probe listener of order `OG-pr-1`: a second uvicorn server inside the gateway process bound to `127.0.0.1:8099`, off by default, armed by an SSM lease (`/opal-gateway/probe/lease`, 60 minutes or less), serving exactly `etfs_compare_peers` and `client_get_transactions` for one fixed principal and the lease's one account, writing an audit record labelled `probe:<order>`. It was built by worker `~146` (merged `dde85bf0ae`) and its lease read was repaired by worker `~147` (merged `83d6309811`: async `current_lease`, one lazily created SSM client with short timeouts, a failed read cached as unarmed for 5 s, a single-flight lock). `tests/test_og_pr1.py` holds `test_ogpr1_ac01` to `test_ogpr1_ac06`, all passing. Read both files in full first.

TWO DEFECTS remain, both in `probe_listener.py` (you write only `app/probe_listener.py` and `tests/test_og_pr1.py`; `app/audit.py` and `app/server.py` are read-only for you):

DEFECT 1 -- THE AUDIT WRITE IS INLINE ON THE SHARED LOOP. The listener shares the gateway's event loop (that is its point). `_audit` calls `audit.log_call`, which appends the JSONL floor and, when `AUDIT_S3_BUCKET` is set, calls boto3 `put_object` with default timeouts. `probe_call` calls `_audit` (through `_refuse`, and on the ok and error paths) directly on the event loop, so a slow or unreachable S3 would stall every request on the gateway, `/health` included, exactly as the lease read did before its repair. REPAIR: every audit write in `probe_call` runs through `run_in_threadpool` (`_refuse` becomes `async` and awaits `run_in_threadpool(_audit, ...)`; the ok and error paths await it too). Do NOT change `audit.py` (the same inline pattern elsewhere in the gateway is the issuer's note, not this cell).

DEFECT 2 -- A REFUSED CALL CAN RESET THE CONNECTION. `test_ogpr1_ac02` failed once in three runs on the issuer's machine with `ConnectionResetError: [WinError 10054]`: `probe_call` answers a refusal (403 `probe_not_armed`, 404 `probe_tool_refused`, 403 `probe_account_refused`) BEFORE it reads the request body, and a server that replies and closes with an unread body can reset the client's connection before the client reads the answer. A probe whose refusal cannot be read makes the Phase B evidence ("another tool and another account are refused") flaky. REPAIR: read the request body FIRST in `probe_call`, bounded: `body_bytes = await request.body()`; if it is longer than 65536 bytes answer 413 `probe_body_too_large` (audited, no parsing); then parse the JSON from those bytes (not by calling `request.json()` a second time). The order of refusals after that is unchanged: not armed, then tool, then body shape, then account.

NEW TESTS in `tests/test_og_pr1.py` (keep `test_ogpr1_ac01` to `test_ogpr1_ac06` passing, unchanged in meaning; read them for the fixtures: the fake clock, the fake lease reader, the real loopback server on an ephemeral port):
- `test_ogpr1_ac07` REFUSALS ANSWER CLEANLY: against the real loopback server, 40 consecutive refused calls, each WITH a JSON body of about 2 KB (10 unarmed, 10 a third tool name, 10 a wrong account, 10 with a body over 65536 bytes), each returns its HTTP status and error code and none raises a connection error; run the whole loop twice.
- `test_ogpr1_ac08` THE AUDIT WRITE IS OFF THE LOOP: with the module's audit writer replaced by a fake that sleeps 1.0 s (`time.sleep`) while a concurrent trivial coroutine ticks on the same loop, the ticker advances at least 8 times during a served call and during a refused call, and one audit record (label `probe:<order>` or `probe:unarmed`) is still written per call.

Mutant controls to run and report (restore the files byte-equal afterwards): the old inline `_audit` makes `ac08` fail; answering a refusal before reading the body makes `ac07` fail (if it does not on your machine, say so; the connection reset is timing-dependent).

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no Terraform, no change to `server.py`, `audit.py`, `tools.py`, the adapters or any other app file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret, an account number or a client value (`****<last4>` forms only).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/probe_listener.py
infra/aws/ec2/opal-gateway/tests/test_og_pr1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/probe_listener.py` and `tests/test_og_pr1.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~148/`. Rows: id `NFRA_OPLGTW-Z-W148-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_pr1.py test_ogpr1_ac01 test_ogpr1_ac02 test_ogpr1_ac03 test_ogpr1_ac04 test_ogpr1_ac05 test_ogpr1_ac06 test_ogpr1_ac07 test_ogpr1_ac08; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 8 of 8; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~148 '^infra/aws/ec2/opal-gateway/(app/probe_listener\.py|tests/test_og_pr1\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~148: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh pr2set tests/test_og_pr1.py tests/test_og_en21.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_en9.py; echo "exit=$?"</invocation><expect>(?s)pr2set forward: passed (\d+); failed 0.*pr2set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the eight named tests pass (the six inherited and the two new: refusals answer cleanly; the audit write is off the loop). `AC2`: your commits touch only the module and its test file. `AC3`: the new tests and four existing gateway test files pass together in both orders with the same count. Run `AC1` and `AC3` THREE times each and report the three results (the reset is timing-dependent; a flaky pass is not a pass).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pr-2.round-42-probe-listener-audit-off-loop-and-clean-refusals.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines and the three-run results, the mutant controls).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-B (a second issuance in round 42: the gate allows one issuance per workstream; decomposition addendum R3-T.119, amendment A4). `OG-pr-1` is SUPERSEDED by this cell for its closure: the status gate graded `OG-pr-1`'s old proof instances (`~146`'s and `~147`'s, which sit in each worker's own deliverables lane and which the COO may not move) against the amended criteria and refused the flip (row `Z-W147-S2`). A fresh order gives a fresh instance name. The release `OG-ap-40` takes the same three files byte-equal from trunk (`app/probe_listener.py`, `app/server.py`, `tests/test_og_pr1.py`); its dependency now reads `OG-pr-2` complete.
- Review that produced this cell: the issuer read the merged module and found (1) the lease read blocking the loop (repaired by `~147`), (2) the audit write blocking the loop (worker row `Z-W147-S1`), (3) a refusal answered before the body is read (a flaky `ConnectionResetError` on the issuer's machine, 1 of 3 forward runs of the both-orders set). Items 2 and 3 are this cell.
- Pre-cut: `AC1` base FAIL as expected (`ac07` and `ac08` are absent); `AC3` passes at the base.

<status>complete</status>
<round>42</round>
<workstream>ENRICH-R42-B</workstream>
<slot>~148</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
