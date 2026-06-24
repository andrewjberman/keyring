# 0.6.0_AE_PartnerETL -- 06-24 session-close (delta since 6849634e2): DC-LEV catalog staging + ULN cutover step-2a
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (ULN cutover skill repoint), COORDINATE (DC-LEV catalog + DS cutover legs + COO movement-checks)

## Window
06-24 ~1426Z-1614Z, since the prior log (6849634e2, which covered startup + D1/D4 spec-complete + the SS4c pair-verify). This is the post-milestone delta + wind-down. D1+D4 were COO-CLOSED in the prior window; this window = the gated-deep DC-LEV staging + fast-follow-1.

## What landed
**DC-LEV catalog staging (COORDINATE, gated-deep prep).** base-AE built+tested the DC0 catalog interface (a849a35c5) with my 3 fields (data_plane / graphql_operation / consumption_status) + aud/scope decode + redacted response-shapes. I supplied the SmartX **consumed-today key set GROUNDED vs the live pull source** (pull_smartx_models_rest.py + pull_smartx_model_monthly_performance.py + smartx_jwt_refresher) -- 6 keys: connect/token, api/3.1 models/{id}, enterprises/aum, reportedmodels/{id}/holdings, models/{id}/performance, performance.smartx/models/performance. Rule-22 catch: corrected my own earlier memory-based "+statistics" over-list (/statistics is NOT consumed = a genuine leverage candidate). The grounded keys ALSO surfaced a real bug in base-AE's spine (literal-path vs templated-path matching -> would have false-positived my parameterized consumed endpoints as leverage candidates); base-AE fixed it (templatePath, e474103cf, 47/47). Path-grain match confirmed sufficient.

**ULN cutover #1 -- BUILD-COMPLETE (IMPLEMENT).** The COO-approved fast-follow, executed in response to a movement-check:
- step-1 (DS): lots_to_silver ULN-schema union-widen (0571c6dcc).
- **step-2a (me, a11331b35): /49-schwab-conv SKILL.md repoint** -- Step-5 convert_schwab_uln_to_silver.py -> convert_schwab_lots_to_silver.py uln (canonical long+short, kills the Rule-17 long-only filter); ADDED the trn_nna Layer-B step (convert_schwab_trn_to_nna_silver.py -> silver/trn_nna/, the gold-consumed C_01.canonical_nna feed = the never-run D1 orphan, runs after trn Layer A); fixed the misleading TRN "(NNA enrichment)" comment; 7-step framing + verify-loop +trn_nna; ULT NOT added (BD-B_03-sourced). Grounded the deploy story first (skill runs converters local-from-repo -> the repoint IS the functional cutover; validates on next manual ingest). Deploy-ledger 20260624T1535Z (my code-leg CLOSED).
- step-2b (DS, ade72da3d): convert_schwab_uln_to_silver.py DEPRECATED (I left the .py to DS = Rule-13 bronze-deploy-cycle + avoid the ds-gate ruff-on-whole-file trap).
- leg-3 (verify): DS-owned, rides the next manual /49-schwab-conv run (B_02 unified uln + canonical_nna source_system flip to {bd,schwab_imputed} + the schwab_imputed materiality number).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| native Grep on the live SmartX pull source | ground the consumed-today key set (Rule-22, not memory) | resolved the 6 grounded keys + the /statistics correction |
No comp-* tool this window. Why: the consumed-today grounding is a source-endpoint enumeration of the live pull code (Grep/Read -- no comp-tool enumerates a script's outbound API calls); the ULN cutover was a SKILL.md (.md) repoint + a change-mgmt ledger (.md), no .py edit / no data/infra change -> no comp trigger (the gold-script _emit edit + the IAM TF are deferred to the SS4c-IAM fresh block, where comp-iam gaps will run).

## MCP traffic
~16 this window (heavy COORDINATE, post-milestone). Significant: base-AE DC-LEV catalog-interface COMPLETE + my grounded consumed-today set (surfaced+fixed the spine path-templating bug); DS ULN cutover step-2b DONE + leg-3-on-next-run; 2 COO movement-checks (attested progressing -> delivered the cutover -> winding-down). DS~B host-vs-compute FYI (folded for the DC-LEV map axis).

## Blockers
None. SS4c-IAM (fresh block) + DC-LEV map (gated on the DC0-catalog/SmartX-vendor-2-crawl) are scoped-next, not blocked. ULN cutover leg-3 is DS-owned on the next ingest.

## Current State (handoff)
- **D1+D4:** spec-complete, CVO-PASS, CTO-accepted, COO-CLOSED (TOs complete). Specs: docs/briefs/DATA_PLATFORM_D1_SCHWAB_FIELD_SPEC.md (7fda2ea32) + _D4_SMARTX_ENDPOINT_SWEEP.md (6d7d30ba0); CTO canonicalizing briefs->architecture.
- **ULN cutover:** BUILD-COMPLETE (0571c6dcc + a11331b35 + ade72da3d). /49-schwab-conv now runs lots_to_silver uln + the trn_nna Layer-B. Leg-3 verify = next manual /49-schwab-conv run (DS RAVC2s). Ledger 20260624T1535Z.
- **DC-LEV:** catalog interface live + correct (a849a35c5 + e474103cf); my 6 consumed-today keys wired; map builds off base-AE's catalog when the crawl reaches SmartX vendor-2 (post-Orion, gated on COO's DC0 TO + CTO arch-gate). Host-vs-compute axis (DS~B) for the map.
- **SS4c:** cutover verified clean (DELTA=0). Open: the weekly cw-metric-IAM gap (bd-exporter-ec2-role lacks cw:PutMetricData) + the egress-inert SNS -- both non-urgent (07-01), the IAM fix is fast-follow-2.

## Next Steps
1. [0.6.0_AE_PartnerETL] SS4c IAM fast-follow (FRESH block, deploy-ledger): ns-conditioned cloudwatch:PutMetricData (GLDINC/SS4c) on bd-exporter-ec2-role via BD-pipeline TF (mirror canary role) + the gldinc_ss4c_weekly.py _emit-non-fatal hardening (gold-deploy-cycle). Before 07-01. comp-iam gaps after the iam.tf change.
2. [0.6.0_AE_PartnerETL] DC-LEV capability-leverage map -- off base-AE's per-vendor catalog when the SmartX vendor-2 crawl lands (host-vs-compute axis).
3. [0.4.0_DS_ClientPlatform] ULN cutover leg-3 co-verify on the next /49-schwab-conv run -> RAVC2.
4. [2.0.0_SA_COO] DC0 harness TO (Orion-first) -> unblocks the SmartX crawl.
</content>
