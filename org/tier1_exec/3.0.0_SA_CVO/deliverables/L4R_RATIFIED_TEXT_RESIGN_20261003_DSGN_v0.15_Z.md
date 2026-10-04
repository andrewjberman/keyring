# L4-R ratified-text half -- DSGN_AMGTV1 v0.15 -- SIGN

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-03 ~23:1xZ
**Delivery:** `1.0.0_SA_CTO~Z` msgs 29053 and 29055 at `ff31355b93`. The half hash, recomputed by this seat, is `36d8b7ee059b` and
equals the delivery.
**Method:** the ratified-text sections at `4bf316bb48` (v0.14, signed @`9f10f10ea4`), diffed against `ff31355b93`: +12/-10, in FWD-1,
FWD-4, FWD-13 and FWD-22.

## What moved

| FWD | change |
|---|---|
| FWD-1 ACCEPT | "reads its header as four cards and opens the Financials one" becomes "reads its header's key figures (v0.15: the SAUX-03 row)" |
| FWD-4 | "headline figures as four cards, each opening to the detail" becomes "headline figures at a glance in the header". ACCEPT: ONE key-figures row (price, market cap, enterprise value, net debt, beta, average volume, short interest), every figure at rest, none appearing twice, and every money figure in the company's own currency |
| FWD-13 | its DONE WHEN reads the figures "in the header's key-figures row" and "in the row once, under its plain label" instead of "on the four header cards" / "on one named card" |
| FWD-22 | at 90D/365D the face may print the served "not produced yet" reason instead of bars (FWD-26 v0.11's interim branch) until the PX_LAST history serves |

## Review

- **FWD-1/4/13 follow their pin.** The register row SAUX-03 (`docs/briefs/amgt-security-analysis-ui-findings-20261002.json`) accepts
  "one key-figures card with every figure at rest (price, market cap, enterprise value, net debt, beta, average volume, short
  interest), or each opened modal adds only figures that are not on the face; no figure appears twice". v0.15 takes the first branch
  word for word.
  - The row is `andrew_item: inferred`. Andrew's ~17:33Z word authorized inference ("you can infer off that basis what other things
    could be similarly improved"), and the CTO folded it at v0.9.
  - The built page already reads this way: this seat's round-29 read of BA (v33) saw seven key figures in one row.
  - "every money figure in the company's own currency" and "walked on names in more than one currency" are kept.
- **FWD-22's clause** is the mirror of RESAPP FWD-36's interim branch that this seat asked for at v0.35/v0.11. It is not a read of the
  90/365 price path.
- **Nothing else moved** in ENDPOINT or CONTRACTS.

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
