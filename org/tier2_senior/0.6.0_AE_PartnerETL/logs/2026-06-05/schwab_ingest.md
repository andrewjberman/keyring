# 0.6.0_AE_PartnerETL~A session log -- 2026-06-05

## Schwab ingest -- Andrew direct

Andrew direct 2026-06-05: "run the converter/upload function for the new Schwab files. Last time we had gotten schwab files was 5/26, now we have data up to june 4."

Full 6-step §Schwab Ingest sequence per prompt.md lines 194-233 executed. Prior ingest (5/26) carried partitions through 20260522; this run extends all five tables through **20260604**.

New business dates ingested: 20260526, 20260527, 20260528, 20260529, 20260601, 20260602, 20260603, 20260604 (8 trading days).

### Step 1 -- sync OneDrive -> S3

```
python data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py --upload
```

- Local CRS files: 1,803
- `01_raw/`: 6,828 -> 6,919 (**91 uploaded**)
- `bronze/rps/`: 303 -> 311 (**8 *.RPS mirrored**)

### Steps 2-6 -- silver converters (parallel)

| Feed | Cmd | New dates | Latest partition (20260604) |
|---|---|---|---|
| ACC | `convert_schwab_acc_to_parquet.py` | 8 (20260526-20260604) | 6,996 accounts |
| RPS | `convert_schwab_rps_to_parquet.py` | 8 (20260526-20260604) | 91,429 positions |
| TRN | `convert_schwab_trn_to_parquet.py` | 8 (20260526-20260604) | 24,502 rows |
| ULN | `convert_schwab_uln_to_silver.py` | 8 (20260526-20260604) | 242,701 long lots |
| RLD | `convert_schwab_lots_to_silver.py rld` | 8 OK + 1 SKIP | 424 lots |

RLD SKIP = 20250109 (no DL rows; historical, unrelated to this batch). All converters idempotent, exit 0, OK=8 each.

### Verification

S3 confirm of `date=20260604/data.parquet` for all five tables (LastModified 2026-06-05 13:xxZ, all non-zero):
- acc 428,271 B | rps 1,418,699 B | trn 402,799 B | uln 5,769,242 B | rld 58,102 B

All five tables extend through 20260604. RLD non-optional (B_02.canonical_lots.py primary realized-lot tax source) -- present through 20260604.

### Downstream

- Andrew notified directly (in-session) + MCP summary to 0.0.0_AB_MSTR per prompt.md line 233.
- DS 0.4.0_DS_ClientPlatform notified: new partitions through 20260604 available for BD <-> Schwab reconciliation.

### Session ops

- /watcher self-heal complete at load; Monitor re-armed once after an expected exit-143 SIGTERM mid-ingest (task bye1msz6y); lossless, inbox empty throughout. Not escalated (per LD-0146 caveat).
- broker registration LIVE.
