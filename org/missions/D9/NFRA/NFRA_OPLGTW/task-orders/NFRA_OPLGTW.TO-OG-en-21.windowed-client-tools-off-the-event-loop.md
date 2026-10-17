# NFRA_OPLGTW task order -- `OG-en-21` -- run the windowed client tools off the event loop, so health and every route answer during a page (round 41; CTO round-40 analysis item 1; row Z-S353)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-21</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-21</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~134</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 analysis item 1 (`ledger/ROUND_ANALYSIS.round40.md` @66aeb73b0c: "FIRST and thread-breaking: today a 22-34 s page blocks health and every route") on the CVO's row Z-S350 and the issuer's ruling Z-S353.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-21` (decomposition addendum R3-T.111, round 41, workstream ENRICH-R41)

THE DEFECT. In `app/tools.py`, `client_get_transactions` and `client_get_fees` (decorated `@mcp.tool()`, about lines 1593 to 1608) are plain `def` tools whose body is `return _run(...)`. The installed `mcp` (1.28.x) runs a plain `def` tool ON the event loop (`server/fastmcp/utilities/func_metadata.py` calls a sync function directly), so a windowed read of 22 to 34 s holds up every other route of the service, `/health` included, and the adapter's one-read gate (`WINDOW_READ_GATE` in `app/client_adapter_bd49f.py`) can never contend: a second call just queues behind the first with no 15 s bound. `_PolicyGuardedMCP.call_tool` already uses `anyio.to_thread.run_sync` for its own guard (read the class, about lines 68 to 106), which is the primitive to use.

THE FIX (code only; read `app/tools.py` around the two tools and `_run` first):
1. Make `client_get_transactions` and `client_get_fees` `async def` tools whose body awaits `anyio.to_thread.run_sync(functools.partial(_run, <the same arguments as today>))`, so the whole `_run` (its tier and entitlement gates, its audit write, the adapter read) runs in a worker thread and the event loop stays free. Keep the tool names, signatures, docstrings, registration order, every `_run` argument and the returned value exactly as they are.
2. The request context must reach the thread: `_run` calls `get_current_email()` and `get_current_principal()` and the guard's `remember_allowed` token is set in `_PolicyGuardedMCP.call_tool`. `anyio.to_thread.run_sync` runs the callable in a COPY of the current context; your test must PROVE the principal and email are visible inside `_run` from the thread and that exactly one audit line is written per call.
3. No other tool changes, no change to `app/client_adapter_bd49f.py`, `app/client_core.py`, `app/data_entitlement.py` or `app/server.py`. (Other sync tools stay as they are in this round.)

TESTS (new file `tests/test_og_en21.py`; read the existing gateway tests that drive tools through the registered `mcp` object or `tools.py` functions for the fixtures, for example `tests/test_og_en18.py` and the tools tests; use `anyio` or `asyncio` for the loop):
- `test_ogen21_ac01`: with the adapter call patched to block on an event for 3 s, start one `client_get_transactions` call through the registered tool as a background task on a running loop, and WHILE it is blocked call the app's `/health` handler (`app/server.py` `health`) on the same loop: it answers in under 1 s. Then release the event and the tool call completes with its normal result.
- `test_ogen21_ac02`: with `WINDOW_GATE_WAIT_SECONDS` patched to 0.3 and one windowed call blocked inside the gate, a SECOND concurrent windowed call through the tool returns the `window_read_busy` answer (`absent_reason`) in under 1.5 s while the first is still blocked and reads nothing; after the first finishes a third call succeeds.
- `test_ogen21_ac03`: inside the offloaded body the principal and email equal those set by the caller, one audit line is written per call, and a call whose principal the guard denies is still denied before the body runs (the denial dict unchanged).
If an existing test calls these two tools as plain functions or pins them as sync, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no registry change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_og_en21.py
infra/aws/ec2/opal-gateway/tests/test_og_en20.py
infra/aws/ec2/opal-gateway/tests/test_og_en19.py
infra/aws/ec2/opal-gateway/tests/test_og_en18.py
infra/aws/ec2/opal-gateway/tests/test_og_en17.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/ec2/opal-gateway/tests/test_og_en13.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/tools.py` and `tests/test_og_en21.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~134/`. Rows: id `NFRA_OPLGTW-Z-W134-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-21"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en21.py test_ogen21_ac01 test_ogen21_ac02 test_ogen21_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-21"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~134 '^infra/aws/ec2/opal-gateway/(app/tools\.py|tests/test_og_(en21|en20|en19|en18|en17|en15|en13|cl2)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~134: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-21"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en21set tests/test_og_en4.py tests/test_og_en12.py tests/test_og_cl2.py tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en21.py; echo "exit=$?"</invocation><expect>(?s)en21set forward: passed (\d+); failed 0.*en21set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the listed files. `AC3`: the ten window test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-21.windowed-client-tools-off-the-event-loop.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hashes, the AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41 (decomposition addendum R3-T.111), cell 1 of the CTO's round-40 analysis, FIRST and thread-breaking. Risk WORLD by the L6 floor (a gateway path); no deploy in this cell. It ships in the batched release `OG-ap-36` with item 3 (the deployed-commit marker) under its own never-widen; that release's Phase A re-reads the service heap and runs a health probe during a page chain.
- The CTO's criteria: health answers in under 1 s while a full page runs (`test_ogen21_ac01`); the one-read gate refuses a second concurrent window read instead of queueing behind it (`test_ogen21_ac02`; the refusal comes after the adapter's 15 s gate wait, here patched short). `test_ogen21_ac03` guards the one risk of offloading (the request context and the audit).
- Honest limit: the offline tests prove the loop stays free and the gate contends; the host effect (health during a real page) is measured in the release's Phase B.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent); `AC3` base FAIL (the file is absent; both orders error).

<status>complete</status>
<round>41</round>
<workstream>ENRICH-R41</workstream>
<slot>~134</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
