# Deploy Completion Record
**Date opened:** 2026-09-17T18:03:35.509383+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260917T182453Z
**Deploy:** OG-i-3: rename Schwab reader identities to builder names, create the read-only SSM document + operator pin, add the browser-download ALB listener rule
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | opal-gateway TF root: rename 5 replaced resources + create SSM document/pin policy/ALB rule | terraform apply plan JSON + live readback (iam get-role x2, ssm get-document, elbv2 describe-rules) | safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply rc0 2026-09-17T18:1xZ-18:2xZ: 'Apply complete! Resources: 8 added, 0 changed, 5 destroyed.' Naming plan gate WARN 48 graded (no REFUSE), comp-tagauthz PASSED, tombstone CLEAN 8 creates vs 7 tombstones. Live readback: iam get-role gateway-schwab-read-role/gateway-schwab-catalog-read-role present, opal-mcp-emp-menachem-schwab-read/opal-mcp-schwab-catalog-read NoSuchEntity; ssm describe-document gateway-readonly-host-document Active. Evidence: deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i3/{plan.json,apply.log} | CLOSED 20260917T182453Z |
| readback | verify | OGI3-AC1..AC6 probe re-run against live state | probe VERDICT lines + printed measurements | elbv2 describe-rules on the HTTPS listener: rules 10/20/30/31/32/33/default byte-equal to OG-p-1 baseline, new rule 34 carries exactly the 4 browser paths; wafv2 get-web-acl-for-resource == baseline (opal-gateway-waf, 5 rules); idle_timeout.timeout_seconds=60 == baseline; unauthenticated GET /og-i-3-unrelated-probe-path -> 302 to login.microsoftonline.com, GET on each of the 4 explicit paths -> 404 server=uvicorn (reaches the app, no Location). Evidence: deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i3/{live_rules.json,live_waf.json} | CLOSED 20260917T182453Z |

## Log

- 20260917T180335Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 2 leg(s)
- 20260917T182453Z LEG apply closed: safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply rc0 2026-09-17T18:1xZ-18:2xZ: 'Apply complete! Resources: 8 
- 20260917T182453Z LEG readback closed: elbv2 describe-rules on the HTTPS listener: rules 10/20/30/31/32/33/default byte-equal to OG-p-1 baseline, new rule 34 c
- 20260917T182453Z CLOSED -- all 2 legs proven
