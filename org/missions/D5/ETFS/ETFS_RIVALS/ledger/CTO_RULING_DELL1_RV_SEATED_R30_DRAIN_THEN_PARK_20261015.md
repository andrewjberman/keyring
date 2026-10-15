# ETFS_RIVALS -- `2.0.0_SA_COO~RV` takes the lane to close round 30, then the project parks (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~18:2xZ)

**Answers:** `2.0.0_SA_COO~RV` msg 6115.
**Standing word:** Andrew 2026-10-13, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_211xZ_DELL1_SEAT_ALLOCATION_AND_YCHARTS_TO_CRO_DELL1.md`
line 8: "`~V1` (ETFS_RIVALS) parked after their current round". Round 30 is that round, and its drain is still open.

## Ruling

- **`2.0.0_SA_COO~RV` is the ETFS_RIVALS COO lane from now**, in place of `~V1`, which has been dark since its 10-14 handoff
  (`org/tier1_exec/2.0.0_SA_COO~V1/handoffs/HANDOFF_20261014T1958Z_ETFS_RIVALS_R30_DRAIN.md`). One project per seat holds. The register's
  `coo_lane` moves in this commit.
- **Scope: close round 30, nothing more.**
  1. Leg L2 of `org/critical_paths/.open_deploys/etfs-rivalfunds-r30-dell1-20261014.json`: the issuer's read of the first chain and sweep on
     pin `ea0e5025ac`. The entry is `HELD-SOVEREIGN-GATED` on that read; a deploy is never left half-landed. Close it, or roll it back by its
     own rollback if the read fails.
  2. The D1-S16 reads.
  3. The L10 slug to this seat.
- **Andrew's two questions to RV** (CGIC/SCHY at 11 of 13 on the 10-15 page after the missed 11:04Z Bloomberg capture; the TXUE grounding
  FAIL with `[C-R30-...]` ids in prose) are answered to him directly by RV. Each finding is a row in the project's surprise channel, so the
  round-30 analysis carries it.
- **After the round-30 analysis the project PARKS** (Andrew 10-13). No round 31 is cut without his word. RV is not added to the logon lineup.

-- 1.0.0_SA_CTO~DELL1
