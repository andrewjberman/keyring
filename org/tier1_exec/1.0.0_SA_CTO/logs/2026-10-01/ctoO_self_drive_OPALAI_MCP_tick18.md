# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 18 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** the inter-tick acts 19:3xZ-20:2xZ, and tick 18 (20:24Z). Cron 84d0ab03.
**state:** ARMED

## Andrew-direct received (at this terminal)

1. ~19:3xZ: *"lets start with 1., what do you need"* (act 1, the 8194 elevated run). I read the script in full at
   r2-dev @eeca5ca7d1 (blob b60f67b1) and ran `-Plan` (rc=0, 2 well-formed lines, 0 existing rules). Then I gave him
   the one elevated command. He replied: *"done"*.
2. ~19:5xZ: *"i had turned it off to save bandwidth bu tyou can sign in"* (the Bloomberg Terminal).

## Driver acts

- **8194 wall applied** by Andrew, elevated. Read-back here: 2 of 2 rules live.
  - Each rule is Outbound Block TCP/8194, RemoteAddress 127.0.0.0/8, LocalUser SID -1007 (Opal_Agent) and -1008
    (Opal_MSP), enabled.
  - Routed to `2.0.0_SA_COO~AI` (20261001T194032Z).
- **Terminal signed in** per `integrations/bloomberg/READ_HERE.md` section 2.
  - `--check` OK.
  - Fill screenshot verified: a 12-character login and 9 masked dots, both matching the fingerprint.
  - ONE submit (ledger: 27 attempts in total).
  - `bloomberg_health` ok, and a real read returned SPY PX_LAST 764.78.
  - The AC3 respawn was routed (20261001T200055Z).
- **AC3 read** (`2.0.0_SA_COO~AI` msg 28054, F10_ACCEPTANCE.json, drained @1552d46a70, row Z-W25-S3).
  - Opal_Agent: 8194 OPEN, 8790 OPEN.
  - Opal_MSP: 8194 OPEN, 8790 OPEN.
  - operator: 8194 OPEN.
  - **The falsifier FIRED: Windows per-user Firewall rules are LOOPBACK-EXEMPT here; the rules are live but inert.**
  - **Precedent defect, surfaced:** I cited the `codex_sandbox_offline_block_loopback_*` rules (SID -1005) as R1's
    precedent. Read at 20:2xZ, they have the identical shape. That precedent was SHAPE ONLY, never proven to block,
    and those rules are likely inert too. The question is with the CRO (question 4).

## Calls ruled

| call | ruling | reason / route |
|---|---|---|
| Remove the inert rules or leave them (28054) | **LEAVE.** They are removed or kept in the same elevated sitting as the WFP install, and recorded as INERT on the order and the row. | Removal needs another elevated sitting. Inert rules harm nothing once they are labelled. Routed to `2.0.0_SA_COO~AI` 20261001T202920Z. |
| The mechanism after LOOPBACK-EXEMPT | **DESIGN FORK -> `4.0.0_SA_CRO~O` research** (20261001T202908Z). R2.1 already names the raw WFP filter; I re-rule when the research lands, and then `2.0.0_SA_COO~AI` cuts ONE cell (installer, -Plan, AC3). | Unknown: whether a WFP block in its own sublayer overrides the firewall's loopback permit, and the minimal non-vendor installer. |

The item-0 close run stays HELD, and the interim (no DAPI client in the runtime) holds.

## Measurement (20:24Z)

- **Inbox:** 0 unread at the tick. 28054 read and acked since.
- **Sequence:** OPLGTW and MCPINDEX PLACED at stage 0 with no flags. OPALAI, MCPMSP and MCPORTAL UNPLACED.
- **Ports:** 8194 LISTENING (bbcomm). 8790 has 0 listeners; the worker stopped the view server.

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 8 of 67 |
| NFRA_MCPINDEX | active | EXECUTING | 53 of 86 |
| NFRA_OPALAI | active | EXECUTING | 6 of 37 |
| NFRA_MCPMSP | active | EXECUTING | 7 of 24 |
| NFRA_MCPORTAL | active | EXECUTING | 6 of 18 |

## Acts only Andrew can perform (each with its citation)

1. **The Terminal sign-out**, back to his bandwidth setting. AC3 has read. It is his machine-use choice ("i had
   turned it off to save bandwidth").
2. **The WFP filter install, elevated**, once the cell is cut (isolation design R1 class: host administration; this
   fabric's seats run non-elevated). It is not yet ready.
3. **opal_ai DEV fast-forward** fd8ab8a -> 9c0a80b (PRD "DEV/PROD release on Andrew's word"). REC: approve.
4. **MCPORTAL G-CLOSE with Alyssa**, at a time he sets (staged @154894312f).
5. **G-W:** the R20 acknowledgement for `platinum/advi` (CLAUDE.md rule 30).
6. **r6.J1:** Alyssa's Schwab cold run.
7. **An invitation to the Research Team Meeting series** (calendar membership; OG-tx-2's fourth meeting).
- **Done this tick:** the 8194 elevated run (the old act 1).

## Completion test

NOT DONE: 0 of 5 complete.
- REACHABLE 2: OPLGTW and MCPINDEX.
- UNREACHABLE 3:
  - MCPORTAL: G-CLOSE.
  - OPALAI: the WFP mechanism (CRO research, then a cell, then Andrew's elevated install), then the close run.
  - MCPMSP: G-MSPID, deferred.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| PowerShell | `wall-dapi-8194.ps1 -Plan` at eeca5ca | rc=0, 2 lines | before handing over the elevated command |
| PowerShell | `Get-NetFirewallRule` + filters, read-back | 2 of 2 live, exact shape | after Andrew's run |
| bbg_credentials / bbg_signin | `--check`, `-Phase fill`, `-Phase submit` | ONE attempt, listener up | fill screenshot verified first |
| bloomberg MCP | `bloomberg_health`; `reference_data` SPY | ok; 764.78 | a real read, not only the port |
| PowerShell | `codex_sandbox_offline_block_loopback_*` read | same shape as ours | the precedent was shape-only |
