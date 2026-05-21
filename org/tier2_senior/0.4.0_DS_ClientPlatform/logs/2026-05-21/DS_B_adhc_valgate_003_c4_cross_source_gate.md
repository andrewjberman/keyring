# DS~B Session Log -- ADHC_VALGATE.003 (C-4 cross-source row-content parity gate)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**Branch:** CLOUD
**TO:** ADHC_VALGATE.003 -- C-4 cross-source row-content parity gate
**PRD:** docs/architecture/ADHC_VALGATE.md v0.1 (section 4.C C-4, section 7 Q5)
**Depends on:** ADHC_VALGATE.001 (baseline machinery + gate-fire surface)

## Summary

C-4 is the cross-source row-content parity gate: when two writers/sources
produce overlapping-date output for the same logical artifact, C-4 computes a
comparison statistic on each (for the shared date) and WARNs when they diverge
beyond epsilon. Built GENERAL + configuration-driven -- a new dual-source pair
is a registry entry, not new code.

Per the PRD Q5 resolution: the originating anchor (ADVI_DWSPLT silver/
transactions dual-writer) is CLOSED -- so C-4 is NOT wired DWSPLT-specifically;
it ships engine-complete as the general gate, activating per pair.

## Phase 1 -- the C-4 engine

`gate_c4(df_a, df_b, entry)` in valgate_gate.py -- pure function:
- config-driven via a registry entry (statistic, epsilon, epsilon_mode).
- `_c4_statistic()` computes the comparison statistic: row_count / sum(column)
  / nunique(column).
- compares |stat_A - stat_B| vs epsilon (absolute or relative); WARN on
  divergence, PASS within.
- SKIP when (a) no registry entry, (b) source B unavailable for the date, or
  (c) the statistic is not evaluable (named column absent).
- baseline-independent -- evaluated in every mode (never bootstrap-SUPPRESSED).
`_load_cross_source_b()` reads source B's {prefix}/{date}.parquet from S3.

## Phase 2 -- the config map

`CROSS_SOURCE_REGISTRY` in valgate_baseline.py. SHIPS EMPTY + DOCUMENTED:
ADVI_DWSPLT (the originating anchor) is closed, and no other dual-source pair
is live at ship time -- so C-4 SKIPs for every artifact until a pair is
registered. The registry comment carries the entry schema + a copy-paste
ACTIVATION TEMPLATE (the anticipated candidate is an Eclipse/Orion WS-C
overlap). comp-pipescript io: N/A -- no live cross-source producer pair to
trace (per the TO's explicit allowance for an empty-but-documented config).

## Phase 3 -- wiring

C-4 wired INSIDE valgate_gate.run_gates() -- rides VALGATE.001's existing
dispatcher invocation (valgate_gate.py --artifact ... @ orion-gold-dispatch.sh),
ZERO new dispatcher surface. Verified firing on a real partition: C-4 [SKIP]
on silver/transactions 2026-05-20 (empty registry -- correct).

## Section-3.2 six-field gate table -- C-4

| Field | C-4 |
|-------|-----|
| name | cross-source row-content parity |
| trigger | post silver/gold partition build, pre-platinum-emit (the VALGATE.001 orion-gold-dispatch.sh step -- C-4 rides the same invocation) |
| input | a comparison statistic (row_count / sum / nunique) on the freshly-built partition (source A) for the date |
| reference | the same statistic on the paired source B for the same date (valgate_baseline.CROSS_SOURCE_REGISTRY) |
| comparison | \|stat_A - stat_B\| vs the configured epsilon (absolute or relative) |
| verdict | WARN on divergence beyond epsilon (v1; PASS within; SKIP with no registry entry or no paired source-B partition). Baseline-independent -- never bootstrap-SUPPRESSED |
| action | surface the WARN to the chain-log + session-log, route to the artifact owner to reconcile the two sources; does NOT fail the chain in v1 |

(Also in-code as `GATE_SPEC["C-4"]`.)

## Verification

**Fixtures (valgate_gate_fixtures.py): 12/12 PASS** -- the 9 prior cases +
3 new C-4 cases:
- TEST 10 -- two sources within epsilon -> C-4 PASS.
- TEST 11 -- a deliberate divergence (the DWSPLT 115-vs-16,882 dual-writer
  class) -> C-4 WARN, finding=breach.
- TEST 12 -- C-4 SKIPs with no registry entry / no source-B partition; the
  sum-statistic + relative-epsilon path works.
**Real-partition run:** C-4 [SKIP] on silver/transactions 2026-05-20 (empty
registry) -- confirms C-4 rides run_gates / the .001 invocation.

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/valgate_baseline.py | + CROSS_SOURCE_REGISTRY (empty + documented) + get_cross_source_entry() |
| data/orion/scripts/gold/valgate_gate.py | + gate_c4 + _c4_statistic + _load_cross_source_b + GATE_SPEC['C-4']; run_gates wires C-4 (baseline-independent); docstrings |
| data/orion/scripts/gold/valgate_gate_fixtures.py | + 3 C-4 tests (12/12) |

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | exit 0 -- all 3 files (Rule 15 first-import; ruff; AST) |
| comp-pipescript io | N/A -- no live cross-source producer pair (DWSPLT closed); C-4 ships engine-complete with the documented-empty config, per the TO |
| comp-pipescript deployed | md5 local-vs-S3 MATCH (deploy section) |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- 3 files |
| Commit | <commit> -- 3 valgate scripts + this log |
| Push | origin/CLOUD -- safe-deploy auto-deployed to s3://opal-data-inf/code/gold/ |
| Deployed | md5 local==S3 MATCH (all 3) |

## Current State

ADHC_VALGATE.003 COMPLETE -- C-4 engine shipped (config-driven, general),
verified (12/12 fixtures + real-partition run), wired (zero new dispatcher
surface). RAVC2 to COO~B CC CTO~B.

## Next

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- .003 complete. The VALGATE Class-C suite (C-1/C-2/C-3/C-4) is now fully shipped. |
| **CTO~B 1.0.0** | CC on RAVC2. |
