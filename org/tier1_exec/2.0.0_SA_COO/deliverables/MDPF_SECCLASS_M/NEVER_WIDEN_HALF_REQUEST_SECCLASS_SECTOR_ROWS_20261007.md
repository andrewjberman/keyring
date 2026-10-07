# Never-widen half request, MDPF_SECCLASS FWD-12 SC-e-28 -- the scheduled sector writer: apply, artifact upload, first real fire

**Author:** `0.9.0_WK_MDPF_SECCLASS~24` (worker, TO-SC-e28), 2026-10-07. **For:** `2.0.0_SA_COO~M1` to sign and send. **Status: UNSIGNED. Nothing is applied, nothing is uploaded, nothing is written to the table or S3, nothing is pushed.**
The candidate lives on branch `wk-MDPF_SECCLASS-24` (base `6a02099256`); the code commit is named in the worker's report.

## The act

By the issuer, in this order, after both halves sign:

1. **Open** a change-management ledger entry (`org/critical_paths/change_management/`) naming the six resources below, the artifact and the table.
2. **Register the departure** (R20 entry Andrew acknowledges) for the characteristics home `opal-data-etfs/bbg/` (no builder address; row `MDPF_SECCLASS-W24-S3`) and supply it as `var.bbg_prefix`.
3. **Add the function** `mdpf-secclass-sector-writer-lambda` to `infra/aws/lambda/ci/lambda-source-map.json` (files: `lambda_function.py`, `org/standards/MDPF_SECCLASS_CONTRACT.json` flat beside it, `rivalfunds_classification.py`, `etf_classification.py`; row `MDPF_SECCLASS-W24-S4`), then build and upload the artifact with `bash infra/aws/lambda/ci/build-and-upload.sh mdpf-secclass mdpf-secclass-sector-writer-lambda`.
4. **Apply** the root `infra/aws/terraform/mdpf-secclass/sector-writer/` with `.tools/safe-apply.sh` (never a bare apply). It creates six resources (names are `lib/opal_naming.py name()` output; none has a `resources.json` row, because the registry refuses a row for a name that resolves its own system, row `MDPF_SECCLASS-W24-S8`):

| resource | name | type |
|---|---|---|
| Lambda | `mdpf-secclass-sector-writer-lambda` | python3.11, 1024 MB, 300 s, layer `pandas-pyarrow-requests-layer:1` |
| role | `mdpf-secclass-sector-writer-role` | IAM_ROLE |
| inline policy | `mdpf-secclass-sector-writer-policy` | IAM_POLICY |
| scheduler role | `mdpf-secclass-sector-writer-scheduler-role` | IAM_ROLE |
| scheduler policy | `mdpf-secclass-sector-writer-scheduler-policy` | IAM_POLICY |
| schedule | `mdpf-secclass-sector-writer-daily` | SCHEDULE, `cron(30 10 ? * MON-FRI *)` America/New_York, input `{"write": true}` |

