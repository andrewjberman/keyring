# /self-drive ~O fabric -- ticks 19-21 (2026-09-26 11:50Z - 12:51Z)

- Driver `1.0.0_SA_CTO~O`; arming record `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d; cron 9999d604.
- state: ARMED. Written on the hourly floor.

## Calls and verdicts
No open calls in scope. No new verdicts.

## Fabric movement
- **MX-s-3 complete** @d9efea9be2: AC1-AC3 PASS, instance VALID (rc=0), re-run by `0.7.0_AE_CloudOps~I` itself. The
  earlier INVALID (@765a8f105e) was decomposition-side, cured by `2.0.0_SA_COO~O`'s R2.6 rows @9f323d492d.
- **MX-s-5 issued** @fa1af39c3c: the Lambda source map goes ASCII. This is COO~O's ruling on row NFRA_MCPINDEX-Z-S12
  (the shared deploy-record tool's unguarded UTF-8 read).
- **Independent check of the upload fix:** `3.0.0_SA_CVO~O`'s CVO-MODE log @1d76febf04 records gateway release
  c5f8099440 verified live. That is a second, non-acting read beside the issuer's own.
- `2.0.0_SA_COO~O` /canonical-drive log @e66ded5638: one [STUCK] raised in error (a drained branch tip) and withdrawn.
- OA-g-2 (the portal-grant release) still in progress.

## Scope state (order files, last status tag)
| project | open orders |
|---|---|
| NFRA_OPALAI | OA-g-2, OA-g-3, OA-t-1, OA-t-3 |
| NFRA_MCPORTAL | MP-a-1 |
| NFRA_MCPINDEX | MX-r-3, MX-s-1, MX-s-2, MX-s-4, MX-s-5 |
| NFRA_OPLGTW | OG-v-4, OG-v-5 |

## Waiting on
- Andrew: the switchover sitting (the runbook's Parts A, B, D now; C after OA-g-3).
- The laptop: releasing NFRA_OPLGTW's CTO and CVO legs to ~O. Gates MCPORTAL C6.

## Completion test
NOT DONE: 0 of 4 `complete`. Reachable 4 of 4.

## Compiler Tools
None.
