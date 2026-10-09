# NFRA_OPALAI task order -- `OA-f-11` -- DIRECT ACT, ADDENDUM R2-A9: Opal_Agent and Opal_MSP walled off DAPI 8194 by a raw WFP filter pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~26</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a script and one measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC3's operator arm is the live control and its agent arms are the falsifier.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-11` (decomposition ADDENDUM R2-A9)

Two local Windows accounts run Claude Code agents on this box: `Opal_Agent` and `Opal_MSP`. Each must reach Bloomberg
only through the view server on `127.0.0.1:8790`, and NEVER the Terminal's DAPI port `127.0.0.1:8194`.

A per-user Windows Firewall Outbound Block rule was measured INERT on loopback: with both rules live, both accounts
still opened 8194. Those rules are `opal_runtime_block_dapi_8194_Opal_Agent` and `_Opal_MSP`. The reason is a
max-weight boot-time loopback PERMIT in the Firewall's own WFP sublayer. Under WFP filter arbitration, a BLOCK in a
higher-priority sublayer is final.

Build ONE new script, `opal_ai/opal/runtime/provision/wall-dapi-8194-wfp.ps1 [-Plan | -Remove]`:

1. **The P/Invoke layer.** Use `Add-Type` with C# that P/Invokes `fwpuclnt.dll`:
   - engine: `FwpmEngineOpen0`, `FwpmEngineClose0`;
   - transactions: `FwpmTransactionBegin0`, `FwpmTransactionCommit0`, `FwpmTransactionAbort0`;
   - adds: `FwpmSubLayerAdd0`, `FwpmFilterAdd0`;
   - reads and deletes: the filter and sublayer enum/get and delete calls the modes need;
   - plus `ConvertStringSecurityDescriptorToSecurityDescriptorW` (advapi32), to turn the SDDL into the self-relative
     security descriptor the `ALE_USER_ID` condition takes.

   No vendor tool, no install, no module download. GUIDs for layers and conditions come from the Windows SDK names
   (`FWPM_LAYER_ALE_AUTH_CONNECT_V4/_V6`, `FWPM_CONDITION_ALE_USER_ID`, `FWPM_CONDITION_IP_REMOTE_PORT`,
   `FWPM_CONDITION_FLAGS`); write them as constants with their SDK names in comments. This script's own sublayer and
   filter keys are fixed GUIDs you generate once and commit, so `-Remove` and re-runs find them.
2. **What it installs.**
   - One sublayer `opal_runtime_dapi_8194_wall`: `FWPM_SUBLAYER_FLAG_PERSISTENT`, weight `0xFFFF`.
   - Two filters in it, `opal_runtime_dapi_8194_block_v4` at `ALE_AUTH_CONNECT_V4` and `..._v6` at `ALE_AUTH_CONNECT_V6`.
     Each is `FWP_ACTION_BLOCK`, `FWPM_FILTER_FLAG_PERSISTENT`, and ANDs three conditions:
     - `ALE_USER_ID` = SDDL `O:LSD:(A;;CC;;;<Opal_Agent SID>)(A;;CC;;;<Opal_MSP SID>)`. Resolve each SID at run time
       with `Get-LocalUser`; type no SID. An unknown account prints `WFP: REFUSE UNKNOWN-ACCOUNT <name>` and exits 2,
       before any act.
     - `IP_REMOTE_PORT` = 8194.
     - `FLAGS` `FWP_MATCH_FLAGS_ALL_SET` `FWP_CONDITION_FLAG_IS_LOOPBACK`.

     Port 8790 is never named.
3. **`-Plan`** (any privilege; it opens no engine and changes nothing):
   - it compiles the `Add-Type` type and prints `COMPILE: OK`;
   - then exactly ONE line `PLAN: SUBLAYER opal_runtime_dapi_8194_wall PERSISTENT WEIGHT 0xFFFF`;
   - then exactly TWO lines `PLAN: FILTER <name> <ALE_AUTH_CONNECT_V4|ALE_AUTH_CONNECT_V6> BLOCK PERSISTENT REMOTE_PORT
     8194 IS_LOOPBACK USER <SDDL with both SIDs>`;
   - then it exits 0.
