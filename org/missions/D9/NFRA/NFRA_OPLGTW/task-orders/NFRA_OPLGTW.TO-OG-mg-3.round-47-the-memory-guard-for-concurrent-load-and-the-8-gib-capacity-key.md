# NFRA_OPLGTW task order -- `OG-mg-3` -- the memory guard for concurrent load: a process-wide bound on tool calls running at once, hooked at the one dispatch chokepoint, and the contract's `target_memory_mib` set to the real 8 GiB (round 47; round-46 analysis item 3; row Z-S425, Z-S420)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mg-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-mg-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~169</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code, contract and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429), rank 3: "the memory guard for concurrent load (Z-S425), with `target_memory_mib` set to the real 8 GiB in the same release. A run of parallel callers is bounded by the service, never by the courtesy of the callers."
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-mg-3` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY. On 2026-10-19 the gateway host (then `t4g.small`, `MemoryHigh` 1.2 GB) stopped answering for 80 minutes while six parallel audit runners called it; the service was at its soft memory limit. The host is now `t4g.large` (7.8 GiB) with `MemoryHigh` 5600M, but nothing in the SERVICE bounds how many tool calls run at once: the only bound today is the courtesy of the callers, and the gateway's calls have different sizes (some replies are hundreds of KB). The fix is a process-wide bound on concurrent tool calls, at the one chokepoint every tool goes through. Separately the contract's `capacity.target_memory_mib` still reads 2048, the old 2 GiB host.

READ FIRST (all under `infra/aws/ec2/opal-gateway/`): `app/tools.py` lines 68-106 (`_PolicyGuardedMCP.call_tool`, the dispatch chokepoint of EVERY native, integration and later tool) and the imports at its top; `app/blast_cap.py` (a different guard, for orientation only); `deploy/NFRA_OPLGTW_CONTRACT.json` lines 355-363 (the `capacity` block); `tests/test_og_un1.py` and `tests/test_grant_calendar_months.py::test_ogcm1_ac05` (what pins the unit limits and the byte-equality of the two contract copies).

DO:

1. **A new module `app/inflight_guard.py`** with exactly this API (a probe calls it): module constants `MAX_INFLIGHT = 4` and `QUEUE_WAIT_S = 20.0`; `class Busy(Exception)` with the class attribute `code = "gateway_busy"`; `class InflightGuard` with `__init__(self, limit=MAX_INFLIGHT, wait_s=QUEUE_WAIT_S)`, an async context manager method `slot(self, tool)` and `snapshot(self)` returning `{"limit", "inflight", "waiting", "refused", "peak"}` (integers); and the process-wide instance `guard = InflightGuard()`. Behaviour: at most `limit` bodies run inside `slot` at once; a caller beyond that WAITS for a slot up to `wait_s` seconds and then raises `Busy` (counted in `refused`); `peak` is the highest `inflight` seen; a body that raises releases its slot; the asyncio primitives are created lazily inside the running event loop (the gateway runs Python 3.9: do not build an `asyncio.Semaphore` at import time). No environment variable, no config key, no file: the `.env` key count of the host is pinned at 65, so the two constants are the whole configuration. Imports: the standard library only.
2. **Hook it in `app/tools.py` `_PolicyGuardedMCP.call_tool`**, and only there: add `inflight_guard` to the module's existing `from . import ...` line, and wrap the existing `return await super().call_tool(name, arguments)` (inside the existing `try`/`finally` that forgets the allowed token) in `async with inflight_guard.guard.slot(name):`. The guard comes AFTER the entitlement denial (a denied call returns exactly as before and takes NO slot). On `inflight_guard.Busy` return a `CallToolResult` with `isError=True`, `structuredContent` = `{"error": "gateway_busy", "code": "gateway_busy", "retry_after_s": 5}` and `content` = one `TextContent` of the same dict as `json.dumps(body, indent=2)`, and write one audit row `audit.log_call(get_current_email(), name, {}, "denied", "gateway_busy")`. Reference the module attribute (`inflight_guard.guard`) at call time, never a from-import, so a test can replace the instance. Change nothing else in the file.
3. **The contract, BOTH copies, byte-equal:** in `deploy/NFRA_OPLGTW_CONTRACT.json` and `org/standards/NFRA_OPLGTW_CONTRACT.json` change `capacity.target_memory_mib` from `2048` to `8192`, and nothing else (the multiplier `1.25`, the OS reserve `134217728`, the instance type, the architecture and the other keys stay). Use a byte-level edit that keeps the file's line endings and trailing newline; then `cmp` the two files.
4. **The new test file `tests/test_og_mg3.py`** with at least these tests (names fixed): `test_ogmg3_limit_and_queue` (limit 2, five holders: short wait refuses the surplus, long wait queues them all), `test_ogmg3_released_on_error`, `test_ogmg3_call_tool_busy_envelope` (the parent `FastMCP.call_tool` replaced by a slow fake, the entitlement denial patched to allowed, the guard replaced by `InflightGuard(2, 0.1)`: two run, the rest return the `gateway_busy` result and are audited), `test_ogmg3_denied_takes_no_slot`, `test_ogmg3_contract_capacity` (the key reads 8192 and the two copies are byte-equal). Fakes only.

## 2. BOUNDS

- Write only `app/inflight_guard.py`, `app/tools.py` (the one hunk above), the two contract copies (one value), `tests/test_og_mg3.py`, `W/` and, if a row is needed, the channel. NO unit file (`deploy/opal-gateway.service` stays), no other product file, no release, no deploy, no Terraform, no AWS call.
- The order after this one in your queue (`OG-tp-1`) also writes `app/tools.py`; leave its functions (`search_files`, `search_site_files`, `poll_addressed_impl`) untouched here.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, email address or client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/inflight_guard.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
org/standards/NFRA_OPLGTW_CONTRACT.json
infra/aws/ec2/opal-gateway/tests/test_og_mg3.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~169/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W169-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mg-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mg3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)module constants: ok.*short wait: two ran, three refused, peak 2, inflight 0: ok.*long wait: five ran, none refused, peak 2: ok.*a raising body releases its slot: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-mg-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mg3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)six concurrent calls: 2 ran, 4 refused, no exception: ok.*at most 2 ran at once: ok.*refusals: isError true, code and error gateway_busy, integer retry_after_s: ok.*each refusal audited once: ok.*denied calls: five denials as before, no slot taken: ok.*a single call after the burst runs: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-mg-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mg3.AC3.sh; echo "exit=$?"</invocation><expect>(?s)contract copies byte-equal: yes.*target_memory_mib 8192 \(want 8192\); the other capacity keys unchanged yes.*new file tests/test_og_mg3.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*denial envelope \(alone\): [1-9]\d* passed.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the guard module's bound, queue and release. `AC2`: the hook at the chokepoint (the order of the denial and the slot, the busy envelope, the audit row), probed with a fake parent. `AC3`: the contract in both copies and your test file beside the existing neighbours (the denial-envelope test runs alone because it is order-dependent after two other files).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-mg-3.round-47-the-memory-guard-for-concurrent-load-and-the-8-gib-capacity-key.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once. Then your queue continues with `OG-tp-1` (the same worktree and branch).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) rank 3; Z-S420 disarms on this cell and `OG-sz-1` together, but only after the release's Phase B drives N parallel large calls with `/health` 200 (the applier order).
- READINGS DISCLOSED TO THE CTO: (1) the bound is a COUNT of concurrent calls (4), not bytes: it is the simplest guard the service can enforce itself, and the host has 7.8 GiB with `MemoryHigh` 5600M; the value 4 and the 20 s wait are the issuer's, not measured against a hang. (2) The bound is global, not per principal: a burst by one caller can queue another's call (up to 20 s, then `gateway_busy`, which a poller treats as a missed cycle). (3) The 20 s wait is under the load balancer's 60 s timeout, so a queued call answers rather than timing out. (4) `target_memory_mib` is read by the on-host benchmark harness only (`tests/acceptance/onhost_bench.py`), not by a live admission; changing it changes no running behaviour. (5) The unit file (`MemoryHigh` 5600M / `MemoryMax` 6400M) is unchanged: `OG-rz-1` set it.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (module absent); both were fed a reference implementation in a scratch copy of `app/` and read PASS on every line (the `inflight_guard.py` reference and the `tools.py` hunk described above), then discarded. `AC3` base FAIL as expected (`target_memory_mib` 2048; no test file). The neighbours pass at the base except the one carried red `test_ogz1_ac08` (and the denial-envelope test is run alone).

<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~169</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
