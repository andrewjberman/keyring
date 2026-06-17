# PMTRDX.001 financial deploy (COMPLETE, all 3 legs LIVE-verified) + D8-FP AC2 RAVC1 + SS4c sign-off + deploy-tooling APPROVE

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE, IMPLEMENT

**Agent:** 0.7.0_AE_CloudOps (base) · **Date:** 2026-06-17 · **Window:** ~1438Z -> ~1620Z (since cold_start log b393e594a)

## Summary
Executed + CLOSED **PMTRDX.001** -- an URGENT Andrew-direct trade-weight unit fix on a LIVE financial path -- end-to-end with full gating + live egress-verification. Caught a 100x-broker flaw in the dispatch brief (DE's all-fraction PATCH2 would send a 100x-wrong weight to Vident), corrected to a per-output conversion, built a BINDING empirical byte-identical broker proof, held each leg for its gate (CTO financial co-sign + Andrew EXPLICIT clear on the live-record write), and egress-verified all 3 legs on live state. Also: authored the **D8-FP AC2 RAVC1 design** (CTO conditional sign-off + COO concur, C2/C3 resolved), gave the **SS4c** binding cost-safety sign-off, and APPROVED the **CTO deploy-tooling** pass.

## PMTRDX.001 -- trade-weight unit fix (COMPLETE)
Bug: PM-export trade submissions stored weights as percent-numbers; portal (x100-display) rendered 555% vs 5.55%. The 06-03 producer fix (canonical=FRACTION, CTO fa9dc3cb3) never shipped.
- **CTO correction grounded:** DE's brief PATCH2 (all-fraction) would 100x-break the broker -- Vident ingests the RAW cell value, and workflow-handler generate_vident_excel (workflow_handler.py:392 -> send_brokerage_email -> email_utils:420) is broker-facing + reads the now-fraction record. Confirmed in code; owned my earlier verify gap (I'd called the trade excel-gens download-only).
- **Fix (c48ca8423):** PATCH1 producer build_trade_securities ÷100 + weight_unit='fraction' (record/portal=fraction, Vident funcs untouched); PATCH2 both excel-gens *100-on-read (DE recipe -- keeps broker output byte-identical, the existing col5/col7 /100 cancels) + pre-existing F401/bare-except cleanup.
- **Binding empirical gate (4a4360909):** patched-code+fraction-record vs pre-patch-code(c48ca8423^)+percent-record, diffed every cell -- 47 cells, 0 diffs, col-6 raw stays 5.05 (NOT 0.0505). COO VALIDATED PASS.
- **Deploy (Terraform-only, NOT the banned deploy.sh):** 3 source-only zips -> s3 cp to lambda-artifacts (content-sha256 metadata, versioned) -> safe-apply per module from saved plans (portfolio-management 0/1/0 + trade-pipeline 0/2/0, repoint-ONLY, 0 other drift). Egress-verified: all 3 deployed CodeSha256 == new zip shas. source-map synced (d38fda377).
- **PATCH3 remediation (both gates: CTO co-sign + Andrew EXPLICIT):** --apply on the 2 reviewed records; LIVE-DDB post-verify both weight_unit=fraction + ÷100'd (AMZN TRADE-20260617-144856 0.0555/0.0505/-0.005; AMD TRADE-20260602-135824 0.0212/0.0175/-0.0037), PENDING_APPROVAL preserved.
- **Ledger (596b4afd4):** deploy-completion pmtrdx-001-weight-unit opened 3-leg -> all 3 closed -> check --red nothing-half-landed. final-RAVC2 COO-ACCEPTED. PMTRDX.001 CLOSED.

## D8-FP AC2 RAVC1 (design GO'd, resuming implementation)
RAVC1 design doc (7e137b481): Option-A per-surface AWS-backend MEMBERSHIP (producer-identity-anchored, per-firm) replacing the portal-keyed file_path matching. Caught that a naive AWS-scope re-sign BLINDS the scan (AWS nodes file_path="full-derive", surfaces portal-keyed -> 0 findings) -- held it, CTO ruled Option A. CTO conditional sign-off: +2 AC3 category rows (serving-Lambda opal-portal-data-proxy + served-bucket opal-data-inf); C2 getAUMMetrics = portal-endpoint (division to B5 hook, not gap); C3 cot-ADVI = documented no-op. COO concur. RESUMING the implementation (deploy window clear).