4. **Real mode (no switch) and `-Remove`.** Each first refuses a non-elevated token, BEFORE any act:
   `ELEVATION REQUIRED: ... No action was taken.`, exit 3.
   - **Real mode, elevated:**
     - (a) BEFORE any act, enumerate the filters at `ALE_AUTH_CONNECT_V4` whose action is PERMIT and that match loopback.
       Print each one's sublayer key, name and weight. If ANY such sublayer's weight is >= 0xFFFF, print `WFP: REFUSE
       PERMIT-WEIGHT <sublayer> <weight>` and exit 5 with NO act.
     - (b) In ONE transaction, add the sublayer and both filters (replacing this script's own existing ones by key,
       idempotent). Commit, or abort on any error and exit 4.
     - (c) Read back the sublayer and both filters by key, printing `VERIFY: <name> OK` (3 lines) or `... FAIL` with
       exit 4.
     - (d) Only after (c) is all OK, remove the two inert R1 rules `opal_runtime_block_dapi_8194_Opal_Agent` and
       `_Opal_MSP` (`Remove-NetFirewallRule`, ignore if absent), printing `R1: REMOVED <n>`.
   - **`-Remove`, elevated:** delete both filters and the sublayer in one transaction and print `REMOVED: <n>`.
5. **Header.** One paragraph saying what it blocks, that 8790 stays open, that it needs an Administrator, and how to
   roll back (`-Remove`).

**AC3, the acceptance, runs only after an Administrator's apply.** Your session cannot apply: never elevate. If the
filters are absent when you get here, still run AC3. Record its FAIL as the expected first read, leave the order open,
and report it. Once the apply is done:
- **Inputs:**
  - `0.0.0_AB_MSTR~Z` returns the elevated run's VERIFY lines to the issuer, who hands them to you; put them in
    `apply_verify`.
  - The Terminal must be up, meaning `127.0.0.1:8194` is listening.
- **The probe:**
  - TCP connect only (`System.Net.Sockets.TcpClient`, 3 s timeout), as Opal_Agent, as Opal_MSP, and as the operator.
  - Credentials are `%USERPROFILE%\.opal_runtime\opal_agent_cred.xml` and `opal_msp_cred.xml`. Never print, copy or
    export them.
  - Opal_Agent's probe runs from `C:\opal_runtime\state`. Opal_MSP has no ACE there, so its probe runs from
    `C:\Users\Public`. Delete each probe and its result afterwards.
- **The view server:** if nothing listens on 8790, start it as the operator for the probe only, then stop it. It is
  `integrations/bloomberg/mcp/server.py` with `BLOOMBERG_MCP_TRANSPORT=streamable-http`, on the operator's Python 3.11.
- **The record:** write
  `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~26/F11_ACCEPTANCE.json` with `measured_at`,
  `apply_verify` (the VERIFY lines), `arms` (each `{account (Opal_Agent|Opal_MSP|operator), whoami, port, result}`) and
  `view_server`.

**ISSUER AMENDMENT 2 (2.0.0_SA_COO~AI, 2026-10-09 ~01:3xZ): AC4, R5's persistence arm, re-opens this order.** The box
rebooted after the apply (LastBootUpTime 2026-10-08T20:56:05Z, after AC3's 2026-10-02T03:02Z), so the arm R5 named "read
at the next natural reboot" is readable now. AC1 and AC3 stand as graded; you run AC4 only. Nothing is built.
1. **Preconditions, read first:** `127.0.0.1:8194` is listening (`Get-NetTCPConnection -State Listen -LocalPort 8194`).
   If not, STOP: write no record and REFUSE AC4 with that measurement. Never sign in to or start the Bloomberg Terminal.
   Read `(Get-CimInstance Win32_OperatingSystem).LastBootUpTime` in UTC.
2. **The probe:** exactly AC3's probe above (TCP connect only, 3 s, the same two credential files never printed, copied
   or exported, the same working directories, the view server started and stopped only if 8790 is not listening).
   Delete each probe and its result file afterwards, and check both directories hold nothing you wrote.
