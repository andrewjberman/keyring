# version_pin coverage derivation + coverage-mutant battery class + 07_maturity prose fix — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch 20260725T112844Z (CVO~Z cycle 13, routed; off-main-fabric group)
**Status:** COMPLETE
**Cycle wall:** ~11:28Z dispatch (queued) → ~11:55Z committed

---

## Objective

The pin fixed the predicate; the coverage was still hand-listed — `cse_schema @0.4` survived live in
07_maturity.md while the 1-file pin passed (predicate insensitivity and coverage insufficiency are
independent axes). In CVO~Z's order: derive the site denominator at run time (both units), report what
the rulebank hand-list missed, add the COVERAGE-MUTANT battery class, THEN fix the prose so the widened
check verifies the fix.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| site-population measurement | tracked-file sweep for both prefixes (pre-build) | 2 false-sites found | "rule-bank vocab" + a ledger marker-quote match bare prefix → predicate refined to prefix+DIGIT before building |
| `commit-gate` | on edited `system_parity.py` | PASS | clean |
| `system_parity.py` | `--self-test` | **26/26 rc=0** | 4 new COVERAGE-MUTANT cells (22–25); 21 predicate cells + negative unchanged |
| `system_parity.py` | `--self-test-negative` | 25/26 **rc=1** | still reddens |
| `system_parity.py` | `--worktree --domain ontology` (PRE-prose-fix) | ont-cse **FAIL naming 07_maturity.md** | "1 of 3 enumerated assertion site(s) STALE"; rulebank: both limbs FAIL, 6 of 7 sites stale v1.1, all named |
| `system_parity.py` | same (POST-prose-fix) | ont-cse **PASS** | "every enumerated assertion site current [coverage: 3 …]" — the check verified the fix |

**What worked:** measuring the true site populations BEFORE building surfaced both design forks early
(the false-site predicate problem; the vacuous-pass hole that pure hand-list-death would open on the
rulebank unit) — both resolved by design and stated as divergences in the memo rather than silently
implemented.

**What failed:** nothing this cycle.

**Gap found (routed):** the rulebank unit's REAL site population — 4 hand-listed files carry no
assertion at all; 7 true sites exist, 6 stale at v1.1 (sdk tenants/examples), only scaffold.py current.
By-design-vs-stale is the owner's call.

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. `_coverage_sites()` (vintage-respecting git enumeration; prefix+digit assertion predicate;
   `__pycache__` + fixed 2-file self-exclusion, printed; raises → ASSUMPTION).
2. `_version_pin` coverage limb (opt-in `coverage_root`); both contract units migrated; required-files
   limb kept at original any-of semantics (design divergence #1, memo §1).
3. Battery cells 22–25 (coverage mutants both shapes + green + fail-closed); negative renumbered 26.
4. Prose fix landed LAST: `07_maturity.md:13` `@0.4 → @0.5`, with the pin FAIL→PASS sequence captured.

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/system/system_parity.py` | `_coverage_sites` + coverage limb + 4 battery cells | This session, this lane |
| `infra/system/scope_contract.json` | `coverage_root` on both version_pin units | This session, this lane |
| `infra/system/07_maturity.md` | 1 word: `@0.4 → @0.5` (landed after the widened pin) | This session, this lane |
| `.../NFRA_TOOLUNIFY_CENSUS/VERSION_PIN_COVERAGE_C.md` | New memo | No — CTO~Z tree, on disk |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

## Blockers

None.

## Current State

Both version_pin units now derive their site denominator at run time; the battery holds coverage
mutants; the prose fix was verified by the check it widened. Rulebank's 6 stale sdk sites routed for
owner disposition. Reported to CTO~Z + CVO~Z this turn.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify with your pre-named check (cell 22 is it, synthetic; §2's pre-fix run is
   it, live); attack surfaces listed in memo §5.
2. **[1.0.0_SA_CTO~Z]** Dispose the rulebank 6-site staleness (by-design → exclusion-with-reason or
   per-site pin; stale → DENOM item A widens); commit the census-path memo.
3. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.
