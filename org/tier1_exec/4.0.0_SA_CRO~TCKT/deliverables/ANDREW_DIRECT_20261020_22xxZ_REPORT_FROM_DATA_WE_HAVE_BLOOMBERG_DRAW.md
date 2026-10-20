# ANDREW_DIRECT 2026-10-20 ~22:xxZ -- generate the report from data we have or can foreseeably get; maybe a Bloomberg draw

Channel: Claude Code session, seat 4.0.0_SA_CRO~TCKT (box dell2). Andrew's reply after he read the Opal Overview sample
that run 7d saved for him (`C:/dev/andrew_samples/Opal_Overview_sample_E2E7D.pdf`; REQ-bb8793fa8c8e2c9da8bc033d, 39
pages, 100 sections, 13 with values).

Verbatim:

> I just saw it. the issue with this generation is that we need to do it based off data that we actually have/forseeably
> could get. It could be a situation where we need to set up a draw on bloomberg for the individual security info and
> have the process work on that basis.

Two follow-on messages, same session, minutes later, verbatim:

> There are no data restraints for this, if we have to run it on bloomberg to get beta, duration, etc characteristics
> and so on to be able to generate a bunch of pie charts on concentrations and so on, then so be it.

> the purpose of sending the actual Y Chart packet is to basically assess what data we would need to be able to generate
> a packet

A third follow-on message, same session, verbatim:

> if we cannot get that from yfinance, then we need to get it from bloomberg

A fourth follow-on message, same session, verbatim:

> I do not give a shit what this packet looks like as long as it has a bunch of charts and concentrations and etc. on it

Read by this seat (his words above govern):
- THE BAR IS CONTENT, NOT LAYOUT: the packet must carry many charts and concentration breakdowns built from real data.
  Matching the YCharts page layout is not required. The sample is a guide to what data is useful, not a template.
- SOURCE ORDER for per-security information: yfinance first; Bloomberg where yfinance cannot supply it. This matches
  the PRD v0.22 rule "yfinance first ... everywhere in this process".
- NO DATA RESTRAINT: Bloomberg may be used for per-security characteristics (beta, duration, "etc"), and for the
  concentration pie charts they feed.
- The YCharts packet he supplied (the 2026-09-16 Comprehensive Overview sample, a client document held locally) is the
  SPECIFICATION: from it, list the data each component needs, then source each one.
- The report must be built from data Opal holds, or can foreseeably obtain. A component with no such source is not a
  standing "not available" placeholder.
- A Bloomberg draw of per-security information is a candidate source he names ("it could be"), not yet a ruling.

Prior ruling it touches:
- C-PRICES (IRPT_ANLREQ PRD) keeps Bloomberg OUT of the PRICE chain.
- His words here are about security INFORMATION (reference data), so this seat treats them as an extension to research,
  not a reversal.
- Research in progress: `RESEARCH_OPAL_REPORT_DATA_GAP_MAP_BLOOMBERG_20261020.md`.
