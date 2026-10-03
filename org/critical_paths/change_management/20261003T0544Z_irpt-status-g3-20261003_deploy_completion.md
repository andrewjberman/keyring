# Deploy Completion Record
**Date opened:** 2026-10-03T05:44:26.729393+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T065600Z
**Deploy:** G3 (CTO batch 175): irpt-status gains the render-grant ports -- the grant read (I1), then the code and IRPT_EVIDENCE_BUCKET (D1)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip with grant.py + report_owner.py from an autocrlf=false checkout | read back by version; members equal git; census vs live 6VQejBfs; cold-start smoke with the bucket set | s3 version In5BnMbPSWafGWf16g4CasBPJRhM.Ykl, 347090 bytes, read back by version with sha256 hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E= equal to the build; autocrlf=false checkout at b6bce5866a (repin 899b9cad63, files 9b3e128a3b); census vs live 6VQejBfs: 46 identical, 1 changed, 2 added, 0 differ from the pin, 0 CRLF; cold-start smoke with IRPT_EVIDENCE_BUCKET set PASS on 4 routes; render ports install from the zip, None without the bucket (G3_STATUS/) | CLOSED 20261003T061054Z |
| I1 | activation | ONE targeted safe-apply of aws_iam_role_policy.irpt_status_render_grant_read (ops root) | policy read back; GetObject only on render_grant.json, ListBucket bounded | CTO half batch 212 (msg 104561) on blob 85eb94e84c; before-read 06:19:54Z (6VQejBfs, no bucket var, key In5BnMbP, no render-grant policy); re-plan 1 to add; safe-apply rc=0; irpt-status-render-grant-read-policy read back: ReadOnlyRenderGrants GetObject on firms/*/generations/exr_*/render_grant.json; ListOnlyRenderGrantShapes ListBucket with s3:prefix that shape (G3_STATUS/I1_READBACK_20261003.txt) | CLOSED 20261003T062540Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (code + IRPT_EVIDENCE_BUCKET) | CodeSha256 and env read back; live empty-headers invoke | re-plan code + IRPT_EVIDENCE_BUCKET (core output), 1 to change; safe-apply rc=0; CodeSha256 hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E= Successful 06:28:49Z; env names gain IRPT_EVIDENCE_BUCKET; live empty-headers invoke 200, no FunctionError, CONTRACT_VERSION; V1 arm 1: 18 of 18 non-render reads equal to the before-read (G3_STATUS/READS_AFTER_G3_*) | CLOSED 20261003T063123Z |
| V1 | verify | every non-render read equal to live; a foreign render token refused; the positive arm rides E4's first Analysis export | reads recorded | arm 1: 18 of 18 non-render reads equal to the before-read (G3_STATUS/READS_AFTER_G3_*); arm 2 CLOSED by CTO batch 217 (msg 104576): 2.0.0_SA_COO~P's foreign render token refused live upstream (sections 403 authorizer, status 401 edge; IRPT_MVP_P/G3_V1_NEGATIVE_ARM_20261003.md) plus _authz/tests/test_render_delegate_pins.py:73 and :98 at the pin (45 passed); arm 3 (the live wiring, a RENDER_DELEGATE read of a real Analysis export) is E4's per batch 217, carried by E4's own ledger | CLOSED 20261003T065600Z |

## Log

- 20261003T054426Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261003T061054Z LEG U1 closed: s3 version In5BnMbPSWafGWf16g4CasBPJRhM.Ykl, 347090 bytes, read back by version with sha256 hC6PramtsshP40jo3OJ91k4qxlHn
- 20261003T062540Z LEG I1 closed: CTO half batch 212 (msg 104561) on blob 85eb94e84c; before-read 06:19:54Z (6VQejBfs, no bucket var, key In5BnMbP, no ren
- 20261003T063123Z LEG D1 closed: re-plan code + IRPT_EVIDENCE_BUCKET (core output), 1 to change; safe-apply rc=0; CodeSha256 hC6PramtsshP40jo3OJ91k4qxlHn
- 20261003T065600Z LEG V1 closed: arm 1: 18 of 18 non-render reads equal to the before-read (G3_STATUS/READS_AFTER_G3_*); arm 2 CLOSED by CTO batch 217 (m
- 20261003T065600Z CLOSED -- all 4 legs proven
