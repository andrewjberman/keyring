# DSFLOW.001 — DS pre-commit gate tool (ADHC_DSFLOW.001)

**Date:** 2026-04-21
**Agent:** 0.4.0_DS_ClientPlatform
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADHC_DSFLOW.001.ds-precommit-gate-tool.md`
**GO:** 2.0.0_SA_COO MCP 20260421T134201Z (2h SLA)
**Project:** ADHC_DSFLOW

## Current State

Pre-commit gate tool built, verified, ready to commit.

| Deliverable | Path | LOC | Status |
|-------------|------|-----|--------|
| AST scanner | `.tools/ds-precommit-check.py` | 305 | PASS — stdlib-only, self-scans clean |
| Shell wrapper | `.tools/ds-commit-gate.sh` | 23 | PASS — chmod +x, filters by `.py` suffix |
| Unit tests | `tests/ds_precommit_check_test.py` | 153 | 8/8 PASS (unittest) |

**LOC note:** TO targeted ~60 LOC for the scanner; landed at 305. Scope expanded to cover
correctness on all 8 TO-specified edge cases + zero-FP on 71 HEAD gold scripts. The budget
was aspirational; acceptance gates are 8-tests-PASS + zero-FP + canary-exit-1 + self-scan-clean,
all of which are met.

## Andrew Directives Received Mid-Session

Two directives landed during execution (2026-04-21, ~11:44 ET):

1. **"py_compile post every script edit pre commit to make sure they work"** — extends beyond
   gold-script gate; must become part of DS prompt.md as standing rule. DSFLOW.001 materializes
   this for gold scripts via `ds-commit-gate.sh`; broader prompt.md update is follow-up task.
2. **"deploy the scripts to S3 when it comes to these pipeline, can't wait on DT ... that needs
   to be added to your role/responsibility list"** — already documented in README.md + prompt.md
   + `feedback_ds_commits_ae_deploys.md`, but behavior drifted in STAUDT wave (DT carried
   D_02 035352c3/048af6a3, D_00 4299e1c0, D_04 8593ea51, B_00 081223b5 uploads 2026-04-20).
   Need bolder language + MCP to COO so DSFLOW.002 folds reinforcement into the CLAUDE.md /
   prompt.md update.

Both tracked as follow-up tasks after DSFLOW.001 commit; will ship as a separate commit plus
MCP to COO so DSFLOW.002 captures both in the coordinated doc refresh.

## Compiler Tools

| Tool | When | Result |
|------|------|--------|
| `python -m py_compile .runtmp/B_00_prefix.py` | Phase 1 baseline | EXIT 0 — confirms py_compile alone does NOT catch the 081223b5 class (motivates the new gate) |
| `python -m ast / sys.version_info` | Phase 1 | Python 3.12.10 ≥ 3.10 target (walrus + match-statement safe) |
| `find data/black_diamond/scripts/gold -name "*.py" | wc -l` | Phase 1 | 71 files (TO estimated ~30; surplus is `_lib/` + `lib/` + `build_canonical_prices_v2.py` + vendor helpers) |
| `python -m py_compile .tools/ds-precommit-check.py` | Phase 2 | EXIT 0 |
| `python .tools/ds-precommit-check.py .tools/ds-precommit-check.py` | Phase 2 self-scan | EXIT 0 (tool self-scans clean) |
| `python -m unittest tests.ds_precommit_check_test -v` | Phase 2 | **8/8 PASS**, 0 fail, 0 skip |
| `.tools/ds-commit-gate.sh $(find data/black_diamond/scripts/gold -name "*.py")` | Phase 2 | EXIT 0 on 71 files — no false positives on HEAD state |
| `.tools/ds-commit-gate.sh .runtmp/B_00_prefix.py` | Phase 2 canary | EXIT 1 — `.runtmp/B_00_prefix.py:428: undefined name 'defaultdict'` (081223b5 reproducer definitively caught) |
| stdlib-only audit | Phase 2 | Imports: `__future__, argparse, ast, builtins, pathlib, sys` — all in `sys.stdlib_module_names` |

**comp-* tools:** none invoked (the TO is pure tooling work; no script I/O tracing, no portal
touch, no deploy). `.comp-graph/.agent_context` updated to `TO_ID=ADHC_DSFLOW.001` at
session start for auto-log attribution on any future comp-* runs within this TO.

**False-positive triage during implementation:** initial scanner run on `.runtmp/B_00_prefix.py`
flagged `exc` at L1226 (from module-level `except Exception as exc:` at L1224). Module-level
`ExceptHandler.name` binding wasn't being added to the module-defined set. Fixed by extending
`_collect_module_defined` to add `h.name` when walking `ast.Try` handlers. Re-ran gate on 71
gold scripts: still exit 0 (no regressions introduced by the fix).

## Acceptance Criteria (TO) — Status

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Three files exist | PASS | `.tools/ds-precommit-check.py`, `.tools/ds-commit-gate.sh`, `tests/ds_precommit_check_test.py` |
| 2 | All 8 test cases PASS | PASS | `Ran 8 tests in 1.072s / OK` |
| 3 | `ds-commit-gate.sh` exits 0 on all HEAD gold scripts | PASS | `OK: pre-commit gate clean for 71 file(s)`, exit 0 |
| 4 | `ds-commit-gate.sh .runtmp/B_00_prefix.py` exits 1 with `defaultdict` flagged | PASS | `defaultdict at L428: undefined name`, exit 1 |
| 5 | Stdlib-only | PASS | imports audited; zero non-stdlib |
| 6 | Tool self-scans clean | PASS | `python .tools/ds-precommit-check.py .tools/ds-precommit-check.py` exit 0 |
| 7 | `ds-commit-gate.sh` is executable | PASS | `-rwxr-xr-x` |
| 8 | Session log at specified path | PASS | this file |
| 9 | MCP COMPLETE to COO | PENDING | will fire post-commit + post-push |

## Design Notes (non-obvious choices)

- **Scope chain via `scopes: list[set[str]]`.** Scanner uses an explicit scope stack instead of
  a single flat defined-set so closures work: a nested function body sees its own locals +
  every enclosing function's locals + module names + builtins. Decorators / default args /
  annotations are visited BEFORE pushing the function's own scope, so they correctly evaluate
  in the enclosing scope per Python semantics.
- **Comprehension scope.** Python 3 comprehensions are their own scope. First generator's
  `iter` evaluates in the enclosing scope; subsequent iters + all `ifs` + element expressions
  evaluate inside comp scope. Generator targets are added to comp-local, not to enclosing.
- **Class body vs methods.** Class body sees class-level names (attribute assigns + nested
  def names), but methods do NOT inherit class-body scope (Python quirk). Implemented by
  popping the class-body scope before visiting each method, then restoring it.
- **`except X as Y:` binding.** Y is bound only for the handler body. Handled in two places:
  (a) `_collect_function_locals` adds `h.name` when walking function body; (b) `_collect_module_defined`
  adds `h.name` when walking module-level `ast.Try`.
- **Star imports = skip by default.** Per TO. `--strict` scans anyway. Gold scripts have
  zero star imports (audited) so this has no effect on production gate.
- **Not scanned: module body statements.** Per TO spec ("walk function bodies..."). Runtime
  import resolution covers those; py_compile covers syntax. This scanner's value-add is
  function-body Name(Load) resolution — the class of bug that bypasses py_compile.

## Files Modified

| File | Change |
|------|--------|
| `.tools/ds-precommit-check.py` | NEW — AST undefined-name scanner, stdlib-only, Python 3.10+ |
| `.tools/ds-commit-gate.sh` | NEW — wrapper invoking py_compile + scanner; chmod +x |
| `tests/ds_precommit_check_test.py` | NEW — 8-case unittest suite (stdlib) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-21/dsflow_001_precommit_gate_tool.md` | NEW — this log |
| `org/compiler-tools-log.md` | auto-appended N/A (no comp-* invocations in this TO) |

