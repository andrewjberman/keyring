# DESIGN FORK CARD -- does the Performance window end on the holdings as-of (one date per page) or on its own source's as-of?

**For:** 1.0.0_SA_CTO (msg 101757, from 2.0.0_SA_COO~D 101751). **By:** 4.0.0_SA_CRO, 2026-09-27 ~03:5xZ. Read-only.
**The fork:**
- **(a)** every Performance preset ends on the holdings snapshot's as-of, so the page carries one date (today's rule, CTO 101422);
- **(b)** Performance ends on its own source's as-of (Orion / twr), with each section's date on the face.

## REC: (a), with an exception label

- The page has ONE date: the holdings business date in the header (FWD-2), and Performance presets end on it.
- A section whose own source cannot reach that date shows its own date on its face, in the page's one date format.
  For example: "Returns through Sep 18".
- The gap that prompts the fork (INF holdings 09-22, INF directory and Orion 09-25) is holdings staleness. Fix it at
  the source (UIR-23, by the R4 scheduled T-1 publication), not by giving each section a fresher date.

## Findings (each with what was read)

1. **The PRD already puts one date in the header.** FWD-2 (`DSGN_IRPTV1_PRD.md:56-58`): the advisor "answers who /
   how much / as of when", and the header shows "the holdings total and the business date".
2. **CTO 101422 admits both readings.** Presets "end on the data's as-of (business) date from the served response or
   snapshot, never on the browser's calendar date". It does not say WHICH data. ~D's implementation reads the
   holdings snapshot, and that is the choice now being decided.
3. **Andrew's own acceptance rule fits either option, as long as the difference is labeled.** UIR-33: "Every
   percentage states its base (of this account / of the client), or both views use one base". The same rule appears
   in UIR-36 and UIR-47. Carried over to dates:
   - one date for every section meets it;
   - a labeled difference meets it;
   - an unlabeled difference fails it.
4. **The gap is a defect, not a steady state.** Andrew's UIR-23 reads: "Holdings are as of 2026-09-22 on Saturday
   2026-09-26: three trading days behind". Its acceptance is "Holdings read as of the last trading day (T-1)", met by R4
   (PRD `:389`, `:418`). Once holdings are T-1, holdings, the directory and Orion all read T-1, and (a) and (b) give the
   same date. Under (a), today's cost is the 3-day lag, and it ends when R4 lands.
5. **Showing dates on the face collides with Andrew's review unless it is written as a client fact.**
   - UIR-28: "source dates Business/Observed" on the face are system facts and belong one click away.
   - UIR-45: three date formats on one page; the acceptance is one date format.
   - So (b)'s "each section's date on the face" re-opens UIR-28/45 unless the date sits in the period label as a
     client fact, in the one format.
6. **Black Diamond uses one date per page**, and Andrew said "match the same shape" (@964fb4ed6b).
   `ADVI_PERFRP_PRD.md:67-68` catalogues BD's Client View Portfolio Dashboard: a header "period picker (Last 3 Months,
   Year To Date ... as of date)" over nine cards. The Advisor Dashboard likewise has "period (Annually / Year to Date,
   as-of date, Apply)". There is one as-of date, set in the header, for every card.
7. **The way (a) goes wrong: one stamp that is untrue for a section.** CVO 2026-08-04
   (`ANDREW_DIRECT_de_portal_dataflow_assessment_20260804.md:46`): "the page's visible as-of stamp honestly reads the
   OTHER (timeseries) family, so 07-22 metrics wear a fresh page with zero on-screen tell". This is why the exception
   label is part of the REC: a section that does not reach the page date must say so.
8. **A value carries its own date.** The asset-management report format Andrew sent (Andrew-direct 2026-09-19,
   `ANDREW_DIRECT_20260919_023xZ_AMGT_RESAPP_REPORT_FORMAT_REFERENCES_CTO_INTAKE.md:40`) has "price WITH its as-of
   date". So does the doctrine `A_VALUE_MUST_CARRY_ITS_CLAIM`. The exception label is that principle, applied only
   where the dates differ.
9. **"Performance is account-level" says nothing about dates.** The record
   (`ANDREW_DIRECT_20260926_151xZ_PERFORMANCE_ACCOUNT_LEVEL_FRONTEND_ROUTES_CLOSER_TRACE.md`) returns 0 matches for
   date, as-of, window and period. It bears on grain, not on the date.

## Why (a) over (b)

- It is BD's shape (6).
- It gives Andrew's "one base" branch (3): the Performance ending value and the header's holdings total then describe
  the same day.
- It keeps system dates off the face (5).
- Its only failure mode, a stamp that is false for a section, is closed by the exception label (7, 8).

(b) shows fresher returns while holdings are stale. But it answers a source defect with page clutter, and it keeps
two dates on the face even after R4 makes them equal.

**Consistency:** the INF one-use plan re-cut to the served holdings as-of (ruling (b) at ~P 101752; this seat's
addendum 3) is (a) applied.

## What this card does not claim

- This seat did not open BD's rendered pages, only the ADVI_PERFRP catalogue of them.
- It did not measure how often an account's Performance source sits BEHIND its holdings as-of, which is how often the
  exception label would show.
- It did not read `period.ts`, the portal's date-window code.
