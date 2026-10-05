# IRPT_YCDGEN brief addendum A -- DRAFT, handed to 4.0.0_SA_CRO (base)

Andrew-direct 2026-10-05, at the 4.0.0_SA_CRO~2026 terminal, VERBATIM: "The YCharts insourcing solution I want handled
by CRO Base, so they can focus on that exclusively. Regarding "whether opal has the right to show each data source", if
we own the process off our data from our licensed vendors (e.g. BBG), then this question is moot."

- Owner from here: `4.0.0_SA_CRO` (base), exclusively. 4.0.0_SA_CRO~2026 wound down the same session (Andrew-direct
  "wind down this device"); this file is its partial draft, offered as input, not as a finished section.
- The ask: `1.0.0_SA_CTO` msg 105308 to 4.0.0_SA_CRO~2026 -- a short L1 brief addendum for IRPT_YCDGEN on Andrew's
  insourcing order (record
  `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/ANDREW_DIRECT_20261005T143xZ_INSOURCE_YCHARTS_GENERATION.md`
  @a812d50ff1), covering past patterns where Opal replaced a vendor computation, what to keep from YCharts and what to
  rebuild, and the risks; input is `2.0.0_SA_COO~Y`'s assessment (not received by ~2026). 4.0.0_SA_CRO~2026 had replied
  that it takes it (msg to the CTO 2026-10-05 15:11Z); Andrew has since reassigned it to the base seat. The CTO has NOT
  been told of the reassignment (Andrew: "no need to broadcast").
- Base brief: `docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md` (4.0.0_SA_CRO, 2026-10-03).

## A. Precedents: where Opal already replaced a vendor's computation (from the registry and git)

| When | What Opal replaced | What it kept from the vendor | What happened | Lesson for YCharts |
|---|---|---|---|---|
| 2026-06-19 to 06-25 | Black Diamond browser scrape -> Black Diamond DataMining REST API (ADVI_BDAPIMIG) | the vendor, via a documented API | Email-code MFA on the vendor's site froze 49 Financial's data for 6 days, silently | A session-based vendor path is an outage source; detect staleness and prefer documented interfaces |
| 2026-06-23 | Feasibility to replace Black Diamond and Orion with an Opal-owned custodian-data layer (DATA_PLATFORM) | -- | Closed in the 2026-08-25 registry clean-up, which records that it is not a work verdict | The insourcing thesis already exists; this is its next instance |
| 2026-06-29 to 08-19 | 49 Financial moved off Black Diamond onto Schwab as source of record (DATA_SSOTMG); first scheduled Schwab runs 07-14; Schwab-based Advisor Intelligence 08-19 | Black Diamond as a comparison only | Opal reads the custodian directly; the middle tier no longer sets the numbers | Go to the primary source; keep the vendor as a check, not a dependency |
| 2026-08-24 to 10-03 | 49 Financial performance computed by Opal (ADVI_PERFRP, then IRPT): total return before advisory fees, GIPS-aligned; live 10-03 | Black Diamond's own figures, compared by the parity harness (ADVI_BDPARITY: EXACT / EXACT-SHIFTED / TIGHT / LARGE / MIX, each with a named mechanism) | Every 49 Financial account published on Opal's method, with print, export and download | Rebuild the calculation, publish the method, and measure every figure against the vendor's with a named reason for each difference (outcome O6 of the base brief) |
| 2026-10-01 | Cottonwood historical performance from Opal's legacy-model figures while Black Diamond's history conversion slipped to late December or January | -- | Opal supplied the figures for client meetings in the meantime (email, Alongside and Opal) | Owning the calculation takes the vendor's timeline out of client meetings |

## B. Keep from YCharts, rebuild in Opal -- NOT WRITTEN (needs ~Y's cross-reference)

Working hypothesis only, to be tested against the assessment: rebuild the report document (layout, Opal branding; F4
of the base brief), every statistic that is a function of a price or return series Opal holds, and every
holdings-derived element (Opal's own holdings, per firm); source series from Opal's licensed vendors (for example
Bloomberg) so YCharts dependencies go toward zero.

## C. Dependencies toward zero -- NOT WRITTEN (needs ~Y's assessment)

## D. Risks (draft)

- Data rights: RULED MOOT by Andrew (above) where the process runs off Opal's data from its licensed vendors. Not a
  risk entry.
- Convention drift: returns, annualisation and benchmark conventions will differ from YCharts' in places; the base
  brief's O6 side-by-side names each difference before a client sees it.
- Unmapped elements: anything computed only inside YCharts' generation (scores, ratings) is rebuilt from data Opal holds
  or plainly absent, never imitated (base brief, bar 5).
- Residual session fragility: while any YCharts call remains, the shared session and its WAF tolerance still bound run
  time and reliability.
- Ownership cost: an in-house generator is code Opal maintains; the served YCharts path keeps running until Opal's
  matches it.
