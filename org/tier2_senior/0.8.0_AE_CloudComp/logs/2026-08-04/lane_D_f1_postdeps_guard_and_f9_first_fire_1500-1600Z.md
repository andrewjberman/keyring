# F1 postdeps two-half guard landed + F9 first real fire OBSERVED GREEN -- 0.8.0_AE_CloudComp~D

**archetype:** IMPLEMENT

Window: 2026-08-04 ~1500Z -> ~1600Z. TO: `ADHOC.comp-pipescript-postdeps-f1-guard` (SEV-HIGH,
$22M-class guard). Both TOs of the COO GO now COMPLETE: F9 @783d508 (+first fire @9b0340a87),
F1 @9b0340a87.

---

## F1: what landed (@9b0340a87)

**Half (a) -- unknown script_id rc=2 with a DERIVED universe.** `cmd_postdeps` now
discriminates UNKNOWN (rc=2 REFUSED, tree + universe size + resolution source printed) from
KNOWN-with-no-deps (rc=0 "No dependencies declared" preserved -- a true answer). Universe =
tree DAG script ids (`_build_dag(_FIRM_TO_PIPELINE[firm])`) UNION deps-config keys, derived at
runtime from the SAME maps the tool resolves trees from -- predicate-not-roster
(`pipeline_cli.py` cmd_postdeps tail @9b0340a87). ~B's assets-tree widening extends it with
zero edits to the guard. `build_canonical_prices` (a deps key that is NOT a tree DAG id) pins
the UNION in the permanent fixture.

**Half (b) -- NAMED-DEFAULT-LOUD, required-flag REJECTED by the live-caller inventory** (the
TO's own decision rule). Inventory found 3 LIVE flagless call sites, all dispatch gates with
rc+stderr swallowed and stdout-grep parsing (`[BLOCKING] Must run:`):
- `data/black_diamond/scripts/gold/gold_dispatch.sh:596` (check_partial_deps) -- WORKS today
- `data/cot/scripts/gold/gold_dispatch.sh` check_partial_deps -- VACUOUS today (bare cot ids
  vs bd config)
- `data/inf/scripts/gold/orion-gold-dispatch.sh` check_partial_deps -- same class
A flagless rc=2 = empty stdout = zero BLOCKING lines = the WORKING bd $22M-class gate passes
VACUOUSLY -- the exact silent caller-break the TO forbids. With half (a) live, the composition
(flagless + typo) still dies rc=2. Verified live post-fix: flagless `build_canonical_prices`
still prints its BLOCKING line rc=0 (bd caller contract intact) with the DEFAULT-TREE NOTICE
above it.

**The composition fixture** `test_pipescript_postdeps_guard.py` (5 tests) is a PERMANENT suite
member: run against the PRE-fix engine = 3 failed / 2 preservation passed (discriminates);
post-fix = 5/5. Suite denominator 46 -> 51.

**Regression:** io + deployed on one script per tree (bd A_00 / inf INF_A_04 / cot A_00 /
mdpf build_aggregate_aua_timeseries): 8/8 captures BYTE-IDENTICAL pre/post. No behavior change
to io/deployed/stats/inject; WS4 `:270` stub untouched. commit-gate clean on both .py files.

## F9: FULL ACCEPTANCE DISCHARGED

The F1 landing commit @9b0340a87 staged `pipeline_cli.py` + `test_pipescript_postdeps_guard.py`
-> the gate fired on a real, non-authoring commit:

```
[pipescript-suite-gate] watched path staged -- running the comp-pipescript suite (6 files) ...
[pipescript-suite-gate] OK: 51 passed in 24.45s
```

- 6 files: the new fixture AUTO-ENROLLED via the `test_pipescript_*.py` glob, ZERO gate edits
  (TO F9 scope 4 proven on a live commit).
- Audit trail (`org/pipescript-suite-gate-audit.log`): smoke PERMITTED 46 -> mutant DENIED ->
  first-fire PERMITTED 51, each line carrying author + denominator + trigger paths.
- Per `feedback_gate_accepted_on_observed_green_run_never_authoring_commit`: observed green on
  a non-authoring commit = full acceptance (was ACCEPTED-AT-BUILD @783d508).

## Compiler Tools (this window)

| Tool | Invocation | Result vs expect |
|---|---|---|
| comp-pipescript | `postdeps ZZZ_NO_SUCH_SCRIPT.py --firm bd` (pre-fix, pipe-free rc) | rc=0 false-clean reproduced = expect PASS |
| comp-pipescript | `postdeps ZZZ_NO_SUCH_SCRIPT.py` flagless (pre-fix) | rc=0 silent `[bd]` reproduced = expect PASS |
| comp-pydeps | `consumers pipeline_cli` | 5 consumers, no new since TO authoring = expect PASS |
| pytest | 5-file suite pre-edit | 46 passed baseline green = expect PASS |
| pytest | new fixture vs PRE-fix engine | 3 failed / 2 passed -- discriminates = expect PASS |
| pytest | full 6-file suite post-fix | 51 passed = expect PASS |
| comp-pipescript | post-fix controls (a)+(b), identical invocations | rc=2 both; (a) names tree+universe(35 distinct); (b) composition refused under loud default = expect PASS |
| comp-pipescript | io+deployed x 4 trees pre/post | 8/8 byte-identical = expect PASS |
| comp-grep | `postdeps` caller inventory (.tools/data/infra/org-modules) | 3 live flagless callers found -- decision datum for half (b) |
| commit-gate.sh | both .py files | rc=0 clean |

## Routed / surfaced (not mine)

1. **[COO]** cot + inf dispatch postdeps gates are VACUOUS today (bare ids vs bd config;
   pre-existing). Caller fix = add `--firm cot` / `--firm inf` at the call sites + EC2 deploy
   cycle (DS/AE lanes). bd call site works; NOT touched per TO scope.
2. **[COO]** `org/modules/graph/tests/test_adapter_audit.py` is COLLECTION-BROKEN at HEAD
   (imports `adapter_audit_cli.py`, absent -- likely mass-deletion residue); any whole-dir
   pytest run of the tests dir dies at collection.
3. **[CTO]** `org/pipescript-suite-gate-audit.log` tracked-or-not: my lane holds no ownership
   on that path (owned-paths exercised False); rcg-sweep-audit precedent says GOVERNANCE_AUDIT
   lane + un-gitignore. CTO's call.
4. **[CVO]** re-dial trigger 5: engine/subparser changed @9b0340a87 (MCP sent this window).

## Blockers

None.

-- 0.8.0_AE_CloudComp~D
