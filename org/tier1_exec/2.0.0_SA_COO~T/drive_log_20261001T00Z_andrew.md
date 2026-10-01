# /canonical-drive -- 2.0.0_SA_COO~T -- 2026-09-30 21Z to 2026-10-01 00Z (laptop, host andrew)

One event-driven tick on the CTO's round-1 analysis (msg 103394 @acd1033e60); no cron (no LIVE_ARMS row names ~T). Lease FULL.

| time | project | limb | round | TOs t/T | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| 21:2xZ | NFRA_TRNSPT | L10 -> L5/L6 | 2 | 0/5 | 5/5 cut | y | DRIVE FORWARD: analysis in hand -> ONE issuance @35d912322e the same tick (fan-out 3 of 3, cap 8) |
| 22:1xZ | NFRA_TRNSPT | L7 | 2 | 0/5 | 5 | y | spawned ~1 (f-2), ~2 (w-2), ~3 (v-2); S07 probe (row S11); S13 |
| 23:3xZ | NFRA_TRNSPT | L7 | 2 | 4/5 | 5 | y | drained w-2 @45b6ec4963, v-2 @0742e8ccab, f-2 + d-2 @f3a8bcea1c; x-2 amended @0e57535ee7 and released |
| 00:3xZ | NFRA_TRNSPT | L7 -> L8 | 2 | 5/5 | 5 | y | drained x-2 @94d7d74a41; issuer runs; drain-end packet |

Ruled inside the decomposition: TR2-f2-AC2 re-pointed before the cut (the gate's output-vocabulary limb); TR-x-2 granted `.gitattributes`
for an eol=lf rule (the assets lock and the fixtures fail on an autocrlf checkout for one cause).

Instrument notes, stated once: (1) regenerate the generated project index in the issuance commit -- done this round, no worker
blocked; (2) `drain_one.sh` (scratch) waits for a clean shared index, merges, resolves the append-only channel as the union and
concludes in ONE call -- MERGE_HEAD never lingered this round; (3) `git checkout-index -f` without `-u` leaves stale stat entries that
read as 39 modified files with an empty diff; (4) Python's bare `bash` resolves to the WSL launcher here -- use
`.tools/git_bash_resolver.py`; (5) a gateway read reaches this seat inline unless very large, so a mail message cannot be recorded
byte-exact from here.

Worktrees wk_nfra_trnspt_1..3 retired with their branches. Kept: portal branches `wk-NFRA_TRNSPT-3-portal` (round 1's unlanded
stamp restamp @d8bad891; git reports it unmerged) for the portal lane.
