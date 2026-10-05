# Never-widen half, MDPF_SECCLASS FWD-10 -- the new-security producer: build, apply, first fire (CTO rulings batch 257 Q5)

**Author:** `2.0.0_SA_COO~M`, 2026-10-05 13:3xZ (cell `SC-e-19` drained @e8ca95dd8e; the SC-e-17 module and writer it imports
drained @58629060b0; combined tests 54 passed on CLOUD). **For:** `1.0.0_SA_CTO`, second half.
**Status: DRAFT. COO half UNSIGNED, pending one sovereign item (the R20 entry, below). CTO half UNSIGNED. Nothing is built,
uploaded or applied.**

## The act (issuer, in order, under ledger `secclass-fwd10-apply-m-<date>` opened first)

1. **Source map (row `MDPF_SECCLASS-W16-S2`).** Add `mdpf-secclass-new-security-lambda` to
   `infra/aws/lambda/ci/lambda-source-map.json`: `files[]` = `lambda_function.py` plus the four `_shared` modules it imports
   (`rivalfunds_classification`, `etf_classification_scheduled`, `etf_classifications_dynamodb`, `etf_classification`), the
   tf file and resource, the role. Its packaged layout is the one `R7_CHECKS/r7_fwd10_dry_run.py --packaged` imports from.
2. **Build and upload:** `bash infra/aws/lambda/ci/build-and-upload.sh mdpf-secclass mdpf-secclass-new-security-lambda` to
   `s3://opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip` with `content-sha256`.
3. **Plan, then apply:** `.tools/terraform.exe -chdir=infra/aws/terraform/mdpf-secclass/new-security-classifier init
   -plugin-dir=C:/Users/AndrewBerman/.terraform.d/plugin-cache`, then `plan -var silver_prefix=silver/holdings/ -out <plan>`.
   The plan must read **7 to add, 0 to change, 0 to destroy**, or the act stops. Then `HALT_ACK=1 bash .tools/safe-apply.sh
   -chdir=... apply <plan>`.
4. **First fire, DRY:** one invoke with `{}` (no `write`) for the latest day with a previous day. Its `FWD10-DRY-RUN` line
   is compared with the laptop's `r7_fwd10_dry_run.py --packaged` line for the same day; they must be equal.
5. **First scheduled fire, WRITING:** Monday to Friday at 10:00 America/New_York, input `{"write": true}`. The first one
   after the apply is read (acceptance 3).

## Blast radius

**Created (7):**
- `aws_lambda_function` `mdpf-secclass-new-security-lambda`, and its CloudWatch log group;
- `aws_iam_role` plus an inline policy for the function;
- `aws_iam_role` plus an inline policy for the scheduler;
- `aws_scheduler_schedule` `mdpf-secclass-new-security-daily`.

Every name is `name()` output. The state key is new (`mdpf-secclass/new-security-classifier/tfstate`), so no existing
resource is in it.

**Granted:**
- `s3:GetObject` on `opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/*` and on `opal-data-etfs/<silver_prefix>*`;
- `s3:ListBucket` on `opal-data-etfs`;
- `dynamodb:GetItem` and `dynamodb:PutItem` on `etf-classifications`;
- `s3:PutObject` only on `opal-data-etfs/mdpf/etfs/gold/new_securities/date=*/new_securities.json`.

**Written per writing fire:**
- one put on absence per NEW stock key (`attribute_not_exists(ticker)`, through `etf_classification_scheduled.write()`):
  - US listings are bare tickers;
  - every other listing is `BBG:<ticker>:<exch>`, the FWD-9 keys.
- one S3 object, the day's new-stock list.

No existing row and no existing object changes.

**Served effect, named from the producer rules:**
- A `BBG:` key matches no firm's holdings ticker, so it moves nothing served (the FWD-9 branch 1 argument).
- A NEW US bare-ticker row that a client also holds is read by that firm's next holdings build. Today such a holding reads a
  fallback basis (`NAME_ALIAS` / `TICKER_SHAPE`, measured at cottonwood for ATI, BG and JAN). After the row exists it reads
  `asset_class_basis` `TABLE`, with the row's class (`equity`) and its sub-class: GICS where RESOLVED, otherwise none with
  `low_confidence: true`.
- This is the same question as FWD-9 branch 2. Its held census (today, after 14:15Z) gives the measured before-state for
  the 31 current US keys. The CTO's signature here covers it as the ONGOING branch: a held US ticker newly entering an ETF
  gains a TABLE row.

## Writers counted (`etf-classifications`), both branches

N = 7 writers read:
- the seed path (`yang-pipeline-lambda-role`);
- E_18 `detect_new_securities` (bd-securities, through `write()`);
- the CUSIP rows writer;
- `write-model-rows.py`;
- the one-off multi_asset and FWD-9 acts (closed);
- this producer.

Every scheduled path puts on absence, so none overwrites another.
- **Branch A, a new key is absent:** the put lands and the list marks it `written`.
- **Branch B, the key appeared since the plan's consistent get** (another writer, or a retried put meeting its own row, as
  `BBG:8354:JP` did today): `ConditionalCheckFailedException`, the row is left exactly as it was, and the list marks it
  `present`.

## The sovereign item (R20) -- COO half waits on it

The Opal ETFs' silver holdings (`s3://opal-data-etfs/silver/holdings/{run_date}.parquet`, written by `etfs-netassets-daily`)
have no builder address. LGIC rule 30 requires every S3 address to be `address()` output. A deliberate departure is an R20
register entry in `infra/logic/06_CONFORMANCE_LEDGER.md` section 6, acknowledged by Andrew. The draft entry:

`MDPF_SECCLASS new-security-classifier | A3 storage-path | READS the legacy key prefix opal-data-etfs/silver/holdings/
(etfs-netassets-daily's output), passed as var.silver_prefix; it writes nothing there | WHY: two Opal ETFs (PFDE, DIVZ) are
held only there, not in the rival canonical_shape (measured 2026-10-05), and FWD-10 covers Opal ETFs | acknowledged by:
Andrew | when: <date> | CONDITIONAL: ends when etfs-netassets migrates to an address() home (R19), or when the canonical_shape
carries every Opal ETF`

Without the entry, the alternative is to drop the silver read. FWD-10 would then miss PFDE and DIVZ new stocks, which
narrows FWD-10 and is an endpoint change.

## Rollback

- Disable the schedule (`state DISABLED`, reversible).
- Destroy the 7 created resources from their own state key; re-applying restores them.
- A row the producer wrote is deleted only on Andrew's word.
- The S3 lists are left in place.

## Acceptance

1. The plan reads 7 / 0 / 0, and the apply prints the same. The deployed `CodeSha256` equals the artifact's
   `content-sha256`.
2. The dry invoke's `FWD10-DRY-RUN` line equals the laptop packaged dry run for the same day.
3. The first writing fire, read back:
   - the list object exists at its address;
   - every `written` key reads back with `classified_by scheduled` and `updated_by` the producer's value;
   - every `present` key is unchanged;
   - the log shows no `BLOCKED`.

## Local candidate

- Code @e8ca95dd8e:
  - `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py` (19 tests);
  - `infra/aws/terraform/mdpf-secclass/new-security-classifier/` (validates).
- `R7_CHECKS/r7_fwd10_dry_run.py --packaged`: `FWD10-DRY-RUN day=2026-10-02 previous=2026-10-01 sources=2 new_stocks=0
  planned_writes=0 present=0` (10-02 is a partial landing, row W16-S4).

## COO half -- [PENDING SIGNATURE: waits on the R20 acknowledgement]

## CTO half -- [PENDING SIGNATURE]
