# 2.0.0_SA_COO~Z drive log -- 2026-10-02 10:4x-11:5xZ (/canonical-drive AMGT_RESAPP 30m, cron a1ea685c)

| project | limb | round | thread | act fired |
|---|---|---|---|---|
| AMGT_RESAPP | L6 -> L8 -> L10 | 62 CLOSED (CTO @3d590fcb31) -- demo risk, BA /timeline/day | y | DRIVE FORWARD, then HOLD + FREEZE |

- **Demo risk (CTO msg 28407, ruling 5).** Every BA `/timeline/day` call had died at the 29 s ceiling since 10:14Z (CVO row Z-C-S29).
  - Pre probe: 27.2 s warm at 1769 MB.
  - ONE issuance `59d350c2a4` (al-1, the memory raise); GO 10:45Z.
  - 3538 missed (20.4-22.9 s); 10240 passed 3 of 3 cold (16.6-19.1 s). ~460 MB used at every tier: CPU-bound, and 10240 is the maximum.
- **Track B (ruling 5a; freeze 12:30Z).**
  - al-2: the silver read runs under an 18 s deadline from handler start. On the deadline: headline null plus one plain
    `headline_reason`, status 200.
  - Code `a12291728f`, drained `a2ff06d1a1`; build-only 1 changed; tests 3 passed.
  - Pair: COO `a12291728f`, CTO `57dfa6bd84`.
  - LIVE 11:27Z (`bZBmEtRr`), graded 11:32Z: 3 of 3 cold 200, one at 18,006 ms with the reason; controls byte-equal. al-1 CLOSED.
- **L8 and L10.** Packet `16d66aa310`. CVO slug `5542cd4564`, then the CTO closed round 62.
  - Warm-up `warmup_pair.py` armed for 12:50Z: 2 sequential read-only BA Sept 8 invokes. Repeat once on MSTR~Z's start word.
- **Price ranking:** both axes serve 2026-10-01, stale_trading_days 0 (the 07:13 ET generation landed).
- **Next:** the warm-up pair at 12:50Z; hold and freeze through Andrew's read. Round 63 (track C) is post-demo.
