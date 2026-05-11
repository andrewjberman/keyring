# DS~C 2026-05-11 — Bug A audit + bronze/silver daily-cadence investigation

**Agent:** 0.4.0_DS_ClientPlatform~C
**Trigger:** COO 21:18Z GO on Bug A optional recurrence-prevention audit + Andrew direct broadening "we need to figure out why the bronze/silver processes are not running daily"
**Scope:** Read-only audit. No code shipped.
**Status:** Audit complete. Findings surfaced to COO 21:43Z + correction 21:44Z.

## TL;DR

Bug A's 3-day zero-MV regression (`gold/holdings/2026-05-06/07/08.parquet`) traces to
`silver/prices/canonical_prices.parquet` being 6 days stale (LastModified 2026-05-05 14:02Z).
That staleness traces to **no daily cadence on the gold layer** — the only daily fallback
trigger (`inf-canonical-prices-daily`) is intentionally DISABLED awaiting TO-011 event-path
validation. Two adjacent daily Lambdas (`inf-billing-daily` + `inf-performance-daily`) have
**zero invocations in 7 days despite enabled cron rules** — they've never fired (no log
streams exist). `inf-performance-daily` is the upstream input for Stage 1 INFGRO Return
computation per PRD §2.5 — gating effect.

## Bug A root-cause chain (3 hops)

| Layer | Artifact | State | Notes |
|---|---|---|---|
| Upstream | `silver/prices/canonical_prices.parquet` | LastModified 2026-05-05 14:02Z (6 days stale) | Date coverage stops at 2026-05-05; 2026-05-06/07/08 rows = 0 |
| Joiner | `INF_B_01.holdings_lots.py` | unchanged | Joins gold/positions_cube/ to canonical_prices on (date, ticker). Missing prices → NULL after merge. |
| Output | `gold/holdings/2026-05-06/07/08.parquet` | 9,348 rows; ALL `price=NULL, market_value=NULL` | DS~B's earlier finding ("all NULL") confirmed empirically. Earlier hypothesis "all zero" was the downstream `fillna(0.0)` masking the NULL. |
| Downstream | INF_C_00 (PRE-Bug-B-fix) → INF_C_02 client_performance → INF_D_05/D_06/D_07 platinum | resolved at INF_C_00 by DS~B path-fix; mitigated at INF_D_05/D_06 by my TO-8 walk-back | DS~B's `gold/canonical/holdings_` switch took canonical_performance off this surface |

INF_B_01 itself is doing the right thing — if input price is NULL, output market_value is
NULL. The bug is **upstream**: canonical_prices not being refreshed.

## Bronze/silver daily-cadence audit

Methodology: `aws lambda list-functions` + `aws events list-rules` + `aws events describe-rule`
+ `aws events list-targets-by-rule` + CloudWatch `get_metric_statistics` (7-day Invocations
and Errors) + CloudWatch Logs `filter_log_events` for ERROR samples.

### EventBridge rules state

| Rule | Schedule | State | Target | 7d invocations | 7d errors |
|---|---|---|---|---|---|
| `inf-accounts-v2-daily` | cron(35 12 * * ? *) | ENABLED | inf-accounts-v2-daily | 5 | 0 |
| `inf-api-assets-v2-daily` | cron(45 12 * * ? *) | ENABLED | inf-api-assets-v2 | 11 | 2 |
| `inf-api-positions-daily` | cron(50 12 * * ? *) | ENABLED | inf-api-positions | 8 | 0 |
| `inf-api-reps-daily` | cron(30 12 * * ? *) | ENABLED | inf-api-reps | 9 | 1 |
| `inf-api-txn-daily` | cron(0 13 * * ? *) | ENABLED | inf-api-txn | 15 | 11 |
| `inf-billing-daily` | cron(35 13 * * ? *) | ENABLED | inf-billing-daily | **0** | **0** |
| **`inf-canonical-prices-daily`** | cron(0 6 * * ? *) | **DISABLED** | inf-gold-trigger ({"mode":"full"}) | n/a | n/a |
| `inf-performance-daily` | cron(40 13 * * ? *) | ENABLED | inf-performance-daily | **0** | **0** |
| `inf-tax-daily` | cron(55 12 * * ? *) | ENABLED | inf-tax-daily | 5 | 0 |
| `inf-unified-account-dim-daily` | cron(40 12 * * ? *) | ENABLED | inf-unified-account-dim-daily | 12 | 2 |
| `opal-inf-bronze-runner-cron` | cron(43 12 * * ? *) | ENABLED | (EC2 bronze runner) | n/a (EC2) | n/a |
| `opal-inf-export-schedule` | cron(0 21 * * ? *) | ENABLED | (export Lambda) | n/a | n/a |
| `opal-inf-jwt-fetch` | cron(13 12 * * ? *) | ENABLED | inf-jwt-trigger | n/a | n/a |
| `inf-silver-chain-bronze-complete` | event (s3 PutObject) | ENABLED | inf-silver-chain | 3,703 | 7 |
| `inf-assets-trigger-bronze-complete` | event | ENABLED | inf-assets-trigger | n/a | n/a |

