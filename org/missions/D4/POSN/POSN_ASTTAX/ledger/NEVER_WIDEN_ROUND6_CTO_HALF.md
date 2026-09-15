# NEVER-WIDEN SIGN-OFF -- CTO HALF -- POSN_ASTTAX round 6: B6 (the characteristics artifact gains the per-ticker block; the rule moves; a driven run)

**Signer:** `1.0.0_SA_CTO~Z` (L2/L4 owner). **Counterpart:** `2.0.0_SA_COO~Z`, `ledger/NEVER_WIDEN_ROUND6_COO_HALF.md` @`56f4d41933`.
**Order:** `TO-W1-1` (cell `AT6-s-1`, worker `0.9.0_WK_POSN_ASTTAX~24`), issued @`910815809f`. **PRD:** v0.10 @`59113e257a`, both halves
SIGNED (`3.0.0_SA_CVO~W` @`d3e74ab1ea`, `4.0.0_SA_CRO~W` @`d1f7199013`) -- `C-HOLDING-MEASURES` as amended, `C-B4-SCHEDULE`.
**Andrew:** ~02:3xZ @`0553548fe2` (fix it tonight), ~03:0xZ @`365580f244` (the vendor change). Pure ASCII.

This half is written from THIS SEAT'S OWN READS at 2026-09-15 ~03:4xZ, on instruments different from the COO half's, and names the
blast radius of the act whichever branch the producer takes.

## 1. BASELINE, READ BY THIS SEAT (not copied from the COO half)

| object | read | value |
|---|---|---|
| `s3://opal-data-cot/platinum/satellites/characteristics.json` | `s3api head-object` 03:42Z | VersionId `rt61ogajZQy79meUlsY1X_mIdPngxJTZ`, 54825 B, LastModified 2026-09-14T21:45:13Z, ETag `2c94f7a7d1dba8225c4904e65c762734`; bucket versioning Enabled |
| `cot-satellites-characteristics-producer` | `lambda get-function-configuration` 03:42Z | CodeSha256 `6M4Co5N81OD/SxD+fS0/pzbByeBKeYaVh8z/kszV3Vk=`, LastModified 2026-09-14T21:43:59Z, no environment |
| the function's artifact `s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip` | `s3api head-object` (current AND `--version-id sZ0o...`) | current version IS `sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml`, 36184 B, Metadata `content-sha256` == the function's CodeSha256; bucket versioning Enabled |
| rule `cot-satellites-characteristics-producer-daily` | `events describe-rule` + `list-targets-by-rule` 03:42Z | `cron(20 7 * * ? *)` ENABLED; ONE target, the function's ARN, no `Input` override |
| IAM `aws_iam_role_policy.cot_satellites_characteristics_producer_s3` | `satellites-characteristics-producer.tf:96-141` at HEAD | GetObject `holdings.json`; GetObject `positioning_data.json`; GetObject `opal-data-etfs/bbg/*/characteristics.parquet` + `run_manifest.json`; ONE PutObject pinned to `characteristics.json`; the separate cross-firm Deny on `opal-data-bd` / `opal-data-inf` (`:156-175`) |

## 2. WRITERS OF THE PROPERTY -- N PRINTED, BY A SECOND INSTRUMENT

**N = 1.** Instrument: a TEXT census of the repository's code files (`*.py, *.tf, *.ts, *.tsx, *.js, *.sh, *.json`) for the key
`satellites/characteristics.json` and every `OUT_KEY =` assignment. Writers found: `data/assets/scripts/gold/build_satellites_characteristics.py`
(`OUT_KEY` `:108`, `publish()` `:429-434`) through the function, whose role holds the ONE PutObject pinned to the key (`.tf:131-136`). Every
other hit is a READER (the B5 edge route, worker fixture builders and probes under `deliverables/`, the round-5 ledger sentinel) or a
comment. The COO half reached the same N by `comp-iam gaps` on the role grants -- two instruments, one count.

## 3. THE ACT AND WHAT IT MAY TOUCH -- per object, with the rollback for each

| object | change the act may make | rollback |
|---|---|---|
| `platinum/satellites/characteristics.json` (opal-data-cot) | ADDITIVE: a `tickers` block (every ticker any satellite holds, once, with `source`) and `method.tickers_block`; every other field identical for the same three inputs | `copy_object` of VersionId `rt61ogajZQy79meUlsY1X_mIdPngxJTZ` onto the key (a new version, never a delete) |
| the artifact zip (lambda-artifacts bucket) | ONE new version (`W1-AC7`) | the function re-pointed to `sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml` by a targeted apply; the new version is left in place, not deleted |
| the function | `s3_object_version` + `source_code_hash` (and memory only if the plan names it) | as above |
| the rule | `cron(20 7 * * ? *)` -> `cron(30 12 * * ? *)`; target and state unchanged | revert the one `.tf` line, targeted apply |
| the IAM policy | READ-ONLY widening: `s3:ListBucket` on `arn:aws:s3:::opal-data-etfs` conditioned (`s3:prefix`) to `bbg/*` and `bbg-testpull/tickers/*`; `s3:GetObject` on `opal-data-etfs/bbg/*/history_topup.parquet` and `opal-data-etfs/bbg-testpull/tickers/*/history.csv`. No new PutObject, no new bucket; the cross-firm Deny unchanged | revert the `.tf`, targeted apply |
| `lambda-source-map.json` / `CHANGELOG.json` (repo) | the deploy record (`W1-AC14`) | a revert commit |
| `registry.json`, `holdings.json`, `positioning_data.json`, every `bbg/` and `bbg-testpull/` object | READ only | -- |
| anything else | **NOT SIGNED** | -- |

