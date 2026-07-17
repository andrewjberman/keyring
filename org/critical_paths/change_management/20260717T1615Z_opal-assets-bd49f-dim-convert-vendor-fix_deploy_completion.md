# Deploy-Completion Ledger -- opal-assets-bd49f-dim-convert (stream_parquet vendor fix)

**Status:** COMPLETE
**Closed:** 2026-07-17T16:48Z
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
- [x] 1. Source committed (commit-gate)
- [x] 2. build-and-upload.sh opal-assets opal-assets-bd49f-dim-convert
- [x] 3. terraform plan (expect: bd49f_convert lambda artifact swap ONLY)
- [x] 4. safe-apply
- [x] 5. 0-diff plan
- [x] 6. record-terraform-deploy + tag + push --follow-tags
- [x] 7. Behavior verify: invoke {"date":"2026-07-16"} -> silver date=2026-07-16 lands for BOTH
        dims (ListObjectsV2 acceptance) OR loud sidecar refusal (exit 1) if the gate rules -- and
        tomorrow's 03:05Z fire is the standing-schedule proof, read at next AM.

## Rollback surface
Prior artifact version in S3 (versioned); revert = re-point s3_object_version / prior zip + apply.

## Closure evidence (exercised, 16:2x-16:4xZ)
- THREE stacked defects cured, each surfaced only by exercising the previous fix:
  (1) stream_parquet missing from zip (vendor fix, closure now MECHANICAL ast-scan);
  (2) openpyxl absent from layer set (pandas.read_excel runtime dep -- invisible to import
  scans; existing openpyxl-layer v3 added in TF);
  (3) IAM: original scope-exact policy modeled WRITES only -- own-silver GetObject (SCD2 seed)
  + schwab/08335338/silver/fact_acc read/list (ship-gate denominator) granted narrowly.
- Chain: commits 6a45a04c0/6a...(+map)/94e6ca4c6, three plan->safe-apply->0-diff cycles,
  tag opal-assets-v0.26.0 pushed --follow-tags.
- BEHAVIOR (Rule 22a): invoke {"date":"2026-07-16"} -> rc=0; BOTH dims landed listing-verified
  (dim_advisor_fee_role date=2026-07-16 rows=16008/288661B; dim_account_xref rows=6200/228032B);
  ship-gate coverage 5288/7142 (74.0%) vs 0833 universe; 1 fee-schedule conflict flagged
  deterministic-highest-bps; manifest bd49f-dims-2026-07-16-20260717T163539Z-5f5ecf7c.json.
- ABSENCE TWIN: fired 05:00Z + PUBLISHED (frontier 2026-07-15 < expected 2026-07-16) --
  detection layer PROVEN live; subscriber wiring remains the estate-wide known gap (Andrew:
  alarms not a gate).
- STANDING PROOF pending: tomorrow's 03:05Z scheduled fire (first unattended success) -- read
  at 07-18 AM; twin re-checks 05:00Z.
