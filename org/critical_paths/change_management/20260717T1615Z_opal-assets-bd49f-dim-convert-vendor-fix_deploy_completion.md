# Deploy-Completion Ledger -- opal-assets-bd49f-dim-convert (stream_parquet vendor fix)

**Status:** OPEN
**Opened:** 2026-07-17T16:15Z
**Owner:** 0.2.0_DT_PortfolioAnalytics (Andrew-direct: assess + begin work on the BD tax-pt2 table chain)
**Lambda:** opal-assets-bd49f-dim-convert (pipeline: opal-assets)

## Defect (grounded)
First scheduled fire (opal-assets-bd49f-dim-convert-daily, 03:05:48Z 2026-07-17, req cf6a599b)
crashed ModuleNotFoundError 'stream_parquet' x3 (initial + 2 retries). The deployed zip carries
only lambda_function.py + bd49f_dim_conversion.py; the converter imports first-party
stream_parquet (vendored-flat by design -- silver-etf/orion/schwab sibling pattern). The
BUILD_MANIFEST's import-closure claim ("pandas+pyarrow+stdlib ONLY") was a hand census, not a
measurement. Consequence: silver dims frozen at date=2026-07-15 while bronze is current at
2026-07-16; tax-pt2's fee-schedule reads unaffected (they read bronze) but the dim chain is dark.

## Fix
stream_parquet.py vendored flat (sha256 2e3762e1... == canonical data/assets/scripts/lib ==
all three siblings); BUILD_MANIFEST corrected + closure now verified MECHANICALLY (ast import
scan, gaps=NONE); source-map files list corrected.

## Legs
- [ ] 1. Source committed (commit-gate)
- [ ] 2. build-and-upload.sh opal-assets opal-assets-bd49f-dim-convert
- [ ] 3. terraform plan (expect: bd49f_convert lambda artifact swap ONLY)
- [ ] 4. safe-apply
- [ ] 5. 0-diff plan
- [ ] 6. record-terraform-deploy + tag + push --follow-tags
- [ ] 7. Behavior verify: invoke {"date":"2026-07-16"} -> silver date=2026-07-16 lands for BOTH
        dims (ListObjectsV2 acceptance) OR loud sidecar refusal (exit 1) if the gate rules -- and
        tomorrow's 03:05Z fire is the standing-schedule proof, read at next AM.

## Rollback surface
Prior artifact version in S3 (versioned); revert = re-point s3_object_version / prior zip + apply.
