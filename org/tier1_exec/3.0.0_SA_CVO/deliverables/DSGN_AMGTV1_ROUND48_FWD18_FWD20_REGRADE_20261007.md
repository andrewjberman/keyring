# DSGN_AMGTV1 round 48 -- re-grade of FWD-18 and FWD-20 (3.0.0_SA_CVO~Z, 2026-10-07 ~11:5xZ)

**Ask:** `1.0.0_SA_CTO~Z` msg 30853. **Input:**
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round48/ROUND48_CLOSE.md` @92926540f5.
**Graded against:** PRD v0.17 ENDPOINT (ratified-text half signed by this seat on half_hash `a7aeaf409bd4`).
**Candidate:** portal `97598dc3`, branch `dsgn-r48-onto-dev` in `C:/tmp/wk-dsgn-amgtv1-92/portal`. It is NOT on DEV:
`git -C portal ls-remote origin DEV` read `8ddfe409` at 10:2xZ and the push is Andrew's word. So both grades below are
grades of the candidate, not of the served page.

## Verdicts

| row | round 46 | now | on |
|---|---|---|---|
| FWD-18 | REALIZED against the outcome, DONE WHEN stale | **REALIZED** | the v0.17 DONE WHEN, as written |
| FWD-20 | NOT_REALIZED (65 PASS / 11 FAIL) | **REALIZED**, with one reading for the CTO to rule | the render check at 76 PASS / 0 FAIL / 1 N/A |

Both become grades of the served page only when `97598dc3` is on DEV. Until then the board row for the served page
has not moved.

## What this seat read itself

- **The candidate's diff.** `git diff --stat ec9f9a0e 97598dc3`: one file, `scripts/ui-contract-check.mjs`, +3/-5.
  `8ddfe409` is an ancestor of `97598dc3`. I read the three hunks: the `purpleFills` predicate passes a Security state
  only at 0 and the Universe state at 0 or 1; `gradeFwd18` fails a Security state unless 0, drops the Refresh demand,
  and fails the Universe state above 1. That is the v0.17 text and nothing looser.
- **`round48/instrument35-candidate-grades.json`, every cell.** Result 76 / 0 / 0 / 1 of 77. `purpleFills` 0 and PASS
  on 6 of 6 states. `fwd18_controls` PASS on 6 of 6. `sizes` reads smallest 11 on 6 of 6 (round 46: 10 on the Model
  state). Harnesses 8 of 8, 20 of 20, 32 of 32. Faces PASS (price 19 of 19, chatter 55 of 55).
- **The run's own logs** in `C:/tmp/r35-scratch-c/out-20261007T112904Z/` (device-local): `candidate.log` ends
  `RESULT: PASS`; `pre-8fa7abde.log` ends `RESULT: FAIL` with 31 FAIL cells; `plant-two-bands.log` and
  `plant-light-on-dark.log` each end `RESULT: FAIL` with 2 FAIL cells; `plant-control.log` grades every clause cell
  PASS.
- **Three of the six state PNGs** from that run, at full size: list, thesis, model. No filled purple control on any
  of the three. I cite no clause for rejection.

Not re-run by this seat: the instrument (about 13 minutes on the worker's tree). Not read: the exec, peers and posture
PNGs. Not re-walked: the live page; the commit changes the check, not the page.

## FWD-18 -- REALIZED

DONE WHEN (v0.17): segmented controls whose active state is weight and rule, the generation and resolution lines in a
"Source:" footer, `purpleFills <= 1` in every view and `== 0` in Security mode.
- The list state's `fwd18_controls` cell is PASS (affordances 2, subject 2, chatter footer 1).
- `purpleFills` reads 0 on all six states, so both halves of the count hold.
- The check now grades the text as written, so the grade no longer rests on "against the outcome".

## FWD-20 -- REALIZED, with one reading to rule

DONE WHEN: the render check PASSES on six states, the harnesses are green, the same instrument FAILS a planted page on
each clause and FAILS the real pre-redesign page on the band clause, and a person reads the six PNGs.
- **Passes:** 76 PASS, 0 FAIL. The two round-46 causes are both gone: the stale purple-fill clause (10 cells) and the
  10 px text on the Model tab (1 cell).
- **Fails the pre-redesign page:** 31 FAIL cells on portal `8fa7abde`, the band clause among them (lightOnDark 58 or
  59 on the exec, peers, model and posture states, the four I read in the log).
- **Fails planted pages:** two plants, both on the band clause (two dark bands; a white card on a dark band), beside a
  clean control.
- **Person's read:** three of six states read here; the side-by-side read is FWD-11's.

**The reading for the CTO.** "FAILS a planted page on each clause" has been met since round 35 by planting the band
clause's two limbs only. The instrument's own header says so. For the other clauses the evidence that each can fail
is indirect or absent:
- purpleFills: the pre-redesign page fails it on 5 states, and `round47/checks/r47i/r47i.cjs` shows the predicate
  refusing 1 in a Security state and 2 in the Universe state;
- sizes: it failed for real at round 46;
- fonts, weights, radii, shadows, lowContrastChars: no planted page and no observed failure that I found. Earlier
  rounds may hold one; I did not search them.

I grade REALIZED on the reading the board has used since round 35. If "each clause" means all of them, FWD-20 is
NOT_REALIZED until five more plants exist, and that is a round-49 instrument cell. That call is the CTO's.

## Noted, not graded

The instrument renders fixtures, not the live API: its list state shows vendor-capital names ("NIKE INC -CL",
"NOVARTIS AG-REG") and grey bubbles. That is the fixture's data. FWD-27 and FWD-21 are graded on the live walk.

-- 3.0.0_SA_CVO~Z
