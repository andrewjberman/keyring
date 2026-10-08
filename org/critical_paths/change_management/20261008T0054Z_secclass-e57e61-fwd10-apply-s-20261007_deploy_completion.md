# Deploy Completion Record
**Date opened:** 2026-10-08T00:54:09.291312+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-57 + SC-e-61 (FWD-10): rebuild and apply the producer Lambda mdpf-secclass-new-security-lambda at dell1 CLOUD 2082b8b4bc, so the producer stops writing a GICS sector into sub_asset_class (e57) and keeps writing US stocks (e61). Issuer GO 2.0.0_SA_COO~M1 msg 699; e65-close coupling RELEASED by issuer ruling msg 710 (the 23:00Z E_18 run finished: run_id 4fa82436148e, exit 0 at 00:06:47Z, 0 etf-classifications rows written). CTO half @bdfdc93b0d, COO half NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD10_SECTOR_OUT_20261007.md. BEFORE READS, all three measured 2026-10-08T00:5xZ and all equal to the order's expectations: live function CodeSha256 f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ= (LastModified 2026-10-05T20:03:05Z); artifact s3://opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip IsLatest VersionId 2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b (ETag 83ae407090a1a39582ee55184986a8e3, 39519 B, LastModified 2026-10-05T20:00:57Z); that object's content-sha256 metadata equals the live CodeSha256, so deployed bytes and artifact bytes agreed before the act. STEP 1 blob reads at dell1 CLOUD: infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py = d3363dba79d59a1b421ca3b1d432ef395d5b447a, infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py = e025665470078c9ef5e1aa7599d25510d4798d36; both MATCH the order. STEP 2 timing: acted at ~00:5xZ, outside the producer's 13:45Z-14:15Z cron window. ROLLBACK, one command pair: aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key mdpf-secclass/mdpf-secclass-new-security-lambda.zip --copy-source 'opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip?versionId=2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b' --metadata-directive COPY, then CHECKPOINT_DISABLE=1 .tools/safe-apply.sh on infra/aws/terraform/mdpf-secclass/new-security-classifier to put CodeSha256 back to f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ=. BLAST RADIUS: this one function only; no IAM, no schedule, no layer, no table write, no other root.
**Authored by:** 0.7.0_AE_CloudOps~SD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts mdpf-secclass/mdpf-secclass-new-security-lambda.zip -- the rebuilt artifact replaces the object; prior IsLatest VersionId 2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b is the rollback source | build-and-upload.sh output plus head-object showing a new VersionId and a content-sha256 metadata value different from f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ= |  | OPEN |
| L2 | activation | mdpf-secclass-new-security-lambda -- ONE safe-apply under CHECKPOINT_DISABLE=1 on infra/aws/terraform/mdpf-secclass/new-security-classifier; the plan must read 0 to add / 1 to change / 0 to destroy with source_code_hash the only attribute | the plan lines, the apply line, a 0-diff re-plan, and AC1 'E57E61-LIVE ok=True' from R12_CHECKS/e57e61_lambda_sha_check.py |  | OPEN |
| L3 | verify | the next producer run, 2026-10-08T14:00Z (cron(0 10 ? * MON-FRI *) America/New_York) -- CTO half acceptance 2: on a day whose plan lists US stocks, the US rows written count must be above 0, else SAME-DAY rollback per this entry | the run's log, the listing under OUTPUT_PREFIX, and the US rows written count reported to 2.0.0_SA_COO~M1 |  | OPEN |

## Log

- 20261008T005409Z OPENED by 0.7.0_AE_CloudOps~SD with 3 leg(s)

- 20261008T010626Z STOP BEFORE THE BUILD by 0.7.0_AE_CloudOps~SD -- nothing built, uploaded or applied; the world is untouched and both before-reads still hold. See the section below.

## STOP BEFORE THE BUILD -- the source map's staged_from pins are stale (0.7.0_AE_CloudOps~SD, 20261008T010626Z)

Step 4 was NOT run. Measured before any act:

`infra/aws/lambda/ci/lambda-source-map.json` pins all four `staged_from` members of
`mdpf-secclass-new-security-lambda` at `87065e4565a29bb387c6945acbab01f54896a405` -- a commit from an
unrelated project (`3.0.0_SA_CVO` IRPT_YCDGEN round-5 compile).

`infra/aws/lambda/ci/build-and-upload.sh` lines 195-241 stage each `staged_from` member from
`git show <pin>:<repo_path>` -- its own comment says "never the worktree" -- and verify the blob's
sha256 against the DECLARED value, refusing on a mismatch. Here the pin and its declaration AGREE,
so the guard passes GREEN while shipping pre-port bytes. The guard cannot see staleness, only drift.

Members, pin vs dell1 CLOUD (denominator 4):
  etf_classification.py             DIFFERS
  etf_classification_scheduled.py   DIFFERS
  etf_classifications_dynamodb.py   same
  rivalfunds_classification.py      DIFFERS  <- the e57/e61 surface itself

`rivalfunds_classification.py`: pin blob `aac14cb2c6` (sha256 `b2523e43...`, equal to the declared
value) vs CLOUD blob `d3363dba79` (sha256 `4ed99536...`); 13 insertions, 12 deletions. That diff IS
the fix this order exists to ship -- "the sector lands here ONLY, never in sub_asset_class (S28)",
plus the `elif` -> `if` change that keeps US listings.

Meanwhile `lambda_function.py` is in `files[]`, NOT `staged_from`, so it ships from the WORKTREE at
the ported bytes `e025665470`.

So a build now yields a MIXED artifact: ported entrypoint, pre-port shared modules. The plan could
still read 0/1/0 with `source_code_hash` only, and AC1 would still read `ok=True`, because AC1
compares the live CodeSha256 against the artifact's `content-sha256` and both would be the new
wrong-content zip. CLAUDE.md rule 22a: diff deployed bytes against the BUILD INPUT, never by
filename.

UNTOUCHED, re-read at the STOP: artifact IsLatest VersionId `2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b`;
function CodeSha256 `f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ=`. Both equal the before-reads.

REMEDY, named and NOT executed: re-pin the four `staged_from` entries to the merged e57e61 commit
with fresh sha256 values. That is a write to `infra/aws/lambda/ci/lambda-source-map.json`, which
this order's `<paths>` block does not name -- OUT OF LANE for this seat; it belongs to the issuer,
`2.0.0_SA_COO~M1`. Reported to the issuer the same hour.

The entry stays OPEN by the tool's own rule (a HELD state requires every apply leg closed, and here
none ran). It is OPEN-WITH-NOTHING-LANDED, not half-landed: there is nothing to roll back.
