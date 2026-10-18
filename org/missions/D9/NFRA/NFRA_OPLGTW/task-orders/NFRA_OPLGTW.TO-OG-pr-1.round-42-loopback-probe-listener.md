# NFRA_OPLGTW task order -- `OG-pr-1` -- the loopback probe listener: a separate 127.0.0.1 listener on the running gateway, off by default, armed by an SSM lease of 60 minutes or less, serving exactly two tools for a fixed probe principal (round 42; CTO decision msg 35584, option A with the heap read as its instrument)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pr-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~147</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- this order changes NO IAM. If the gateway's instance role cannot read the lease parameter (`ssm:GetParameter`), that is a BLOCKING row for the issuer, never an IAM edit by you.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision 35584 (option A: a loopback-only listener; options B, C and D refused).
EGRESS CLASS, declared: NONE (the listener binds the loopback interface only).
</preflight>

## 0. AMENDMENT A1 -- A REPAIR, AND YOU ARE THE SECOND WORKER OF THIS CELL (read this BEFORE section 1)

The first worker (`0.9.0_WK_NFRA_OPLGTW~146`) built the listener as section 1 below describes; its three commits (`8d76ae9045`, `761e6f96f5`, `1833ad09dd`) are merged into your branch and are INHERITED STATE: `app/probe_listener.py`, the hookup in `app/server.py` and `tests/test_og_pr1.py` already exist and pass their four tests. Do NOT rebuild them. The issuer's review of the module found ONE defect class, in the lease read, and your whole job is to repair it (your write set is `app/probe_listener.py` and `tests/test_og_pr1.py` only; `server.py` does not change).

THE DEFECT. The listener shares the gateway's event loop and heap (that is its point). `current_lease()` is called synchronously inside the async handler `probe_call`, and `_read_lease_parameter` builds a boto3 SSM client and calls `get_parameter` with the default timeouts. If SSM is slow or unreachable, that blocking call STALLS THE WHOLE GATEWAY'S EVENT LOOP (every request, `/health` included) for the boto3 timeout, and because "a failure is never cached", a stream of local requests repeats it: an unarmed, harmless listener could take the service down. A second point: many requests arriving together at a cache expiry each read SSM.

THE REPAIR (all three, in `app/probe_listener.py`):
1. The lease read runs OFF the event loop: `current_lease` becomes `async def` (call it with `await` in `probe_call`) and the read goes through `run_in_threadpool`.
2. The SSM client uses short timeouts and no retry storm: `botocore.config.Config(connect_timeout=2, read_timeout=3, retries={"max_attempts": 1})`, and the client is created once and reused (module-level, created lazily; the test hook `LEASE_READER` still replaces the whole read).
3. A FAILED read is cached too, as "unarmed", for the same `LEASE_CACHE_SECONDS` (5 s), and the read is SINGLE-FLIGHT: an `asyncio.Lock` so that concurrent requests at an expiry make ONE read, not one each. A successful read is cached as before. Validity is still judged at the request's own `now` (a cached value never extends a lease past `expires_at`).

NEW TESTS in `tests/test_og_pr1.py` (keep `test_ogpr1_ac01` to `test_ogpr1_ac04` passing, unchanged in meaning):
- `test_ogpr1_ac05` OFF THE LOOP: a lease reader that sleeps 1.0 s (a `time.sleep` inside the fake reader) while a concurrent trivial coroutine ticks on the same loop: the ticker advances at least 8 times during the read (the loop is not blocked), and the call still answers 403 `probe_not_armed` for an absent lease.
- `test_ogpr1_ac06` FAILURE CACHED AND SINGLE-FLIGHT: with a reader that raises, 20 concurrent requests make exactly ONE reader call and all answer 403 `probe_not_armed`; a second burst inside 5 s makes ZERO more calls; after the fake clock passes 5 s one more call is made.
- (Lease expiry stays honoured under the cache: a cached valid lease is refused once the fake clock passes `expires_at`, even inside the 5-second window; add it to `ac06` or `ac01`.)

ALSO, in your report, state for the issuer (no code change): the disarm by DELETING the lease parameter takes effect within the cache window (5 s), so a check of "the next call is refused" after a delete must wait 6 s; and the instance role needs `ssm:GetParameter` on `/opal-gateway/probe/lease` (not measured).

## 1. THE CELL -- `OG-pr-1` (decomposition addendum R3-T.119, round 42, workstream ENRICH-R42-A)

YOU ARE SPAWNED ONLY AFTER `OG-sec-1` has drained and `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~145/SSRF_AUDIT.json` reads `"verdict": "CLEAN"` on your branch. If it is absent or reads STOP, STOP and file a BLOCKING row.