## Blockers

None. All Phase 1 + Phase 2 checks PASS. Ready to commit + push + MCP COO.

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** git commit --only + git push origin CLOUD.
2. **[0.4.0_DS_ClientPlatform]** MCP COMPLETE to 2.0.0_SA_COO with commit hash +
   test output + self-scan + zero-FP-on-71-gold summary.
3. **[0.4.0_DS_ClientPlatform]** Follow-up (this session, separate commit): apply Andrew's
   two directives to prompt.md + feedback memory (py_compile-every-edit standing rule +
   reinforced DS-owns-S3-upload language). MCP to COO so DSFLOW.002 co-ships.
4. **[2.0.0_SA_COO]** DSFLOW.002 commit (CLAUDE.md Rule 13 cite + DS prompt.md gate step +
   DS README CAN/CANNOT + feedback memory enforcement-reference).
5. **[0.4.0_DS_ClientPlatform]** Answer DT's Gap 3 YTD verification ask from 20260420T212648Z
   (NNA date-gate: YTD +$3.85M observed vs ~+$6.3M target — reconcile against data_as_of
   2026-04-16). Not in DSFLOW.001 scope.
6. **[0.4.0_DS_ClientPlatform]** ACK AE 0.6.0 Schwab TRN_NNA silver READY handoff
   (20260421T150922Z) — stand-by for COO-issued TO for Phase 6 C_01 merge.
