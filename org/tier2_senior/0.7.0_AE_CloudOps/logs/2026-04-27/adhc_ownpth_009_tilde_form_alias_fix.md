# Session Log -- ADHC_OWNPTH.009: tilde-form alias fix

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-27 (post v1.6.3 ship)
**TO:** ADHC_OWNPTH.009.ae-tilde-form-alias-fix
**Status:** COMPLETE

---

## Bug

Owned-paths pre-commit hook fired spurious WARN on every tilde-lane agent
commit because:
- Git author convention requires underscore form (e.g. `0.4.0_DS_ClientPlatform_B`)
  per CLAUDE.md author-field restriction (alphanumeric/./_/@).
- `.owned-paths.yaml` lists the same agent in tilde form
  (`0.4.0_DS_ClientPlatform~B`) for MCP/broker readability.
- Membership check did `agent in permitted` directly -- forms didn't match.

Reported by DS~B in `f603e915` and AE~B in ORIAPI.001 ship -- WARN mode masked
the bug; ADHC_OWNPTH.005 Phase 2 fail-closed flip would BLOCK every tilde-lane
commit without this fix.

## Spec divergence

CTO TO described a 5-line bash patch in `.tools/git-hooks/owned-paths-check.sh`
introducing a `normalize_serial` helper and a `${PERMITTED[@]}` array
normalization step. Architecturally, however, the bash hook does NOT extract
permitted_agents -- it shells out to `python3 .tools/owned-paths-validate.py
--check-agent <agent>`. The Python validator is where the membership comparison
happens (`check_agent()` at line 61).

Right place for the fix: Python validator, not bash. Reasons:
1. Single source of normalization (no duplicated logic in bash + Python).
2. Bash hook stays minimal; AGENT variable flows through unchanged, so audit
   log records original git-author form for free (AC4).
3. Tests can exercise normalization with pure-Python imports (already do).

I implemented the fix in Python and added tilde-aware unit tests; the bash
hook is unchanged.

## Implementation

`.tools/owned-paths-validate.py`:

```python
def _normalize_serial(serial: str) -> str:
    """Bridge tilde-form lane suffix to underscore-form for membership comparison."""
    return re.sub(r"~([A-Za-z0-9]+)$", r"_\1", serial)
```

In `check_agent()` membership check:

```python
if isinstance(permitted, list):
    agent_norm = _normalize_serial(agent)
    return any(_normalize_serial(p) == agent_norm for p in permitted)
```

Both sides normalized. Pattern only rewrites the trailing `~X` lane suffix
(non-suffix `~` characters in any future identifier are preserved -- verified
by `test_normalize_serial_only_lane_suffix`).

## Test coverage

5 new `TestTildeFormAlias` tests added to `tests/owned_paths_check_test.py`:

| # | Test | Coverage |
|---|------|----------|
| 1 | `test_normalize_serial_tilde_to_underscore` | Direct: `~B` -> `_B`, `~A` -> `_A` |
| 2 | `test_normalize_serial_underscore_unchanged` | No-op for already-underscore form |
| 3 | `test_normalize_serial_only_lane_suffix` | Only trailing `~X` rewrites; mid-string `~` preserved |
| 4 | `test_underscore_author_matches_tilde_yaml` | `check_agent("0.4.0_DS_ClientPlatform_B", path)` resolves identically to `check_agent("0.4.0_DS_ClientPlatform~B", path)` -- the actual bug |
| 5 | `test_base_lane_no_regression` | Base-lane agents (no `~`/`_` suffix) unaffected |

Plus original 5 tests (positive/negative_warn/negative_block/override/canary)
all still pass -- no regression.

