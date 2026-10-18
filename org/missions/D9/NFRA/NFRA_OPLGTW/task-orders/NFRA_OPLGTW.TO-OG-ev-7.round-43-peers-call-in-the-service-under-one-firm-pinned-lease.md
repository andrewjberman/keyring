# NFRA_OPLGTW task order -- `OG-ev-7` -- MEASURE the peers call's 17.9 s in the running service under ONE armed lease that pins the firm (round 43; row `Z-S389`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ev-7</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ev-7</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The arming act writes ONE SSM parameter (`/opal-gateway/probe/lease`, a lease of 25 minutes or less holding an order id, the test account's `****<last4>/<vendor>/<alias>` reference, its FIRM and two times, no secret) with YOUR OWN role, and DELETES it before you finish.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-42 analysis item 6, after item 5 is live.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (the listener binds the loopback interface only).
</preflight>

## 1. THE CELL -- `OG-ev-7` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

WHY. In the OG-ap-40 arming, `etfs_compare_peers` took 17.9 s through the probe listener in the running service against 4.5 s in a fresh process (57 rows each way; row `Z-S389`). One reading, one arming. This cell explains it WITHOUT changing anything. **It is a measurement, not a fix, and its rule is fixed before the run** (the block below is also in `ev7.AC1.sh`'s header and the check recomputes the verdict from your numbers).

⛔ **STAGED BEHIND `OG-ap-42`**: START ONLY on the issuer's GO, which names (a) `OG-ap-42`'s ledger `nfra-oplgtw-gateway-release-batch10` CLOSED and the live sha, and (b) the three never-widen halves signed on your ask. **NO ARMING happens before the firm pin is live**: read `/opt/opal-gateway/.deployed_commit` and confirm it equals the sha in the GO; if it does not, STOP and file a row.

METHOD = `OG-ap-40` Phase B step 6's, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-40.round-42-eighth-batched-release-probe-listener.md` and the scripts it left in `W` (`ap40_probe_run.py`, `ap40_probe_host.py`, `ap40_facts.json`): reuse the same call arguments, the same SIGUSR2 heap read and the same fresh-process harness; this order states only what differs.

### STEP 1 (only on the GO): the ask. NO arming

Write `W/NEVER_WIDEN_ASK_OG-ev-7.md` for THREE halves, each under a heading containing its word: the `widening` (ONE arming of 25 minutes or less of the loopback listener, with a lease that PINS THE FIRM of the test account; three `etfs_compare_peers` calls through the service, which read market data only and take no firm or account argument; one fresh guarded process on the host running the same call; then the lease deleted); the `order` of acts; `both branches` (armed, unarmed); the `rollback` (delete the parameter; the listener closes by itself at the lease's expiry); the `triggers` (VmRSS after any call above 1200 MB (the CTO's CT3 ceiling); the service PID changing; `NRestarts` above 0; host memory above 85 percent; the listener answering any call with no lease; ParameterNotFound not reading after the delete); the bound rule below. Commit, REPORT, STOP.

### STEP 2 (only on the issuer's GO naming all three halves signed at the ask's sha256)

1. Read the lease parameter ABSENT; a connection to the listener answers 403 `probe_not_armed` (record it).
2. ARM ONCE: write the lease (`order` `OG-ev-7`, the test account reference, its `firm`, 25 minutes or less).
3. Three `etfs_compare_peers` calls through the listener, back to back, in the same service process, with the same arguments as the OG-ap-40 peers call: calls 1 and 2 with the SIGUSR2 heap read around them (`heap_signal` `on`), call 3 WITHOUT any SIGUSR2 (`heap_signal` `off`; read `VmRSS`/`VmHWM` only from `/proc/<pid>/status` afterwards). Record per call `wall_s`, `vmrss_mb`, `hwm_mb` and `service_pid`.
4. The SAME call once in a FRESH guarded process on the host (the OG-ap-40 harness), recorded as `fresh_process_wall_s` (the CTO measured 4.5 s earlier; yours is the number that counts).
5. DELETE the lease parameter and show ParameterNotFound and a refused call; read the listener closed at rest; `NRestarts` 0 after.
6. The verdict by the rule: `COLD` if call 1's wall is at least 2 times call 2's; else `SLOW_IN_SERVICE` if every one of the three walls is more than 2 times `fresh_process_wall_s`; else `SIGNAL_COST` if call 3's wall is at least 20 percent below call 2's; otherwise `INCONCLUSIVE`. Write `W/PEERS_MEASURE.json` (fields as in `ev7.AC1.sh`'s header) and commit.

## 2. BOUNDS

- ONE arming, 25 minutes or less, the lease deleted before you finish. No release, no deploy, no IAM, no Terraform, no env key, no other SSM write. No account number, person's name, credential or object content in any record (`****<last4>` form only).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; leave the lease parameter in place; arm a second time (a STOP is a row and a report); **run gateway code on the host without the hard guard** (the three calls go to the RUNNING service, which carries the unit's memory ceiling, only through the listener).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ev-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ev7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)three calls in the order on/on/off with walls .* one PID yes; fresh-process wall .*lease \d+ minutes \(25 or fewer\), armings 1 \(want 1\), firm pinned True, ParameterNotFound after the delete True, listener closed at rest True, restarts after 0: ok.*verdict by the rule fixed before the run: (COLD|SLOW_IN_SERVICE|SIGNAL_COST|INCONCLUSIVE); the record says \1: consistent.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three calls ran in the stated order within the safety bounds, the framing facts hold (one arming, the firm pinned, the delete read), and the record's verdict is the one the rule gives from its numbers. Any of the four verdicts PASSES; `INCONCLUSIVE` is an answer.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ev-7.round-43-peers-call-in-the-service-under-one-firm-pinned-lease.proof_of_spec.json` and validate it with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`. The `<status>` flip is mine. Report once per step: the four walls, the VmRSS values, the verdict, the CLOSED time of the lease.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 6 ("two peers calls in the same service, back to back, then one with the heap signal off; print the wall time and VmRSS of each; a measurement, not a fix; its bound is set in the cell before the run"). The cell adds a fresh-process call in the same session as the contrast (the CTO's 4.5 s is the only fresh-process number on record and was measured on another occasion) and defines the four verdicts and the bounds before the run, as the analysis asks.
- The bounds are SAFETY bounds (VmRSS at most 1200 MB, one PID, `NRestarts` 0, one arming); the 17.9 s itself carries no pass/fail bound, because the cell explains it and does not grade it.
- Risk WORLD (a production arming and a gateway path floor); needs a three-half ask like the OG-ap-40 arming (the firm is pinned this time).
- Chain: follows `OG-ap-42` CLOSED. Applier `~NFRA1`.
- Pre-cut: `AC1` base FAIL as expected (the record is absent).

<status>staged</status>
<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
