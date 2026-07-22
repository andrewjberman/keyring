# MDPF_REVAMP.S5 exact-9 cutover diffs -- BUILT, plan-verified, CTO-GATED (apply held)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-21 ~23:50Z -> 2026-07-22 ~00:51Z (since last log @acb08a7d3)

## Summary
On CTO's "BUILD the exact-9 routing diffs NOW" (after CTO resolved my exact-8-vs-9 grounding flag -> exact-9 confirmed: coherent-8 + the A2 aum-timeseries reversal). Built all 4 pieces of the MDPF cutover, plan-verified them ADDITIVE via the -json plan (the human CF ordered-list plan is positional-churn cosmetics), caught + scope-isolated an unrelated pending TAXSMA change sharing the opal-assets state, and got CTO's design+plan GATE. Committed @803f8b1e7 (pushed). Apply HELD on DE render-clean + COO co-sign; then a scope-isolated opal-assets-targeted apply + evidence bring-back before the portal-auth flip (CTO's final GO).

## Work done (IMPLEMENT) -- 1 commit @803f8b1e7 (4 files, 148+/23-)
The Option-C mechanism (grounded on my prior log @s5_oac_signing + the S5 briefs + live truth): each of 9 CF behaviors is an EXACT CLONE of the /api/general/* catch-all (behavior 8) -- SAME auth-validator + public-data-router (/api/general/->/json/ rewrite) + cache-control-injector L@E -- differing ONLY in path_pattern + target_origin_id. NO L@E origin-swap (that 403s under OAC); the dedicated assets OAC signs the router-rewritten URI natively (b1-proven).

1. **portal-auth/cloudfront-distribution.tf**: `aws_cloudfront_origin_access_control.assets` (opal-data-assets-mdpf-oac, sigv4/always) + a new `S3-opal-data-assets` origin (OAC-backed, no s3_origin_config) + a `dynamic "ordered_cache_behavior"` over a 9-path local, placed BEFORE behavior 8.
2. **opal-assets/monolith.tf**: bucket-policy +Statement `AllowMdpfPortalCloudFrontOACRead` -- cloudfront.amazonaws.com GetObject on the 9 EXACT json/ keys, Condition AWS:SourceArn=arn:aws:cloudfront::313476888478:distribution/EVTSA9VEHNZVH. Exact-key (not prefix); disjoint from DenyParquetUnderBronze17a.
3. **opal-assets-mdpf-portal-publisher/lambda_function.py**: PUBLISH_MAP retargeted portal/* -> the 9 FE-read json/mdpf|portfolios/* hyphen keys. FIXED the aum pair: source segment was ("global","aum_metrics") but DS staged gold/mdpf_revamp/**portfolios**/aum-metrics.json (hyphenated) -> changed to ("portfolios","aum-metrics")/("portfolios","aum-timeseries").
4. **opal-assets/mdpf_portal_publisher.tf**: `mdpf_publisher_write_prefixes` portal/* -> ["json/mdpf/*","json/portfolios/*"] (drives PutObject Resource + ListBucket cond).

The 9 keys (source gold/mdpf_revamp/{seg}/{name} -> FE-read json/): global/49f/inflection aggregate_aua_timeseries -> json/mdpf/{firm}/aggregate-aua-timeseries.json; 49f/inflection account_distribution -> json/mdpf/{firm}/account-distribution.json; global account_distribution -> json/portfolios/account-distribution.json; global non_model_assets -> json/portfolios/non_model_assets.json; portfolios/aum-metrics + aum-timeseries -> json/portfolios/aum-{metrics,timeseries}.json. Global aggregate = the FLAT json/mdpf/global/... live read, NOT the vestigial json/mdpf/aggregate-aua-timeseries.json (443K nested, 0 call sites).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-which HUD rail | (multiple bash) | ENFORCED | blocked a bd49f_reporting_io infra/*.tf grep; switched to native Grep + rail-checked markers on the plan/aws inspections. Working as designed. |
| terraform validate/plan (-json) | opal-assets + portal-auth | PASS | the -json plan is the ACCEPTANCE instrument for a CF ordered-LIST diff (human plan = positional cosmetics). Parsed before/after: origins 7->8, behaviors 24->33, 0 removed, 0 existing changed, my9 before catchall. |
| commit-gate.sh | publisher lambda_function.py | PASS | py_compile + ds-precommit (future-annotations ok) + ruff clean. |
| (raw aws s3api ListObjectsV2 / get-bucket-policy struct) | portal-v2 + assets | PASS | rail-checked markers; grounded the 9 live FE-read keys + the 9 staged source keys before hardcoding paths. |

- **What worked:** grounding the 9 keys on LIVE portal-v2 + staged gold/mdpf_revamp (not the stale S5 brief's 7-key table) caught the global-key flat-vs-vestigial distinction + the aum source-segment mismatch. The -json additivity parse turned an alarming human plan into a provable-clean gate.
- **Gap found:** the Terraform CF ordered_cache_behavior mid-list insertion renders as a scary positional `~ path_pattern`/`- origin_id->null` cascade in the human plan -- ONLY the -json before/after proves it additive. Banked as the CF-plan acceptance method. Also: `record-terraform-deploy.sh` remains absent (flagged prior).

## Key catch -- shared opal-assets state, out-of-scope pending change
The opal-assets plan showed 3 changes, but only 2 were mine. The 3rd -- aws_iam_role_policy.bd49f_reporting_io +ReadTaxsmaRoster (GetObject blackdiamond/49f/_ops/taxsma_roster.json) -- is 0.5.0_AE_OpalETL~A's committed+pushed-but-UNAPPLIED TAXSMA_REGISTRY WS-R3 change (@bb9e26566, "staged for CTO apply"). A blind opal-assets apply would sweep a 49f/TAXSMA change into the MDPF window. Surfaced to CTO -> CTO ruled (b) SCOPE-ISOLATE: my apply `--target`s ONLY aws_s3_bucket_policy.monolith + aws_iam_role_policy.mdpf_publisher_scoped; WS-R3 applies in its own TAXSMA lane.

## Current State (handoff)
- **Diffs @803f8b1e7 (pushed), CTO design+plan GATE GIVEN.** DT 3/3 DONE. Apply HELD on: DE render-clean (pending, DE lane) + COO co-sign on the live 9.
- **APPLY SEQUENCE (CTO-approved, held):** (1) opal-assets `--target` bucket-policy + mdpf_publisher_scoped apply (re-plan WITH --targets, verify ONLY those 2 -- if more, STOP); (2) publisher build+upload + lambda deploy (module.mdpf_publisher -- the PUBLISH_MAP code) ; (3) MANUAL publisher invoke -> populate the 9 json/ keys; (4) ListObjectsV2 verify; (5) live `get-bucket-policy` verify (grounded on the LIVE primitive, NOT comp-iam DESIRED -- Rule 22a); (6) C-pre-flight BOTH shapes on an ISOLATED THROWAWAY distro (200 authed / neg-403 unauthed / failsafe); (7) BRING CTO (a) get-bucket-policy + (b) C-pre-flight; (8) on CTO FINAL GO + DE joint live-URL 404-catch -> portal-auth flip (add OAC+origin+9 behaviors); (9) verify 9 FE URLs serve JSON; (10) rollback TESTED-armed w/ negative control BEFORE publish.
- **ROLLBACK:** primary = remove the 9 behaviors -> paths fall to catch-all 8 -> portal-v2 (UNTOUCHED shadow, legacy nightly keeps writing). Negative control = a legacy /api/general/* path NOT in the 9 stays portal-v2 throughout. Secondary = version-restore (both buckets versioned).
- **cot WS-5 = DONE** (v0.1.0, ledger 5/5, CVO issued) -- logged @acb08a7d3.

## Next Steps
- **[0.4.0_DE_ClientPlatform]** render-check clean on the exact-9 revamp artifacts -> unblocks COO co-sign.
- **[2.0.0_SA_COO]** co-sign on the live 9 (after DE render clean).
- **[1.0.0_SA_CTO]** relay DE-render-clean + COO-co-sign -> my GO-to-apply; give the portal-auth FINAL GO after my (a)+(b) evidence + DE's joint live-URL 404-catch.
- **[0.7.0_AE_CloudOps]** on CTO GO: run the scope-isolated apply sequence above.

## Blockers
None. Apply is HELD (a deliberate multi-gate: DE render + COO co-sign, then CTO final GO) -- a gate state, not a blocker. Diffs built + gated.
