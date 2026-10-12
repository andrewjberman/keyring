# IRPT_ANLREQ -- decomposition, round 15, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO ruling `1.0.0_SA_CTO~DELL2` msg 6019 (2026-10-11 ~22:5xZ), on row `DSGN_IRPTV1-D2-W65-S1`: "one cell now, not after the
service release: regenerate the wire TYPE only, the optional member declared and sent by nothing. The form sending it still waits
for 2.0.0_SA_COO~P2's release. A portal candidate to me with the suite at 0 failing." No PRD addendum; the endpoint is unchanged.

**Why a round of its own while round 14's last order (`TO-AR-y-145`, a read) is still running:** the ruling says now; the cell
shares no file with any round-14 cell (round 14's portal cell is on DEV; its open order writes only a census record); and the two
tests it clears fail on EVERY portal head, so every other lane's suite reads 2 failing until it lands.

**Thread:** FWD-1 is not live. This cell repairs the portal's vendored copy of a contract the trunk has already moved.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-151` | CTO msg 6019 | the portal's generated wire type for the analysis submission request declares the optional `commentary_requested`, by running the generator and committing exactly what it writes; nothing sends the member | portal `src/pages/InvestorReporting/contracts/wire/` (generated files only) | LOCAL |

## Not cells

- The form SENDING the member: parked until `2.0.0_SA_COO~P2`'s release of the submission's member is live and read (CTO msg 5864).

## Edges and chains

- One cell. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one cell.