WHY. Two ARMED hazards cannot be disarmed because nothing can call the RUNNING gateway process on demand: `Z-S375` (`etfs_compare_peers` was repaired and measured only in fresh processes) and `Z-S338` (the service heap over a full window chain). The CTO ruled a small probe path INTO the running service, and nothing else: no new identity on the internet side, no change to the ALB or OAuth.

THE BUILD (one new module, one hookup, one test file). Read `app/server.py` (the FastAPI `app`, its `lifespan` near the line `async with mcp.session_manager.run()`, and how a tool call reaches `app/tools.py`/`app/client_core.py` with a principal), `app/identity.py` and `app/audit.py` (how a call is attributed and audited), `app/config.py` (settings), and an existing SSM or boto3 use in `app/` for the client style. Then:

1. NEW `app/probe_listener.py`. It starts a SECOND uvicorn server INSIDE THE SAME PROCESS (the same heap is the point), as a task started from `lifespan`, bound to `host="127.0.0.1"` and the module constant `PROBE_PORT = 8099` (pick another free constant port only if 8099 is used anywhere; say so in your report). It is NOT added to any ALB target group and NOT reachable from the network interface.
2. OFF BY DEFAULT, ARMED BY A LEASE. The listener does not accept a request unless a lease parameter in SSM Parameter Store is valid at that request: parameter name `/opal-gateway/probe/lease` (the module constant), value JSON `{"order": "<order id>", "account_ref": "<the Phase A test account in the ****<last4>/<vendor>/<alias> form>", "expires_at": "<UTC ISO time>", "set_at": "<UTC ISO time>"}`. Valid means: now is before `expires_at`, and `expires_at` minus `set_at` is 60 minutes or less. A missing, malformed, expired or over-long lease answers 403 `probe_not_armed` with no data. The lease is read (with a short in-process cache of at most 5 seconds) on every request, so it EXPIRES CLOSED without a restart. The parameter is created by the applier at arming time, never by this code, and holds no secret. If the instance role cannot read it, file the BLOCKING row described in the preflight.
3. WHAT IT SERVES. EXACTLY two tools, `etfs_compare_peers` and `client_get_transactions`, called through the SAME functions the MCP path calls (do not copy logic). Any other tool name answers 404 `probe_tool_refused`. `client_get_transactions` accepts only the `account_ref` the lease carries (any other account answers 403 `probe_account_refused`); the scope is "the test account and the ETF peer tables the Phase A fresh-process runs already read under the gateway role": no other data plane, no new grant. Responses are the tool's own answer JSON.
4. THE FIXED PROBE PRINCIPAL. The call runs as ONE server-held principal built in the module (not from a token, a header or a request value): a restricted profile that allows only those two tools. Read how an existing restricted principal is represented (`app/identity.py`, `app/internal_role.py`, `app/client_role.py`) and reuse that type; do not add a new identity provider and do not touch OAuth.
5. AUDIT. Every call (served or refused) writes an audit record through the existing audit path with the label `probe:<order>` taken from the lease (`probe:unarmed` when there is none).
6. THE HEAP READ. A signal handler for `SIGUSR2`, registered at startup, writes ONE line to the service log: the process id, `VmRSS` and `VmHWM` read from `/proc/self/status`, and `sys.getallocatedblocks()`. It writes no object content. (This is the "heap read of the service PID on a signal" the CTO named; the applier sends the signal over SSM before and after each probe call.)
7. HOOKUP in `app/server.py`: in `lifespan`, start the listener task and cancel it on shutdown. NOTHING ELSE in `server.py` changes (no route, no middleware, no import beyond the module). The existing 103 tools and every existing route answer exactly as before.

