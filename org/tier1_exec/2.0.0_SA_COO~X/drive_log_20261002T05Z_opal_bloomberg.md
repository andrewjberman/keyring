# 2.0.0_SA_COO~X -- /canonical-drive AMGT_CORPUS 30m -- 2026-10-02 05Z (relaunch after the site-Z reboot)

**archetype:** COORDINATE

The seat was relaunched on Andrew's ~04:55Z "go"
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_045xZ_GO_RELAUNCH_SITEZ_AMGT_DEMO_FLEET.md`). The loop was
re-armed on the live LIVE_ARMS row (`1.0.0_SA_CTO~Z` `/self-drive 60m`, which pairs this lane at `/canonical-drive <own
project> 30m`) and on Andrew's ~04:59Z word relayed by `0.0.0_AB_MSTR~Z` (msg 28200, record
`ANDREW_DIRECT_20261002_045xZ_CANONICAL_DRIVE_ALL_COOS_RV_CLOSER_DRIVE_RIVALFUNDS_DEMOABLE_TODAY.md`).

- **Cron:** `21a4937a`, `13,43 * * * *`, `/canonical-drive AMGT_CORPUS once`. Reported to MSTR~Z as asked.
- **Inbox:** msgs 28162, 28170 and 28187 (pre-reboot: PROD promote, disk limit, wind-down) and 28200 (arm the loop) were
  read and acked. Disk measured at 05:0xZ: 82 GB free on C:.

## Tick 1 (05:09Z)

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| AMGT_CORPUS (lease FULL) | L10 closed | 31 | 87/87 terminal | none open | none | NO-OP by round-31 ruling 1; project.json reconciled |

- **Why NO-OP:** round-31 analysis `85df450e8d` ruling 1 says no further CORPUS cell before the freeze. The issuance stays
  open for a Friday-walk finding, and none has been filed on the CORPUS tree since `85df450e8d`.
- **Measured:** portal `c6aacc68` (the CORPUS Model-tab face) is an ancestor of origin PROD `b3a1d8a6`
  (portal-v2.1.193). The positive control `f2731ad3` is also in. So the face reached the demo surface.
- **Reconciled:** `project.json` `phase` and `blocking` still described round 7 (09-26). They now state the round-31
  close and the four carried after-Friday items.

**Next:** each tick reads the CORPUS tree for a Friday-walk finding. A finding is cut that tick, through the direct-act
path if it is LOCAL and under the size floor. Otherwise the seat holds until after Friday.