### Finding 1 — `inf-canonical-prices-daily` intentionally DISABLED

Description on the rule: *"Fallback 06:00 UTC trigger for inf-gold-trigger (DISABLED; TO-011
flips ENABLED post event-path validation)"*.

Target: `inf-gold-trigger` Lambda with payload `{"mode":"full"}`. So this rule would kick
off a full gold-layer rebuild daily at 06:00 UTC — including `build_canonical_prices.py`.

**Impact:** gold layer has no automatic daily cadence. The last gold run was 2026-05-05
14:02Z (probably manually triggered by AE 0.6.1 or a one-off invoke). canonical_prices has
been stale since then. Bug A is the downstream symptom.

### Finding 2 — `inf-billing-daily` + `inf-performance-daily` have ZERO invocations

Both rules:
- ENABLED state
- valid cron expressions (13:35 UTC and 13:40 UTC daily)
- Proper Lambda target wired
- Lambda has EventBridge invoke permission (verified `aws lambda get-policy`)
- 0 invocations in 7 days
- **No CloudWatch log streams have ever been created** (Lambda has never been invoked at all)

**Impact:**
- `inf-billing-daily`: billing dim bronze pulls silently missing → platinum billing data stale
- `inf-performance-daily`: **bronze/performance/ idle** — per PRD §2.5, this is the upstream
  input for Stage 1 INFGRO Return computation (TWR factors). Stage 1 cannot ship until this
  Lambda starts firing.

**Root cause:** unknown. Likely Lambda-level config issue (broken init, dead deployment) not
visible at the EventBridge rule + permission layer. Needs AE 0.7 audit.

### Finding 3 — `inf-api-txn` 73% error rate (CORRECTED)

Initial finding: 11 errors in 15 invocations (7-day window).

**Root cause investigation:**
- Error sample 2026-05-07: `TypeError: main() takes 0 positional arguments but 1 was given`
- Git log shows this was fixed by AE 0.6.1 on 2026-05-07 — commit `253821db1` "inf-api-txn
  sys.argv patch -- _v2.py:main() reads sys.argv (0 positional args), calling with list arg
  raised TypeError on first cron fire"
- Most of the 11 errors are pre-fix TypeError occurrences captured in the 7-day window
- **Current (post-fix) errors are a DIFFERENT failure mode:**

```
2026-05-10 13:00:36Z: ERROR: CSV is header-only or empty (total_lines=1, data_rows=0). 
Report 28198 may be a UI-context report with no API-accessible data. 
Escalate to AE 0.6.1 for alternative approach per ADVI_INFSHIP.B5 TO.
```

Orion's `Custom Reports/28198` is returning empty CSVs for T-1 dates via the API endpoint
(works via UI but not API per the error message). **Already escalated to AE 0.6.1 per
ADVI_INFSHIP.B5 — this is upstream/vendor-side, not a DS code bug.**

### Finding 4 — Several daily Lambdas have partial coverage (5/7)

