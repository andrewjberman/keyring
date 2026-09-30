# IRPT_BCKEND decomposition -- ROUND 26, WORKSTREAM ~M (2026-09-29, 2.0.0_SA_COO~M, on CTO DECISION 103025)

Cut on 1.0.0_SA_CTO DECISION 103025 (walk-2 backend placed, on the state table
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/walk-v2-state-table-20260929.md` @f80d019a6c; Andrew
3054ca47ec "we'd prefer to do a lot of that work server side"). The CTO's words: "W2-11 fold is NOT legal -- the server
serves the aggregate"; "~M: W2-11 per-security aggregate and W2-15 per-class weights, both served". Rounds 20-25 ~M are
issued, so this rides round 26 (GATE (x)).

The rest of 103025's ~M list needs no new cell:
- W2-13 sector: IB-mr-251 already serves it. etf-classifications holds the GICS sector as `sub_asset_class` for a
  single stock (AAPL -> Information Technology, read 20:3xZ). The table holds no industry field, so the served
  industry half is referred to 1.0.0_SA_CTO (O8 / canonical-table project).
- W2-19: source_vendor_keys is absent from all three served headers today (business date 2026-09-28, read 20:4xZ). It
  arrives with the 2026-09-30 fire on the re-minted packages, which IB-mr-222 Part 2 reads.
- W2-20 and W2-21 ride the same re-mint (IB-mr-222 Part 2).

| cell | item | ruling carried | outcome served | risk | depends on |
|---|---|---|---|---|---|
| `IB-mr-261` | The producer serves, in the Holdings snapshot, one aggregate per security identity (value and weight of the scope total, summed across accounts; W2-11) and one total per asset class (value and weight; W2-15), as new optional contract properties in the three tracked HoldingsSnapshot schema copies; a census from real local builds at three firms; the half. LOCAL build + record: no upload, no mint, no deploy | CTO 103025; F7-AC4 and CTO 102522 (the page prints only producer-served totals) | FWD-5 (Holdings) | WORLD (reads the firm buckets for local builds) | IB-mr-251 (same file, holdings_snapshot.py; the aggregates carry 251's classes) |

Chains: A = 251 -> 261 (one chain; 261 edits the file 251 is editing and aggregates the classes 251 serves). Worker slot
`0.9.0_WK_IRPT_BCKEND~84` takes 261 as the second order of its queue once 251 drains. The served move is a later
Holdings re-mint under this cell's half, released after 251's.
