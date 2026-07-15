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
| 1 | Commit the enable before deploy | CLOSED -- 3cf844107 (enable line + provenance comment; 0.5.0~A's queued tools verified NOT in tree; their committed c0cd853c1 redirect fix rides intentionally) |
| 2 | safe-ec2-deploy | CLOSED -- DEPLOYMENT COMPLETE; wrapper's manifest auto-record lane-blocked, recorded manually per the wrapper's own instruction @ b3084df84 |
| 3 | Restart + health | CLOSED -- restart 18:21:25Z (journal); on-box smoke passed in-deploy (health 200 local, AS metadata 200, /mcp 401); independent: public /mcp 401 Bearer-enforcement @ 18:23:18Z (ALB /health 302 = its normal OIDC front). REGISTRATION PROOF: journal 18:21:25Z '[integrations] enabled: [ycharts, opal_portal]' w/ tools=[opal_data_refresh_upload] + the full spec incl. 4 consumer-annotated hosts |
| 4 | FIRST ENABLED DRY_RUN (date=20260710, real delegated-Graph leg) | OPEN -- the tool is LIVE on the gateway surface; a dry_run needs a FRESH MCP client connection (session clients fix their tool list at connect; this session's predates the restart). Runs on the first fresh connection (Andrew reconnect / any new session) |
| 5 | Evidence to CTO | CLOSED -- sent 18:2xZ w/ the journal proof + leg-4 state |

**Legs 1-3+5 CLOSED same-session; leg 4 rides the first fresh MCP connection (minutes-class,
not a box operation -- 0.5.0~A's queued deploy is NOT held by it; box cycle complete, the
enable persists in the deploy script so their redeploy keeps it).**

**Rollback:** redeploy with ENABLED_INTEGRATIONS=ycharts (one env line) -- the integration
disables fail-closed; code presence is inert. Secret + grant may stay (inert without the enable).
