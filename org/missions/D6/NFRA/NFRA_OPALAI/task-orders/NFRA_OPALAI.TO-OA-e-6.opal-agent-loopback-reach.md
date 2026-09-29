# NFRA_OPALAI task order -- `OA-e-6` -- ROUND 2, E6 first cell: can Opal_Agent reach the Bloomberg loopback ports? (MEASURE ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~14</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one bounded probe; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a measurement; nothing is changed.
EGRESS CLASS, declared: NONE (loopback TCP connects only).
</preflight>

## 1. THE CELL -- `OA-e-6` (round 2, decomposition section R2.1)

The Bloomberg view server (`integrations/bloomberg/mcp/server.py`, four tools) talks to the terminal's DAPI at
`127.0.0.1:8194`, and can serve over `streamable-http` on loopback `127.0.0.1:8790` (`BLOOMBERG_MCP_TRANSPORT=streamable-http`,
`server.py:83-86`). The recommended shape (design note
`org/tier1_exec/1.0.0_SA_CTO/deliverables/OPAL_AI_S15_BLOOMBERG_VIEW_DESIGN_NOTE_20260924.md`, section 2(b)) is: the
OPERATOR runs the server, and the separate local account `Opal_Agent` calls it over loopback. **Whether a second local
account reaches both ports is untested. That is this cell's one measurement.**

In order:
1. **Operator arms (the control).** From your own session, open a TCP connection to `127.0.0.1:8194` and to
   `127.0.0.1:8790` (PowerShell `System.Net.Sockets.TcpClient`, a 3-second timeout; connect then close). Record each as
   `OPEN`, `REFUSED` or `TIMEOUT`, with `whoami` for the account.
   - If nothing listens on 8790, start the view server as the operator for the probe only: the operator's Python, from its
     current workspace path, with `BLOOMBERG_MCP_TRANSPORT=streamable-http`. Wait for the listener, probe, and STOP it
     afterwards. Record `view_server.started_by_cell` and `view_server.stopped`.
   - If 8194 is not OPEN (the terminal's `bbcomm.exe` is not running), the control is dead and the measurement cannot
     discriminate. Record it, file a row, and do not start the terminal.
2. **Opal_Agent arms.** Run the same probe AS `Opal_Agent`:
   `Start-Process powershell -Credential (Import-Clixml "$env:USERPROFILE\.opal_runtime\opal_agent_cred.xml") -Wait ...`.
   - The credential file is the one Part A's provisioning stored, DPAPI-protected, in the operator profile. Never print,
     copy or export it.
   - The probe script and its result file live in `Opal_Agent`'s `state_dir` (`C:\opal_runtime\state`, per
     `C:\opal_runtime\runtime.config.json`). The result records `whoami` as run by that account.
   - Remove the probe script and its result from `state_dir` after you have read them.
3. **TCP connect ONLY.** No MCP request and no Bloomberg request go through either port (DAPI requests consume quota).
4. **Write** `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/E6_LOOPBACK_REACH.json`:
   - `measured_at`;
   - `arms`: exactly four objects `{account_whoami, port, result}`, operator and Opal_Agent crossed with 8194 and 8790;
   - `view_server`: `{started_by_cell, transport, stopped}`;
   - `verdict`: `REACHABLE` if both Opal_Agent arms are OPEN; `NOT-REACHABLE` if neither is; `PARTIAL` otherwise.

**Not this cell's:** the server's move into `opal_ai/opal/mcp/bloomberg/`, and the history-cap CONTRACT question (the
design note's section 3.2). Those are cut from this measurement later.

## 2. BOUNDS

1. You change no file outside your deliverables. You change no account, ACL, group or service. You start nothing but
   the probe processes and, if needed, the view server, which you stop.
2. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `integrations/bloomberg/mcp/server.py`, `C:\opal_runtime\runtime.config.json`, the design note above.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W14-S<k>`
(next free k for W14).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the measurement file is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e6.AC1.sh; echo "exit=$?"</invocation><expect>arms=4; cells filled once 4 of 4; valid results 4; verdict equals implied -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e6.AC2.sh; echo "exit=$?"</invocation><expect>operator 8194=OPEN 8790=OPEN view_server_stopped=yes; Opal_Agent account=present -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~14/NFRA_OPALAI.TO-OA-e-6.opal-agent-loopback-reach.proof_of_spec.json`.
Report once: the four arms, whether you started and stopped the view server, the verdict, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E6's first cell (S15 section 3.1). AC2 is the discriminator: a closed Opal_Agent arm means something
only while the operator's arms on the same ports read OPEN. It also reads the account LIVE, so a file cannot stand in for
Part A.

**Dry-run at base** (main tree, CLOUD `7cb7c7f33d`):
- e6.AC1 base: FAIL as expected (the file is absent).
- e6.AC2 base: FAIL as expected (the file is absent; `Opal_Agent` is absent).

Checker arms were exercised with a synthetic file, then removed:
- GREEN: AC1 PASS on four consistent arms.
- RED: AC1 FAIL on a verdict the arms do not imply.
- AC2 on the green file: FAIL, on the live account read alone (`Opal_Agent` does not exist before Part A), as designed.

**SPAWN ONLY WHEN** Part A has landed: `Opal_Agent` exists, and `verify-boundary.ps1` reads `BOUNDARY: DENIED-OK`. The
slot continues here after OA-e-5.

<status>pending</status>
<round>2</round>
<slot>~14</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
