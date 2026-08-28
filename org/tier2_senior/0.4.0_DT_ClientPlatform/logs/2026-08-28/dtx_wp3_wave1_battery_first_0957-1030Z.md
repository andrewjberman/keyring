# The battery before the code — and five findings against the things that measure it — 0.4.0_DT_ClientPlatform~X

**Date:** 2026-08-28
**Task Order:** NFRA_C3MATERIALIZE.TO-WP3-1-DTX (WP-3 ledger build, wave 1)
**Status:** BLOCKED (deliverable complete; the proof instance cannot validate for a reason outside it)
**Window:** 09:57–10:30Z
**Archetype:** BUILDER-UNDER-A-FROZEN-SPEC

## Objective

Discharge wave 1 of the WP-3 identity-ledger build: engine chosen by ONE stated criterion, and the
battery built FIRST from the design's sec 3 — 8 acceptance criteria over 53 cells, no ledger code,
fixtures only, no byte of the frozen `v0.3-candidate+27`, and **no typed count anywhere**.

## Compiler Tools

`git` object-database reads for every measurement (`git show <commit>:<path>`, `git archive`,
`git rev-parse` for blob identity); `arm_census.py`, `build_manifest.py`, `run_battery.py`,
`carrier_dependency.py` (all built this wave); `bundle_identity.py` read (not run) for AC8's member
list; `.tools/proof-of-spec-check.py` for the deliverable.

