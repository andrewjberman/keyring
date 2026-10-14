# ANDREW-DIRECT 2026-10-14 ~15:0xZ -- client data for the gateway comes ONLY from the opal-data-assets vendor silver folders

**Recorded by:** 1.0.0_SA_CTO~Z, site Z terminal. **Projects:** NFRA_OPLGTW (FWD-22), NFRA_MCPINDEX (FWD-22).
**Context:** answer to the CTO's report that CRO~Z's G2f mapped 49F Black Diamond live tables in `opal-data-bd`.

## His words (verbatim)

> opal-data-bd is not a bucket we want to use for this at all, the only client-data we want to be using explicitly at
> this time is the silver vendor folders in opal-data-assets

## What it changes (recorder's reading; the verbatim governs)

- Every `client_*` tool and adapter reads client data ONLY from `s3://opal-data-assets/<vendor>/<firm>/silver/` folders
  (blackdiamond, orion, eclipse, smartx, schwab, commonwealth, and the Tax SMA table censused there).
- NOT used for client data: `opal-data-bd` (v3.1 Ruling 5 struck; G2f superseded), the account-grain MDPF feeds in
  `opal-data-mdpf` (v3.3 G4 item 2 struck), and the per-firm buckets' `taxsma_assets` gold (G2e struck).
- "at this time": a later word may widen it; nothing is deleted.
- Firm-level aggregates that are not account data (portal-v2 `platinum/mdpf/<scope>/` served by the existing mdpf tools,
  and `opal-data-etfs` partner ownership totals) are read as NOT client data under this word; the CTO surfaced that
  reading to Andrew in the same turn.
