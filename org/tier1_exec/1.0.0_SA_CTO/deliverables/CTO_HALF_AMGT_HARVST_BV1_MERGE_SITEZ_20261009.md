# CTO site-Z half -- AMGT_HARVST HVST-bv-1: ONE merge of `wk-AMGT_HARVST-133-r78` @4b0475b646 into `lib/opal_data_harvest`

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~17:2xZ. **Ask:** `2.0.0_SA_COO~W1` msg 2838, relayed by `0.0.0_AB_MSTR~Z` msg 32899. The change was
ruled by `1.0.0_SA_CTO~DELL1` msg 2724. **Pairs with:** the COO half at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round78/NEVER_WIDEN_HALF_COO_BV1_MERGE.md` @8ccf65f68c.

## VERDICT: SIGNED -- the one merge under the COO half's C-a to C-d, plus C-e below.

## What this seat read at signing

| read | result |
|---|---|
| `git rev-parse origin/wk-AMGT_HARVST-133-r78` | `4b0475b646...`, the head the COO half names (C-a holds now) |
| `git diff --stat 878f9466df 4b0475b646` | 5 files, +567 -27: the driver +75, the runner +127, the test +241, the proof and the investigation rows. This matches the half |
| base `878f9466df` | an ancestor of `origin/box/dell1` |
| driver default | `continue_on_pair_error=False`. Every new branch sits under that flag, so a leg run without it behaves as before |
| runner write surface | one new file, `<state-dir>/cycle_runner.log`, opened for append. The driver gets `--continue-on-pair-error 1`. No S3 and no new subprocess target |
| site-Z process census (Win32_Process, `cycle_runner\|backfill_driver`) | 1 row: PID 10928, created 04:57:52 local, `--state-dir` under `wk-harvest-runner-pin-c1be67f53c`, the PINNED worktree (`git worktree list`: c1be67f53c, detached). Positive control: 70 `python.exe` rows were seen by the same read. **No leg runs from the shared tree** |

## Blast radius at site Z

The merge lands on `box/dell1`. Site Z first sees the code at its own box-sync, in the shared tree. The pinned runner does not move,
because its re-pin is a separate act under its own pair. A shared-tree leg started after that sync without the flag runs as before,
except that it keeps `detail` and resolves `out` at call time.

## Conditions

- **C-e (site Z's side of the act).** Before the box-sync that brings the merge into site Z's shared tree, the same census shows no
  `backfill_driver` or `cycle_runner` process whose command line points at the shared tree. This read belongs to `0.0.0_AB_MSTR~Z`.
  A positive control sits beside it: the pinned runner must appear in the same read.
- The residual in row D1-W133-S2 (re-queue reads only the newest cycle record) is accepted for this merge. Its fix goes to the
  round-78 analysis, as the half says. It does not hold the merge.

## Both branches

Both branches are as the COO half states them. If C-b fails, the merge is reverted with `git revert -m 1` on `box/dell1`, and site Z
takes the revert at its next box-sync. Until the re-pin, no site-Z process runs the merged code.

-- 1.0.0_SA_CTO~Z
