# 0.7.0_AE_CloudOps — MDPF_REVAMP S4 deploy (COMPLETE) + S5 cutover planning (in-flight)
**archetype:** MIXED
**secondary_archetypes:** DEPLOY, COORDINATE, DIAGNOSE
**Session:** crash-restore ~2026-07-21T16:29Z -> ~19:25Z (open; holding for CTO gate)

## Summary
Crash-restore of the MDPF chain owner. Two arcs:
1. **S4 DEPLOY (COMPLETE + verified):** wired the revamp PRODUCER to run PARALLEL on the mdpf-daily-runner nightly (dispatch Stage 6, non-fatal, gold/mdpf_revamp/* ONLY, publisher OFF = publish-HELD). Deploy-completion ledger 6/6 CLOSED. Andrew-direct deep deployed-state IAM verify all-green. Folded account_distribution into the 7-key scheduled set per Andrew-direct.
2. **S5 CUTOVER planning (in-flight, gated):** what looked like a schema-divergence blocker was diagnosed to DEAD CODE; the data is correct/models-only; the roll-over is a pure serving cutover. Ran a tandem with 0.4.0_DE_ClientPlatform (spawned this session). CTO ruled Option A (origin-repoint via L@E origin-select). Pre-serving render-check: Global+49F PASS, INFLECTION held on a revamp-DATA gap. Proposed a per-firm split. Holding for CTO split-vs-hold + diff gate.

## Work done
### S4 (DEPLOY)
- Mechanism (lowest-blast, CTO ruling A): NEW non-fatal Stage 6 in the EXISTING infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh -- reuses trigger+EC2+cadence; runs dim_mdpf_aggregate_aua_timeseries --firm all + dim_mdpf_account_distribution --firm {49financial,inflection,global} --upload + dim_mdpf_non_model_assets --upload; wrapper stages aggregate (script has no self-upload) + writes gold/mdpf_revamp/meta/cycle-complete.json marker LAST. NEVER portal/*, NEVER legacy Door-6.
- IAM: infra/aws/terraform/mdpf-pipeline/{main.tf,iam.tf} +3 tight stmts on mdpf-runner-scoped (AssetsRevampSilverRead GetObject on opal-data-assets silver 4 trees + gold/mdpf_revamp; AssetsRevampStagingWrite PutObject gold/mdpf_revamp ONLY -- NO portal write; AssetsRevampListScoped prefix-conditioned ListBucket). terraform plan 0-add/1-change/0-destroy.
- Code deploy: 5 files (3 producers + mdpf_revamp_model_crosswalk + _trading_day_calendar) -> s3://opal-data-mdpf/code/scripts/gold/ byte-identical (ETag==md5); dispatch -> code/mdpf-daily-dispatch.sh. _trading_day_calendar diff vs old S3 = pure-comment (legacy Stage 5 is_trading_day byte-identical -> UNCHANGED).
- Deep deployed-state verify (Andrew-direct "check aws iam ... nothing missing from deployed state"): live get-role-policy 21==TF 21 (nothing dropped); opal-data-assets bucket policy = only DenyParquetUnderBronze17a (does NOT catch gold/mdpf_revamp JSON or silver reads); i-02448edb624a7a7cf -> mdpf-daily-runner-profile -> mdpf-daily-runner-ec2-role (grant reaches runtime); bucket enc AES256 blocks only SSE-C.

### S5 (COORDINATE + DIAGNOSE)
- Material flag raised (revamp global 62% smaller than "served") -> CTO HELD the push. DIAGNOSED: was comparing json/mdpf/aggregate-aua-timeseries.json (443K NESTED, VESTIGIAL 0-call-sites); the FE's LIVE global read is getMdpfAggregateAUATimeSeriesByFirm('global') -> json/mdpf/global/aggregate-aua-timeseries.json (161K FLAT, ModelPortfolios L378-380) which is field-identical to revamp (165K). Independently re-verified (grep call-sites + head-object sizes). ZERO FE change across all 7 keys.
- Andrew reframes folded: data-side correct / models-only / ETFs future / FE-aligns-forward. account_distribution + aum_metrics/aum_timeseries dispositions (TO-2, legacy-served).
- A-vs-2 reconciliation: DURABILITY finding (verified at source build_aggregate_aua_timeseries.py L503/L651: legacy slice_per_firm rewrites json/mdpf/{firm}/ incl global nightly -> content-swap Option 2 CLOBBERED). CTO ruled OPTION A (repoint). Caught + corrected an A-vs-2 conflation (CTO/DE briefly).
- Sub-mechanism: A-L@E (origin-select in the shared /api/general/* router) over A-behaviors (distro at 25-behavior soft-limit). Material catch: /portfolios/* prefix too broad (would 404 legacy aum-metrics/aum-ts) -> route EXACT 7 keys only + fail-safe default portal-v2 + negative control.
- Ground-first (CTO cond 4): correct L@E = infra/aws/lambda-edge/public-data-router/index.mjs (v4 /api/general/*->/json/*); the infra/aws/lambda/public-data-router/ copy is the STALE /api/public/* predecessor. comp-blast: no downstream consumers.
- Render-check (DE @b30f03c1f, route-injection vs 7 revamp artifacts): Global PASS + 49F PASS; INFLECTION picket-fence from revamp-DATA post-onset None gaps (NOT FE/serving). Proposed per-firm SPLIT (Global+49F 5 keys now / inflection 2 later).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-blast | mdpf-daily-runner | PASS | blast = MDPF nightly chain; HOLD claims all historical/closed |
| comp-iam service | mdpf-daily-runner-ec2-role | PASS | DESIRED 19 stmts pre-change; confirmed zero opal-data-assets grant (the gap) |
| comp-pipescript io | dim_mdpf_aggregate_aua_timeseries | WARN | dynamic keys -> "no s3_layout"; read write path directly |
| comp-pipescript deployed | 3 revamp producers | GAP | scoped to opal-data-bd/code; does NOT cover the mdpf runner code prefix -> used live ETag==md5 instead |
| comp-iam gaps | full | PASS | NO new gap for mdpf-daily-runner-ec2-role (8 reported are other roles, pre-existing) |
| comp-routes behaviors/origins | portal distro | PASS | /api/general/* -> portal-v2-json + public-data-router L@E; opal-data-assets NOT yet a CF origin; distro at 25 behaviors |
| comp-routes trace | /api/general/... | FAIL | MSYS mangles leading-slash arg; MSYS_NO_PATHCONV=1 breaks the tool's own path -> fell back to `behaviors` |
| comp-blast | public-data-router | PASS | leaf; no downstream lambda/pipeline consumers |

- **What worked:** comp-blast + comp-iam grounded the S4 blast + the IAM gap cleanly; comp-routes behaviors/origins gave the CF cutover surface (no assets origin, 25-behavior limit) that drove the A-L@E pick.
- **What failed:** comp-routes trace unusable on `/api/...` URLs (MSYS leading-slash mangle both ways) -- behaviors/origins covered it.
- **Gap found:** (1) comp-pipescript deployed has NO coverage of the mdpf-daily-runner code prefix (bd-centric PIPELINE_MAP) -> "DEPLOYED==imported" fell to live head-object ETag==md5. Flagged to CTO for a future comp build. (2) IAM simulate-principal-policy remains the necessary primitive for new-key grants (comp-iam is action-only).

## Deployment Sequence + Verification (AE)
1. safe-commit 88fba8ccc (TF + dispatch + ledger) -> push origin/CLOUD.
2. `terraform plan -out` -> `0 to add, 1 to change, 0 to destroy` (aws_iam_role_policy.mdpf_runner in-place).
3. `.tools/safe-apply.sh -chdir=infra/aws/terraform/mdpf-pipeline apply s4-iam.tfplan` -> "Apply complete! Resources: 0 added, 1 changed, 0 destroyed" (comp-tagauthz PASSED).
4. 0-diff re-plan -> "No changes. Your infrastructure matches the configuration."
5. tag mdpf-pipeline-v1.6.0 (annotated on 88fba8ccc) -> push --follow-tags.
6. `aws s3 cp` 5 code files + dispatch -> live head-object ETag==local-md5 MATCH all 6.
7. IAM simulate-principal-policy (SEPARATE calls, 1 arn each, context on conditioned ListBucket): POS GetObject silver=allowed, POS PutObject gold/mdpf_revamp=allowed, POS ListBucket+prefix=allowed, NEG PutObject portal/*=implicitDeny (DISCRIMINATING).
8. Deep deployed-state verify (get-role-policy 21==21, bucket policy, instance->role, encryption) all-green.
9. Ledger 20260721T1704Z: L1-L6 all closed -> `deploy_ledger.py close` OK.

## Blockers
- **INFLECTION cutover: HELD (routed, not mine)** -- revamp inflection by_model.model_value has post-onset None gaps (onset 05-15; None on 05-21/06-01/07-01/07-13-15 + 16 zeros last 60d) absent in served (onset 05-18, zero post-onset nulls) -> daily chart would degrade smooth->picket-fence. Evidence: DE render-check @b30f03c1f. NOT FE/serving -- a revamp inflection DATA gap (likely in-flight DS Eclipse finalization). Routed by DE to CTO to assign the revamp-inflection owner. Global+49F unaffected.

## Current State (handoff — zero-context reader)
- **S4 = DONE + LIVE.** mdpf-pipeline-v1.6.0 applied; mdpf-runner-scoped role has the 3 AssetsRevamp stmts (live-verified); Stage 6 deployed to s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh + 5 code files at code/scripts/gold/. The revamp producer stages 7 keys to s3://opal-data-assets/gold/mdpf_revamp/* each nightly (publisher OFF). Cycle-1 = next INF-completion-triggered fire (mdpf-daily-refresh-trigger event-driven on opal-data-inf/gold/meta/pipeline-complete.json); AE responds on CTO's per-cycle S3-verify signal (NO session-Monitor, per COO). Ledger CLOSED @0839af36d.
- **S5 = IN-FLIGHT, HELD.** Architecture LOCKED: Option A / A-L@E origin-select. Correct L@E = infra/aws/lambda-edge/public-data-router/index.mjs (add an EXACT-7(or 5)-key branch: origin=opal-data-assets + /json/* rewrite; else untouched portal-v2 fail-safe). Needs: NEW CF origin S3-opal-data-assets-json (OAI/OAC) + opal-data-assets bucket-policy Allow for that OAI on json/mdpf/*+json/portfolios/* ONLY; publisher PUBLISH_MAP retarget (portal/* underscore -> json/mdpf|portfolios/* hyphen, 7 keys, drop aum_metrics/aum_timeseries) + publisher IAM PutObject json/*. Serving-target map + FE-consumption audit: docs/briefs/mdpf-revamp-s5-rollover-FE-consumption-audit-20260721.md (DE @b30f03c1f). Strategy/compare doc: docs/briefs/mdpf-revamp-s5-rollover-compare-20260721.md (@178bb9066). Rollback = L@E-revert (instant, legacy shadow) + version-manifest; version copy-object restore EXERCISED byte-identical. Distro EVTSA9VEHNZVH.
- **Pre-cutover gate (all required):** DE render-check PASS (Global+49F done; inflection held) -> CTO gates the diffs -> IAM simulate per-key + NEGATIVE control (aum-metrics/aum-ts stay portal-v2) -> pre-repoint populate+verify -> router-revert tested-armed WITH neg control -> COO re-co-sign -> Andrew PUSH-NOW GO -> route-switch (single serve-widen) -> verify-before-serve cycle-1 (publisher HELD/manual through cycle-1, auto-arm deferred).

## Next Steps
- **[1.0.0_SA_CTO]** decide per-firm SPLIT (Global+49F 5 keys now / inflection 2 later) vs hold-all-7; then gate the L@E diff + origin/OAC/bucket-policy TF + publisher diff (I bring same-turn on your call).
- **[0.7.0_AE_CloudOps]** on CTO's split-vs-hold: build the A-L@E origin-select diff (resolve the OAC-signing pattern for the new assets origin) + the CF/publisher diffs; run IAM simulate per new key + the negative control; test the router-revert.
- **[revamp-inflection owner (DS Eclipse, CTO to assign)]** fill the post-onset inflection model_value gaps OR rule them expected (-> DE does a small FE null-carry-forward). Gates the inflection cutover only.
- **[0.4.0_DE_ClientPlatform]** LIVE-URL render-check against the real 7 /api/general/... URLs once the serving-target is up (the 404-catch); confirm inflection stays legacy-smooth if we split.

## MCP traffic
~30 messages handled. Significant: CTO GO on S4 apply (172531Z) + S4 completion ACCEPTED (175939Z); CTO S5 STANDBY + verify-before-serve refine + Option-A RULING (185126/185745/190507Z); CTO A-L@E gate + 6 conditions (191420Z); COO S4 GO (163250Z) + direction (cycle-1 detector = durable marker, no session-Monitor; recon staged, NFRA held) (175824Z); DE tandem (audit @86c741876, render-check @b30f03c1f, seam catches). Andrew-direct mid-session: account_distribution scope, deployed-state IAM verify, models-only/data-correct/FE-alignment reframes.
