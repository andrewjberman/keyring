# Deploy Completion Record
**Date opened:** 2026-09-23T17:36:36.188585+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T182044Z
**Deploy:** IRPT exact directory bootstrap staging and gated serving under CTO18e2835c5f
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | Exact existing S3 directory artifact staging | Immutable downloaded version equals a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b | Canonical single-function build-and-upload PASS; immutable version 1ogxCxUa61vTvMPtXB.BehRWB7aJTCnj independently downloaded 155747 bytes SHA256 a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b; source-map changes only directory artifact_sha256. CTO18e2835 exact staging boundary. No serving apply. | CLOSED 20260923T173827Z |
| P1 | verify | Saved directory-only Terraform plan | Plan hash JSON and CTO exact apply adjudication | CTO e186d7ea22 independently verified exact saved plan c5ef7ef7357ad194bdc38dabd827dd170cc5544e923fd573cb9436c0d40348ca and authorized only its apply. Canonical safe-apply succeeded0add1change0destroy; no regenerated-plan authorization. | CLOSED 20260923T175124Z |
| V1 | verify | Post-apply directory runtime | Code hash config role route equality targeted zero diff and canonical scoped recorder | SUPERSEDED 2026-09-24T18:2xZ by 2.0.0_SA_COO~P (crash-recovery C1, CTO 100730): the artifact this leg verifies (CodeSha256 o590uh5o) no longer runs. irpt-directory-search was replaced at 2026-09-24T05:16:11Z by o9Qu0Jm7 under ledger irpt-directory-keepwarm-rule-20260924, CLOSED 05:25:14Z, whose V1 (0-diff re-plan) and R1 (recorder d79dac8675) cover the successor. Live read 18:2xZ: list-functions CodeSha256 o9Qu0Jm7jidtrlBeGWD9d2ZsxROK3NXcQTEOUOMvGus= LastModified 05:16:11Z. | CLOSED 20260924T182043Z |
| B1 | verify | Paired signed-in first hop | Real bootstrap list selection reload outcome without S1-S7 overclaim | SUPERSEDED as a deploy leg by 2.0.0_SA_COO~P (C1, CTO 100730): the signed-in bootstrap-list-selection-reload hop is a JOURNEY outcome, not a completion of this deploy. Its artifact was replaced (see V1). The hop is carried by the goal record ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md (COT journey on Anna's plan, CRO return brief s.7), graded on the live function o9Qu0Jm7. | CLOSED 20260924T182044Z |
| irpt-directory-search | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | Exact saved-plan safe-apply e186d7ea22 completed. Active/Successful; live independent downloadedZIP155747bytes a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b; CodeSha256 o590uh5oisCtHPKzorGMJ/k9VJPcgtLSg4SKfe4KYYs=; RevisionId8522ea10-8d47-484c-aa00-7b57d255983b. Target post-apply plan zero changes. No config/environment/role/policy/routes change. Canonical recorder incomplete/widened; V1 stays open. | CLOSED 20260923T175124Z |

## Log

- 20260923T173636Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260923T173827Z LEG S1 closed: Canonical single-function build-and-upload PASS; immutable version 1ogxCxUa61vTvMPtXB.BehRWB7aJTCnj independently downlo
- 20260923T175124Z LEG P1 closed: CTO e186d7ea22 independently verified exact saved plan c5ef7ef7357ad194bdc38dabd827dd170cc5544e923fd573cb9436c0d40348ca 
- 20260923T175124Z LEG irpt-directory-search closed: Exact saved-plan safe-apply e186d7ea22 completed. Active/Successful; live independent downloadedZIP155747bytes a39f74ba1
- 20260924T182043Z LEG V1 closed: SUPERSEDED 2026-09-24T18:2xZ by 2.0.0_SA_COO~P (crash-recovery C1, CTO 100730): the artifact this leg verifies (CodeSha2
- 20260924T182044Z LEG B1 closed: SUPERSEDED as a deploy leg by 2.0.0_SA_COO~P (C1, CTO 100730): the signed-in bootstrap-list-selection-reload hop is a JO
- 20260924T182044Z CLOSED -- all 5 legs proven
