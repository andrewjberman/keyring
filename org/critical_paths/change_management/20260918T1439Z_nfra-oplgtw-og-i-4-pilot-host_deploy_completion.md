# Deploy Completion Record
**Date opened:** 2026-09-18T14:39:08.022282+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T150654Z
**Deploy:** NFRA_OPLGTW.TO-OG-i-4 -- pilot host resize t4g.nano to t4g.small on aws_instance.gw (i-07dccb1615503ac99). G-A lifted by Andrew-direct org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_140xZ_FOUR_CARDS_ANSWERED_GA_YES_SPRINT_EMPLOYEES.md@80558e1508 (Call 1: Yes go ahead), scoped to this stop/start only.
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply resize of aws_instance.gw instance_type via saved planfile (0 add, 1 change, 0 destroy) | terraform apply output + before/after describe-instances | safe-apply -chdir=infra/aws/terraform/opal-gateway apply -no-color -input=false <saved planfile resize.tfplan> rc=0: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' (aws_instance.gw: Modifications complete after 43s). BEFORE (describe-instances): InstanceType=t4g.nano Architecture=arm64 State=running LaunchTime=2026-08-21T07:58:44.000Z. AFTER (describe-instances): InstanceType=t4g.small Architecture=arm64 State=running LaunchTime=2026-09-18T14:53:48.000Z PublicIp=54.197.78.28 (new ephemeral IP, no EIP, expected per plan). safe-apply's tag-authz and tombstone gates both PASSED (no plan resource overwrites a tag; no planned create matches a tombstone). halt-gate: routine-only (25 messages, none STOP-class, issuer 2.0.0_SA_COO~O's inbox scanned since this worker carries none), acked HALT_ACK=1 per its own documented routine-ack contract. | CLOSED 20260918T145747Z |
| L2 | verify | post-apply live host state: instance type/arch/running, systemd opal-gateway active, unauthenticated /mcp 401 resource challenge, existing-user latency baseline (OG-p-1 OGP1-AC11 instrument/window) re-taken | SSM host reads + HTTPS probe + CloudWatch p95 read | POST-APPLY LIVE STATE, all read after L1 closed: (1) describe-instances i-07dccb1615503ac99 -> InstanceType=t4g.small Architecture=arm64 State=running LaunchTime=2026-09-18T14:53:48.000Z. (2) SSM AWS-RunShellScript (command 381e1b4b-b9f1-4f1e-a233-463ba83dc708, Success): systemctl show opal-gateway -> ActiveState=active SubState=running MainPID=1549 NRestarts=0 ActiveEnterTimestamp='Fri 2026-09-18 14:53:58 UTC'; uname -m=aarch64; curl localhost:8080/health -> 200. (3) External unauthenticated GET https://mcp.opalinvest.dev/mcp at 2026-09-18T15:03:51Z -> HTTP 401, WWW-Authenticate: Bearer resource_metadata="https://mcp.opalinvest.dev/.well-known/oauth-protected-resource", body {"error":"invalid_token","error_description":"missing bearer credential"}. (4) Existing-user baseline re-taken with OG-p-1's OGP1-AC11 instrument (cloudwatch GetMetricStatistics AWS/ApplicationELB TargetResponseTime, SampleCount+p95, one 14-day period) and window rule (trailing 14 days from read time): window 2026-09-04T15:05:06Z..2026-09-18T15:05:06Z, overall sample_count=39899 p95_seconds=0.5506999186879076, target group opal-gateway-tg identical (single TG). Compares against OG-p-1's pre-change reading (sample_count=43745 p95=0.5535024102704742, window ending 2026-09-16T19:15:00Z) -- same instrument, same 14-day window rule, later trailing window as expected for a re-take. | CLOSED 20260918T150612Z |

## Log

- 20260918T143908Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 2 leg(s)
- 20260918T145747Z LEG L1 closed: safe-apply -chdir=infra/aws/terraform/opal-gateway apply -no-color -input=false <saved planfile resize.tfplan> rc=0: 'Ap
- 20260918T150612Z LEG L2 closed: POST-APPLY LIVE STATE, all read after L1 closed: (1) describe-instances i-07dccb1615503ac99 -> InstanceType=t4g.small Ar
- 20260918T150654Z CLOSED -- all 2 legs proven
