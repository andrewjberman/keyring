# DS~B Session Log -- ADHC_VALGATE.002 (C-3 sentinel-rows-present gate)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** ADHC_VALGATE.002 -- C-3 sentinel-rows-present gate
**PRD:** docs/architecture/ADHC_VALGATE.md v0.1 (section 4.C C-3, section 3.2 gate anatomy, section 7 Q1 verdict policy)
**Depends on:** ADHC_VALGATE.001 (rolling-baseline machinery + the gate-fire surface) -- RAVC-accepted

## Summary

C-3 is the sentinel-rows-present gate. It diffs a freshly-built partition's
present key-identifier set against a declared registry of KNOWN-STABLE
identifiers and WARNs on any sentinel absent -- catching the failure mode
where a partition is shape-clean and not row-count-anomalous (C-1 + C-2 both
pass) but a specific known-stable entity silently dropped out. Anchor: the
INFGRO/INFNNA rep_id drop-out class.

C-3 is registry-vs-partition, NOT baseline-vs-partition -- so unlike C-1/C-2
it needs no rolling window and is never bootstrap-SUPPRESSED. It is evaluated
in every mode, cold artifact included.

## Phase 1 -- the declared sentinel-identifier registry

Empirically sourced, not picked arbitrarily. C-3 gates `silver/transactions`
(`s3://opal-data-inf/silver/transactions/{date}.parquet`) on the `rep_id` key
column -- the same artifact VALGATE.001 gates for C-1/C-2.

Phase-1 sweep (2026-05-20): the 15 most-recent silver/transactions partitions,
2026-05-01..2026-05-20. silver/transactions is allowlist-filtered to
`INFLECTION_REP_IDS = {3, 6, 11, 12}` (`_orion_api_silver_lib.py:113`), so
those four rep_ids are the entire universe of the artifact.

| rep_id | presence (15 partitions) | verdict |
|--------|--------------------------|---------|
| 11 | 15/15 -- incl. the 79-row 2026-05-12 partition | **SENTINEL** |
| 12 | 15/15 -- incl. the 79-row floor case | **SENTINEL** |
| 3 | 11/15 -- churns by business activity, NOT row-count-monotonic (absent from 1,247- and 1,499-row partitions, present in a 361-row one); rep_id 3 = the firm-level rep | excluded |
| 6 | 11/15 -- same activity-driven churn | excluded |

Registry: `SENTINEL_REGISTRY` in `valgate_baseline.py` -- per-artifact
`key_column` + `sentinels` ({id: basis}) + `excluded` ({id: reason}). rep_id
{11,12} registered as sentinels; {3,6} carry an explicit exclusion reason so a
future curator does not naively re-add a churning identifier.

## Phase 2 -- the C-3 gate

`gate_c3(df, config, registry_entry)` in `valgate_gate.py`:
- Material partition (row_count >= material_min_rows): diff the present key
  set against the declared sentinels; WARN on any absent.
- SKIP when (a) no registry entry, (b) the key column is absent, or (c) the
  partition is below the material-activity floor (a tiny partition
  legitimately carries no sentinels -- AC3).
- Key normalization: str -> strip -> drop trailing '.0' float artifact, so
  11 / "11" / "11.0" all match.
- v1 verdict policy = WARN-not-BLOCK (PRD section 7 Q1), reusing VALGATE.001's
  `verdict_for()` + the WARN->BLOCK ratchet.

## Phase 3 -- wiring

