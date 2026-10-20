# /endpoint --forward -- IRPT_ANLREQ report engine (Core, then parity): FWD-9 to FWD-12

**Seat:** 1.0.0_SA_CTO~DELL2. **Date:** 2026-10-20 ~14:57Z.
**State:** DRAFT, put to Andrew at the dell2 terminal ~14:5xZ. These lines are NOT YET LANDED in the PRD. They land as
IRPT_ANLREQ PRD v0.25 (ENDPOINT section, appended after FWD-8) on his confirmation of the DONE WHEN lines.

**Brief:** `docs/briefs/irpt-anlreq-report-engine-core-then-parity-brief-20261020.md` @e197f63e58 (197 lines,
`4.0.0_SA_CRO~TCKT`).
**Authority:** `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/ANDREW_DIRECT_20261020_15xxZ_TCKT_SYNTHESIS_ANSWERS.md` @f2581e90b9.
**Numbering:** the PRD at v0.24 (@7b55cfefe1) holds FWD-1 to FWD-8, so the next unused number is 9. FWD-1 to FWD-8 are unchanged.

```
  FWD-9   Andrew judges the Opal Overview against the YCharts sample he supplied
          DONE WHEN  EXERCISED -- an Opal person files an Overview (no comparables) on the live product, opens the
                     Opal-generated report from the ticket, and Andrew reads it beside the 2026-09-16 YCharts
                     Comprehensive Overview sample and gives a verdict
          ACCEPT     Andrew says, having read both, whether the Opal Overview looks correct and has the right
                     information; anything he names as wrong or missing becomes work on the Overview pages
          SOURCE     Andrew 2026-10-20 ("I just need to see that export in a sample run to gauge whether it looks
                     correct and has the right information"); brief O1

  FWD-10  (Core, first) A reader can tell how the portfolio did against each comparable it was compared with
          DONE WHEN  EXERCISED -- one Multi-Comp filed on the live product (two Opal models and one ETF) shows, for
                     the portfolio and each comparable: a cumulative return chart over one common window, periodic
                     total returns, risk figures (standard deviation, Sharpe, Sortino, drawdown, alpha and beta, each
                     against a stated reference) and asset allocation side by side. Opal computes every figure from
                     prices and held data, and the page states the common window and its rule
          ACCEPT     a person reading the report can answer "did this portfolio beat each model I picked, and with
                     how much risk" without opening YCharts; nothing Opal can work out from prices it already holds
                     is shown as unavailable
          SOURCE     Andrew 2026-10-20 ("We can start with Core to get a functioning chart out"); brief O2, Part III

  FWD-11  (Parity, starts as soon as FWD-10 is met) The Opal Comparison and Multi-Comp reports carry every kind of
          information the YCharts versions do
          DONE WHEN  EXERCISED -- one Comparison and one Multi-Comp, filed after FWD-10 is met, show for the
                     portfolio and each comparable: region and country, style and market cap, sector, bond sector,
                     credit quality and maturity, fundamentals, the risk/reward scatter, standardized returns and the
                     holdings tables
          ACCEPT     someone who knows the YCharts comparison and multi reports finds each kind of information in the
                     Opal report, or a plain sentence saying why it is missing for that comparable
          SOURCE     Andrew 2026-10-20 ("as soon as we get that done, the build for the full parity version should
                     get started"); brief O3

  FWD-12  A part of the report Opal cannot fill says so in words
          DONE WHEN  EXERCISED -- in a report where some comparable has no source for a part, that place on the
                     page reads "not available for <comparable>: <reason>"; the PDF carries no construction cards
          ACCEPT     a reader never meets a blank or silently missing section; each gap says what is missing and why,
                     and the report still reads as a report
          SOURCE     brief O4
```

## Readings stated to Andrew

- FWD-9 is not a gate on FWD-10. His words ask to see a sample, not to hold Core (CLAUDE.md section 2: never convert his
  word into a gate).
- The front-end walkthrough rulings are built by `4.0.0_SA_CRO~TCKT` in one closer pass: an advisor field pre-filled and
  editable, the date field removed, Enter-to-chip ETFs, and the audit record in the firm bucket. They fold into FWD-1 and FWD-2
  text in the same v0.25 after that pass. They are not new outcomes here.
- Run 7 (GO 14:31Z) is a request with comparables, so it does not meet FWD-9; one Overview filing follows it.

## Provenance

- **READ:** the brief above, in full. The PRD v0.24 ENDPOINT section (lines 25-104) and its header `endpoint_outcomes`.
  Andrew's record @f2581e90b9.
- **NOT READ:** IRPT_ANLREQ task-order files, decompositions, the project JSON's `phase` and `blocking` fields, the YCharts
  sample PDF (client document), and the maps beyond the brief's own figures.
