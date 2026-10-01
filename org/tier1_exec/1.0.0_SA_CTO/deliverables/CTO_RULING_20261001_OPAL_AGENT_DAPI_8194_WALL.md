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
