# 0.6.0_AE_PartnerETL DEPLOY LOG — 2026-06-08 (MDPF_CADENCE convergence-gate, mdpf-pipeline-v1.2.0)

**archetype:** DEPLOY · **secondary:** IMPLEMENT, COORDINATE

COO-assigned (151054Z, freeing 0.7.0 for the CMPAWS sovereign goal). CTO design ruling (151508Z + precondition-confirm 151741Z + counter/constraint confirms). Replaces the MDPF weekday cron with an event-driven convergence gate. Apply held until COO post-MDPF_COUNTS-close GO (154048Z, Andrew sovereign waived the 15:55Z gate via MDPF_COUNTS close 1318ec306).

## What changed
The `mdpf-daily-refresh-trigger` EventBridge rule fired `cron(0 15 ? * MON-FRI *)` — a WEEKDAY cron that missed the Sat T+1 INF reconciliation (the root-cause bug). Now it fires on the **INF spine sentinel ObjectCreated** (`opal-data-inf/gold/meta/pipeline-complete.json`, daily incl weekends), and the `mdpf-daily-trigger` Lambda applies a **per-source-vintage freshness precondition** before dispatch:
- **INF spine:** daily-incl-weekend calendar (sentinel just fired -> ~always fresh).
- **BD silver (49F):** weekday-Path-A calendar — fresh iff latest `silver/{allocations,fees}` partition is <= BD_MAX_LAG_TRADING_DAYS (=2, DS-confirmed) trading days behind the expected last trading day. **NOT date-equality with INF** — the load-bearing constraint (CTO+DS): naive equality false-defers every weekend = reintroduces the weekday-only bug at the gate.
- BD-stale -> DEFER (no dispatch); the existing mdpf-freshness-checker alarm catches an unresolved defer. v1 = defer+alarm, NO auto-recheck (COO YAGNI ruling).

Output contract UNCHANGED (only WHEN fires; mdpf_aggregate_aua + the MDPF_COUNTS-validated artifact untouched).

## Deployment Sequence
| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source + TF + source-map | `025c31ff3` feat(MDPF_CADENCE) [ready-to-apply]; +`851ca4977` (DS-confirmed MAX_LAG comments) |
| 2 | build-and-upload.sh mdpf-pipeline mdpf-daily-trigger | SHA256: `MG+190tDiM4DNlNNoA2yeHfYQxza7EtvfAOscBm3r0w=` |
| 3 | Commit source map | `bcde60bf1` ci: upload artifact + sha [skip ci] |
| 4 | terraform plan | 0 add / 4 change IN-PLACE / 0 destroy (rule cron->event_pattern same ARN; target; iam; Lambda source_code_hash+timeout/env) |
| 5 | safe-apply (HALTGT) | HALTGT passed silently (empty inbox); Apply complete — 0 added / 4 changed / 0 destroyed |
| 6 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 7 | record-terraform-deploy + CHANGELOG | `fe5ab37e8` ci: record deploy [skip ci] |
| 8 | Tag + push | `mdpf-pipeline-v1.2.0` pushed --follow-tags |
| 9 | CVO eventing-oracle re-cert | PINGED 154454Z (property delta on the in-place rule swap) |

## Verification (live, clean shell)
- `aws events describe-rule mdpf-daily-refresh-trigger`: state=ENABLED, **schedule=null** (cron gone -> S3-ObjectCreated active).
- `aws lambda get-function-configuration mdpf-daily-trigger`: **timeout=360**, **GATE_ENFORCE=1**, **BD_MAX_LAG_TRADING_DAYS=2**.
- terraform validate PASS; comp-iam service mdpf-daily-trigger PASS (s3:GetObject GRANTED for INF sentinel + BD silver; ListBucket granted explicitly — comp-iam paginator blind spot).

## Deployment Tags
| Pipeline | Tag | Commit |
|----------|-----|--------|
| mdpf-pipeline | mdpf-pipeline-v1.2.0 | fe5ab37e8 |

## No-run-today (expected) + Next Steps
- Today's INF sentinel already fired 14:31Z (before the rule existed) + the 15:00Z cron already ran -> NO double-run today. **First real gate fire = TOMORROW's ~10:21Z INF sentinel** (+ the Sat reconciliation).
- **[0.6.0 tomorrow]** Verify the first real gate fire: BD fresh -> dispatched + rollup advanced, OR correctly deferred on a real BD stale (then defer logged + freshness alarm). Confirm the Sat reconciliation fires the gate (the whole point of the fix).
- **[CVO]** eventing-oracle re-cert (pinged).
- **[COO]** flip MDPF_CADENCE project state (registry lane).
- Optional future: post-18:03Z gate timing for 1-day BD slack (DS-routed; NOT folded — pre-write ~10:21Z is intended per Andrew "both at 10a" INF-sync). Auto-recheck only if defers prove frequent.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| comp-iam service mdpf-daily-trigger | PASS (5 ops GRANTED) | confirmed the new INF-sentinel + BD-silver reads before apply; ListBucket granted explicitly (paginator not auto-detected) |
| ds-commit-gate.sh (lambda_function.py) | PASS | py_compile + ds-precommit + ruff; pure ASCII; from __future__ import annotations |
| terraform validate / plan / 0-diff | PASS / 4-in-place / No-changes | in-place swap (ARN preserved -> DLQ+permission+CVO node coherent) |
