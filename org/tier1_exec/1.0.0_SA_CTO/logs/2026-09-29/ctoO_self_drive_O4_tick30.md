# /self-drive O4 -- ticks 27-30 (1.0.0_SA_CTO~O, site Z, 2026-09-29 13:13Z)

- **State:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md` @7612f001c4
- **Cron:** 0eef1ea2
- **Why this log:** the one-hour floor since tick 26 (@de6978f41c).

## Measured (13:13Z)

- Inbox: 0 unread.
- Sequence check: no flags for any of the 4 projects.
- Open task orders: 13 of 180.

  | project | open | total |
  |---|---|---|
  | OPLGTW | 5 | 54 |
  | OPALAI | 4 | 35 |
  | MCPORTAL | 2 | 18 |
  | MCPINDEX | 2 | 73 |

- Completion test: 0 of 4 complete; 4 REACHABLE.
- Ticks 27, 28 and 29 were quiet. Their lines are in `org/mcp/drive_ticks/1.0.0_SA_CTO~O.md`.

## Since tick 26

- **MX-t-11 SUPERSEDED** by 2.0.0_SA_COO~MI at ~12:0xZ.
  - Reason: platinum/advi widening is NOT YET, under the ruling Andrew adopted, and DATA_CATALOG.yaml:32 reads
    "WIDENING IS ANDREW-ONLY".
  - No work was started and no path was touched. The cell is carried to the round-4 analysis.
- **The ETF patch is still unapplied on the laptop.**
  - remediations.json holds 0 ETFS_CANON rows, and origin/CLOUD is still 15655f4a25.
  - This tick I sent a status ask to 0.0.0_AB_MSTR~Z for relay to the laptop 1.0.0_SA_CTO.
  - MX-t-10 waits only on the patch.

## Calls

No open calls in scope (ticks 27-30).

## Andrew acts (cited)

- G-C: create one unprivileged M365 test user (tenant admin plus licence). OG-g-1 waits only on this.
- G-ACCT: step 5, the setup-token sign-in (his login), and step 6, one MFA.
- MCPORTAL G-2ND: the Opal Bloomberg sign-in.
- MCPORTAL G-CLOSE and OPLGTW G-D: the person-operated runs.
