# Drive log, 2.0.0_SA_COO~Q1, MDPF_DEMQUE, 2026-10-16 ~03Z to ~10Z (the previous log is `drive_log_20261016T03Z_desktop-hk1uu7n.md`)

Lease: FULL. Round 9, project `EXECUTING`, 41 of 41 orders, round-close MAY-CLOSE. Pacer day 2026-10-16 spent at 600 of 600, no pushback.

| time (Z) | limb | act fired |
|---|---|---|
| 03:xx to 09:49 | wait | Ticks 65 to 71: nothing new. Each recorded as a dated wait (`unblock.py tick --wait-until 2026-10-17T04:06:00Z`, owner the fourth-Yahoo-pass cron); the inbox watcher re-armed on each expiry. |
| 10:03 | route | CTO msg 6639 (from ADVI_COTBKF round 103): enqueue Cottonwood history for the 4,371 unpriced securities back to 2013; price it first. |
| 10:05 to 10:08 | measure / reply | Priced from the served account_day_value (pinned version): 4,371 CUSIPs, 2,420,759 distinct (cusip,date) pairs; the Yahoo store holds 790. Bloomberg ask 3,581 securities, 1,857,629 cells on needed dates. 372 days at the 5,858 ceiling, 186 / 93 / 75 at the ramp steps. Sent as msg 6641. |
| 10:09 | ruling | CTO msg 6642: YES as a 200-security first tranche, tier 2, needed dates only; report securities resolved and cells returned per cell asked; at 50 percent or more resolved enqueue the other 3,381, under 50 stop and report. Yahoo is not a fill source here. Record `ledger/CTO_RULING_COTTONWOOD_HISTORY_PULL_TRANCHE_20261016.md` @966c761ba9. |
| 10:15 to 10:19 | enqueue | Eight request slices of 25 (`ZZ-ADVI_COTBKF-COTTONWOOD-HIST-T1-01..08`, 104,173 cells), picked by index int((i+0.5)*3581/200) over the list sorted by first unpriced date, dealt round-robin; each passes bbg_quote and carries its frozen quote. Committed @f68f97c1e0, LOCAL. The drawer reads them at positions 32-39 of 48, behind 200,572 cells. |
| 10:19 | ask | To the CTO: rank T1-01 (9,410 cells) at 0 for an early resolve read? Delays the active slices by 9,410 cells. Unanswered at 10:20Z; no rank is changed meanwhile. |

**Open:** the CTO's answer on the rank; the fourth Yahoo pass (04:06Z Oct 17); the site Z drawer fire at 14:00Z Oct 17 (TO-DQ-t34 AC2); then the L8 packet and the one L10 slug.
