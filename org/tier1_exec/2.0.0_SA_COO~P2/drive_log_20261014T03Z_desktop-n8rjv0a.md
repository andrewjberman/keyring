# Drive log -- 2.0.0_SA_COO~P2 (IRPT_BCKEND ~P, dell2), 2026-10-14 ~00:00Z to ~03:20Z

Substantive ticks since the 23Z log (`drive_log_20261013T23Z_desktop-n8rjv0a.md`). Push state: LOCAL on `box/dell2` (ls-remote not equal to HEAD at the last read).

| time (Z) | round | act | result |
|---|---|---|---|
| ~00:xx | 186 | IB-pr-521 export re-pin apply and IB-pr-522 activity-backfill census merged, criteria re-run on the merged tree | PASS; packet to the CVO |
| ~01:xx | 187 | IB-pr-523 stage-selection build (handler.py, `backfill_stages`) and IB-pr-524 COT/INF source read merged | PASS; COT can produce all 19 columns, INF 17 |
| ~02:2x | 188 | IB-pr-525 Design-B census and never-widen packet (COO half signed at packet sha256 `f6dd828322d4`) and IB-pr-526 IR holdings class count merged; `round-close-check` MAY-CLOSE; packet `0c5677447a`; three findings to the CTO (rows D2-S158, S159) | CTO ruled all three (`fc61718f5b`); CVO adjudication v89 dismissed 10 rows |
| ~02:4x | -- | L6 read of the catalogue on the live zip's bytes (`xP47NQDn`, 3 firms, five Opal models in order); ledger `irpt-ycg-catalogue-ultrashort-20261013` CLOSED (`aea9aa8e33`); `2.0.0_SA_COO~Y2` told | Y2's L3 released |
| ~03:0x | 189 | Cottonwood lost-account read (direct act; rows D2-S160, S161); ONE issuance `1d3605e19c`: IB-pr-527 (cash rule build, LOCAL) and IB-pr-528 (count by layer, FDRXX check, packet, SERVED); workers ~374 and ~375 spawned | in flight; one call at the CTO (a branch-2 pair for the one account) |

Waiting on others: the CTO's call; the CVO compile of rounds 186-188; Andrew's PROD execution ID for IB-pr-456 (open act `f61b`); D2's thresholds-swap ledger leg L7 (read 2026-10-14T11:41Z) and FWD-21's reader of `account_activity_daily` (both gate the Design-B CTO half).
