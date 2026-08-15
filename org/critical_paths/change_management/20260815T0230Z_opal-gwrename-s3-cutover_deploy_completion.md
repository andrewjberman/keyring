# Deploy-completion ledger -- OPAL_GWRENAME S3-S5 live cutover (m365 -> opal-gateway)

**Opened:** 20260815T0230Z by 0.7.0_AE_CloudOps (TO-1; COO S3 GO 20260815T022625Z; Andrew-direct 2026-08-15)
**Spec:** docs/runbooks/opal-gateway-rename-cutover-runbook.md @c0e8ead091 | LD-0414 / LD-0415
**Repo state applied:** @f6031fd6f7 (S2 + revert; user_data residual carried: TRIP-CONDITION on any future instance replacement + Entra-CA egress-IP precondition for any approved stop/start), plan 40 add / 7 change / 35 destroy,
aws_instance.gw in-place.
**Status: OPEN -- a begun deploy FINISHES in-session or rolls back + escalates loud (NEVER#8).**

| Leg | Act | Proof required | State |
|---|---|---|---|
| S3-11 | safe-apply the rename cascade | apply rc + post-apply re-plan 0-diff | **DONE w/ INCIDENT** -- apply-1 rc=1: SG-replacement deadlock (default destroy-first vs instance ENI; old listeners+rules+WAF-assoc destroyed, new ALB chain stranded -> ~35min full outage on mcp.opalinvest.dev, COO-confirmed HTTP:000 025215Z). Roll-forward: CBD on both SGs @e0e4c62fba (MSTR-endorsed; rollback was NO LONGER a restore path -- old listeners already gone). apply-2 rc=0; post-apply plan **"No changes" 0-diff**. -target fork pre-authorized by MSTR was NOT needed. |
| S3-12 | H1: CLI re-set OIDC client_secret on NEW listener | modify-listener applied + unauth curl 302s to login.microsoftonline.com | **DONE** -- modify-listener on listener/app/opal-gateway/89166a68f337e5a4/2904a0140214f982, value in-memory from opal/mcp/opal-gateway-login, ClientId cross-checked (53360468-...). Unauth curl: HTTP 302 -> login.microsoftonline.com/6810043e-.../authorize, correct client_id + redirect_uri. **302 proves restore+wiring, NOT the secret** (exercised only at token exchange) -- S5-17 cold login stays the oracle. |
| S3-13 | WAF re-association check | web-acl association on NEW ALB live-read | **DONE** -- get-web-acl-for-resource on the new ALB = opal-gateway-waf. |
| S4-14 | safe-ec2-deploy from ec2/opal-gateway/* to /opt/opal-gateway | ON-BOX systemd active + /health + md5s (never wrapper rc) | PENDING |
| S4-15 | opal-gateway.service live; m365 unit stopped/disabled/removed | on-box systemctl reads | PENDING |
| S5-16 | /health on-box | curl 200 | PENDING |
| S5-17 | GW-6 COLD OIDC login through mcp.opalinvest.dev (fresh seat) | cold mount + first tool call succeeds; warm calls recorded non-discriminating | PENDING |
| S5-18 | Acceptance census, HISTORY/PRODUCERS split, denominators | 0 m365 across 14 surfaces (declared exceptions named) | PENDING |

**Rollback lane (runbook sec 3):** re-flip var.name -> m365-mcp-gateway + re-apply + re-set OIDC
secret. Old secrets + old S3 prefix + old unit all survive until S6 -- S6 does not open under this
ledger and starts only after S5-17 PASSES on both executor and COO reads.

**Closed:** {S5_CLOSE_TS} -- {CLOSE_SUMMARY}
