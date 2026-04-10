# 0.4.0_DT Log: ADVI_49PUSH.047 -- clients-tab-slim Lambda deploy
**Date:** 2026-04-09
**Agent:** 0.4.0_DT_ClientPlatform
**Tag:** partners-api-v1.15.6
**DS commit:** 547ed0dd

## Context

DS .047 rewired the clients-tab endpoint to serve a pre-built slim file
instead of pseudonymizing a 206 kB payload on every request.

Change in lambda_function.py (547ed0dd):
- handle_clients_tab(): reads platinum/firm/clients-tab-slim.json (was gold/artifacts/clients_tab.json)
- /clients-tab handler: returns handle_clients_tab(bucket) directly, no _pseudonymize_s3_response
- D_04 now writes the slim file at gold run time (once per run, not per request)

Note: v1.15.5 built BEFORE 547ed0dd was in the artifact. This deploy (v1.15.6)
bundles BOTH .047 (slim path) and .048 (firm bucket cache) into one artifact.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| py_compile | python -m py_compile lambda_function.py | PASS |
| git show | 547ed0dd -- lambda_function.py | Reviewed diff -- 2 hunks, slim path + no pseudonymize |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | py_compile | PASS |
| 2 | build-and-upload.sh partners-api opal-partners-data | SHA: 8g9rOyYV8+1H2ZQLsutuXgMUrVvmqng9Gk1Jpw1nJEw= |
| 3 | git commit (source map) | 8c3f8d93 ci: upload artifact .047+048 [skip ci] |
| 4 | terraform plan | 1 change: source_code_hash |
| 5 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | record-terraform-deploy.sh | committed [skip ci] |
| 8 | git tag | partners-api-v1.15.6 |
| 9 | git push --follow-tags | CLOUD: 580fc0ab..35387b17 + tag pushed |

## Deployment Tags

| Pipeline | Tag | Commit |
|---------|-----|--------|
| partners-api | partners-api-v1.15.6 | 35387b17 |

## Artifact Contents

This artifact includes cumulative changes from:
- ADVI_49PUSH.047 (547ed0dd): slim S3 path + no pseudonymize on clients-tab
- ADVI_49PUSH.048 (f3a5f003): _bucket_cache module-level dict in get_firm_bucket

SHA before (.047 not included): SIaoy8Xmtwe2+g1cl6OXYZnY5OfDRzR19n58dOKyZKk=
SHA after (.047 + .048):        8g9rOyYV8+1H2ZQLsutuXgMUrVvmqng9Gk1Jpw1nJEw=

## DE Handoff

Messaged 0.4.0_DE_ClientPlatform: make clients field optional in ClientsTabResponse.
  clients?: ClientOption[]  (was clients: ClientOption[])
Waiting for DE commit to portal DEV before pushing DEV.

## Current State

- partners-api-v1.15.6 live
- clients-tab: 350 bytes, ~100-150ms latency (was 206 kB, 7s)
- Slim file live on S3 (DS confirmed)
- DE type fix pending

## Next Steps

- [DE] Make clients?: ClientOption[] optional in ClientsTabResponse, commit to portal DEV
- [DT] Push portal DEV after DE commits
