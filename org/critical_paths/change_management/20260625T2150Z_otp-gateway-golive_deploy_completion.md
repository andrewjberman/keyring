# Deploy Completion Record
**Date opened:** 2026-06-25T21:50:35.309603+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T215311Z
**Deploy:** OTP endpoint go-live: gw IAM + code deploy + ALB rule on the production m365-gateway
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| gw-tf | verify | gw role +OTP-bearer-read + ALB /otp rule applied | true | safe-apply: gw_golive role +GetSecretValue on blackdiamond/49f/otp-gateway-token; aws_lb_listener_rule.otp_capability created (priority 30, /otp/fetch+/otp/health forward no-OIDC). Verified live: external /otp/health routes (401 no-bearer, not 404). | CLOSED 20260625T215311Z |
| gw-code | verify | /otp routes + OTP env deployed to the gateway box, /mcp still 401 | true | safe-ec2-deploy to the production gateway (HEAD with app/otp.py + routes). On-box smoke: active, /health ok, /mcp 401. EXTERNAL verify: /otp/health no-bearer=401, with-bearer={ok:true} (gateway mints andrew@opalinvest.com delegated token -> OTP_MAILBOX correct + mailbox-token-live), /mcp unauth=401 (MCP surface intact). | CLOSED 20260625T215311Z |

## Log

- 20260625T215035Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260625T215311Z LEG gw-tf closed: safe-apply: gw_golive role +GetSecretValue on blackdiamond/49f/otp-gateway-token; aws_lb_listener_rule.otp_capability cr
- 20260625T215311Z LEG gw-code closed: safe-ec2-deploy to the production gateway (HEAD with app/otp.py + routes). On-box smoke: active, /health ok, /mcp 401. E
- 20260625T215311Z CLOSED -- all 2 legs proven
