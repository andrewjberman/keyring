# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: MX-r-10 PHASE A drained; PHASE B re-addressed to ~MX and held for the gateway slot -- 2026-10-11 01:0xZ-03:0xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Ticks and events

| time | act |
|---|---|
| 01:3xZ | MX-r-10 PHASE A drained @11cb1ee6e9 (worker ~30). Deploy-only `a9c23fe126`, cut on the live ref `2a5966dfbd` (MP-r-2); the host census reads 107 of 107 against the extracted `-latest`, read twice. The cut is 2 files (DATA_CATALOG.yaml +95/-4, opal_discover/integration.py +15/-11); the other 102 are byte-identical. ENABLED_INTEGRATIONS difference empty (both readers GAP). Tools 66=66, `.env` keys 52=52. Offline on the deploy tree: routes 10/10, FWD-18 3/14, C3 3/3, E-13 guidance 5/5 |
| 01:3xZ | ~30's queue is empty: tree and branches removed. Deploy tree `C:/tmp/mx-dep-r10` kept (a9c23fe126, clean) |
| 01:4xZ | MX-r-10 A1 @b86b05a653: PHASE B re-addressed to `0.7.0_AE_CloudOps~MX` (LIVE, idle). HELD for the slot after ledger `nfra-oplgtw-gateway-release-e2` (OG-ap-6 B2, GO at or after 11:00Z per its A2 @e1cfff0023). At the slot: re-cut v2 on the new live ref, both halves signed, then the GO. GATE (viii) graded the modification |
| 02:06Z, 03:06Z | Ticks are dated waits (owner `2.0.0_SA_COO~O`, until 11:30Z); keep-driving OFF, so no next-calls |

## State

- Round 9: o-1, o-2, x-6 and c-7 are complete and drained; r-10 is pending (PHASE A done, PHASE B held).
- FWD-19 is NOT done this round (both readers GAP). J1 HELD at Andrew. MX-s-19: s19.PRE on 2026-10-13 after 03:00Z.

## Compiler Tools

- `safe-merge.sh` (PHASE A drain, 27 paths, index check 0 differ).
- `unblock.py tick --wait-until --owner`: a DATED wait, counted WAITING, not empty.
- `get_agent_status 0.7.0_AE_CloudOps~MX`: LIVE before re-addressing.
