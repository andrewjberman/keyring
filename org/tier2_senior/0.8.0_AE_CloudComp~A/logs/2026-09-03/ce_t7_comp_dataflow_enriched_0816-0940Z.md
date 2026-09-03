# TO-CE-T-7 -- comp-dataflow honest-unresolved preserved + enriched print + Rule T -- 0.8.0_AE_CloudComp~A

**Date:** 2026-09-03
**Task Order:** NFRA_COMPEFFICACY.TO-CE-T-7.comp-dataflow-s4-audit
**Status:** COMPLETE (pending CVO grade + MSTR push)

---

## Objective

Deliver the s.4 per-tool audit for `comp-dataflow` (row T-7, cell CE-t-7, STAGE 2), preserve the
4/4 honest-unresolved read while enriching its print with a reason class (DYNAMIC-PATH /
DEPLOY-TIME-ONLY / FIRM-TREE-ABSENT / OTHER, never resolving anything by consulting deploy-time
config), and wire Rule T's form onto the tool's one corpus-width loop (the `gate` sweep). No
battery existed for this tool at cut.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read org/modules/graph/comp_dataflow.py --for "where a read is classified resolved or unresolved..."` (before write) | PASS | located `is_unresolved` (:280 at cut), the unresolved print (`cmd_origin`), and the summary counts (`_denominator`) exactly |
| comp-dataflow gate | a real baseline sweep over `data/` BEFORE any code change (the TO's own mandate: name the current specimens first) | PASS | 532 producer files, 1036 reads scanned, 604 unresolved -- 542 bare-`{*}` shapes, 62 partial-literal-no-layer-word shapes; this split is what grounded the DYNAMIC-PATH/FIRM-TREE-ABSENT design |
| commit-gate.sh | on `org/modules/graph/comp_dataflow.py`, `.tools/tests/test_comp_dataflow_battery.py` | PASS | clean, 2 of 2 |
| proof-of-spec-check.py | on this instance | see below | validated before the `complete` flip |

**What worked:** the TO's own required baseline sweep (before writing any code) turned out to be
load-bearing, not procedural -- it revealed the REAL population split (542 DYNAMIC-PATH-shaped /
62 FIRM-TREE-ABSENT-shaped / 0 of the other two classes), which is what grounded the classifier
design instead of guessing at four evenly-populated buckets. The exact taxonomy
(DYNAMIC-PATH/DEPLOY-TIME-ONLY/FIRM-TREE-ABSENT/OTHER) was confirmed by census to be minted fresh
by this TO itself (0 prior occurrences anywhere in the estate), so its precise meaning was this
seat's own design act, grounded in the real 604-row population rather than inherited from a spec.

**What failed, found, and fixed BEFORE the deliverable was finalized:** the PRESENT_WITH_ZERO_RESULTS
planted case was drafted against `data/mdpf/scripts/gold` on the assumption it would sweep clean --
it did not (`gate` found one real served-origin finding there once run for real). Caught by actually
EXECUTING every quoted command before publishing (Rule 22 discipline), not by reasoning from memory.
Replaced with `data/inf/scripts/silver`, verified live to sweep clean with a non-zero denominator.

**Gap found, not fixed (this cell's own new code, disclosed not hidden):** F4 -- a budget-limited
partial `gate` sweep with zero findings among the files it reached still returns rc=0, identical to
a genuinely complete clean sweep. Flagged as sharper here than the analogous finding in CE-t-1/
CE-t-2/CE-t-3, because this tool's archetype (a real GATE) binds rc to the verdict by design, unlike
the GRADED-MEASUREMENT archetype of the prior three tools.

---

## Work Completed

### 1. The enriched unresolved print, commit `8fdc3d0602`

A SEPARATE, ADDITIVE reason-classifier (`_unresolved_reason`, `_is_env_access`,
`_env_derived_names`) that never touches the existing `is_unresolved`/`resolved`/`layer`/`is_served`
fields (BOUNDS: enrichment on the print, not the classification). `_is_env_access` statically
detects `os.environ.get(...)`/`os.environ[...]`/`os.getenv(...)` shapes to power the
DEPLOY-TIME-ONLY label -- it NEVER evaluates the call or substitutes its value (BOUNDS: never guess
through deploy-time config). `cmd_origin`'s UNRESOLVED line now carries a `reason:` line beneath it;
`_denominator`'s enriched breakdown prints all four classes even at 0.

### 2. Rule T on the gate sweep, same commit

`cmd_gate`'s per-file loop is the tool's ONE corpus-width loop; wired with `--budget`/`--cursor`,
a shared `_compbudget.Clock`, deterministic sorted scan order, a real DEFERRED bucket, and the
WITHIN BUDGET / BUDGET REACHED tokens. `origin` (always exactly one file) carries no `--budget` flag
at all -- exercised and confirmed via `--help` on both subcommands. Cursor-resume exercised
end-to-end: re-running with the printed `--cursor` value skipped exactly the completed unit and
advanced to the next in sorted order.

### 3. New battery: `.tools/tests/test_comp_dataflow_battery.py`, same commit

8 of 8 `rec()`-calls PASS (4 logical arms as real+mutant pairs, plus two standalone regression
controls). The FIRST arm is the never-guess control the TO itself names: a mutant that lets an
unresolved Name fall back to a LIVE `os.environ` read (built in a scratch mirror tree matching
`comp_dataflow.py`'s own `_WS`-resolution depth -- three `.parent`s from the file to the workspace
root, mirroring `comp-which-routing-test.py`'s `build_mirror()` precedent) correctly RESOLVES the
DEPLOY-TIME-ONLY fixture when its env var is actually set in the mutant's process -- proving the
real code's refusal to do this is what the control certifies. Two further mutants (an all-OTHER
reason classifier, a carrier that ignores `--budget`) both FIRED-AS-EXPECTED. Two of the four
honest-unresolved specimens are REAL production files (named at cut by the baseline sweep); two
(DEPLOY-TIME-ONLY, OTHER) are PLANTED fixtures, since the live population currently has zero
occurrences of either -- disclosed honestly in the deliverable, not hidden, matching the s.4.3
enum's own "four planted cases" allowance.

### 4. Deliverable + proof instance

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.result.md`
(the T-16/T-1/T-2/T-3 shape, all 31 s.4 fields present or explicitly ABSENT with a reason) and its
proof instance, validated against `PROOF_OF_SPEC.schema.json` and `.tools/proof-of-spec-check.py`
before the `<status>` complete flip, which this seat commits itself.

---

## Acceptance (summary; full evidence in the deliverable + proof instance)

T7-AC1 (parses, 4.1 from the engine, shim named as shim) PASS · T7-AC2 (four planted cases on the
SOURCE plane, two findings F1/F2) PASS · T7-AC3 (4/4 honest-unresolved PRESERVED and ENRICHED, the
never-guess mutant fires) PASS · T7-AC4 (Rule T on gate, origin's non-application stated) PASS ·
T7-AC5 (new battery, never-guess first, 8/8 PASS both grains, directory grain stated) PASS ·
T7-AC6 (push state measured at report, not asserted).

---

## Push State

Measured in the commit report to `2.0.0_SA_COO`, not asserted here.
