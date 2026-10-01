# NFRA_OPALAI task order -- `OA-f-10` -- ADDENDUM R2-A8: Opal_Agent and Opal_MSP walled off Bloomberg DAPI 8194 (falsifier, apply script, acceptance)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~25</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a script and two measurements; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the falsifier (AC1) is the adversary read of the mechanism; AC3's operator arm is the live control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-10` (decomposition ADDENDUM R2-A8)

Two local Windows accounts on this box run Claude Code agents: `Opal_Agent` (the Teams Analyst) and `Opal_MSP`. A
measurement showed `Opal_Agent` can open a TCP connection to `127.0.0.1:8194`, the Bloomberg Terminal's DAPI port.
DAPI draws on the signed-in Terminal user's data limits and refuses no second OS user. These agents may reach
Bloomberg only through the view server on `127.0.0.1:8790`.

The ruling is a Windows Firewall rule per account:
- Outbound, Block, TCP;
- `LocalUser` = that account's SID;
- RemoteAddress `127.0.0.0/8` only (AMENDMENT 2: no IPv6 arm; bbcomm listens on 127.0.0.1 only, and New-NetFirewallRule rejects `::1`);
- RemotePort **8194 only**.

**8790 stays open.** The shape is the same as two rules already live on this box, `codex_sandbox_offline_block_loopback_tcp`
and `_udp`, whose `LocalUser` reads `O:LSD:(A;;CC;;;<SID>)`. You do three things.

1. **The falsifier (measure first; it changes no host state).** Does a per-user Firewall rule block LOOPBACK here?
   - Inside the Codex OFFLINE sandbox, open a TCP connection to `127.0.0.1:8194` with
     `System.Net.Sockets.TcpClient` and a 3-second timeout. Record `OPEN`, `REFUSED` or `TIMEOUT`, plus `whoami` as
     printed inside. The sandbox you need is the one whose identity the `codex_sandbox_offline_block_loopback_*` rules
     name.
   - Run the same probe outside, as yourself. That is the control, and it must read `OPEN`: the Terminal is running.
   - The CLI is `codex` on PATH. `codex sandbox [OPTIONS] <COMMAND>...` runs a command under a Windows restricted
     token, and `--sandbox-state-disable-network`, `-P <permission profile>` and `--sandbox-state-json` are its
     options. Plain `codex sandbox whoami` prints the OPERATOR, which is not the offline identity. Find the invocation
     whose `whoami` differs from yours. Install nothing, and change no codex config file.
   - Write `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~25/F10_FALSIFIER.json` with:
     - `measured_at`;
     - `inside` and `outside`, each `{whoami, result, command}`;
     - `mechanism`: `FIREWALL-RULE` when inside reads REFUSED or TIMEOUT, `LOOPBACK-EXEMPT` when inside reads OPEN.
   - If no invocation gives a distinct identity, record what you tried, set `mechanism: INCONCLUSIVE`, file a row, and
     refuse AC1.
2. **The apply script.** NEW `opal_ai/opal/runtime/provision/wall-dapi-8194.ps1 [-Accounts <names>] [-Plan]`.
   - `-Accounts` defaults to `Opal_Agent,Opal_MSP`.
   - Each account's SID is resolved at run time with `Get-LocalUser`. No SID is typed in the file. An unknown account
     prints `WALL: REFUSE UNKNOWN-ACCOUNT <name>` and exits 2, before any act.
   - **`-Plan`** changes nothing and runs at any privilege. It prints exactly one line per account,
     `PLAN: RULE opal_runtime_block_dapi_8194_<account> OUTBOUND BLOCK TCP 127.0.0.0/8 REMOTEPORT 8194 LOCALUSER <SID>`,
     then exits 0. No line names 8790.
   - **Real mode** first refuses a non-elevated token: `ELEVATION REQUIRED: ... No action was taken.` and exit 3,
     before any act. Elevated, it does the following:
     - for each account, creates the rule with `New-NetFirewallRule`, replacing any existing rule with that
       DisplayName. Use `-LocalUser "O:LSD:(A;;CC;;;<SID>)"`, `-RemotePort 8194`, `-RemoteAddress 127.0.0.0/8`
       and `-Profile Any`;
     - reads each rule back (port filter 8194/TCP, the address filter, `LocalUser` containing the SID) and prints
       `VERIFY: <displayname> OK`, or `VERIFY: <displayname> FAIL` with exit 4.
   - Header: one paragraph saying what the rule blocks, that 8790 stays open, and that the apply is an Administrator
     act.
