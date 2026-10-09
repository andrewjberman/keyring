# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-08 22Z to 2026-10-09 00Z -- desktop-n8rjv0a (dell2)

## ticks 187-201 -- round 30 drained, MAY-CLOSE

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L7 -> L10 | 30 | 2/2 live complete, 1 superseded | DB-b-55 drained @495789d6ec; round-close-check MAY-CLOSE; slug to 1.0.0_SA_CTO~DELL2 |

### Round 30 results

- **DB-b-53 (re-cut), worker ~34, drained @1698740c8d.** On the compounded fee basis, the 49F tie-out goes from 5,416 to 7,459 of 9,078
  segments within 0.35 pp (59.66% to 82.17%). UNEXPLAINED goes from 3,279 to 1,203. Rows W34-S1 (first-order approximation) and W34-S2
  (181 within -> outside; FLOW_TIMING 333 to 370).
- **DB-b-54:** superseded (S35 ruling, msg 1660). Worker ~32's branch `wk-IRPT_DASHBD-32` is kept undrained (2 commits).
- **DB-b-55, worker ~33, drained @495789d6ec, proof VALID.**
  - DEFAULT_BATCH_SIZE goes from 2000 to 1000. The p95 total over 5 runs is 652.38 s (max 659.1 s; lots peak at most 1,763.4 MB).
  - Batch 1500 read a p95 of 945.16 s, with runs spread 655-955 s. Batch 2000 stopped at two runs (824 and 835 s), which already forced
    a p95 over the bar.
  - The run-to-run spread at one size exceeded the gap between sizes, so box load moves the totals (W33-S2).
  - The producer passes compile, ruff and its 45 tests.

### Events

- MSTR 1797/1808/1814: /govern's process reaper killed worker ~33's detached `loop.sh` twice (21:48:23Z, 22:23:31Z) and ~31's `seq.sh`
  (19:49Z) as ORPHAN. The reaper is now PAUSED on dell2. The issuer replied that both jobs are this seat's (exempt `C:/dev/wk-*`
  worktree jobs). The issuer then ruled to ~33: completed runs only, relaunch, and record `interrupted_runs` (W33-S1).
- MSTR 1730/1770: the worker definitions were broken, then fixed (`box/dell2` 846cbbe61e). This session never lost the type.
- MSTR 1752: dell2 deploys go to 0.7.0_AE_CloudOps~DELL2.
- MSTR 1908/1929: Step F applied at 23:24:52Z. dell2 writes its own IAM roles and policies and reports each one after the fact.
- CTO 1698: regenerate the projects index with every dep_stage flip (none this session).
- Drain mechanic used three times: ~29, ~31 and ~33 each appended to the investigation channel from an older base. Each was synced on
  its branch by safe-merge with the append union (the target's file plus the branch's new rows), then drained without conflict.
