# 0.7.0_AE_CloudOps — MDPF S5 mechanism (OAC test + Option C) + WS-5 gate-ready build
**archetype:** MIXED
**secondary_archetypes:** VALIDATE, COORDINATE, IMPLEMENT
**Window:** ~2026-07-21T19:29Z -> ~22:26Z (continues; both workstreams gated/held)

## Summary
Two workstreams in a long CTO/COO/peer coordination loop:
1. **MDPF S5 cutover MECHANISM** settled end-to-end. My "62% smaller schema" blocker was DIAGNOSED to DEAD CODE (the FE reads the flat json/mdpf/global/ slice, not the vestigial 443K nested one). Architecture went A-repoint -> C-direct-behaviors after I proved the OAC+L@E-swap signing likely fails; the "25-behavior limit" I'd carried was a MISCOUNT (real quota 75). Ran an ISOLATED-throwaway-distro OAC signing test (b1): PROVEN 200 + discriminating 403, ZERO residual. Design = exact-8 direct behaviors, then exact-9 (Andrew re-added aum-timeseries as DS-produced). CENSUS DONE/co-signed; apply held on A1+A2 producers + co-sign.
2. **WS-5** (WSE_COTMDL): built the cot-rebalancer producer's scoped role + daily schedule TF gate-ready; caught + COO-endorsed an over-grant (TO conflated the chain); reconciled to the canonical BD-REST rework; caught+fixed an env-var firm-safety seam. 4 commits, validate-clean, deploy-ready.

