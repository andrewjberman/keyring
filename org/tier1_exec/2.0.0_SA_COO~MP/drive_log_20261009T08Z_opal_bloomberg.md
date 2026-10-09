# 2.0.0_SA_COO~MP -- drive log 2026-10-09 07Z-09Z (opal_bloomberg) -- NFRA_MCPORTAL

Post-reboot re-instantiation. The lease is FULL, and the loop is `/canonical-drive NFRA_MCPORTAL once` at :22/:52 (cron
2978c641; LIVE_ARMS row `1.0.0_SA_CTO~O` + `~MP` 30m).

| tick (UTC) | limb | act fired |
|---|---|---|
| ~07:05 | L6 (CP2) | Start: /watcher, the XXX.md steps, msg 32217 (round-4 analysis) superseded by the round-5 issuance. G-REL is closed: r29 is merged @76ff10095c but not deployed (msg 32482), and the applier reads the same (32488). |
| ~08:05 | L6 (CP2) | CP2 round 1 ISSUED @7f29d5ccd9: 7 orders, decomposition v6 CP2, 15 checks dry-run FAIL at base. Issued from a linked worktree: the shared tree carried a peer's NFRA_IAMROLES202609 index drift, which the tree validator refused. |
| ~08:15 | L6 | AMENDMENT 1 @adfc7412bf: the cell id `MP-g-1` collided with round 2's cell, so the CP2 cell is now `MP-s-1` (the file keeps its path; GATE (x) refuses a renamed file). Found because my own `mv` glob swept the round-2 order; that order was restored from HEAD the same minute. |
| ~08:32 | L7 | Workers ~8 ~9 ~10 ~11 spawned. GO MP-k-2 sent to 0.7.0_AE_CloudOps~MP. |
| ~08:35 | L7 | EMPTY tick. /next-calls --drive queued the round-4 worktree removal (sitez queue); 0 FREE options. Unblock tick read KEEP-DRIVING. |
| ~09:00 | L7 drain | All four drained. The issuer re-ran both ACs per cell: all PASS, instances VALID, write sets inside `<paths>`. ~9 merged @faeb6e4ac9. ~8, ~10 and ~11 merged in the issuer worktree (the shared index carried a peer's HARVST ledger staging), landed @5e5ad87980. mcportal bc37107 pinned on branch `nfra-mcportal-cp2-p2`. |
| ~09:10 | L7 | Hookup REFUSED (lane CLOUD_OPS_OR_ETL on `admin_api.py`), so AMENDMENT 2 @0f34bea5a1 makes it MP-r-2 step 0. Measured uncommitted: routes 4 of 4, admin and fabric tests 58 passed. |
| ~09:25 | L7 (k-2) | ASK @77184244cf read whole. COO half SIGNED. AMENDMENT 3 @2724889425: the CTO half goes to `1.0.0_SA_CTO~Z` (~O retired, Andrew-direct ~07:4xZ). Merged @a7ff380da2. Ask sent to CTO~Z. |

**State at 09:26Z.**
- CP2: 4 of 7 orders complete (o-1, s-1, k-1, p-2).
- k-2: pending the CTO~Z half.
- r-2: staged on G-REL2 (MP-x-4 live, k-2 applied).
- q-1: staged on G-SEE2.
- Round 5: all 4 staged; MP-x-4 waits on the r29 deploy (the CVO~Z half).
