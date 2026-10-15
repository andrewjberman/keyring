# CTO ruling -- NFRA_OPLGTW: the G2 client-data cells (opal-data-assets) were never cut; cut them now, 2026-10-15 ~17:0xZ

By: `1.0.0_SA_CTO~Z`, on Andrew's question at this terminal (~16:4xZ): where the chain breaks on opal-data-portal-v2,
opal-data-mdpf, opal-data-etfs and, "most importantly now", opal-data-assets.

## Measured (~16:5xZ)

**Gateway coverage.** `DATA_CATALOG.yaml` v0.5, at HEAD on box/sitez, counting catalog rows whose `read_tool` names a
deployed tool:

| bucket | rows with a tool | rows |
|---|---|---|
| opal-data-harvest | 78 | 78 |
| opal-data-portal-v2 | 16 | 41 |
| opal-data-etfs | 7 | 36 (the ten rival-fund tools are staged in OG-ap-22, not live) |
| opal-data-mdpf | 0 | 7 |
| opal-data-bd | 0 | 8 |
| **opal-data-assets** | **0** | **111** |

**The break.**
- Decomposition addendum R3-T.52 plans G2 as `OG-cl-0` (design, read only) and then `OG-cl-1..n`: the vendor adapters
  behind `client_get_holdings`, `client_get_transactions`, `client_get_allocation` and `client_get_fees`, gated on
  "cl-0 and gt-6".
- `OG-gt-6` and `OG-cl-0` are both `complete`. cl-0 flipped on 10-14 at about 17:0xZ.
- **No `OG-cl-1` or later task order exists.**
- Meanwhile the slot named "ap-21 (G2 core)" was spent on the person-record reader and the role moves.
- The rival funds (G5r) were built although PRD v3.7 orders them "after Schwab and 49F Black Diamond".
- No seat flagged the gap. My `/self-drive` ticks read open calls, which were all Andrew's person acts, and never
  compared the PRD's build order with the cut orders. That is this seat's miss as well as the issuer's.

## Ruling

1. **`2.0.0_SA_COO~O` cuts the G2 adapters now, in the PRD v3.6 order**, as BUILD cells in parallel with the release
   queue. Building does not wait on a release slot.
   - `OG-cl-1`: Schwab. Its gateway-trusted role exists.
   - `OG-cl-2`: 49F Black Diamond. It reads `opal-data-bd/silver/` through its own scoped role, per Andrew's 49F word.
   - Then Orion/Inflection (Eclipse), BD Cottonwood, SmartX (with the row filter) and Commonwealth, each with one
     prefix-conditioned role and one never-widen ask.
   - Client data never reads through `gateway-global-internal-reader-role` (v3.2).
2. **Releases:** the shared gateway slot stays one release at a time. G2 Schwab and 49F rejoin the queue directly after
   OG-ap-22 (rival funds), ahead of OG-ap-17.
3. **G3 and G5 remainders, cut in the same issuance:**
   - G3: the 25 portal-v2 rows and 7 mdpf rows with no tool. The census ranks mdpf only where portal-v2 does not
     already carry it.
   - G5 wave B: the 29 etfs rows with no tool.
   - These are the next workers once G2 Schwab and 49F are seated, within the cap of 8.
4. **NFRA_MCPINDEX is not the break.** By ruling (rounds 12-16 analysis, ruling 3) a catalog row's `read_tool` moves only
   after its OPLGTW tool deploys. MCPINDEX follows each release with a catalog cell.
5. **This seat's own fix:** from this tick, each `/self-drive` tick also compares the OPLGTW decomposition's planned
   cells with the cut task orders, and names any planned cell whose gates are met but which has no order.
