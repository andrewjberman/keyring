# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-08 23:4xZ -> 2026-10-09 01:00Z (host opal_bloomberg)

**archetype:** COORDINATE

Lease FULL on every tick.

| tick | time (Z) | limb | TOs t/T | outcome |
|---|---|---|---|---|
| 2 | 10-08 23:47 | L7 r7 | 6/7 | NO-OP: MX-s-19 gated on the 10-12/10-13 reads |
| 3 | 10-09 00:00 | L7 r7 | 6/7 | NO-OP: the 10-09 runner run was still in flight |
| 4 | 10-09 00:35 | L7 r7 | 6/7 | NO-OP on the limb; off-task row Z-S84 filed |
| 5 | 10-09 01:00 | L7 r7 | 6/7 | NO-OP: inbox empty, no project commits since Z-S84 |

- **Second live run of the MX-s-18 code (2026-10-09 00:00Z).** It printed `OK: bronze sentinel emitted for 2026-10-09
  (tables=[transactions, realized])` after the read-back; RESULT failed=[]. This is not a graded read: the A2 reads are
  Monday 10-12 and Tuesday 10-13.
- **Row Z-S84 @248f3efc04 (OBSERVATION, INERT).** The txn chunk sweep's older restatement chunks fail HTTP 401 at the
  tail of the run on 2 of 2 runs read. Cause: `cot_bronze_ingest.py:802-834` reuses one bearer and never re-mints.
  The engine is under data/cot/, outside this lane.
- **Msg 32164 read and acked** (the law edit making per-box branches official). No act for this lane: commits
  already go to box/sitez.

## Open

- MX-s-19: GO to 0.7.0_AE_CloudOps~Z after the Monday 10-12 and Tuesday 10-13 reads both pass.
- Round-7 L8 compile and slug: after MX-s-19.

## Compiler Tools

- `comp-surprise --armed`: 14.
- `comp-find "self-heals next run" --limit 10`: ran past 120s and was backgrounded. Native Grep on data/ found the
  source instead.
- `.tools/aws logs get-log-events`: the 10-09 run.
- `safe-commit.sh`: Z-S84 committed first try.
