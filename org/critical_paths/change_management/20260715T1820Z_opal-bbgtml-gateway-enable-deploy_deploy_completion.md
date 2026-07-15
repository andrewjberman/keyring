# Deploy-completion ledger — OPAL_BBGTML gateway enable deploy (m365-mcp-gateway EC2)

**Opened:** 2026-07-15 ~18:20Z by 0.2.0_DT_PortfolioAnalytics (sovereign delegate)
**Authorization chain:** CTO enable-gate review PASSED 20260715T181026Z (source + his own
isolated 22a) -> Andrew tempo ruling ~18:1xZ (verbatim at 080183d60) -> CTO GO-FLIP-NOW
20260715T181610Z. Allowlist question resolved in-spec @ 454f76fa4 (accepted).
**Change:** canonical safe-ec2-deploy of the gateway (code incl. opal_portal integration +
.env ENABLED_INTEGRATIONS=ycharts opal_portal + systemd restart). Live MCP surface gains ONE
mutating tool (opal_data_refresh_upload, min_tier=standard, confirm-gated).
**Operational note (CTO):** the restart interrupts m365 MCP availability fabric-wide for
seconds -- restart timestamp recorded below for any concurrent-call forensics.

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | Commit the enable (deploy script env line + comment) before deploy | OPEN |
| 2 | safe-ec2-deploy (S3 artifact -> SSM pull -> .env -> restart -> on-box health+smoke) | OPEN |
| 3 | Restart timestamp recorded + gateway healthy (health 200, /mcp 401-unauth) | OPEN |
| 4 | FIRST ENABLED DRY_RUN (date=20260710, real delegated-Graph leg -- closes the substitution) | OPEN |
| 5 | Evidence to CTO | OPEN |

**Rollback:** redeploy with ENABLED_INTEGRATIONS=ycharts (one env line) -- the integration
disables fail-closed; code presence is inert. Secret + grant may stay (inert without the enable).