## SS4c + deploy-tooling
- **ADHC_GLDINC.SS4c** (co-assignee, BINDING): PRELIMINARY design GO -- piggyback append CONFIRMED (no manufactured run), weekday=Wed (stagger anchor), §7 ~$2-6/mo marginal (true-up on first actual run); conditions: guard-envelope register + Wed-gate + validate-on-actuals. Held to peer's TF RAVC1.
- **CTO deploy-tooling review:** APPROVE both (safe-destroy.sh + deploy_ledger --red), 0 blockers; verified CM_DIR/re/entry_path/py_compile. Landing pref = CTO author line.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-kuzu | D8-FP carve: producer membership per surface/firm (benchmark/peers/aum/ADVI bd+inf+cot writers, instance->profile->role) | PASS | provenance=current; surfaced bucket-grain too coarse (portal-v2 ~38 writers, portfolio 21) -> producer-identity anchoring |
| safe-apply.sh | portfolio-management + trade-pipeline (PMTRDX, saved plans) | PASS | HALTGT cleared; repoint-only applies, 0 other drift |
| ds-commit-gate.sh | 3 PMTRDX Lambda files (x2 -- F401 fix) + proof deliverable | PASS | caught pre-existing F401 + E402; cleaned |
| deploy_ledger.py | open/close-leg x3/close/check --red (pmtrdx-001-weight-unit) | PASS | 3-leg opened at deploy-start, all closed, --red clean |
| aws (cli) | lambda get-function-configuration (CodeSha256 egress-verify x3), dynamodb get-item (live-DDB verify x2), s3 cp/head-object, terraform plan | PASS | every leg egress-verified on live state, not rc |
| comp-iam | NOT run | n/a | PMTRDX code-only, no iam.tf change; the repoint-only plans confirmed 0 IAM drift |

**What worked:** the empirical byte-identical proof (not by-construction) caught/eliminated the 100x-broker risk; egress-verifying every leg on live state (CodeSha256 + live-DDB) instead of rc=0; gating the financial-record --apply on Andrew-EXPLICIT (not assumed). **What failed:** nothing landed wrong. **Gap found:** the banned deploy.sh (aws lambda update-function-code + pip install -t . inline deps + emojis -- Rules 1/3/ASCII) -- footgun vs TF-managed state; filed for cleanup (task #9, COO low-pri).

## Deployment Sequence + Verification (AE)
```
PMTRDX.001 (Terraform-only S3-artifact repoint):
  zips (source-only, deps in openpyxl-layer:3): portfolio-excel-gen 6233B, workflow-handler 17376B, dashboard-api 8481B
  s3 cp -> opal-313476888478-lambda-artifacts (content-sha256 metadata, new versions)
  safe-apply portfolio-management (saved plan, 0/1/0) -> opal-portfolio-excel-generator CodeSha256=3KhyVvll.. (LM 15:55:13Z)
  safe-apply trade-pipeline   (saved plan, 0/2/0) -> trade-workflow-handler jKU+Mk.. + trade-dashboard-api CLpMor.. (LM 15:55:57Z)
  EGRESS-VERIFY: 3/3 deployed CodeSha256 == new zip shas. PASS.
  PATCH3 --apply: 2 records remediated; LIVE-DDB re-pull -> weight_unit=fraction + ÷100'd values confirmed.
  ledger pmtrdx-001-weight-unit: 3/3 legs CLOSED (596b4afd4); check --red = nothing half-landed.
```

## Blockers
None. PMTRDX.001 CLOSED. D8-FP AC2 implementation GO'd (deploy window clear). GCONTR TO-3 load gated on CVO (planned). SS4c held to peer's TF RAVC1 (planned). deploy-tooling awaiting CTO landing (planned).

## Current State
- PMTRDX.001 COMPLETE: producer fraction-canonical going-forward (weight_unit='fraction' stamped); broker Vident byte-identical (unaffected); 2 live PENDING_APPROVAL records remediated; portal renders 5.55% not 555%. Deployed Lambdas: opal-portfolio-excel-generator (3KhyVvll), trade-workflow-handler (jKU+Mk), trade-dashboard-api (CLpMor). source-map synced.
- D8-FP AC2: RAVC1 design committed (7e137b481, deliverable NFRA_GRAPHS.D8-FP.ravc1-design.md); CTO conditional sign-off + COO concur; resuming the in-derive scan membership re-implementation (critical-surfaces.yaml aws_backend + derive_runner run_critical_surface_scan + re-sign + AC3 egress + AC4). Interim KNOWN-FP ledger (79d999355) covers the 06-17 02:00Z SEV1/SEV2.
- Deliberate queue (COO sequence behind D8-FP + GCONTR TO-3): volatility-fetcher adjudication + source-map fix, OIDC deploy-role hardening, COSTAWS, deploy.sh cleanup.

## Next Steps
- [0.7.0_AE_CloudOps] RESUME D8-FP AC2: encode per-surface aws_backend membership -> scan-matching change -> rebuild (S3-ZIP re-zip) -> re-sign -> AC3 (5+2 rows) -> AC4 -> RAVC2 to [2.0.0_SA_COO] CC [1.0.0_SA_CTO].
- [3.0.0_SA_CVO] GCONTR TO-3: author NNA SEV1 row (canonical_writer=bd-exporter-ec2-role) + upload YAML -> ping me for GO-time --load-contracts (folds the §3 loader hardening).
- [0.6.0_AE_PartnerETL] SS4c TF RAVC1 -> I re-confirm the 3 binding conditions (guard-envelope + Wed-gate + validate-on-actuals).
- [1.0.0_SA_CTO] land the deploy-tooling pass (safe-destroy.sh git add -f + deploy_ledger.py) under CTO author line.
