# Deploy Completion Record
**Date opened:** 2026-07-07T09:31:30.573360+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260707T093634Z
**Deploy:** SCTY_PREMCP C3-WAF: regional WAFv2 WebACL on the m365-mcp-gateway internet-facing ALB (rate-based 2000/5min + IpReputation BLOCK day-1; KnownBadInputs + CommonRuleSet COUNT-first w/ committed staggered flip-to-BLOCK; CW-Logs + all-auth-header redaction). CTO arch-gate GO 0901Z, COO apply-GO 0930Z. Last PREMCP P1 network-layer build.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit waf.tf 4711ecf56 | hash pushed origin/CLOUD | waf.tf 4711ecf56 (WAF stack) + 819c6add5 (description-charset fix) committed + pushed origin/CLOUD | CLOSED 20260707T093633Z |
| L2 | activation | safe-apply WAF stack (WebACL+association+logging+log-group+resource-policy) | plan 5add/0chg/0destroy applied + 0-diff re-plan | safe-apply (HALTGT passed) applied all 5 WAF resources: 2 passes -- first partial (log-group+resource-policy landed, WebACL failed WAFv2 description-charset validation), fixed+finished (WebACL+association+logging created). 0-diff re-plan: 'No changes, infrastructure matches configuration'. | CLOSED 20260707T093633Z |
| L3 | verify | WAF associated to aws_lb.gw + logging live + #0/#1 BLOCK #2/#3 COUNT | get-web-acl-for-resource + get-logging-configuration + 0-diff | LIVE: get-web-acl-for-resource on the ALB shows m365-mcp-gateway-waf associated, 4 rules [rate-based-ip, ip-reputation, known-bad-inputs, common-rule-set], default Allow. get-logging-configuration: dest=aws-waf-logs-m365-mcp-gateway CW group, ALL 6 auth headers redacted (authorization/cookie/x-amzn-ava-user-context/x-amzn-oidc-accesstoken/data/identity). 0-diff re-plan. Behavioral cert (flood trips #0, legit MCP/OAuth passes, #0/#1 BLOCK #2/#3 COUNT) = CVO scope. | CLOSED 20260707T093634Z |

## Log

- 20260707T093130Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260707T093633Z LEG L1 closed: waf.tf 4711ecf56 (WAF stack) + 819c6add5 (description-charset fix) committed + pushed origin/CLOUD
- 20260707T093633Z LEG L2 closed: safe-apply (HALTGT passed) applied all 5 WAF resources: 2 passes -- first partial (log-group+resource-policy landed, Web
- 20260707T093634Z LEG L3 closed: LIVE: get-web-acl-for-resource on the ALB shows m365-mcp-gateway-waf associated, 4 rules [rate-based-ip, ip-reputation, 
- 20260707T093634Z CLOSED -- all 3 legs proven
