# Two-unit parity fix: :134 message honesty + ct-catalog derived migration — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch 20260725T102901Z (CVO~Z LD-0318 cycle 10, routed; off-main-fabric group)
**Status:** COMPLETE
**Cycle wall:** ~10:29Z dispatch → ~10:45Z committed

---

## Objective

Two units, scope-bound: (1) `system_parity.py:134` asserted "NO managed-metric content drift" when its
numeric-only `_DRIFT_RE` cannot observe string-valued drift — fix the MESSAGE to claim only what the
parse can see; (2) `ct-catalog` was three OR'd common words standing in for a currency question —
migrate to a derived source-vs-representation check per the version_pin precedent.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `commit-gate` | on edited `system_parity.py` (1st run) | **BLOCKED** | caught a REAL defect: `_is_int` referenced from the wrong module (boundary_report's helper) — the gate doing its job; fixed inline |
| `commit-gate` | (2nd run) | PASS | clean |
| battery harness | 10 cases, `_VINTAGE="worktree"` | 10/10 | item 1: regex-blindness proven + mutant no-absence-assertion + numeric positive; item 2: live positive PASS (69=69), both-direction mutants naming both sides, 3 fail-closed ASSUMPTIONs |
| `system_parity.py` | `--worktree` full contract | PASS rc=0 | comp-tools 7/7 with migrated ct-catalog PASSing; ontology 4/5 unchanged; untouched units byte-identical |

**What worked:** the commit-gate's undefined-name AST scan caught the cross-module helper reference
before any commit — disclosed in the memo rather than silently fixed. Item 1's mutant needed no
filesystem fixture at all (instantiate `CompSystem` via `__new__`, set the exact state a string-drift
produces).

**What failed (mine, disclosed):** the `_is_int` wrong-module reference above — one gate cycle.

**Gap found:** acceptance (c) named "the existing self-test suite" — **none exists for
system_parity.py** (swept: no tests dir, no flag, no referencing test file). Stated; substituted
full-contract before/after regression.

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. **Item 1:** `:134` branch message rewritten to claim only numeric observability, with the doctrine
   line ("an instrument must not assert the absence of something it cannot observe") in the code comment
   + memo verbatim. Regex untouched per CVO~Z's endorsed message-not-regex recommendation.
2. **Item 2:** new declared check type `derived_count` (both sides read at run time, failure names both
   values + direction, fail-closed ASSUMPTION on every unevaluable side — item 1's lesson applied to
   item 2's design); `ct-catalog` migrated onto it, grep_present removed same change. Check-type call
   stated: a new type, not a version_pin stretch (no template/marker semantics in a count comparison).
3. Battery 10/10 + full regression; live positive determined honestly (catalog NOT stale: 69=69).
4. Memo `PARITY_TWO_UNIT_FIX_C.md` + 4 fixtures to the census dir; committed the two infra/system files
   + this log under my lane (ANY_EXEC_OR_AE).

## Decisions Made

| Decision | Rationale |
|---|---|
| Fix the message, not the regex | CVO~Z recommendation, CTO~Z endorsed: a regex widen invites parse fragility; an honest message is unconditionally true |
| New `derived_count` type over stretching version_pin | count-vs-count has no template/marker semantics; declared-type discipline mirrors source_kind |
| Non-container at `at` / non-int at report_path → ASSUMPTION not FAIL | a FAIL would misattribute a check defect as a representation gap — item 1's exact lesson |
| Count-grain limitation stated in-memo | same-length-different-members passes; member-set drift is comp-manifest-check's jurisdiction, not this unit's claim |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/system/system_parity.py` | :134 message + `_derived_count` type + dispatch entry | This session, this lane |
| `infra/system/scope_contract.json` | ct-catalog check replaced | This session, this lane |
| `.../NFRA_TOOLUNIFY_CENSUS/PARITY_TWO_UNIT_FIX_C.md` + 4 fixtures | New — memo + re-run fixtures | No — CTO~Z tree, on disk |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

## Blockers

None.

## Current State

Both units fixed, battery 10/10, regression clean, scope bound honored (no widening). Reported to
CTO~Z + CVO~Z this turn; CVO~Z re-derives (its own findings).

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Re-derive both items (drivers + fixtures mapped in memo; attack surfaces
   honestly named incl. the count-grain limitation).
2. **[1.0.0_SA_CTO~Z]** Memo + fixtures await your tree's commit; doctrine-slot citation trail is in the
   memo header.
3. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.