3. **Acceptance (AC3).** This runs only after an Administrator has applied the rules. Your session cannot apply them:
   never elevate.
   - **First read.** If the rules are absent when you get here, still run AC3. Record its FAIL with the line it
     prints, which is expected before the apply. Leave the order open and report it.
   - **Once the rules are live.** Re-run the loopback probe as each account. The credentials are
     `%USERPROFILE%\.opal_runtime\opal_agent_cred.xml` and `...\opal_msp_cred.xml` (DPAPI-protected); never print, copy
     or export them. Run each probe script with `-File` from `C:\opal_runtime\state`, and remove the script and its
     result afterwards.
   - **The arms:** each account to 8194 and 8790, and the operator to 8194. If nothing listens on 8790, start the view
     server as the operator for the probe only, then stop it:
     - `integrations/bloomberg/mcp/server.py` with `BLOOMBERG_MCP_TRANSPORT=streamable-http`;
     - use the operator's Python 3.11, which has blpapi and mcp; the default 3.14 has neither.
   - **The record:** write
     `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~25/F10_ACCEPTANCE.json` with `measured_at` and
     `arms`, each `{account (Opal_Agent|Opal_MSP|operator), whoami, port, result}`.

## 2. BOUNDS

1. **TCP connect ONLY.** No MCP request and no Bloomberg request go through any port; DAPI requests consume quota.
2. **Never elevate.** Never run the script's real mode except to read its `ELEVATION REQUIRED` refusal. Never create,
   change or delete a firewall rule, account, ACL or codex config.
3. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `e69acf7`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~25 <0.9.0_WK_NFRA_OPALAI~25@opal.agent>" -F <msgfile> -- <nested paths>`,
   the msgfile written with the Write tool. The parent `opal_ai` gitlink is NOT yours.
4. **Status flip:** flip `
**ISSUER AMENDMENT 1 (2.0.0_SA_COO~AI, 2026-10-01 ~12:4xZ; `1.0.0_SA_CTO~O` msg 27829 amends ruling R2.1):** AC1 is retired
from the proof of spec, and AC3's Opal_Agent -> 8194 arm IS the falsifier (apply, then measure). The worker's AC1
stays recorded as REFUSED/INCONCLUSIVE (rows Z-W25-S1 and S2): `codex sandbox` here is unelevated and runs as the operator,
and an elevated run re-ACLs. Readings:
- REFUSED on Opal_Agent -> 8194, with 8790 and the operator arm OPEN: the wall stands.
- OPEN: loopback is exempt; the rule is removed or left inert, and the CTO re-rules to a raw WFP filter.
The item-0 close run stays held until the 8194 arm reads REFUSED. Gate: LIMB 6 does not fire on a modification, and
GATE (viii) graded it (<placeholders>NONE).


**ISSUER AMENDMENT 2 (2.0.0_SA_COO~AI, 2026-10-01 ~17:5xZ; `1.0.0_SA_CTO~O` msg 28005):** the first elevated apply
(0.0.0_AB_MSTR~Z, msg 28003, from PROD 9c0a80b, under Andrew's UAC) FAILED on both creates: "New-NetFirewallRule : An
unspecified, multicast, broadcast, or loopback IPv6 address was specified." 0 rules were created and nothing was left
partial. RULED: `-RemoteAddress '127.0.0.0/8'` only, because bbcomm listens on 127.0.0.1 only (CRO research @5d804ea419).
The VERIFY readback drops its `::1` term. f10.AC2 now requires `127.0.0.0/8` and no `::1`. Dry-run at 9c0a80b:
well-formed=0, FAIL as expected. The fix lands on r2-dev, and 0.0.0_AB_MSTR~Z re-runs it from that reviewed commit
(blob sha verified) under Andrew's "sure". Promoting it to PROD rides the next G-PUSH. Gate: LIMB 6 does not fire on a
modification, and GATE (viii) graded it.


**ISSUER NOTE 3 (2.0.0_SA_COO~AI, 2026-10-01 ~20:3xZ; `1.0.0_SA_CTO~O` msg 28057):** AC3 read @1552d46a70, and the falsifier
FIRED. With both rules live, Opal_Agent -> 8194 and Opal_MSP -> 8194 read OPEN (LOOPBACK-EXEMPT, rows Z-W25-S3 and Z-S52). The two
`opal_runtime_block_dapi_8194_*` rules are LEFT LIVE but **INERT. They are NOT a wall.** They come out, or are kept, in the
same elevated sitting as the WFP install. The mechanism goes back to the CTO: a raw WFP filter, now at
`4.0.0_SA_CRO~O` research. On that ruling the issuer cuts ONE new cell (the installer, a -Plan, and the same AC3). This
order stays open until then. The item-0 close run stays HELD, and the interim (no DAPI client in the runtime) holds.

<status>` IN PLACE, by replacing the existing tag. Never append a second tag; the row gate
   reads the FIRST tag. Standing rules also apply: no push, no install, no vendor call. REFUSE a criterion you cannot
   meet as written, and report the refusal with its measurement.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/wall-dapi-8194.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~25/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-f-10.dapi-8194-wall.md
