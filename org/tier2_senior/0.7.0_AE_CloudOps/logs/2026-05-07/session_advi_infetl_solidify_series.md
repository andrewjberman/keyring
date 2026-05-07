# AE 0.7.0_AE_CloudOps — INFETL Solidify Series Session

**Date:** 2026-05-07  
**Agent:** 0.7.0_AE_CloudOps  
**Theme:** ADVI_INFETL solidify-series TO sweep — gold event-trigger chain end-to-end

## Shipped (chronological by tag)

| # | Time | Tag / Commit | TO | Outcome |
|---|------|--------------|----|---------|
| 1 | early | inf-pipeline-v1.7.33 | INFETL.001 + 005 | Fallback gold cron (DISABLED) + S3 ObjectCreated→portal-publisher notification (commit `7e9d30e7d`) |
| 2 | early | inf-pipeline-v1.7.34 | INFETL.GOLD-EVENT-TRIGGER | inf-gold-trigger now accepts aggregator event `{"snapshot_date":"…"}` + idempotency via `gold/meta/pipeline-complete.json` (commit `c6500c313`) |
| 3 | mid | n/a | OWNPTH-WIDEN (URGENT) | `infra/aws/lambda/inf-*/**` glob — unblocks DS~C INFETL.004 + future LAMBDA-DIMS (commit `bc93a1c52`) |
| 4 | mid | inf-pipeline-v1.7.35 | INFETL.IAM-CF (MINI-TO) | `cloudfront:CreateInvalidation` for `inf-gold-layer-lambda-role` scoped to dist `EVTSA9VEHNZVH` (commit `19c267f18`) |
| 5 | mid | portal-auth-v1.15.1 | INFETL.ROUTER-DRIFT | Lambda@Edge `shared-advisor-router` reconciled local↔deployed; stale `lambda/shared-advisor-router/index.mjs` v1 deleted; CF dist :19→:20 (commit `59919e763`); CloudTrail audit: 11 `UpdateFunctionCode` events 2026-04-06→2026-04-21 by Andrew_Berman IAMUser |
| 6 | late | inf-pipeline-v1.7.36 | INFETL.004 (DS~C) | inf-portal-advisor-publisher full impl deployed; lambda-source-map entry was empty (`{}`), added in `21a00aec4`. 10-Lambda batch update in same apply pass |
| 7 | late | n/a | INFETL.DAILY-AUDIT | `docs/architecture/INFETL_DAILY_PULLS_MATRIX.md` (220 lines, 9 dims). New `docs/architecture/INFETL_*` lane in `.owned-paths.yaml` (mirrors `INFLEC_*` precedent). Gap counts: A=0, B=5, C=1, D=0 (commits `f365b8c72` + `5be235f67`) |
| 8 | late | inf-pipeline-v1.7.37 | INFETL.SILVER-AGGREGATOR | inf-silver-aggregator Lambda (256 MB/60s); idempotent via `_AGGREGATOR_FIRED.json`; smoke + synthetic-event empirical PASS (commit `f4f7d35df`) |

**Sub-tasks dispatched/handled:**

- INF_D_00d 3-iteration loop (DS~D bugs surfaced + reported each iteration):
  - Iter1 fail: state-source root cause (DS~D fixed `689e9bc81`)
  - Iter2 fail: `INFLECTION_FIRM_TAG = 'inflection'` mismatched parquet `'inflection_wealth_management'` (DS~D fixed `2227a8ac1`)
  - Iter3 fail: `household_id` float `18.0` vs string `'18'` join mismatch (DS~D fixed `fc18781eb`)
  - Iter4 PASS on geo (`['WA','MT','CA','IN','MN','ID','AZ','TX','Other']`) → PROD published to `platinum/firm/cumulative_chart.json` → CF invalidation `I5O09RFW9TFJQ43D7RAU3N73FC`
  - Known non-blocking: adv shows 3/4 advisors + last-row total $189.2M vs $199.6M expected (linked; DS~D investigating post-QA pass)

## Pending / blocked at session pause

