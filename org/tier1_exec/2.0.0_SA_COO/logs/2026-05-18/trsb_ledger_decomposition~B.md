# Session — TRSB_LEDGER PRD v0.1 Decomposition (COO ~B lane)

**Date:** 2026-05-18
**Author:** 2.0.0_SA_COO~B
**Project:** TRSB_LEDGER (Trade Submission: Executor Authorization Enforcement + Audit-Trail Integrity)

---

## Executive Summary

COO ~B lane booted this session and paired with CTO~B for two projects: **TRSB_LEDGER** (primary — decomposed this log) and **ADHC_VALGATE** (secondary — inherited pre-decomposed, parked on shared-pod capacity).

Startup arc:
1. Booted COO ~B; base `2.0.0_SA_COO` is LIVE driving MDPF_ASSETS + the INF gold-chain cluster. Negotiated a clean lane split — a stale first proposal crossed in flight with Andrew's override and produced a transient divergence (base COO "CONFIRMED" the wrong split); corrected immediately with an explicit CORRECTION message. Base COO absorbed it; no orphan risk — base owns MDPF + INF, ~B owns TRSB_LEDGER + VALGATE.
2. Received TRSB_LEDGER PRD v0.1 handoff from CTO~B (commit `7946fb8d9`). Andrew direct: TRSB_LEDGER routes through COO~B only, not base.
3. Decomposed PRD §6 (9 TO candidates) into **10 TOs**, with **TO-7 dropped** per Andrew's Q4 deferral.

## Rulings collected before authoring

| Q | Source | Ruling |
|---|--------|--------|
| Q1 — `role` field disposition | CTO~B | Demote, do NOT remove. `role` stays a display + dev-segregation-bypass attribute; `groups` is canonical for authz. |
| Q2 — `COMPLETE` status | Andrew | RETIRE `COMPLETE`. `EXECUTED` is the durable terminal state. The back-office handoff IS the last step — no manual "settled" close. |
| Q3 — `audit_events` storage | CTO~B | Embedded list on the submission item for v0.1. Atomicity with the status update is decisive. Separate table = documented scale-up path, not v1. |
| Q4 — `trade-users` mgmt form | Andrew | DEFERRED — "I can control this in the meantime directly." → **TO-7 dropped this round.** |
| TO-8 surfacing mechanism | CTO~B | Dedicated `/api/general/trades/users/me` endpoint, NOT a JWT claim (claim pollutes portal-wide token, forces hot-path cross-read, stale 8-12min). |
| Q5 — identity-enforcement depth | (deferred) | Adjudicated by CTO~B once TO-0 reports — wired as the TO-2 escalation fork. |

## Decomposition decisions

- **4 separate backend TOs kept (not merged 2×2)** — each has a distinct machine-checkable acceptance test; merging would muddy acceptance. CTO~B approved.
- **Backend lane = single agent (AE 0.7.0), serial.** TO-1..TO-5 + TO-8 all edit `workflow_handler.py` / `submission_handler.py` / `dashboard_api.py`. Splitting across agents is false parallelism + merge contention (CTO~B). The lane serializes regardless of agent count.
- **TO-5 lane correction.** PRD §6 named AE 0.5.0 for TO-5 as a "Terraform-only, no Lambda-source overlap" TO. That is incorrect — TO-5 edits `workflow_handler.py` (write `decided_at` on approve+reject) AND `dashboard_api.py` (GSI read repoint) AND `dynamodb.tf`. Reassigned TO-5 to the AE 0.7.0 serial lane. Only **TO-6** (pure `dynamodb.tf` table attrs) is the genuine concurrent infra TO → AE 0.5.0. Flagged to CTO~B.
- **TO-8 split into backend + portal.** TO-8 (AE 0.7.0) = the `/users/me` endpoint; TO-8b (RD 0.3.2) = the portal role-aware gating that consumes it. RD cannot author backend Lambda, so the split is structural.
- **Q2 `COMPLETE` retirement spans two TOs.** Backend enum retirement = TO-4 (AE). FE `completeSubmission` orphan removal = TO-8b (RD). Legacy `COMPLETE` rows are NOT migrated — the FE must tolerate them on read (encoded in both TOs).

## Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.000.ae-identity-seeding-probe.md | TO-0: identity/seeding probe — authorizer claims + trade-users `groups` population. Read-only brief. pending (GO). |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.001.ae-group-auth-enforcement.md | TO-1: group-based authz enforcement in workflow_handler.py (closes A1). pending (GO). |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.002.ae-actor-identity-binding.md | TO-2: JWT-authorizer actor binding (closes A5); §7-Q5 fork escalates to CTO~B if TO-0 finds no usable identity. pending (GO), dep TO-0. |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.003.ae-append-only-audit-events.md | TO-3: embedded append-only audit_events incl. EXECUTION_FAILED before revert (closes B1/B3/B7). pending (GO). |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.004.ae-compliance-json-snapshot-status-model.md | TO-4: compliance JSON snapshot + EXECUTED-rests + retire COMPLETE backend (closes B2/B4). pending (GO). |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.005.ae-by-approver-gsi-repoint.md | TO-5: by-approver GSI repoint via planned create/backfill/cutover/drop (closes B5, R3 highest-care). pending (GO). |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.008.ae-trade-groups-me-endpoint.md | TO-8: dedicated /api/general/trades/users/me endpoint. pending (GO). |
| 0.7.0_AE_CloudOps | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.009.ae-resubmission-lineage.md | TO-9: resubmission lineage (closes B6). STAGED — droppable stretch. |
| 0.5.0_AE_OpalETL | org/tier2_senior/0.5.0_AE_OpalETL/task_orders/TRSB_LEDGER.006.ae-dynamodb-durability.md | TO-6: PITR + deletion_protection on trade_submissions + trade_users (closes B8). pending (GO), concurrent. |
| 0.3.2_RD_TradeSubmission | org/tier3_junior/0.3.2_RD_TradeSubmission/task_orders/TRSB_LEDGER.008b.rd-portal-role-aware-gating.md | TO-8b: portal role-aware tab gating + completeSubmission removal (closes A4). STAGED, gated on TO-8. |

Execution dependencies:

```
AE 0.7.0 serial lane:  TO-0 -> TO-1 -> TO-2 -> TO-3 -> TO-4 -> TO-5 -> TO-8   (one file family; serializes)
                         |                                                     -> TO-9 (staged stretch)
                         +-- TO-2 hard-gates on TO-0's authorizer finding (satisfied in-lane)
AE 0.5.0 concurrent:   TO-6  (pure dynamodb.tf — runs alongside the AE 0.7.0 lane)
RD 0.3.2 portal:       TO-8b  (staged — GO fires when TO-8 ships)

Cross-file: TO-5 + TO-6 both edit dynamodb.tf — different stanzas; cross_domain_coordination
            blocks in both mandate MCP-sync before commit (TO-6 recommended to land first).
```

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| comp-blast / comp-iam / comp-routes on trade-* | NOT re-run | The trade pipeline is uninstrumented in the comp graph — CTO~B already ran all three at PRD authoring (PRD §5: comp-blast "no downstream consumers", comp-iam "no service matching", comp-routes empty). Re-running reproduces the same empty output; PRD §5 is the authoritative documented evidence. IAM adequacy verified by direct `iam.tf` read (PRD §2.C). |
| Direct source-path verification | 5/5 paths confirmed | Globbed and confirmed every file path the TOs reference: `workflow_handler.py`, `submission_handler.py`, `dashboard_api.py` under `infra/aws/lambda/trade-pipeline/`; `dynamodb.tf`/`iam.tf`/`apigateway.tf` under `infra/aws/terraform/trade-pipeline/`; `portal/src/pages/TradeSubmission/`. No TO references a non-existent path. |
| Portal comp tools (comp-transform schema-check, comp-cache collisions) | Mandated in TO-8b | The portal IS in the comp graph; TO-8b carries `comp-transform schema-check TradeSubmission` + `comp-cache collisions` as Phase-1 mandates for the RD agent (new trade-permissions query key). COO does not pre-run these — the TO carries them. |

Per-TO `<compiler_tools_mandate>` blocks: every TO carries the three-phase structure. For the uninstrumented backend TOs, the Phase-1 check is a direct `iam.tf` read with `<expect>`/`<if_mismatch>` (the sanctioned substitute per PRD §5); Phase-3 checks are deployed-Lambda empirical smokes. TO-8b carries the real portal comp-tool runs.

## Open Items at Log Close

1. **GO dispatch** — sequence-GO to AE 0.7.0 (TO-0→TO-1→TO-2→TO-3→TO-4→TO-5→TO-8) + GO to AE 0.5.0 (TO-6). TO-8b + TO-9 staged.
2. **TO-2 §7-Q5 fork** — open until TO-0's probe reports. If the trade authorizer carries no usable identity, TO-2 escalates to CTO~B for re-scope.
3. **AE 0.7.0 capacity** — AE 0.7.0 is mid chain-#2 monitoring (base-COO INF lane) until ~17:30Z; TRSB backend queues behind that. TRSB backend is not same-hour urgent (CTO~B).
4. **ADHC_VALGATE** (secondary project) — inherited pre-decomposed (8 TOs staged/dispatch_held by base COO). No authoring. Dispatch gated on (a) DS0.4/DE0.4/AE0.7 shared-pod capacity freeing and (b) lane-timing sync with base COO. Parked until TRSB dispatch is out.

— 2.0.0_SA_COO~B
