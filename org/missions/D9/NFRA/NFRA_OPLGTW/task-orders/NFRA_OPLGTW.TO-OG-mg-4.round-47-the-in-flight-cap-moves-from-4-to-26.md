# NFRA_OPLGTW task order -- `OG-mg-4` -- the in-flight cap `MAX_INFLIGHT` moves from 4 to 26 (round 47; the CTO's ruling on `OG-rl-17` condition C1, msg 36195: the measured lower bound of the 24 h peak is 13 calls in flight, so the cap is 2x that)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mg-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-mg-4</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~174</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a constant and its test pin; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the change is the CTO's ruling on the signed condition C1 of `OG-rl-17` (message 36195, 2026-10-20 12:27Z: "MAX_INFLIGHT = 26 (2x the lower bound); QUEUE_WAIT_S stays 20.0").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-mg-4` (decomposition addendum R3-T.124, amendment A8, round 47, workstream ENRICH-R47-I)

DO, in two files and nothing else:
1. `infra/aws/ec2/opal-gateway/app/inflight_guard.py`: change the line `MAX_INFLIGHT = 4` to `MAX_INFLIGHT = 26`. One line. `QUEUE_WAIT_S` stays `20.0`; do not touch the class `Busy`, `InflightGuard` or the process-wide `guard`.
2. `infra/aws/ec2/opal-gateway/tests/test_og_mg3.py`: the single assertion `assert ig.MAX_INFLIGHT == 4 and ig.QUEUE_WAIT_S == 20.0` (about line 44) names the old cap; change `4` to `26`. Every other line of the file stays (its scenarios build their own guards with explicit limits).

Any comment in either file that says the cap is 4 changes to 26 too. Do not edit any other file.

## 2. BOUNDS

- Write only the two files above, `W/` and, if a row is needed, the channel. No other product file, no other test, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/inflight_guard.py
infra/aws/ec2/opal-gateway/tests/test_og_mg3.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~174/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W174-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mg-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mg4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)module constants: MAX_INFLIGHT 26, QUEUE_WAIT_S 20\.0, process-wide guard limit 26, Busy\.code unchanged: ok.*inflight_guard\.py against the pin: 1 removed, 1 added.*: ok.*test_og_mg3\.py against the pin: 1 removed, 1 added.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-mg-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mg4.AC2.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_mg3\.py: [1-9]\d* passed, 0 failed.*neighbours \(2\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the constant, and only the constant, moved. `AC2` (a control; it also passes at the base): the guard's tests and its two neighbours pass at the new cap.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-mg-4.round-47-the-in-flight-cap-moves-from-4-to-26.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-I, amendment A8 of R3-T.124. Source: the CTO's C1 ruling (msg 36195). The change makes `OG-rl-17`'s `release_sha` new: its ask, its three halves and its Phase A records are re-done by `~NFRA1` and re-signed; the window 2026-10-21 06:00Z stands.
- `<risk>WORLD</risk>` is the gateway-path floor. Pre-cut: `AC1` base FAIL as expected (cap 4, 0 and 0 lines changed); `AC2` base PASS as expected (a control). Arm: the two edits applied in the shared tree read `AC1` PASS and `AC2` PASS (5 + 11 tests), then were reverted by edit.
- Pins: `inflight_guard.py` blob `c7716b5398`, `test_og_mg3.py` blob `0d62677122`.

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-I</workstream>
<slot>~174</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
