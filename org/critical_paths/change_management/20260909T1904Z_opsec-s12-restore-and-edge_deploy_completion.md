# Deploy Completion Record
**Date opened:** 2026-09-09T19:04:31.424631+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-12 RESTORE: the operative half was reverted on the box by a later 2026-09-04 deploy (row Z-S153) and the two exchange endpoints have no ALB listener rule. TWO legs: (1) redeploy the gateway from HEAD 3054872f2b, strictly forward -- range 4c3999de4a..HEAD is 3 gateway commits (S12 64577c3cc6, CLDGRPH 03b1cb0f7d, MSTR integrate e3a9d207dc) so it rewinds no lane; (2) safe-apply the ALB rules adding /otp/token in-place to otp_capability and /ms/token as new rule ms_token_capability priority 33 (ms_ingest_capability is AT the 5-value match-evaluation cap). ADDITIVE THROUGHOUT: dual-accept keeps all five callers on their static bearers, nothing is retired, no caller can break in either direction. ROLLBACK NAMED BEFORE THE FIRST ACT: code leg -> redeploy 4c3999de4a (exactly today's live state, artifact resolvable by content); edge leg -> restore otp_capability values to [/otp/fetch,/otp/health] and destroy ms_token_capability, both trivially reversible in-place listener-rule edits touching no target group and no ALB attribute. TARGETED APPLY BY DESIGN: the unscoped plan reads 1-add/3-change because waf.tf carries two PRE-EXISTING committed description drifts on aws_wafv2_ip_set.opal_blocked_ips_regional_v4/v6 that belong to the OP-s-15 / C-2 lane -- derived as not-mine by reads only (my diff touches alb.tf + ms-ingest.tf; waf.tf is untouched and HEAD already carries the drifting string), so they are DISCLOSED and NOT ridden. deletion_protection.enabled stays false, untouched, per the face.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | /opt/opal-gateway RUNNING path on i-07dccb1615503ac99 carries the operative half again | SSM md5 of the RUNNING path + symbol presence (log_credential call sites, otp/token) + OTP_BEARER_LABELS back in .env -- S3 ETag is NOT valid proof |  | OPEN |
| L2 | activation | safe-apply the two listener rules, targeted to aws_lb_listener_rule.otp_capability and aws_lb_listener_rule.ms_token_capability | apply changed-resource list with its count + targeted re-plan 0-diff + the pre-existing waf.tf drift disclosed and shown untouched |  | OPEN |
| L3 | verify | THE PLANE THE ORIGINAL PROOF MISSED: the exchange reachable THROUGH THE ALB, not on-box. The 09-04 proof exercised /otp/token on localhost where the ALB is not in the path, which is exactly why an unreachable endpoint and a correct proof coexisted | curl through https://mcp.opalinvest.dev showing server: uvicorn rather than Server: awselb/2.0 on /otp/token and /ms/token |  | OPEN |
| L4 | verify | S12-AC3 RE-EXERCISED end-to-end THROUGH THE EDGE: a capability token accepted, and the SAME token refused after its exp | both HTTP exchanges with timestamps, plus the gw_cred_observe record proving the observation instrument records the presence the retirement gate reads |  | OPEN |
| L5 | verify | no caller broken and nothing retired: the static bearers still accepted on the data endpoints throughout | a static-bearer call still authorizing after both legs land, plus push state MEASURED by ls-remote |  | OPEN |

## Log

- 20260909T190431Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