</paths>

Read-only: `integrations/bloomberg/mcp/server.py`; the live firewall (`Get-NetFirewallRule`). Rows:
`org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W25-S<k>`
(none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC2" cell_refs="OA-f-10"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f10.AC2.sh; echo "exit=$?"</invocation><expect>plan rc=0 PLAN: RULE lines=2 well-formed=2 Opal_Agent SID named=1 Opal_MSP SID named=1 lines naming 8790=0; unknown 'WALL: REFUSE UNKNOWN-ACCOUNT' rc=2; real-mode 'ELEVATION REQUIRED' rc=3; S-1-5-21 literals=0; parse errors=0; other files changed vs e69acf7=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-f-10"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f10.AC3.sh; echo "exit=$?"</invocation><expect>live 8194 block rules matching an account SID: 2 of 2; agent 8194=REFUSED|TIMEOUT 8790=OPEN; msp 8194=REFUSED|TIMEOUT 8790=OPEN; operator 8194=OPEN; arms ok=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~25/NFRA_OPALAI.TO-OA-f-10.dapi-8194-wall.proof_of_spec.json`.
Report once:
- the falsifier's two arms, the invocation that ran inside, and the mechanism;
- the script's `-Plan` output;
- the nested commit hash;
- AC3's line, and whether the rules were live;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on `1.0.0_SA_CTO~O`'s ruling `CTO_RULING_20261001_OPAL_AGENT_DAPI_8194_WALL.md` @ff362bfa86
(msg 27807): "cut ONE cell carrying (a) the Codex OFFLINE-sandbox falsifier, (b) the apply runbook ... applied as
Andrew's admin act, and (c) the three-arm E6 re-run as acceptance". The research is `4.0.0_SA_CRO~O`
`OPAL_AGENT_DAPI_8194_WALL_RESEARCH_20261001.md` @5d804ea419.

Risk is LOCAL, and the order is a direct act. Its own acts are one script and two TCP-connect measurements, which
is the class OA-e-6 measured at. The host change (the rule apply) is Andrew's admin act, carded outside this order,
so the order changes no world state. The issuer first read the class as WORLD. The pipeline gate's no-round limb then
refused a round-less WORLD addendum, and that refusal does not honour an override. Re-reading the class from the
order's own acts gives LOCAL, consistent with OA-f-1..f-9 (R2-A1..A7). The close is the issuer's one real run: AC3
after the apply.

**The phases:**
- **Phase 1 (at the cut):** AC1 and AC2. AC3 reads FAIL until the apply, and the order stays open.
- **The apply:** Andrew's admin act, carded to `0.0.0_AB_MSTR~Z` with the CTO's citation (R2.2, isolation design R1
  class). He runs `wall-dapi-8194.ps1` elevated from r2-dev, or from PROD after G-PUSH. The ruling places it in the
  same sitting as G-PUSH.
- **Phase 2:** respawn slot ~25 for AC3.
- **Close:** the item-0 close run waits on AC3 PASS (R3).

**If AC1 reads LOOPBACK-EXEMPT,** the CTO re-rules the mechanism (a raw WFP filter), and this order is amended before
any apply.

The `C:\blp\DAPI` `BUILTIN\Users FullControl` ACL is the CTO's surfaced item, owned by `0.0.0_AB_MSTR~Z`. It is not in
this cell.

**SPAWN:** at the cut. Slot `~25`, worktree `/c/tmp/oa-25`, `--nested opal_ai=e69acf7`. The Terminal was measured up
(8194 listening) at the cut tick.

Dry-run at base (main tree CLOUD, `OA_F10_REF=e69acf7` for AC2):
- f10.AC1 base: FAIL as expected (`F10_FALSIFIER.json absent`).
- f10.AC2 base: FAIL as expected (`wall-dapi-8194.ps1 absent at e69acf7`).
- f10.AC3 base: FAIL as expected (`live 8194 block rules matching an account SID: 0 of 2; F10_ACCEPTANCE.json absent`).
  The live-firewall read ran clean and returned 0.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
