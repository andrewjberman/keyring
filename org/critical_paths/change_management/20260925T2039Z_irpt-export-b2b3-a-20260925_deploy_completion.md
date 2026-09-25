# Deploy Completion Record
**Date opened:** 2026-09-25T20:39:27.714881+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T204458Z
**Deploy:** Export B2/B3 deploy (A): irpt-render-deps layer + irpt-export-render with B2/B3 code, render switch OFF + render-host scripts + export root IAM (token carriage, pending.json) -- publish ee90f9912b, export root 6c5cd9a288
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-layers/irpt-render-deps-layer.zip | put + head: content-sha256 of the 04624dab.. build | s3://opal-313476888478-lambda-layers/irpt-render-deps-layer.zip put 663509 bytes, version tejYymyzChB4SO.L3dG6sjb35gGfV7g., content-sha256 metadata BGJNq5c0dnAD/DpK7exFFXiJB2YXTI5Yq7Jm+n8N3Jo=; read-back sha256 04624dab9734.. == the built zip | CLOSED 20260925T204044Z |
| H1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/{render_export.cjs,run-export-render.sh} | put + read-back sha256 equal to backend 266741ad88 | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs (16401 B, sha ce2928295a48..) and run-export-render.sh (1840 B, sha 3662e160353b..) put from git show 266741ad88 and read back byte-equal | CLOSED 20260925T204045Z |
| A1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | build-and-upload VERIFIED line of the ee90f9912b build | build-and-upload irpt-export-render from publish ee90f9912b (42 staged rows pinned 83e8b9577a, sha-verified): irpt-export-render.zip write VERIFIED size=351647, content-sha256 ryEMGlRuOmI3wq+5kPNVYEBgRxbQMLkI2JW2+iIizjo= | CLOSED 20260925T204146Z |
| A2 | activation | export root apply | layer version created and attached; CodeSha256 == uploaded; IRPT_EXPORT_RENDER=off; new policies present; SSM document default version carries RenderTokenName/PrintQuery | safe-apply 3 added / 3 changed / 0 destroyed. Live irpt-export-render CodeSha256 ryEMGlRu.. == uploaded, Active/Successful; layers irpt-common:5 + irpt-render-deps-layer:1; IRPT_EXPORT_RENDER=off, IRPT_RENDER_PRIVATE_KEY_SECRET=opal/auth/irpt-render-jwt-private-key; export role 8 policies incl. irpt-export-render-token-carriage-policy; irpt-ycharts-runner-role has irpt-export-render-host-token-policy; SSM irpt-export-render-run default version 5 with RenderTokenName + PrintQuery. | CLOSED 20260925T204431Z |
| N1 | verify | negative arm before and after | ungranted advisor NOT_AUTHORIZED; internal submit of a nonexistent report OBJECT_NOT_COVERED; internal receipt of a nonexistent export NOT_FOUND; 0 objects under generations/exr_* and 0 names under /irpt/render-token/ | Same direct-invoke probes before (1oJDhe..) and after (ryEMGl..): internal submit of a nonexistent report OBJECT_NOT_COVERED both; ungranted advisor NOT_AUTHORIZED both; internal receipt of a nonexistent export NOT_FOUND both (B3's pointer read finds none -> unchanged answer); no data key; 0 objects under generations/exr_* at 3 firms; 0 names under /irpt/render-token/ (switch off: nothing minted). | CLOSED 20260925T204431Z |
| V1 | verify | export root re-plan | No changes | export root re-plan after apply (-detailed-exitcode rc=0): No changes. | CLOSED 20260925T204458Z |

## Log

- 20260925T203927Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260925T204044Z LEG L1 closed: s3://opal-313476888478-lambda-layers/irpt-render-deps-layer.zip put 663509 bytes, version tejYymyzChB4SO.L3dG6sjb35gGfV7
- 20260925T204045Z LEG H1 closed: s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs (16401 B, sha ce2928295a48..) an
- 20260925T204146Z LEG A1 closed: build-and-upload irpt-export-render from publish ee90f9912b (42 staged rows pinned 83e8b9577a, sha-verified): irpt-expor
- 20260925T204431Z LEG A2 closed: safe-apply 3 added / 3 changed / 0 destroyed. Live irpt-export-render CodeSha256 ryEMGlRu.. == uploaded, Active/Successf
- 20260925T204431Z LEG N1 closed: Same direct-invoke probes before (1oJDhe..) and after (ryEMGl..): internal submit of a nonexistent report OBJECT_NOT_COV
- 20260925T204458Z LEG V1 closed: export root re-plan after apply (-detailed-exitcode rc=0): No changes.
- 20260925T204458Z CLOSED -- all 6 legs proven
