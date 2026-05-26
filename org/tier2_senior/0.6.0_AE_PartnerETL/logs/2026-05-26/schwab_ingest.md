# 0.6.0_AE_PartnerETL session log -- 2026-05-26

## Schwab ingest -- Andrew direct

Andrew direct 2026-05-26T~18:00Z: "I just downloaded the new schwab files, check your sys prompt for the converter and uploader scripts and get them in there."

Full 6-step §Schwab Ingest sequence per prompt.md lines 194-233 executed.

### Step 1 -- sync OneDrive -> S3

```
python data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py --upload
```

- Local CRS files: 1,712
- Existing in `s3://opal-data-schwab/01_raw/`: 6,771 -> 6,828
- Existing in `s3://opal-data-schwab/bronze/rps/`: 298 -> 303
- Uploaded: 57 to `01_raw/`, 5 *.RPS mirror to `bronze/rps/`

### Steps 2-6 -- silver converters (parallel)

| Feed | Cmd | New dates | Latest partition |
|---|---|---|---|
| ACC | `convert_schwab_acc_to_parquet.py` | 5 (20260518-20260522) | 20260522 = 6,956 accounts |
| RPS | `convert_schwab_rps_to_parquet.py` | 5 (20260518-20260522) | 20260522 = 90,588 positions |
| TRN | `convert_schwab_trn_to_parquet.py` | 10 (20260511-20260522) | 20260522 = 8,271 rows |
| ULN | `convert_schwab_uln_to_silver.py` | 10 (20260511-20260522) | 20260522 = 227,882 long lots |
| RLD | `convert_schwab_lots_to_silver.py rld` | 10 OK + 1 SKIP | 20260521 = 11,744 lots |

All five tables now extend through **20260522** (Friday). RLD latest = 20260521 (20260522 not yet available on Schwab side).

All converters idempotent, exit 0.

### Andrew summary MCP

`20260526T180241Z_0.6.0_AE_PartnerETL__ANDREW-DIRECT__Schwab_ingest_complete_-` delivered to 0.0.0_AB_MSTR per prompt.md line 233 ("After the run, message Andrew with: number of new files synced, list of new silver date partitions per table, latest silver date for each table").

### Downstream

DS 0.4.0_DS_ClientPlatform unblocked for BD <-> Schwab reconciliation on the new partitions per §Schwab Ingest closing line.

### Session ops

- /watcher self-heal complete; tracked watcher task `bdfmg8477` (PID 231006); VERDICT PROCESS-OK
- broker registration LIVE
- `/work 20m` cron armed (job `4b65bbe7`, fires :07/:27/:47)
- DT 0.4 inbox msg 20260513T223353Z stale-log ask -- superseded by `bf553ae3b log(0.6.0_AE_PartnerETL 2026-05-07): schwab MAY ingest (commit-on-behalf -- AE 0.6.0 offline)`; ACKing DT
- DT 0.4 inbox msg 20260526T173247Z ADVI_DEMOV1 UAT 3 findings -- FYI-CC only (COO is routing authority per body); banked; standing for COO dispatch on F1/F2 (AE-scope), F3 routes to DE per body
