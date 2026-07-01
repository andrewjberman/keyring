# Deploy Completion Record
**Date opened:** 2026-07-01T19:41:52.229673+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260701T210639Z
**Deploy:** SCTY_MCPGUARD guardrail landing to live m365-mcp-gateway (tier + G2 fail-closed denials + G6 tier-audit); scope-isolated SCTY-only YCharts-absent; roster andrew@=master alyssa@=write else=read-only; box i-07dccb1615503ac99. Author 0.5.0, verify+deploy 0.7.0~A.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | scty-mcpguard-deploy-build commit = 0.5.0 integrated source + YCharts isolated in deploy tree | build-branch hash + 0.5.0 author-faithful ack + my hard-verify config/server SCTY-present YCharts-absent roster-correct + 47/47 on applied app package tree | Build 8b24cd2bb (507bd7e1e isolate + roster cherry-pick) on local branch scty-mcpguard-deploy-build. 0.5.0 authored 2763b3035 + author-faithful nod; CTO landing-gate PASS (byte-verified @507bd7e1e); my hard-verify: applied diff vs box-current 28ecbd838 = SCTY-only (7 files/361 ins), 47/47 on applied app tree, R8-PRIV preserved, YCharts absent, validate anchor untouched. CLOUD YCharts 1bc81dd26 untouched. | CLOSED 20260701T203217Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway artifact + latest | s3 cp confirmation URI + artifact sha | s3://opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway/m365-mcp-gateway-8b24cd2bb.tar.gz + m365-mcp-gateway-latest.tar.gz uploaded (deploy-to-ec2.sh). SCTY-only tarball (app/ has tier/guard/destructive_ops, NO integrations). | CLOSED 20260701T203217Z |
| L3 | ec2-baked-asset | /opt/m365-mcp-gateway/app baked on i-07dccb1615503ac99 | SSM md5 of running app server/tools/config/audit.py + tier/guard/destructive_ops PRESENT + integrations ABSENT | On-box /opt/m365-mcp-gateway/app md5 == artifact md5 BYTE-IDENTICAL all 7 files (server c2580cea / tools 6e9f0490 / config 8384014c / audit 20f3f573 / tier cee1104b / guard 251b5c89 / destructive_ops 3ad7b905). tier/guard/destructive_ops PRESENT; integrations ABSENT (SCTY-only live). SSM cmd 70e7889b. | CLOSED 20260701T203218Z |
| L4 | activation | systemctl restart m365-mcp-gateway.service | is-active active + fresh start-time/PID (restart not enable-now) | systemctl restart -> is-active active, fresh MainPID 314381 (was 234713), ActiveEnterTimestamp 2026-07-01 20:29:04 UTC. New process running new code (restart not enable-now). config.validate() passed on boot (service active) + explicit RUN of deployed code OK. | CLOSED 20260701T203218Z |
| L5 | verify | on-box smoke + CVO live-cert | /mcp 401 unauth + config.validate OK + IDENTITY_PROVIDER=alb_oidc + CVO 3-case cert READ_ONLY-mutating DENY / no-identity-mutating DENY / andrew@ PASS plus alyssa@ write | CVO 3.0.0 live-cert VERDICT=PASS 4/4 (independent S3 pulls, not self-report). Record org/tier1_exec/3.0.0_SA_CVO/SCTY_MCPGUARD_LIVE_CERT_VERDICT_20260701.md. Case3 andrew@->master_admin PASS (live create_draft; served audit ok/master_admin 20:37:55.825Z). Case4 alyssa@->standard live (teams-poll served audit ok/standard; mutating-PASS compositional). Case2 no-id->identity_required: outcome-live (POST /mcp unauth->401 uvicorn) + deployed-bytes belt; served audit denied/identity_required/tier='' 21:02:09.291Z (CVO PULLED, matches). Case1 nonroster->read_only_denied: deployed-bytes floor; served audit denied/read_only_denied/tier=read_only 21:02:09.773Z (CVO PULLED, matches). Deployed md5 tier cee1104b/guard 251b5c89/destr 3ad7b905 == artifact, ZERO logic delta vs analyzed source. /mcp 401 unauth, config.validate OK, IDENTITY_PROVIDER=alb_oidc, G6 tier on ok+denied, R8-PRIV preserved on denials, zero egress (denies never hit fn(token)). Rule-12 in-process deny-proof CommandId 8710fb1f. Non-blocking follow-ups tracked: Case-1 GOLD real-login upgrade (does NOT gate close); provider-verify-vs-bearer-sub seam note (docs/briefs/scty-mcpguard-provider-check-vs-bearer-sub-seam-20260701.md, behavior correct). | CLOSED 20260701T210631Z |

## Log

- 20260701T194152Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
- 20260701T203217Z LEG L1 closed: Build 8b24cd2bb (507bd7e1e isolate + roster cherry-pick) on local branch scty-mcpguard-deploy-build. 0.5.0 authored 2763
- 20260701T203217Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway/m365-mcp-gateway-8b24cd2bb.tar.gz + m365-mcp-gateway-latest
- 20260701T203218Z LEG L3 closed: On-box /opt/m365-mcp-gateway/app md5 == artifact md5 BYTE-IDENTICAL all 7 files (server c2580cea / tools 6e9f0490 / conf
- 20260701T203218Z LEG L4 closed: systemctl restart -> is-active active, fresh MainPID 314381 (was 234713), ActiveEnterTimestamp 2026-07-01 20:29:04 UTC. 
- 20260701T210631Z LEG L5 closed: CVO 3.0.0 live-cert VERDICT=PASS 4/4 (independent S3 pulls, not self-report). Record org/tier1_exec/3.0.0_SA_CVO/SCTY_MC
- 20260701T210639Z CLOSED -- all 5 legs proven
