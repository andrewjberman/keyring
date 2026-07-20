# Deploy Completion Record
**Date opened:** 2026-07-20T16:29:12.931405+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260720T163015Z
**Deploy:** PORTAL_AUTHHARD Wave-1 auth-handler abuse-resistance (WS1 throttle + WS2a refresh-recheck + WS8 pwd-policy)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commits + tag portal-auth-v1.20.0 | hashes + tag pushed FF | commits 70b2560f0 (src .ts) + a6d4f52ed (TF+source-map) + 067da416e (deploy-record) + tag portal-auth-v1.20.0 pushed FF 5300b8867..067da416e CLOUD->CLOUD; safe-deploy hook clean; VALGATE clean. | CLOSED 20260720T163014Z |
| L2 | activation | terraform safe-apply portal-auth (DDB table + IAM append + WAF rule + Lambda artifact swap) | apply result + source_code_hash == built zip | safe-apply of the saved reviewed plan /tmp/wave1.tfplan: comp-tagauthz gate PASSED (0 tag overwrites); Apply complete! 1 added (aws_dynamodb_table.portal_auth_throttle) 3 changed (auth_permissions IAM append-only, opal_cloudfront_protection WAF +AuthLoginRateLimit rule, auth_handler artifact swap source_code_hash NrS1jz->eTSZUm8eVGheF4tolXuoaOQPDh0nbV7qTle+q+xpJVc= == built zip) 0 destroyed. | CLOSED 20260720T163014Z |
| L3 | verify | 0-diff replan | No changes | terraform plan post-apply: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260720T163014Z |

## Log

- 20260720T162912Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260720T163014Z LEG L1 closed: commits 70b2560f0 (src .ts) + a6d4f52ed (TF+source-map) + 067da416e (deploy-record) + tag portal-auth-v1.20.0 pushed FF 
- 20260720T163014Z LEG L2 closed: safe-apply of the saved reviewed plan /tmp/wave1.tfplan: comp-tagauthz gate PASSED (0 tag overwrites); Apply complete! 1
- 20260720T163014Z LEG L3 closed: terraform plan post-apply: 'No changes. Your infrastructure matches the configuration.'
- 20260720T163015Z CLOSED -- all 3 legs proven
