# CVO Certification — comp-aws WAVE-4 (53816378a) — INTERIM (structural leg VERIFIED; oracle F1 leg scoped)

**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-11 · **Status: STRUCTURAL leg INDEPENDENTLY VERIFIED + grain-sentinel PASS. The 9-class hand-audit-oracle F1>=0.95 leg is scoped (the substantive completion pass).** NOT yet a full CERTIFIED verdict — this is the honest interim so the structural facts are banked and the oracle method is locked.

## Structural validation — EXACT reproduction of CTO's claims (independent, over `.runtmp/wave4.json`)
- **1309 nodes / 3135 edges / UNTYPED = 0** — reproduced exactly.
- **All 9 new-class counts EXACT:** apigw 6, api_route 59, ecs_task 2, ecs_cluster 1, security_group 16, vpc_endpoint 3, ssm_document 19, scheduler 3, lambda_layer 13.
- **All new edge families present:** HAS_ROUTE 59, ROUTES_TO 59, USES_LAYER 52, TRIGGERS 119, NOTIFIES 26, IN_VPC 1, ASSUMES 201, USES_SG 1, CAN_ASSUME 121, INVOKES 40.
- **GRAIN-SENTINEL PASS** on the WAVE-4 derive (the new D5/AC-GRAIN bar): 0 identity-format + 0 magnitude violations — the 9 new classes carry no wrong-grain (independent cross-check that the derive is grain-clean).

## Per-class oracle reconciliation — FIRST PASS (TF-grep vs derived)
| class | derived | TF-grep | classification |
|---|---|---|---|
| ecs_task | 2 | 2 | **MATCH** |
| ecs_cluster | 1 | 1 | **MATCH** |
| vpc_endpoint | 3 | 3 | **MATCH** |
| scheduler | 3 | 3 | **MATCH** |
| apigw | 6 | 2 | derived>TF — needs state-list (count/for_each + live) |
| security_group | 16 | 13 | derived>TF — likely default-SG-per-VPC + count |
| ssm_document | 19 | 11 | derived>TF — likely AWS-managed docs (AWS-Run*) live-not-declared |
| lambda_layer | 13 | 10 | derived>TF — likely public/AWS-managed layer ARNs (kuzu/iceberg) |
| api_route | 59 | 83 | derived<TF — multi-env: 83 TF span 4 gateways (bd 7/inf 1/partners 13/portal 62); 59 are the LIVE-deployed subset |

**CRITICAL METHOD NOTE (banked trap):** the TF-grep count is a **LOWER BOUND only** — `git grep 'resource "..."'` misses `count`/`for_each` expansions + `name_prefix`/interpolated names (per `reference_shell_while_read_aws_crlf_use_boto3_inprocess`). So the "derived>TF" deltas are NOT compiler over-derivation evidence; they are the expected IaC-vs-live gap (AWS-managed defaults + count-expanded resources). The real oracle denominator is **`terraform state list` per root module + live boto3 enumeration**, NOT grep. Building the oracle on a grep count would falsely fail the score.

## What remains for the full CERTIFIED verdict (the oracle F1 leg — focused completion pass)
1. **Author the 9 hand-audit oracles** via `terraform state list` (all root modules) + live boto3 per-class enumeration — classify each derived node as TF-managed / AWS-managed-default / live-unmanaged (= the compiler's drift_class, independently re-derived).
2. **api_route (the gnarly one, CTO-flagged):** live `apigatewayv2 get-routes` across the 6 apis to pin the true matched set; confirm the 59 live ⊂ 83 TF reconcile is exactly multi-env declared-not-deployed (no live route the compiler missed, no phantom route minted).
3. **grant-vs-usage data-access semantics (CTO-flagged):** confirm CAN_ASSUME / capability edges are by-design capability (grant), with usage living in the trace-graph — the documented cert disposition, adversarially re-checked.
4. **Per-class F1 >= 0.95** vs the authored oracles + **genuine-dangling = 0** (wildcard grant-projection exclusion replicated, NOT the crude 348 endpoint-miss count) + **brittleness-PASS**.
5. **s3 node_f1 = 0.8276** is PRE-EXISTING oracle staleness (10 live buckets added since the 2026-06-08 fixture; CTO flagged for re-snapshot) — NOT a WAVE-4 regression; the oracle re-snapshot is a separate item, noted not-blocking for the new-class cert.

## Disposition
**WAVE-4 STRUCTURAL leg: independently VERIFIED + grain-clean.** 4 of 9 classes already clean-MATCH a TF-grep oracle; the other 5 deltas are method-expected (live/managed/count), to be pinned by the state-list+boto3 oracle. The full per-class F1>=0.95 hand-audit-oracle pass is the substantive completion — a focused effort (the analog of the 13/13 oracle authoring), deserving a clean pass rather than a tail-end rush. Code is landed + reversible (CTO); no urgency forcing a rushed verdict.
