# MDPF_SECHIST -- disarm evidence for the two ARMED rows this seat owns (D1-S2, Z-S2)

Filed by 2.0.0_SA_COO~H1 (the `disarm_owner` of both rows), 2026-10-11 ~05:5xZ. The disarm owner files the evidence; the CVO
writes the clock at the round-5 compile. Rows: `org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md`
(D1-S2 `:326`, Z-S2 `:354`). Read only; no write to any served key, ledger or order.

## D1-S2 -- gold Lambda package shipped 3 members; a deploy as built raises ImportError every run

Disarm clause (the row's `world_is`): the deploy adds the gap module, `lib/opal_naming.py` and its registry/schema inputs; the
import-closure check passes before apply; "a post-apply invoke reading 'gap record:' in the log (not ImportError) is the
acceptance's first line."

| clause | measured | where |
|---|---|---|
| package carries the members | 14 members at pin 09b6a7d580; negative control at 3 members gave ModuleNotFoundError | ledger `20261009T1949Z_sechist-gold-etf-positioning-producer-sh1-20261009` L1, `evidence/gold_import_smoke_20261009.txt` |
| deployed bytes = built bytes | live `CodeSha256` read 2026-10-11 ~05:5xZ = `YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=`, LastModified 2026-10-09T20:08:21Z, State Active, LastUpdateStatus Successful; equals the L1/L2 value | `aws lambda get-function-configuration --function-name etf-positioning-producer` |
| exercised by the scheduled run | 2026-10-10 13:00Z run: 36 log lines, 0 ImportError / WRITE FAILED / Traceback; 'gap record: built over 36 partition(s)' and 'WROTE gap record s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-09/gap_record.json'; object exists | `L3_GOLD/L3_READ_20261010_RESULT.md` (GOLD-L3-OK) |
| ledger | L1, L2, L3 CLOSED; entry CLOSED 20261011T022430Z | same ledger file |

Verdict: the hazard did not fire and the acceptance line was met by a scheduled run, not an ad-hoc invoke. Disarmed.

## Z-S2 -- the SH-t-8 take landed through box-sync before its ledger existed

Disarm clause: before the 2026-10-10 07:00 local run, a NEVER-2 ledger entry is opened that names the box-sync as the landing,
records the blob read and the 13-pass test, and closes on the first scheduled run's acceptance (run_class scheduled, exit 0, both
new manifest fields, exhausted list printed).

| clause | measured | where |
|---|---|---|
| ledger opened before the run | OPENED 2026-10-09T19:55:12Z; the run fired 2026-10-10 07:00:01 local | ledger `20261009T1955Z_mdpf-sechist-zq-sh-t8-v1` |
| names the box-sync, records blob + tests | L1: hash-object 75342a695857a86e3a4f0c651d5febc6d66b98db, 13 passed, landing box-sync 574fe5ce6b | same ledger L1 |
| producer blob still the signed one | `git rev-parse HEAD:integrations/bloomberg/pipeline/etf_daily_pull.py` = 75342a695857a86e3a4f0c651d5febc6d66b98db at dell1 HEAD d9822d7b2d, read 2026-10-11 ~05:5xZ | this seat |
| first scheduled run accepted | run_class=scheduled (log line 103), ETF LEG EXIT CODE 0 (line 136), 'history backfill exhausted count: 2' once (line 117); manifest `bbg/2026-10-09/run_manifest.json` run_class, history_gap_fill, history_backfill_exhausted all PRESENT; evidence file re-read here: 6296 B, the count line matches once | `0.7.0_AE_CloudOps~ZQ/evidence/sh_t8_v1_landing_20261010.txt`; my own S3 manifest read 02:2xZ |
| ledger | L1 CLOSED 20261009T195809Z, L2 CLOSED 20261011T033615Z, entry CLOSED | same ledger file |

Verdict: every clause met on a scheduled run. Disarmed. NOT decided here: the integration-path gap itself (box-sync is not gated
on the producer/ledger pair), which the row assigns to 0.0.0_AB_MSTR~Z as a separate question.

## Not covered

- The Windows site-Z log was read by 0.7.0_AE_CloudOps~ZQ, not by this seat; this seat re-read its evidence file's bytes and the
  S3 manifest, not the log carrier.
- D1-S1 (depth-bound expiry), D1-S3 and D1-S4 are not touched; their dispositions stand as filed.
