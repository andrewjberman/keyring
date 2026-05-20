# DS~B Session Log -- ADHC_VALGATE.001 (Class-C gates C-1 + C-2)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** ADHC_VALGATE.001 -- C-1 row-count + C-2 classification-distribution
gate + shared rolling-baseline machinery
**PRD:** docs/architecture/ADHC_VALGATE.md v0.1

## Summary

VALGATE Phase-1 foundation TO. Built the rolling-baseline machinery + the C-1
and C-2 Class-C data-correctness gates. Phases 0-3 SHIPPED; Phase 4
(chain-wire) is AE-sequenced (pending RUNDATE-DISPATCH-IMPL + SYNC-COLLISION
clearance on the hot orion-gold-dispatch.sh).

Anchor: DWSPLT chain #27 -- a mode=full chain passed every A/B/C/D sentinel
green while silver/transactions carried 16,882 rows vs 115 the prior day
(150x) with zero NNA-classified rows. C-1 + C-2 are the gates that WARN it.

## Phase 0 -- gate placement (AC1)

Decision: the gate fires as a STEP INSIDE orion-gold-dispatch.sh, post
silver/gold build, pre-platinum-emit -- gate logic in a standalone versioned
module, dispatcher edit = one invocation line. NOT a post-chain Lambda.
Rationale (full: docs/briefs/adhc-valgate-001-phase0-gate-placement-20260520.md,
commit e0b21f60b): placement fidelity (pre-emit, not post-emit); the
WARN->BLOCK ratchet stays a one-line policy flip; fails-loudest; no new infra;
hot-dispatcher collision shrunk to one line. AE 0.5.0~B CONCURRED. AE rider
adopted: the dispatcher invocation is exit-code-gated from day one
(verdict->exit-code in the module) so the ratchet needs zero dispatcher edit.

## Phase 1 -- rolling-baseline machinery (AC2)

`data/orion/scripts/gold/valgate_baseline.py` -- the reusable foundation
VALGATE.002/.003 hard-gate on:
- `BaselineStore` -- per-(artifact,date) statistic samples at
  `gold/meta/valgate-baseline/{artifact}/{date}.json`; dual backend (S3 for
  the runner; local-dir for fixtures) off one code path.
- `compute_partition_stats()` -- row count + per-bucket classification rates
  (a null bucket folds to the literal '(null)' so classification-loss is
  visible, not silently dropped).
- `ARTIFACT_CONFIG` / `get_config()` -- per-artifact N / K / bucket_column /
  bucket_floors / distribution-distance-threshold / material_min_rows, with a
  DEFAULT_CONFIG merge.
- `load_window()` -- the rolling-window read API (strictly-before semantics:
  a gate compares against PRIOR history, never a same-date re-run sample).
- `rolling_median_row_count()`, `rolling_bucket_rates()`,
  `total_variation_distance()` -- the C-1/C-2 reference aggregates.
- `is_bootstrapped()` -- WARN-SUPPRESSED until >= N/2 samples.

## Phases 2-3 -- C-1 + C-2 gates (AC3 + AC4)

`data/orion/scripts/gold/valgate_gate.py` -- C-1 + C-2 on the machinery, plus
the CLI entry point. Verdict model: v1 policy WARN-not-BLOCK (PRD section 7
Q1); verdict->exit-code map (WARN/PASS/SUPPRESSED/SKIP -> 0, BLOCK -> 1) so
the dispatcher invocation is exit-code-gated and the WARN->BLOCK ratchet is a
one-line flip of `GATE_VERDICT_POLICY` -- no dispatcher edit.

### Section-3.2 six-field gate table

**C-1 -- row-count stability**
| Field | Value |
|-------|-------|
| Trigger | post silver/gold partition build, pre-platinum-emit (orion-gold-dispatch.sh step) |
| Input | the freshly-built partition's row count |
| Reference | rolling N-day median row count for the artifact (valgate-baseline store) |
| Comparison | current / baseline_median outside [1/K, K] (K=5 for silver_transactions) |
| Verdict | WARN on breach (v1; PASS otherwise; SUPPRESSED in the bootstrap window) |
| Action | surface the WARN to the chain-log + session-log, route to the artifact owner; does NOT fail the chain in v1 |

