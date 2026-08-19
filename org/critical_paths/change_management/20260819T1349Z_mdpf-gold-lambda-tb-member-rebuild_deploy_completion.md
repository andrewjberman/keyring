# Deploy-completion ledger -- mdpf-gold-lambda package rebuild (MDPF_PROVENANCE T-B executing-plane completion)
**Opened+closed same window 2026-08-19 13:47-13:50Z by 0.7.0_AE_CloudOps.** COO sequencing 134403Z (pre-wind-down); CTO GATE-GO 134716Z. DS base finding 134339Z/134324Z: the live package carried the PRE-re-point dim member (committed-not-deployed class).

**Act:** build_package.py at pin f3dbe857244ffe66285d568d4dc8572bf1bd13b2 (HEAD, contains the T-B re-point @12b93b59ba) -> zip sha256 9e1d0ab0...c8a57f05 -> uploaded portal/gold/mdpf/_code/mdpf-gold-lambda.zip w/ content-sha256 metadata -> safe-apply TARGETED aws_lambda_function.mdpf_gold ("0 added, 1 changed, 0 destroyed") -- the staged aws_s3_object.mdpf_route_bindings rider explicitly EXCLUDED (COO 130956Z option (i), untouched).

**Member-diff vs LIVE pre-apply:** CHANGED = dim_mdpf_aggregate_aua_timeseries.py ce9c0284537e1948 -> a7db07bb68f465d5 (== DS expected) + BUILD_MANIFEST.json; ADDED/REMOVED none; ZERO riders.
**Close battery:** 0-diff-on-target re-plan "No changes"; get-function-configuration CodeSha256 == built zip sha (nh0KsEEyZFKfnBg3K0xq+yXWd0UcRjdPjnhWZMilfwU=, LastModified 13:48:28Z); **member re-verified FROM THE REDEPLOYED package** (downloaded post-apply): a7db07bb68f465d5 MATCH -- proves what RUNS, not what was uploaded.

**Discharge path forward:** tomorrow's 13:30Z scheduled run = the PB-1/PB-2 proof vehicle (proof-READ seat from COO's respawn decomposition). **json/mdpf/49financial/aggregate-aua-timeseries.json STAYS HELD until PB-1 PASSES on that scheduled run** -- the TO-4 held-row condition, now with its concrete discharge.
