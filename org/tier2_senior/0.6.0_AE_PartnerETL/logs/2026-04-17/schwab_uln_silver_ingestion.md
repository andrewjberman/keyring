# Session Log -- Schwab ULN silver ingestion

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-17
**Session purpose:** Build silver/ULN/ from Schwab custodian unrealized gain/loss files to give B_01 a second open-position authority (parallel to BD silver/unrealized). Per DS brief `docs/briefs/ae-brief-schwab-uln-silver-ingestion.md`.

---

## Phase Overview

| Phase | Action | Outcome |
|---|---|---|
| 1 | Startup: register + inbox catchup + read prev log (CP-AE1) | Inbox empty; prior session context loaded |
| 2 | Inspect real ULN file structure in S3 (raw + anonymized + mapping JSON) | Pipe-delimited, H1/H2/H3/DL/T1 record types; 349 STANDARD + 217 GLACIER in 01_raw/ |
| 3 | Confirm DL column positions empirically (brief table was off-by-1/2 after col 22) | Fixed 0-indexed positions: current_quantity=22, long_short=23, unrealized_gain_loss=35 |
| 4 | Chose 01_raw/ only (full 566-date coverage with original account_ids; 02_anonymized partial + needs mapping round-trip) | Simpler + authoritative; matches RPS converter pattern |
| 5 | Wrote `convert_schwab_uln_to_silver.py` — ProcessPoolExecutor(8 workers), idempotent, positional column extract, L-only filter, numeric/date parse | py_compile clean |
| 6 | Dry-run on 2026-04-15 | 213,253 long lots / 3,621 accounts / 99.97% cusip coverage; unrealized G/L sum = $68.77M |
| 7 | Kicked off parallel backfills (Windows ProcessPoolExecutor spawns detached workers — had 34 concurrent workers across multiple invocations) | Idempotent, no conflicts |
| 8 | Final foreground run cleaned up 2 S3 read-timeouts on large 2026 files | OK=21, re-ran --date for 20260320 and 20260410 → OK |
| 9 | Verified final count | **349 STANDARD partitions** (2024-01-12 → 2026-04-15); 217 GLACIER dates deferred for restore |
| 10 | Updated `prompt.md` Schwab Ingest section to include ULN converter in roll-silver-forward sequence | Forward-compatible for next AE session |

---

## Compiler Tools

| Phase | Tool | Command | Result / rationale |
|---|---|---|---|
| 2 | awk | `awk -F'|' '/^DL/ && /CRWD/ {...}'` on downloaded ULN | Positional column enumeration — brief had some off-by-one positions starting at current_quantity; fixed via empirical check. |
| 2 | aws s3api list-objects-v2 | `--query 'Contents[?ends_with(Key, ``.ULN``)].[Key,StorageClass]'` | 349 STANDARD + 217 GLACIER — flagged Glacier restore as out-of-scope for this TO. |
| 5 | py_compile | `python -m py_compile convert_schwab_uln_to_silver.py` | exit 0. |
| 6 | pandas (manual) | read silver/ULN/date=20260415 parquet, schema + coverage | 213,253 rows; all long_short=L; 99.97% cusip non-null; dtypes float64/date/object as spec. |
| 6 | pandas (manual) | `(uln.account_id, uln.cusip)` vs `(hl.account_id, hl.cusip)` on gold/holdings_lots/2026-04-15 | 0 intersection — **confirmed expected**: ULN emits Schwab item_ids (same as silver/RPS convention `0010023253`); BD holdings_lots uses internal BD account_ids (`z...`). Bridge mapping is DS responsibility per brief. |
| 6 | pandas (manual) | silver/RPS/date=20260415 schema check | account_id format identical to ULN (`0010023253`) — confirms ULN matches the RPS-era convention. No divergence. |

**Role-minimum (AE):**
- `comp-pipescript deployed` — N/A (silver producer, not gold script).
- `comp-pipescript postdeps` — N/A (no gold run invocation from this session).
- `comp-iam gaps` — N/A (no iam.tf change).
- `comp-blast` — N/A (silver producer not in gold corpus, same blind spot noted in CP-AE1 session).

Silver-layer compiler corpus remains a known gap — flagged in CP-AE1 session log already.

---

## Artifact State

| Resource | State |
|---|---|
| `data/black_diamond/scripts/bronze/convert_schwab_uln_to_silver.py` | NEW (280 lines); ProcessPool, idempotent, L-filter, positional extract |
| `s3://opal-data-schwab/silver/ULN/date={YYYYMMDD}/data.parquet` | 349 partitions, 2024-01-12 → 2026-04-15 (STANDARD class source coverage) |
| `org/tier2_senior/0.6.0_AE_PartnerETL/prompt.md` | Schwab Ingest section updated — ULN converter added to roll-silver-forward sequence |

