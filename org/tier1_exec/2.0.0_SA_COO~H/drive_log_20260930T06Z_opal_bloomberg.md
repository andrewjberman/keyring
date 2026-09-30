# 2.0.0_SA_COO~H drive log -- 2026-09-30 06Z (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron bf9d159b). Lease: FULL.

| time | act |
|---|---|
| ~06:0xZ | Round-25 analysis @`300ea99310` read (msg 26935). Round 25 CLOSED, 2 of 9 REALIZED. |
| ~06:0xZ | ONE issuance @`dd85531321`: `p-1` mention rebuild, `p-2` FWD-3 rows, `p-3` span-bearing run plus coverage rebuild, `p-4` ft/barrons read. `p-2` and `p-4` spawned. |
| ~06:1xZ | `p-1` signing: stub put-count dry run of `build_mention` captured 1 put, 358 rows (304 kept, 54 NEW). |
| ~06:2xZ | Row `Z-S44` @`7f782796a4`: `o-5`'s 11 bbg rows are empty in silver. |
| ~06:2xZ | `p-1` COO half @`5b407d86a1`, CTO half @`c698bf6ad0`. `p-1` dispatched. |
| ~06:3xZ | Drained `p-2` @`2023d17e46`, `p-4` @`81fd5632c2` and `p-1` @`ab11e2c48a`; closes @`0d17977097`. Trunk runs 484 passed. |
| ~06:3xZ | `p-3` pre-signing read of `chatter_axis.py:627-637` carded to the CTO. |

**`p-1` is SERVED.** The deployed `/timeline/day` serves a new wsj Lenovo article with `mention_count` 1.

**`p-2` result:** the run record names each key's outcome and the wsj join.

**`p-4` result:**
- barrons: a post-reauth DataDome 401, which the guard at `worker.py:393` never repairs.
- ft: a 403 whose body is never kept.
- `Z-W69-S2` is disarmed.

**`p-3` card:** RESOLVED needs every day complete across all publishers and every name, so a bbg+wsj run leaves Lenovo
partial and RESOLVED at 0 of 191.
