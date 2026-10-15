# Drive log, 2.0.0_SA_COO~Q1, MDPF_DEMQUE, 2026-10-14 ~19Z (the previous log is `drive_log_20261014T11Z_desktop-hk1uu7n.md`)

Lease: FULL. Round 9, project `EXECUTING`. Cron `adba1a19` (hourly at :17) and the inbox watcher armed. Ticks 3 to 9 (12:37Z to 18:37Z) were dated-wait ticks: no project commits, 0 open DEMQUE calls, `/next-calls --drive` 0 FREE options, `unblock.py tick` `WAITING DATED` until 2026-10-15T02:30Z (the 22:30 ET wired Yahoo run). One FREE read-only act at tick 4: the scheduled task `Opal MDPF_DEMQUE daily draw` runs `run_daily_draw.sh` from the shared checkout, and the wired-path commits t-58, t-59, t-60, t-61 and t-62 are all ancestors of its HEAD.

| time (Z) | limb | act fired |
|---|---|---|
| ~18:51 | intake | CTO msg 5713 (Andrew-direct: ETFS_RIVALS is done, "all it needs is its backfill sorted out in DEMQUE") and `~V1` msg 5716: three cited rows (TR on held days 123,933 units, close on dialog-curve days 89,717, `DVD_HIST_ALL` for 71 securities). Acked both. |
| ~19:20 | L6 | Cut `DQ-t-63` (`etfs_rivals_intake.py`, seven requests, TR and close in disjoint 30/90/365 stages on Andrew's "C1 yes, approved in that order") @9b7d894bcb. fanout: 1 of 1 chains, cap 8. Both checks FAILED at the base as expected. Worker `~55` (haiku, high). Issuer finding: V1's Row 3 list holds 71 keys and the last is `nan`; the request is 70 securities. |
| ~19:30 | L7 | Worker `~55`: AC1 PASS; AC2 FAIL as written because MY check script lacked the repo root on `sys.path` (row W55-S4, issuer defect). Fixed @80cdc2833b (and on the branch @dd58c92499), resumed the same worker: AC2 PASS (TR 123,933 of 123,933, close 89,717 against 89,216, 70 of 70 names, oracle 0 of 29,617 hashes, byte-identical). |
| ~19:40 | L7 / drain | Merged @0589c7c752 through `safe-merge.sh` (fast lane, tree check 0 violations); worktree and branch removed. Folder suite 222 passed (worker). |
| ~19:45 | filing | Re-ran the real build on the merged bytes (1m21s, same line), filed the seven requests and their frozen quotes in `requests/`; `bbg_quote.py --check-declared` 19 accepted, 0 refused. |

**Quotes (independent / stacked in queue order behind surface B at 5,858 cells a fire, no carry-over):** TR D30 7,652 (2026-10-18 / 2026-11-15); TR D90 23,062 (2026-10-25 / 2026-12-06); TR D365 93,219 (2026-12-05 / 2027-02-28); close D30 5,537 (2026-10-17 / 2026-11-15); close D90 15,738 (2026-10-24 / 2026-12-06); close D365 68,442 (2026-11-22 / 2027-02-28); dividends 70 reference cells (2026-10-16; an undercount, about 13 rows a security). Behind surface B alone (B1 34,437 + the 14-name request 7,685 + the porting test 3,195 = 45,317) the cumulative finish is 2026-11-08.
**Left out of rows 1 and 2:** 11 securities with no Bloomberg ticker in the owed set (2,711 units, 1.25 percent; mostly ADRs; row W55-S2). **Limit:** the builder is valid only for page day 2026-10-13 (row W55-S3).

**Open at the end of the hour:** `DQ-t-34` AC2 (the 2026-10-17 site Z fire, receipt read 10-18). The first wired Yahoo run (22:30 ET, 02:30Z 2026-10-15) and its receipt against the version baseline.
