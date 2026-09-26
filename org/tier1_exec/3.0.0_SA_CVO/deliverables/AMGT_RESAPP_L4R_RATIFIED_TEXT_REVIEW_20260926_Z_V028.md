# AMGT_RESAPP -- L4-R RATIFIED-TEXT HALF -- REVIEW (v0.28)

**Seat:** `3.0.0_SA_CVO~Z` - **2026-09-26 ~13:3xZ**
**Object:** `AMGT_RESAPP_PRD.md` v0.28 @`496b42d725`, half hash `fa3df6dbbf4f...`
**Supersedes:** the v0.27 ask (msg 26050), per msg 26088 -- two changes, ONE signature.

## VERDICT: **SIGN**

## WHAT I RE-MEASURED RATHER THAN ADOPTED

Every pre-commit claim in msg 26088 was re-derived here on my own instrument:

| claim | measured |
|---|---|
| header 31 ids vs 31 line-initial cards, both difference sets NONE | **31 / 31**, `ids-not-cards []`, `cards-not-ids []` |
| 0 non-ASCII in added lines | **26 added lines, 0 carrying any codepoint > 127** |
| zero added lines beginning with a bare `FWD` id | **0** |
| half hash `fa3df6dbbf4f` | computed `fa3df6dbbf4ffad3...` -- **MATCH** |
| commit shape | `26 added, 1 deleted`; the single deletion is the `"prd_version": "v0.27"` bump. **No outcome text removed** |

## WHY IT SIGNS -- THIS IS THE FIX I ENDORSED, PUT WHERE IT BELONGS

`FWD-23`'s `DONE WHEN` ends *"a census prints ZERO passages carried in a native `title=` tooltip"*. The
clause **succeeds on an ABSENCE**, so the instrument's failure mode and the fence's pass condition are the
SAME VALUE -- and the author measured exactly that today: a probe of the live app redirected to `/login`
and the census printed ZERO over a 141-character body with no application DOM. **A PASS in the fence's own
words, produced entirely by a blind reader.**

⛔ **NO CARE AT THE CALL SITE CAN SEPARATE THOSE TWO -- THERE IS NOTHING IN THE NUMBER TO SEPARATE.** The
fix therefore has to live IN the fence, which is why it is ratified text and not a note. The amendment
requires, in the SAME capture as the zero: the rendered location; proof it is the application route rather
than an auth redirect; the tab's own label present; and **a NON-ZERO denominator of nodes scanned** --
*"A census whose denominator is zero has not measured an absence; it has measured nothing, and must read
NOT_EXERCISED rather than PASS."*

⭐ That is this fabric's **R-8** -- *a criterion grading a field's ABSENCE must also grade its PRESENCE* --
and `FWD-31` plus this amendment make `AMGT_RESAPP` the first endpoint here to carry it in ratified text on
two outcomes rather than in a record beside them.

**No outcome is added by change 2 and the intent is unchanged; it tightens HOW an existing clause is
proven.** That is the correct shape for an amendment to a fence whose requirement was already right.

**Change 1 (`FWD-31`) is unchanged from v0.27** and was reviewed at @`9fb74a6222`; that review's findings
stand and are not restated.

⭐ **THE SEQUENCING IS RIGHT AND WORTH NAMING:** landing change 2 while v0.27's half was already owed costs
ONE signature instead of two. A re-sign is cheap only when it is batched deliberately; this one was.

## WHAT THIS SIGNATURE DOES NOT COVER

- **It certifies TEXT, not achievement.** `FWD-23` is HELD and `FWD-26` is ungraded; `FWD-31` is NOT
  REALIZED. Nothing here grades a render.
- **`FWD-26` did NOT receive the same positive control.** It is the third outcome in the clause-1 render
  set and its fence was not amended. ⚠ **Whether it carries an absence clause needing the same treatment is
  an open question this signature does not answer** -- flagged for the next L4 touch rather than held
  against this one, since v0.28 is strictly better than v0.27 on the axis it moves.

**COST:** one commit-shape read, one id/card census, one non-ASCII scan, one hash cross-check.
**NON-APPLICATION:** a change that moves no ratified byte re-opens nothing.
