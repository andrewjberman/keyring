# Session Log — ADHC_COMPIL.011 INF ID Resolver

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-30
**TO:** ADHC_COMPIL.011.ds-inf-script-id-resolver
**Status:** COMPLETE

---

## File-list Audit (Phase 1 — before write)

### INF gold scripts (data/orion/scripts/gold/ — CATALOG-indexed)
32 active scripts with INF_ prefix IDs:
INF_09, INF_A_00–INF_A_04, INF_B_00–INF_B_03, INF_C_00–INF_C_08 (incl. INF_C_01b),
INF_D_00c, INF_D_02, INF_D_04–INF_D_08, INF_I_D00, INF_I_D00b, INF_I_D02d, INF_I_D03

Note: The orion gold dir also contains non-prefixed files (B_00.canonical_holdings.py,
D_04.client_portal_summary.py, etc.) — these are legacy copies; the CATALOG references
the INF_*-prefixed filenames. build_inf_gold_dag uses CATALOG exclusively (not dir walk).
INF_I_* prefix scheme acknowledged as inconsistent naming (to be cleaned up in future TO).

### BD silver scripts (data/black_diamond/scripts/silver/)
Includes: bd_price_update.py, inject_scoped_overrides.py, and others.

### INF silver scripts (data/orion/scripts/silver/)
Includes: convert_orion_to_silver.py, and others.

---

## Dispatcher-indexing Implementation Choice

**Choice:** Parse via existing `_parse_dispatch` / `_parse_orion_dispatch` functions (sidecar-via-existing-parser approach), not shell-parse-inline or sidecar manifest.

**Rationale:** `_parse_orion_dispatch` and `_parse_dispatch` already exist in extract_pipeline.py and correctly parse the CATALOG heredoc + CHAIN_ variable format. The dispatcher output (chains, catalog) is printed directly via `_format_dispatcher_io()` which calls these parsers and exits 0. No new indexing layer required — the dispatcher nodes are not added to the DAG scripts dict; they are handled as a separate routing branch in `_auto_resolve_script_id` via the `_DISPATCHER_NODES` lookup dict.

---

## Baseline Verification (Phase 1)

`comp-pipescript io INF_D_04` before fix → FAIL (BD-only DAG default, INF scripts unreachable)
`comp-pipescript io INF_B_00` before fix → FAIL
`comp-pipescript io convert_orion_to_silver` before fix → FAIL

---

## Implementation Summary

**File modified:** `org/modules/graph/pipeline_cli.py`

Key changes:
1. Extended imports: `build_inf_gold_dag`, `build_silver_dag`, `build_multi_pipeline_dag`, `_parse_dispatch`, `_parse_orion_dispatch`
2. Extended `_PIPELINE_CHOICES` to include `bd`, `inf` shorthand
3. Extended `_build_dag()` to support `inf-gold`, `bd-silver`, `inf-silver`, `all`, `bd`, `inf` pipelines
4. Added `_DISPATCHER_NODES` dict for hyphenated dispatcher names
5. Added `_format_dispatcher_io()` — prints chain/catalog declaration and exits 0
6. Added `_canonicalize_script_id()` — strips data/ paths and .py suffixes
7. Added `_auto_resolve_script_id()` — full resolver:
   - INF_* prefix → inf-gold DAG (dedicated fast path)
   - dispatcher names → `_format_dispatcher_io` (exits)
   - snake_case silver-like IDs → bd-silver + inf-silver (collision detection)
   - bare BD/INF gold IDs → EXACT match in both DAGs (no substring) → disambiguation if both hit
   - on miss → `difflib.get_close_matches(cutoff=0.45)` closest-match suggestion
8. Restructured `cmd_io`: default/shorthand pipelines always route through `_auto_resolve_script_id`
   (AC6 fix); explicit non-default pipelines use direct DAG lookup

**Key design decision — exact match for disambiguation:**
Initial implementation used substring match (`upper in s` where s is an INF script ID).
This caused AC8 regression: `D_04` matched `INF_D_04` via substring, firing false
disambiguation. Root cause: all INF gold scripts have `INF_*` prefix IDs in the DAG;
bare BD IDs (`D_04`, `C_08`) never collide under exact match. Fixed to exact-match-only
for cross-pipeline disambiguation. INF-specific scripts (INF_D_04 etc.) are handled before
this section by the dedicated `upper.startswith("INF_")` branch.

---

## AC Verification

| AC | Test | Result |
|----|------|--------|
| AC1 | `comp-pipescript io INF_B_00` → exit 0 + I/O MANIFEST [inf-gold] | PASS |
| AC1b | `comp-pipescript io INF_B_99` → exit 1 + Did you mean: INF_B_03, INF_B_02, INF_B_01 | PASS |
| AC2 | `comp-pipescript io INF_D_04` → exit 0 + 6 READS | PASS |
| AC3 | `comp-pipescript io inf-gold-dispatch` → DISPATCHER: inf-gold-dispatch (3 chains, 41 catalog) | PASS |
| AC3 | `comp-pipescript io bd-gold-dispatch` → DISPATCHER: bd-gold-dispatch | PASS |
| AC3 | `comp-pipescript io orion-gold-dispatch` → DISPATCHER: orion-gold-dispatch | PASS |
| AC4 | `comp-pipescript io convert_orion_to_silver` → exit 0 [inf-silver] | PASS |
| AC5 | `comp-pipescript io bd_price_update` → exit 0 [bd-silver] | PASS |
| AC6 | synthetic: CATALOG entry `B_00\|B_00.placeholder.py` + file → exit 1 Ambiguous | PASS |
| AC7 | `--pipeline inf B_00` → [inf-gold]; `--pipeline bd B_00` → [bd-gold] | PASS |
| AC8 | B_01/D_04/C_08 → bd-gold unchanged (exact-match fix eliminates false disambiguation) | PASS |
| AC9 | `comp-blast INF_D_04` → no crash (returns "No nodes matching" — not in comp-trace graph; resolver extension confirmed transparent to callers) | PASS |
| AC10 | test_inf_id_resolver.sh → 15/15 cases pass | PASS |
| AC11 | org/compiler-tools-log.md rows appended | PASS |

**Regression guard:** `python -m pytest tests/ --ignore=tests/comp_pipescript` → 122 passed, 1 skipped

---

## File-count Audit (resolver extension coverage)

- INF gold scripts now resolvable via ID form: **32** (all INF_* IDs in CATALOG)
- INF silver scripts now resolvable via bare name: **7** (data/orion/scripts/silver/)
- BD silver scripts now resolvable via bare name: **8** (data/black_diamond/scripts/silver/)
- Dispatcher nodes now resolvable: **3** (inf-gold-dispatch, bd-gold-dispatch, orion-gold-dispatch)
- Total new IDs resolvable: **50+**
