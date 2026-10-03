# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 20:1xZ-21Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 20:1xZ-20:2xZ | IRPT_BCKEND S308 (CTO batch 228) | the export render's "names no selection" | root cause: the render host's PRINT_QUERY_KEYS (render_export.cjs:83) drops account/version; PROD's PrintEntry already accepts them (served asset read). Re-pointed to ~P (batch 229); no promote owed | DRIVE FORWARD (routed) |
| 20:2xZ-20:3xZ | IRPT_DASHBD row S24 (the CVO) | 557862f1's blind pin and Loading hang | the tab's own PATH A read skips only on its OWN served dashboard; component pin in both directions; LANDED portal `f2d2f17c`; row S25 disarms S24 | DRIVE FORWARD |
| 20:3xZ-20:5xZ | IRPT_BCKEND Y-5 V1 (~Y) | Aproxy live | run 1: upload refused UNAVAILABLE/UNEXPECTED (no firm chosen). Run 2 (Cottonwood client): UP-852105aa..., NEEDS_CORRECTION, but the finding's value is null so no proxy box (~Y owns the fix) | DRIVE FORWARD (routed) |
| 20:4xZ-20:5xZ | P-2 leg V, R1 (~P) | export ****0090 | accepted exr_357f26fa...; RENDERING, then a receipt read HTTP 500 via the local proxy; ~P traced the render to S311 | DRIVE FORWARD |
| 21:0xZ-21:1xZ | IRPT_BCKEND S311 (CTO batch 231) | the frozen print's manifest read | a frozen print reads the series alone; LANDED portal `1f42eb08`; DEV head sent to 0.0.0_AB_MSTR for the same-window promote | DRIVE FORWARD |
| 21:1xZ | DSGN_IRPTV1 (FAST) | R1's raw failure text | a failed receipt read is worded for a person; committed `cbf41e6e`, held off DEV until the promote of 1f42eb08 is done | DRIVE FORWARD (held) |

## Notes

- The UI-walker was armed four times this hour (stop check aside), with ARM and DISARMED sent to 0.0.0_AB_MSTR each
  time and each disarm proving the login refused.
- portal DEV CI was RED from site Z's round 29 (one ESLint error) when 1f42eb08 landed on it. The promote waits for that
  fix and a green CI.

## Open

- The same-window promote of 1f42eb08, then ~P's re-dispatch of the 49F export.
- cbf41e6e lands on DEV after that promote.
- ~Y: the NAME_PROXY finding must carry its ticker. Aproxy re-fires on ~Y's word.
- The print's bundle reference on the face: put to Andrew.
