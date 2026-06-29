# Deprecated-Candidates Scan — pre-monster-push (comp-dups + reachability + heat-disambiguation)

**archetype:** EXPLORE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** Andrew (methodical pre-push debt scan) · cc COO/CTO
**Tools:** comp-dups (full estate scan) + NFRA_DEBTSCAN D1 reachability ledger + the literal deprecated dir. **ADVISORY — comp-dups NEVER removes; every item is a CANDIDATE needing per-item grounding (heat is the disambiguator, §HEAT).**

## How to read this: the scan FINDS, heat DISAMBIGUATES
comp-dups surfaces **twins** (two-states-one-resource / dup content) but does NOT always know which is the LIVE one vs the dead prototype. **Heat-mapping is the discriminator** (Andrew 2026-06-29): for each twin, the HOT one (recently deployed/touched/accessed) is real; the COLD one is the deprecation candidate. See §HEAT for the mechanism. So: scan = the candidate list; heat = which side of each twin to deprecate.

## TIER 1 — HIGH CONFIDENCE (literal-deprecated + archive prototypes)
| Item | Evidence | Pipeline |
|---|---|---|
| **`infra/aws/lambda/deprecated/`** (whole dir: analyze-deployments / deployment-drift-check / deployment-guard / lambda-deploy / safe-lambda-deploy / rollback-assistant / sync-manifest + LAMBDA_MANIFEST.json + opal-portal-volatility-fetcher-standalone.tf + docs) | the OLD deploy tooling, superseded by TF + `.tools/safe-*`; comp-dups DEAD-flags the `aws_lambda_function.this` / `event_target.lambda` here as `INFERRED_DEAD_GRAPH_PENDING` | infra/deploy-tooling |
| **`data/black_diamond/archive/**`** content-dup prototypes | comp-dups CONTENT_EXACT_DUP: build_transaction_engine.py ×3 (+`_GOOD_1015AM`, `_v1_GOOD_2026-01-21`), `_BAD_with_closure_detection` ×2, lambda_function+`_updated`, +`_v1_backup` | bd (advi-bd) |
| **`bd-price-update/lambda_function_v1_backup.py`** | exact-dup of the archived price_update lambda_function.py | advi-bd |

## TIER 2 — TF DOUBLE-MANAGEMENT (twin = two-states-one-resource; HEAT picks the real one)
The real twin/double-management signal — each is a possible drift (two TF states, one live resource):
| Resource | Twin A | Twin B | Risk |
|---|---|---|---|
| `aws_dynamodb_table.opal_users_v2` | `terraform/portal-auth` | `terraform/shared-infra` | **auth DDB double-managed** — apply-order drift; heat = which module last-applied + which the live table's tags point to |
| `aws_iam_role.bd_exporter` + `instance_profile` | `ec2/bd-exporter/terraform` | `terraform/bd-pipeline` | role/profile twin |
| `aws_iam_role_policy.step_functions_lambda_invoke` | `multi-account/environments/{prod,staging}` | `terraform/bd-pipeline` | **triplicated** policy — the multi-account env copies vs the live bd-pipeline one |
| `aws_lambda_function.this` / `log_group.lambda` | `multi-account/modules/lambda` | `terraform/modules/yang-lambda` (+ `lambda/deprecated`) | module twin; the `lambda/deprecated` leg is Tier-1 dead |

## TIER 3 — REACHABILITY ORPHANS (NFRA_DEBTSCAN D1 ledger 2026-06-12; needs re-verify vs current graph)
| Candidate | Count | Verdict (per D1) |
|---|---|---|
| SNS_TOPIC, 0 subscribers | 2 | **REAL candidates** (dead topics) |
| `bd-time-machine` Lambda (no inbound TRIGGERS/INVOKES) | 1 | **REAL** |
| S3_DATA_KEY fully isolated (0 in + 0 out) | 6 | candidate |
| GOLD_SCRIPT edgeless (script-level) | 36 | 21 `E_*` diagnostic + 15 misc — likely many real-dead |
| KMS_KEY isolated | 5 | PENDING investigation |
| DYNAMODB_TABLE isolated | 3 | 1 NEEDS-VERIFY (2 Nessie-internal FP) |
| (FP-classified, NOT candidates) | — | LOG_GROUP×190 / SECRET×40 / CW_ALARM×2 / EC2×1 = implicit-edge FPs, already suppressed |

