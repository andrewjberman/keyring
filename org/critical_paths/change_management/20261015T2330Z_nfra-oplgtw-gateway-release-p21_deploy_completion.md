# Deploy Completion Record
**Date opened:** 2026-10-15T23:30:52.056858+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-21 Phase B: the person reader, the news and invoke role moves and harvest_get_published_analysis -- release d577e0e7297b3ecba183023d8374855a93f148a7 onto live base c4c106aea1cc47d15f81397208226bd9b292c9dc, all three halves signed (CTO 378438988e, COO c9c5cb0e07, CVO bee4c81023) against ask sha256 862a1de9a7c6, GO msg 34606
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| news-policy | activation | gateway-global-news-read-internal-policy ADDED on the assumed internal reader role, applied ALONE through safe-apply targeted | proof: get-role-policy read-back -- 1 statement, dynamodb:Query and GetItem only, 4 resources (3 tables + 1 date-index), no Scan, no write, no wildcard; and gw_news_read still present on the instance role at this point |  | OPEN |
| invoke-policy | activation | gateway-global-harvest-published-invoke-policy applied on the internal reader role, ALONE and after the news read-back -- a NEW grant, not a move: it was never applied to any role | proof: get-role-policy read-back -- 1 statement, lambda:InvokeFunction on exactly one function ARN, no wildcard; plus the pre-act control that opal-gateway-role never carried it |  | OPEN |
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-p21 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=c4c106aea1cc47d15f81397208226bd9b292c9dc under the C2 guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the wrapper's own stale-base guard equal at both checkpoints, and an SSM md5 walk showing the host equal to the release blobs across app, deploy and lib |  | OPEN |
| served-read | verify | the served read through the INSTALLED code: the five news tools and the published-analysis tool answer an Opal stand-in THROUGH THE ASSUMED internal reader identity and refuse a non-Opal with zero DynamoDB reads AND zero Lambda invokes; the person reader arms exercised on a STUB store writing no record | proof: W/P21_SERVED.json -- registry 75 to 76, the assumed-role identity recorded beside the instance role's, two counters both zero, three person arms ok, contract-staging test green |  | OPEN |
| destroy-old | activation | ONLY AFTER a news tool answers through the internal reader: gw_news_read destroyed BY NAME through safe-apply targeted, and the old invoke statement confirmed gone from aws_iam_role.gw | proof: get-role-policy NoSuchEntity for the old names, the instance role's other statements byte-identical to a capture taken BEFORE the destroy, and one news tool plus the published-analysis tool re-run still served |  | OPEN |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; 2.0.0_SA_COO~MI told the live commit | proof: the commit hash carrying both, with every recomputed checksum cross-checked against the host's own measured md5 |  | OPEN |

## Log

- 20261015T233052Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
