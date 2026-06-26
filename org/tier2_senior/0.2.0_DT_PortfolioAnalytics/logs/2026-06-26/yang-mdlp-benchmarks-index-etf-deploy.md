# yang-model-portfolio-benchmarks index/etf timeseries deploy (yang-v2.4.12)
**archetype:** DEPLOY

**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-06-26
**Window:** session start (15:55Z) -> 15:10Z; 4 commits, ~6 MCP messages, 1 deploy/tag

## Summary

Session-start /watcher + org/XXX.md startup, then picked up an Andrew-direct deploy
handoff from 0.2.0_DS_PortfolioAnalytics: deploy the `yang-model-portfolio-benchmarks`
Lambda (DS commit f3cfe6a4a) that adds `index_benchmark_return` + `etf_benchmark_return`
to each `model_portfolio_timeseries.json` row (`benchmark_return` retained as back-compat
alias == index). Powers the MDLP_RVVALT Index/ETF toggle on the Model Portfolios Benchmark
tab (Up/Down Capture, Rolling Sharpe, Max Drawdown — previously index-only). Terraform-only
deploy, full cycle landed + verified in-session, tag pushed, deploy-completion ledger CLOSED.

## What happened

1. **Reconcile before deploy.** Working tree showed lambda_function.py as ` M` while DS said
   committed at f3cfe6a4a. Ground-truthed: f3cfe6a4a IS in CLOUD lineage (ancestor of HEAD),
   `git diff HEAD -- file` empty, no commit touched the file after f3cfe6a4a. The ` M` was a
   stat-cache/CRLF-normalization artifact (DS confirmed). Deployed the committed artifact.
2. **Build + upload** (Terraform-only, Rule 1): build-and-upload.sh yang-pipeline
   yang-model-portfolio-benchmarks -> zip SHA256 `CTF3JGXMj4E+VC48PIOaTQygcU9nxpoVO+2Vyfp72Dg=`.
3. **safe-apply** (Rule 18): 1 in-place change (source_code_hash -> CTF3...); 0-diff second
   plan = "No changes."
4. **F5 live verify:** `aws lambda get-function` CodeSha256 = CTF3... (matches artifact),
   LastModified 2026-06-26T15:02:51Z.
5. **Version-collision catch:** initially assumed next tag = 2.4.10, but yang-v2.4.10/2.4.11
   already exist (Jun-1 AE positioning ETF-name deploys; my first `tail -3` was lexical not
   `sort -V`). record-terraform-deploy had stamped CHANGELOG `yang-pipeline-v2.4.10` (wrong
   number AND wrong series prefix — CHANGELOG uses `yang-v*`). Fixed forward (commit c71afeab6)
   to **yang-v2.4.12** before tagging. No collision shipped.
6. **Tag + push:** yang-v2.4.12 -> origin/CLOUD (7559aab01..c71afeab6 --follow-tags). Clean
   fast-forward (origin had advanced to include my earlier commits via a shared-branch push by
   another agent; ahead=2 behind=0).
7. **Ledger CLOSED:** 20260626T1458Z_yang-mdlp-timeseries-index-etf — all 3 legs proven.

## Deployment Sequence + Verification (actual output)

```
TF plan (pre-apply):  ~ module.model_portfolio_benchmarks.aws_lambda_function.this
                      source_code_hash DLYgGbEN... -> CTF3JGXMj4E+VC48PIOaTQygcU9nxpoVO+2Vyfp72Dg=
                      Plan: 0 to add, 1 to change, 0 to destroy.
TF apply:             Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
TF plan (0-diff):     No changes. Your infrastructure matches the configuration.
Live AWS (F5):        CodeSha256 CTF3JGXMj4E+VC48PIOaTQygcU9nxpoVO+2Vyfp72Dg=  2026-06-26T15:02:51Z
Tag:                  yang-v2.4.12 on origin/CLOUD (c71afeab6)
```

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-pipescript io | yang-model-portfolio-benchmarks | OUT-OF-SCOPE | correctly routed: globgrph-owned (model-portfolios), not medallion -> used comp-blast |
| comp-blast | yang-model-portfolio-benchmarks | PASS | confirmed producer writes model_portfolio_timeseries.json -> portal_data_proxy -> portal; additive change, no breaking edges. Satisfies Rule 20 pre-infra graph check |

What worked: comp-blast gave the blast radius + consumer chain to clear the additive change.
What failed: none. Gap: comp-pipescript io doesn't model globgrph-owned (non-medallion) threads
— it routed me to `pipescript model-portfolios` (known boundary, not a defect).

## Files Modified

see commit messages: 3b5145257 (source map), 7559aab01 (deployment_map), 88ac2c85f
(record-deploy CHANGELOG), c71afeab6 (version-collision fix). deployment_map.xml also
reconciled stale current_tag 2.3.4 -> 2.4.12 (lagged behind AE 2.4.x deploys).

## MCP traffic

DS handoff (deploy + reconcile reply) ACK'd + closed with evidence; COO flagged (low-pri)
on the owned-paths DT-enumeration gap (see below). DE is CC'd by DS on the parallel FE half.

## Owned-paths lane note

DT is not enumerated in the owned-paths permitted_agents for infra/aws/lambda/ci +
yang-pipeline TF dirs (lane = CLOUD_OPS_OR_ETL, AE-only), but deploying a yang-pipeline lambda
mechanically requires committing the source map + CHANGELOG. Used the audited
`GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` escape hatch (3 commits, logged to
org/git-author-override-audit.log) — role-authorized per README "Full DT Authority". Flagged
to COO to consider enumerating DT permanently.

## Blockers

None.

## Current State

- yang-model-portfolio-benchmarks Lambda is LIVE with the index/etf timeseries change
  (CodeSha256 CTF3JGXMj4E+VC48PIOaTQygcU9nxpoVO+2Vyfp72Dg=). Tag yang-v2.4.12 on origin/CLOUD.
- New fields (`index_benchmark_return`, `etf_benchmark_return`) materialize in
  `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` on the NEXT
  scheduled yang-pipeline run (served at /api/general/benchmarks/model_portfolio_timeseries.json).
- Code path fully deployed; served-artifact verify is the post-nightly follow-on (no ad-hoc
  gold run per Rule).

## Next Steps

- [0.2.0_DT_PortfolioAnalytics] Post next scheduled yang run: served-verify
  model_portfolio_timeseries.json — assert each row has index_benchmark_return +
  etf_benchmark_return; index_benchmark_return == benchmark_return (alias invariant);
  etf_benchmark_return != index on a recent date (distinct series).
- [0.2.0_DE_PortfolioAnalytics] FE threading of the 3 charts to benchmarkType (per DS brief
  docs/briefs/devops-brief-model-portfolio-timeseries-index-etf-toggle.md) — independent of
  this deploy; producer now supplies both series.
- [2.0.0_SA_COO] (optional) owned-paths DT-enumeration for infra/aws/lambda + owned pipeline TF.