- **LAMBDA-DIMS (P1+)**: clarification request out to COO re: naming convention conflict — existing `inf-api-{reps,assets-v2,positions,txn}` Lambdas vs TO list `inf-{dim}-daily`. Recommended Option A: add sentinel-write to existing 4 + build 5 new for missing dims. Awaiting COO decision before kicking off P1 build (`inf-accounts-v2-daily`).
- **DS~C INFETL.004**: empirical invoke pending (their step) on inf-portal-advisor-publisher.
- **DS~D 4th-advisor fix**: separate DS~D investigation; non-blocking for portal cumulative_chart fix.
- **RD INFETL.007-rd**: visual-verify of cumulative_chart post-CF-invalidation (their step).

## Watcher hygiene

- Tracked `inbox-watch.sh 0.7.0_AE_CloudOps` PID 156210 (relaunched 15:34 UTC after harness restart).
- `inbox-watch.sh 0.7.0_AE_CloudOps~B` is a legitimate sibling agent (FIRMSEP work) — do NOT kill.
- Earlier in session I incorrectly killed `~B` watchers (PIDs 160864, 162722) thinking they were orphans; correction applied — `~B` is a separately-registered MCP agent.

## Key insights / surprises

- **Lambda@Edge ROUTER-DRIFT was a false drift**: deployed code matched local `lambda-edge/shared-advisor-router/index.mjs` (v13) exactly. The "drift" appearance came from the stale `lambda/shared-advisor-router/index.mjs` v1 file at the wrong path. Resolution was a delete, not a code change. CloudTrail confirmed Andrew was the only actor; iterative `aws lambda update-function-code` between 2026-04-06 and 2026-04-21 happened to land identical content to the canonical local source.
- **Persistent multi-Lambda batch updates**: each `terraform apply` on `inf-pipeline` picked up several Lambda zip uploads from concurrent DS work (DS~B, DS~C). Single-shot batch applies are how this pipeline naturally trends; nothing wrong with applying 10 Lambda zip refreshes at once.
- **EC2_MANIFEST shows inf-gold-qa-runner** but probing it revealed `/opt/inf-gold-qa-layer` was the planned path, not the real one — actual code lives elsewhere on QA. Used `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` + `--single INF_D_00d` invocation pattern instead of the planned direct-script invocation. This is the canonical Inflection gold-script dispatch flow.

## Tags shipped this session

`inf-pipeline-v1.7.33` → `1.7.34` → `1.7.35` → `1.7.36` → `1.7.37` and `portal-auth-v1.15.1`.

## Continuation — LAMBDA-DIMS Phase A + B + ADHC TOs (post-compact, 20:09Z–21:30Z)

### Phase A (4-of-4 sentinel-add to existing inf-api-* Lambdas)

| # | Tag | TO | Outcome |
|---|-----|----|---------|
| 9 | `inf-pipeline-v1.7.38` | LAMBDA-DIMS Phase A | 4 inf-api-* (reps, assets-v2, positions, txn): silver-complete sentinel writes + IAM s3:PutObject grants on `silver/_silver_complete/*/{dim}.json`. **REGRESSION** — 3 of 4 had nested-path source_map files leading to ModuleNotFoundError; caught + fixed in v1.7.39 hotfix same session. Commit `6198182a7`. |
| 10 | `inf-pipeline-v1.7.39` | LAMBDA-DIMS Phase A HOTFIX | (a) Flatten source_map files for reps/positions/assets-v2; restage flat. (b) Switch inf-api-assets-v2 layer from `pandas_layer` (no requests) to `pandas_pyarrow_requests_layer` — old zip masked the layer mismatch via inline-vendoring. Smoke PASS all 4. Commit `3f0bb6fd8`. |

### Phase B P1 + P2 (5 new inf-{dim}-daily Lambdas covering missing aggregator quorum dims)

| # | Tag | TO | Outcome |
|---|-----|----|---------|
| 11 | `inf-pipeline-v1.7.40` | LAMBDA-DIMS Phase B P1 | inf-accounts-v2-daily (NewPortfolio sync; ~1.2s; 852 rows post-INFNNA filter). Initial cron 12:55. Commit `b88d7c497`. |
| 12 | `inf-pipeline-v1.7.41` | Phase B P1 cron correction | inf-accounts-v2-daily 12:55 → 12:35 UTC per COO 20:38Z. Commit `21264bf2e`. |
| 13 | `inf-pipeline-v1.7.42` | Phase B P2 (1/2) | inf-unified-account-dim-daily — ExcelReports async bronze-only pull. Commit `330982d92`. |
| 14 | `inf-pipeline-v1.7.43` | Phase B P2 (2/2) + UAD cron correction | inf-tax-daily (two-pass ExcelReports unrealized 3y + realized YTD) + UAD cron 12:35 → 12:40 (collision resolution). Commit `0a6a842dc`. |

