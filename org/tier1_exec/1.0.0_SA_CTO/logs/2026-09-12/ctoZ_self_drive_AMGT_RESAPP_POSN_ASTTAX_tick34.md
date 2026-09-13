# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 34

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-12T22:39:59Z**
(`date -u`.) Tick 33's log is `@69052108eb`. **Written for ONE reason: a pattern that is the subject
of the round-7 analysis this seat will have to write, and that no artifact currently states.**

---

## 1. THE PATTERN -- TWO ORDERS, TWO DEFECTS, BOTH IN THE CUT, BOTH CAUGHT BY THE WORKER

`0.9.0_WK_AMGT_RESAPP~11` produced twice this window and **left BOTH orders OPEN rather than
self-grading around the wall**:

| commit | order | what the worker refused to do |
|---|---|---|
| `862291e62f` 22:10Z | `rf-2` | *"AC1 BLOCKED BY THE ORDER'S OWN GRANT, order left OPEN"* -- the order is TITLED "a `<paths>` repair" and its own nine-entry grant omitted `infra/aws/lambda/`, where every handler package lives. AC1 could not reach a non-zero integer by any legal act. |
| `ebcfc4051f` 22:30Z | `rf-3` | *"183 of 183 rows restored via a producer-tied scope contract; AC2 CANNOT PASS AS WRITTEN, order left OPEN"* -- substance delivered, criterion refused. |

`2.0.0_SA_COO~ZZZ` repaired both same-tick (`545ee5ee82` grant 9 -> 11, deliberately narrow;
`5dc02a83d5` amending rf-3 with *"TWO OF MY OWN CRITERIA COULD NOT DISCRIMINATE"*) and filed rows
against its own cut.

⭐ **THE CTO READING, WHICH IS THE PART NOT RECORDED ANYWHERE ELSE: THIS IS NOT N SEPARATE REPAIRS,
IT IS A DECOMPOSITION-QUALITY SIGNAL, AND IT IS THE SAME CLASS THIS PROJECT HAS PRODUCED ALL
SESSION.** The round-5 analysis already named it -- *"FOUR PROJECTS-WORTH OF CELLS CONVERGED ON ONE
DEFECT CLASS IN ONE EVENING: A CRITERION THAT CANNOT FAIL IN THE BROKEN WORLD"* (`rd-8`'s AC2/AC3,
POSN's `S2-AC5`, step (2), `T6-AC4`). Round 7 is now producing the MIRROR of it -- criteria that
cannot PASS in the fixed world -- at `rf-2` AC1 (unsatisfiable inside its own grant), `rf-2` AC2 (a
terraform `route_key` bands SURFACED, 68 of 68 estate-wide, so a "CONFIG or DEF band" clause is
unsatisfiable for any artifact built the way the order mandates) and `rf-3`'s two.
**ALWAYS-PASSES AND CANNOT-PASS ARE ONE DEFECT WITH TWO SIGNS: A CRITERION WRITTEN WITHOUT RUNNING
IT AGAINST THE WORLD IT WILL BE GRADED IN.** The round-7 analysis states it once at that grain rather
than as six repairs, or the recut inherits the shape.
⚠ **AND THE HEALTHY HALF IS LOUDER THAN THE DEFECT.** A worker that STOPS ON THE CLAUSE and files a
row is the reason these are twenty-minute repairs instead of round-8 findings. The estate's older
failure was cells self-grading past a bar; this is the opposite and it is working.

## 2. THIS SEAT'S ONE ACT SINCE TICK 33

**`AMGT_RESAPP-Z-S36` `@92781851bc`** -- `to-check.py` reports a round's ACTIVE count off the
WORKER-FACE INSTRUCTION PROSE, not the `<status>` element (6 ACTIVE while rf-1 and rf-6 read
`complete`). **The ENFORCING gate is correct and that was measured, not assumed:**
`_open_tos_for_project` returns AMGT 4 of 43 and POSN 4 of 15, both matching disk, with
`ZZZZ_NOSUCH` -> 0 of 0 as the negative control. Blast radius is REPORTING, not enforcement.
⭐ Corroborated by `2.0.0_SA_COO~ZZZ` on a DIFFERENT instrument (its grep requires a whole
`<status>...</status>` element, which the prose does not form) -- two methods, one answer, so this is
corroboration and not a re-run of this seat's method.
⛔ **THE GATE THEN CAUGHT A DEFECT IN THAT ROW**: the first commit was REFUSED on
`/surfaced_at` because this seat typed `22:2x:00Z`, a placeholder rather than a timestamp, into a row
whose whole subject is an instrument reporting something other than the field it claims to read.
Replaced with a measured `date -u`. **This tick's counts are read with `_open_tos_for_project`, not
`to-check` -- the row's own interim practice, applied to the seat that wrote it.**

## 3. AND A CARRIED CARD AT ANDREW IS NO LONGER HYPOTHETICAL

The **LIMB 6 widening** card was raised on a possibility. It now has a measured instance: the rf-2
grant amendment `@545ee5ee82` widened a live `<paths>` grant under a working worker, and
`to-pipeline-gate` printed **`OK: 0 newly-added TO file(s)`** on that very commit -- the banked
VACUOUS PASS. `2.0.0_SA_COO~ZZZ` hand-verified instead (zero illegal shapes, status still staged,
criterion count still 5, cell text unchanged, +25 additive lines). **A `<paths>` grant is exactly the
field class the card proposes grading, and it changed with nothing refusing.** The card is otherwise
unchanged and NOT re-carded; Andrew simply has an instance behind it now.

## 4. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED · NO PITCH (unchanged; CVO-confirmed at tick 31 and
                     nothing has changed their citations. Re-pitching is repetition.)
  CARRIED   portal DEV push · LIMB 6 widening (now with a measured instance) · Bright Data proxy
  NOT-MINE  POSN round-3 four-of-fifteen · the half-hash mechanical-change carve-out (both MSTR's)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  4 OPEN of 43 [rf-2..rf-5]; rf-1+rf-6 terminal; ~11 MOVING
  POSN_ASTTAX  active/EXECUTING  REACHABLE  4 OPEN of 15 [S2-1,S3-1,T6-1,T7-1]; round 4 not cut
  UNREACHABLE: 0     HELD-AT-STOP: not reached
  (counts from _open_tos_for_project with its negative control -- NOT from to-check, per Z-S36)
```
⚠ D4 `open_tos=6` vs measured 4: fourth tick carrying it, still UNDETERMINED (lag vs grain), still
not reported as a defect on an undetermined cause. ⭐ Z-S36 makes a shared-parse cause PLAUSIBLE and
that is explicitly NOT claimed -- different tool, different set, and it errs the other way on POSN.

**Push state:** `origin/SITEZ 9b36f585fa`; local HEAD `5dc02a83d5`, **1 ahead** (the COO's rf-3
amendment). This seat's work through `92781851bc` is published. `HEAD:portal e85f6eb84f` unchanged.

## Compiler Tools

`_open_tos_for_project` loaded directly from `surprise-row-gate.py` with a `ZZZZ_NOSUCH` negative
control (the round-state instrument; **`to-check`'s ACTIVE count is not, per Z-S36**) · `git log
--all --author` for the worker plane · `git ls-remote` · `date -u` · a python `<status>` read to stay
off the comp rail after a directory-glob grep aborted a whole call · `safe-commit.sh -F`.
