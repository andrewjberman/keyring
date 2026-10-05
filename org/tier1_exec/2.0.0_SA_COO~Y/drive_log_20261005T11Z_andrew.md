# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-05 11Z-12Z (host andrew)

Leases: IRPT_BCKEND~Y FAST (renewed by presence); IRPT_YCDGEN FULL (issuer ~Y).

| tick (UTC) | project, limb | act fired | evidence |
|---|---|---|---|
| 11:03 | IRPT_BCKEND~Y Y-6 | run 7's inputs POST 500: generate's log shows it never invoked (local proxy) -- to ~D | -- |
| 11:15 | fabric | C: at 883 MB free and falling: [STUCK] to MSTR (12 merged worktrees ~29 GB) | msg 11:15Z |
| 11:2x | IRPT_BCKEND~Y Y-6 | backend joins for runs 5-6 (before the HARs are reclaimed) | Y6/run05-06 |
| 11:3x | IRPT_YCDGEN L7 | sparse worktrees blocked org/missions commits (INDEX-ORPHAN): widened to every mission home; a fresh ~1 re-landed r-5's proof and row with no override | bcb83344c1 |
| 11:4x-12:0x | IRPT_YCDGEN drain | m-5, r-5, p-5 merged; orders closed with rulings (W1-S2, W2-S7/S8/S9) | bb0c22bd1e, 84a7af1854, 306a315dc9 |
| 12:15 | IRPT_YCDGEN E4 | leg 1 live in ~D's freed slot: PLAN requests=2, COMPLETE; the lookup printed the kept level series live (no_previous by contract) | YCD-R5-E4-20261005T1215Z |
| 12:2x | fabric | MSTR reclaimed C: on Andrew's word (35 GB free); the sweep cleared this seat's scratch (tools rebuilt from git) | msg 105257 |
| 12:3x | IRPT_YCDGEN drain | h-5 merged (86 OPAL_HELD, 72 NOT_HELD; W3-S7 ruled); p-5 and h-5 closed; w-5 spawned on a full worktree from 79452258c9 | a979784ea4 |
| 12:4x | fabric | free space fell 36 -> 22 GB in 25 min, then held at 22.1 GB (other seats' new worktrees) | df reads 12:39-12:46Z |

Next:
- w-5 (join), then E6: the budgeted Overview live, rendered, timed, link to Andrew;
- E4 leg 2 after today's close reaches YCharts;
- the round-5 packet to the CVO;
- Y-6 runs 7-10 (~D); the firewall-window probe after Y-6.
