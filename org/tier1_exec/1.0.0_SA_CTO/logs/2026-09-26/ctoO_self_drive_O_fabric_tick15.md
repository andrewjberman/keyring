# /self-drive ~O fabric -- ticks 12-15 (2026-09-26 08:49Z - 09:50Z)

- Driver `1.0.0_SA_CTO~O`; arming record `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d; cron 9999d604.
- state: ARMED.

## Calls and verdicts
No open calls in scope. No new verdicts.

## Fabric movement
- **OA-f-2 LIVE** (`2.0.0_SA_COO~O` drain @837d4d1e1d): release c5f8099440, base 0af72fb1d0 by content, serving on
  opal-gateway since 07:44:41Z. The drain reports:
  - ledger nfra-opalai-zs18-gateway-client-scope CLOSED 6 of 6;
  - tool list 46 = 46, empty diff;
  - AC2: the live identity_scope md5 equals the release;
  - AC3: live upload rows unqualified 0, client-qualified 1;
  - on-box /health 200.
  The order file still reads `pending`; the flip is COO~O's. **Switchover precondition (d), the upload refused to the
  runtime, is met at the served plane.** Measured by the issuer, not re-measured here.
- **OA-g-1 complete** (drain @45ddd8d948): the grant grammar admits a portal-only asker grant (`portal_channels`,
  zero Schwab masters). Row Z-S27 @e4e8b75d71 disarms Z-W9-S1.
- `0.4.0_DS_ClientPlatform~D`: row NFRA_MCPINDEX-Z-S11 @7a11ae5ddf (the pathfinder gap is a conversion failure on two
  well-formed deliveries); MX-s-1 addendum @e222674bc3.
- `0.7.0_AE_CloudOps~I`: MX-s-3 deploy ledger opened @e76b307c67 (7 legs).

## Scope state (order files, last status tag)
| project | open orders |
|---|---|
| NFRA_OPALAI | OA-f-2 (live, flip owed), OA-g-2, OA-g-3, OA-t-1, OA-t-3 |
| NFRA_MCPORTAL | MP-a-1 |
| NFRA_MCPINDEX | MX-r-3, MX-s-1, MX-s-2, MX-s-3 (deploying), MX-s-4 |
| NFRA_OPLGTW | OG-v-4, OG-v-5 |

MX-r-1 and MX-r-2 print an empty tag under the `[a-z_]*` pattern; both were superseded at round-1 close (their status
lines carry text the pattern stops at). Not open.

## Waiting on
- COO~O: OA-g-2 (the portal-grant release) and OA-g-3 (Alyssa's grant), then the switchover confirmation message.
- The laptop: releasing NFRA_OPLGTW's CTO and CVO legs to ~O (msg 20260926T045815Z). This also gates MCPORTAL C6
  (pre-draft @3af3761b0c).
- Andrew, at the switchover sitting: the Analyst's gateway sign-in as Opal Bloomberg, and his own oid for MP-a-1.

## Completion test
NOT DONE: 0 of 4 `complete`. Reachable 4 of 4.

## Compiler Tools
None.
