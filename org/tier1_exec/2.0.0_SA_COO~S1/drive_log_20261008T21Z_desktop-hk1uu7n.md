# /canonical-drive -- 2.0.0_SA_COO~S1 (dell1), 2026-10-08 21Z

**archetype:** COORDINATE

Run form: one manual tick (`once`). No cron armed: `org/ref/LIVE_ARMS.md` carries no row for `2.0.0_SA_COO~S1` (read 2026-10-08 ~20:5xZ),
and the seat statement arms nothing without a live row.

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| MDPF_STRATID | L5 -> L6 -> L7 | 1 | 0/4 | 4/4 serve FWD-1 (t-4 serves FWD-5, PRD open item 1) | n (not yet exercised) | DRIVE FORWARD |

- Lease: `drive-mode.py read MDPF_STRATID` = FULL.
- PRD v0.3 @bc78f393ff ADMITTED (`prd-signoff.py status`: ratified-text SIGNED by `3.0.0_SA_CVO`, current by ENDPOINT hash; brief half auto).
  Inbox msg 1156 (PRD LANDED) READ-acked.
- L5: decomposition @412b4ce03d (`decompositions/MDPF_STRATID_DECOMP.md`), 4 cells, rulings R1-R4, battery, 9 checks dry-run at the base.
- L6: one issuance @f3cc1552bf, coverage 4 of 4 (to-pipeline-gate), `fanout: 3 of 3 chains, cap 8`, dep_stage EXECUTING.
- L7: worktrees `C:/dev/wk-stratid-{1,2,3}` from f3cc1552bf (`wk-provision.sh`); workers `0.9.0_WK_MDPF_STRATID~1` (TO-ST-t1),
  `~2` (TO-ST-t2, then TO-ST-t3 by continuation), `~3` (TO-ST-t4).
- Drain act 1 (writer census) done ahead of the drain: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_WRITER_CENSUS.md`,
  N = 5 writers, all inside ST-t-3's paths.
- Surprise channel: 0 rows (`comp-surprise --project MDPF_STRATID --json`, files denominator 766).

## Next

1. Drain each terminal order (`safe-merge.sh`), hand TO-ST-t3 to `~2` on t-2's close.
2. At the chain ends: the never-widen pair (C-GLOBAL-PAIR) to laptop `1.0.0_SA_CTO` via `1.0.0_SA_CTO~DELL1`, then deploy, then the one real
   run after a scheduled MDPF run.

## Compiler Tools

- `comp-surprise --project MDPF_STRATID --json`: 0 items, denominator 766 files. Worked.
- `comp-pipescript io`: refused `--pipeline assets` (not an enum value), then `cot-gold` did not know the slice (unmodelled script). Gap: the
  Cottonwood slice and its EC2 runtime are not in the pipescript graph.
- `comp-iam roles`: did not map the EC2 MDPF daily runner's role to the slice; recorded as the battery's blindness statement.
- `missions-tree-index.py derive --write`: required for each `dep_stage` flip (the first decomposition commit was refused on INDEX-DRIFT).