TESTS (new file `tests/test_og_pr1.py`; no network, no AWS: fake the SSM read and the clock with module-level hooks you expose for the test, and run the listener on an ephemeral loopback port):
- `test_ogpr1_ac01` OFF BY DEFAULT AND ARM/CALL/EXPIRE: with no lease a call answers 403 `probe_not_armed`; with a valid lease (45 minutes) a call to `etfs_compare_peers` answers its normal body; advance the fake clock past `expires_at` and the next call answers 403 `probe_not_armed` again; a lease whose `expires_at - set_at` is 61 minutes is refused.
- `test_ogpr1_ac02` SCOPE: a third tool name answers 404 `probe_tool_refused`; `client_get_transactions` for an `account_ref` other than the lease's answers 403 `probe_account_refused`; the bound address is `127.0.0.1` (assert on the server socket) and the module has no other bind.
- `test_ogpr1_ac03` AUDIT AND PRINCIPAL: each of the calls above leaves an audit record whose label is `probe:<order>` (or `probe:unarmed`), and the principal used is the module's fixed one (a header or token on the request changes nothing).
- `test_ogpr1_ac04` HEAP READ: sending `SIGUSR2` to the process (on Windows, where the signal is absent, call the handler function directly) logs one line holding `VmRSS`, `VmHWM` and an allocated-blocks count and nothing else.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no Terraform, no change to `tools.py`, the adapters, `client_core.py`, `typed_scope.py`, the unit file or the deploy script. No SSM parameter is created by code or by you.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret, an account number or a client value (use `****<last4>` forms only).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/probe_listener.py
infra/aws/ec2/opal-gateway/tests/test_og_pr1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/probe_listener.py` and `tests/test_og_pr1.py` (the repair of section 0); the rest you only READ (`server.py` is read-only for you). `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~147/`. Rows: id `NFRA_OPLGTW-Z-W147-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_pr1.py test_ogpr1_ac01 test_ogpr1_ac02 test_ogpr1_ac03 test_ogpr1_ac04 test_ogpr1_ac05 test_ogpr1_ac06; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 6 of 6; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~147 '^infra/aws/ec2/opal-gateway/(app/probe_listener\.py|tests/test_og_pr1\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~147: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh pr1set tests/test_og_pr1.py tests/test_og_en21.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_en9.py; echo "exit=$?"</invocation><expect>(?s)pr1set forward: passed (\d+); failed 0.*pr1set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the six named tests pass (off by default and arm/call/expire; scope; audit and principal; heap read; the lease read off the loop; a failed read cached and single-flight). `AC2`: your commits touch only the module and its test file. `AC3`: the new tests and four existing gateway test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pr-1.round-42-loopback-probe-listener.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines, the port, the lease parameter name, how the principal is built, and whether the instance role needs any permission it lacks).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). The CTO's cell 5 (msg 35584) built to its list: a separate loopback listener (not a route check), outside the ALB target group, off by default, an SSM lease of at most 60 minutes that expires closed, exactly two tools, a fixed server-held probe principal, the audit label `probe:<order>`, the data scope of the Phase A runs, one test of the arm/call/expiry path, and a heap read of the service PID before and after each call. The heap method the check accepts: `tracemalloc_signal`, `py_spy_dump` or `proc_status_signal` (this order's `SIGUSR2` handler is the last).
- Release: `OG-ap-40` (staged; its own never-widen; takes these three files byte-equal from trunk). Disarm: `Z-S375` on `etfs_compare_peers` through the listener with the service heap and `NRestarts` printed; `Z-S338` closes on a full window chain through it with the service heap flat.
- The lease parameter holds an `account_ref` in the `****<last4>/<vendor>/<alias>` form, so the code holds no client identifier. If `ssm:GetParameter` on `/opal-gateway/probe/*` is not in the instance role, the cell stops at a BLOCKING row and the IAM act is a separate order.
- A1 (2.0.0_SA_COO~O, round 42, ~02:5xZ): first worker `~146` drained at `dde85bf0ae` (my runs of the four tests and the both-orders set passed, proof VALID); the issuer's REVIEW of the module found the lease read blocking the shared event loop (section 0 of the worker face). Re-seated as `~147` on the merged state; the criteria now count six tests. The first worker's rows `Z-W146-S1` to `S3` (ARMED observations: the allowlist is in the module, the probe bypasses `_run`'s guard chain and enforces its own checks, the principal's Opal-domain display address exists only in code) are carried to the never-widen ask of `OG-ap-40` and to the CTO and the CVO; they are not repaired here. Gate limb: none graded this amendment (the modified order declares no placeholder change).
- Pre-cut: `AC1` base FAIL as expected (the test file is absent); `AC3` base FAIL (the file is absent).

- CLOSED AS SUPERSEDED (2.0.0_SA_COO~O, round 42, ~03:3xZ): built by `~146` (merged `dde85bf0ae`), its lease read repaired by `~147` under amendment A1 (merged `83d6309811`; the six named tests pass on my run). The issuer's review found two more defects, repaired by the new cell `OG-pr-2` (worker `~148`, the audit write off the loop and refusals reading the body first). This order cannot flip `complete`: the status gate grades the two older proof instances (each worker's own deliverables lane, which the COO may not move) against the amended criteria (row `Z-W147-S2`). `OG-pr-2` is the live record; `OG-ap-40` depends on it. Gate limb: none graded this flip.

<status>superseded</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~147</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
