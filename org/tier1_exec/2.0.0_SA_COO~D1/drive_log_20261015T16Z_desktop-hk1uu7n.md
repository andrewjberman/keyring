# drive log 2026-10-15 15Z-17Z -- 2.0.0_SA_COO~D1 -- MDPF_CANON (lease FULL, keep-driving ON)

Re-seat after the operator restart: registered, watcher armed, cron hourly :23 per `org/ref/LIVE_ARMS.md`.

| time (Z) | limb | act fired |
|---|---|---|
| 15:55 | round 10 drain, 2 of 2 orders complete | sent the CTO the two never-widen pairs (CTO halves owed); E4 GO already READ by CloudOps~DELL1 |
| 16:01 | L7 deploy | CTO halves GIVEN (msg 6061, `9b9408fce1`); both CloudOps orders moved to `pending` (`e9bf373d86`); GOs sent (pins `b6352de8f8`, `3df2f0851a`) |
| 16:08 | surprise D1-S29 | CVO asked if the fix exists; measured portal DEV `ad7c100b` and PROD `33ad65ee` both carry `trendGrouping.ts` `a3d11cfe`: NOT fixed; replied |
| 16:25 | surprise D1-S29 | Andrew-direct via CTO msg 6082: a demo Global session uses Variant 1; Variant 2 not repaired; lands on DEV in round 11, rides the next PROD promote |
| 16:27 | L7 deploy | gold deploy DONE (msg 6083); issuer read `mdpf-gold-lambda` CodeSha256 `vNRXwWym...`, `MDPF_GOLD_COMMIT` equals the pin |
| 16:45 | L8 | drafted `round10/ROUND10_DRAIN_END.md` (CN-r-1 AC4 needs the 2026-10-16 13:30Z fire; A4 objects are write-once per date) |
| 16:55 | L7 deploy | publisher deploy DONE (msg 6088); issuer read the role: four inline policies, the new one is `s3:GetObject` on `platinum/mdpf/*` only; packet draft updated `6e83877912`; worker worktrees `wk-canon-r10-29/30` removed |

Waiting (dated, owners live): the 2026-10-16 13:30Z gold and 13:50Z publisher fires (`schedule:mdpf-scheduled-floor`), then the readback `round10/checks/r9_trend_groups_readback.py read --pin b6352de843f3726ad5c51c650d9035ca8336db`, the CTO's two asks (name the unchanged pairs; any reader keyed on a served `written_at`) and the FINAL packet to the CVO. E4 24 h read due 2026-10-16 16:05Z (CloudOps~DELL1). Round 11 is cut when the CTO's round-10 analysis arrives (carries the S29 remedy).

Push state at 17:33Z (ls-remote read, origin `box/dell1` `09baa39bd8`): `e9bf373d86`, `6e83877912`, CloudOps `fc295efc23` and `ebe7b0aefd` are all on origin (merge-base read).
