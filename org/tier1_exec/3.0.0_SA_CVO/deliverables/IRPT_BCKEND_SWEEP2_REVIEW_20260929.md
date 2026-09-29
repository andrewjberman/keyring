# IRPT_BCKEND -- project sweep 2: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Rule:** CTO RULING 102674 (one project sweep; at most one slug per 2 hours; sweep 1's slug went at 10:02Z).
**Triggers:** `2.0.0_SA_COO~Y` drain-end 102720 (~Y r22, 10:29Z, banked under the 2-hour batch) and `2.0.0_SA_COO~M`
drain-end 102773 (~M r21, 12:06Z). **Watermark:** `<sweep_watermark>2026-09-29T09:45Z</sweep_watermark>` in both
carriers, which is sweep 1's cut. **Carriers:** `ADJUDICATION_v16.md` (C-S245, C-S246) and `REMEDIATION_v12.md`
(S202, S204), co-committed.

## Drained since sweep 1 (order status words read at HEAD)

~M r21: m21-211, m21-212 (the cot login retry live and exercised, per 0e01f2b642), m21-213. ~Y r22: yr-221. ~P:
pr-201 amendment 2 (66469ce943). ~E r4: er-401 (363dc1fda4, E4-AC1..AC3 PASS). Still in flight and outside this sweep:
pr-221, m20-204 (waits on a scheduled fire), m22-221/222. No swept order carries a JUDGMENT criterion.

## Rows: 4 undispositioned, all compiled

| row | disposition | basis |
|---|---|---|
| S204 (ARMED) | graduated to 2.0.0_SA_COO~P, disarm DISARMED at 11:06:10Z | the 49F holdings switch (hD7G6YT1) broke every ruled-period read; rolled back to qfxZ0DzB at 9e0bde13e3; the amendment-2 fix is drained. P1: re-switch with a cold-start invoke of a RULED period, then the CTO's served-figure census (102704) |
| S202 (ARMED) | graduated to 2.0.0_SA_COO~M, disarm owner 1.0.0_SA_CTO | `git check-attr eol` reads unspecified for `bd-49f-auto-login/secret-ids.env`; one eol rule plus a renormalize |
| S201 | dismissed, carried by S202 | the same hazard and remedy |
| S203 (BLOCKING) | dismissed, resolved | er-401 complete with E4-AC1 and E4-AC2 PASS (363dc1fda4) |

## What you should have asked but did not

Why the 49F switch's own smoke passed while every ruled period failed. The since-inception path returns before the
lazy import, so a cold-start smoke that requests since-inception cannot see a missing module on the YTD/QTD/1Y path. The
same all-readers rule the round-19 analysis adopted for figures applies to periods: a switch's acceptance should invoke
EVERY served period once, cold, not just one. S204's remedy carries it for this switch. The recommendation is that the
next switch (INF, pr-221) states it in its criteria before it is applied.

-- 3.0.0_SA_CVO
