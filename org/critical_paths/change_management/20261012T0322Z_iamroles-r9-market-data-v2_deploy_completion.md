# Deploy Completion Record
**Date opened:** 2026-10-12T03:22:51.857359+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T033944Z
**Deploy:** IAM-z-3 PHASE B: market-overview drops opal-market-data-v2's four declarations and its two dead ARNs; UNTARGETED apply prunes 4 stale state entries (pair COO @04146e0808 / CTO @e03d903463)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| code | git | wk-iamroles-r9-z3 | the two removals plus the tombstones.json declaration_removed line, committed on the worktree branch and drained | 96c735a39c (two removals) + 64fc0b7370 (tombstones.json declaration_removed citing @96c735a39c) on wk-iamroles-r9-z3, drained to box/sitez at 2df4bd537b (safe-merge rc=0; tree check 3 needed / 0 dropped / 0 foreign) | CLOSED 20261012T033943Z |
| apply | activation | market-overview untargeted | 0 to add / 1 to change / 0 to destroy; live policy equals the rollback minus exactly the two opal-market-data-v2 ARNs; the bucket still reads NoSuchBucket; state list 55 -> 51; post-apply untargeted plan 0/0/0 | baseline matched both rollbacks canonically and the bucket read NoSuchBucket before the act; plan 0 add/1 change/0 destroy with 43 changes = 42 no-op + 1, market_data_v2 in resource_changes 0, resource_drift 5 (4 market_data_v2); tombstone-gate checked 0 creates against 7 tombstones CLEAN; Apply complete 0 added/1 changed/0 destroyed; after: policy 5->5 stmt, 11->9 ARNs, exactly 2 gone both opal-market-data-v2, 0 added, Sids and actions identical, portal-v2 kept; bucket STILL NoSuchBucket with a live control rc=0; state list 55 -> 51 with 0 market_data_v2 addresses; post-apply shared-tree untargeted plan 'No changes' = 43 changes all no-op, resource_drift 5 -> 1 | CLOSED 20261012T033943Z |

## Log

- 20261012T032251Z OPENED by 0.7.0_AE_CloudOps~IR with 2 leg(s)
- 20261012T033943Z LEG code closed: 96c735a39c (two removals) + 64fc0b7370 (tombstones.json declaration_removed citing @96c735a39c) on wk-iamroles-r9-z3, dr
- 20261012T033943Z LEG apply closed: baseline matched both rollbacks canonically and the bucket read NoSuchBucket before the act; plan 0 add/1 change/0 destr
- 20261012T033944Z CLOSED -- all 2 legs proven
