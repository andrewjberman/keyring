# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 09Z-10Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by presence); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 09:0x | IRPT_BCKEND~Y Y-6 | ~D: the run 3-4 list misses are local transit (dev proxy under CPU load); run 4 backend join | ad911f26a6 |
| 09:2x | IRPT_BCKEND~Y Y-6 | Y6_BACKEND_SUMMARY.md (runs 1-4: 15m07s of each job is the 900 s release) | 90a573a726 |
| 09:29 | IRPT_YCDGEN L9/L10 | CVO grade @d6f334c003 (m-4.AC3 FAIL narrowly; FWD-2 not realized by a changed request); slug to the CTO | -- |
| 09:40 | IRPT_YCDGEN L10 | CTO round-4 analysis @a1b47e6b3f: FWD-6 binds the Overview at 12 requests (2 windows) | -- |
| 09:5x | IRPT_YCDGEN L6 | ONE issuance: r-5, p-5, h-5, m-5, w-5 (join); 12 checks FAIL at the base | 2f901c0a21 |
| 09:40, 10:07 | IRPT_BCKEND~Y Y-6 | runs 5-6 (Multi-Comp) READY; each read-back drew the firewall challenge, absorbed by the release | 2de858a8a8 |
| 10:1x | fabric | C: full (1.9 GB free): all four worktree adds failed; my drained wk-ycdgen-2 removed (2.5 GB); MSTR asked to drain 12 merged worktrees (~30 GB) | msg 10:34Z |
| 10:4x | IRPT_YCDGEN L7 | four SPARSE worktrees (0.6 GB each) and workers ~1-~4 spawned | -- |

Next:
- the round-5 workers, then merges per chain end; w-5 after p-5 and h-5;
- E4 live: one indexed level-series run on the merged runner, then the identical request after today's close;
- E6 live: the budgeted Overview, rendered, timed, link to Andrew;
- Y-6 runs 7-10 (~D); the firewall-window probe after Y-6.