**C-2 -- classification-distribution stability**
| Field | Value |
|-------|-------|
| Trigger | post silver/gold partition build, pre-platinum-emit (orion-gold-dispatch.sh step) |
| Input | the per-bucket classification rates of the partition (config bucket_column) |
| Reference | rolling N-day per-bucket rates for the artifact (valgate-baseline store) |
| Comparison | a bucket rate below its absolute floor in a material partition, OR total-variation distance vs baseline above the threshold |
| Verdict | WARN on breach (v1; PASS otherwise; SUPPRESSED bootstrap; SKIP when no bucket_column) |
| Action | surface the WARN to the chain-log + session-log, route to the artifact owner; does NOT fail the chain in v1 |

(Also embedded in-code as `valgate_gate.GATE_SPEC` so the contract travels
with the gate.)

### Verification -- fixtures

`valgate_gate_fixtures.py` -- 6/6 PASS. `valgate_baseline.py` self-check
16/16 PASS. Both offline (local BaselineStore backend, synthetic partitions).
- AC3: DWSPLT-#27 class -- a 16,882-row partition vs a ~115-row baseline ->
  C-1 WARN (ratio 146.8x, outside [0.20, 5.00]).
- AC4: zero NNA in a 16,882-row material partition -> C-2 WARN (NNA rate
  0.0000 below the 0.0001 floor; also TVD 0.400 > 0.350).
- Bootstrap: a cold artifact -> both gates SUPPRESSED, statistic still
  recorded. Immaterial partition (< material_min_rows) -> floor check
  suppressed. Verdict->exit-code map verified.

## Baseline read API -- for VALGATE.002 (C-3) + .003 (C-4) reuse

VALGATE.002/.003 import `valgate_baseline` and reuse:
- `BaselineStore(local_dir=None)` -- `.read_sample(artifact, date)`,
  `.write_sample(artifact, date, stats)`, `.list_dates(artifact)`,
  `.load_window(artifact, before_date, n)`.
- `compute_partition_stats(df, bucket_column)` -- the standard statistic.
- `get_config(artifact)` / `ARTIFACT_CONFIG` -- add the .002/.003 artifacts +
  their C-3 sentinel-id sets / C-4 parameters as new config keys.
- `is_bootstrapped(window, n)` -- the same WARN-SUPPRESSED bootstrap rule.
- `artifact_slug(s3_key_prefix)` -- the artifact -> path-segment normalizer.
A C-3 / C-4 gate is a new `gate_c3()` / `gate_c4()` in valgate_gate.py
following the C-1/C-2 dict-return shape (gate / verdict / finding / detail /
measured) + a GATE_SPEC entry.

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/valgate_baseline.py | NEW -- rolling-baseline machinery (Phase 1) |
| data/orion/scripts/gold/valgate_gate.py | NEW -- C-1 + C-2 gates + CLI (Phases 2-3) |
| data/orion/scripts/gold/valgate_gate_fixtures.py | NEW -- 6-test fixture suite |
| docs/briefs/adhc-valgate-001-phase0-gate-placement-20260520.md | NEW -- Phase 0 decision |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- all 3 .py (py_compile + AST + ruff); Rule 15 `from __future__` first import |
| Commits | e0b21f60b (Phase 0 brief), 96b5cbd17 (Phase 1), c26cffa10 (Phases 2-3) -- pushed origin/CLOUD |
| S3 deploy | safe-deploy pre-push hook auto-deployed data/orion/scripts/gold/valgate_*.py -- "all files deployed and verified" |

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-pipescript io convert_transactions_to_silver | WRITES silver/transactions/{*}.parquet (S3-DYNAMIC) -- confirms the gate reads the same artifact the producer writes; no mismatch |
| ds-commit-gate.sh | exit 0 on all 3 .py edits |
| comp-pipescript deployed | the orion mdpf comp-graph does not model these new gold-dir modules yet; safe-deploy's own deploy-verify ("all files deployed and verified") is the deploy MATCH |

## Current State

ADHC_VALGATE.001 Phases 0-3 COMPLETE + shipped. Phase 4 (chain-wire) reached
-- AE-sequenced. Gates are surface-agnostic; the chain-wire is the only
remaining step.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | Sequence Phase 4 (chain-wire) with the ~B AE gold-chain owner (0.5.0_AE_OpalETL~B) -- the one-line exit-code-gated invocation of valgate_gate.py at the post-D-chain-build / pre-platinum-emit point in orion-gold-dispatch.sh, after RUNDATE-DISPATCH-IMPL + SYNC-COLLISION land. On the wire + a verified real-chain WARN-emit, RAVC2 closes (CC CTO~B). |
| **DS~B (self)** | On the AE chain-wire, verify the gate fires on a real chain run (AC5), then RAVC2. VALGATE.002 (C-3) + .003 (C-4) unstage on .001 RAVC2-accept and reuse the baseline read API above. |
