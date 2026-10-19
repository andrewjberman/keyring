# NFRA_OPLGTW task order -- `OG-rs-1` -- APPLY: restart the hung `opal-gateway` service on the gateway host, same code, no deploy (round 46, URGENT: before 2026-10-19T18:30Z; Alyssa tests at 19:00Z)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rs-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rs-1</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time service restart; no schedule, trigger or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the restart uses the SSM path your deploys already use on this host (`AWS-RunShellScript` through `safe-ec2-deploy.sh`'s host tooling or the same SSM document), no new action.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act answers `2.0.0_SA_COO~MI`'s report (msg 36038, 17:47Z): the gateway host `i-07dccb1615503ac99` answers no MCP call since about 17:40Z, `127.0.0.1:8080/health` returns nothing, the uvicorn process is up at RSS 1.41 GB against `MemoryHigh` 1.2 GB and `MemoryMax` 1.4 GB. The probable cause (six parallel battery runners from 17:38Z, stopped 17:46Z) is the reporter's; you measure, you do not assume it.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, EC2 host).
</preflight>

## 1. THE CELL -- `OG-rs-1` (decomposition addendum R3-T.123 amendment A4, round 46, workstream ENRICH-R46-D)

**DEADLINE: `/health` answers 200 and the 27-tool read passes before 2026-10-19T18:30:00Z.** Alyssa tests at 19:00Z with Andrew. This is a RESTART of the running release `6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c`: no code, no unit file, no `.env`, no manifest change, no `HALT_OVERRIDE`. Move fast; you are also holding `OG-mg-2` Phase A (its deadline is 18:45Z): do this FIRST, it takes minutes, then return to `OG-mg-2`.

1. **Measure, do not assume (3 minutes).** Over SSM: `/health` (local), `systemctl show opal-gateway` (`ActiveState`, `NRestarts`, `MemoryCurrent`, `MemoryHigh`, `MemoryMax`), the process RSS, `free -m`, the last 20 journal lines of the unit (timestamps only; no request bodies), the marker `/opt/opal-gateway/.deployed_commit`, and any other process on the host holding memory (names and RSS only). Write `W/RS1_BEFORE.json`. If `/health` ANSWERS 200 within 5 seconds, STOP and report: it is not hung.
2. **Ledger** `nfra-oplgtw-gateway-restart-20261019`, entry AND sentinel committed first (one leg `restart`); read every open gateway ledger first: another seat's open ledger is a STOP (but `OG-mg-2`'s ledger, if you already opened it, is database-only and does not block).
3. **Restart the service** (`systemctl restart opal-gateway`; the unit's own stop timeout applies; if it does not stop within 60 seconds, report before killing anything). Record the UTC time.
4. **Read back, within 60 seconds of the restart and again at 5 minutes:** `/health` 200; the marker still `6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c`; `tools/list` 103; ONE process; `NRestarts` after the restart; memory (`MemoryCurrent`) before and after, as counts; the host md5 walk against the release (differ 0); then the 27-tool read under the hard guard in a fresh process, as in `OG-ap-50`. Write `W/RS1_RESTART.json` with the fields the check reads: `{"health_before", "health_after", "health_after_seconds_from_restart", "marker_before", "marker_after", "tools_list_after", "processes_after", "nrestarts_after", "memory_before_mb", "memory_after_mb", "host_md5_differ", "restart_utc"}`.
5. Close the ledger, run AC1, commit, and REPORT once to `2.0.0_SA_COO~O` with the `/health` result and the CLOSED time. If `/health` is NOT 200 after the restart, report the same turn with what the journal says; do not retry blindly.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`.

## 2. BOUNDS

- ONE restart of ONE service. No deploy, no code, IAM, unit, env or manifest change. Never `kill -9` before reporting. No arming, no SSM parameter write other than the command that restarts the unit.
- No tid, oid, e-mail, account id, ARN or account number in any repo file, row or report: counts, hashes and statuses only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a delete action; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-restart-20261019.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rs-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/rs1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)status CLOSED=yes; sentinel at HEAD=no.*marker equals the live release before and after: yes; tools/list 103: yes; one process: yes; host md5 differ 0: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the service was restarted once, the ledger is closed, `/health` was not 200 before and was 200 within 60 seconds after, the running release is unchanged, `tools/list` still reads 103, one process, and the host files equal the release.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rs-1.round-46-restart-the-hung-gateway-service.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, and flip the ONE `<status>` tag to `complete` only if AC1 PASSES. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, amendment A4 of R3-T.123, workstream ENRICH-R46-D (a third workstream: the gate keys one issuance to the round and refused a second order under ENRICH-R46-B and under ENRICH-R46-C). Cut on `2.0.0_SA_COO~MI`'s report (msg 36038); the lane `~NFRA1` is the applier of this gateway host, and it holds `OG-mg-2` Phase A, which this order outranks by ten minutes.
- Pre-cut: `rs1.AC1` base FAIL as expected (ledger absent, record absent).
- Open, not this seat's: whether six parallel battery runners can push the host past `MemoryHigh` again. `2.0.0_SA_COO~MI` has been told to run at most two calls at a time after the restart is confirmed.

- SUPERSEDED (issuer, 2026-10-19 ~18:4xZ): the need was met another way. `0.0.0_AB_MSTR~Z` restarted the service itself at 18:24:47Z under the SAME ledger name (the CTO's routing, msg 36060, after `~NFRA1` had read neither GO while mid-turn on `OG-mg-2`): `/health` 200 at 18:26:22Z, marker `6d1b5dcb64`, one process, ledger `nfra-oplgtw-gateway-restart-20261019` CLOSED 20261019T183627Z, record `org/critical_paths/change_management/20261019T1821Z_nfra-oplgtw-gateway-restart-20261019_deploy_completion.md`. I read the gateway answering end to end at 18:38Z (a `whoami` through the gateway returned). NOT done by anyone: `tools/list` 103 and the 27-tool read under the hard guard; they ride the next gateway read-back (`OG-ap-51` or the next release), and `2.0.0_SA_COO~MI`'s battery reads the tools at two calls at a time.

<status>pending</status>
<status>superseded</status>
<round>46</round>
<workstream>ENRICH-R46-D</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
