# NFRA_OPLGTW task order -- `OG-pr-3` -- the probe listener reads a request body with a BOUND on the read itself, not only on the answer (round 42; worker row `Z-W148-S1` of `OG-pr-2`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pr-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~149</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the issuer's own repair of a cell the CTO ruled (decision msg 35584, option A).
EGRESS CLASS, declared: NONE (the listener binds the loopback interface only).
</preflight>

## 1. THE CELL -- `OG-pr-3` (decomposition addendum R3-T.119 amendment A5, round 42, workstream ENRICH-R42-C)

INHERITED STATE (in your tree, merged, passing; do NOT rebuild or restructure it): `infra/aws/ec2/opal-gateway/app/probe_listener.py` is the loopback probe listener (orders `OG-pr-1` and `OG-pr-2`): a second uvicorn server inside the gateway process bound to `127.0.0.1:8099`, off by default, armed by an SSM lease, serving two tools for one fixed principal, with its lease read and its audit write off the event loop and, since `OG-pr-2`, a handler `probe_call` that reads the request body FIRST (so a refusal is never answered over an unread body) and refuses a body over 65536 bytes with 413 `probe_body_too_large`. `tests/test_og_pr1.py` holds `test_ogpr1_ac01` to `test_ogpr1_ac08`, all passing. Read both files in full first.

THE DEFECT (the second worker's row `Z-W148-S1`): the body-first read is `body_bytes = await request.body()`, which BUFFERS THE WHOLE REQUEST BODY into memory and only then compares its length with 65536. The check bounds the answer, not the read. The listener shares the gateway's heap (that is its point) and runs even when unarmed, so any process on the host can make the gateway buffer a body of any size, exactly the runaway-memory class that took the host down on 2026-10-17 (`Z-S375`). The service unit has a memory ceiling now, which turns an overrun into a kill and restart, but the listener must not be a way to reach it.

THE REPAIR (in `app/probe_listener.py`; you write only that file and `tests/test_og_pr1.py`; `server.py`, `audit.py` and every other file are read-only for you):
1. Read the `Content-Length` header first. If it parses to an integer over 65536, answer 413 `probe_body_too_large` (audited like every refusal) WITHOUT reading any of the body.
2. Otherwise read the body by streaming: `async for chunk in request.stream():`, adding to a bytearray and the running byte count, and STOP READING as soon as the count passes 65536: answer 413 `probe_body_too_large` at that point (a request with no `Content-Length`, as in chunked transfer, is bounded by the same count; it is acceptable that the connection is then closed over the unread rest, because only an abusive client sends an oversized body).
3. The rest of `probe_call` is unchanged: the body is read before any other refusal so ordinary refusals (not armed, tool, account) still answer cleanly; the order of refusals after the body read stays; the 413 still comes first, ahead of the not-armed 403 (a stated, accepted order: the oversized body is refused before the lease is consulted).

NEW TESTS in `tests/test_og_pr1.py` (keep `test_ogpr1_ac01` to `test_ogpr1_ac08` passing, unchanged in meaning):
- `test_ogpr1_ac09` THE READ IS BOUNDED: call `probe_app` through an ASGI-level harness (for example `httpx.ASGITransport`, or a hand-written ASGI call) with a streamed request body made of 50 chunks of 16384 bytes (800 KB) produced by a generator that COUNTS how many chunks the server pulled; assert the answer is 413 `probe_body_too_large` and the generator was pulled at most 6 times (65536 / 16384 = 4, plus one over the line, plus one of slack); then repeat with a request that declares `Content-Length: 5000000` and sends a small body: 413, and the server pulled at most 1 chunk.
- `test_ogpr1_ac10` A BODY AT THE LIMIT IS STILL SERVED: a valid lease and a JSON body of exactly 65536 bytes (pad a harmless string field) is NOT refused for size (it reaches the tool or the normal body-shape refusal), and a body of 65537 bytes is refused 413; both through the same harness.

Mutant control to run and report (restore the file byte-equal afterwards): replacing the streamed read with `await request.body()` makes `ac09` fail.

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

You WRITE `app/probe_listener.py` and `tests/test_og_pr1.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~149/`. Rows: id `NFRA_OPLGTW-Z-W149-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_pr1.py test_ogpr1_ac01 test_ogpr1_ac02 test_ogpr1_ac03 test_ogpr1_ac04 test_ogpr1_ac05 test_ogpr1_ac06 test_ogpr1_ac07 test_ogpr1_ac08 test_ogpr1_ac09 test_ogpr1_ac10; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 10 of 10; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~149 '^infra/aws/ec2/opal-gateway/(app/probe_listener\.py|tests/test_og_pr1\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~149: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh pr3set tests/test_og_pr1.py tests/test_og_en21.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_en9.py; echo "exit=$?"</invocation><expect>(?s)pr3set forward: passed (\d+); failed 0.*pr3set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the ten named tests pass (the eight inherited and the two new: the read is bounded; a body at the limit is still served and one byte over is refused). `AC2`: your commits touch only the module and its test file. `AC3`: the new tests and four existing gateway test files pass together in both orders with the same count. Run `AC1` and `AC3` THREE times each and report the three results.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pr-3.round-42-probe-listener-bounded-body-read.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines and the three-run results, the mutant control).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-C (a third issuance in round 42: the gate allows one issuance per workstream; decomposition addendum R3-T.119 amendment A5). The third repair of the probe listener, from the second repair worker's own row (`Z-W148-S1`): the fix for the connection reset (read the body first) introduced an unbounded read, a find that only a reader asking "what does this do with a hostile caller" makes. `OG-ap-40` waits on this cell (spawn only after `OG-pr-2` has drained to trunk).
- `Z-W148-S3` (the refusal-before-body mutant did not fail `ac07` on the worker's machine in 3 of 3 runs, so `ac07` proves clean answers, not the reset itself) is carried to the ask: the reset was seen once on the issuer's machine and the body-first read is the protocol-correct fix, but the test does not discriminate it. `Z-W148-S2` (413 ahead of 403) is the accepted order above.
- Pre-cut: `AC1` base FAIL as expected (`ac09` and `ac10` are absent); `AC3` passes at the base.

<status>complete</status>
<round>42</round>
<workstream>ENRICH-R42-C</workstream>
<slot>~149</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
