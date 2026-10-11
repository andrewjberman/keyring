# Deploy Completion Record
**Date opened:** 2026-10-11T11:41:30.692435+00:00
**Status:** OPEN
**Deploy:** OG-ap-6 B2 step 7: the E2 .xlsx gateway release (copy_site_file_to_s3 -> bronze fee_statement) deployed from the re-cut release worktree
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the re-cut release exists at release_sha with all three halves re-pinned to it | release_sha 6aadf7db37a8605389110e08bb64f6e15e1d3026 on rel-nfra-oplgtw-r16c; re-pins CTO b2bb4caabf, COO 3d5fc13ecf, CVO b8b7ab0f11 |  | OPEN |
| L2 | activation | infra\aws\ec2\safe-ec2-deploy.sh run FROM C;C:\Users\OPALBL~1\AppData\Local\Temp\og-rel16c with DEPLOY_BASE_REF=2a5966dfbd89be9fe6cc0ef3566831e502b81d42, no HALT_OVERRIDE | the deploy returns success and the service restarts |  | OPEN |
| L3 | verify | ap6_verify.py after, run IMMEDIATELY, against the before-state read at the act | all checks PASS: /health 200 and active; every listed shipped file identical to the re-cut release; exactly copy_site_file_to_s3 added and none removed; exactly ADVI_FEE_STATEMENT_S3_ROOT added and none removed; no other .env value digest moved; dashboard/ unchanged including all four orphans |  | OPEN |
| L4 | git | EC2_MANIFEST.json opal-gateway deployed_commit recorded by hand as the release_sha | the commit carrying the manifest edit |  | OPEN |
| L5 | verify | ap6.AC2 | both ledgers CLOSED with sentinels gone and the host running the re-cut release -- RESULT PASS at rc=0 |  | OPEN |

## Log

- 20261011T114130Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
