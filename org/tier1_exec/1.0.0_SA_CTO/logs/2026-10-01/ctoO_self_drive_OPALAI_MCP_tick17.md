# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 17 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** the inter-tick acts 18:3xZ-19:2xZ, and tick 17 (19:26Z). Cron 84d0ab03.
**state:** ARMED

## Since tick 16

1. **The Tax SMA gateway release is CLOSED** (`0.0.0_AB_MSTR~Z` msg 28033).
   - This seat signed its CTO half at ~18:3xZ: `CTO_NEVER_WIDEN_HALF_OG-tr-1_20261001.md`.
   - **Verified here:** the S3 `opal-gateway-latest` `git-ref` reads `3a7d6a7dc85fe3c54a4b63b27b59055abc9adca7`
     (LastModified 18:49:35Z).
   - Public no-bearer probes: `/ms/taxsma-workbook` 401 and `/hx/mail` 401.
   - The ledger closed at 18:57Z, 4 of 4.
   - The priority hold is lifted, and the TAXSMA exclusion is back in force.
2. **NFRA_OPLGTW round 12 is terminal** (`2.0.0_SA_COO~O` msg 28041, project.json @9a3cb68).
   - The issuer re-grade passed: tt.AC2, tr.AC1 4 of 4, and tr.AC2.
   - New rows:
     - Z-S41 (ARMED, COO): the Tax route's `_OTHER_ROUTE_BEARERS` tuple fix, carried into the next gateway release.
     - A carrying note: the shipped template refuses without `OG_TAXSMA_WORKBOOK_IDENTITY` in the deploy shell. That
       holds until the value moves host-side; it goes to the next enrichment beside Z-S32 and Z-S34. The template fails
       closed, so no act is needed here.
3. **OG-tx-2 live read** (msg 28042, @c8514e1447, row Z-S42).
   - As Andrew, on 3a7d6a7dc8, the Morning Meeting, OCIO IC and Asset Management IC each read complete and attributed
     (last cue within 4.1 s of endDateTime), with Andrew an invitee, not the organizer.
   - The Research Team Meeting returns 403/3003; Andrew is not invited to that series.
   - **G-TEAMS-TX DROPS** (no tenant-setting error appeared), which confirms the tick-16 provisional removal.

## Calls ruled (driver, on its own rec)

| call | REC / RULING | reason | routed |
|---|---|---|---|
| OG-tx-2: how the fourth meeting (Research) is reached -- (a) Andrew invited to the series, or (b) the application route as an analysis item | **(a)**; (b) NOT an analysis item, and it re-opens only if the invitation is refused | (a) needs no code and no widening. (b) is a tenant-wide transcript read: it needs admin consent and an application access policy, and it breaks the bound-identity design that 3 of 3 just confirmed. AC1 grades 3 of 4 and FAILS honestly; no amendment. The 403 on a meeting Andrew is not invited to is the correct boundary, and it is already the negative arm. | reply to `2.0.0_SA_COO~O` 20261001T192318Z; carried to the OPLGTW L10 analysis |

This was not routed to the CRO as a design fork: the evidence was in hand (the record @c8514e1447 and the spec's own
fallback text), and the rejected branch is a widening, not a design alternative.

## Measurement (19:26Z)

- **Inbox:** 0 unread. Read and acked since tick 16: 28033, 28041, 28042.
- **Sequence:** NFRA_OPLGTW and NFRA_MCPINDEX are PLACED at stage 0 with no flags. NFRA_OPALAI, NFRA_MCPMSP and
  NFRA_MCPORTAL are UNPLACED, so their own directive governs them.
- **Served:** opal-gateway 3a7d6a7dc8.
- **NEVER-2:** census over 115 worktrees (Python porcelain).
  - The shared tree holds one in-scope sentinel, `nfra-mcpindex-r6-bd-merge-retire`, by design.
  - Every other hit is an inherited copy of `bd-playwright-strip`, `r6-bd-merge-retire` or `r5-rollback-4ce7946`, on
    a branch cut while that sentinel was on CLOUD. These are not live deploys.
- **Active commitments (24 h):** one in-scope line, the OA-f-10 cut (12:16Z). That work has since landed (AC2 PASS
  @c1d3fd8ef3).

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 8 of 67 |
| NFRA_MCPINDEX | active | EXECUTING | 53 of 86 |
| NFRA_OPALAI | active | EXECUTING | 6 of 37 |
| NFRA_MCPMSP | active | EXECUTING | 7 of 24 |
| NFRA_MCPORTAL | active | EXECUTING | 6 of 18 |

## Owed at this seat (event-gated, on CVO slugs)

- The NFRA_OPLGTW L10 analysis. It carries:
  - Z-S32 shape fix and Z-S34;
  - Z-W21-S19 and Z-W19-S13;
  - the C7 text drift and the C7 "/ms structure-only" tension;
  - Z-S41;
  - the deploy-shell identity note;
  - the fourth-meeting reach item.
- The NFRA_MCPINDEX round-6 L10 analysis (REMEDIATION_v5 @c5710a5111: the cot sentinel fix and Z-S74).

## Acts only Andrew can perform (each with its citation)

1. **Re-run the 8194 rule elevated.** It needs his UAC elevation; it is already approved ("sure", msg 28000).
2. **opal_ai DEV fast-forward** fd8ab8a -> 9c0a80b (PRD "DEV/PROD release on Andrew's word"). REC: approve.
3. **MCPORTAL G-CLOSE with Alyssa**, at a time he sets (staged @154894312f).
4. **G-W:** an R20 acknowledgement for `platinum/advi` (CLAUDE.md rule 30, "a deliberate departure is an R20 register
   entry Andrew acknowledges").
5. **r6.J1:** Alyssa's Schwab cold run.
6. **NEW: be invited to the Research Team Meeting series** (or have its organizer invite him). This is a calendar
   membership only he or the organizer holds, and it is the one path to OG-tx-2's fourth meeting.
- **Removed:** G-TEAMS-TX (the live read confirmed it).
- **Deferred by his word, not listed:** G-MSPID and G-2ND.

## Completion test

NOT DONE: 0 of 5 complete.
- REACHABLE 2: OPLGTW and MCPINDEX.
- UNREACHABLE 3:
  - MCPORTAL: G-CLOSE, at Andrew's time.
  - OPALAI: the 8194 elevated run, then the close run.
  - MCPMSP: G-MSPID, deferred by Andrew ~17:4xZ.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| aws (read-only) | `s3api head-object` on the opal-gateway artifact | git-ref 3a7d6a7dc8 | independent of the MSTR report |
| curl | public no-bearer GETs | 401 / 401 | the Tax route is mounted and guarded |
| sequence-check | `--project` x5 | 2 PLACED, 3 UNPLACED, 0 flags | |
| git worktree census | Python porcelain, 115 worktrees | 1 live in-scope sentinel (by design) | inherited branch copies excluded |
