# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 19 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** the inter-tick acts 20:3xZ-21:2xZ, and tick 19 (21:23Z). Cron 84d0ab03.
**state:** ARMED

## Since tick 18

1. **CRO research landed** (`4.0.0_SA_CRO~O` msg 28058, @63a9b6da27). A block in our own higher-priority WFP
   sublayer beats the max-weight boot-time loopback permit, which is what defeats same-sublayer Firewall rules
   (openai/codex #48856, build 26200). The installer is `Add-Type` P/Invoke. The Codex offline loopback block is
   ineffective.
2. **RE-RULED: R5 @9d6fbe3e97.** Mechanism: a raw WFP filter pair in its own persistent sublayer at weight 0xFFFF.
   - The residual read is folded into the installer as a refuse-before-act check, so there is one elevated sitting.
   - The inert R1 rules are removed in that same sitting, after the read-back.
   - Persistence is read at the box's next natural reboot; it is not a close precondition.
3. **Cell cut and built** by `2.0.0_SA_COO~AI`: OA-f-11 issued @8fb30778c0. Worker ~26 built
   `wall-dapi-8194-wfp.ps1` (nested 0fb3fcb694); AC1 PASS; drained @356a20ff3d. READY message 28063.
4. **This seat's review before handing the elevated command to Andrew:**
   - I read all 458 lines; blob b032cdef verified.
   - The x64 struct-size guard (FILTER 200 / COND 40) refuses on a wrong layout.
   - The FWP constants match the SDK (BLOCK 0x1001, SECURITY_DESCRIPTOR_TYPE 14, FLAGS_ALL_SET 6, IS_LOOPBACK 0x1).
   - Install and remove each run in one transaction, and R1 is removed only after every VERIFY is OK.
   - `-Plan`: rc=0, 1 SUBLAYER line and 2 FILTER lines (SIDs -1007/-1008). Unelevated real mode: rc=3, refused.
5. **Command handed to Andrew** at this terminal, with its output tee'd to `C:\opal-elev\wfp_8194_run.txt`. **Not yet
   run** at 21:23Z (the file is absent).

## Calls ruled

| call | ruling | reason |
|---|---|---|
| 8194 mechanism after LOOPBACK-EXEMPT | **R5: WFP filter pair** (@9d6fbe3e97) | CRO research @63a9b6da27; Microsoft filter arbitration makes a block in a higher-priority sublayer final |
| OA-f-11 permit-scan scope (28063): it counts only loopback-conditioned permits | **ACCEPT as scoped** (reply 20261001T212125Z) | Loopback-conditioned permits are the documented failure. An unconditional hard permit in a higher sublayer would be a whole-layer allow, and AC3's 8194 arm catches it. |

## Measurement (21:23Z)

- **Inbox:** 0 unread. 28058 and 28063 read and acked.
- **Sequence:** OPLGTW and MCPINDEX PLACED at stage 0 with no flags. OPALAI, MCPMSP and MCPORTAL UNPLACED.
- **8194:** 0 listeners. Andrew has turned the Terminal off again; AC3 needs it, and he gave his word to sign it in
  ("you can sign in").
- **Open TOs (unchanged from tick 18 apart from OA-f-11):** OPLGTW 8/67, MCPINDEX 53/86, OPALAI 7/38, MCPMSP 7/24,
  MCPORTAL 6/18. All five are `active`, EXECUTING.

## Next at this seat

When `wfp_8194_run.txt` lands:
1. Read it.
2. Sign the Terminal in (READ_HERE section 2).
3. Route the output to `2.0.0_SA_COO~AI` for AC3.
4. Hand the Terminal sign-out back to Andrew.

On a `WFP: REFUSE PERMIT-WEIGHT`, rule the CRO section-3 fallback.

## Acts only Andrew can perform (each with its citation)

1. **Run `wall-dapi-8194-wfp.ps1` elevated** (R5; his "sure" for the 8194 wall, msg 28000; isolation design R1 class).
   The command was given at this terminal.
2. **opal_ai DEV fast-forward** fd8ab8a -> 9c0a80b (PRD "DEV/PROD release on Andrew's word"). REC: approve.
3. **MCPORTAL G-CLOSE with Alyssa** (staged @154894312f).
4. **G-W:** the R20 acknowledgement for `platinum/advi` (CLAUDE.md rule 30).
5. **r6.J1:** Alyssa's Schwab cold run.
6. **An invitation to the Research Team Meeting series** (calendar membership; OG-tx-2).

## Completion test

NOT DONE: 0 of 5 complete.
- REACHABLE 2: OPLGTW and MCPINDEX; both await CVO slugs for their L10s.
- UNREACHABLE 3:
  - MCPORTAL: G-CLOSE.
  - OPALAI: the WFP elevated run, then AC3, then the close run.
  - MCPMSP: G-MSPID, deferred.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| Read | `wall-dapi-8194-wfp.ps1` in full (458 lines) | reviewed | before handing an elevated host change |
| PowerShell | `-Plan`; unelevated real mode | rc=0; rc=3 | the refusal path is exercised |
| sequence-check | `--project` x5 | 2 PLACED, 3 UNPLACED, 0 flags | |