### Final cron sequence (post-Phase-B P1+P2)

```
12:30 inf-api-reps                  -> hh_rep_mapping bronze (existing)
12:35 inf-accounts-v2-daily         -> NewPortfolio sync; INFNNA-filtered silver
12:40 inf-unified-account-dim-daily -> ExcelReports bronze CSV (silver downstream)
12:45 inf-api-assets-v2             -> existing
12:50 inf-api-positions             -> existing
12:55 inf-tax-daily                 -> ExcelReports two-pass bronze CSVs
13:00 inf-api-txn                   -> existing (T-1 default)
```

### inf-silver-aggregator quorum status (2026-05-07 EOD)

6/9 sentinels landed: representatives, accounts_v2, unified_account_dim, assets_v2, positions_daily, tax. Missing 3: transactions (will land via cron 13:00 tomorrow → 7/9), billing + performance (P3 — gates on bronze backfill ~22:55Z + ~23:35Z tonight).

### Hotfix and structural defenses

- `memory/feedback_lambda_zip_layout_and_layer_attribution.md` dropped + indexed (Rule 1: source_map files lists are FLAT logical names; Rule 2: layer ARN docstrings drift from layer requirements.txt; corrected Windows build-and-upload.sh quirks for bun-only mode)
- ADHC TO #1 doc additions: handed off to CTO (lane gate); CTO committed as `c9059ebaf` with my Co-Authored-By attribution. New sections in `LAMBDA_DEPLOYMENT_PROTOCOL.md`: §2.4a FLAT files convention + when-nested-is-legitimate exemptions (Node.js bundles, Python `__init__.py` packages, read-as-data files); §2.4b layer verification; §2c Lambda@Edge TWO-STAGE APPLY (incorporates ~B's plan-time locals subtlety from FIRMSEP.03); §2b refresh Mode A vs Mode B Windows build. New PRD: `docs/architecture/ADHC_LAMBDADOC.md`.
- ADHC TO #2 MVP shipped: `.tools/check-lambda-layer-deps` (commit `fc4d1f18f` + parser refinement `59350fdc2`). AST-extracts top-level imports per Lambda, parses layers from .tf (now handles `local.X`, `aws_lambda_layer_version.X.arn`, `module.X.layer_arn`), checks against layer requirements.txt + opaque-layer registry. **Verified replay** of v1.7.38 inf-api-assets-v2 incident: with the buggy `pandas_layer` it correctly reports `FAIL ... MISSING imports: ['requests']`; with the corrected layer 0 FAIL. Coverage: 147 functions, 115 OK, 32 still FAIL (mostly source_map entries with null tf_file or inline-vendored deps; iterative TO-003 follow-on scope).

### Cross-pod coordination

- AE 0.7.0~B (FIRMSEP work): three-way exchange on Lambda@Edge two-stage pattern. ~B's empirical FIRMSEP.03 evidence was absorbed into LAMBDA_DEPLOYMENT_PROTOCOL.md §2c (timing table verbatim + plan-time locals subtlety), CTO committed.
- 1.0.0_SA_CTO: handoff for cross-lane doc commits (docs/architecture + docs/deployment are CTO-owned per .owned-paths.yaml). Pattern: AE drafts + sends commit message + git commands; CTO commits with `Co-Authored-By` to preserve author attribution. Worked cleanly first attempt.
- 2.0.0_SA_COO: 6 RAVCs sent, 6 ACKs received. COO course-corrected cron slots twice (12:55 → 12:35 for accounts_v2; 12:35 → 12:40 for UAD); both corrections accepted + shipped same session.

### Tags shipped this continuation

`inf-pipeline-v1.7.38` → `1.7.39` (HOTFIX) → `1.7.40` → `1.7.41` (cron correction) → `1.7.42` → `1.7.43`. Plus `c9059ebaf` (CTO; ADHC_LAMBDADOC.001) and `fc4d1f18f` + `59350fdc2` (.tools/check-lambda-layer-deps MVP + refinement).
