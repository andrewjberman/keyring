# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-02 01Z -> 04Z (host opal_bloomberg)

Lease FULL. Round 7 is issued and at L7. The span ends on Andrew-direct "log and wind down" (0.0.0_AB_MSTR~Z msg 28179,
~03:58Z): the cron loop is cancelled and no new act is started.

## Decisions closed this span

- **Round-6 L10 analysis read** (`ROUND_ANALYSIS.round6.md` @361b186c92, msg 28126). The CTO's hold for the D9->D6 move
  was lifted by msg 28146 (02:25Z): owned-paths refuses a one-commit tree move, so the move is deferred to a later round
  boundary and round 7 issues into D9.
- **Round 7 ISSUED @9108f11494** (27 files, `fanout: 4 of 4 chains, cap 8`):
  - [MX-s-17 -> MX-s-18 -> MX-s-19] worker ~24 (WORLD);
  - MX-f-1 ~25, MX-m-2 ~26, MX-x-5 ~27 (LOCAL; ~27 worker-light).
  - The battery was dry-run at base cb234fbfa0: 15 build checks FAIL, the `data/cot/` control PASS.
  - Two instrument defects were fixed before the cut:
    - s18.AC3 now expands the deploy script's variables; a fixed-copy control reads rc=0.
    - s19.AC2 counts client-side, after paginated `length()` returned per-page counts. The 10-01 + 10-02 control reads
      2 of 2, and the gap day 09-29 reads ABSENT.
- **Finding:** the sentinel-less run dates in 09-03..10-02 are 9: every Monday and Tuesday, plus Wednesday 09-09. So
  MX-s-19's acceptance is the scheduled runs of 2026-10-05 and 2026-10-06.
- **Worker results:**
  - MX-x-5 COMPLETE (worker 852353c904; AC1 6/6 arms, AC2 3/3, AC3 both arms). **Drained @4a888eb59e.**
  - MX-m-2 worker-complete (3f8588f71b, AC1 PASS: Orion 24, Eclipse 8, SmartX 13 datasets; 0 catalog rows).
    - Row S1: the order's SmartX bucket does not exist; SmartX silver is in `opal-data-assets`.
    - Row S2: Orion and Eclipse are duplicated in `opal-data-assets`.
  - MX-f-1 worker-complete (5f937435cc, AC1-AC3 PASS).
    - The skip path is `not_on_path` (`gold_dispatch.sh:1349-1350`, scheduled run 2026-09-30T01:11Z).
    - Both weekly tables land Sunday 00:12-00:32Z.
    - Rows S1 and S2 filed. The drain must regenerate `infra/system/06_current_state.*` (comp-system override on
      3d7fb62105).
- **Disk (Andrew /cleanup, MSTR 28165):** 23 drained MCPINDEX worktrees were removed (rounds 4-6 workers and the
  rel/dep/rb release trees), 0 failed. Every HEAD was in CLOUD or on a named branch. C: went from 3.2G to 70G free.

## Open at wind-down (each with its condition)

- **MX-m-2 drain refused, not merged; no MERGE_HEAD.** The cause is a FOREIGN corpus failure, row
  `NFRA_OPLGTW-Z-S44 /surfaced_at` (not this project's). Re-run `bash /c/tmp/mx-r7-drain.sh wk-nfra_mcpindex-r7-26 ...`
  once that row is fixed by its issuer.
- **MX-f-1 drain:** not started; after MX-m-2, with the comp-system regeneration.
- **Worker ~24 (MX-s-17 + MX-s-18 PHASE A):** it was running at the wind-down. Its PHASE A ends at the ANNOUNCEs with
  no publish or apply. Both PHASE Bs wait on never-widen halves (COO + CTO). MX-s-19's acceptance needs MX-s-17 and
  MX-s-18 applied before 2026-10-05.
- **Status flips:** MX-m-2 still reads `issued` and the issuer owes its flip; ~25 and ~27 flipped their own.
- **Worktrees to remove at each drain:** r7-24..27 (`git worktree remove`). r7-27 is drained and removable now.
- **r6.J1** (Alyssa) is still booked via MSTR~Z. The sitting time and "captured" are owed to COO~MP.

## Compiler Tools

`safe-merge.sh` (with a foreign-staging retry wrapper), `safe-commit.sh`, the round-7 battery
(`deliverables/2.0.0_SA_COO~MI/round7/checks/`), `git worktree remove`.
