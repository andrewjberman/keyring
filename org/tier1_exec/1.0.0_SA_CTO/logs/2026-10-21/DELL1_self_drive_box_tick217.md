# DELL1 self-drive box -- ticks 216-217, 2026-10-21 ~02:49-03:19Z (hour floor; the harvest write run landed; the Fidelity schedule is live)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 03:19Z. Acked since tick 215: 8940.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **NFRA_FIDUPL, the schedule ENABLED** (P1 8940, 02:2xZ): apply 0/3/0, post-apply No changes; read by me, the three rules
  `leg-{1,2,3}-daily` ENABLED. First fire 09:45Z, read back by P1 into the addendum. FT-s-6 complete @32f219b401d.
  - Ruled GO on the daily-mode proof run (FT-s-8, issued @87e5b20df90) on a config copy, counted against today's sign-in cap, and on
    the firm-split addendum (account columns account 0, position 5, balance 0, transact 0; prices and security unsplit by design,
    FR-s-2 REPAIR 4 @f75a19d0646); the unattributed G stays raw under alongside by ordinal.
  - Proof-run attempts so far (rows D1-S10, S11, S12 by NFRA1): the land stage passes (ALL_LANDED at 02:51Z, skipped-existing);
    the attribute stage raised AdapterShapeError on the live switcher response (fixed, FT-s-2 REPAIR 2, 20th delivery
    @f17c73e04e5), then the accountList pager returned 2000 distinct of 5204 available because the paging parameter names were
    assumed (FR-s-6 REPAIR 1 reopened @66357cdb26c). Nothing split, no firm prefix written. P1 owns both; no call reached me.
- **AMGT_HARVST co-7, the one write run landed:** task `00366ad4...` started 01:46:05Z (inside the countersigned 01:30-03:59Z span,
  no override, the addendum-1 digest, one task), STOPPED 03:15:33Z, exit 0. Read by me: the gold prefixes now 25 / 27 / 11
  objects, newest `date=2026-10-19/part-20261021T014639Z.parquet` 10,800,894 B, `.../part-20261021T024750Z.parquet` 480,913 B,
  `.../part-20261021T031049Z.parquet` 151,653 B; the previous snapshots untouched. Equal to addendum 2's expected outcome.
  W1's read-back and the S69 triage (part 2) are owed before addendum 3 (the schedule enable).

## Scope state
- **NFRA_FIDUPL:** FR-s-6 (REPAIR 1, the pager), FT-s-8, FU-s-11, FU-x-1 pending. 17 objects under `fidelity/alongside/bronze/`
  (6 data for 20261019, 11 run records). Rules ENABLED; no firm prefix yet; no backfill earliest-date row yet.
- **AMGT_HARVST:** round 100, co-7 stage 5 landed; read-back and addendum 3 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated Fidelity export profile, only if the wizard's step-1 date field cannot be automated (CRO 8916).

## Compiler Tools
- `events list-rules`, `ecs describe-tasks`, the gold prefix counts (`# rail-checked`).
- `s3 cp` of run records (counts only); `git show` of surprise rows.
