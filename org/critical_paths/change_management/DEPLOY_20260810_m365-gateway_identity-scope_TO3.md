# Deploy ledger — m365-mcp-gateway identity_scope (OPAL_ANALYST.TO3)

- **Opened:** 2026-08-10T17:15Z by 0.5.0_AE_OpalETL~Z
- **CLOSED:** 2026-08-10T17:30Z by 0.5.0_AE_OpalETL~Z — COMPLETE, exercised
- **Commits:** 42444e64b (identity_scope + wiring + tests) · overlay row (# andrew-asked
  @e77bec6e5) · 2582eb244 (artifact include-list fix) · manifest records 0b5f5009d + 2 more
- **Mechanism:** infra/aws/ec2/safe-ec2-deploy.sh m365-mcp-gateway (S3 artifact -> SSM pull)
- **Target:** i-07dccb1615503ac99 (/opt/m365-mcp-gateway)
- **Deploys:** 3 (17:16Z code; 17:25Z overlay-intended — overlay NOT packed, caught by
  exercised run (d), never by the wrapper's green; 17:29Z with include-list fix — verified)

## Steps
- [x] commit before deploy
- [x] deploy executed (SSM Success 25cc4d7a / 5033f07a)
- [x] behavior verified by EXERCISE (not config-read), separate invocations:
      (a) bbg key + list_recent_email -> code identity_scope_denied, quotable — PASS
      (b) bbg key + whoami -> serves as Opal Bloomberg — PASS
      (c) Andrew key + list_recent_email -> unaffected, data served — PASS
      (d) bbg key + opal_data_refresh_upload -> passes scope, integration confirm-gates,
          nothing fired — PASS (overlay live); (a)-recheck still denied — PASS
- [x] manifest entries committed (SHARED_CLOUD_OPS override, audited)
- [x] CLOSED

## Note for the record
Run (d) FAILED on the second deploy: the deploy script's tar include list is explicit
(`app deploy requirements.txt`) and silently omitted the new root-level overlay file — the
wrapper reported green both times. The exercised control, not the deploy tooling, caught
it. Fix: one token added to the include list (2582eb244).
