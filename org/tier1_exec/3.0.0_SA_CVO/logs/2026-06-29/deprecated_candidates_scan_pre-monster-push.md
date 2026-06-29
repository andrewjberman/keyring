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