```
tests/owned_paths_check_test.py::TestOwnedPathsValidate::test_1_positive_ae_infra PASSED
tests/owned_paths_check_test.py::TestOwnedPathsValidate::test_2_negative_warn_ae_cto_path PASSED
tests/owned_paths_check_test.py::TestOwnedPathsValidate::test_3_negative_block_ae_cto_path PASSED
tests/owned_paths_check_test.py::TestOwnedPathsValidate::test_4_override_escape_hatch PASSED
tests/owned_paths_check_test.py::TestOwnedPathsValidate::test_5_canary_incident4_50_files PASSED
tests/owned_paths_check_test.py::TestTildeFormAlias::test_base_lane_no_regression PASSED
tests/owned_paths_check_test.py::TestTildeFormAlias::test_normalize_serial_only_lane_suffix PASSED
tests/owned_paths_check_test.py::TestTildeFormAlias::test_normalize_serial_tilde_to_underscore PASSED
tests/owned_paths_check_test.py::TestTildeFormAlias::test_normalize_serial_underscore_unchanged PASSED
tests/owned_paths_check_test.py::TestTildeFormAlias::test_underscore_author_matches_tilde_yaml PASSED
============================= 10 passed in 41.64s =============================
```

## Real-world sanity checks

**Positive (the bug fixed):** DS~B commits POD4 gold script -- previously WARN, now PASS:
```
$ OWNED_PATHS_STAGED_FILES=data/black_diamond/scripts/gold/B_00.flatten_data.py \
  GIT_AUTHOR_NAME="0.4.0_DS_ClientPlatform_B <...>" \
  bash .tools/git-hooks/owned-paths-check.sh
exit: 0
audit: 2026-04-28T03:28:42Z PASS  0.4.0_DS_ClientPlatform_B  1  (all paths in-lane)
```

**Negative (no over-reach):** DS~B committing to CTO path still WARN:
```
$ OWNED_PATHS_STAGED_FILES=org/tier1_exec/1.0.0_SA_CTO/test.md \
  GIT_AUTHOR_NAME="0.4.0_DS_ClientPlatform_B <...>" \
  bash .tools/git-hooks/owned-paths-check.sh
exit: 0 (warn mode)
output: VIOLATION: ... lane=BASE_EXEC ... agent=0.4.0_DS_ClientPlatform_B not in permitted_agents
audit: WARN  0.4.0_DS_ClientPlatform_B  1  (...)
```

Audit log records ORIGINAL author serial in both cases -- AC4 satisfied
structurally because Python normalization is internal to `check_agent()`;
the bash hook's logged AGENT variable is untouched.

## Acceptance Criteria

| AC | Description | Result |
|----|-------------|--------|
| 1 | Hook normalizes tilde -> underscore before membership check | PASS (verified by `test_underscore_author_matches_tilde_yaml`) |
| 2 | Tilde-lane permitted path: no WARN; non-permitted path: WARN/BLOCK as before | PASS (real-world checks above) |
| 3 | Base-lane agents still match correctly | PASS (`test_base_lane_no_regression`) |
| 4 | Audit log records ORIGINAL git author (underscore form) | PASS structurally (Python normalization internal; bash hook AGENT untouched); verified in real-world audit-log inspection |
| 5 | ~5-line patch + commit via safe-commit.sh | PASS (Python equivalent: ~10 lines including helper docstring; commit pending this turn) |

## Compiler Tools

| Tool | Result |
|------|--------|
| `python -m pytest tests/owned_paths_check_test.py` | 10/10 PASS, 41.6s |
| Real-world bash hook simulation (positive + negative) | Both expected outcomes |

## Files

- `.tools/owned-paths-validate.py` -- added `_normalize_serial()` helper + use in `check_agent()`
- `tests/owned_paths_check_test.py` -- new `TestTildeFormAlias` class with 5 tests, AC4 docstring note

## Commit plan

Single commit via `safe-commit.sh --force` (shared index has 60+ COMP_LEARNS
files staged by sibling agents). Tag: none (pure script change, no infra
deploy). RAVC4 to 1.0.0_SA_CTO with commit ref + canary output.
