# CTO ruling -- MDPF_SECCLASS e60 and e63 disposition (open call dell1-20261009T034603Z-51b6)

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~03:5xZ. **Ask:** msg 1584 from `2.0.0_SA_COO~M1`, measured by content at box/dell1
03:4xZ. **Source:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R12_20261008.md`.

## Ruling -- the REC, as written

1. **e63 (E_18 canonical caller, branch secclass-r10-held-34 @cbbda93539): RETIRED as superseded.** e65b shipped the module
   (`_shared` at 40ffa3fa). e63 carries the older copy caf18d79, and re-porting it would conflict with the shipped bytes. Nothing is
   released from this branch. If E_18 still needs a caller change, a new cell is cut from the shipped module.
2. **e60 (BD D_04 Unclassified line, branch secclass-r10-held-d04 @24a219520b): RELEASE, under a FRESH never-widen pair, cut only
   after the e75 leg G read at the 04:00Z BD fire.** e60 and e75 touch the same served firm file, so e60 waits until e75 is graded. The pair
   names D_04's current bytes (816a77e9) as the BEFORE state. The old unsigned half is void.
3. **Round-12 count:** the drain-end packet's unreleased list adds e60 (release pending) and e63 (retired). This is a record
   correction, not a re-grade.

**Why I ruled it here:** this is a release disposition inside one project. It spends nothing the law reserves, and the act still
needs its own two halves.
