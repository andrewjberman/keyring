# DSGN_AMGTV1 -- FWD-20's clause count, and the FWD-27 re-grade on the round-47 candidate (3.0.0_SA_CVO~Z, 2026-10-07 ~12:0xZ)

**Asks:** `1.0.0_SA_CTO~Z` msgs 30858 (which clauses remain) and 30860 (grade FWD-27 on `round47/ROUND47_CLOSE.md` item 2).
Both are read on a candidate that is not on DEV (`git -C portal ls-remote origin DEV` read `8ddfe409` at 11:5xZ).

## 1. FWD-20: which clauses still lack a fail-and-clean pair

Ruling (msg 30858): every clause needs one violation beside a clean control; a clause that failed on the real page and
then passed after its fix has its pair already.

Source: the five `grades.json` files of the round-48 run, `C:/tmp/r35-scratch-c/out-20261007T112904Z/` (device-local),
read cell by cell by this seat. "Pre" is the real pre-redesign page, portal `8fa7abde`; "candidate" is `97598dc3`.

| clause of the DONE WHEN | where it FAILS | where it is clean | pair? |
|---|---|---|---|
| bandContainersTopLevel <= 1 | planted two-bands page (value 2) | planted control; candidate 6 of 6 | YES, planted |
| lightOnDark == 0 | planted light-on-dark page; pre, 6 of 6 states | planted control; candidate 6 of 6 | YES, planted and real |
| no size below 11 | pre, 5 of 6 states (smallest 10); round 46's Model state | candidate 6 of 6 | YES, real |
| lowContrastChars == 0 | pre, 5 of 6 states (value 6) | candidate 6 of 6 | YES, real |
| purpleFills per FWD-18 | pre, 5 of 6 states (value 1 in a Security state) | candidate 6 of 6 | YES, real |
| fonts == {Lato} | nowhere: 0 FAIL cells in all five runs | -- | **NO** |
| weights within {400,700} | nowhere | -- | **NO** |
| radii within {2,3,4,pill} | nowhere | -- | **NO** |
| shadows == 0 outside the focus ring | nowhere | -- | **NO** |
| the three states of FWD-19 present | only when the sweep is not run (a missing capture, not a violation) | candidate | **NO** |

**Five clauses remain: fonts, weights, radii, shadows, and the states-present clause.** Round 49's cell needs five
planted pages and can reuse the existing clean control.

**A correction to my re-grade file** (`DSGN_AMGTV1_ROUND48_FWD18_FWD20_REGRADE_20261007.md` @4a94e19089): it listed
lowContrastChars among the clauses with "no planted page and no observed failure". That was wrong. The pre-redesign
page fails it on 5 of 6 states in the same run; I had not tabulated the pre-redesign cells when I wrote it.

Not a clause of the DONE WHEN, noted: the instrument also grades `tabPanelsWhite`, which fails nowhere.

## 2. FWD-27 on the round-47 candidate `ec9f9a0e` -- NOT_REALIZED, moved

Read: the Model tab text of BA US, VLO US and AMD US in `round35/walk/read-20261007T105958Z/` (files 09, 12, 15), the
three display-name reads (24, 25, 26) and the account-menu read (23). These are the issuer's walk on the candidate
against the live API; I did not re-walk.

**Cured, both round-46 grounds:**
- The vendor short-name line is gone on 3 of 3 names; "CO/THE" appears nowhere in the BA US Model text. The
  display-name reads carry one string per security (10, 10 and 9 surfaces).
- The system wording is replaced: "2 of 6 kinds of input have been collected for this name." and "News: Articles we
  collect; last ran October 5th, 2026 and worked."

**Still on the same foot, 3 of 3 names, which is why the row does not close:**
1. **One money format (the DONE WHEN's third limb).** The foot prints "Market capitalisation: USD 152,320 million" and
   "Average daily value traded (three months): USD 1,356,158,848" on a page whose header and What-changed table print
   market cap as "USD 152B". That is three money formats for page-formatted figures on one tab.
2. **A vendor string beside the page's own form.** The foot prints "Country: UNITED STATES" where the identity header
   prints "Industrials -- US". It is the same class as the short-name line that was removed. One What-changed row
   on BA US is also labelled in the vendor's words: "Market capitalization adjusted to the requested currency
   (Bloomberg's currency-adjusted market capit...".
3. **Two statements that disagree.** The foot says "Filings: no source set up yet; has not run yet." The Exec tab of
   BA US and VLO US lists officers "from Item 10" of the 10-K, and the Thesis is drawn from the 10-K. A reader is
   told the filings both feed the page and have never run.

**These three were on the page at round 46 and I did not cite them then.** I read the foot for the two lines the
round-41 list named and stopped. They are not regressions.

Whether items 1 and 2 are page text or served text is unread; round 47's "all three lines were page text" covered
the three lines it changed. Item 3's input list is likely the producer's (AMGT_RESAPP). The first act of a round-49
cell is that read.

Holding and unchanged: Escape closes the account menu; officers and time zone were not re-read for this grade.

**Board, as I read it after msg 30860:** unchanged at 21 REALIZED, 4 NOT_REALIZED (FWD-7, 8, 20, 27), 1
NOT_EVALUATED, 1 RETIRED.

-- 3.0.0_SA_CVO~Z
