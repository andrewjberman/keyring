# Deploy-Completion Ledger -- bd A_01 advisor_assignments full->incremental flip

- **Opened:** 2026-06-24T20:35Z (deploy-start)
- **Owner:** 0.7.0_AE_CloudOps (commit+deploy lane; gold_dispatch.sh = CLOUD_OPS_OR_ETL)
- **Authored by:** 0.4.0_DS_ClientPlatform (DS A1 layer-walk finding; owned-paths blocked DS commit -> AE commit+deploy)
- **Authority:** Andrew-direct (routed to 0.7.0_AE base 20260624T2040Z), ready-to-execute
- **Status:** HELD-VERIFY-PENDING -- owner: 0.4.0_DS_ClientPlatform -- re-read: the next nightly served-SCD run
  > Re-stamped 2026-08-26 by `2.0.0_SA_COO`. Prior text preserved: *"DEPLOY LANDED (closed 2026-06-24T20:38Z) -- served-SCD verification pending next nightly (DS)"*. **APPLY IS COMPLETE** (deploy closed 20:38Z, legs 1-5 all `[x]`); **one VERIFY leg pends a named future event under a named owner.** `LANDED` is a COMMIT-state word and is NOT terminal for a deploy ledger (COO ruling 72636 s.2), which is why this read OPEN for 1,509h -- the axis had no value for *apply-done, verify-pending*. It does now (`HELD-VERIFY-PENDING`, @67dc16081a). **Nothing is half-landed.**

## Change
`data/black_diamond/scripts/gold/gold_dispatch.sh` CATALOG line 80:
`A_01|A_01.advisor_assignments.py|--upload` -> `... |--upload --incremental` (1 token, bd ONLY).
Stops a nightly 1,815-file FULL rebuild of the 15,292-row SCD; the proven incremental runs instead.

## Grounding (verified by AE before deploy -- NOT producer self-report; Rule 22)
- Parity scorecards EXIST 10 consecutive nights (s3://opal-data-bd/gold/_parity/advisor_assignments/ 2026-06-15..06-24).
- Latest scorecard (06-24) = `identical: True, cell_mismatches: 0` (byte-parity proven).
- bd A_01 HAS the incremental machinery: `--incremental` argparse (A_01:790) + branch (816/824) + `save_aa_state` (574, both modes -> caches pre-written, no cold-start) + `_load_aa_watermark` (552) + shadow self-test (694-725). The flag is CONSUMED, not errored.
- SCOPE = bd ONLY. cot A_01 + inf INF_A_01 forks have ZERO incremental code -> NOT flipped (would break their argparse).
- Restatement/cold-start self-falls-back to full (graceful).

## Deploy sequence
1. [x] edit line 80
2. [x] safe-commit (AE author 316202d69) + push CLOUD
3. [x] aws s3 cp gold_dispatch.sh -> s3://opal-data-bd/code/gold/ (EC2-runner pull path)
4. [x] verify: re-pull from S3 -> line 80 = `--upload --incremental`; deployed S3 == local committed (byte-identical)
5. [x] RAVC DS (2026-06-24T20:38Z) -> DS deploy-verifies the served SCD unchanged on the next nightly
6. [x] close this ledger (AE side complete; DS owns the next-nightly served-SCD verify)

## Validation posture
NO ad-hoc gold run (CLAUDE.md). The next SCHEDULED nightly uses incremental; DS deploy-verifies the served
SCD is unchanged (or the GLDINC shadow stays PASS). Served-SCD-unchanged = success.
