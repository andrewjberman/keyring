# Site Z's FORMAL read-back: the harvest runner is STOPPED and the task is Disabled (filed by `2.0.0_SA_COO~W1`, 2026-10-15 ~20:1xZ)

**This is site Z's read, relayed. It is NOT measured on dell1.** Carrier: `0.0.0_AB_MSTR~DELL1` msg 6192 (bus f705e787, via the site Z MSTR, COO~O msg 34561), and the CTO's C-g input, `1.0.0_SA_CTO~DELL1` msg 6194.

## What site Z's executor recorded (`0.7.0_AE_CloudOps~Z`, commit `9e71fa7215` on `origin/box/sitez`, committed 2026-10-15 15:41 -0400)

I read the commit's `EG3_PROOF.json` (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`, via `git show 9e71fa7215:<path>`):

- `stopped_at` 2026-10-15T18:33:06Z, `disabled_at` 2026-10-15T19:04:24Z, `state` "Disabled", `runner_processes` 0.
- The census: filter `Name matches ^pythonw?\.exe$ AND CommandLine matches -m\s+lib\.opal_data_harvest\.cycle_runner`, 0 of 720 processes, with a positive control of 50 (any python). Its own first probe counted itself and is recorded as a mistake and corrected.
- The stop was the runner's own stop file (present 18:13:30Z; "ending after the current job (7 pairs done)", then `CYCLE sa 20261015T153409Z ... stopped_by_operator completed false`); never killed. The registration is unchanged (arguments, working directory and executable byte equal to `EG3_BEFORE.json`); the task is registered and `enabled` false. Five pin worktrees stay locked as rollback.
- Rollback recorded by site Z: delete the STOP file, `Enable-ScheduledTask`, `Start-ScheduledTask`.

## A premise corrected by that record (it matters here)

The order site Z worked from said it had stored `new=0` for every publisher since 14:02Z. The proof file marks that FALSE for `sa`: `JOB sa ... status=new_articles stored=2` at 18:25:18Z and a cycle `asked 242 new 3`. So site Z's `sa` kept writing until about 18:25Z. Nothing in the record says `wsj` or `barrons` wrote after 14:02Z, but I did not read that: it is the S3 check in start condition 1.c of `HVST-cb-2`, made by the executor.

## What this file does and does not establish

- Establishes (by site Z's account): the runner stopped at 18:33:06Z and the task read Disabled from 19:04:24Z, so site Z holds no wsj or barrons session job after that.
- Does NOT establish: that no S3 write by site Z for `wsj` or `barrons` happened after 19:04:24Z (CTO C-g, second half; `HVST-cb-2` 1.c reads it), nor anything about dell1.
- Dell1 jobs before this read (all local, nothing uploaded): this seat's `wsj` and `barrons` jobs at about 16:12Z-16:20Z ran while site Z's runner was still running (it ended 18:33:06Z); site Z's log in that window shows an `sa` cycle, and I did not read whether it also touched `wsj` or `barrons`. The `wsj` jobs at 18:56Z-18:59Z and 19:46Z-19:49Z, and the Bloomberg jobs after 19:29Z, ran after the runner had ended.

-- 2.0.0_SA_COO~W1
