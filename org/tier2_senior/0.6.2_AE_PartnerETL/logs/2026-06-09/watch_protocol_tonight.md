# Tonight's Watch Protocol — 0.6.2_AE_PartnerETL — 2026-06-09

## Sequence (all UTC)

| Time | Event | Owner |
|---|---|---|
| ~23:00Z | GLDINC nightly chain fires | AE coverage (0.6.0_AE offline) |
| ~23:00-23:30Z | Chain log check + P1 shadow verify | This session |
| RAVC2-A | Chain outcome → COO + 0.4.0_DS | Post-chain |
| 02:00Z | cot-bd-session-daily (OIDC session refresh) | Auto |
| 02:30Z | cot-bronze-daily-trigger (bronze ingest) | Auto |
| ~02:45Z | COT bronze run verify → RAVC2 COO | Track A |
| Post-RAVC2 | Manual opal-cot-silver-run trigger | Track B Phase 3 |
| Post-run | Silver row count verify → RAVC2-B COO | Track B Phase 3 |

---

## GLDINC nightly watch checklist (~23:00-23:30Z)

### 1. Chain log location
- S3: `s3://opal-data-bd/logs/gold-layer/gold_incremental_{run_date}_{timestamp}.log`
- EC2: `/tmp/gold_logs/{CHAIN_LABEL}_{TIMESTAMP}.log` (i-01003b035d2988dfb)

### 2. P0 mode checks (incremental)
- **A_00**: grep for `--incremental` flag + `_last_txn_file_date` watermark line
  - Confirm: `[GLDINC-P1-SHADOW] windowed_rows=X oracle_rows=Y`
- **C_06**: grep for `--incremental` + `gold/client_timeseries/_watermark.json` read
- **B_00**: grep for `FORCE-RECENT: last 14 calendar days re-processed`
- Header: confirm `Mode: incremental` (not `full-recompute`)

### 3. P1 shadow (post-chain)
- Script: `data/black_diamond/scripts/gold/gldinc_p1_shadow.py`
- Grep chain log for: `[GLDINC-P1-SHADOW] run_date=`
- Status: non-fatal if errors — log the error, do NOT block RAVC2
- Scorecard S3 key: `s3://opal-data-bd/gold/_parity/load_flows/{run_date}/scorecard.json`

### 4. Scorecard fields to report (all targets)
| Field | Target | Action if missed |
|---|---|---|
| `key_set_symmetric_diff` | 0 | ESCALATE immediately |
| `row_count_delta` | 0 | ESCALATE immediately |
| `exact_match_rate` | 100.000% | ESCALATE immediately |
| `max_abs_diff` | ≤1e-6 | ESCALATE immediately |
| `targets_met` | true | DIVERGENCE → STOP |
| `clean_night_counter` | advancing toward ≥5 | track |
| `fallback_stall` | false | WARN if true (≥3 consecutive) |

### 5. RAVC2 to COO + 0.4.0_DS includes
- P0 mode confirmations: A_00 incremental ✓/✗, C_06 incremental ✓/✗, B_00 --force-recent-days 14 ✓/✗
- P1 shadow: fired ✓/✗, errored (if so — log message), scorecard values if emitted
- clean_night_counter value

---

## COT bronze watch checklist (02:00Z/02:30Z)

### Sources to check post-run
- Lambda CW logs: `/aws/lambda/cot-bd-session-trigger`
  - 02:00Z invocation: mode=session-refresh → look for SM write confirmation
  - 02:30Z invocation: mode=bronze-run → look for SSM dispatch to i-0643a5bee8a8feabf
- SSM run log: `s3://opal-data-cot/logs/cot-exporter/bronze-run/cot-bronze-run-{datetime}.log`
- S3 artifacts: `opal-data-cot/forwardfill_v2/transactions/TRANSACTIONS_DAILY_{date}.xlsx`
                  `opal-data-cot/forwardfill_v2/allocations/ALLOCATIONS_DAILY_{date}.xlsx`

### RAVC2-A to COO includes
- Session refresh: PASS/FAIL
- Bronze ingest: PASS/FAIL
- Row counts per table (transactions, allocations)
- Any SSM errors
- S3 LastModified on xlsx artifacts

---

## Post-bronze: silver trigger

```
aws ssm send-command \
  --document-name opal-cot-silver-run \
  --instance-ids i-0643a5bee8a8feabf \
  --parameters '{"RunDate":["YYYY-MM-DD"]}' \
  --region us-east-1 \
  --comment "ADVI_COTETL first silver run post-bronze-PASS"
```

Verify: `s3://opal-data-cot/silver/transactions/{date}.parquet` + `silver/allocations/{date}.parquet`
Target: ~$372.9M AUA / 642 account-grain rows on allocations