C-3 is wired INSIDE `valgate_gate.run_gates()` -- so it rides VALGATE.001's
existing dispatcher invocation (`python3 valgate_gate.py --artifact
silver/transactions --date $RUN_DATE` at orion-gold-dispatch.sh:686) with
ZERO new dispatcher surface, exactly as the TO requires ("reuse .001's
gate-fire surface, do not re-decide"). No orion-gold-dispatch.sh edit -- no
owned-paths reroute, no hot-dispatcher collision.

## Section-3.2 six-field gate table -- C-3

| Field | C-3 |
|-------|-----|
| name | sentinel-rows-present |
| trigger | post silver/gold partition build, pre-platinum-emit (the VALGATE.001 orion-gold-dispatch.sh step -- C-3 rides the same invocation) |
| input | the set of key identifiers present in the partition (the registry key_column) |
| reference | the declared sentinel-identifier registry -- known-stable identifiers per artifact (`valgate_baseline.SENTINEL_REGISTRY`) |
| comparison | set difference -- a declared sentinel absent from a material partition's present key set |
| verdict | WARN on any sentinel absent (v1; PASS when all present; SKIP below the material floor / no registry entry / key column absent). Baseline-independent -- never bootstrap-SUPPRESSED |
| action | surface the WARN to the chain-log + session-log, route to the artifact owner for registry curation; does NOT fail the chain in v1 |

(Also lives in-code as `GATE_SPEC["C-3"]` so the contract travels with the gate.)

## Verification

**Fixtures (`valgate_gate_fixtures.py`): 9/9 PASS** -- the 6 VALGATE.001 cases
re-baselined for the 3-gate report + 3 new C-3 cases:
- TEST 7 -- all sentinels present in a material partition -> C-3 PASS.
- TEST 8 -- sentinel rep_id 11 dropped from a material partition -> C-3 WARN,
  finding=breach, sentinels_missing=['11'] (the INFGRO/INFNNA drop-out class).
- TEST 9 -- immaterial partition (40 rows) with a sentinel absent -> C-3 SKIP
  (NOT WARN -- AC3); also the no-registry SKIP path.

**Real-partition runs (`--no-record`, non-mutating):**
- 2026-05-12 (79 rows, material): C-1/C-2 SUPPRESSED (cold baseline), C-3 PASS
  -- proves C-3 evaluates while the baseline-dependent gates are bootstrapped.
- 2026-05-20 (1,309,459 rows): C-3 PASS, all sentinels present.

Note on AC4 "WARN verdict": the WARN path is deterministically proven by
fixture TEST 8. A live WARN occurs only on an actual sentinel drop-out (the
gate's whole purpose) -- real silver/transactions has no genuine drop (that is
the healthy state), so a real-chain WARN cannot be manufactured without
corrupting data. C-3 is verified FIRING on real partitions above; it emits its
verdict line on every chain run via the inherited .001 dispatcher wire.

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/valgate_baseline.py | + SENTINEL_REGISTRY + get_sentinel_registry() |
| data/orion/scripts/gold/valgate_gate.py | + gate_c3 + _present_key_set + GATE_SPEC['C-3']; run_gates wires C-3 (baseline-independent); docstrings |
| data/orion/scripts/gold/valgate_gate_fixtures.py | _df + rep_id column; TEST 1 fixed for the 3-gate report; + 3 C-3 tests (9/9) |

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | exit 0 -- all 3 files (Rule 15 first-import; ruff; AST undefined-name) |
| comp-pipescript io (equivalent) | direct trace -- convert_transactions_to_silver.py confirms silver/transactions carries `rep_id` (JOIN from accounts_v2); INF_C_01 confirms rep_id is the INFNNA key |
| comp-pipescript deployed | the default profile checks opal-data-bd; orion gold deploys to s3://opal-data-inf/code/gold/ -- md5 local-vs-S3 MATCH verified directly (deploy section) |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- 3 files |
| Commit | <commit> -- 3 valgate scripts + this log |
| Push | origin/CLOUD |
| S3 deploy | s3://opal-data-inf/code/gold/ -- valgate_baseline.py + valgate_gate.py + valgate_gate_fixtures.py, md5 local==S3 MATCH |

## Current State

ADHC_VALGATE.002 COMPLETE -- C-3 sentinel gate shipped, wired (zero new
dispatcher surface), verified (9/9 fixtures + real-partition runs). RAVC2 to
COO~B CC CTO~B.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- .002 complete. Next-in-queue: ADHC_VALGATE.003 (C-4 cross-source row-content parity). |
| **CTO~B 1.0.0** | CC on RAVC2. |
| (parked) | MDPF_ASSETS.029 Phase 1 -- Andrew-signed-off; awaiting COO~B's formal Phase-1 GO. |
