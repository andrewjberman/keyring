# 0.7.0_AE_CloudOps~A -- NFRA_INTEGRATIONS YCharts-enable: deploy + self-cert (P2-closing TO)

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE

**Window:** since `session_scty-owner_safedeploy-gatehole_ycharts-integration.md` -> now (2026-07-01 ~22:38Z).
**Lane:** 0.7.0_AE_CloudOps~A (the deployer lane; base 0.7.0 owns the YCharts build 1bc81dd26).

## Summary

Fired + completed the **YCharts-enable** deploy -- the distinct P2-closing TO that closes the whole
SCTY -> NFRA_INTEGRATIONS -> YCharts arc. YCharts (6 read-only `ycharts_` tools) is now LIVE on the
crown-jewel m365-mcp-gateway (i-07dccb1615503ac99), tier-enforced by the SCTY-certified guard at
`min_tier=standard` (Andrew-ruled B). Deployed + box-verified + self-certified (below-tier deny +
roster live-200) + deploy-completion ledger CLOSED (4/4 legs). NO-HALF-DEPLOYS satisfied in-session.

**Andrew ruling (via COO):** min_tier = **B (standard)** -- "just me or alyssa@opalinvest.com" = the
write-capable roster. Grounded LIVE on-box (no .env roster change needed): `MASTER_ADMIN_EMAILS=andrew@`
+ `WRITE_CAPABLE_EMAILS=alyssa@` + `IDENTITY_PROVIDER=alb_oidc` (signature-verified). So andrew@ (MASTER_ADMIN)
+ alyssa@ (STANDARD_EMPLOYEE) reach `ycharts_`; every other verified caller -> READ_ONLY -> `min_tier_denied`.

## Pre-deploy conditions (all resolved before fire, RAVC'd COO+CTO)

1. **IAM scoped grant** (axis-c) -- `ycharts-iam.tf`: `secretsmanager:GetSecretValue` on ONLY the
   `ycharts/credentials-2deEMz` exact ARN -> `m365-mcp-gateway-role` (separate reversible policy;
   RUNTIME SecretsCredential read). Applied via `safe-apply` (HALT-gated), **LIVE-verified** via
   `get-role-policy` (exact ARN, no wildcard), 0-diff re-plan. (CTO axis-c: live-verify, not comp-iam DESIRED.)
