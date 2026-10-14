# self-drive sitez open calls -- ticks 9-10 (2026-10-14 04:50Z and 05:50Z), `1.0.0_SA_CTO~Z`

arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md` @ce0ba39d90
state: ARMED   cadence: 60m (cron 5032b669 at :41, confirmed by CronList 05:26Z)   ticks covered: 9 (quiet) and 10

## Measurements (05:50Z)

- inbox: 0 unread.
- open calls on sitez: 44 rows, 10 OPEN, all `act`, unchanged since tick 4.

## Calls ruled since tick 8

| call | ruling | carrier |
|---|---|---|
| MX-r-12 v2 (MI 33976) | CTO half SIGNED: catalog-only 43088464f5 on live 027fedfda4, the six legacy research rows (FWD-21 research 7 of 7) | @f0a6f0a8aa |
| r30 C3 re-sign #2 (O 33984) | RE-SIGNED at 90967e39ba on live 43088464f5; patch-id eac7550c45 unchanged | @0314607f88 |
| MCPINDEX round-11 slug (CVO 33987) | FWD-21 REALIZED on list v4; FWD-20 depth NOT for the second round (sample-only check). Round 12 = one cell graded on EVERY (a) tool, then park | @05caf1144b |
| Z-W34-S8 (safe-commit file types) | routed to the gate's owner NFRA_CTLPLN (laptop COO~C queued it for its round 14, msg 33991); site Z's workaround stands | msgs via MSTR~Z |

## ACTS ONLY ANDREW (OR A PERSON) CAN DO -- 10 OPEN rows, unchanged

The most time-bound is row 6c9f: the R2/R3 hold-lift yes or no, with the R2 revert at 10:30Z on no answer. Row 763e
(Terminal sign-in before 07:00 ET = 11:00Z) may already be met (DAPI UP at 21:14Z, row Z-S16).

## Completion test

NOT DONE. Stop: Andrew's stand-down.

## Compiler Tools

`check_inbox`, `.tools/open-calls.py list`, `CronList`, `git patch-id --stable`, the blob-equality check, `s3api head-object`
(live-base agreement). Gap: none.
