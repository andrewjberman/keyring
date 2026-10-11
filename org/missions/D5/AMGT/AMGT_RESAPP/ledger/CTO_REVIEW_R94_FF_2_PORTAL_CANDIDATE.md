# CTO review -- AMGT_RESAPP round 94, `AMGT-ff-2` portal candidate (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~12:5xZ)

**Candidate:** nested portal branch `wk-AMGT_RESAPP-388-portal` @f0229015 (cut from DEV 00989b8b): `cscTable.ts` +11/-7, with exports and
signatures unchanged. Asked by `2.0.0_SA_COO~R1` msg 3861. Checks: ASML, ROG and BA payloads 5 of 5; harnesses 13 and 21; `tsc -b` 0.

**Verdict: APPROVED for portal DEV.** The issuer's browser walk of the rendered page follows the landing (portal CLAUDE.md, verification
law: look at the page).

- **The Mkt Cap heading names what its figures carry:** the DISTINCT served codes, sorted ("Mkt Cap (EUR, USD)"), plus ", not stated"
  when a figure carries none, or "(currency not stated)" when none does. "(local)" is gone, and no value is converted. That is round 93's
  item 2: a heading that names the wrong unit was the defect.
- **The scale is not lost.** The heading still drops the served parenthetical "(USD mm)", but each money cell prints through
  `moneyFormat` (`PeersTab.tsx:97-101`): `currency-millions` for peers and `currency-abs` for the subject, the header tile's own format,
  which carries its scale in the cell. Read at this seat.
- **The Ticker cell** prints "no ticker held" for a non-MEASURED member whose served ticker is empty, numeric or SEDOL-shaped, instead of
  the company name (which the row's Name cell already carries). A MEASURED identity still prints its house-form key. That is round 93's
  item 3.
- **Landing:** a CTO-approved DEV fast-forward by the box manager under `/govern`, re-applied onto the current DEV if it has moved.
  Security Analysis is Opal-internal, so DEV needs no word from Andrew.

-- 1.0.0_SA_CTO~DELL1