3. **The record:** write `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~26/F11_PERSISTENCE.json`
   with `measured_at` (UTC `YYYY-MM-DDTHH:MMZ`), `boot_time` (UTC ISO), `method`, `arms` (each `{account
   (Opal_Agent|Opal_MSP|operator), whoami, port, result}`) and `view_server`. Never edit F11_ACCEPTANCE.json.
4. Append AC4's result to the existing proof_of_spec instance, keeping AC1 and AC3 as they are. An agent arm reading
   `OPEN` on 8194 is the finding: record it, file a row, and leave the order open.

## 2. BOUNDS

1. TCP connect ONLY: no MCP request and no Bloomberg request through any port.
2. Never elevate. Never run real mode or `-Remove` except to read their `ELEVATION REQUIRED` refusals. Never create or
   delete a WFP object, firewall rule, account or ACL.
3. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `eeca5ca7d1`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~26 <0.9.0_WK_NFRA_OPALAI~26@opal.agent>" -F <msgfile> -- <nested path>`,
   the msgfile written with the Write tool. The parent gitlink is NOT yours.
4. Flip `
**ISSUER AMENDMENT 1 + CLOSE (2.0.0_SA_COO~AI, 2026-10-02 ~03:1xZ; R5 author `1.0.0_SA_CTO~O` msg concurs):** Andrew ran
the installer elevated (`C:\opal-elev\wfp_8194_run.txt`). The permit scan found max loopback-permit weight 0x0007, so no
refusal. block_v4 and block_v6 read VERIFY OK; the sublayer read VERIFY FAIL. Andrew's elevated `netsh wfp show state`
dump (`F11_SUBLAYER_EVIDENCE.json`) shows the sublayer PRESENT and PERSISTENT at weight 0xFFE2, holding both BLOCK filters
(157756 V4, 157757 V6; 8194; IS_LOOPBACK; both SIDs). SentinelOne and WebProtectionDriver hold 0xFFFF..0xFFE3, so the
installer's exact `weight == 0xFFFF` VERIFY can never pass on this box (row Z-S54). AC3's apply limb is amended IN
PLACE to accept both filter VERIFY OK lines plus that evidence. Negative control: with the evidence file hidden it FAILs.
Issuer re-grade of AC3 on CLOUD: PASS. The arms (F11_ACCEPTANCE.json @52640d92c7, 03:02Z): Opal_Agent 8194 REFUSED / 8790
OPEN; Opal_MSP 8194 REFUSED / 8790 OPEN; operator 8194 OPEN. The R1 rules were removed by Andrew (0 live). Gate: LIMB 6
does not fire on a modification, and GATE (viii) graded it. Persistence is the sixth arm, read at the next natural
reboot (R5), and is not a close precondition. R3 is met, so the item-0 close run UN-HOLDS.

the `<status>` tag IN PLACE, by replacing the single tag, and only when every criterion passes. Standing: no push, no
   install, no vendor call. REFUSE a criterion you cannot meet as written, with its measurement.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/wall-dapi-8194-wfp.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~26/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-f-11.dapi-8194-wfp-wall.md
</paths>

Read-only: `opal_ai/opal/runtime/provision/wall-dapi-8194.ps1` (the R1 script, for its SID-resolution and refusal
patterns) and `integrations/bloomberg/mcp/server.py`. Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W26-S<k>` (none
at the cut).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-11"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f11.AC1.sh; echo "exit=$?"</invocation><expect>plan rc=0 COMPILE OK>=1 SUBLAYER persistent 0xFFFF=1 FILTER lines=2 (V4=1 V6=1) well-formed=2 lines naming 8790=0; real and -Remove ELEVATION REQUIRED rc=3; S-1-5-21 literals=0; P/Invoke tokens=4 of 4; PERMIT-WEIGHT refusal>=1; removes R1 rules=1; parse errors=0; other files changed vs eeca5ca7d1=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-f-11"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f11.AC3.sh; echo "exit=$?"</invocation><expect>R1 Firewall rules still present: 0; agent 8194=REFUSED|TIMEOUT 8790=OPEN; msp 8194=REFUSED|TIMEOUT 8790=OPEN; operator 8194=OPEN; apply VERIFY OK lines>=3; arms ok=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OA-f-11"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f11.AC4.sh; echo "exit=$?"</invocation><expect>R1 Firewall rules present: 0; boot after apply=yes; agent 8194=REFUSED|TIMEOUT 8790=OPEN; msp 8194=REFUSED|TIMEOUT 8790=OPEN; operator 8194=OPEN; arms ok=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~26/NFRA_OPALAI.TO-OA-f-11.dapi-8194-wfp-wall.proof_of_spec.json`.
Report once:
- the `-Plan` output;
- the nested commit hash and the script's blob sha;
- the GUIDs you fixed;
- AC1's line, and AC3's line (expected FAIL before the apply);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on `1.0.0_SA_CTO~O` msg 28059, ruling R5 @9d6fbe3e97 (CRO research @63a9b6da27,
`WFP_LOOPBACK_8194_WALL_RESEARCH_20261001.md`): "Cut ONE cell".

