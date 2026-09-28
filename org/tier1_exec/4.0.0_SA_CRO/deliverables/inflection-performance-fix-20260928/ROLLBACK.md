# Scoped rollback record

Authority: Andrew's direct instruction in ANDREW_DIRECT_20260928_PORTAL_TOTAL_RETURN_FIX.md.
Source fix: 978e4b0eec. Baseline: 06d66b589344c59c7841f17b69d9619828274107.
Pre-deploy versions and hashes: predeploy_versions.json.

If verification fails, restore the old handler source in a new scoped commit,
build/upload the two artifacts with build-and-upload.sh, review a saved Terraform
plan limited to module.generate_positioning.aws_lambda_function.this and
module.generate_etf_returns.aws_lambda_function.this, and apply using safe-apply.sh.
Alternatively restore the captured old artifact S3 versions as new current
versions (including their content-sha256 metadata), then deploy those versions
through the same Terraform procedure. Never update Lambda code outside Terraform.

Restore the three data objects from their recorded S3 VersionIds as new current
versions, preserving ContentType, ContentEncoding and CacheControl. The two
Positioning objects are gzip encoded; ETF returns is plain JSON. Do not delete
versions or restore the unchanged model_portfolio_benchmarks.json.

Invalidate the exact CloudFront request paths for Positioning, Opal aggregate,
and ETF returns on distribution EVTSA9VEHNZVH, plus rewritten /json/ equivalents.
Verify the restored source, output hashes and scoped zero-diff plan; record the
rollback in the deploy-completion ledger. The ignored fix snapshot directory
also contains byte-for-byte pre-deploy packages and outputs for recovery.

Pre-deploy regression result: four tests pass with corrected source; the same
tests against downloaded production source fail 49 subtest comparisons, with
zero execution errors. Inputs include opening-day returns, exact calendar
cutoffs, gaps between sessions, percentage/decimal representations, and an
observation after the requested as-of date.