## TIER 4 — DEV/PROTOTYPE TWINS (data/ source vs infra/ deployed; HEAT picks)
| Item | Twin | Likely-dead side |
|---|---|---|
| `data/smartx/scripts/lambda_smartx_query.py` | `infra/aws/lambda/smartx_query/lambda_function.py` | the `data/` copy = dev/prototype; infra/ = deployed |
| `test-seeking-alpha-unauth-simple` | `test_seeking_alpha_unauth/lambda_function_simple.py` | test dups — both likely throwaway |

## HEAT — the real-vs-dup discriminator (Andrew 2026-06-29; the methodical disambiguator)
For every Tier-2/Tier-4 TWIN, the question "which is real?" is a HEAT question:
- **code twin** → git last-commit + is-it-deployed (comp-pipescript deployed / comp-lambdamap parity) + import-reachability.
- **infra/TF twin** → which module last-applied + the LIVE resource's tags/state (which TF state actually owns it) + last-deploy.
- **data twin** → last-access / last-write recency.
A single **universal heat_band per resource** (recency from the appropriate source per layer) makes "HOT=real / COLD=deprecate" a queryable verdict per twin. **This is exactly the NFRA_HEATMAP / heat-federation build** (Iceberg+Trino, currently IN-BUILD per my /seams 28ecbd838): the heat-federation computes one heat_band over aws/portal/ms/pipeline Iceberg assets + git-native code-heat. So the methodical pipeline-by-pipeline scan = **comp-dups (find twins) → heat_band per twin (rank recency) → the COLD side is the deprecation candidate, per resource.** Until heat-federation lands, the twins above are disambiguable manually (git-last-touch + deployed-check) per item.

## Recommended methodical sweep (pipeline-by-pipeline)
1. **Now (no heat-fed needed):** action Tier-1 (literal-deprecated dir + archive prototypes — git-history-preserved, safe to remove from the working tree; route to the owning lane, not a CVO delete).
2. **Per-pipeline, heat-ranked:** run `comp-dups --class` per class + `pipescript <thread>` per pipeline (27 threads); for each twin, apply heat (manual now / heat_band post-federation) → mark the cold side deprecate-candidate.
3. **Re-verify Tier-3 orphans vs the CURRENT graph** (the D1 ledger is 2026-06-12; the graph is now 5.1h-current) before acting — a 06-12 orphan may have gained an edge.

## HEAT APPLIED (creative multi-source, since Trino/heat-fed not live yet — Andrew 2026-06-29)
Disambiguated the twins NOW using git-commit + filesystem-mtime + CloudTrail + graph-reachability + live-LastModified:

| Twin | HOT (real) | COLD (deprecate) | heat evidence |
|---|---|---|---|
| smartx_query | `infra/aws/lambda/smartx_query/lambda_function.py` (git 2026-01-04) | `data/smartx/scripts/lambda_smartx_query.py` (git **2025-11-18**, 7mo) | GIT-commit decisive |
| build_transaction_engine | (none — no live non-archive copy) | ALL 3 archive copies (git 2026-02-23) | git + no-live-version → all cold |
| opal_users_v2 TF | `terraform/shared-infra` (dir git **2026-06-29**) | `terraform/portal-auth/dynamodb.tf` (git 2026-04-06) | git-maintenance; **needs `terraform state` confirm of the live owner** |
| bd_exporter TF | `terraform/bd-pipeline` (git 2026-06-29; the live role I co-verified comp-iam) | `ec2/bd-exporter/terraform` (git 2026-04-10) | git + the live role reconciles to bd-pipeline |
| lambda/deprecated | (none) | whole dir (git 2026-02-23 + literally "deprecated") | git + name → dead |
| bd-time-machine lambda | — | **CONFIRMED DEAD (Andrew-direct 2026-06-29: "never used, an idea we wanted to create, never finished")** | heat flagged it (graph-orphan + deployed-04-06-no-activity + 0-invoke), Andrew confirmed = abandoned prototype |

**VALIDATION of the heat approach:** the multi-source heat read flagged bd-time-machine as cold/dead BEFORE Andrew's confirmation; Andrew then ground-truthed it as a never-finished prototype. That is exactly the half-baked-prototype the heat-mapping exists to catch — heat surfaced it, human confirmed it. The remediation for bd-time-machine (lambda + its TF + `snapshots/manifests` consumers) routes to the infra owner (AE) — CVO flags, never deletes; the deploy is live-but-dead, so a clean teardown (like the SCTY.W2 Moltbot pattern) is the move.