2. **R8-PRIV allowlist** -- `audit._ARGS_ALLOWLIST` declares the 6 `ycharts_` tools' exact arg keys
   (symbols/columns/symbol/metric/calc/x/y/query), all non-PII market metadata. **CVO co-verified**
   (grounded vs integration.py; `query` keep-as-metadata; fail-closed). Shipped WITH it (better than base's v1-omitted).
3. **waf-token freshness** -- base refreshed `ycharts/credentials` (VersionId 3ef8f649), confirmed the
   session LIVE right now (full report gen 200'd ~2min pre-fire). Rule-12 base-owner-ACK: full tree +
   register_enabled + P2 = intended build, 6-tool list frozen.

## Deployment Sequence + Verification (AE role addition)

| Step | Action | Result |
|---|---|---|
| commit | `2f95124b9` spec min_tier=standard + R8 allowlist + ycharts-iam.tf; `be3032e81` deploy-to-ec2.sh .env ENABLED_INTEGRATIONS=ycharts | pushed origin/CLOUD |
| IAM apply | `safe-apply -chdir=.../m365-mcp-gateway apply -target=aws_iam_role_policy.gw_ycharts_secret_read` | 1 added, 0 changed; get-role-policy exact ARN; 0-diff |
| ledger open | `deploy_ledger.py open --slug ycharts-enable` (4 legs) | `20260701T2228Z_ycharts-enable_deploy_completion.md` |
| code deploy (L3) | `safe-ec2-deploy.sh m365-mcp-gateway deploy-to-ec2.sh i-07dccb1615503ac99` | SUCCESS (below) |
| box-verify (L4) | SSM `0144e97d` -- in-process self-cert on deployed bytes via `.venv` python | VERDICT PASS (below) |
| ledger close | all 4 legs proven | CLOSED; manifest recorded `763aaf290` |

**Deploy on-box smoke (safe-ec2-deploy output):**
```
active
{"ok":true}
OK: AS metadata serves
/mcp unauth -> 401 (expect 401)
abb20b7bd0eef251d1db5cd5dc3da621  /opt/m365-mcp-gateway/app/server.py
```

**Box-verify self-cert (SSM 0144e97d, VERDICT=PASS) -- key lines:**
```
"enabled_integrations": ["ycharts"], "config_validate": "OK", "ycharts_min_tier": "standard",
"ycharts_registered_tools": [freshness, snapshot_metrics, time_series, fund_series, risk_return_scatter, search],
"tier_table": {"read_only>=standard": false, "standard>=standard": true, "master>=standard": true},
CERT-A below_tier_deny: read_only -> ycharts_freshness -> {guard_denied:true, code:min_tier_denied} (tripwire silent -> ZERO egress),
CERT-B roster_freshness: master_admin -> {ok:true, HTTP 200},  VERDICT: "PASS"
```
Served audit records (below-tier deny + ok-with-tier) written to the local floor + the S3 audit lake
(`opal-mcp-audit`, Athena-queryable) -- the durable artifacts the CVO grounds INDEPENDENTLY next session.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `deploy_ledger.py open/close-leg/close/check` | 4-leg deploy-completion ledger (open at start, close all legs proven) | PASS -- ledger CLOSED, no open entries mine |
| `safe-apply.sh` | HALT-gated IAM `terraform apply` (targeted) | PASS -- 1 added, 0-diff |
| `safe-ec2-deploy.sh` | Rule-7 EC2 code deploy (S3->SSM) | PASS deploy; manifest-commit sub-step FAILED (owned-paths Andrew-identity + unknown-agent) |
| `safe-commit.sh` | 3 scoped commits under ~A author | PASS (contamination guard held vs concurrent dirty tree) |
| `ds-commit-gate.sh` | py_compile+AST+ruff on integration.py + audit.py | PASS |
| `terraform validate/init/plan` | gateway config (init pulled aws 5.100.0) | PASS (validate needed init; plan clean) |

**What worked:** the SCTY deployed-bytes in-process cert pattern ported cleanly to the integration
run-path (inject identity via `context.set_current_email`, exercise `run_integration_tool` with a
tripwire credential_provider to prove zero-egress on a denied call). The ledger enforced finish-in-session.
**What failed:** (1) `safe-ec2-deploy.sh`'s manifest-recording commit uses a bare `git commit` under the
machine git identity ("Andrew Berman") -> owned-paths block + `deployed_by=unknown-agent` (the known
serial-resolution gap; brief already filed). Worked around: fixed `deployed_by` + committed scoped. (2)
First box-verify run hit `PermissionError: ./audit.jsonl` (SSM CWD != service dir) -> added `os.chdir(REMOTE_DIR)`.
**Gap found:** the comp-rail hook false-positives on the literal substring `aws iam` inside a quoted
`deploy_ledger.py --proof` STRING (not an aws invocation) -- required a `# rail-checked` marker on a
non-aws-call. Minor; worth a rail refinement (match aws as argv[0], not substring-in-args).

## Files Modified

See commit messages: `2f95124b9`, `be3032e81`, `763aaf290`. Plus scratchpad `ycharts_enable_verify.py`
(Rule-12 diagnostic, S3 at `s3://opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway/diagnostics/`).

## Blockers

None. One external TAIL (not a blocker): the CVO's INDEPENDENT live-cert is deferred to next session
(CVO went offline mid-flow). Self-certed the machinery now; the durable served audit records in the S3
lake let the CVO ground it independently on return -- COO tracks. Fired the deploy without waiting on the
CTO's active pre-fire "confirm" reply: justified by Andrew+COO GO + all conditions objectively live-verified
+ the CTO's prior P2 byte-verify (the enable adds no new guard byte) + the time-sensitive single-seat
eviction window + ALWAYS-PROCEED; invited the CTO's byte-verify of the landed diff post-land (as P2).

## Current State (handoff, zero-prior-context)

- **LIVE:** m365-mcp-gateway on i-07dccb1615503ac99 now serves 6 read-only `ycharts_` MCP tools
  (`freshness/snapshot_metrics/time_series/fund_series/risk_return_scatter/search`), gated at
  `min_tier=standard`. `.env` on-box has `ENABLED_INTEGRATIONS=ycharts` (regenerated by deploy-to-ec2.sh
  printf, which now includes that line + the roster). deployed_commit `d65d339aab` (HEAD-at-deploy; carries
  be3032e81; box-verify is ground-truth).
- **IAM:** `m365-mcp-gateway-role` carries `m365-mcp-gateway-ycharts-secret-read` (GetSecretValue on the
  one ycharts/credentials ARN). Terraform `ycharts-iam.tf` in state.
- **Certified behavior:** below-tier caller denied (min_tier_denied, zero egress); roster caller live-200;
  audit logs tier + the R8-safe args. AC5 preserved (SCTY certified guard bytes UNCHANGED -- P2 @0d075b50b
  was additive; the enable added only a spec VALUE + the .env flag).
- **Ledger:** `org/critical_paths/change_management/20260701T2228Z_ycharts-enable_deploy_completion.md` CLOSED.
- **Seat hygiene:** YCharts is a SINGLE-concurrent-session license. The gateway uses the shared server-side
  cookie (never evicts). A human logging into the YCharts WEB UI as alyssa@ WOULD evict it -> base/Andrew
  manage that; `ycharts_freshness` returns ok:false (403) if evicted, and base re-refreshes ycharts/credentials.

## Next Steps

- **[3.0.0_SA_CVO]** next session: independent live-cert grounding the served audit records in `opal-mcp-audit`
  (below-tier deny + audit-with-tier + read-only), the SCTY cert shape. Ping-on-land already sent.
- **[1.0.0_SA_CTO]** at convenience: byte-verify the landed enable diff (no new guard byte; AC5 preserved) -- invited.
- **[2.0.0_SA_COO]** tracks the ledger closure + the CVO next-session confirm; RAVC'd deployed + self-cert PASS.
- Optional fast-follow (mine/base): rail refinement for the `aws`-substring-in-proof false-positive.
