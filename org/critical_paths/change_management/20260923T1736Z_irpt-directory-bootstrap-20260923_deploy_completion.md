# Deploy Completion Record
**Date opened:** 2026-09-23T17:36:36.188585+00:00
**Status:** OPEN
**Deploy:** IRPT exact directory bootstrap staging and gated serving under CTO18e2835c5f
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | Exact existing S3 directory artifact staging | Immutable downloaded version equals a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b | Canonical single-function build-and-upload PASS; immutable version 1ogxCxUa61vTvMPtXB.BehRWB7aJTCnj independently downloaded 155747 bytes SHA256 a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b; source-map changes only directory artifact_sha256. CTO18e2835 exact staging boundary. No serving apply. | CLOSED 20260923T173827Z |
| P1 | verify | Saved directory-only Terraform plan | Plan hash JSON and CTO exact apply adjudication |  | OPEN |
| V1 | verify | Post-apply directory runtime | Code hash config role route equality targeted zero diff and canonical scoped recorder |  | OPEN |
| B1 | verify | Paired signed-in first hop | Real bootstrap list selection reload outcome without S1-S7 overclaim |  | OPEN |
| irpt-directory-search | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260923T173636Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260923T173827Z LEG S1 closed: Canonical single-function build-and-upload PASS; immutable version 1ogxCxUa61vTvMPtXB.BehRWB7aJTCnj independently downlo
