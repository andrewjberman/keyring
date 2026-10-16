# ADVI_COTBKF decomposition -- ROUND 96 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- measure the served move on dell2's run data

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the CTO's word on the served move (msg 6455, 2026-10-16 ~03:18Z): "under 3adb (a) every value's DELTA should be 0, with only the label added, so any value that moves is a finding and a stop." Andrew's call `3adb` (a): served Yahoo-priced days for securities held in V2 stay, labelled interim-Yahoo. The CTO's route B (msg 6467; record `ledger/CTO_RULING_DELL1_ROUTE_B_DELL2_RUN_DATA_20261016.md`): the rebuild reads dell2's own run data.

**What round 95 left.** `CB-cq-1` (worker ~185, drained @c2f2aff341) stopped at provisioning: the as-traded price basis reads a Yahoo close cache (3,580 per-ticker files) that was on dell2 only (row `ADVI_COTBKF-D1-W185-S1`, BLOCKING, inert). Round 96 does not provision anything: dell2's `.scratch/advi_cotbkf` arrived by Taildrop and sits at `.scratch/advi_cotbkf/` on dell1 (gitignored, off git). Received and checked by the issuer: zip sha256 equal to the dell2 manager's report; 20,563 files (equal to dell2's listing); 4,478,568,892 bytes extracted (equal to the zip's own uncompressed total; dell2's exact listing bytes asked for, CTO confirmation records "4.3 GB").

**Served-move facts (read 2026-10-16 ~03:4xZ and at the draft of the COO half).** Served `run_commit` `6f70d5cc01bb2e196266799a657be6d0b2dc8a16` (row `D1-S9`, the CB-ah-3 held build). The move adds TWO columns to each served table (`use_class`, `porting_verdict`; `porting_verdict` was built in round 83 and never applied). `run_commit` changes on every row (the build is at a later HEAD): it is excluded from the comparison and counted separately.

**Rule 24.** Domain: the measurement that decides whether the served move may be signed (the pre-existing columns equal, only labels added). Subtraction: the rebuild at the served settings, the control against the three served tables and the label counts -> `CB-cr-1`. Uncovered here by design: the signed pair (the COO half is this seat's act, the CTO half his), the apply (a CloudOps seat under the pair), the CVO's grade of the labelled tables; and `W185-S1` is disposed by the issuer from `CB-cr-1`'s record, not by a cell.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cr-1` | on dell1, from the received dell2 run data, rebuild the three tables locally at the served settings (cash leg `method_r28`, price basis `as_traded`, hold list `05613L3H2,95000U2D4,651639AX4`, policy `interim`); read the three SERVED tables; prove every pre-existing column equals the served one row for row (`run_commit` excluded and counted); count what the two added columns say; record the received folder's file count and total bytes; stop and record if the control fails | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~186` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
