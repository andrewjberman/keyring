# Session Log — 0.7.0_AE_CloudOps — YALP_MDSRC.C2 (AE infra-side) — 2026-05-22

## Summary

Deployed the AE infra-side of **YALP_MDSRC.C2** — the DS-authored
`ycharts-market-data-pull` module (WS-1 replaceable surfaces + WS-2 hybrid
legs). Per the YCHARTS_PULL_MODULE lane split (DS code / AE infra+deploy):
added the source-map entry + the ycharts-pipeline Terraform, deployed the
Lambda **dormant** (C1 pattern — no EventBridge schedule, no live YCharts
execution). Bridges C2 -> D1.

## Blocker handled

On pickup, `ws1_surface_pull.py` was uncommitted in the working tree (the
WS1-VAL-01 valuation-multiples live-validation resolution). build-and-upload
zips the working tree — deploying would have put uncommitted code in the
artifact (Rule 2). The C2 module is the DS code lane — not mine to commit.
Routed to 0.1.0_DS, who committed it (`3d9617427`). Resumed clean.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Source-map entry | `ycharts-market-data-pull` added (8 files) |
| 2 | build-and-upload | SHA256 `ortIQgLi7FFO2E0dn9TTzucwiLbqpwwkwYSWwHLrqV0=`; `ycharts-pipeline/ycharts-market-data-pull.zip` (30,120 bytes) |
| 3 | Commit source + map | `deede289d` feat(ycharts-pipeline): C2 market-data-pull Lambda |
| 4 | terraform plan | 5 to add, 0 change, 0 destroy |
| 5 | safe-apply (HALTGT clean) | 5 added, 0 changed, 0 destroyed |
| 6 | 0-diff replan | No changes. Infrastructure matches the configuration. |
| 7 | Invoke `validate` mode | StatusCode 200, ok=True, "7/7 modules structurally valid" — no YCharts call |
| 8 | record-deploy + tag + push | `922978f55` ci: record deploy; tag `ycharts-pipeline-v1.2.0` |

## Stale-build catch + correction

After the v1.2.0 deploy, 0.1.0_DS flagged that `ws1_surface_pull.py` had one
more DS-lane commit (`e3688eb00`, the VAL-01 hybrid-surface ruling) that landed
between my first build and the push. A deployed-vs-HEAD **byte check** confirmed
it: the v1.2.0 artifact's `ws1_surface_pull.py` matched `3d9617427`, NOT HEAD
(`e3688eb00`) — one ws1 commit stale; the other 7 files matched HEAD. Caught
empirically, not assumed. Recovery: verified the module working tree == HEAD ==
origin, rebuilt the artifact, re-applied. The corrected v1.2.1 artifact's all-8
files now byte-match HEAD. Lesson: re-verify the Lambda source path is at
current origin/HEAD *immediately* before `build-and-upload` — the multi-agent
CLOUD branch moves under you.

## Deployment Tags

| Pipeline | Tag | Note |
|----------|-----|------|
| ycharts-pipeline | `ycharts-pipeline-v1.2.0` | first deploy — artifact one ws1 commit stale |
| ycharts-pipeline | `ycharts-pipeline-v1.2.1` | **corrected** — rebuilt from HEAD, all 8 files byte-match |

## Infrastructure

- `aws_lambda_function.ycharts_market_data_pull` — zip Lambda, python3.11,
  512 MB / 300 s, x86_64. Handler `lambda_function.lambda_handler`. Pure
  stdlib (urllib + boto3 runtime) — no layer, no image.
- IAM `YChartsMarketDataPullLambdaRole` — least-privilege: basic execution +
  `secretsmanager:GetSecretValue` on exactly `ycharts/credentials` (the
  session cookie bundle, via `ycharts_client.py`) and `opal/external-apis`
  (the FRED key, via `ws2_mp_benchmark_pull.py`). **No S3 grant** — the
  handler returns its pull result in the response; persistence is TO-D1.
- **No EventBridge schedule** — deployed dormant.

## Verification — DORMANT (YCharts freeze respected)

- `ycharts-market-data-pull`: State=Active, LastUpdateStatus=Successful, python3.11.
- **Deployed artifact == HEAD**: all 8 module files in the deployed (v1.2.1)
  zip byte-match `git show HEAD:` — confirmed after the rebuild.
- `validate`-mode invoke: 200, ok=True, "7/7 modules structurally valid" —
  the handler's freeze-aware structural self-test (synthetic data, NO network,
  NO YCharts call). The live `pull` path is wired but unused; it fail-fasts on
  `freshness_probe()` against a dead seat.
- terraform 0-diff replan: clean.

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 | `comp-iam service` on the new Lambda | Graph pre-deploy-stale; manual enumeration: 2 boto3 calls — `GetSecretValue` on `ycharts/credentials` + `opal/external-apis` — both matched 1:1 by `ycharts_market_data_pull_secrets` (resource-scoped to those 2 ARNs, least-privilege). No S3/other surface. |
| 2 | `comp-iam gaps` | N/A pre-graph-rebuild; the IAM is a closed set (2 GetSecretValue grants, both present). |
| 3 | terraform 0-diff replan + `aws lambda get-function-configuration` + validate-invoke | All PASS. |

## Current State

| Item | Status |
|------|--------|
| C2 AE infra-side | COMPLETE — `ycharts-pipeline-v1.2.1` (v1.2.0 corrected for a stale ws1); Lambda Active, dormant, artifact byte-matches HEAD |
| EventBridge | None — dormant by design (go-live = TO-D1 + seat) |
| C2 RAVC2 | SENT — COO (no CC CTO per Andrew) |

## Next Steps

1. [2.0.0_SA_COO] RAVC4 / fold into the C2 close; C2 -> D1 bridge is in place.
2. [D1, downstream] the surface cutover behind the parallel-run diff gate —
   needs this Lambda (exists now) + the dedicated YCharts seat.
3. [Andrew/procurement] dedicated YCharts seat -> go-live (enable a schedule
   or the D1 invoke path).
