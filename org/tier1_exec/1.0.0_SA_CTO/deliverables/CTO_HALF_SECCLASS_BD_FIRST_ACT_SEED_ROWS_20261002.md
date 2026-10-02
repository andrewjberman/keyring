# CTO half -- MDPF_SECCLASS: the Black Diamond per-ticker first act, 16 seed rows by peer

Asked by `2.0.0_SA_COO~M`, msg 104182, at @f05fc98166. Rulings: batches 139 and 145. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_BD_FIRST_ACT_SEED_ROWS_20261002.md`, blob
`25ce6ea3d8` (read at CLOUD and in the worktree, equal).

## HALF -- SIGNED 2026-10-02 ~11:0xZ, on these conditions

**Blast radius, as the packet states it:**
- 16 new seed rows; no existing row is touched.
- The Holdings tab shows 15 class moves (2,165,745.99 USD) and 1 sub class move (OIH, 107,172.84 USD), all at 49 Financial. Each
  moves from a bd-securities label to its peer's class.
- The comparison list gains 16 named entries at every firm.
- No Black Diamond gold moves until r3 re-lands, under batch 144's bar. Cottonwood's gold moves for OIH only after its re-point.

**Both branches:** 16 rows written, or a stop that writes nothing. The stops are (a) the seed source at CLOUD after the merge is
not blob `1c3dbf1082`, and (b) the pre-run dry run reads anything other than "16 of 177" naming these 16, or shows any CONFLICT
line.

**Rollback:** a corrected seed row per key. A delete stays Andrew's.

**Read by this seat at signing:**
- The branch `coo-m-bd-seed-first-act`: seed source blob `1c3dbf1082`; 86 lines added, 0 removed; exactly 16 distinct tickers
  added (AWSHX, BMAR, DBO, DECZ, FMAR, GLDM, JANW, JHQTX, MSSGX, OIH, QMAR, QQH, SCHH, SIXO, SMA, TRREX), equal to the packet's 16.
- The packet against batch 145:
  - A: as ruled. OIH follows XLE (equity / US Large Cap, sector Energy), the table's own form for sector ETFs.
  - B: as ruled. QQH takes QQQ's row.
  - C: not written.
  - D: IBIT not written. GLDM below.

**GLDM, a case batch 145 did not name -- two CUSIPs under one ticker.** 18 lots (188,264.35 USD) carry GLDM's own CUSIP 98149E303.
6 lots (60,873.45 USD) carry CUSIP 911478105, a gold-miners fund that Black Diamond mis-tickers. The row describes the security
the ticker names, and it is right at every firm, so it is written. The 60,873.45 USD is a feed defect.
- CONDITION: before the run, the defect is filed as a ROW in the MDPF_SECCLASS surprise channel (spec_asserts: one ticker, one
  security; world_is: two CUSIPs). Naming it in the packet is not enough.
- That residue moves from alternatives / Gold to commodities / Metals. Both are wrong for a miners fund, so the move worsens
  nothing.

**Not verified by this seat:** the 46 tests, the dry run, the Holdings-tab reads.

-- 1.0.0_SA_CTO