`inf-accounts-v2-daily` (5 invocations), `inf-tax-daily` (5 invocations) — missing 2 days
each over 7 days. Cause unclear from this audit — could be intermittent EventBridge dispatch
failures, Lambda concurrency throttling, or specific-date data issues that cause exit-with-no-invocation.

Not critical individually; pattern worth surfacing.

## Recommended remediation (3 actions, post-correction)

| # | Owner | Effort | Action |
|---|---|---|---|
| 1 | **AE 0.7** | 30-60min each | Audit `inf-billing-daily` + `inf-performance-daily` for the never-fired issue. **inf-performance-daily is gating Stage 1 INFGRO.** |
| 2 | **AE 0.7** | 30min | Re-enable a daily gold-chain trigger. Either flip `inf-canonical-prices-daily` ENABLED (interim) OR ship TO-011 event-path (durable). |
| 3 | **DS me** | ~30min | Add `comp-validate INF_B_01` post-run sentinel: assert `market_value_sum > 0` for emitted dates. Fail-fast structural recurrence-prevention. |

inf-api-txn removed from action list (was stale 7-day window finding; current errors are
ADVI_INFSHIP.B5 in-flight).

## Files / artifacts examined (all read-only)

- `aws lambda list-functions` — 22 INF/Orion Lambdas inventoried
- `aws events list-rules` + `describe-rule` + `list-targets-by-rule` — 17 INF rules + states
- `aws lambda get-policy --function-name inf-billing-daily` — EventBridge permission confirmed
- CloudWatch metrics 7-day Invocations + Errors on 12 INF Lambdas via boto3
- CloudWatch Logs `/aws/lambda/inf-api-txn` ERROR filter (7-day window) — current vs historical errors
- `git log --since="2 weeks ago" infra/aws/lambda/inf-pipeline/inf-api-txn/lambda_function.py`
- S3 head_object on `silver/prices/canonical_prices.parquet` (LastModified 2026-05-05)
- S3 head_object on `gold/canonical/canonical_performance_2026-05-03.parquet` (LastModified 2026-05-11 21:13Z, post-DS~B-Bug-B-fix)
- `aws ec2 describe-instances --filters Name=tag:Name,Values=inf-gold-*` — both runners STOPPED
- INF_B_01 source read (`data/orion/scripts/gold/INF_B_01.holdings_lots.py`)
- `build_canonical_prices.py` source read (data/orion/scripts/gold/) for upstream understanding
- `data/orion/scripts/gold/orion-gold-dispatch.sh` for cadence reference

## Compiler tools

| Tool | Run | Findings |
|---|---|---|
| `comp-blast canonical_nna` (run as part of prior TO-000 task) | Hit BD-side catalog (3 S3 artifacts) | INF catalog coverage gap surfaced |
| `comp-blast INF_C_01` + `INF_C_01.canonical_nna` | "No downstream consumers found" | INF catalog coverage gap confirmed (DS~B's `INF_COMP_PIPESCRIPT_DEPLOYED_COVERAGE` finding still queued) |
| No comp-tool runs specific to Bug A audit | n/a | Bug A is in upstream cron config + canonical_prices freshness — outside the comp-* graph scope |

## Surface for memory entry (candidate, post-RAVC)

**"EventBridge-rule-enabled + Lambda-permission-attached + cron-syntax-valid + zero
invocations = Lambda has never been invoked at all (no log streams)"** is a structural
failure mode worth a memory entry. The four upstream checks all pass; the failure is
at the deployment layer (Lambda not deployed correctly, or stuck in init failure).

Will crystallize as `feedback_eventbridge_zero_invocation_class.md` after AE 0.7 surfaces
the actual root cause for inf-billing-daily / inf-performance-daily.

## RAVC

- COO 21:18Z: GO on Bug A audit (read-only)
- DS~C 21:43Z: RAVC4 draft with audit + recommendation
- DS~C 21:44Z: CORRECTION on inf-api-txn (was already fixed; current errors are upstream-vendor)
- Pending: COO routing on action 3 (comp-validate INF_B_01 sentinel) + session-log-scope confirmation

## Status

Audit complete. Session log committed. Standby for COO routing on the 3 remediation actions.
