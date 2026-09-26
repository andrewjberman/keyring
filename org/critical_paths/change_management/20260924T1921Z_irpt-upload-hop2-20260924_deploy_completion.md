# Deploy Completion Record
**Date opened:** 2026-09-24T19:21:19.302731+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T140707Z
**Deploy:** IRPT Analysis upload hops 2+3: ycharts-root grants, resident package with RESOLVE_UPLOAD, irpt-ycharts-generate rebuild (Y bb1eb7f92b/10a16bd89d/d16b7c8743, P a58859baa7 + 19b38e2f22)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | activation | ycharts root: aws_iam_role_policy.generate + runner_resident | safe-apply of the saved plan 0/2/0; 0-diff replan | safe-apply (HALT_ACK=1, terraform 1.9.8, backend worktree ycharts root) of the saved plan 0 add / 2 change / 0 destroy at 19:22Z: aws_iam_role_policy.generate + Sid RetainOriginalHoldingsUploadsOnly (s3 Put/Get/GetVersion on opal-data-irpt/irpt/{49financial,cottonwood,inflection}/state/original_holdings/*); aws_iam_role_policy.runner_resident write families + NORMALIZED_PORTFOLIO, read families REQUEST_COMPOSITION + ORIGINAL_HOLDINGS, KMS StringLike lists follow; prefixes derived from infra/logic/registry/reporting_policies.json (CLOUD blob 925fbbdc08, M's ACTIVE registry); re-plan -detailed-exitcode rc=0 No changes 19:22Z | CLOSED 20260924T192301Z |
| R1 | activation | resident package on i-0167fd745ad906a66 carrying resident_worker resolve_upload | SSM install rc 0; unit active; IRPT_RESIDENT_POLL lines; manifest sha | package f624e8a72f built from committed blobs (build_resident_package.py, 225 members + SHA256SUMS; local import closure 12 of 12, X10 ACTIVE, bindings load); tar sha256 6651fd476458811e.. 720119 bytes at s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-ycharts/resident/irpt-resident-f624e8a72f.tar.gz version bNyb3H6sl49OWwZCLQFTAJEleaX0Jx8o; SSM 10cde8d4 Success rc 0: factory dry run as ec2-user OK (enrolled 1276035, queue irpt-generation) BEFORE the unit moved, install-resident.sh rc 0, host manifest eb37b38b525b9ce3.. (3652 members with pydeps), unit irpt-analysis-resident.service active MainPID 62369 NRestarts 0 since 19:43:01Z on /opt/irpt-resident/f624e8a72f, IRPT_RESIDENT_POLL handled=0 at 19:43:22Z and 19:43:42Z, no traceback; rollback root /opt/irpt-resident/ab2e088b5b retained | CLOSED 20260924T194420Z |
| L1 | activation | irpt-ycharts-generate artifact + apply | census vs deployed; safe-apply; readback CodeSha256; 0-diff replan; recorder | source map 501b2f83e5 on irpt-p-publish-20260923 (backend head f624e8a72f merged at c0c05628cc; six rows re-pinned + upload_resolution.py); artifact LdjdnnLh5Rqff4VV/tWXS7HY/xKU05+i2uV5gpTIw8Y= 518785 bytes, S3 version .tgaCjYf50HE4wnf3qhxAA5w1lXSK.4f; census vs deployed 4fkloyC1: 106 -> 107 (+upload_resolution.py), exactly custody_portfolio/errors/generate_installed/maintained_sources/resident_worker/served/uploads differ; import-closure 56/56; plan 0/1/0 (source_code_hash + s3_object_version only); safe-apply 19:49:52Z; readback Active/Successful handler generate_installed.lambda_handler; replan rc=0 No changes; invoke {} -> 200 named CONTRACT_VERSION refusal, cold start clean; recorder 174e39b4ad | CLOSED 20260924T195122Z |
| S1 | verify | live upload acceptance | Andrew posts the 12.03 template: RESOLVING, one IRPT_RESIDENT_POLL handled=1, NORMALIZED with total_dollars 12.03 | 2026-09-26 live acceptance by 2.0.0_SA_COO~Y as the bounded admin+Dev walk principal (packet v3 07b7a000, K4): ONE POST /analysis/inputs 13:54:56Z of aapl-vnq-12.03.csv (AAPL 10.01 / VNQ 2.02, USD) -> RESOLVING; resident IRPT_RESIDENT_POLL handled=1 at 13:55:02Z (one securities_info GET, CTO 100667(1)); NORMALIZED 12.03. Keys: IRPT_MVP_Y/LIVE_UPLOAD_1203_EVIDENCE_20260926.md @3cc73f2b79; scrubbed log LIVE_UPLOAD_1203_20260926_RUN2.json. Served generate IJD6bd1I (ledger irpt-generate-closure-fix-20260926). | CLOSED 20260926T140707Z |

## Log

- 20260924T192119Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260924T192301Z LEG G1 closed: safe-apply (HALT_ACK=1, terraform 1.9.8, backend worktree ycharts root) of the saved plan 0 add / 2 change / 0 destroy a
- 20260924T194420Z LEG R1 closed: package f624e8a72f built from committed blobs (build_resident_package.py, 225 members + SHA256SUMS; local import closure
- 20260924T195122Z LEG L1 closed: source map 501b2f83e5 on irpt-p-publish-20260923 (backend head f624e8a72f merged at c0c05628cc; six rows re-pinned + upl
- 20260926T140707Z LEG S1 closed: 2026-09-26 live acceptance by 2.0.0_SA_COO~Y as the bounded admin+Dev walk principal (packet v3 07b7a000, K4): ONE POST 
- 20260926T140707Z CLOSED -- all 4 legs proven
