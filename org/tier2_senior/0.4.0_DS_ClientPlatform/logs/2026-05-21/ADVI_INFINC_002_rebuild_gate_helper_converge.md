# ADVI_INFINC.002 — INFINC_REBUILD gate-value bug class — 2026-05-21

**Agent:** 0.4.0_DS_ClientPlatform (base — fallback owner; TO slugged `dsd-`, `~D`
lane phantom per the TO's dispatch_unblock_condition; CTO nudged base directly).
**TO:** ADVI_INFINC.002.dsd-infinc-rebuild-gate-value-bug-class
**Branch:** CLOUD
**Status:** COMPLETE — committed `43e13faf6`, pushed + S3-deployed. RAVC2 to COO CC CTO.

## Current State

The systemic INFINC_REBUILD gate-value bug (surfaced by ADVI_INFGRO.009): 4
inline Pattern-B `_force_rebuild` gates checked `INFINC_REBUILD == 'true'` while
the canonical value is `'1'` (orion-gold-dispatch.sh emit + `lib/skip_gate.py`) —
so a chain-driven rebuild silently no-op'd INF_C_03 / INF_D_05 / INF_D_06 /
INF_D_09. All 4 fixed; the 5th (INF_C_02) retrofitted off its ADVI_INFGRO.009 P2
inline fix. No rebuild chain triggered (code fix only, per the TO).

## Path taken — PREFERRED (helper-consumption), not the fallback

CTO ruling offered preferred (consume a shared `lib/skip_gate.py` helper) vs
fallback (4 inline value-aligns + a converge follow-up). **Preferred taken** —
the helper-signature inspection: all 4 scripts ALREADY carry the
`sys.path.insert(0, .../lib)` + `from schema_version import ...` pattern, so
adding a `from skip_gate import rebuild_requested` import is a 1-line low-delta
change per script. `lib/skip_gate.py` had no bare rebuild-flag helper
(`is_rebuild_active` is window-aware + needs a `partition_date`), so a new bare
helper was added:

- `lib/skip_gate.py` — NEW `rebuild_requested() -> bool`: the canonical bare
  rebuild-flag check (accepts `'1'` + truthy synonyms `true/yes/on`; one source
  of truth). Documented as the replacement for the 5 divergent inline gates.
- INF_C_03 / INF_D_05 / INF_D_06 / INF_D_09 — `_force_rebuild` now calls
  `rebuild_requested()`; `from skip_gate import rebuild_requested` added.
- INF_C_02 — RETROFITTED off its inline `4ccbce567` fix to call
  `rebuild_requested()` too, so all 5 Pattern-B gates are uniform — the
  re-inline-drift root cause is removed (AC2: preferred path -> INF_C_02
  retrofit done; no fallback follow-up needed).
- INF_C_03 — dropped the now-unused `import os` (the gate line was its only
  `os` use; ruff flagged it; INF_D_05/06/09 keep `os` — still used for
  `OUTPUT_PREFIX`).

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/lib/skip_gate.py | NEW `rebuild_requested()` helper |
| data/orion/scripts/gold/INF_C_02.client_performance.py | gate -> `rebuild_requested()` (retrofit); skip_gate import |
| data/orion/scripts/gold/INF_C_03.account_performance.py | gate -> `rebuild_requested()`; skip_gate import; dropped unused `import os` |
| data/orion/scripts/gold/INF_D_05.client_top_holdings.py | gate -> `rebuild_requested()`; skip_gate import |
| data/orion/scripts/gold/INF_D_06.client_timeseries.py | gate -> `rebuild_requested()`; skip_gate import |
| data/orion/scripts/gold/INF_D_09.account_timeseries.py | gate -> `rebuild_requested()`; skip_gate import |

Commit `43e13faf6`, pushed origin/CLOUD; safe-deploy gate DEPLOYED all 5 gold
scripts + skip_gate.py to `s3://opal-data-inf/code/gold/` and verified.

## Compiler Tools

| Phase | Run | Result |
|-------|-----|--------|
| 1 (before) | `comp-pipescript io` x4 (INF_C_03/D_05/D_06/D_09) | All RESOLVED as inf-gold nodes (INF_C_03 Order 280, INF_D_05 490, INF_D_06 500, INF_D_09 480). Gate edits sit in `main()` append-only blocks, clear of column-gaps. |
| 2 (before commit) | `.tools/ds-commit-gate.sh` x6 | Exit 0 all 6 (py_compile + ds-precommit AST scan + ruff py39). First pass flagged INF_C_03's now-unused `import os` — removed; re-run clean. |
| 3 (after) | helper logic test + gate grep | `rebuild_requested()` -> True for `1/true/TRUE/yes/on`, False for `0/empty/false/unset`. grep: all 5 gates read `rebuild_requested()`; zero surviving inline `INFINC_REBUILD ... == true` in `data/orion/scripts/gold/*.py`. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — ADVI_INFINC.002 COMPLETE, AC1-AC4 met. Preferred helper path taken; all 5 INFINC_REBUILD gates converged onto `skip_gate.rebuild_requested()`; no follow-up owed (INF_C_02 retrofitted). |
| **CTO 1.0.0** | CC on RAVC2 — the re-inline-drift root cause is removed; the next rebuild chain run will genuinely re-materialize all 5 dims. |
