# IRPT_BCKEND PRD v0.35 -- ratified-text review (ADDENDUM v0.35, the date-basis claim repaired)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @289d8ddd27.
**Asked by:** `1.0.0_SA_CTO~DELL2` msgs 4987 and 4989. **Prior review:** `IRPT_BCKEND_PRD_v0.34_RATIFIED_TEXT_REVIEW_20261011.md` @3f67123932 (REFUSED).
**Verdict: SIGNED, with one point the first cell must carry.**

## The two defects

| defect of v0.34 | v0.35 | read |
|---|---|---|
| `OWN_DATE` admitted a day holding an ungradeable priced security | The claims are decided in a stated order and `UNGRADEABLE` is first: one or more priced securities the instrument cannot place at a close, "whatever its other rows read" | **Repaired.** A served day now has every priced row placed at its own date, or nothing the basis can move |
| The four kinds did not hold the anchor-not-landed day | A fifth kind, `ANCHOR_NOT_LANDED`, and the kinds are a list of every kind present | **Repaired.** It is also named as the only kind a later grading removes |

The two smaller points are answered: the order is in the text, and the four-postulate record and a token census are in it.

## What else this seat checked

- **The residue.** After the first three claims, what is left is a day with no ungradeable row and no gradeable moved security.
  That includes a day holding only securities whose close did not move. Its value is the same on either close, so calling it
  `NOTHING_TO_GRADE` and serving it is consistent with the claim's one intent.
- **The cost is honestly withdrawn.** 25.0 percent blank is now stated as a floor, and no gold producer is cut before the re-count.
- **The rename.** `PRIOR_CLOSE` is a value of another field at the three places the addendum cites; each line prints as cited.
  `PRIOR_DATE` reads 0 files.

## The one point the first cell must carry

**The census missed the tree the claim will be written in.** Its scope was the investor-reporting functions and the portal, and it
reads `OWN_DATE` 0. In `data/assets/scripts/gold/irpt_holdings_performance/`, the producer this addendum extends, `OWN_DATE` is
already a value: `holdings_performance.py:145` (`CLOSE_OWN_DATE = "OWN_DATE"`) and five `"holds": "OWN_DATE"` lines of `sources.json`
(printed by this seat). That is the SOURCE's declared basis. The new `OWN_DATE` is an ACCOUNT-DAY's measured claim. Same word, same
axis, two grains and two provenances, in one file family.

This is not a ground to refuse: the meanings agree, and the addendum says the rest of the repo was not swept. But a reader of the
gold will meet both. The first cell's record states the two, by field name, and says which one a consumer rejects on. The other
ten tokens read 0 files in that tree as well.

## The gate

The delivery for this review came by message from the CTO, as the addendum now says it will. The half's hash is unchanged from
v0.33 (`74a6900e44fe`), which is the gap recorded in IRPT_BCKEND row D2-S83: two contract-changing addenda under one hash.

## What this seat read

The addendum's 45 lines (`git show 289d8ddd27`); the three cited lines; a word-boundary census of eleven tokens over
`infra/aws/lambda/investor-reporting` and `data/assets/scripts`, and of four over portal DEV `src`. Not read: the instrument's code.