5. **The first real fire** (the schedule's or one invoke with `{"write": true}`): the writer sets `gics_sector` and `gics_industry_group` on the planned rows and writes its run list.

What the writer does (read at `lambda_function.py`): for the newest `bbg/<day>/` holding both `run_manifest.json` and `characteristics.parquet`, per security it resolves the table key as the producers do (`US` -> bare ticker, else `BBG:<ticker>:<exch>`), refuses any value outside the contract's closed lists (version read from the contract file, 0.5.0: 10 sectors, 23 industry groups), never creates a row, never sets a field the seed source holds, skips a field already equal, and otherwise issues one `UpdateItem` `SET` of ONLY the field(s) that differ with `ConditionExpression attribute_exists(ticker)`. The default is a dry run.

## Blast radius

**Table:** `etf-classifications` (3,507 rows, key `ticker`). Attributes touched: `gics_sector` and `gics_industry_group` only. `sector` (the legacy attribute), `sub_asset_class`, `asset_class`, `classified_by`, `last_updated`, `updated_by` and every other attribute keep their bytes; no row is created or deleted; the role has no `PutItem`/`DeleteItem`.

**Rows, from the live dry run** (`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sector_writer_dry_run.py --packaged`, 2026-10-07, packaged import, read-only wrappers on S3 and the table):

`SECTOR-WRITER-DRY-RUN partition=2026-10-05 securities=114 planned=107 present=0 no_row=0 out_of_list=0 seed_wins=0 no_value=7`

- Key resolution: 114 of 114 characteristics securities resolve to an existing row (all are `<ticker> US Equity`; none needs a `BBG:` key); 0 `NO-ROW`. **The act would touch 107 of the 3,507 rows (3.1 percent)**; 0 of the 107 carry either new attribute today (present=0).
- `NO-VALUE` 7 (both labels null in the file, nothing written): `FXFXX`, `GLD`, `VXX`, `DIVZ`, `IDVZ`, `PFDE`, `PFOE`.
- Planned row set (107 keys): `2602335D AAPL ABBV ADM AIZ AMAT AMD AMP AMZN ANET C CIEN CMI CNC CVX ASML AVGO BA BAC BBY BE BEN BKNG BN BNY DAL DECK DELL DG EBAY ECHO ED EL ES ETR GL GLW GM GOOG GOOGL EXPD F FCX FDX FER FIX FLEX FTNT GEV META MNST MPWR MRK MRNA KEYS KO LITE LLY LMT LRCX LUV MA MAR MELI GS HESAY HWM IDXX INCY INTC ISRG JBHT JNJ JPM PM PWR QXO REGN ROST SNDK SPOT STLD STT STX T TJX TRV TSLA TSM MRVL MSFT MU NEM NOW NTRS NU NVDA PCG PLTR UAL UBER UNH V VLO WDAY WDC WM`. Each key's two planned values are the dry run's `SECTOR-WRITER-ITEM` lines (re-run to print them).
- Planned `gics_sector` counts: Information Technology 27, Industrials 18, Financials 17, Consumer Discretionary 13, Health Care 11, Consumer Staples 6, Communication Services 6, Utilities 4, Materials 3, Energy 2 (total 107; all in the closed list; 23 distinct industry groups, all in the closed list).

**S3:** one object per write run at `s3://opal-data-etfs/mdpf/etfs/gold/sector_writer_runs/date=<run date>/sector_writer_run.json` (`lib/opal_naming.py address()` output; the role's `s3:PutObject` is that pattern only). Reads: `s3:GetObject` and `s3:ListBucket` on `opal-data-etfs/bbg/` only.

**Schedule:** Monday to Friday 10:30 ET (rationale in `schedule.tf`: 12 of the 14 newest partitions landed 07:02-07:12 ET, one at 08:32, one at 15:42; Friday's partition is Monday's answer; 10:30 follows the 10:00 new-security-classifier). After the first fire, each weekday run touches only rows whose labels differ from the file (a vendor reclassification or a newly held security): idempotent.

**IAM** (`comp-iam service mdpf-secclass-sector-writer`, read from the declared root, 5 statements): logs (own group); `s3:GetObject` on `opal-data-etfs/bbg/*`; `s3:ListBucket` on the bucket with `s3:prefix` like `bbg/*`; `dynamodb:GetItem` + `dynamodb:UpdateItem` on `table/etf-classifications`; `s3:PutObject` on `<run list prefix>date=*/sector_writer_run.json`. IAM cannot demand the `ConditionExpression`; the condition is the code's (a unit test pins it). A stricter grant (`dynamodb:Attributes` limited to the two fields) was not declared because it could not be exercised here (no apply).

**Not measured by this cell (the signers should know):** the readers of `etf-classifications` that return a whole item or iterate its attributes were not censused here (C-NOCHAR keeps the two additions to labels; SC-e-38's trace is the reader census). The two new attributes are strings; no reader named them before this contract version.

**Not validated by this cell:** the declared root was never `terraform init`-ed or validated (no provider cache, no download allowed; row `MDPF_SECCLASS-W24-S5`). The issuer runs SC8-e28-AC3 where the provider is cached before the apply. Its registry limb will read `ok=False missing=<5 names>` whatever the provider (row `MDPF_SECCLASS-W24-S8`).

## Rollback per key

The prior value of both attributes is **absent** on every one of the 107 rows (dry run: `present=0`; the run list also records each row's `prior` values per key). Rollback per key, from the run list's key set:

`UpdateItem` `Key={"ticker": <key>}` `REMOVE gics_sector, gics_industry_group` with `ConditionExpression attribute_exists(ticker)`, executed by the issuer (the writer's role cannot remove). Rows not in the run list are untouched. Infrastructure rollback: `.tools/safe-apply.sh` on the root with the resources removed (or `state rm` plus delete under the ledger entry), the artifact object and the run-list prefix left or deleted by the issuer's choice. Disabling the schedule alone stops further writes; it does not remove written attributes.

## Both branches of the outcome

- **Lands:** the first fire reads partition 2026-10-05 or newer, sets the two attributes on up to 107 rows (counts equal the dry run's if the file is unchanged), writes the run list, and every later weekday run is `PRESENT` for those rows. A security newly entering the file with a row is labelled; one with no row is `NO-ROW`; a value outside the closed list is `OUT-OF-LIST` and left unwritten, listed by security.
- **Refuses or fails:** a missing environment value or contract file is `BLOCKED` before any read (no write); a partition lacking either file is skipped for the next older one; a table error is raised and the run list for that day is not written; the row that vanished between the get and the update is `NO-ROW`. Nothing in these paths changes a row except the conditional `SET`.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
