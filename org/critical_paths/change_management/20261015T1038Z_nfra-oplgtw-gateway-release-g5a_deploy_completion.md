# Deploy Completion Record
**Date opened:** 2026-10-15T10:38:12.579471+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-20 Phase B: the five G5 wave A etfs tools, mdpf_get_category_views and their one ETF read grant -- release 06cfb6db6471972c7304cd3d7a5b93e6f521ad72 onto live base 1b18b94979d2ba0e4c6eba8ee4a0a5a0cae52bc0, all three halves signed (CTO d53b7dbba1, COO 4ffb7a40c0, CVO d463859c97), GO msg 34417
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | the ONE IAM policy gateway-global-etfs-read-policy applied to gateway-global-internal-reader-role through safe-apply targeted, grant BEFORE deploy per all three halves | proof: get-role-policy read-back -- 2 statements, 9 s3:GetObject resources, ListBucket confined by s3:prefix to 7 directory prefixes, no Put, no Delete, no wildcard |  | OPEN |
| L2 | ec2-baked-asset | the release deployed from C:/tmp/og-rel-g5a through infra/aws/ec2/safe-ec2-deploy.sh with DEPLOY_BASE_REF=1b18b94979d2ba0e4c6eba8ee4a0a5a0cae52bc0, no HALT_OVERRIDE | proof: SSM md5 of the RUNNING path equal to the release blobs across app, deploy and lib |  | OPEN |
| L3 | verify | the served read of all six tools through the INSTALLED code and through the public endpoint (CVO condition 1), with etfs_get_ownership_rollup proving the single-object ARN platinum/etf_ownership_dashboard.json (CVO condition 2) | proof: W/G5A_SERVED.json -- registry_before 69 to registry_count 75, per-tool 6 of 6 opal_served and non_opal_refused with reads_on_refusal 0, policies_live true |  | OPEN |
| L4 | git | the standing release clauses: runbook 7.2 names the new live release, EC2_MANIFEST deployed_commit and file_checksums taken from the release blobs | proof: the commit hash carrying both |  | OPEN |
| L5 | verify | ap20.AC2 graded on the repaired check script | proof: RESULT PASS with exit 0 |  | OPEN |

## Log

- 20261015T103812Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
