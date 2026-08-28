# The ledger, until the battery passed — and the four controls that could not fire — 0.4.0_DT_ClientPlatform~X

**Date:** 2026-08-28
**Task Order:** NFRA_C3MATERIALIZE.TO-WP3-2-DTX (WP-3 ledger build, wave 2)
**Status:** COMPLETE except AC8, which is BLOCKED upstream by a measured, routed defect
**Window:** 10:44–12:15Z
**Archetype:** BUILDER-UNDER-A-FROZEN-SPEC

## Objective

Build the WP-3 identity ledger until the battery passes from a clean clone: 130 cells, 9 acceptance
criteria, in the rectangle's `depends_on` order, committing per unit. The completion evidence is
AC6 — `run_battery.py` on a fresh clone printing `ran N of N` by counting, exit 0.

## Outcome

**`ran 188 of 188 -- COUNTED`, exit 0, from a clean clone of `91f38fb966`.** 0 wrong, 0 errored,
0 unimplemented, reconciliation printed. Proof-of-spec instance VALID, 9/9 criteria, 130/130 cells
forward and backward. Thirteen commits, all under the lane row `f94ef2f3d1`, no override used.

## Compiler Tools

`run_battery.py` (rewritten this wave), `build_manifest.py` (rewritten), `controls.py` and
`carrier_measure.py` (new), `bundle_identity.py` (read and derived, never written),
`.tools/proof-of-spec-check.py`, `git` object-database reads for every measurement.

**What worked:** mutating the ledger's own rules one at a time and printing *which* arms turned. It
found more real defects than any review did, and it is the only technique here that distinguishes
"this arm passes" from "this arm tests what its id says". It caught: five row-13 arms refused by
other rows; the load-bearingness of the VOIDED derivation; and the fact that a wrong ORDER in the
actor check is invisible to every arm but one.

**What failed:** my own instruments, repeatedly, and always by *validating the wrong property*.

## The through-line: four controls that could not fire

This is the wave's finding, and every instance is mine.

1. **The runner's execution loop** appended every arm id unconditionally. An empty `engine.py`
   would have printed a green `190 of 190`. Its docstring hunted three false-pass shapes and all
   three held; the shape it missed was *numerator real, denominator real, arms never executed*.
2. **It was unreachable anyway** — `clean_clone` was passed the manifest's *census* vintage, which
   predates all ledger code, so the branch could never run. Two defects, the second hiding the
   first. Found by `3.0.0_SA_CVO~X`.
3. **The manifest's uniqueness controls U1–U4** proved uniqueness, single-kindedness,
   template-freedom and ASCII. A separator my elision expansion ate produced four *fused* ids —
   unique, single-kinded, template-free, ASCII. Every control passed a defect they were structurally
   blind to. U5 now compares against the design's spelled text, which is the property that matters.
4. **The fresh-clone-dir refusal** was preceded by an unconditional delete of that directory. The
   advertised control was dead code, and my first repair kept the delete while adding a
   `--clone-dir` a verifier would name — which would have silently deleted their directory.

Underneath all four: **I wrote the control set and the thing it controls in the same sitting, so the
controls cover the shapes I was already thinking about.** The defect is never in that set.

## Work Completed

Per-unit, in the rectangle's dependency order, each with its own commit and its own mutation:

| unit | commit | arms |
|---|---|---|
| manifest expansion (61 templates → ids) | `33ec669780` | denominator 188 / 190 citations |
| runner repair + unit 1 (store, admission, envelope, anchors) | `4c3dbd0309` | 16 |
| resolver — sec 2d's 30 reference rows, arms GENERATED | `d6ed40dc6e` | 77 |
| stored wrong-class control (correcting a commit body) | `94c7a674ba` | — |
| row 4 binding machine + VOIDED | `f4d5d524e9` | 86 |
| separator repair + U5 | `cf87ed220a` | — |
| row 6 mint + authority epoch | `df73fa3fc4` | 105 |
| row 7 lineage, cycles, forks, lifecycle | `7bfbf40640` | 127 |
| rows 8–11 surfaces | `f45c3dee06` | 145 |
| row 5 folds | `d7456b969a` | 159 |
| row 13 contests | `1df65cb07c` | 188 |
| runner never deletes its destination | `91f38fb966` | 188, exit 0 |
| AC7 carrier measurement | `67f320c4c2` | 13 of 13 |

## Decisions Made

- **Generate the 61 resolver arms rather than hand-write them.** Sixty near-identical fixtures
  differing in one field is where a transcription slip yields a *green* arm. Generating them from
  the table the resolver itself reads means an arm cannot disagree with the policy it tests.
- **Make each generated reject arm assert WHICH refusal it got.** Immediately caught a row-2 arm
  being refused by row 6 — right verdict, wrong rule, and a pass either way without the assertion.
- **Stop tuning the AC7 instrument.** After removing universal scaffold mechanically I was adding a
  discriminator per pass until the number looked right. That is tuning toward a preferred answer.
  Stopped, reported both readings and the instrument's own non-decisiveness.
- **Do not fire `--receipt` for AC8.** The precondition is measured as unsatisfiable and a receipt
  slot is set once; firing it would be a risk, not a control.

## Findings Filed

| id | class | substance |
|---|---|---|
| 77685 | OBSERVATION/ARMED | the runner's stub loop would have faked AC6; disarmed same-turn |
| 77691 | BLOCKING | 61 of 190 manifest arms were unexpanded templates, unaddressable by id |
| 77720 | OBSERVATION | sec 2d's STRICT has a CLASS half no row-2 arm can express; implemented, controlled in-commit, arm landed at HEAD for the next pin |
| — | OBSERVATION | `L-13-consequence-unresolved` cannot be attributed to row 13: sec 2d and row 13 state one rule and the resolver runs first |
| — | OBSERVATION | AC7's subset test is not decisive as specified; the carrier half is, and agrees 13/13 |
| 77766 | BLOCKING | the freeze commit wrote its freeze entry into `ISCK_CONTRACT.md`, a bundle member, so no post-freeze commit derives the frozen bundle and AC8's receipt is unobtainable |

## Blockers

**AC8 only.** `derive(7a44b65f50~1)` = the frozen `+27` bundle; `derive(7a44b65f50)` = a different
one; exactly 1 of 14 members differs across that commit and 0 of 14 from there to HEAD. The ledger
code exists only after the freeze, so no satisfiable `run_commit` exists. Three correct decisions —
the freeze entry belonging in sec 8, the member list predating it, and R3-CRO-36's run binding added
later — compose into an unobtainable receipt, and none is visible from inside the others. Routed;
not worked around.

## Current State

`ran 188 of 188`, exit 0, at `91f38fb966`; instance VALID; AC9 evidenced with both denominators and
a positive control. My 15 commits since the pin touch **0 of the 14 bundle members** and nothing
outside `ledger/` and my own deliverables. Push state MEASURED: **LOCAL** — `origin/CLOUD`
`540503df0a`; every wave-2 commit is local-only.

## The transferable half

A control validates a *property*. Four times this wave I built a control set that validated a
property the defect satisfied — uniqueness where the defect was a fused separator, three false-pass
shapes where the defect was a fourth, a refusal preceded by a delete. Each set was internally
sound. **The question that would have caught all four is not "is this control correct?" but "what
would this control still say if the thing it guards were broken in a way I have not imagined?"** —
and the only way I found to ask it mechanically is to break the thing and watch, one rule at a time,
printing *which* arms turn rather than how many.