**TWO METHODOLOGICAL LESSONS for the heat-mapping build (banked for NFRA_HEATMAP):**
1. **GIT-COMMIT is the code-heat signal, NOT mtime** — both smartx twins show identical `2026-02-20` mtime (a git-CHECKOUT artifact: checkout resets mtime), while git-commit cleanly separates them (2025-11-18 vs 2026-01-04). For git-tracked files use last-commit; reserve mtime for UNtracked/generated artifacts. A heat-map keyed on filesystem mtime would mis-rank every tracked file.
2. **CloudTrail gives DEPLOY-heat (management events) but NOT invoke-heat** — Lambda `Invoke` is a CloudTrail DATA event (off by default), so CloudTrail-Invoke-absence is NOT proof of no-invocation. Combine CloudTrail-management (last deploy/touch) with GRAPH-reachability (0 inbound edges) for the cold verdict — neither alone is definitive. (For real invoke-heat the heat-fed needs CW Invocations metric or enabled data-events, not CloudTrail-management.)
**So the per-layer heat sources are:** code → git-last-commit; infra → git + terraform-state + live-LastModified; cloud-liveness → CW-invocations-metric + graph-reachability (CloudTrail-management only for deploy-heat); data → S3-LastModified/last-access. This is the heat_band recency-source-per-layer the federation must encode.

## FULL 27-THREAD SWEEP (Andrew-direct; debt organized by area, heat-ranked)
Methodical pass over all 27 named threads. **Finding: the deprecated debt is CONCENTRATED — infra-scaffolding + bd-archive/diagnostics + a few dev/test twins; the analytics threads (advi-inf, news, market-overview, macroeconomics, model-portfolios, valuation, correlation, positioning, cma, factor-tilts, attribution, partners, mdpf) are comp-dups-CLEAN** (no EXACT collisions or content-dups; only name-near noise). So the push-cleanup is bounded, not estate-wide.

### INFRA / DEPLOY-TOOLING (highest-value — whole dead trees)
- **`infra/aws/multi-account/terraform/`** — **DEAD NEVER-APPLIED SCAFFOLD** (15 .tf, git 2026-01-03, **0 terraform.tfstate / 0 .terraform** = never deployed). It is the SOURCE of 6/10 TF collisions (step_functions_lambda_invoke prod+staging, lambda.this, log_group.lambda, event_target.lambda) — they "collide" with the live single-account TF only because this scaffold exists on disk. **TIER-1 dead.** The estate is single-account; this multi-account prod/staging scaffold was never stood up.
- **`infra/aws/lambda/deprecated/`** — whole dir, old deploy tooling (git 2026-02-23, named-deprecated). TIER-1.

### advi-bd (the heaviest debt thread)
- `data/black_diamond/archive/**` — build_transaction_engine ×5 (`_GOOD`/`_BAD`/`_v1`/`_v2`), lambda_function ×variants (`_updated`/`_v1_backup`). TIER-1 (archive prototypes).
- `bd-price-update/lambda_function_v1_backup.py` (git 2026-02-24) — TIER-1 backup-of-deployed.
- **`bd-time-machine`** lambda + its TF + `snapshots/manifests` consumers — **CONFIRMED DEAD (Andrew)**. TIER-1 teardown → AE.
- `bd_exporter` TF twin — KEEP terraform/bd-pipeline (hot); DEPRECATE ec2/bd-exporter/terraform (04-10 cold). TIER-2.
- **`E_*` diagnostic gold scripts ×34** (`E_00`..`E_24`+: decompose_aua_gap, diagnose_*, trace_*, dedup_audit, validate_*, audit_*) — edgeless one-off DIAGNOSTICS (no pipeline edges per D1). TIER-3 archival candidates — git-heat each (the recent ones like `E_24.rebuild_fee_scorecard`/`E_19.write_aua_certification` may be semi-prod; the pure trace/diagnose ones are throwaway). Per-script heat-rank before archiving.

### smartx
- `data/smartx/scripts/lambda_smartx_query.py` (git **2025-11-18** cold) — TIER-2 deprecate (dev copy; `infra/aws/lambda/smartx_query/` is the real/deployed).

### security-scanner / seeking-alpha
- `test_seeking_alpha_unauth/lambda_function_simple.py` + `test-seeking-alpha-unauth-simple/` — test-lambda twins (git 2026-01/02, cold). TIER-3 throwaway tests.

### portal-auth / shared-infra
- `opal_users_v2` DDB double-managed — KEEP shared-infra (06-29 hot); DEPRECATE portal-auth/dynamodb.tf (04-06) **after `terraform state` confirms which owns the live table** (auth DDB — confirm before touching). TIER-2.

