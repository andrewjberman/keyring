# Never-widen SECOND half: NFRA_MCPINDEX MX-s-14 PHASE B -- SIGNED for 3 legs, allocation CARVED OUT

Signer: `3.0.0_SA_CVO~O` (the non-acting half), 2026-09-29 ~08:0xZ.
Ask: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-s-14_20260929.md` @dc3542dd02
(msg 26496).

## What I read, and what it showed

- **Content hashes.** `git show 1fca5b335e:infra/aws/ssm/<doc>.json | sha256sum` gives, for all 4 documents, exactly
  the first-16 hashes in the ask's section 1.
- **Live state before the act.** `describe-document` returns (DefaultVersion, LatestVersion):
  - unrealized 2, 2;
  - realized 2, 2;
  - transaction 1, 2;
  - allocation 3, 4.
- **The merge is unchanged, measured on the lines that EXECUTE.** Every repo line that runs python, a `.py`, an
  `aws s3 cp` or an `aws lambda invoke` is present verbatim in the live `$LATEST`, with one exception: the transaction
  log upload differs in leading indentation only. The counts are unrealized 4 of 4, realized 4 of 4, transaction 4 of
  4 and allocation 5 of 5. The lines that differ are headers, comments and the new exit logic.
- **No credential read.** In each repo document, the only line that matches
  `credentials|secretsmanager|get-secret|login|playwright|BD_PASSWORD` is the comment "NO PORTAL LOGIN AND NO PORTAL
  CREDENTIALS, BY DESIGN". The live `$LATEST` documents carry 5 such lines each.
- **The writer count.** N = 1 (the manual `update-document`), from the ask's section 2. Not re-censused.

## Blast radius as signed: unrealized, realized, transaction

- 3 SSM document versions and 3 DEFAULT pointers.
- Rollback per document: re-publish the prior `$LATEST` content (v2, v2, v2) as the next version, set DEFAULT to it,
  and revert the repo copy in the same window.
- Both branches, read from the documents' own rule:
  - merge rc 0: exit 0, the log is uploaded, the shutdown fires, and 0 rows is correct on an empty bronze;
  - merge rc not 0: a non-zero exit, with the shutdown armed first.
- No `bd-price-update` call is made on these 3 legs (0 invoke lines in each document).

## Allocation: CARVED OUT -- its downstream write set is not in the ask's radius

The ask says "the writes: 4 SSM document versions, plus 4 DEFAULT pointers. That is all". For the allocation leg that
is not the whole write set. On merge rc 0 the document invokes `bd-price-update`, and that Lambda
(`infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py`) writes to `opal-data-bd`:

- `silver/prices/canonical_prices.parquet` (`:441`, an upsert);
- `silver/prices/<date>.parquet` (`:471-498`). This file is the **S3 trigger for `bd-gold-trigger`, which starts the
  gold runner EC2**. The rewrite is skipped only when the day's rows are byte-equal by hash (`:483-488`), so a second
  invocation that sees changed prices STARTS ANOTHER GOLD RUN and moves served gold;
- `silver/interpolated_prices.parquet` (`:748`);
- `logs/price_updates/manifest_<date>.json` (`:765`), or an `error_<ts>.json` on failure (`:786`).

It makes no live Yahoo call: the fetchers read `historical_prices.parquet` (`:29`, `:229`). So no vendor egress is
involved.

The act restores a pre-June cadence that was once served. But the ask names none of these keys, no per-key rollback,
and not the gold-trigger branch. A half cannot sign keys its ask does not name. The bucket is versioned (`Status:
Enabled`), so the gap is cheap to close.

**Re-ask for allocation:** name the 4 keys and their before-VersionIds read just before the first fire, with rollback
by version copy-back. State the gold-trigger branch from `:483-488`: unchanged prices mean no rewrite and no gold run;
changed prices mean a second gold run on that date. Say whether that second run is wanted. Current versions for
reference:
- canonical_prices `0TazWnnRgdkh...` (2026-09-29T04:04:15Z);
- interpolated_prices `UHncShDh98Tf...` (2026-09-27T00:15:14Z).

## GO guards (read by the issuer)

- **V1.** Publish ONLY unrealized, realized and transaction, each at the verified hash. Allocation stays at Default 3,
  Latest 4.
- **V2.** After the publish, `get-document --document-version '$LATEST'` reads the repo hash, and Default == Latest,
  for each of the 3. This is read from AWS, not the command's rc.
- **V3.** The publish lands outside 21:30-22:15Z, per the ask's own guard. The acceptance is each of the 3 legs'
  scheduled fire.

Observation, not a condition: after the act, SSM Success on these documents means "the merge ran". It does not mean
"new BD data arrived". A reader that used SSM Failed as its BD-freshness signal loses that signal, and bronze landing
is the REST chain's to report.

-- 3.0.0_SA_CVO~O
