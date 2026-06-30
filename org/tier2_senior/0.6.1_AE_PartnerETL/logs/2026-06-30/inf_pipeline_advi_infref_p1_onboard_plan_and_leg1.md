# ADVI_INFREF P1 — inf-AE onboard, plan arch-gate, Leg-1 landed (gold two-flow)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, IMPLEMENT, DEPLOY, TRACE
**Agent:** 0.6.1_AE_PartnerETL (inf-refactor AE lane)
**Date:** 2026-06-30
**Assignment:** ADVI_INFREF P1 (COO onboard 20260630T173401Z, Andrew-direct; CTO brief 20260629 inf-AUA-frozen)
**Status:** Leg-1 GREEN (CTO-accepted). Leg-2 scoped + de-risked, joint-sequenced with DS~A, awaiting ~A's cataloged dim-list.

---

## Summary

Spawned as the Inflection AE lane (0.6.N firm-map: 0.6.1=inf). Completed XXX.md startup + reachability, oriented across the ADVI_INFREF refactor (PRD + SPEC-1 bronze + SPEC-4 runtime + COO decomp), authored the P1-infra PLAN, got it CTO arch-gated, and LANDED Leg-1 (the EventBridge two-flow) end-to-end with full deploy discipline. Leg-2 (the keystone single-pull-stage + 4-dim de-convert) is scoped, de-risked, and joint-sequenced with DS~A; the build is gated on ~A's cataloged dim-list + ~A authoring the pull-stage module (their script lane).

## Context — the P1 mandate

The recurring inf nightly freeze is the gold chain's REDUNDANT inline perf re-pull (`pull_inflection_performance_rest.py`) hanging on the Orion perf endpoint (103/41min) before B_00 under `set -e` (source-confirmed `9ea447b3a`). Tactical fix is LIVE (timeout-tolerate on every INF_API_PULL_*, served VERIFIED restored 17:20Z). **P1 = the DURABLE structural fix:** a single timeout-guarded pull per dim on `inf_gold_layer_runner` EC2 (no redundant second pull left to hang the chain) + EventBridge two-flow trigger composition. AE owns the EC2/runner/EventBridge/IAM infra; DS~A owns the pull/silver/gold scripts + chain composition.

## What I did

1. **Startup + reachability:** register, persistent inbox Monitor (bvfqc6gum), serial file, hooks, comp-context.
2. **Orientation (TRACE):** PRD §1/§4/§5, SPEC-1 §2/§3/§5 (bronze), SPEC-4 §1/§5 (runtime), COO decomp brief; grounded the current architecture (orion-gold-dispatch.sh CATALOG + CHAIN_FULL interleaved INF_API_PULL_*, the `9ea447b3a` run_script timeout-tolerate, the 9 cron pull λ, the inf-gold-trigger single-dispatcher + inf-canonical-prices-daily {mode:full} cron).
3. **P1-infra PLAN** (`bd9604ead` + addendum `12f91f4f1`): single-pull-layer EC2 design + two-flow EventBridge + never-widen IAM + honesty-fix fold + lane boundary. **CTO ARCH-GATED** — open question ruled FRONT-OF-CHAIN with a clean PULL/COMPUTE module-boundary condition; the 4-dim de-convert made binding ATOMIC-PER-DIM + parity-checked, jointly sequenced with ~A.
4. **Leg-1 LANDED (IMPLEMENT/DEPLOY) — gold two-flow, parity-neutral:**
   - Grounded that inf-gold-trigger ALREADY supports `incremental` (VALID_MODES + _MODE_TTL_SECONDS["incremental"]=900 + handler L263 mode->`--chain incremental`) ⇒ NO Lambda code change; Leg-1 is purely the missing EventBridge half.
   - Added a WIRED-NOT-ARMED (state=DISABLED) `inf-gold-incremental-daily` rule -> inf-gold-trigger {mode:incremental} + target (same DLQ + retry(0) anti-storm) + lambda_permission; extended the DLQ queue policy ArnEquals to both flow rule ARNs. Full nightly UNCHANGED. Commit `5816a4f36`.
   - Deploy per CTO's 3 conditions: saved-plan flow (plan -out=tfplan.leg1 -> 3 add/1 chg/0 destroy) -> safe-apply HALTGT (Apply complete! 3 added, 1 changed, 0 destroyed) -> LIVE verify `aws events describe-rule` State=DISABLED (Rule 22) -> 0-diff re-plan "No changes" -> CHANGELOG inf-pipeline-v1.7.77 (`629ac3856`) -> tag inf-pipeline-v1.7.77 pushed --follow-tags -> deploy-completion ledger opened (20260630T1748Z) + CLOSED all-3-legs-proven (`1769b7d9c`). NEVER half-landed. **CTO ACCEPTED GREEN.**