## Work done
### MDPF S5 (VALIDATE + COORDINATE) -- no repo commits (design/test/coordination)
- SCHEMA FLAG RESOLVED: independently re-verified the DE audit -- getMdpfAggregateAUATimeSeries() (443K nested) has 0 page/component call sites (vestigial); the live global read is ByFirm('global') -> json/mdpf/global/aggregate-aua-timeseries.json (161K FLAT) == revamp global. ZERO FE change.
- A-vs-2 durability finding -> CTO ruled Option A; then the OAC+L@E-swap signing risk (doc + shared-advisor-router uses OAI, not OAC) FLIPPED it to Option C (direct behaviors: own-origin OAC signs natively, no swap). QUOTA correction: L-F432D044 default=75, distro at 25 -> 50 headroom -> exact-behaviors, no quota increase (did NOT file the unnecessary request).
- b1 OAC SIGNING TEST (isolated, zero-residual): stood up throwaway distro E31OM0DKGN8S2J + OAC E1L5EJVWCXN0P0 + scoped bucket-policy (SourceArn=test distro) + test key. curl POS=200(body), NEG=403(un-granted key). Torn down ALL (distro NoSuchDistribution, OAC NoSuchOriginAccessControl, policy reverted to 17a-only, key deleted, NO L@E created). Proved Option C's own-origin OAC signing model.
- Design C APPROVED (CTO): 8->9 exact behaviors = clones of the catch-all /api/general/* (same auth L@E + public-data-router rewrite L@E, ONLY TargetOriginId->assets origin) + dedicated OAC + exact-key SourceArn bucket-policy + publisher 9-key PUBLISH_MAP retarget. Rollback=remove-behaviors (legacy portal-v2 untouched shadow). C-pre-flight (both path shapes) exercises revert before any real flip.
- Andrew redirect: A2 aum-timeseries FE-derive -> canonical DS-produced -> exact-9 (+1 behavior, +1 publisher key, +1 policy key). CENSUS DONE/co-signed. Readiness pulse -> READY-TO-EXECUTE-ON-CLEAR (no AE blocker; ~1-1.5h wall-clock, CF-propagation-bound).

### WS-5 (IMPLEMENT) -- 4 commits
- see commit messages: ab268cb90 (gate-ready role+schedule), b2add5091 (canonical BD-REST reconcile: rename cot-rebalancer-runner, DROP layer->py3.12, role unchanged), bc9f2585a (env-var firm-safety fix), 5d49bd8b1 (TODO cleanup).
- Scope corrected to per-producer least-privilege (COO-endorsed): the TO conflated the WS-E chain into one role; WS-5 = WS-1 bronze producer role ONLY. Stamp->silver deferred to WS-2 (COO ruling: build-where-target-lives). Secret grant GetSecretValue-only (CTO ruling: runner is DUMB ABOUT AUTH, refresh chain owns it).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-routes behaviors/origins | portal distro EVTSA9VEHNZVH | PASS | /api/general/* -> portal-v2-json + public-data-router L@E; opal-data-assets NOT a CF origin; 25 behaviors (=count, not the 75 limit) |
| comp-routes trace | /api/general/... | FAIL | MSYS mangles leading-slash both ways (with + without NO_PATHCONV) -> used `behaviors`/`origins` |
| comp-blast | public-data-router | PASS | leaf L@E, no downstream lambda/pipeline consumers -> additive-branch-safe |
| (grep/read) | bd49f_pull.tf, producer code, lambda-source-map | n/a | WS-5 template + I/O grounding (native Read/Grep, on-rail) |

- **What worked:** comp-routes behaviors/origins gave the CF cutover surface (no assets origin, the L@E, the true 75 quota after I cross-checked service-quotas) that drove Option C; comp-blast confirmed the L@E is a safe additive-branch target.
- **What failed:** comp-routes trace unusable on /api/... URLs (MSYS leading-slash mangle in BOTH directions; NO_PATHCONV=1 breaks the tool's own path). Fell back to `behaviors`.
- **Gap found:** the b1 OAC signing test needed raw `aws cloudfront` (create/delete distro+OAC, curl) -- no comp-tool models a CF origin-signing exercise; operational, correctly off-rail. And the "25-behavior LIMIT" assumption (mine, carried into CTO's steer) was a COUNT -- corrected via `aws service-quotas` (L-F432D044=75), the kind of grounding-before-acting that killed an unnecessary quota-increase request.

## Deployment Sequence + Verification (AE) -- the b1 OAC signing test (EXERCISED, zero-residual)
1. `aws cloudfront create-origin-access-control` -> OAC E1L5EJVWCXN0P0 (sigv4/always/s3).
2. `aws s3 cp` test key -> opal-data-assets/json/mdpf/_oac_b1_test.json.
3. `aws cloudfront create-distribution` (opal-data-assets origin via the test OAC) -> distro E31OM0DKGN8S2J.
4. bucket policy: snapshot original (17a-only) -> merge scoped Allow (cloudfront SourceArn=test-distro, GetObject the test key) -> `put-bucket-policy` -> `get-bucket-policy` APPLIED-verify.
5. `aws cloudfront wait distribution-deployed` (bg).
6. POS: `curl` the granted key -> HTTP 200 + body. NEG: `curl` a non-granted key -> HTTP 403 AccessDenied (DISCRIMINATING).
7. TEARDOWN: revert bucket policy (get-bucket-policy = ['DenyParquetUnderBronze17a'] only) + delete key (head-object Not Found) + disable+wait+delete distro (NoSuchDistribution) + delete OAC (NoSuchOriginAccessControl). ZERO residual, no L@E.

## Blockers
None AE-side. MDPF apply gated on A1(aum-metrics)+A2(aum-timeseries) DS producers landing + the CTO+COO+Andrew co-sign (census DONE). WS-5 deploy gated on my window (MDPF precedence) + the 0.6.2 Rule-22a verify pair (egress word GRANTED @64fdd919c; no longer a gate).

## Current State (handoff — zero-context reader)
- **MDPF S5 mechanism = SETTLED, apply HELD.** Option C exact-9 direct behaviors. Design approved by CTO in shape. The 9 keys: 5 json/mdpf/* (global/49f/inflection aggregate-aua-timeseries + 49f/inflection account-distribution) + 4 json/portfolios/* (account-distribution, non_model_assets, aum-metrics, aum-timeseries). Each behavior = a CLONE of the catch-all /api/general/* on distro EVTSA9VEHNZVH (same auth L@E + public-data-router rewrite L@E infra/aws/lambda-edge/public-data-router/index.mjs, only TargetOriginId -> a NEW opal-data-assets OAC origin). + opal-assets bucket-policy: cloudfront GetObject on the 9 EXACT keys, SourceArn=EVTSA9VEHNZVH (b1-proven pattern; disjoint from DenyParquetUnderBronze17a). + publisher (opal-assets-mdpf-portal-publisher) PUBLISH_MAP retarget to the 9 json/hyphen keys. Rollback = remove behaviors -> catch-all resumes portal-v2 (untouched). Concrete diffs NOT yet committed (build near A1/A2 landing per CTO; ~20-30min; can pre-build on the word). Compare/audit docs: docs/briefs/mdpf-revamp-s5-rollover-*.md.
- **APPLY SEQUENCE (held):** commit exact-9 diffs -> CTO gate -> opal-assets bucket-policy + portal-auth origin/OAC apply+VERIFY-live (get-bucket-policy + origin exists) -> C-pre-flight both shapes (scratch /api/general/mdpf/ + /api/general/portfolios/ -> 200 + neg 403 + fail-safe portal-v2) -> DE render-check on exact-9 -> co-sign -> add the 9 behaviors (THE FLIP). Publisher held/manual through cycle-1 (verify-before-serve).
- **WS-5 = DONE + deploy-ready @5d49bd8b1.** infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf: role cot-rebalancer-runner-role (PutObject blackdiamond/cottonwood/{bronze,meta}/*, ListBucket cottonwood/*, GetSecretValue blackdiamond/cot/session READ-ONLY, explicit Deny blackdiamond/49f/*, one_way_fan_in_fence) + daily EventBridge {mode:pull} + yang-lambda module py3.12/512MB/300s (NO layer -- stdlib urllib+boto3). Code: infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/ (WS-1, 0.6.2, CTO-passed @1a6f32b7c). Deploy at my window: build-and-upload.sh opal-assets -> source-map entry -> Rule-22a verify pair -> safe-apply -> tag cot-rebalancer-runner-v0.1.0. TF validate OK.
- **S4 = DONE + live** (mdpf-pipeline-v1.6.0; revamp producer nightly, publisher OFF; cycle-1 = next INF-completion fire, I respond on CTO's S3-verify signal).

## Next Steps
- **[0.7.0_AE_CloudOps]** build+commit the exact-9 MDPF concrete diffs near A1/A2 landing (or now if greenlit); execute the apply sequence on co-sign. Deploy WS-5 at the window (post-MDPF) w/ 0.6.2.
- **[DS]** land A1 (aum-metrics) + A2 (aum-timeseries, reversed to DS-produced) revamp producers -> unblocks the MDPF publisher's 9-key set + the render-check.
- **[0.4.0_DE_ClientPlatform]** render-check on the exact-9 artifacts (incl aum-timeseries) at the flip.
- **[1.0.0_SA_CTO]** gate the exact-9 concrete diffs; run per-cycle S3 re-verify for cycle-1.
- **[0.6.2_AE_PartnerETL]** pair on the WS-5 Rule-22a verify at the deploy window.

## MCP traffic
~40 messages (dense CTO/COO/0.6.2 loop). Significant: CTO S5 STANDBY->Option-A-ruling->A-L@E-gate->venue-A->decompose-(ii)->PROCEED-C->exact-8-confirm->design-pass-APPROVED->Andrew-exact-9-redirect (census DONE); COO greenlight WS-5 (i) + least-privilege-correction + stamp-trigger-ruling + readiness-pulse; 0.6.2 WS-5 spec/re-sync/env-catch/verify; Andrew-direct (via CTO/COO) exact-9 + cot-BD egress word GRANTED @64fdd919c.