Glacier deferred: 217 dates need S3 restore (Glacier class) before conversion. Majority cluster in gaps between the STANDARD-class dates — non-contiguous. Not blocking B_01 wiring; restore-on-demand if DS reports a specific missing date gating investigation.

---

## Schema (silver/ULN/date={YYYYMMDD}/data.parquet)

```
account_id              string   -- Schwab item_id (same convention as silver/RPS; B_01 bridge-maps)
cusip                   string   -- 99.97% non-null on 2026-04-15
ticker                  string
asset_name              null     -- column reserved; B_01 joins on cusip
product_code            string   -- COM/FGO/FII/MFD/UIE/...
product_category        string   -- EQTY/FIXD/CASH/...
tax_code                string
current_quantity        float64  -- long positions only (long_short=='L' filter)
long_short              string   -- always 'L' after filter
current_market_value    float64
cost_basis              float64
cost_per_share          float64
unrealized_gain_loss    float64
acquired_date           date
original_purchase_date  date
file_date               date     -- partition key
_source_file            string   -- provenance: 01_raw/CRS{date}.ULN
```

---

## Sample Spot Check (2026-04-15)

- Rows: 213,253 long lots
- Accounts: 3,621 unique Schwab item_ids
- CUSIPs: 792 unique
- CUSIP non-null: 99.97%
- Unrealized G/L portfolio sum: $68,772,078
- Quantity range: 0.0001 .. 1,148,000

---

## Commits

| Commit | Author | Subject |
|---|---|---|
| (pending this session) | 0.6.0_AE_PartnerETL | feat(silver): schwab ULN -> silver/ULN/ ingestion + prompt ingest seq |

---

## MCP outbound

| To | Subject | Status |
|---|---|---|
| 0.4.0_DS_ClientPlatform | silver/ULN/ live — 349 partitions, ready for B_01 Rule 3 cross-reference wiring | pending this session |
| 2.0.0_SA_COO | FYI silver/ULN/ backfill complete | pending this session |

---

## Open / Followups

- **217 GLACIER dates** (2024-02-xx through 2025-10-xx intermittent) need `s3api restore-object` before conversion. Not gating — restore-on-demand if DS needs a specific missing date. Total Glacier restore cost estimate: Expedited ~$0.03/GB = ~$1 for all 217 files combined. Bulk restore (5-12h, $0.0025/GB) is cheaper if/when scope widens.
- **B_01 wiring** (DS lane) — DS owns the bridge from Schwab item_id → BD account_id (same pattern as silver/RPS). No AE action needed unless DS reports an IAM / bucket policy issue.
- **Nightly cadence** — `sync_schwab_onedrive_to_s3.py` already uploads all CRS*.{EXT} extensions generically; new ULN files auto-flow to 01_raw/ on sync. AE runs `convert_schwab_uln_to_silver.py` alongside RPS/ACC/TRN converters during the manual Schwab ingest session (prompt.md updated).

---

## Incidents / Lessons

- **Brief column positions were empirically off** starting at current_quantity (brief said col 23, actual 0-indexed pos 22). Verified via awk enumeration on a downloaded CRWD row — noted in the source docstring. Lesson: always enumerate positional columns on a real file before trusting a brief's column table — off-by-one is common when humans count from first-non-prefix column.
- **Windows ProcessPoolExecutor detached worker behavior** — multiple `python convert_...` invocations in Git Bash spawned pool workers that survived shell-parent exit. Parent shell reported "completed exit 0" after printing header lines, but workers kept writing parquet in background. Not destructive (idempotent), but log output is incomplete. Lesson: for long-running ProcessPool scripts on Windows, run foreground with explicit timeout (480000ms worked for the final 23-date cleanup) rather than backgrounding — parent-exit behavior is unreliable in Git Bash.
- **Read-timeout on large 2026 files** — 2 dates (20260320, 20260410) errored with S3 `Read timeout on endpoint URL: None` during the final backfill pass. Retry via `--date` flag resolved cleanly both times. Files are ~42MB raw → ~213k rows → ~3MB parquet; boto3 default read timeout (60s) can lose with concurrent network pressure. Non-systemic; tolerable with retry.

---

## Next Steps

- **[0.6.0_AE]** Commit converter + prompt update this session; MCP DS + COO.
- **[0.4.0_DS_ClientPlatform]** Wire ULN as B_01 Rule 3 cross-reference (upgrade Band B → Band A when `(account_id, cusip)` appears in silver/ULN with `current_quantity > 0`). Bridge mapping Schwab item_id → BD account_id is DS lane — same pattern as existing silver/RPS consumption.
- **[0.6.0_AE]** On-demand: restore Glacier ULN dates if DS reports a gap blocking a specific investigation. Pass date list to `aws s3api restore-object --restore-request '{"Days":7,"GlacierJobParameters":{"Tier":"Expedited"}}'` then re-run converter.
