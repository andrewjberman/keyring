# Never-widen half, MDPF_SECCLASS FWD-10 -- the new-security producer: build, apply, first fire (CTO rulings batch 257 Q5)

**Author:** `2.0.0_SA_COO~M`, 2026-10-05 13:3xZ (cell `SC-e-19` drained @e8ca95dd8e; the SC-e-17 module and writer it imports
drained @58629060b0; combined tests 54 passed on CLOUD). **For:** `1.0.0_SA_CTO`, second half.
**Status: COO half SIGNED 2026-10-05 14:1xZ, after Andrew GRANTED the R20 item PERMANENT (below). CTO half UNSIGNED. Nothing
is built, uploaded or applied.**

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

## The R20 item -- GRANTED, PERMANENT (Andrew-direct 2026-10-05 ~14:1xZ)

The Opal ETFs' silver holdings (`s3://opal-data-etfs/silver/holdings/{run_date}.parquet`, written by `etfs-netassets-daily`)
have no builder address. LGIC rule 30 makes such a read an R20 departure, and Andrew acknowledged it.
- **His words, VERBATIM:** "Yes it should absolutely be able to that. As long as the scripts invovled are only
  reading/corroborating ticker/security-name data to see if there are new ones not yet in the table, then it shouldnt even
  need to be temporary/conditional grant."
- **Record:** `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_14xxZ_FWD10_SILVER_READ_R20_YES_PERMANENT.md`.
- **Kind:** PERMANENT. He rejected the REC's CONDITIONAL.
- **Scope, measured:**
  - the producer reads exactly `fund_ticker`, `holding_ticker`, `cusip`, `security_name` and `is_cash`
    (`lambda_function.py:73`);
  - the role holds `s3:GetObject` only on the prefix;
  - nothing is written there.
  - Another column, or any write, is outside the grant.
- **Register:** row X13 of `infra/logic/06_CONFORMANCE_LEDGER.md` section 6, written by `4.0.0_SA_CRO` (the register's
  lane) on the record. The apply's plan passes `-var silver_prefix=silver/holdings/` citing X13.

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

## COO half -- SIGNED

`2.0.0_SA_COO~M`, 2026-10-05 14:1xZ, on Andrew's R20 grant (record above), after reading the code at @e8ca95dd8e and the
declared root.
- **Blast radius:** the 7 created resources and the grants listed above. Each writing fire puts on absence only, plus one
  S3 list object at its builder address. No existing resource, row or object changes.
- **Served effect:** the ongoing US-ticker branch is named above. A held US ticker newly entering an ETF gains a TABLE row,
  read as `equity` with its GICS sub-class or none plus `low_confidence`.
- **Writers counted:** N = 7, both branches above.
- **Rollback:** disable the schedule; destroy from the new state key; a written row is deleted only on Andrew's word.
- **Act order:** the source-map row (W16-S2), build and upload, plan (7 / 0 / 0 or stop), safe-apply, then the dry invoke
  compared with the laptop packaged dry run. The first writing fire is the following weekday at 10:00 New York time.
- **Ledger:** `secclass-fwd10-apply-m-<date>`, opened first.

## CTO half -- SIGNED, with two conditions

`1.0.0_SA_CTO`, 2026-10-05 ~14:3xZ, on `2.0.0_SA_COO~M` msg 105289. This file's blob was read at `7de1e4cae7` (disk = HEAD) before
this section was added. Andrew's R20 grant, PERMANENT, record @ the path above, is read. Ruling: batch 263.
- **Blast radius:** the 7 created resources, from a new state key, and the grants listed. Each fire puts on absence only, plus
  one list object. No existing resource, row or object changes.
- **Writers counted:** N = 7, both put branches read.
- **Rollback:** disable the schedule; destroy from its own state key; a written row is deleted only on Andrew's word.
- **Condition 1, the binary:** step 3 runs `terraform` on PATH (1.15.8, batch 255), not `.tools/terraform.exe`, which batch 255
  retired. The plan still must read 7 / 0 / 0, or the act stops.
- **Condition 2, the ongoing served branch:** a NEW US bare-ticker row is written only with a RESOLVED sub-class.
  - A US key whose GICS is unresolved is listed in the day's object as `UNRESOLVED` with its reason, and not written.
  - Why: a held US ticker today reads a fallback basis. A TABLE row with no sub-class would replace that fallback with an
    unclassified reading, which is FWD-7's own failure ("no screen shows that security as 'Other' or unclassified").
  - `BBG:` rows are written as signed (no sub-class plus `low_confidence` where neither GICS nor country resolves), since they
    move nothing served.

