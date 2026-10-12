# SELF-DRIVE cluster open calls -- tick 11 (2026-10-12 20:00Z, cron 9c76a283) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Ticks covered: 10 (quiet, 19:15Z,
runtime line) and 11. Last committed log: tick 9 @d56b5e8165 (19:1xZ). Hourly-floor log carrying one delta.

## Measurements

- open rows: 11 (sitez 6, dell1 1, dell2 4, laptop 0), closed 89; fork 1 (sitez 1b36, a grant on the cited list), act 10. No new
  row since tick 8. inbox: 0 unread at both ticks. No unacked crossbox call to a laptop seat.
- The superseded-close verb worked across boxes: `XB-20261012T082300Z-d5e7` reads CLOSED-BOTH on origin/CLOUD, closed from-side by
  `2.0.0_SA_COO~B1` at 19:18:49Z with `to_by = superseded-by XB-20261012T174358Z-894b` -- so dell1 carried f8f29843ba within the
  hour and B1 ran it as relayed. (b312 not re-read this tick.)

## Calls since the last log

- RULED by the driver: 0 new. VERDICTS: CVO~L addendum @89c1366b5f (msg 108661): "marker in closed.to_by ACCEPTED for
  crossbox/1 (selftest 35/35 re-run)"; carry-forward for the CT-w-6 split: in crossbox/2 the superseded mark lives in sender file
  A, never in the recipient file's closed. Recorded here for the round that cuts CT-w-6.
- DESIGN FORKS at CRO research: 0. GOVERNANCE FORKS: 0 open.
- ACTS ONLY ANDREW CAN DO: 15 unchanged (tick-1 record section B).

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `check_inbox`; `python .tools/crossbox-call.py list --open`; `git show origin/CLOUD:<file>`;
`safe-commit.sh`.