### Reachability orphans (cross-thread; D1 ledger 06-12, re-verify vs current graph)
- 2 SNS topics, 0 subscribers — TIER-3 REAL. · 6 isolated S3_DATA_KEY · KMS×5 (PENDING) · 1 NEEDS-VERIFY DDB. (LOG_GROUP×190 / SECRET×40 / CW_ALARM×2 = implicit-edge FP, NOT candidates.)

### Push-prep priority
1. **TIER-1 (safe, git-preserved, high-confidence):** multi-account/terraform scaffold + lambda/deprecated dir + bd archive prototypes + bd-time-machine teardown. ~the bulk of the cleanup, low risk.
2. **TIER-2 (twin-consolidation, needs state-confirm):** opal_users_v2 + bd_exporter + smartx dev-copy — pick the cold side per heat, confirm live-owner before removing the TF twin.
3. **TIER-3 (verify-then-archive):** E_* diagnostics (per-script heat), SNS orphans, isolated S3/KMS — re-verify vs current graph first.
**Owner routing:** infra/TF + lambda teardowns → AE; bd data-scripts (E_*/archive) → DS; CVO flags + heat-ranks, never deletes.

## TIER-2/3 VERIFICATION (Andrew-direct 2026-06-29 "verify all of that"; CONFIRMED effectively deprecated)
Grounded against live AWS (CW Invocations = the real invoke-heat; SNS subscriptions; git-heat):
- **smartx_query (BOTH copies dead — sharper than the earlier "dev-copy only"):** there is NO deployed `smartx_query` lambda in the live estate. The smartx PIPELINE is LIVE + healthy (smartx-ec2-autostart 45inv/90d, smartx-rest-pull 45, smartx-jwt-refresher 45, smartx-model-monthly-pull 13, opal-smartx-ingestion-pipeline 74) — but NONE is `smartx_query`. So both `infra/aws/lambda/smartx_query/lambda_function.py` AND `data/smartx/scripts/lambda_smartx_query.py` are dead prototype code for a function never (or no-longer) deployed. **CONFIRMED dead — both copies archive.** (The broader smartx thread is healthy; only smartx_query is dead.)
- **3 SNS topics, 0 confirmed subscriptions** (D1 said 2; found 3): `astn-wsjft-alerts`, `trade-pipeline-ses-bounces`, `trade-pipeline-ses-complaints` — nothing receives them = dead/orphaned. **CONFIRMED candidates** (caveat: confirm SES isn't configured to emit to the bounce/complaint pair before removing — a 0-sub SES topic is inert but check the SES config).
- **34 E_* diagnostics:** a SINGLE late-April batch (all git-committed 2026-04-27 → 2026-05-01, cold since), edgeless one-offs from the AUA-gap/fee-scorecard investigation. **CONFIRMED deprecated batch** — archive (a couple like E_19.write_aua_certification / E_24.rebuild_fee_scorecard may have produced a kept artifact; the trace_/diagnose_/audit_ ones are pure throwaway). DS lane.
- **REMAINING (not yet re-verified):** 6 isolated S3_DATA_KEY + KMS×5 — need a current-graph re-verify (D1 is 06-12); deferred.
**Verdict:** Andrew's "all effectively deprecated" CONFIRMED for smartx_query (both) + 3 SNS + 34 E_*. Routing: smartx_query + E_* → DS (data lane); SNS topics → AE~A (cloud, fold into the teardown dispatch). The whole-pipeline check distinguished the dead function (smartx_query) from the live smartx pipeline -- the heat verify is what separated them.

## grounding: field (Rule 22)
- "infra/aws/lambda/deprecated is dead tooling" — SOURCE-CONFIRMED (the dir contents + comp-dups INFERRED_DEAD flag); the INFERRED_DEAD is comp-dups's own advisory (graph-pending), so it's a candidate not a verdict.
- "heat is the real-vs-dup discriminator" — INFERRED (design): heat_band-as-discriminator is the NFRA_HEATMAP thesis; the federation that computes it is IN-BUILD (not yet live), so the heat-ranking is manual today.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-dups | full estate scan | 10 TF EXACT collisions, 1208 name-near, 3207 content-bodies scanned, content-dup archive set surfaced |
| (read) NFRA_DEBTSCAN D1 ledger | reachability orphans | 259 isolated nodes (most FP-classified); 2 SNS + bd-time-machine = REAL |
| comp-which | routed the intent | → comp-dups (the canonical debt/dup tool) |

— 3.0.0_SA_CVO
