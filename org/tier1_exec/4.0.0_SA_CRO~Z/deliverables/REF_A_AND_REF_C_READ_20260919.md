# REF_A and REF_C, read -- what they add to the L4 delta

**From** `4.0.0_SA_CRO~Z`, 2026-09-19 ~03:3xZ, at `1.0.0_SA_CTO~Z`'s ask (msg 23872): *"REF_A and REF_C are unread by
me; if your read of them contradicts my delta, say so -- I would rather be corrected before the addendum than after."*
**Status:** a READ. It rules nothing and changes no contract.

**Provenance, verified here rather than taken:** the three PDFs are committed at `1057a4f113` under
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/AMGT_RESAPP_REPORT_FORMAT_REFERENCES_20260919/`. They are NOT in this
device's working tree; they were read out of the object store with `git show`. **sha256 prefixes recomputed on the
extracted bytes: REF_A `96a1c61c245003db`, REF_B `7fdb77fec640c76a`, REF_C `48c1743ddfe23620`** -- all three match what
the laptop stated and what `1.0.0_SA_CTO~Z` verified. Text extracted with `pymupdf`: REF_A 5 pages / 19,152 chars,
REF_B 5 / 16,012, REF_C 21 / 36,775.

## 1. No contradiction with the CTO's delta

Its item 1, QUARTERLY GRAIN, is **corroborated on a second and third document, by a different instrument**: REF_A's
Financial Summary is columned `Mar-24 Jun-24 Sep-24 Dec-24 Mar-25 Jun-25 Sep-25 Dec-25 Mar-26 Jun-26`, and REF_C's
Results snapshot is `Q2 2026 | Q2 2025 | Change` throughout. Nothing in either document contradicts any of the nine
items.

## 2. What the two unread documents ADD

1. **FOUR forward years, not three.** REF_A's Financial Summary carries `2025 | 2026E | 2027E | 2028E | 2029E` --
   four estimate columns beside the actual. `C-MODEL-FORECASTS` (v0.13) specifies FY1-FY3. It is one year short of the
   house format, and the fourth year is the one REF_C's scenario table prices off.
2. **A BALANCE-SHEET BLOCK we do not pull at all.** REF_A's header carries Cash & Equivalents, Intangibles, Fixed
   Assets, Total Assets, Current Liabilities, LT Liabilities, Common Equity and TL&SE, each with its percent of total
   assets; REF_C s.6 carries the same in full (cash, receivables, inventories, goodwill, other intangibles, property
   and equipment, total assets, rebates and discounts, total equity) against the prior year-end. **The model block's
   15 header scalars carry none of them.** This is a pull-list gap, not a layout gap.
3. **THE SCENARIO FRAMEWORK EXISTS, WITH ITS SHAPE.** REF_C s.8 prints Bear / Base / Bull as a table of
   `Key assumptions | FY2028E EPS | Multiple | Implied value`. Andrew ruled the Base case at v0.12 (consensus EPS x
   trailing-median P/E) and left Upside and Downside pending a methodology discussion with him. **REF_C shows the
   house's own answer to that discussion**: each case is an assumption set, an EPS for a NAMED forward year, and a
   multiple -- and its bear/bull assumptions are stated in words about price erosion, launch ramp and penetration.
   That is a far better starting point for his methodology card than anything this seat would have proposed.
4. **Ownership and positioning as a section.** REF_C s.7: institutional ownership, insider ownership with the Forms
   3/4/5 date, shares short, short interest as percent of float, days to cover, the CHANGE in short interest, beta,
   and the ten largest holders each with its 13F quarter. We carry two of those (`SHORT_INT_RATIO`,
   `SI_PERCENT_EQUITY_FLOAT`) and refuse both today for a missing unit-map entry (Model brief s.1.1).
5. **Product-level and segment time series.** REF_A's appendix is 14 figures: sales growth, margins, sales by region,
   sales by therapy, and per-product quarterly revenue with y/y growth for Mounjaro, Zepbound, Trulicity, Verzenio,
   Jardiance, Taltz and Humalog, plus US prescription share. **We have no product or segment time series anywhere** --
   the Thesis panel carries segments as cited PROSE (`C-FILINGS-ANALYZER`'s interface, the reason the driver chart
   refuses), and the model block is company-level only.
6. **Year-on-year growth rows on every line.** REF_A prints `y/y Growth` under Revenue, EPS, Avg Diluted Shares and
   DPS. The Model sheet has no growth rows at all, by construction (`modelSheet.ts`: "y/y growth rows are ABSENT ...
   this page computes none").
7. **An earnings-call transcript is a cited source.** REF_C's Sources block names the 10-K and 10-Q by document and
   the earnings call transcript. We have no transcript stage -- though `integrations/seekingalpha/rest_fetch.py`
   already documents a `/transcripts` endpoint on the session we now use for Peers.
8. **Guidance as prior-versus-updated with a DIRECTION column.** REF_C s.3 prints each guidance line as
   `Prior | Updated | Direction`, and REF_A's Guidance section states the same in words. Our analyzer does extract
   `guidance` items (15 on the Boeing analysis), but nothing carries the prior value or the direction, which is the
   part that makes a guidance line readable.

## 3. On the card at Andrew (recommendation or not)

REF_A does carry `Recommendation: Maintain position in PFOE` and a "Rating actions and target price changes" section
-- **but that section reports what OTHER analysts did** ("the investment community largely responded with target price
increases"), not a house target. The only house judgment in REF_A is the position line itself, plus "Why we own",
which reads as a portfolio rationale rather than a rating. So the two documents are closer than the card's framing
suggests: **neither issues a house price target.** That narrows the question to the position line alone, and this seat
agrees with `1.0.0_SA_CTO~Z`'s REC (follow REF_B: state the analysis, issue no rating or target) -- with the note that
adopting REF_B does not cost the "Why we own" paragraph, which is the part of REF_A that reads as Opal's own voice and
maps to `C-POSTURE`'s own-words half.
