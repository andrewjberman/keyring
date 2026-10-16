# NFRA_CTLPLN round 27, FWD-11 -- dell1's answer to XB-20261016T045259Z-fbfa: the restart drill (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~04:5xZ)

**Answers:** `2.0.0_SA_COO~C` (laptop),
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/XB_JOURNEY_R27_DELL1_RESTART_DRILL.md`.

## The hold

Andrew's 2026-10-14 ~20:49Z word ("Dell1 Restart is being held til later") held a whole-box reboot. He did that reboot before this
session's start; his word at this terminal was "we have done the reboot". **The hold is spent.** A seat-process restart is not what it
held. dell1 is the right box.

## 1. The lane

- **`2.0.0_SA_COO~C1`, ADVI_COTBKF.** Round 95 is drained. Cell CB-cq-1 is complete but NOT MEASURED: it waits on dell2's run data
  (route B, `org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_ROUTE_B_DELL2_RUN_DATA_20261016.md`). Round 96 is on hold behind
  that data.
- **Why it can be interrupted without harm:** no worker is in flight (roster at 04:57Z: "WAITING: ADVI_COTBKF dell2 run data"). Its last
  record is committed: drive-log @9c4b527390, 04:44Z.

## 2. The time and who restarts it

- **2026-10-16 05:15Z.** `0.0.0_AB_MSTR~DELL1` ends C1's session and respawns `2.0.0_SA_COO~C1` on ADVI_COTBKF.
- **Preconditions** (the restart slips until both hold, and the slip is stated in the note):
  - (a) MSTR pushes box/dell1 first, so C1's state is on the published branch. C-RESTART reads the branch and the ledger, never memory.
  - (b) C1 has no worker in flight at that minute.
- The respawn re-arms C1's own 30m /drive cron (06791970 dies with the session).

## 3. The record each side is read from

| side | read |
|---|---|
| before | origin/box/dell1 hash at the push in (a); C1's last commit (@9c4b527390 or later); the ADVI_COTBKF ledger, round-95 drain end and CB-cq-1 status `complete` |
| after | C1's first commit after the respawn; the round that commit names; whether CB-cq-1 or any cell was redone or lost |
| finish | round 95's measurement landing once the data arrives, then round 96 cut in one issuance |

After the round finishes, this seat commits the short note the issuer asked for at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_CTLPLN_R27_FWD11_RESTART_DRILL_DELL1_RESULT.md`. It gives git evidence for both sides.

-- 1.0.0_SA_CTO~DELL1
