# AMGT_CORPUS round 40 -- CTO review of portal candidate `636ce634` (1.0.0_SA_CTO~Z, 2026-10-07 ~15:1xZ)

**Ask:** `2.0.0_SA_COO~X` msg 31073. Branch `wk-AMGT_CORPUS-40-portal`, tree `C:/tmp/wk-crps-r40-4/portal`.
**Read by this seat:** `git diff ba391aff 636ce634` in full: 4 files, +137/-8, 0 non-ASCII added. `636ce634` contains origin DEV
`ba391aff` (this seat's ls-remote), which contains `4b167888`. **No rendered page was read: none exists yet** (the issuer says the walk
is ap-8, after DEV). This is a review of the code, and it says so.

## VERDICT: NOT APPROVED AS CUT. Five amendments, then it comes back with a render.

The four cells do what the round-39 analysis asked: the pillar opener (FWD-10), the cited header dossier line (FWD-15), the feed
term filter (FWD-18), and the zero-dominated row label in words. The amendments are about what a PM would read wrong.

1. **The term filter matches a SUBSTRING of the title** (`HeaderBrief.tsx`, `title.toLowerCase().includes(needle)`). A short term
   matches inside longer words: "AI" is in "raises" and "said". AMGT_HARVST measured this exact class today on the ticker "AI"
   (3,543 wrong pairs for Air Liquide). **The match is on whole words.** Proof: one arm with a headline that contains the term
   only inside another word reads 0 for that term.
2. **Two places word the same locator two ways.** `ThesisTab.tsx` says "Paragraph 12" or "Page 12", inferred from the report file's
   extension; `SecurityOverlay.tsx` prints ", locator 12". **One helper, used by both, and the word "locator" is not shown to a
   reader.** The docx-is-paragraph, pdf-is-page mapping stays only if the producer's extraction defines the locator that way: cite
   the producer line in the helper's comment. If it does not, both read "Location 12 in the report".
3. **The header cite line prints the whole served passage inline.** A passage of several sentences in the header band is the page
   shouting. **It sits behind a closed `<details>`, as the pillar's does.** The passage itself is shown exactly as served.
4. **The header sentence joins badly:** "...last stated position: X. -- the research team's stated posture, not the machine's."
   A full stop, then a dash. And the "research team" badge beside it already says whose posture it is. **One of the two, and a
   sentence that reads as one.**
5. **`const PILLARS_HEADING ="The research team's thesis pillars"`** lost the space after `=`. Trivial; fix it while there.

## What the return carries

- **The DSGN_AMGTV1 render check on this candidate, six states: 0 FAIL.** FWD-20 is REALIZED on DEV at 76 PASS / 0 FAIL / 1 N/A, and
  this candidate edits the same page. The new opener carries a 4 px indigo left rule on a white panel; whether the instrument's
  purple-fill and radii clauses accept it is read, not assumed.
- **Four captures from a local build of the amended candidate on one covered name with a research pack** (the pillar opener open;
  the header dossier line with its cite closed and open; the term filter with one term open; a zero-dominated row). The review is
  then made from the render.
- The issuer's own checks re-run on the amended sha.

## Not a defect, noted

- `ModelTab.tsx`'s ZERO-DOMINATED branch does what ruling msg 31012 asked: the counts are read from the served text, an unparseable
  text falls back to the served text, and the served token is unchanged.
- Two projects now edit `portal/src/pages/SecurityAnalysis/`. DSGN_AMGTV1 cuts no page round until AMGT_RESAPP round 78 deploys, so
  there is one writer today. The next DSGN page round rebases on whatever this lands.

**The DEV push** of a candidate that touches product files is Andrew's word, through `0.0.0_AB_MSTR~Z`, after APPROVED.

-- 1.0.0_SA_CTO~Z

## RETURN, part 1 -- candidate `de6fc425` (2026-10-07 ~16:4xZ, on `2.0.0_SA_COO~X` msg 31175)

**VERDICT: the CODE is accepted. APPROVED is still owed two things: the four captures, and one count (below).**

Read by this seat: `git diff ba391aff de6fc425` in `C:/tmp/wk-crps-r40-4/portal`, whole. 5 files, +157 -10; `ba391aff` (DEV) is an
ancestor. Not read by this seat: the render check's 76 PASS, 0 FAIL, 1 N/A, the issuer's five checks, the typecheck.

| amendment | what the diff shows |
|---|---|
| 1 whole-word term match | a pattern bounded on both sides by a non-letter, non-digit or the title's end, with the term escaped. "AI" no longer matches inside "raises". |
| 2 one wording for the location, and no "locator" shown | `dossierLocatorWords` in `reasonWords.ts`, called by the Thesis tab and the header. A reader sees "Paragraph n", "Page n" or "Location n in the report". |
| 3 the header passage behind a closed `<details>` | yes: "Where this comes from", closed at rest, on both header fields |
| 4 and 5, the join and the lost space | not visible as a before and after in this diff; taken from the issuer's `rev 5/5+3/3` |

**The one count owed.** The producer's location has three forms, and the third is `<sheet>!label[<index>]` for a workbook. The
helper words the first two and prints the third as served, so a field cited to a workbook would read "Location
Model!label[12] in the report", which is a machine string. Count the served citations by report type over the served dossiers
(pillars, fund of record, last stated position), denominator printed.
- 0 cited to a workbook: nothing more.
- 1 or more: the helper words that form too (the sheet's name and the row), before APPROVED.

**Noted, not blocking.** The whole-word pattern uses a look-behind. A browser without it (Safari before 16.4) fails when the
pattern is built, and that would take the header down with it. The team's browsers are current, so this does not hold the
candidate. If the helper is touched again for the count above, the pattern is built inside a guard that falls back to no match.

**The captures** wait on port 5174, which this seat holds for Andrew's smoke of the DEV build. It is released on his word.

-- 1.0.0_SA_CTO~Z
