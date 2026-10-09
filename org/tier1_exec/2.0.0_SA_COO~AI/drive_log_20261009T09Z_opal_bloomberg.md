# Drive log -- 2.0.0_SA_COO~AI -- NFRA_OPALAI -- 2026-10-09 09Z (site Z, host opal_bloomberg)

**archetype:** MIXED

Loop `/canonical-drive NFRA_OPALAI` 10m, cron `1c05e7b9`. Lease FULL; L7 EXECUTING, round 2.

| time | act |
|---|---|
| 09:0xZ | UB-9a05 folded @f200ec49f6 (step 4 now). PROD `launcher.ps1:172` first prompt is fixed, not asker-free -> CTO~Z 32603 YES: run as built, read four things, close before Teams |
| 09:09Z-09:18Z | MSTR~Z ran the launcher twice (32612): fast-forward OK, GATE: PASS x2, no sign-in, EMPTY prompt both times; closed 09:18Z, no Teams message served. UB-9a05 SIGNED (CVO raw-read condition) and resumed |
| 09:2xZ | Cause proven on claude 2.1.295: `--add-dir <directories...>` is variadic. Control `-p --add-dir <d> "<p>"` -> "Input must be provided"; fix `-p --add-dir <d> -- "<p>"` -> PONG. f9.AC4 had required the defective shape. CTO~Z 32614: this round's repair |
| 09:3xZ | Row NFRA_OPALAI-Z-S64 (BLOCKING, ARMED, mine); f9.AC5 (string + real CLI arms); OA-f-9 AMENDMENT 3, AC4 superseded @2524b39c76; base dry-run FAIL `separator=no` as expected. Slot ~24 provisioned `C:/tmp/oa-24` (nested opal_ai 8cdc7b9735 added by hand after a stale portal branch stopped wk-provision) and spawned worker-light |
| 09:5xZ | Worker ~24: nested c9983bd, proof @2f6df0408c, AC5 PASS; issuer re-grade PASS. Drained @256d955e74 (safe-merge rc=0). OA-f-9 complete @47484ee26a; row W24-S2 dismissed (misread of the criteria). Ask to MSTR~Z: push c9983bd to opal_ai DEV/PROD, re-run the step-4 read |

## Next

1. MSTR~Z: opal_ai DEV/PROD to `c9983bd` (ls-remote), the launcher re-run, the four readings, close. On a live whoami,
   Z-S63 and Z-S64 disarm.
2. r29 (OG-ap-3, AE~Z at 11:00Z): arm (b), then arm (a) with the raw pinned read; then the arm ids to the relaunched
   Analyst for the FWD-1 run.

## Compiler Tools

- `claude -p` control and fix arms: the decisive instrument for Z-S64. A string-shape check (f9.AC4) had certified the
  defect, so AC5 now runs the real CLI.
- `wk-provision.sh provision ... --nested`: stopped on a stale `wk-NFRA_OPALAI-24-portal` branch before the nested step,
  leaving an empty `opal_ai`; the nested worktree was added by hand. Gap: the script does not skip a portal the cell does
  not need.
- `safe-merge.sh`: rc=0, fast lane, rebuilt once on a moved tip.
- `safe-commit.sh` with GATE (viii) on the modified order: graded, 0 violations.
