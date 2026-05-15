# DS~C Session 3 — ADHC_COMPIL_V4.029a safe_json_serialize.py shared util lift

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~C
**Authorization:** COO GO (16:30Z broker push) — RAVC1 ACK 16:32:47Z
**TO:** ADHC_COMPIL_V4.029a (Wave 2.a cross-pod hygiene, ~4-6h SLA)
**Commit:** `e0f51a147`
**Wall time:** ~30 min RAVC1 ACK → safe-deploy PASS (well under 4-6h estimate — convention reuse + DS~D's lib/ scaffolding made it fast)

## TL;DR

Lift the `_strip_nan` + `allow_nan=False` defense-in-depth pattern from `INF_D_00c.portal_leaderboard.py` (anchor `de2286d67` earlier this session) to a shared utility at `data/orion/scripts/gold/lib/safe_json_serialize.py`. Pairs with downstream `.029b comp-validate gold-nan` audit tool (AE 0.7) which enumerates every gold-script JSON-emit boundary and audits for shared-util consumption vs inline-or-unguarded.

Single new util file + new test suite (24 cases, all PASS) + 2 reference migrations (INF_D_00c removes its inline helper; INF_D_04 picks up defense at previously-unguarded `_write_json_s3`). Total +325/-24 across 4 files. No forced backfill on the remaining ~13-18 gold-script JSON-emit sites per PRD AC2 — opportunistic per-script during normal maintenance.

## Phase 1 — before-write design

**Existing inline implementations enumerated** (compliance baseline for `.029b` audit):

```bash
grep -rn "_strip_nan\|allow_nan=False" data/orion/scripts/gold/
# data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py — only file with inline _strip_nan
```

Just 1 file (INF_D_00c) — confirmed `de2286d67` is the only anchor.

**Total JSON-emit candidates** (informs .029b scope):

```bash
grep -rn "json\.dumps\|json\.dump\b" data/orion/scripts/gold/
# 58 occurrences across 42 files
```

~13-18 of these are gold-script S3-emit sites (the rest are logging / debug / dry-run prints). Per PRD AC2 framing, those migrate opportunistically.

**Convention discovery — lib/ subdir setup** (per DS~D INFINC.001 `d88b7a7a4`):
- `lib/__init__.py` exists (just `from __future__ import annotations`)
- Existing modules (~12): `dtype_coerce`, `tax_status`, `txn_cache_reader`, `skip_gate`, `empty_sentinel`, `schema_version`, `partition_provenance`, `inflection_rep_scope`, `display_label`, `ticker_overrides`, `parity_check_group_d`
- `lib/tests/` subdir exists with `__init__.py` + 4 test modules

**Import convention** (per `INF_A_00.accounts_dimension.py:75-82`):
```python
sys.path.insert(0, str(Path(__file__).parent / 'lib'))
from dtype_coerce import coerce_id_columns  # noqa: E402
```

**Test convention** (per `lib/tests/test_empty_sentinel.py`):
- `unittest` framework (not pytest)
- `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))` for sibling import
- Run from `data/orion/scripts/gold/`: `python -m unittest lib.tests.test_NAME -v`

COO RAVC1 ACCEPTED 16:33Z confirmed plan tracks + lib/ scaffolding compatible.

## Phase 2 — implementation

### `lib/safe_json_serialize.py` (new file, 88 LOC)

Two exported functions:

```python
def strip_nan(obj: Any) -> Any:
    """Recursively replace non-finite floats (NaN, +Inf, -Inf) with None."""
    if isinstance(obj, dict):
        return {k: strip_nan(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [strip_nan(v) for v in obj]
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    return obj


def safe_json_dumps(obj: Any, **kwargs: Any) -> str:
    """json.dumps wrapped with auto strip_nan + allow_nan=False tripwire."""
    if "allow_nan" in kwargs:
        raise TypeError(
            "safe_json_dumps sets allow_nan=False internally; "
            "pass it through json.dumps directly if you need allow_nan=True."
        )
    return json.dumps(strip_nan(obj), allow_nan=False, **kwargs)
```

Module docstring documents the anchor commit (`de2286d67`), the defense-in-depth rationale (strip = fix, tripwire = fail-loud assertion), and the migration pattern (single-LOC import + single-call swap).

`math.isfinite()` is the predicate — covers NaN + +Inf + -Inf in one call. Tuples convert to lists (matches json.dumps semantics). `allow_nan` kwarg passthrough is BLOCKED via TypeError — callers that genuinely want NaN emission must use `json.dumps` directly with documented justification.

### `lib/tests/test_safe_json_serialize.py` (new file, 145 LOC)

24 test cases across 2 TestCase classes:

**TestStripNan (13 cases):**
- Leaf NaN/+Inf/-Inf → None
- Finite float/int/str/bool/None passthrough
- Dict with NaN value + key preservation
- List/tuple with NaN element + tuple → list conversion
- Deeply nested dict-list-dict with mixed NaN/Inf
- Empty dict/list passthrough
- Idempotence (`strip(strip(x)) == strip(x)`)

**TestSafeJsonDumps (11 cases):**
- Basic dict roundtrip
- Strips NaN before dump
- Strips Inf before dump
- Kwargs forwarded (separators, default, indent)
- allow_nan kwarg raises TypeError (both True and False)
- Tripwire allow_nan=False raises ValueError when strip is monkey-patched out
- End-to-end platinum-shape payload roundtrip
- No NaN/Infinity tokens in output assertion
- math.isfinite documentary test

**Result:** `Ran 24 tests in 0.001s — OK`.

### Reference migrations (AC3 — ≥2 required)

**INF_D_00c.portal_leaderboard.py:**
- Removed inline `_strip_nan` helper (~20 LOC)
- Removed `import math` (no other consumer)
- Added `from pathlib import Path`
- Added `sys.path.insert(0, str(Path(__file__).parent / 'lib'))`
- Added `from safe_json_serialize import safe_json_dumps  # noqa: E402`
- Changed `_write_json_s3` body to consume `safe_json_dumps`
- Net: clean ~20-LOC reduction; semantic identical

**INF_D_04.client_portal_summary.py:**
- Added `from pathlib import Path`
- Added `sys.path.insert(0, str(Path(__file__).parent / 'lib'))`
- Added `from safe_json_serialize import safe_json_dumps  # noqa: E402`
- Changed `_write_json_s3` body to consume `safe_json_dumps`
- Net: opportunistic defense-in-depth add to a previously-unguarded write boundary

The 2 migrations also serve as Tier 1 compliance examples for AE 0.7's `.029b` audit tool baseline.

## Phase 3 — verification + deploy

| Step | Result |
|---|---|
| `.tools/ds-commit-gate.sh` on all 4 files | 4/4 PASS (py_compile + AST + ruff py39 0.15.11) |
| `python -m unittest lib.tests.test_safe_json_serialize -v` | 24/24 PASS in 0.001s |
| End-to-end import smoke (stubbed boto3) on INF_D_00c | Module load OK; `_write_json_s3` strips NaN → 51-byte JSON output |
| End-to-end import smoke (stubbed boto3) on INF_D_04 | Module load OK; `_write_json_s3` strips Inf → 51-byte JSON output |
| `git add` (new files) + `.tools/safe-commit.sh` | Clean commit `e0f51a147` |
| `git push origin CLOUD` (triggers safe-deploy.sh) | safe-deploy PASS — 4 files deployed to `opal-data-inf/code/gold/` |
| `aws s3api head-object` SHA-MATCH verify | All 3 key artifacts fresh @ 16:39:26-35Z |

**S3 ETags:**
- `lib/safe_json_serialize.py`: `87207922d2d312ff93fee7372ae1d478` @ 16:39:35Z, 4,859 bytes
- `INF_D_00c.portal_leaderboard.py`: `a66900c9a18a0bfcb465440fdf521d9b` @ 16:39:26Z
- `INF_D_04.client_portal_summary.py`: `815e4457614ffd84361ac9a0f0dd4e1d` @ 16:39:31Z
- `lib/tests/test_safe_json_serialize.py`: deployed (S3 ETag check skipped — runtime doesn't pull tests but safe-deploy uploaded)

## Files Modified

| File | Change | Action |
|---|---|---|
| `data/orion/scripts/gold/lib/safe_json_serialize.py` | new 88 LOC | create |
| `data/orion/scripts/gold/lib/tests/test_safe_json_serialize.py` | new 145 LOC | create |
| `data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` | -20/+4 (inline `_strip_nan` removed, util consumed) | modify |
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | +5 (sys.path + import + util-consumed `_write_json_s3` body) | modify |

**Total:** +325/-24 across 4 files; 1 commit (`e0f51a147`).

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | `safe_json_serialize.py` exports `safe_json_dumps()` + `strip_nan()` | ✓ |
| AC2 | Tests cover leaf NaN, nested NaN/Inf, negative tripwire, edge cases (dict/list/tuple) | ✓ 24/24 PASS |
| AC3 | ≥2 reference migrations on existing scripts | ✓ INF_D_00c + INF_D_04 |
| AC4 | ds-commit-gate.sh PASS (+ `from __future__ import annotations` first import per Rule 15) | ✓ 4/4 PASS |
| AC5 | safe-deploy.sh SHA-MATCH on S3 | ✓ all 3 key artifacts verified |
| AC6 | AE 0.7 `.029b` dispatch-unblock signal sent | ✓ this turn |
| AC7 | Session log + RAVC2 MCP to COO + CC AE 0.7 | ✓ this log + RAVC2 16:40:21Z + AE signal 16:40:33Z |

All 7 ACs satisfied at commit/log/MCP completion.

## Compiler Tools

| Tool | Runs | Findings |
|---|---|---|
| `grep -rn "_strip_nan\|allow_nan=False"` on `data/orion/scripts/gold/` | 1 | 1 file (INF_D_00c) — confirms `de2286d67` is only anchor |
| `grep -rn "json\.dumps\|json\.dump"` on `data/orion/scripts/gold/` | 1 | 58 occurrences across 42 files — informs `.029b` audit scope |
| `grep -rn "from lib\.\|from \.lib"` | 1 | No matches — DS~D's convention is `sys.path.insert` + bare `from MODULE import NAME`, not `from lib.MODULE` |
| `Read lib/dtype_coerce.py` (existing module reference) | 1 | Type hints + `from __future__ import annotations` + idempotent docstring pattern confirmed |
| `Read lib/tests/test_empty_sentinel.py` (existing test reference) | 1 | `unittest` framework + `sys.path.insert` for sibling import + run command pattern confirmed |
| `.tools/ds-commit-gate.sh` | 1 (on 4 files in one invocation) | 4/4 PASS |
| `python -m unittest lib.tests.test_safe_json_serialize -v` | 1 | 24/24 PASS |
| End-to-end import smoke (stubbed boto3) | 1 | Both INF_D_00c + INF_D_04 load + NaN/Inf strip through `_write_json_s3` |
| `.tools/safe-commit.sh --author=...` | 1 | Clean commit `e0f51a147` (after `git add` for new files per ADHC_OWNPTH gotcha) |
| `.tools/safe-deploy.sh` (pre-push hook) | 1 | DEPLOYED [inf] 4 files PASS |
| `aws s3api head-object` SHA-MATCH | 3 | All 3 key artifacts fresh @ 16:39Z |

**Gotcha caught:** `safe-commit.sh --only` on path that includes NEW files fails with `pathspec 'X' did not match any file(s) known to git`. Fixed per CLAUDE.md 14a — `git add data/orion/scripts/gold/lib/safe_json_serialize.py data/orion/scripts/gold/lib/tests/test_safe_json_serialize.py` first, then `safe-commit.sh --only -- <paths>`. The wrapper still applies its contamination guard via the staged index → working-tree diff comparison.

**Compiler-tool gaps reaffirmed (no new findings):**
- `comp-pipescript deployed` bucket-scope for INF — verified via direct head-object instead
- `comp-platinum reverse` not applicable (lib code, not platinum emit)

## MCPs Sent

| To | At (Z) | Subject |
|---|---|---|
| 2.0.0_SA_COO | 16:32:47 | RAVC1 ACK — ADHC_COMPIL_V4.029a starting |
| 2.0.0_SA_COO | 16:40:21 | RAVC2 — ADHC_COMPIL_V4.029a SHIPPED — e0f51a147 |
| 0.7.0_AE_CloudOps | 16:40:33 | ADHC_COMPIL_V4.029a dispatch-unblock — canonical path live for .029b |

## MCPs Received

| From | Subject | Disposition |
|---|---|---|
| 2.0.0_SA_COO (~16:30Z broker push) | GO — ADHC_COMPIL_V4.029a Wave 2.a | ACKed + executed |
| 2.0.0_SA_COO (~16:33Z) | RAVC1 ACCEPTED — plan tracks; lib/ subdir already exists per DS~D | Plan confirmed; proceeded |

## Next Steps

| Recipient | Item |
|---|---|
| **2.0.0_SA_COO** | Ratify RAVC2 + signal AE 0.7 for `.029b` dispatch unblock. |
| **0.7.0_AE_CloudOps** | Build `.029b comp-validate gold-nan` audit tool. Spec includes 4-tier compliance taxonomy (full util / strip-only / inline / unguarded) per my dispatch-unblock signal. Reference migrations at INF_D_00c + INF_D_04 are Tier 1 examples. |
| **Future agents** | Opportunistic migration during normal maintenance touches on remaining ~13-18 gold-script JSON-emit sites. AE's audit tool surfaces gaps. |
| **Self — passive** | Standing by /loop watchdog. The util is now consumable by any gold script in the orion tree. |

## Decision Notes

1. **One commit for all 4 files vs split commits.** Single commit — the migrations DEPEND on the util being in the same tree. Splitting would make individual commits non-compileable (migrated scripts can't import a util that doesn't exist yet). Atomic .029a ship matches the TO's scope framing.

2. **Migration pattern follows DS~D's convention exactly.** Initially wrote module docstring with `from lib.safe_json_serialize import ...` (Python package style). Switched to `sys.path.insert` + bare `from MODULE import NAME` after reading DS~D's existing INF_A_00.accounts_dimension.py:75-82 — cross-pod consistency matters more than Pythonic-package style for this lib pattern.

3. **`allow_nan` kwarg blocked at API boundary.** `safe_json_dumps` raises TypeError if caller passes `allow_nan` in either direction. Rationale: the util's contract is "defense-in-depth with tripwire" — caller-overridable allow_nan defeats the tripwire. If a caller genuinely needs NaN emission, they should use `json.dumps` directly with explicit documentation, not silently bypass the safety via the util. Explicit > implicit.

4. **`math.isfinite()` over `math.isnan() or math.isinf()`.** Single predicate covering all three non-finite IEEE-754 cases (NaN + +Inf + -Inf). Cleaner + matches the anchor `de2286d67` choice.

5. **Tuple → list conversion in strip_nan.** `json.dumps` serializes tuples as JSON arrays anyway, so the conversion is semantically neutral. Returning consistent type (always list) makes the function output predictable for downstream consumers that might inspect the structure post-strip.

6. **No forced backfill per AC2.** ~13-18 other JSON-emit sites stay unguarded until normal maintenance touches them. AE's `.029b` audit tool provides the visibility; opportunistic migration is the disposition. Forcing a backfill wave would create blast-radius surface that's not worth the risk for a non-P0 hygiene improvement.

7. **End-to-end import smoke vs only unit tests.** Unit tests verify the util in isolation; the smoke test verifies the lib import actually resolves at module-load time for the migrated scripts (`sys.path.insert` runs at import time, not at `py_compile`). Both gates needed — `ds-commit-gate.sh` doesn't catch a broken import path.

## Session Telemetry

- Wall time: ~30 min RAVC1 → safe-deploy PASS (well under 4-6h TO estimate)
- 1 substantive commit (e0f51a147)
- 4 files modified (+325/-24 total)
- 2 MCPs sent post-ship (RAVC2 COO + AE dispatch-unblock)
- 1 MCP sent pre-ship (RAVC1 ACK)
- 2 MCPs received (GO + RAVC1 ACCEPT)
- 24 unit tests written + verified
- 1 end-to-end import smoke (stubbed boto3) confirming both migrations
- ds-commit-gate.sh PASS on first try (4/4)
- safe-deploy gate PASS on first try
- safe-commit.sh failed once on new-file pathspec; corrected via `git add` per CLAUDE.md 14a gotcha
- 0 escalations
- 0 merge conflicts (other agents had committed earlier; clean FF push)