It SUPERSEDES OA-f-10's mechanism. OA-f-10 stays open, with its rules recorded INERT (rows Z-W25-S3, Z-S52), and closes
when this cell's AC3 passes.

LOCAL direct act, as with OA-f-10: the order's own acts are one script and one measurement. The apply is Andrew's admin
act under his "sure" (msg 28000), which per R5 covers the mechanism move. Two criteria:
- AC1: the build, its plan, a compile of the P/Invoke type, and the bounds;
- AC3: the acceptance after the apply.

The persistence arm is read at the next NATURAL reboot (R5). It is not a close precondition, and it is not on this face.
If the apply's pre-act read REFUSES on PERMIT-WEIGHT, R5's fallback (deny Bash/PowerShell to the Analyst runtime by
managed settings) is the CTO's to rule on that measurement.

SPAWN: at the cut. Slot `~26`, `/c/tmp/oa-26`, `--nested opal_ai=eeca5ca7d1`. Worker class `worker`: P/Invoke into WFP is
not a light cell.

Dry-run at base:
- f11.AC1 base (OA_F11_REF=eeca5ca7d1): FAIL as expected (`wall-dapi-8194-wfp.ps1 absent`).
- f11.AC3 base: FAIL as expected (`R1 Firewall rules still present: 2; F11_ACCEPTANCE.json absent`).

**AMENDMENT 2 RECORD (issuer):** cut on an empty `/canonical-drive` tick by `/next-calls NFRA_OPALAI --drive` (Andrew-direct
2026-10-09 ~00:0xZ, the work around a block): every open round-2 order waits on the item-0 close run, and Andrew's 10-06
word was "nothing we can do on the call 1 at this time". First cut as a new order OA-f-15; `.tools/to-pipeline-gate.py`
refused it (round 2 already has its one issuance; "a re-cut into the first issuance MODIFIES its orders and adds no
file"), so the arm rides the order whose record face already named it. Gate on this modification: LIMB 6 does not fire,
GATE (viii) grades it (`<placeholders>NONE`). bbcomm (pid 18020) listens on 8194, nothing on 8790 (read ~01:1xZ). Respawn
slot `~26` (worker-light, sparse cone plus `integrations/bloomberg`, no nested checkout). A worker runs it because row
Z-S41 bars this seat from direct credential use. Dry-run at base (c249be336b): AC4 FAIL as expected (record absent; R1 0;
live boot 2026-10-08T20:56:05Z). Synthetic arms, then removed: GREEN PASS; RED FAIL with Opal_Agent 8194 OPEN; RED FAIL
with boot_time before the apply. A FAIL re-opens R5 at `1.0.0_SA_CTO~O` with its measurement. Gates nothing.

<status>complete</status>
<direct_act>true</direct_act>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
