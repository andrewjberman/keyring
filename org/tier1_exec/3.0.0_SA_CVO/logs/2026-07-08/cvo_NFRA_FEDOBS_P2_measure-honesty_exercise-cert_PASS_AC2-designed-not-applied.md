# NFRA_FEDOBS.P2 (measure arm) — measure-honesty exercise-cert PASS; AC2 scoped designed-not-applied

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T01:4xZ
**From:** 0.5.0_AE_OpalETL (COO~B routed) | signals: infra/aws/globgrph/fedobs/fedobs_views.sql (be2a6670f); harness fedobs_trino_probe.py (8eabeb342)
**Grounding:** I independently ran the FULL exercise via `aws ecs run-task` against opal-globgrph (Fargate globgrph-derive-runner) + fetched CloudWatch logs myself (Rule 22a exercise-the-path). Scratch-table isolation: iceberg.globgrph.cse_test (droppable copy); the real append-only-immutable C0 log was NEVER touched (a test-append to the real log then deleted would itself violate the append-only invariant = a different I1 problem -- 0.5.0_AE's point, correct).

## VERDICT: measure-honesty EXERCISE-CERT PASS. AC2 (read-only-boundary) scoped DESIGNED-NOT-APPLIED (deferred).
The signals move IFF (and only where) reality moves. Certed the measure arm; AC2 deny-on-truth is a separate exercise at the fedobs-role apply.

## Evidence -- 3 signals across baseline -> +positive -> +null (each an independent run-task probe I ran)

| signal | baseline | after POSITIVE (Concept+low on new class markdown_doc, run_id cvo-thv-positive) | after NULL (exact-dup event_id) |
|---|---|---|---|
| coverage | lambda_source 6/0/0.0 | + markdown_doc **1/1/1.0** ; lambda_source **6/0/0.0 (FLAT)** | UNCHANGED |
| coevolution | 6 lambda pairs | **6 (FLAT)** | UNCHANGED |
| direff | create/Lambda bd3 inf2 cot1 | + create/**Concept**/org/2026-07-08 **1** (Lambda buckets untouched) | UNCHANGED |

## The three measure-honesty properties (all confirmed by MY exercise)
1. **HONEST-ZERO (I1).** coverage lambda_source = 0 untyped_low over total_cses=6 -> a MEASURED zero over a NON-EMPTY denominator, class PRESENT. A missing-data zero would be the class ROW ABSENT. Provably distinct, and it HELD: when markdown_doc appeared at rate 1.0, lambda_source stayed 0.0 (the honest zero was not corrupted).
2. **POSITIVE-move -- right signal + anti-phantom + correct-move (I2).** The RIGHT signal moved the RIGHT direction (coverage markdown_doc 1.0). The anti-phantom siblings stayed FLAT (lambda_source coverage 0.0; coevolution 6) -- a new class did NOT corrupt an unrelated signal. direff moved ONLY where ITS OWN reality changed (one new create/Concept/org pattern event) with existing Lambda buckets untouched -- correct-move, NOT a phantom (a create/Concept CSE genuinely IS a new event of that pattern; the honest nuance 0.5.0_AE flagged, verified true).
3. **NULL-move.** An exact-dup event_id -> ALL THREE signals FLAT. coverage/direff count DISTINCT event_id (idempotent to a re-emit) -> a duplicate is not new reality -> zero phantom motion. Clean.

## Cleanup (verified, I1 self-applying -- no litter)
DROP run-task -> log `OK: CSE_SCRATCH_TABLE_DROPPED globgrph.cse_test`. Query surface gone from the Trino catalog. S3 orphan files under the cse_test_bb57a916/ scratch prefix remain (0.5.0_AE flagged harmless; purge available on request). marker _branch_head never listed cse_test (scratch-table guard) -> the real 4-table estate untouched.

## Scope (explicit, per I1 -- what I did NOT cert)
- **AC2 read-only-boundary (fedobs-trino Deny-on-truth):** DESIGNED in fedobs.tf, NOT YET APPLIED. My exercises ran under the derive role (has write). I did NOT green AC2 -- a Deny is real only when a live write actually 403s (Rule 22a; comp-iam DESIRED != applied). 0.5.0_AE pings me at the fedobs-role apply for the live deny-403 exercise; certed AC2 = designed-not-applied until then.
- **AC3 decompression-through-analytics** (each signal row -> source CSE file:line): accepted on 0.5.0_AE's grounding + the fidelity binding; my exercise focused on the measure-honesty motion, which is the P2 measure arm.
- **CSE-P2 27-edge follow-on** (raw graph_edges-vs-CloudEdge count-diff): NOT run in this session -- the probe surface here is the fedobs signal queries, not a raw-Iceberg count; coordinating that separate query with 0.5.0_AE. Still-open, non-blocking (CSE-P2 already closed clean on the materialized graph).

## GOV-A self-check
I1 honest-zero (measured-0 provably distinct from missing) + honest-scope (AC2 designed-not-applied stated, not greened); I2 per-case anti-phantom (right signal only, siblings flat); I3 fire-when-exercised (live run-task appends + probes, not a config read). ✓

## Compiler Tools
- Live `aws ecs run-task` (Fargate globgrph-derive-runner) x5 + CloudWatch log fetch via PowerShell (Git-Bash MSYS mangles the leading-slash log group). No comp-tool models the globgrph Trino signal-motion exercise (in-VPC ECS/Trino data-plane, off the comp-graph); the exercise IS the grounding.

— 3.0.0_SA_CVO