**What worked:** reading the object DB at a cited commit rather than the working tree — the tree
moved three times under me during the wave (sec 3b landed twice, the TO's face four times) and not
one number moved with it. Building the census as a FILE rather than a one-off: AC2, AC3 and AC5 all
consume it, so a single instrument carried three criteria and one fix propagated to all three.

**What failed:** my own instruments, four times, and each failure was silent rather than loud —
a text classifier that read what a row NAMES instead of what its arms EXERCISE; a heredoc that ate
backslashes out of a regex twice; a mutant counter that conflated `_mutants` with `_semantic_mutants`
and reported +0; and a proof instance modelled on an example instead of the schema (19 violations).

**Gap found:** `proof-of-spec-check.py` does not verify that `session_log` resolves to a file. My
instance cited this log before it existed and would have validated with a dangling path. Same class
as the unenforced-provenance-field law in CLAUDE.md §4 — a field no consumer rejects on drifts.
Surfaced here rather than filed: it is the checker's owner's call whether it is worth a control.

## Work Completed

### 1. AC1/AC2 — the census and pairing, counted
`arm_census.py` at `d0398b977d`: **13 rows, 190 arms, 126 distinct, PAIRED 13 of 13**. Reproduces the
integrator's published 190/126 from an independent implementation of the shared predicate. Its
self-test drives four clauses each with a *reachable control* — and the DEDUP clause was exercised
for the first time in the round: it had read 0 double-cited at six consecutive pins, so three seats'
numbers rested on a branch no corpus had ever entered.

### 2. AC4 — engine by one criterion
`ENGINE_CHOICE.md`. Criterion, one sentence, grounded at source (`CLAUDE_ANNEX.md:465`, not
paraphrased): *the store lives on the device that owns the work, and no write is ferried across a
fabric*. Applied to all three candidates before preferring any; Iceberg-under-Nessie rejected on a
stated property. The two survivors are separated NOT by a second criterion but by the design's own
stated requirement (`commit_seq` is a filter every candidate must pass). **SQLite, single file,
local.** DuckDB named as the near miss so the rejection is legible; failure mode written including
the concrete refutation that would overturn the choice.

### 3. AC5/AC6 — manifest generated, runner built
`MANIFEST.json` is GENERATED from the census, never transcribed. `--check` VALID (190/190);
`--check --plant-missing <id>` INVALID — a checker with no demonstrated failing state is not a
control. `run_battery.py` clones the pin into a fresh dir (refuses a reused one), takes numerator and
denominator from DIFFERENT sources, and has **three non-collapsible exit codes**. It reports
`ran 0 of 190 — verdict WITHHELD (exit 3)` and does NOT mark `exercised`, per the TO: with no ledger
code every arm fails for one reason, which measures the wave and not the ledger.

### 4. AC7/AC8 — boundary evidence with positive controls
AC7: zero network/credential/production imports under `ledger/`; every path the runner opens is
inside its own clone. AC8 discharged on the **member-list intersection** (14 members read from
`bundle_identity.py`, 6 staged files, intersection NONE) rather than the TO's own command — see
R4-DT-5.

## Decisions Made

- **Report AC3 by confidence tier rather than as a column.** The mechanical run said 11/2; I said
  plainly I did not believe it and would not file it as the value. The issuer ruled it a decomp
  sequencing defect.
- **Do not ship an instance whose `decomp_ref.doc` disagrees with its TO** to make a validator go
  green. That is the workaround the TO's own boundary forbids one line over.
- **Land the wave in ONE commit** rather than per-criterion, and write this log into it rather than
  letting `/log` cut a second commit. ⛔ **SUPERSEDED at 10:34Z — and the correction is the point.**
  `safe-commit` refused `org/standards/isck/ledger/**` (lane `ANY_EXEC`; this seat is Tier-2 DT). I
  did **not** self-authorize past it and did **not** quietly relocate the battery into my own lane to
  make the refusal go away — AC5 licenses a different location, but every message in the thread names
  "the six ledger/battery files", so moving them unilaterally would have changed a shared expectation
  to dodge a gate. Put to the issuer as two options with no preference stated; ruled (a) at msg 77667
  — battery stays with the package it tests, under a SCOPED `GIT_COMMIT_AUTHOR_OVERRIDE` for that path
  only. **SINGULAR means N lanes = N commits**, so the wave lands as TWO: the six files under the
  override, the instance + this log in this seat's own lane.

## Findings Filed

| id | class | substance |
|---|---|---|
| R4-DT-3 | SEQUENCING | AC3 is not dischargeable by any text instrument; my classifier returned a FALSE PLUS38_ONLY on row 4, and the schema vocabulary collides (`opened`/`closed` in both event carriers, §3.16-allowed). Issuer-ruled; sec 3b landed as the INFERRED interim. |
| R4-DT-4 | OBSERVATION | sec 3b landed the span's FIRST escaped pipe. My census was immune **by the row filter, not by the fix** — a naming convention in someone else's addendum. Acted on at source. |
| R4-DT-5 | PROCESS | The TO's AC8 command cannot measure AC8: a git pathspec `*` crosses `/`, and extension globs miss `run_gates.sh`, a bundle member. Accepted; instrument amended. |
| R4-DT-6 | BLOCKING | Two layers: the decomp cited parenthetically so the checker captured `(DECOMP.md`; and, once fixed, `DECOMP.md` is a narrative holding 6 of 168 cell ids while the cells live in the JSON. Routed, two owners named. |

## Blockers

**R4-DT-6 layer 2.** The instance is complete — 0 structural violations, 8 acceptance rows, mutant
FIRED-AS-EXPECTED, determinism STABLE — and cannot validate. Both branches available to me are
INVALID (match the TO and lose 50 cells, or resolve the cells and disagree with the TO); only the
issuer's declaration makes them coincide. **Not mine to fix, and not mine to work around.**

## Current State

Six files written under `org/standards/isck/ledger/`, nothing committed, tree otherwise clean.
`origin/CLOUD @540503df0a == local HEAD` (measured). Wave 2 (ledger code) is cut by the issuer on
this wave's measured completion.

## Next Steps

1. **[2.0.0_SA_COO~X]** declare the cell-bearing decomp artifact in `<decomp_ref>` (recommend
   `rectangle.final.certified.json`, the certified consumable).
2. **[0.4.0_DT_ClientPlatform~X]** re-validate, land the wave in one commit, report per the TO.
3. **[3.0.0_SA_CVO~X]** the `\S+DECOMP\.md` regex and the unverified `session_log` field, both in
   `proof-of-spec-check.py` — owner's call, neither raised as a demand.

## The transferable half

Four of my five findings this wave were against **instruments, not artifacts** — a classifier, a
regex, a counter, a checker. The pattern underneath every one: *the instrument measured its own
frame and returned the shape a correct answer has.* A text scan returns PLUS38_ONLY when a row does
not name a type; a greedy regex returns a path when it captures a paren; a conflated counter returns
+0; an example-shaped instance returns plausible enum values. **None of them errored.** The only
defence that worked, repeatedly, was building a control that could FAIL and watching whether it did —
and twice tonight that control caught my own fix, not the original defect.
