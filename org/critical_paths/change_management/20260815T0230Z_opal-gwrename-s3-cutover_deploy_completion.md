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
| S4-14 | safe-ec2-deploy from ec2/opal-gateway/* to /opt/opal-gateway | ON-BOX systemd active + /health + md5s (never wrapper rc) | **DONE w/ 2 INCIDENTS + 2 CATCHES** -- (i) local wrapper died on BARE jq (Rule 16 absentee) masked as "Service not found in EC2_MANIFEST"; vendored .tools/jq.exe on PATH for the run, bare-jq defect BANKED. (ii) fresh venv crash-looped: unpinned mcp>=1.2.0 pulled 2.0.0 (removed mcp.server.fastmcp); RESTORED old unit on-box (minutes), pinned mcp==1.28.0 from the live old venv @81615fbd3e, redeployed green. Pre-fix catches @90b89562bc: unit-file content still pointed 4 literals at /opt/m365; old unit holds :8080 so stop-old-first guard added (runbook order unsatisfiable on one port). ON-BOX VERIFIED: systemd active, /health {ok:true}, /mcp unauth 401, **9/9 md5 == local repo**, mcp 1.28.0. Through-ALB: /mcp 401, default-action 302->Entra, TG healthy. Wrapper rc=1 all 3 attempts (#3 = its own curl racing the bind; bounded-wait fix landed); manifest recorded manually per Rule 8. |
| S4-15 | opal-gateway.service live; m365 unit stopped/disabled/removed | on-box systemctl reads | **PARTIAL BY DESIGN** -- opal-gateway.service ACTIVE, m365 unit STOPPED+DISABLED (symlink removed). Unit FILE + /opt/m365-mcp-gateway REMOVAL deliberately HELD until GW-6 cold-seat PASS (COO 030654Z: the old tree is the rollback lane, proven in incident ii). Executes as the last S4-15 act on S5-17 pass. |
| S5-16 | /health on-box | curl 200 | **DONE** -- {"ok":true} on-box 03:07:00Z + ALB health checks 200 from both AZs in the journal. |
| S5-17 | GW-6 COLD OIDC login through mcp.opalinvest.dev (fresh seat) | cold mount + first tool call succeeds; warm calls recorded non-discriminating | PENDING |
| S5-18 | Acceptance census, HISTORY/PRODUCERS split, denominators | 0 m365 across 14 surfaces (declared exceptions named) | PENDING |

**Rollback lane (runbook sec 3):** re-flip var.name -> m365-mcp-gateway + re-apply + re-set OIDC
secret. Old secrets + old S3 prefix + old unit all survive until S6 -- S6 does not open under this
ledger and starts only after S5-17 PASSES on both executor and COO reads.

**Closed:** {S5_CLOSE_TS} -- {CLOSE_SUMMARY}
