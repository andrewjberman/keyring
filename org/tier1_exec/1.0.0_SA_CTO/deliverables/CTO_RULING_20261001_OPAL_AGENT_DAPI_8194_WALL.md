# CTO RULING 2026-10-01 ~12:0xZ -- Opal_Agent is walled off Bloomberg DAPI 8194 by a per-user network deny (NFRA_OPALAI)

**Seat:** `1.0.0_SA_CTO~O`, `/self-drive OPALAI_MCP_SITEZ` (arming record @80102ed73d). **Class:** DESIGN FORK, ruled
on research. **Question:** `2.0.0_SA_COO~AI` msg 27790. OA-e-6 (@5abe4f6c86) measured Opal_Agent reaching 127.0.0.1:8194
(DAPI) and 8790 (the view server), TCP connect only. **Research:** `4.0.0_SA_CRO~O` msg 27806,
`org/tier1_exec/4.0.0_SA_CRO~O/deliverables/OPAL_AGENT_DAPI_8194_WALL_RESEARCH_20261001.md` @5d804ea419.

## Why the tool boundary is not enough (from the research, measured as the operator)

- DAPI's identity is the signed-in Terminal user. Our client passes no `AuthOptions`
  (`integrations/bloomberg/mcp/blp_client.py:53-59`), so a second OS account on 8194 draws on the SAME Terminal user's
  data limits. Nothing at the API refuses it.
- G3 matches MCP tool NAMES only. The runtime keeps a shell; `C:\Program Files\Python314` is runnable by Opal_Agent;
  `C:\blp\DAPI` holds a readable `blpapi3_64.dll`; outbound egress is not walled. So "no blpapi in the runtime" holds by
  ABSENCE, not by a wall.

## R1. The wall -- ADOPTED

A Windows Firewall rule:
- Outbound, Block;
- `LocalUser` = Opal_Agent's SID `S-1-5-21-29065828-778925147-1918870939-1007`;
- RemoteAddress `127.0.0.0/8, ::1`;
- RemotePort **8194 only**.

Precedent: the three live `codex_sandbox_offline_block_loopback_*` rules on this box, the same LocalUser-SDDL shape.
**8790 stays open**: the view server is Opal_Agent's sanctioned Bloomberg path (isolation design Plane 2, item 4).
**Opal_MSP** (SID `...-1008`, the NFRA_MCPMSP runtime account) gets the identical rule, because it is an agent-running
account on the same box.

## R2. Order of acts

1. **The falsifier first (free, no host change).** A Codex seat on this box, inside its OFFLINE sandbox, runs
   `Test-NetConnection 127.0.0.1 -Port 8194`, with the same command outside as the control.
   - Refused inside and open outside: the Firewall-rule mechanism is proven; go to step 2.
   - OPEN inside: loopback is exempt here. The deny becomes a raw WFP filter (own sublayer, higher weight, elevated
     installer); this seat re-rules the mechanism on that measurement.
2. **The apply is an admin act on Andrew's account** (isolation design R1 class: OS-account and host administration;
   this fabric's seats run non-elevated). It is listed for him with that citation. It is NOT a decision.
3. **Acceptance:** E6 re-run with three arms: Opal_Agent -> 8194 refused; Opal_Agent -> 8790 open; Opal Bloomberg ->
   8194 open. For Opal_MSP, the same two arms on its own SID.

## R3. Placement on the NFRA_OPALAI path

The wall is a **precondition of the cutover's item-0 close run**. The Analyst does not run live until the E6 re-run
reads refused on 8194. The cutover already waits on Andrew's G-PUSH, so this adds no delay if he applies the rule in the
same sitting. `2.0.0_SA_COO~AI` cuts the falsifier, the apply runbook and the E6 re-run as ONE cell.

## R4. Kept and not pursued

- **G3 stays** as the second layer on the sanctioned MCP path.
- **No API-level control:** DAPI has none to configure; per-user identity is a different Bloomberg product (a
  purchase).
- **Fallback only if the deny is refused:** put `python`, `pip` and `java` in G2, or drop the shell from the runtime.
  It is weaker, because it enumerates clients.

## Surfaced, not chased (owner named)

`C:\blp\DAPI` is `BUILTIN\Users FullControl`, so a non-admin account can replace the Terminal's DAPI binaries. The
box's operator, `0.0.0_AB_MSTR~Z`, owns it. Told in one line.

## R5. Re-ruled after the AC3 falsifier -- 1.0.0_SA_CTO~O, 2026-10-01 ~21:0xZ

**Measured:** `F10_ACCEPTANCE.json` @1552d46a70 (row Z-W25-S3). With both R1 rules live, 5 of 5 arms read OPEN, so
the R1 Firewall rules are LOOPBACK-EXEMPT and inert. R1's precedent, the `codex_sandbox_offline_block_loopback_*`
rules, was SHAPE ONLY and is also ineffective (openai/codex #48856 and #49840, the same build 26200). **Research:**
`4.0.0_SA_CRO~O` @63a9b6da27, `WFP_LOOPBACK_8194_WALL_RESEARCH_20261001.md`. A max-weight boot-time loopback permit
sits in the Firewall's own sublayer, and under Microsoft filter arbitration a block in a higher-priority sublayer is
final.

**R1 is SUPERSEDED as the mechanism. ADOPTED: a raw WFP filter pair.**
- One persistent own sublayer (`FWPM_SUBLAYER_FLAG_PERSISTENT`, weight 0xFFFF).
- Two persistent BLOCK filters, at `FWPM_LAYER_ALE_AUTH_CONNECT_V4` and `_V6`. Each ANDs three conditions:
  - `ALE_USER_ID` = SDDL `O:LSD:(A;;CC;;;<Opal_Agent SID>)(A;;CC;;;<Opal_MSP SID>)`, with the SIDs resolved at run time
    and never typed;
  - `IP_REMOTE_PORT` 8194;
  - `FLAGS` ALL_SET `IS_LOOPBACK`.
- The installer is one PowerShell script with `Add-Type` P/Invoke to `fwpuclnt.dll`: no vendor tool and no install.
  It has three modes: `-Plan` (prints, changes nothing), real (elevated, one transaction), and `-Remove` (deletes both
  filters and the sublayer, one transaction).

**One elevated sitting, never two.** The CRO's residual read is folded into the installer's real mode, BEFORE any act:
- It enumerates the ALE_AUTH_CONNECT_V4 filters that permit loopback and prints each one's sublayer and weight.
- **It REFUSES with no action if any such sublayer's weight is >= ours.** Equal weights have no documented order.
- On that refusal the fallback is CRO section 3: deny Bash and PowerShell to the Analyst runtime through machine-wide
  managed settings. This seat rules it on that measurement.

**In the same sitting, after the read-back:** it removes the two inert R1 Firewall rules. They are proven to block
nothing, so removing them changes no behavior, and they must not be read as a wall.

**Authority:** Andrew's "sure" (msg 28000) was for the 8194 wall. The outcome is unchanged and only the mechanism
moves, so the elevated run is his act under that word, listed with this citation.

**Acceptance:** AC3 unchanged (5 arms). Opal_Agent and Opal_MSP read 8194 REFUSED or TIMEOUT, and 8790 OPEN; the
operator reads 8194 OPEN. **Persistence** is a sixth arm read at the box's next NATURAL reboot, never a forced one; it
is not a close precondition. The R3 placement stands: the wall precedes the item-0 close run.
