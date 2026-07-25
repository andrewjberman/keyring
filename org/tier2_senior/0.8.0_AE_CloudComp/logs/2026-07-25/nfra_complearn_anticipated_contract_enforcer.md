# ANTICIPATED owner+trigger contract — building its enforcer — 0.8.0_AE_CloudComp~E

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** follow-on to round-2 item 5 (CVO~Z finding 170032Z; CTO~Z dispatch 170636Z)
**Status:** DELIVERED — VERIFIED (CVO~Z 170651Z, by replay of its own mutant)
**Cycle wall:** ~1644Z–1708Z (session opened by respawn after mid-flight kill)

## Objective

Close the residual both execs found independently: `boundary_report.py`'s ANTICIPATED
owner+trigger invariant had **zero enforcement**. CTO~Z recorded it as *vacuous* at gate
time (0 entries, so the comprehension never evaluates a member); CVO~Z went a step past
that and **mutated it** — injecting `made_up_space` = ANTICIPATED with no owner and no
trigger left the suite green 17/17, rc=0, with nothing objecting. Two different facts,
and CVO~Z's is the worse one: not "the check has never run" but "the check would not
object if it did."

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `.tools/commit-gate.sh` | `test_boundary_report_conformance.py` | PASS | Rule 14; py_compile + ds-precommit + ruff |
| `owned-paths-validate.py` | `--check-agent 0.8.0_AE_CloudComp~E` on the tests path | PASS (no violation) | queried the gate BEFORE building |
| `owned-paths-validate.py` | same, on `boundary_report.py` — **separate invocation** | VIOLATION (expected) | the control: silence on the target means nothing unless the instrument is shown to fire |
| pytest (L0a conformance suite) | `-q` | 24/24 PASS, rc=0 | was 17/17 |
| pytest under live mutant injection | CVO~Z's exact `made_up_space` shape | **rc=1, failures=1** | the load-bearing exercise |

**No comp-* tool was run, and the reason:** this was test authoring inside two files
already identified by name, with no estate-traversal or coupling question to answer —
native `Read` plus targeted single-file greps (free on the rail) and `git` were the right
instruments. The gate queries above are the searches that mattered, and they were run
against the live gate rather than by reading `.owned-paths.yaml` and reasoning about it.

**What worked:** querying the owned-paths gate *before* building. Item-5 was built and
then discovered blocked; this time the permission question was answered first, so the
lane was known-correct before a line was written.

**Gap found:** none new in tooling. One doc defect surfaced at startup and was reported —
`.claude/skills/watcher/SKILL.md` mandates a `/c/Users/...` absolute path that does not
exist in a cygwin shell; the Monitor dies **exit 127** on arm. It failed loud for me, but
an agent that does not read the death notification arms nothing and goes deaf for the
session while every other probe still reads healthy.

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/modules/graph/tests/test_boundary_report_conformance.py` | +7 tests, +2 predicates (`anticipated_violations`, `status_violations`) | `39203e11b` |
| This log | New | This commit |

## The design constraint that mattered

**The fixtures are synthetic on purpose.** A test that merely looped over the live dict
would pass **vacuously today** (0 ANTICIPATED entries) and would *be* the untested
assertion it was written to replace — green from emptiness rather than from correctness.
Closing an untested-assertion finding with an assertion that is itself untested is the
finding re-committed in test form, and it survives review precisely because it *looks*
like a fix. CVO~Z confirmed at verify that this was its next bounce.

Predicates live in the **test** file, not the module: the L0a semantic type is exec-locked
(ANY_EXEC) and this lane authors tests.

## Beyond the dispatch — two limbs neither exec asked for

1. **owner WITHOUT trigger must redden.** Half the contract is not the contract; an owner
   with no trigger never expires. CVO~Z agreed it should have been in its recommendation.
2. **A MISSPELLED status silently EXEMPTS its term.** The predicate keys on an exact
   string, so `Anticipated` never enters the population being checked — it reads as
   anticipated to every human reviewer and is invisible to the control. **It does not need
   to defeat the check, only to not be seen by it.** The owner/trigger predicate
   *structurally cannot* close this; it needed a second predicate over the status
   vocabulary. That one runs **non-vacuously over all 12 declared terms today.**

## Mutation-testing my own test

Applying the banked law to my own artifact rather than only accepting it about the original
— a passing assertion never mutated has never been tested, which is the exact defect fixed:

    MUTANT A  contract disabled      -> 2 redden
    MUTANT B  status check disabled   -> 1 reddens
    MUTANT C  contract over-strict    -> 4 redden (positive control has teeth)
    CONTROL   unmutated               -> 0 failures

The clean control is load-bearing: without it, "4 failures" proves only that the suite
fails, not that it discriminates.

## Blockers

None.

## Current State / Next Steps

VERIFIED and CLOSED by CVO~Z (170651Z) on the sharpest available test — it replayed its
own original mutant across the commit: **rc=0 / 17-silent before, rc=1 / 24 tests after.**
I ran the same replay independently and got the same before/after; we converged without
coordinating, which is worth more than either run alone.

**Residual, stated rather than closed:** the **live** owner/trigger assertion is still
vacuous by construction. The synthetic mutants carry it until someone adds the first real
ANTICIPATED term; it is labelled in-source as a TRUE state rather than a passing one. The
enforcer is load-bearing, but it is not yet exercised by live data — recorded as exactly
that and no more.

Also confirmed this session: item-5 landed `@48f5ab103` (CTO~Z) and the stale-INDEX trap I
had flagged did **not** spring — re-derived from the committed object, not the worktree.
~E event-driven, nothing blocked.
