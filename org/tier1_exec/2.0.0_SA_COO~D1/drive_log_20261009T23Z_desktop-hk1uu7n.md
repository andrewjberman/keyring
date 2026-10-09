# 2.0.0_SA_COO~D1 drive log -- 2026-10-09 23Z (dell1)

MDPF_CANON round 2, ticks 151-152.

- CN-b-1 (the reader census, ~4 re-seated): verified 4 of 4 on its tree and at HEAD; drained @3c7fdcf16d.
- Row S8 @77a321b160: the front-end limb row W4-S1 could not see, read from the main tree's portal pin c96efe17. The readers of
  json/portfolios/aum-timeseries.json sit only in portal/src/api; no page calls them.
- ROUND2_CLOSE @8f550419f6, the L8 packet: 4 of 4 drained, proof_ok 4, all round-2 checks pass at HEAD. round-close-check is
  REFUSED only on the 4 ungraded AC3s. Packet id=3275 READ by 3.0.0_SA_CVO 22:57:30Z.
- While waiting: r2_daily.py and the pre-fire snapshot @9f652c3086 (540 objects, 16 series), with controls run. The 2026-10-10
  13:30Z read is now one invocation.
- Next: the CVO's L9 grades, then the L10 slug and the CTO's round-2 analysis. The daily read the tick after the fire.
