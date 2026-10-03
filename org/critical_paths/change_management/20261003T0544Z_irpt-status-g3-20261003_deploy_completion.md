# Deploy Completion Record
**Date opened:** 2026-10-03T05:44:26.729393+00:00
**Status:** OPEN
**Deploy:** G3 (CTO batch 175): irpt-status gains the render-grant ports -- the grant read (I1), then the code and IRPT_EVIDENCE_BUCKET (D1)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip with grant.py + report_owner.py from an autocrlf=false checkout | read back by version; members equal git; census vs live 6VQejBfs; cold-start smoke with the bucket set | s3 version In5BnMbPSWafGWf16g4CasBPJRhM.Ykl, 347090 bytes, read back by version with sha256 hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E= equal to the build; autocrlf=false checkout at b6bce5866a (repin 899b9cad63, files 9b3e128a3b); census vs live 6VQejBfs: 46 identical, 1 changed, 2 added, 0 differ from the pin, 0 CRLF; cold-start smoke with IRPT_EVIDENCE_BUCKET set PASS on 4 routes; render ports install from the zip, None without the bucket (G3_STATUS/) | CLOSED 20261003T061054Z |
| I1 | activation | ONE targeted safe-apply of aws_iam_role_policy.irpt_status_render_grant_read (ops root) | policy read back; GetObject only on render_grant.json, ListBucket bounded |  | OPEN |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (code + IRPT_EVIDENCE_BUCKET) | CodeSha256 and env read back; live empty-headers invoke |  | OPEN |
| V1 | verify | every non-render read equal to live; a foreign render token refused; the positive arm rides E4's first Analysis export | reads recorded |  | OPEN |

## Log

- 20261003T054426Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261003T061054Z LEG U1 closed: s3 version In5BnMbPSWafGWf16g4CasBPJRhM.Ykl, 347090 bytes, read back by version with sha256 hC6PramtsshP40jo3OJ91k4qxlHn
