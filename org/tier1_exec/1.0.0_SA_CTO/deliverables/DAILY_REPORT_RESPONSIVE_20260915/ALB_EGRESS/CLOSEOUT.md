# ALB OIDC egress repair: APPLIED and EXERCISED

Recorded 2026-09-15 by `1.0.0_SA_CTO~A`.

Andrew confirms that the report loads after sign-in. The approved firewall repair is applied, its scoped Terraform postcondition is clean, and live authentication evidence satisfies the exercise condition.

## Applied change

Canonical safe-apply applied the exact saved plan authorized by CTO Msg96877, SHA-256 `00715c0dac2a7f5481d06e8fd352ac247531f94681ae85feafe568207c9d5a2b`: 0 added, 1 in-place change, 0 destroyed. The only changed resource was `aws_security_group.alb` (`sg-02571ff2f33d2f9d4`), egress only.

Live readback at `2026-09-15T04:03:48Z` confirms TCP443 to `0.0.0.0/0` and the preserved TCP8080 rule to `172.31.0.0/16`; ingress is unchanged. `APPLIED.json` and `safe-apply.txt` contain the receipts. The SG-only re-plan at `04:04:12Z` exited 0 with no managed changes or resource drift; see `sg-only-after-apply-summary.json`.

The two empty WAF IP sets retain their known, deliberately unapplied description-only differences. Full-tree zero diff is neither claimed nor expected under Msg96877. `TARGETED_ROUTE.md` records the explicit scoped-plan ruling.

## Exercised evidence

- Andrew's real-session answer is "Report loads" after being prompted to open a fresh `https://mcp.opalinvest.dev/sprint` and sign in; see `USER_VERIFICATION.md`.
- CloudWatch `ELBAuthSuccess` is 1 in the post-apply 04:04Z minute.
- ALB `/oauth2/idpresponse` at `04:04:58.944981Z` returned 302 with action `authenticate` and error reason `-`, replacing the pre-fix 500 / `AuthTokenEpRequestTimeout` failure.
- The delivered post-apply log window contains 11 requests, 0 parse errors, and 0 `AuthTokenEp*` errors. The measurement is at `04:05:37Z`, with delivered requests through `04:04:59Z`. Log delivery can lag; this is bounded observation, not a future error-free guarantee. The report-visible result comes from Andrew; the available log excerpt does not independently establish a `/sprint` 200.

See `POST_APPLY_OBSERVATION.json`. The historical `../SIGNIN_DIAGNOSIS.json` remains the unchanged pre-fix evidence.

## Source and delivery boundary

The exact `alb.tf`-only source commit is `d9d51fc43d418921abe8af894251979ed1fd0f57`, with exact-seat author and committer and the authorized audited `CLOUD_OPS_OR_ETL` lane override. The change-management record is `org/critical_paths/change_management/20260915T0343Z_opal-gateway-alb-oidc-egress_deploy_completion.md`; all declared legs now have evidence for closure.

No Gateway service deployment was needed for this repair. CLOUD push and CLOUD-to-SITEZ merge remain held. If rollback becomes necessary, remove only the added HTTPS egress block, review the resulting one-resource plan, and use canonical safe-apply to restore the original rule.
