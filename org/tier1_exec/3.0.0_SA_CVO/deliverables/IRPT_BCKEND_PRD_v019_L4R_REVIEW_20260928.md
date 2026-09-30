# L4-R review -- IRPT_BCKEND PRD v0.19, ratified-text half (`3.0.0_SA_CVO`)

**Delivery:** `1.0.0_SA_CTO` msgs 102484/102485 (2026-09-28 23:46Z). **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`
@`82e1700237`, half hash `3c9b580c62c4` (per the delivery). **Last signed ratified text:** v0.17 @`1450e05178`
(`3.0.0_SA_CVO~B`). **Pins read:** `391ab19331` (Andrew-direct ~22:2xZ, call 3) and `0b6f598df4` (Andrew-direct ~22:4xZ),
both verbatim blocks read in full.

**Verdict: SIGN.** Two wording items are owed and one reading is flagged for Andrew. None is a condition.

## What changed in ENDPOINT (v0.17 -> v0.19, section diffed line by line)

Exactly three outcomes: FWD-3 re-cut (vendor calculation -> Opal's holdings basis), FWD-12 added (the daily
holdings-basis gold and its manifest), FWD-13 added (a bounded comparison with the vendors' official figures). No other
line of the section moved. CONTRACTS is byte-identical to v0.17 (138 lines each, empty diff).

## Against the ratified pins

| Andrew's words (verbatim block) | ENDPOINT v0.19 | reads |
|---|---|---|
| "cash movements should not matter at all"; "We cannot get involved with inflow/outflow logic" | FWD-3 CONSTRAINT "NO INFLOW/OUTFLOW LOGIC: cash movements do not enter the calculation" | present |
| "calculating performance in any other basis other than end of day asset holdings values" | FWD-3 CONSTRAINT "the only inputs are end-of-day asset holdings values" | present |
| "daily, pro-rated by weight, performance of any securities in a given basket on a given day"; "tracking the delta from the previous day" | FWD-3 ACCEPT "each day's account return is the weight-pro-rated return of the securities it held ... the delta taken day over day; period figures link the daily returns" | present |
| "the weight of the assets relative to the account in question **on the subject day**" | FWD-3 ACCEPT "weights relative to the account's end-of-day value **on the prior day**" | a READING (item R1) |
| "move to holding-based strategy for all channels" | FWD-3 DONE WHEN "one invested account per firm (49F, INF, COT)" | present |
| "assess what is needed in opal-data-assets silver tables ... per firm" | FWD-12 ACCEPT "a per-firm SOURCE DECLARATION (as data) names the silver table, keys, date, value and price columns" | present |
| "a consolidated shape in Gold that is the singular form that the IRPT page reads" | FWD-3 ACCEPT "the page and the export read ONE gold shape in which the firm is a column, never a firm code path" | present |
| "We run this on a daily basis" | FWD-12 "produced every trading day"; "lands daily on its own schedule" | present |
| "verification is ... the 'official' performance reporting for pre-set periods ... compare our methodology at those defined points" | FWD-13 "at pre-set periods"; CONSTRAINT "a bounded check at defined points, never a standing parity comparator" | present, and inside CLAUDE.md section 5's veto |

Operative constraints also present: the FWD-12 addresses are builder calls, and `lib/opal_naming.py address()` returns
all six (run by this seat: `s3://opal-data-{49financial,cottonwood,inflection}/irpt/<firm>/gold/holdings_performance_{daily,manifest}/date=2026-09-25`),
so rule 30 holds. The trading-day axis names `lib/trading_calendar.py`. The gold reads silver only. An ABSENT day
never rolls forward or fills with zero. A new vendor pull needs Andrew's per-use word. The retired rule is gone: 0
hits for vendor calculation in the v0.19 section.

## Items

- **R1 (flag for Andrew, not a condition):** the weight date. Andrew's words say the weight relative to the account
  "on the subject day"; the ENDPOINT says prior-day end-of-day value. The CTO names this as its design reading in
  ADDENDUM v0.19 ruling 2 ("each is a design reading of Andrew's basis that his word can correct"), so it is not
  silent. The prior-day reading is the one that keeps a price-return calculation free of flows: a subject-day weight
  already carries the day's move. It is still the one reading that changes every served number. Recommend that
  `1.0.0_SA_CTO` put it to Andrew as a one-line confirm before FWD-3 is graded REALIZED for the first firm. If he
  answers "subject day", the ENDPOINT changes and this half re-signs.
- **W1 (owed wording):** FWD-3 CONSTRAINT carries "(Andrew-direct 2026-09-28 ~22:2xZ and ~22:4xZ)". That is history
  inside the ratified section, and the PIN line already carries `0b6f598df4`. Move it to ENDPOINT PROVENANCE.
- **W2 (owed wording):** FWD-13 CONSTRAINT carries "(Cottonwood has none landed)". That is current state inside the
  section, and it goes stale the day a pull lands (addendum ruling 8 already carries it). The rule without it reads
  the same: "a NEW vendor pull for a comparison needs Andrew's per-use word". "(CLAUDE.md section 5)" is a law pointer
  and can stay.
  W1 and W2 are prose only. Fixing them changes the section hash and re-opens this half, as a formality. This seat
  signs rather than hold ~E's round 1 at LIMB 6 for prose (the same call as this seat's R11 export-receipt sign, `a683fef3ae`).
- **C1 (counterpart, noted):** the counterpart IRPT_FNTEND PRD still words FWD-3 as vendor-calculated and names
  "the vendor-calculation-only rule" (`IRPT_FNTEND_PRD.md:29-33`). IRPT_FNTEND is closed (`project.json` status
  `closed`), and the live frontend PRD, DSGN_IRPTV1, carries no vendor-calculation rule (0 hits). No live contract
  disagrees. If IRPT_FNTEND ever re-opens, its FWD-3 needs the same re-cut.

## What you should have asked but did not

Whether the holdings basis can reproduce the vendor figures FWD-13 compares against at all. The addendum's ruling 3
gives cash a zero daily return and ruling 4 drops unpriced positions and renormalizes. The vendors' official figures
include income, accruals and cash-flow timing. So a non-zero FWD-13 difference is expected by construction. FWD-13
already says the difference is "never forced to zero". The unasked question is the TOLERANCE at which a difference
reads as a method gap rather than a defect. With no stated band, the first comparison cannot fail, and FWD-13 reduces
to "a number was printed". Recommend the CTO's round-1 analysis states that band per firm, from the first 49F
comparison, before FWD-13 is graded.

-- 3.0.0_SA_CVO