## Leg-2 scoping + de-risk (joint with DS~A)

- **De-convert ORDER (CTO-endorsed):** perf+txn (CSV pattern-setters, mostly dropping the inline-parquet double-write) FIRST -> assets -> positions/AUA LAST (the served-AUA source + now the yahoo-removal price source for all 4 gold consumers — doubly load-bearing; tightest parity, served AUA == Orion to the cent).
- **Atomic-per-dim (binding arch-gate):** each dim's bronze->raw-JSON flip + ~A's silver-converter repoint in ONE step, silver byte-parity before/after; RAVC CTO per-dim, CTO co-signs before the next.
- **INFRA de-risked (read-only grounding):**
  - EC2: `inf_gold_layer_runner` = c6a.4xlarge (16 vCPU/32GB), 200GB gp3 root — AMPLE for the small-book raw surface; no resize likely (confirm vs dim-list).
  - IAM: runner role `inf-gold-layer-ec2-role` already wildcard-covers `opal-data-inf/*` (all new bronze prefixes need NO S3 add) + already has GetSecretValue on `orion/jwt/current-*` (Orion JWT; also read from the S3-mirror). **The ONLY never-widen ADD for Leg-2 = GetSecretValue on `orion/eclipse_jwt/current-*`**, needed solely when the Eclipse pull moves onto the runner (R5) — sequenced WITH that step. inf-exporter holds PutSecretValue on the JWT (producer); runner reads (consumer) — isolation boundary clean.
- **3 cron-only dims confirmed (~A):** tax (unrealized+realized), billing, unified_account_dim move onto the EC2 pull-stage.
- **GATING:** ~A is compiling the full cataloged dim-list (INFLEC_API_ENDPOINTS_CATALOG + D3 S1/S2/S3 — richer than today's 9; adds Trading/Models, Custom Reports, per-client Assets snapshot) and will author the pull-stage module; CTO sanity-checks the surface.

## Lane / scope notes

- inf-exporter KEPT ISOLATED (R-Point 3 — NOT folded); persistent-login directive FLAGGED for the P4 CTO+CVO loop, NOT designed into P1.
- P3 decommission (9 cron λ + bronze-runner + stubs + qa-runner) NOT touched — crons STAY LIVE for parallel-parity; P3 only after the parity gate, never-widen.
- Yahoo repoint gated on ~A's EG-2 per-consumer edge-check.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| Read (PRD/SPEC-1/SPEC-4/decomp/dispatch.sh/lambda/iam.tf/eventbridge.tf) | orient + ground current arch (native Read = free per COMPRAIL) | grounded the freeze locus, trigger arch, IAM baseline |
| `aws events describe-rule` | LIVE verify rule State=DISABLED (Rule 22 ground-truth, parity guarantee) | State:DISABLED confirmed |
| `terraform plan/safe-apply` | saved-plan 3/1/0 -> apply -> 0-diff re-plan | clean, no foreign drift |
| `.tools/deploy_ledger.py open/close-leg/close` | deploy-completion ledger (never half-land) | opened + all-3-legs-proven + closed |
| `comp-iam` (NOT run yet) | deferred to Leg-2 apply-time per CTO (live get-role-policy ground-truth once dim-list fixes the surface) | the grep-based IAM baseline above is the pre-check; comp-iam service/gaps + live get-role-policy at Leg-2 build |

Note: comp-pipescript/comp-* deferred this session — the work was infra (EventBridge/IAM TF + Lambda mode grounding), not a gold-script edit/run; the IAM grounding used direct iam.tf reads + a live describe-rule (Rule 22). comp-iam service/gaps will run at Leg-2 apply-time against the live runner role once ~A's dim-list fixes the surface (per CTO arch-gate).

## Next (event-driven)

Awaiting ~A's cataloged dim-list (sizes EC2/IAM; CTO surface sanity-check) + ~A authoring the pull-stage module. On arrival: confirm EC2/IAM sizing, then build the per-dim de-convert legs (atomic + parity), RAVC CTO each. Broker status kept accurate for COO /drive.
