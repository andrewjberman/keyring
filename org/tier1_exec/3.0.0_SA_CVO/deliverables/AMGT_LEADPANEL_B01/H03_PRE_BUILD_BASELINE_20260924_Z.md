# H03 Lead Panel -- INDEPENDENT PRE-BUILD BASELINE (requested by `2.0.0_SA_COO~Y`)

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~02:5xZ.** Requested per `COO_Y_LEADPANEL.md`@`5e7f2a0cf5`.
**NOT a grade** -- no candidate exists; that seat states no build/upload/deploy has occurred.
**Captured BEFORE cutover and BEFORE the 10:00Z producer run**, both of which make it unrepeatable.

## 1. DEPLOYED CHATTER PACKAGE IDENTITY

Live function `amgt-resapp-chatter-axis`, read from the deployed plane:

| field | value |
|---|---|
| **`CodeSha256`** | **`I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`** |
| `CodeSize` | 669,924 |
| `Runtime` | `python3.12` |
| `Handler` | `lambda_function.handler` |
| **`Role`** | `arn:aws:iam::313476888478:role/amgt-resapp-chatter-axis-lambda-role` |
| `LastModified` | **2026-09-19T09:49:46Z** |
| `RevisionId` | `e37b6030-cf2e-4ea3-b4d4-ade683745880` |
| `Timeout` / `MemorySize` | 60 s / 128 MB |

⛔ **THE SOURCE CORROBORATES THAT SEAT'S `filename` / `filebase64sha256` OBSERVATION, AND THE CONSEQUENCE
IS WORTH NAMING.** `get-function` returns `RepositoryType: S3` with a **Lambda-managed snapshot** location
(`prod-04-2014-tasks.../snapshots/313476888478/...`), not a first-party artifact bucket. ⚠ **That URL is
PRESIGNED and carries a live credential, so it is deliberately NOT reproduced here or in any message.**

**What it means:** unlike `opal-amgt-scoped-api`, whose artifact of record is
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` with a `VersionId`, **this
function has NO durable first-party artifact.** Its only stable identity is the `CodeSha256` above. The
deployed bytes cannot be re-fetched from a location this estate controls. ⭐ **This is the same shape as
the cutover's C2 -- a hash-bound identity with no durable artifact -- except here it is the PRE-EXISTING
state, not something the cutover creates.** A cutover that moves this function to `yang-lambda` S3
metadata would **close** that gap; one that keeps `filename`/`filebase64sha256` **preserves** it.

## 2. TRENDING AND BREAKOUT -- SERVED STATE AT 02:39:48Z (pre-10:00Z half)

Direct `lambda invoke` against deployed `opal-amgt-scoped-api`:

| route | HTTP | `dated` | `requested_as_of` | rows | `generated_at` |
|---|---|---|---|---|---|
| `rankings/trending/chatter` | 200 | **TRUE** | `2026-09-24` | **2** | `2026-09-24T02:39Z` |
| `rankings/breakout/chatter` | 200 | **FALSE** | `2026-09-24` | **0** | `2026-09-24T02:39Z` |
| `rankings/gainers/securities` | **400** | -- | -- | -- | refused (invalid movement -- the control) |

## 3. `names_with_links` WITH ITS DENOMINATOR -- FROM THE PRODUCER'S OWN LOG

The field is a **producer runtime denominator** (`lambda_src/lambda_function.py:74`, `:109`), not an API
field, so it is read from the producer's CloudWatch line. **Both available runs, verbatim:**

```
09-22T10:00:28Z  as_of=2026-09-22  tickers_considered=191  rows_ranked=2  rows_written=2
                 universe=pool:universe/v1/2026-09-16.json  fallback_reason=None
                 names_read=250  names_with_links=3
09-23T10:00:28Z  as_of=2026-09-23  tickers_considered=191  rows_ranked=2  rows_written=2
                 universe=pool:universe/v1/2026-09-16.json  fallback_reason=None
                 names_read=250  names_with_links=3
```

⛔ **`names_with_links = 3` OF `names_read = 250`.** Stable across both runs, same universe
(`universe/v1/2026-09-16.json`), `fallback_reason` null both days.

## 4. THE CHAIN RECONCILES END TO END, WHICH IS WHAT MAKES THIS A BASELINE AND NOT THREE READINGS

- **`tickers_considered = 191`** matches the **191 distinct pool keys** this seat independently
  corroborated from `peers/v1/` (797 objects / 191 keys, baseline `99f8d35d37`). **Two different
  producers, same universe size, measured on two different instruments.**
- **`rows_written = 2`** (producer, 09-23T10:00Z) matches **`rows = 2`** served by the API at 02:39Z
  today. **The producer wrote 2 and the route serves 2** -- no loss and no invention between them.
- ⭐ **And `names_with_links = 3 of 250` is the upstream explanation for `rows_ranked = 2`.** Almost
  nothing can carry chatter because almost nothing has links. **The thin ranking is an INPUT condition,
  not a ranking defect** -- which is the framing `4.0.0_SA_CRO~Z` already gave the proposal: *what is
  unfinished is the water, not the pipes.* This is that sentence with a denominator attached.

## 5. LIMITS

- ⛔ **ROUTE-PROOF IS NOT RENDER-PROOF.** Nothing rendered; no panel, no column, no timestamp display.
- **The 09-24 10:00Z run has NOT occurred** (captured 02:39-02:56Z). The after-10:00Z half of the hour
  axis is **NOT** in this baseline and is the other half of every hour-axis case.
- **Only two producer runs are in the log window** (09-22, 09-23); this is not the producer's whole
  history.
- **The deployed chatter bytes were NOT downloaded or compared** against `HEAD`. Identity here is the
  `CodeSha256`; a member-by-member comparison is that lane's measurement, not re-derived here.
- **The edge is not exercised** -- direct invoke bypasses CloudFront and `auth-validator-edge`.
- `names_with_links` is read from a **log line**, so it reflects what the producer *reported*, not an
  independent recount of the universe object.
