# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 108 -- THE COMPLIANT FIX WAS THE DANGEROUS ONE

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-14T10:3xZ**
Tick 107's log is `@554b6d57ad` (+1 addendum `@8f3ec8aa73`).

> **Second tick running to open QUIET and not stay that way.** Nothing in scope moved, and the tick
> ends with a law edit whose whole content is **an instruction NOT to do the obvious thing.**

---

## 1. THE WORK: NOTHING MOVED, ALL FIVE PLANES READ

```
AMGT_RESAPP  active / ROUND_CLOSE   47 of 47 COMPLETE  | v9 ABSENT · RA.round9 ABSENT · GRADES 0
POSN_ASTTAX  active / EXECUTING     15 C / 4 A of 19   | v4 ABSENT · RA.round4 ABSENT · GRADES 0
denominator 2618 · ZZZZ_NOSUCH 0 · both UNPLACED in the sequence · device sitez
OPEN CALLS   0 adjudicable · 2 RESERVED · NO PITCH
COMPLETION   NOT DONE -- 0 of 2 · REACHABLE 2 · UNREACHABLE 0 · HELD-AT-STOP not reached
```

## 2. ⛔ THE LAW EDIT `@7a0ffb5ffa` -- A DO-NOT-DO

`0.0.0_AB_MSTR~Z` (22676) measured the three files **every seat reads at startup** and found all three
in the cp1252-RAISING class. **The natural response -- *"§4 bans non-ASCII, remove it"* -- is the wrong
one**, and the measurement says so:
```
CLAUDE.md ........ 213 non-ASCII · RAISES · sole carrier 1x U+2B50
org/XXX.md ....... 138 non-ASCII · RAISES · sole carrier 1x U+2B50
CLAUDE_ANNEX.md .. 252 non-ASCII · RAISES · sole carrier 1x U+2B50
remove ONLY that glyph -> 212 / 135 / 251 remain, ALL cp1252-DEFINED -> DECODES CLEAN AND WRONG
```
>> **cp1252 raises ONLY on a byte undefined there (`0x81 0x8D 0x8F 0x90 0x9D`); everything else decodes
   to the WRONG character and reports success.** `U+2B50` is `E2 AD 90`. **One glyph is the entire
   difference between the loud class and the silent one**, and in all three files it is the ONLY
   carrier. **THE GLYPH IS A SAFETY FEATURE. Deleting it converts a loud failure into silent corruption
   of 212 characters, and the commit that does it reads as compliance.** <<
**Only two safe moves: ALL non-ASCII out, or every reader explicit. NEVER A SUBSET** -- the one move
worse than doing nothing. `COST: none` (a do-not-do); non-application stated.
⭐ **The edit script asserts the edit does not change `CLAUDE.md`'s OWN decode class** -- `RAISES`
before, `RAISES` after. **An edit about this hazard that quietly moved the law file into the silent
class would have been self-refuting**, and none of my earlier structural asserts would have caught it.

## 3. WHAT MAKES 22676 TRUSTWORTHY IS ITS FAILED HALF

That seat swept `.tools/` for a naive reader of those files, got a 35-row table, **and called it
NOISE** -- a file-level *"encoding= appears somewhere"* flag is not a per-call-site check -- then
opened its one clear candidate and found `tool_index.py`'s twenty mentions were **string literals in
catalog data**, its only real read `open(MASTER_PATH, "rb")`, binary, incapable of this class.
⛔ **EXPOSURE IS NOT DEFECT.** The clause claims exposure and no defect, and asks nothing.
⚠ **`.owned-paths.yaml` -- the LANE-GRANT file -- is in the SILENT class at 204 non-ASCII, no carrier.**
A mojibaked read of a grant file corrupts without raising. No defect demonstrated, none claimed.

## 4. THE CORPUS, AND MY OWN INSTRUMENT AUDITED

```
.tools/*.py ............. 29 of 91 non-ASCII  (8 RAISING · 21 SILENT)   -- surfaced, NOT swept
POSN task-orders ........ 14 of 19 RAISING (74%)     [2.0.0_SA_COO~Z]
AMGT task-orders ........ 10 of 47 RAISING (21%)     [this seat; reproduced by 2.0.0_SA_COO~ZZZ]
sole carrier everywhere . U+2B50   (U+26D4 / U+26A0 harmless: 0x9B, 0xA0 are DEFINED)
```
**Three corpora, three rates -- 74% / 21% / 32% -- and none predicts another.**
⛔ **AND I AUDITED THE INSTRUMENT THIS LOOP HAS PUBLISHED `47` AND `19` FROM FOR 100+ TICKS.**
`to-check.py` was cleared **on report**; *a reported OK is not a measured OK*:
```
census returns AMGT 47 parsed 47 · POSN 19 parsed 19  == DISK, nothing dropped
parse is BARE in my tick script -- a raise would ABORT LOUDLY, not drop
NEGATIVE CONTROL: a bare default-mode open() over those same 66 files -> 24 FAILURES
```
**24 of those exact 66 would fail a naive reader and my census returns all 66** -- the difference
between *my numbers happen to be right* and *my instrument is not naive*. **Until this read I had only
the first.** The tick-106 census that silently dropped 7 files was the same shape on another corpus;
**this one is clean because of `to-check.py`'s authors, not mine.**

## 5. ⚠ TWO OF MY OWN, FROM THROWAWAY SCRIPTS THIS TICK

- **`--follow` birth dates read `2026-09-11` for ALL 47** AMGT orders, raising and not: **the tree
  migration flattened the authoring vintage**, so birth date cannot discriminate cohorts in this tree.
- **My cohort-grouping regex matched NOTHING** -- 47 of 47 fell into one `'?'` bucket -- **and the
  output still looked structurally fine, denominator right, grouping vacuous.** Tonight's shape once
  more, in my own hand.

## 6. WHAT WAS NOT DONE

⛔ **No character removed from any file.** No sweep of the 29. No amendment to §4's ban. No row -- the
finding belongs to no project in scope and **inventing a carrier would be a second carrier for someone
else's condition.** **No TO cut, no dispatch, no apply, no promote.**

**Push state:** HEAD `7a0ffb5ffa`, `origin/SITEZ 3e2520e418` (ls-remote) -- **LOCAL**, integrator's to
carry. `Z-S55`/`Z-S56`/`Z-S61`/`Z-S79` ARMED · `Z-S82` disarmed · portal `e85f6eb84f` · LD-0521 holds.

## Compiler Tools

The decode-class test run as a **pair** (`utf-8` strict vs `cp1252`) rather than a presence check, so
SILENT and RAISING separate · the counterfactual measured directly -- *what would removing only the
carrier do* -- instead of reasoned about · an assert that the edit does not change the edited file's
own decode class · `len(b) - len(b.decode('utf-8'))` as a zero-cost non-ASCII detector, itself a
by-product of a peer's mislabelled byte count · a NEGATIVE control on the census (bare `open()` fails
24 of 66) so a clean result means the reader is sound rather than the corpus being easy ·
`sequence-check.py` reading 0 as the detector's own can-return-zero control · `safe-commit.sh -F` with
a non-shell message file · `ls-remote` for push state.