The bucket `opal-data-etfs` is already read by this role (`bbg/*/characteristics.parquet`), is Opal's own ETF data, and sits in no
cross-firm foreign list (`.tools/ds-precommit-check.py`); the widening adds prefixes inside it, nothing outside it.

## 4. THE NEW REACHABLE STATES (NEVER#1), EACH COVERED

1. **The driven invoke with an explicit `bbg_as_of`** (`lambda_function.py:82-83` forwards it). The partition is the newest
   `bbg/<date>/` present at the run, listed and printed by the worker. At this read the newest is `2026-09-11`; the 07:00 America/New_York
   pull lands `2026-09-14` at ~11:0xZ, so the value depends on WHEN the worker runs -- both are covered by section 5.
2. **The 12:30Z schedule** -- after its input in both DST states. The first fire (2026-09-15 12:30Z) is the organic leg, recorded by
   `2.0.0_SA_COO~Z`, not waited on.
3. **The returns rule's reads under the widened grant.** `load_history` lists `bbg/` and reads every `history_topup.parquet` in its
   400-day lookback; `_load_backfill_history` lists `bbg-testpull/tickers/` and reads every `history.csv` there (171 tickers plus GLD and
   VXX). A key the listing names but the grant does not cover, or an S3 403-for-404 on a missing object under a prefix-conditioned
   ListBucket, is a RAISE -- section 5, Branch B.

## 5. EXPECTED OUTCOME, BOTH BRANCHES -- read from the producer's rule and the returns rule, not predicted

- **A.** The purity control (`W1-AC3`) prints DEEP-EQUAL for `build()` at HEAD vs the cell over the same three inputs minus the two
  additions; the targeted plan reads 0 add / 3 change / 0 destroy; the apply completes; the unscoped plan reads No changes; the driven
  invoke returns rc 0; the key's VersionId moves off `rt61ogaj...`; the served `tickers` block equals the local dry run over the same
  inputs (25 tickers, each once: 23 `positioning_data`, GLD `bbg`, CASH `none` -- counted at the run, not assumed). **The served
  `satellites` block equals today's served block when the inputs triple is unchanged** -- this seat's read of today's triple:
  `holdings_as_of 2026-09-14` (its content was relabelled at 03:02Z by R2, but B4 reads only tickers and weights, which R2 did not move),
  `positioning_data_as_of 2026-09-11`, `bbg_as_of 2026-09-11`; with a different `bbg_as_of` the comparison is the dry-run arm at the
  same inputs. **GLD's `returns`, read from the rule at `bbg_as_of 2026-09-11`:** this seat ran `etf_positioning_gold.load_history` and
  `compute_returns` over the live history at 03:2xZ (ledger `posn-bbg-gld-vxx-return-history-backfill` L3 @`d3d2ffc4a5`): 8 of 8 windows
  non-null (1D 0.608 ... 1Y 18.9435). At `bbg_as_of 2026-09-14` the frontier is that day's `history_topup` row, which the 07:00 pull
  lands; if that row is absent the rule returns NULL for every window -- also Branch A (a value read from the rule). `describe-rule`
  reads `cron(30 12 * * ? *)` ENABLED with the same single target.
- **B.** Before the apply, any unmet precondition: NOT COVERED, nothing written. After the apply and before the driven run, a failing
  clause: roll back the function version, the rule and the policy in the same session. The driven invoke RAISES (partition absent, a read
  denied, an import failure of the packaged `etf_positioning_gold.py`): nothing was written -- the refusal is the measured act, a row
  names it, and the organic leg stands. After a successful write, a served artifact that differs beyond the two additions (a `satellites`
  leaf moved at unchanged inputs, a ticker twice or missing, an existing `method` field changed): `copy_object` from `rt61ogaj...`, the
  function re-pointed to `sZ0o...`, the rule and policy reverted, the row filed.

## 6. WHAT THIS HALF DOES NOT COVER

The Bloomberg history backfill (this seat's act, its own ledger, closed); F4 and F5 (no served key moves); any promote, DEV/PROD push
or gitlink move; `registry.json` / `holdings.json` (R2's halves); any change to the ETF gold pipeline, its outputs or `bbg-testpull/`
contents; any CloudFront act; any monitor.

## 7. SIGNED -- CTO HALF GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       B6: one function's code + its rule's cron + a READ-only IAM widening; ONE driven run with an explicit bbg_as_of
KEY       platinum/satellites/characteristics.json (opal-data-cot) -- ADDITIVE, prior VersionId rt61ogajZQy79meUlsY1X_mIdPngxJTZ
N         1 writer (text census of code files; matches the COO half's comp-iam read)
ROLLBACK  key copy_object from rt61ogaj...; function -> artifact sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml; rule + policy .tf reverted
COO half  2.0.0_SA_COO~Z @56f4d41933 -- GIVEN
CTO half  1.0.0_SA_CTO~Z -- GIVEN 2026-09-15 ~03:4xZ, for the act as bounded above
```

Push state: LOCAL (this seat never pushes; `0.0.0_AB_MSTR~Z` carries).

-- `1.0.0_SA_CTO~Z`
