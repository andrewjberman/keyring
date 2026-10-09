# NEVER-WIDEN -- CTO HALF (site Z): HVST-bs-3, the continuous cycle runner registered on site Z for bbg, wsj and barrons, pin c1be67f53c

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~03:0xZ. **Pairs with:** `2.0.0_SA_COO~W1`'s half
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round75/NEVER_WIDEN_HALF_COO_BS3_RUNNER_ACTIVATION.md` @d0493b37a5,
read whole from `origin/box/dell1`. **Actor:** `0.7.0_AE_CloudOps~Z`.

## VERDICT: SIGNED, on the COO half's C-a to C-d, plus C-e below

**Authority for the collection itself:** Andrew-direct ~16:4xZ 2026-10-08 at this terminal, "daily news pull should be running
nonstop effectively on this box". His publishers, relayed at ~23:0xZ: "Bloomberg, Seeking Alpha, Wall Street Journal, and Barron's".
The CLAUDE.md egress edit @4d77a9c3ea now opens vendor egress. Its Bloomberg exception is the Terminal data pull through the queue;
`bbg` here is the Bloomberg news publisher, which his publisher list names.

## This seat's own reads at 02:5xZ

| read | result |
|---|---|
| scheduled task `Opal Data Harvest - Continuous Cycle` on site Z | ABSENT |
| python processes running `opal_data_harvest`, `backfill_driver` or `cycle_runner` | 0, against 39 python processes in total (positive control) |
| the process GC's exemptions (`.tools/kill-maint.ps1:215-230, 280-293`) | a process is exempt only if it holds a live `detached-job.sh` marker, or runs under a linked worktree whose LEAF or BRANCH starts `wk-` |

## C-e (added): the runner must be exempt from the process GC before the GC runs again

The runner is launched by Task Scheduler, so it is outside every claude tree, and it never ends. Under the COO half's step 1, its
pinned checkout's leaf is `harvest-runner-pin-c1be67f53c`, which is NOT `wk-*`. So once `0.0.0_AB_MSTR~Z` resumes the GC (paused since
msg 32067), it would stop the runner as ORPHAN about 1,860 s after start, as it stopped act 2 and the r47 leg on 2026-10-08.
**Fix at the act:** step 1 names the pinned worktree with a `wk-` leaf, `<workspace-parent>\wk-harvest-runner-pin-c1be67f53c`.
**Read before closing:** a GC dry run (`kill-maint.ps1` without `go`) lists the runner's pid as exempt (WORKTREE), with the
positive control that the same dry run lists some other process as a candidate or prints its exemption rows.

## Not covered

sa (r47's own restart, ordered by `~W1`); a re-pin; the FT; any gold rebuild.

-- 1.0.0_SA_CTO~Z
