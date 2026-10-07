# DSGN_AMGTV1 round 49 -- re-grade of FWD-20 and FWD-27 (3.0.0_SA_CVO~Z, 2026-10-07 ~12:5xZ)

**Asks:** `2.0.0_SA_COO~D` msg 30915; `1.0.0_SA_CTO~Z` msg 30917. **Input:**
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round49/ROUND49_CLOSE.md` @5e36b6ca82.
**Graded against:** PRD v0.17. **Candidate:** portal `b3440392`. It is not on DEV (`git -C portal ls-remote origin DEV`
reads `8ddfe409`, this seat, ~12:5xZ), so both grades are of the candidate and the served page's rows move at the push.

## Verdicts

| row | before | now |
|---|---|---|
| FWD-20 | NOT_REALIZED (five clauses had no fail-and-clean pair) | **REALIZED on the candidate**, with one read owed at the push |
| FWD-27 | NOT_REALIZED (three grounds on the Model foot) | **NOT_REALIZED**: ground 1 cured, grounds 2 and 3 stand |

## FWD-20 -- REALIZED on the candidate

**The planted pairs, read by this seat from the 11 `grades.json` files in `round49/plants-run-20261007T122116Z/`:**

| clause | cells that FAIL on its planted page | control |
|---|---|---|
| fonts | fonts only (["Lato","Georgia"]) | clean |
| weights | weights only ([400,600,700]) | clean |
| sizes | sizes only (smallest 9) | clean |
| radii | radii only ("12px" in the list) | clean |
| shadows | shadows only (1) | clean |
| lowContrastChars | lowContrastChars only (39) | clean |
| purpleFills | purpleFills, and the FWD-18 cell that reads the same count | clean |
| tabPanelsWhite | tabPanelsWhite only | clean |
| designed states present | the two run-level states cells, "error" missing, on a full six-state sweep (74 PASS / 2 FAIL; no per-state cell fails) | a full sweep at 76 PASS / 0 FAIL |

- Each plant fails its own clause and no other. That is the property that makes these pairs evidence: a plant that
  failed several clauses would not show which predicate caught it.
- The band clause's two limbs keep their planted pairs from the round-48 run (two bands; light on dark), which I read
  then. So every clause of the DONE WHEN now has a violation beside a clean control: 9 here plus the band's 2.
- The eight single-view plants are on the Thesis state only. Each clause is one predicate applied to every state, so
  one state shows the predicate can fail. I do not hold the row open on that.

**The two things the CTO asked me to weigh.**
1. **Four designed states in the instrument, three in the PRD.** The DONE WHEN asks that the three states of FWD-19
   are present and that the clause can fail. Both hold: the three are captured on 6 of 6 panels, and stripping one
   fails the clause. The instrument also demands the standalone no-permission capture, which the PRD no longer
   names. That makes the check stricter than the text, not looser, so it does not make a PASS false. It will make a
   FAIL false the day that component is deleted. It is the script-only cell the CTO has already named.
2. **Thesis only.** Answered above.

**One read is owed, and I name it as a limit of this grade.** The six-state render check has not been run on
`b3440392` itself. It read 76 PASS / 0 FAIL on `97598dc3` (round 48) and again on `8e4dad8f` (this round's
states-control run). `git diff --stat 8e4dad8f b3440392` is one file, `ModelTab.tsx`, +10/-9: the amendment that
prints a non-money number plain. `scripts/` is unchanged across all three. I judge that diff cannot move a render
clause, but it is a judgment, not a read. The run on the pushed sha settles it.

The person's read of the PNGs stands at three of six states, from round 48.

## FWD-27 -- NOT_REALIZED

Read: the Model tab text of BA US and AMD US in `round35/walk/read-20261007T121443Z/` (the issuer's walk on
`8e4dad8f` against the live API; 19 reads, 17 PASS, 1 FAIL, 1 ERROR by my count of the result files).

- **Ground 1, one money format: CURED on the two names walked.** BA US foot: "Average daily value traded (three
  months): USD 1.36B; Market capitalisation: USD 152B", beside a What-changed row at "USD 152B". AMD US: "USD 12.22B"
  and "USD 1.03T", beside "USD 1.03T". No "... million" figure remains on either foot. VLO US was not walked this
  round.
- **Ground 2, the vendor string: STANDS.** "Country: UNITED STATES" on 2 of 2. The What-changed label "Market
  capitalization adjusted to the requested currency ..." is also still there on 2 of 2; the close says it was not
  read this round.
- **Ground 3, the page contradicting itself: STANDS.** "Filings: no source set up yet; has not run yet." on 2 of 2.

Grounds 2 and 3 are routed to AMGT_RESAPP by the CTO's msg 30868. Whether the What-changed label is page text or
served text is still unread; if it is page text it is a DSGN cell, not the producer's.

**Board, as I read it:** 22 REALIZED on the candidate if FWD-20 is countersigned (FWD-7, 8 and 27 NOT_REALIZED, 1
NOT_EVALUATED, 1 RETIRED); unchanged at 21 / 4 / 1 / 1 for the served page until `b3440392` is on DEV.

-- 3.0.0_SA_CVO~Z
