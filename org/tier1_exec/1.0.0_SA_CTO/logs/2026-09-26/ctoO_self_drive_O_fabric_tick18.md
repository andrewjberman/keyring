# /self-drive ~O fabric -- ticks 16-18 (2026-09-26 10:18Z - 11:20Z)

- Driver `1.0.0_SA_CTO~O`; arming record `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d; cron 9999d604.
- state: ARMED. Written on the hourly floor.

## Calls and verdicts
No open calls in scope. No new verdicts.

## Fabric movement
- **NFRA_OPALAI addendum A1 terminal.** OA-f-2 closed `complete` @3558be2482 (AC1-AC3 PASS, instance VALID).
- **Switchover sitting READY.** `2.0.0_SA_COO~O` recorded all four runbook preconditions MET @4dc8fa1221 and sent the
  sitting-ready message for Andrew (msg 26060). It was relayed to Andrew in this session. Parts A, B and D can run now;
  Part C (Alyssa's question) waits on OA-g-2 and OA-g-3.
- **OA-g-2 in progress:** release branch `rel-nfra-opalai-portal-grant-gateway`, last commit 11:18Z by
  `0.9.0_WK_NFRA_OPALAI~9`.
- **MX-s-3 deployed:** `0.7.0_AE_CloudOps~I` closed ledger nfra-mcpindex-silver-etf-rebuild, 7 of 7 legs @547cd9f613.
  Row NFRA_MCPINDEX-Z-S12 @5f7b13787a (BLOCKING, INERT): the shared `record-terraform-deploy.sh:259` opens the Lambda
  source map without `encoding=` and fails on cp1252. The one row was written by hand to the tool's own rule;
  disarm_owner `2.0.0_SA_COO~O`.
- COO~O's watcher is live (1 row, created 11:08Z).

## Scope state (order files, last status tag)
| project | open orders |
|---|---|
| NFRA_OPALAI | OA-g-2 (releasing), OA-g-3, OA-t-1, OA-t-3 |
| NFRA_MCPORTAL | MP-a-1 |
| NFRA_MCPINDEX | MX-r-3, MX-s-1, MX-s-2, MX-s-3 (deployed; flip owed), MX-s-4 |
| NFRA_OPLGTW | OG-v-4, OG-v-5 |

## Waiting on
- Andrew: the switchover sitting (the runbook's Parts A, B, D now; C after OA-g-3).
- The laptop: releasing NFRA_OPLGTW's CTO and CVO legs to ~O (msg 20260926T045815Z). Gates MCPORTAL C6 (pre-draft @3af3761b0c).

## Completion test
NOT DONE: 0 of 4 `complete`. Reachable 4 of 4.

## Compiler Tools
None.
