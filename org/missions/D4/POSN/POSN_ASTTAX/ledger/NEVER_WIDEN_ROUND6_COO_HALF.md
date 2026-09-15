# NEVER-WIDEN SIGN-OFF -- COO HALF -- POSN_ASTTAX round 6: B6 (the characteristics artifact gains the per-ticker block; the rule moves; a driven run)

**Signer:** `2.0.0_SA_COO~Z` (L5/L6 owner). **Counterpart:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND6_CTO_HALF.md` (owed; the
order `TO-W1-1` cites BOTH by path and its worker REFUSES the deploy leg unless both exist at HEAD). **PRD:** v0.10 @`59113e257a`
(C-HOLDING-MEASURES as amended, C-B4-SCHEDULE; the GLD returns rule imported from `etf_positioning_gold.py`, its backfill landed @d3d2ffc4a5); **Andrew:** ~02:3xZ @`0553548fe2` (tonight), ~03:0xZ
@`365580f244` (the return-history backfill, a CTO act this half does NOT cover). **Decomposition:**
`decompositions/POSN_ASTTAX_DECOMP_round6.md` cell `AT6-s-1`. Pure ASCII.

## 1. THE ACT AND ITS BLAST RADIUS -- what the act MAY touch, per key, with the rollback for each

**The act (three legs, one cell, one worker `0.9.0_WK_POSN_ASTTAX~24`):** (a) the producer's code changes -- `tickers` block +
`method.tickers_block`, `etf_positioning_gold.py` packaged by pin as a read-only member; (b) Terraform: the function's artifact
(`s3_object_version`, `source_code_hash`), the rule's cron `cron(20 7 * * ? *)` -> `cron(30 12 * * ? *)`, the IAM policy's READ
grant widened (below); (c) ONE driven invoke with an explicit `bbg_as_of`.

| key (bucket `opal-data-cot`) | writers, N printed | change | rollback |
|---|---|---|---|
| `platinum/satellites/characteristics.json` | **N = 1**: `build_satellites_characteristics.py` `publish()` :429-434 through `cot-satellites-characteristics-producer` (PutObject pinned to this key, Sid `WriteSatellitesCharacteristics`, `satellites-characteristics-producer.tf:132`); the only role holding a PutObject pinned to this key (the B4 order's `comp-iam gaps` read); no other producer names the key as a write target (reader census, s.3) | ADDITIVE: `tickers` (every ticker any satellite holds, once, with `source`) and `method.tickers_block`; **every other field identical for the same inputs** -- the purity difference control (HEAD's `build()` vs the cell's over the same three inputs, minus the two additions) is the discriminator BEFORE the deploy | the prior object version, read at the cut: VersionId `rt61ogajZQy79meUlsY1X_mIdPngxJTZ` (2026-09-14T21:45:13Z, 54825 B; bucket versioning Enabled) restored by `copy_object` (a new version, never a delete); AND the function re-pointed to the prior artifact version `sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml` (content-sha256 `6M4Co5N81OD/SxD+fS0/pzbByeBKeYaVh8z/kszV3Vk=`, B4 ledger L2) by a targeted apply; AND the rule's cron reverted in the `.tf` |
| the rule `cot-satellites-characteristics-producer-daily` | Terraform | `cron(30 12 * * ? *)` UTC (08:30 EDT / 07:30 EST), after the 07:00 America/New_York pull in both DST states; state ENABLED; the target unchanged | revert the one line, re-apply |
| IAM `aws_iam_role_policy.cot_satellites_characteristics_producer_s3` | Terraform | READ ONLY widening: `s3:ListBucket` on `arn:aws:s3:::opal-data-etfs` with `s3:prefix` conditioned to `bbg/*` and `bbg-testpull/tickers/*`; `s3:GetObject` on `opal-data-etfs/bbg/*/history_topup.parquet` and `opal-data-etfs/bbg-testpull/tickers/*/history.csv` (what `load_history` and `_load_backfill_history` read); NO new PutObject, NO new bucket, the cross-firm deny UNCHANGED | revert the `.tf`, re-apply |
| `registry.json`, `holdings.json`, `positioning_data.json`, every `bbg/` object | -- | READ only; **NOT WRITTEN** | -- |
| anything else | -- | **NOT SIGNED** | -- |

**Writers of the property AFTER B6: N = 1, unchanged.** Readers of the key (the consumers of the additive change): the portal Satellites
adapter through the B5 route (`/api/scoped/satellites/characteristics.json`, edge cache DefaultTTL 60 s -- the new bytes reach the page
within a minute of the driven run; no invalidation act is part of this half) and F4 (round 6) which ATTACHES the new block. The B5
router's leaf allowlist is unchanged (the key's path is unchanged).

## 2. THE NEW REACHABLE STATES, NAMED

1. **A driven run off the rule's clock with an explicit `bbg_as_of`** (the handler forwards it, `lambda_function.py:82-83`): the
   partition is the NEWEST `bbg/<date>/characteristics.parquet` present at the run, LISTED and PRINTED by the worker, never assumed; a
   partition that does not exist makes the producer REFUSE (loud, nothing written) -- Branch B below.
2. **A cron that now fires AFTER its input** (the ~11:0xZ pull): on a day the pull is late, the producer refuses loudly at 12:30Z and
   the next fire retries; it never walks back to an older partition (the producer's own rule, unchanged). The rule's first fire
   (2026-09-15 12:30Z) is the ORGANIC leg, recorded by this seat as a row and the B4/B6 ledger's L8 -- not waited on (Rule 27).
3. **A wider READ grant** used by the returns rule -- listed above; graded by `comp-iam gaps` on the `.tf` in the cell and by the
   live apply's HALTGT sweep.

## 3. EXPECTED OUTCOME, BOTH BRANCHES (read from the producer's own rule, never predicted from the input's shape)

- **A -- preconditions met** (the purity control identical minus the two additions; the plan reads exactly the module, the policy and
  the rule; `safe-apply` complete; unscoped 0-diff): the driven invoke returns `rc 0`; `characteristics.json`'s VersionId moves off
  `rt61ogaj...`; the served `tickers` block equals the local dry run's over the same inputs (25 tickers, each once; sources 23
  `positioning_data` / 1 `bbg` (GLD) / 1 `none` (CASH); the five shared tickers' `aum` equal 5 of 5); the served `satellites` block equals
  the pre-deploy served block when the `inputs` triple (`holdings_as_of`, `positioning_data_as_of`, `bbg_as_of`) is unchanged, else the
  dry-run arm at the same inputs; `describe-rule` reads `cron(30 12 * * ? *)` ENABLED. GLD's `returns`: computed where the backfill and
  the frontier exist at the run, else NULL with the rule's reason printed -- BOTH are Branch A (the value is read from the rule).
- **B -- any precondition unmet, or any bar clause fails:** BEFORE the apply, NOT COVERED -- no write. AFTER the apply and before the
  driven run, the deploy is rolled back (the artifact version and the `.tf` above) in the same session. AFTER the driven run, a served
  artifact that differs beyond the two additions (a `satellites` leaf moved at unchanged inputs; a ticker twice; a ticker missing; a
  non-set field changed): `copy_object` from `rt61ogaj...`, the function re-pointed, the rule reverted, the row filed. A driven invoke
  that REFUSES (partition absent, a read denied): nothing was written -- the refusal is the measured act, the row names the reason and
  the organic leg stays.

### R1 AMENDMENT 2026-09-15 ~04:1xZ -- the identity pair (PRD v0.11 @ab2ee8052a C-HOLDING-IDENTITY): a READ on DynamoDB `etf-classifications`

**Why:** Andrew ~04:0xZ (*"looks like none of this is going through ETFClassifier"*; rows Z-S139 by the CTO, Z-S141 by this seat). B6's
`tickers` block ALSO carries `name` and `management_style` for every ticker any satellite holds, read through the estate's one classifier
module (`etf_classifications_dynamodb.py`, `get_item` per distinct ticker, ~25 reads per run -- the same call the registry producer
already makes under its own `ReadEtfClassifications` grant). **What this adds to the act's blast radius:** ONE READ grant --
`dynamodb:GetItem` ONLY on `arn:aws:dynamodb:<region>:<account_id>:table/etf-classifications` (the one action the module's
per-ticker path calls; the CTO half A1 @2c6b7d8887 names exactly it; no BatchGetItem -- narrowed ~04:2xZ from this seat's first text) in
`aws_iam_role_policy.cot_satellites_characteristics_producer_s3` -- and two more fields inside the ADDITIVE block (`name`,
`management_style`, NULL + counted where the table has no row; `method.tickers_block.identity_source` / `identity_missing`). **What it
does NOT change:** the ONE key, N = 1 writer, the rollback (the same prior VersionId and artifact version), the table's own writers
(R1's retag script and the seeder; this act WRITES NOTHING to the table -- no `PutItem`, no `UpdateItem`, no `Scan`, no `BatchGetItem`), the schedule, the
driven run, both branches. The purity control still requires every pre-existing field identical for the same inputs. Rollback of the
grant: revert the `.tf`, re-apply. COO half for this amendment: `2.0.0_SA_COO~Z`, GIVEN, 2026-09-15 ~04:1xZ; the CTO half amends to match.

## 4. WHAT THIS HALF DOES NOT COVER

The Bloomberg return-history backfill (a CTO act, its own ledger); the portal cells F4 and F5 (no served key moves); any promote, push
or gitlink move; `registry.json` / `holdings.json` (R2's halves); any monitor; any change to the ETF gold pipeline or its bucket's
contents.

## 5. SIGNED -- COO HALF GIVEN (for the act as bounded above; the deploy leg still waits on the CTO half at HEAD)

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       B6: one function's code + its rule's cron + a READ-only IAM widening (S3 history prefixes; R1: DynamoDB GetItem on etf-classifications); ONE driven run with an explicit bbg_as_of
KEY       platinum/satellites/characteristics.json (opal-data-cot) -- ADDITIVE change, prior VersionId rt61ogajZQy79meUlsY1X_mIdPngxJTZ
N         1 writer (unchanged); readers: the B5 route -> the Satellites adapter (F3 today, F4 after)
COO half  2.0.0_SA_COO~Z, GIVEN 2026-09-15 ~03:2xZ; re-read at v0.10 @59113e257a ~03:3xZ, key list unchanged (a changed key list re-opens it)
CTO half  1.0.0_SA_CTO~Z -- ledger/NEVER_WIDEN_ROUND6_CTO_HALF.md (owed)
```

-- `2.0.0_SA_COO~Z`
