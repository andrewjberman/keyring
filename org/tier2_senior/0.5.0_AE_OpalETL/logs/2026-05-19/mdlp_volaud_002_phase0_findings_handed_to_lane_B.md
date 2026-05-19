# MDLP_VOLAUD.002 — Phase 0 partial work + lane handoff to 0.5.0_AE_OpalETL~B

**Date:** 2026-05-19
**Agent:** 0.5.0_AE_OpalETL (base)
**TO (paused/superseded):** `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/MDLP_VOLAUD.002.ae-lambda-runtime-1d-wtd-mtd-anomaly-investigation.md`
**Successor TO:** `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/MDLP_VOLAUD.003.ae-yang-generate-benchmark-returns-retire-or-redesign.md` (now ~B's lane per Andrew 2026-05-19)

## Current State

- I picked up MDLP_VOLAUD.002 at session start (15:18Z COO GO in inbox), Phase 0 surfaced a structural finding that changed the diagnostic posture, then COO~B's SSCN_DIVDEF.004 GO arrived and the user redirected me to that priority. After SSCN closed, Andrew clarified that `0.5.0_AE_OpalETL~B` (lane sibling) now owns MDLP_VOLAUD continuation. This log captures the Phase 0 finding for ~B's handoff.
- **MDLP_VOLAUD.002 paused/superseded by base COO 2026-05-19 ~17:3XZ.** New TO **MDLP_VOLAUD.003** carries the dual-writer fix (yang-generate-benchmark-returns retire-or-redesign). Routed to ~B per Andrew clarification.

## Phase 0 Empirical Findings (for ~B handoff)

### Bug not reproducible from `yang-model-portfolio-benchmarks` alone

Fresh `aws lambda invoke` against `yang-model-portfolio-benchmarks` at 2026-05-19T17:18:49Z with the reconstructed Step Functions event payload (same `data_pkl_key=benchmarks/data_20260519_v1.pkl`, `data_as_of_date=2026-05-18`, RequestId `7dcd4176-79ac-4cde-81ff-16c5dd198b6d`) produced **correctly differentiated** 1D / WTD / MTD values across all 5 models. Sample (UST INDEX vol):

| Period | DS~B local probe | Fresh Lambda invoke 17:18Z | Morning JSON (anchor) |
|---|---|---|---|
| 1D | 1.25 | 1.25 ✓ | 1.31 (COLLAPSED) |
| WTD | None (n=1 < min_points=5) | None ✓ | 1.31 |
| MTD | 1.18 | 1.18 ✓ | 1.31 |

Fresh invoke matched DS~B's local probe to-the-cent. Same code, same Layer, same source pickle, same event payload — different output 6h apart.

### S3 versioning revealed two writes 1 second apart on 2026-05-19 morning

| VersionId | LastModified (UTC) | generated_at | Pattern |
|---|---|---|---|
| `numli0VXWkNuusBbhWZOuLBYZTQHOXm9` | 2026-05-19T11:25:03Z | 2026-05-19T11:25:02Z | **CORRECT** (UST idx vol 1D=1.25, WTD=None, MTD=1.18) |
| `Ei1PBpuJhCInkRSP8rVkGNPoRMoSnO33` | 2026-05-19T11:25:04Z | 2026-05-19T11:25:03Z | **COLLAPSED** (UST idx vol 1D=WTD=MTD=1.31) — survivor; the audit anchored on this |

The 2nd write OVERWROTE the 1st. Audit was looking at the survivor (collapsed). Single Lambda invocation of `yang-model-portfolio-benchmarks` produces only ONE upload per key (line 285 of `lambda_function.py`); so two writes 1s apart means two different invocations.

### Second writer found: `yang-generate-benchmark-returns`

Grep for `model_portfolio_benchmarks.json` in `infra/aws/lambda/` surfaced **two** Lambdas writing the same `OUTPUT_KEY_COMPREHENSIVE`:

| Lambda | Runtime | Layer | CodeSha256 | Behavior |
|---|---|---|---|---|
| `yang-model-portfolio-benchmarks` | python3.12 | AWSSDKPandas-Python312:16 | MJ6sOPLnZZNb9brIlQBOMG3JliwvoYd+fxj2/6Qq4pI= | Correctly differentiates |
| `yang-generate-benchmark-returns` | python3.11 | pandas-pyarrow-layer:1 | kq28uQNf3HdeegOrIpXAwO3733lxTf8h/VS603LDTSE= | Produces collapse |

CloudWatch RequestIds at 11:25 morning:
- `yang-model-portfolio-benchmarks`: `fe5f8952-6553-4eaf-bb17-e37947c7008a` (writes v1 CORRECT)
- `yang-generate-benchmark-returns`: `a42208fb-9653-435a-9dd6-85cc652bce20` (writes v2 COLLAPSED 1s later)

Both fired from the SAME Step Functions execution (`pipeline_execution_id=5bad87c2-2903-4921-bc30-de209c6190bb`). Last-writer-wins on the shared S3 key → user sees collapsed JSON.

### Why my fresh invoke produced correct output

My 17:18Z `aws lambda invoke` targeted ONLY `yang-model-portfolio-benchmarks` — single invocation, no race, correct output overwrites the morning's bad data. This INCIDENTALLY repaired the currently-served JSON to differentiated values. The structural bug returns on tomorrow's scheduled SFN run unless fixed.

### Hypotheses (per CTO's MDLP_VOLAUD.003 framing handed to ~B)

- **Hypothesis A — retire** `yang-generate-benchmark-returns`: it's likely a legacy Lambda superseded by `yang-model-portfolio-benchmarks` (the MDLP_RVVALT 2026-05-04 ship) but the Step Functions state machine was never updated to remove the legacy step. Same OUTPUT_KEY argues this. Cleanest path if Phase 0.5 probe confirms no unique consumer.
- **Hypothesis B — redesign**: if some downstream still depends on `yang-generate-benchmark-returns`'s output uniquely (different shape, different fields, etc.), the fix is more involved — separate output keys, sequential SFN states, or merge logic.

CTO leans (A) retire; Phase 0.5 probe-first is the ratification gate.

## Phase 0.5 Probe Checklist for ~B

(Copied from MDLP_VOLAUD.003 TO scope for ~B's convenience)

1. `infra/aws/lambda/ci/lambda-source-map.json` — pull both Lambda entries; check `last_deployed_commit` lineage; verify the legacy-supersession hypothesis.
2. Direct-read `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-benchmark-returns/lambda_function.py` — compare to the newer `yang-model-portfolio-benchmarks`; identify any unique output fields.
3. SFN state machine definition: `aws stepfunctions describe-state-machine --state-machine-arn arn:aws:states:us-east-1:313476888478:stateMachine:YangDataPipeline` — locate the two state transitions for the two Lambdas; check whether `yang-generate-benchmark-returns` is sequential or parallel relative to `yang-model-portfolio-benchmarks`.
4. `comp-blast yang-generate-benchmark-returns` — downstream consumer enumeration. If empty, pure-redundant retire is safe.
5. `comp-routes trace OUTPUT_KEY_COMPREHENSIVE` — portal-consumer indirect check (the JSON is served via CloudFront; portal reads it).
6. `comp-iam service yang-generate-benchmark-returns` — IAM baseline for cleanup planning (Phase 1 will need to remove the role + policies).

If Phase 0.5 returns "pure redundant" → Phase 1 retire path (SFN edit + Lambda removal + IAM cleanup + source-map removal + yang-v{next} tag, ~30-45min).

If Phase 0.5 surfaces unique consumer → PAUSE Phase 1; channel-push verdict to base COO + CC CTO; redesign discussion before any code edit.

## Side Note on Audit-Hypothesis Refinement

DS~B's MDLP_VOLAUD.001 brief stated the collapse covered BOTH returns AND volatilities across 1D/WTD/MTD. My empirical re-inspection of the published JSON refined this:

- **Returns: 1D = WTD only** (mathematically correct on a Monday end_date — both windows contain just that day). MTD returns ARE properly differentiated in the JSON.
- **Volatilities: 1D = WTD = MTD all three collapse** to the same value.

So the "bug" is purely in volatility computation for WTD/MTD branches. The 1D=WTD return identity is intentional behavior on a Monday end_date. Worth noting for ~B's Phase 0.5 probe — if `yang-generate-benchmark-returns` has divergent vol logic for WTD/MTD branches, that's the cause; if its returns also collapse erroneously, the diagnosis is different.

## Artifacts in `.runtmp/`

For ~B's reference (gitignored):
- `.runtmp/anchor_model_portfolio_benchmarks.json` — pre-invoke anchor (11:25:03Z, COLLAPSED)
- `.runtmp/lambda_post_invoke.json` — post-fresh-invoke output (17:18:49Z, CORRECT)
- `.runtmp/v1_1125_03.json` / `.runtmp/v2_1125_04.json` — both versioned S3 objects from the morning race
- `.runtmp/v3_0517.json` — 2026-05-17 prior run (also collapsed; confirming this is not a one-off)
- `.runtmp/benchmarks_LATEST.json` — pickle resolver
- `.runtmp/mdlp_volaud_002_invoke_event.json` — reconstructed Step Functions event payload
- `.runtmp/lambda_invoke_response.json` + `.runtmp/lambda_invoke_meta.json` — invoke metadata + LogResult tail

## Routing

- Phase 0 finding already routed via COO~B → base COO + CTO base. Base COO closed-as-superseded MDLP_VOLAUD.002 + dispatched MDLP_VOLAUD.003 with the dual-writer scope per CTO disposition. Routed to me, but Andrew has now reassigned MDLP_VOLAUD lane to `0.5.0_AE_OpalETL~B`.
- This log handed off to `~B` for Phase 0.5 startup.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `comp-pipescript io yang-model-portfolio-benchmarks` | empty | Lambda not indexed in comp graph (TO §compiler_tools_mandate documented gap; not blocking). |
| Direct file-read `yang-model-portfolio-benchmarks/lambda_function.py:333-477` | OK | Methodology reference (`get_term_returns` + `calculate_period_returns` + `calculate_volatility`). |
| `aws lambda invoke` + diff vs anchor | OK | Single-invocation produces correct output; collapse non-reproducible standalone. |
| `aws s3api list-object-versions` | OK | Surfaced the 2-version morning write pattern. |
| `aws logs filter-log-events` | OK | Cross-pulled RequestIds for both Lambdas at 11:25. |
| `grep model_portfolio_benchmarks.json infra/aws/lambda/` | OK | Surfaced the second writer. |

## Status

- **MDLP_VOLAUD.002:** paused at session start; superseded by base COO as MDLP_VOLAUD.003 with my Phase 0 findings folded in.
- **MDLP_VOLAUD.003:** in `0.5.0_AE_OpalETL` task_orders folder (issued to my serial), but per Andrew clarification 2026-05-19 PM, the work is now `0.5.0_AE_OpalETL~B`'s lane.
- `~B` should: read this log, read MDLP_VOLAUD.003 TO body, run Phase 0.5 probe per checklist above, channel-push verdict to base COO + CC CTO before Phase 1.

## Next Steps

- `[0.5.0_AE_OpalETL~B]` Phase 0.5 probe + retire-vs-redesign verdict; Phase 1 retire or redesign-pause; Phase 2 verify against tomorrow's 14:00Z scheduled cron (~18h margin from now).
- `[0.5.0_AE_OpalETL (base)]` Standing by; SSCN_DIVDEF.004 closed; no other active TOs in queue.
