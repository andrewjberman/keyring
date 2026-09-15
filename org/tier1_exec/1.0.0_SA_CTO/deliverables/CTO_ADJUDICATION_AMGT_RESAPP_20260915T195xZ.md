# CTO ADJUDICATION -- AMGT_RESAPP, /self-drive tick 1 (2026-09-15 ~19:5xZ)

**Adjudicator:** `1.0.0_SA_CTO~W`, on Andrew-direct ~19:3xZ, verbatim in
`ANDREW_DIRECT_20260915_193xZ_GOALS_CTO_W_AND_COO_W_SEE_AMGT_RESAPP_THROUGH_SELF_DRIVE_ADJUDICATE.md` @`2ac5611057`: *"maintain a
/self-drive loop so if any open calls come up in the process, you adjudicate and keep the fabric moving toward that goal."*
**Scope:** AMGT_RESAPP (D5, site Z). **Inputs read:** `4.0.0_SA_CRO~W`'s findings brief @`7bad309f20` (the main source of this tick's
calls), this seat's open-call cards of ~15:xxZ, the round state (11 of 13 drained; rj-10 partial drain @`e0c93010af` and its amendment 5
@`4f0436811b`; rj-3 staged). **Mid-round freeze holds:** every ruling that changes the specification lands in the round-11 L10 addendum,
after the slug; none edits a live order.

```
OPEN CALLS -- AMGT_RESAPP -- 1.0.0_SA_CTO~W, /self-drive tick 1 (14 calls: 12 ADJUDICABLE ruled here, 2 RESERVED at Andrew)

ADJUDICABLE

+-- CALL 1 of 14 ----------------------------------------------------+
  **Which quantity is the Management tab's headline metric?**
  4.0.0_SA_CRO~W reads Andrew's metric as total time at the company; Bloomberg's 33/33 field is time in executive positions.
  --------------------------------------------------------------------
  **REC --** Headline = average time in executive positions at the company; time at the company in general and time in the current
  role are separate companion metrics. Andrew ~18:2xZ said "average exec management time with company" and asked for "average time at
  company as a manager + average time at company in general" as scoped measures (@3f9481ea12).
  --------------------------------------------------------------------
  **RULING --** (REC adopted) `exec_mgmt_tenure_avg_years` is the headline, served from Bloomberg `EXECUTIVE_AVERAGE_TENURE`;
  `exec_company_tenure_avg_years` and `exec_role_tenure_avg_years` are companions, each with its own metric id, roster coverage and date
  precision, ABSENT where the roster dates are not reached. Before the cut relies on it, confirm from Bloomberg's documentation that the
  field counts executive positions at THIS company only.
+---------------------------------------------------------------------+

+-- CALL 2 of 14 ----------------------------------------------------+
  **The authorized Lusha enrich: run it, or hold it?**
  CRO~W stopped under the brief's bound: no documented request excludes emails and phones, and the repo client drops an empty reveal list.
  --------------------------------------------------------------------
  **REC --** Hold the one call; keep the authorization. It runs only when Lusha's v3 API reference (not a tutorial) documents a request
  that returns positions without emails or phones, sent as that exact body.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) The authorization of ~19:0xZ stands unused. 4.0.0_SA_CRO~W reads the v3 API reference for
  `contacts/enrich`; the call is made only with a documented no-contact body, outside the shared client's empty-list drop; otherwise the
  companion metrics stay ABSENT-NOT_REACHED. No change to the shared FIND_INSURE client from this project.
+---------------------------------------------------------------------+

+-- CALL 3 of 14 ----------------------------------------------------+
  **Which dispersion stands in for FCF dispersion in Divergence, and in what form?**
  Andrew ~19:0xZ: "CFPS or EPS is fine." CRO~W measured both and two scalings.
  --------------------------------------------------------------------
  **REC --** CFPS first, EPS as a separately versioned fallback; relative scaling; fiscal-year form until contributor-level data supports NTM.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) s_proxy = |F_cons| * sd(CFPS) / |mean(CFPS)| at 1FY, ABSENT when |mean(CFPS)| is near zero or N(CFPS) < 4;
  where CFPS fails, EPS in the same form, and the score record carries `dispersion_proxy: CFPS | EPS` so a proxy change never reads as a
  changed view. No summing of annual standard deviations into an NTM figure; period ends come from `BEST_PERIOD_END_DATE`.
+---------------------------------------------------------------------+

+-- CALL 4 of 14 ----------------------------------------------------+
  **Divergence needs a house FCF forecast that does not exist. Add it to the endpoint?**
  Andrew ~18:3xZ ruled D with drivers "seeded at least partly independently" of consensus; the estate holds only reported history.
  --------------------------------------------------------------------
  **REC --** Yes: one new outcome for the house forecast; D stays ABSENT until it exists.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) The L10 addendum appends FWD-20: a forecast of FCF per company whose revenue, margin, tax, capex and working-
  capital drivers are seeded from dated filings and operating history, every assumption stored with its source and time, never copied
  from consensus. D is ABSENT with reason until FWD-20 serves; Andrew's sd(D) < 0.25 check runs before D is shown.
+---------------------------------------------------------------------+

+-- CALL 5 of 14 ----------------------------------------------------+
  **Robustness: how to count eligibility, and what to do with the thin inputs?**
  CRO~W showed this seat's 3/33 was a raw field count, not eligibility; x6 is carried (21/33 now); x3 used debt principal for obligations.
  --------------------------------------------------------------------
  **REC --** Correct the instrument; keep Andrew's model and its n >= 5 guard; show S ABSENT with reason where a name is ineligible.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Eligibility is computed only by a windowed instrument (the latest 8 TTM points built from `FUND_PER=Q`
  quarters, the domain guards applied). x6 = `SUPPLY_CHAIN_REVENUE_PERCENTAGE` at the latest point only, earlier points ABSENT, never
  carried back. x3 and x4 use year-1 plus year-2 debt principal, labelled "debt principal due within 24 months" until an obligations field
  is found, and only after the principal fields' documentation is reconciled. No model parameter changes here; a round-12 cell measures an
  annual variant and the eligible count, and a parameter change goes to Andrew only with that count in hand.
+---------------------------------------------------------------------+

+-- CALL 6 of 14 ----------------------------------------------------+
  **Which population does the displayed percentile rank within?**
  Andrew ~17:5xZ: "percentile is relative to the pool of analyzed companies"; the three models write "| sector".
  --------------------------------------------------------------------
  **REC --** Display the whole analyzed-pool percentile; add a labelled sector percentile only where a sector holds enough names.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) P = percentile within the analyzed pool: companies deduplicated by company FIGI, eligible for the metric
  version, one as-of cut, ABSENT below 5. A second figure labelled "sector" is served only where that sector holds at least 5 eligible
  names; the two are never mixed. The pool is analyzed companies, not every `peers/v1` object.
+---------------------------------------------------------------------+

+-- CALL 7 of 14 ----------------------------------------------------+
  **Peers V: what changes beyond the cap Andrew ruled?**
  CRO~W found three contract-fidelity gaps in the measures and traced all 23 empty peer sets to missing subject metadata.
  --------------------------------------------------------------------
  **REC --** Fix the three measure gaps and repair the 23 subjects' identity and headers in round 12.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Measures: a missing dividend or buyback component makes measure 3 ABSENT, never zero; the EBITDA guard
  reads the same period as the measure; NTM EPS growth is its own input (forward EPS against trailing EPS, one currency and share basis),
  not derived from P/E ratios. Members resolve by company FIGI to an exchange-coded security before any read. A round-12 cell repairs the
  subject header and identity for the 23 EMPTY sets without loosening the peer rules.
+---------------------------------------------------------------------+

+-- CALL 8 of 14 ----------------------------------------------------+
  **4.0.0_SA_CRO~W cannot send: its launcher heartbeat fails. Who restores it?**
  Measured by that seat: PermissionError replacing org/mcp/liveness.json; codex-send refuses on absent liveness.
  --------------------------------------------------------------------
  **REC --** 0.0.0_AB_MSTR~Z (seating and runtime) restores the launcher registration; this lane reads that seat's commits meanwhile.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Routed to 0.0.0_AB_MSTR~Z. Until restored, 4.0.0_SA_CRO~W's committed files are its carrier and this lane
  watches them; no alternate heartbeat helper.
+---------------------------------------------------------------------+

+-- CALL 9 of 14 ----------------------------------------------------+
  **ADR or home listing for a company in the pool?**
  Open since ~15:xxZ; BABA carries both an ADR and a Hong Kong line with one company FIGI.
  --------------------------------------------------------------------
  **REC --** One company, deduplicated by company FIGI; the page shows the listing the analyst opened.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Ranking, percentiles and peer sets count a company once by company FIGI; the page renders the listing it was
  opened on, and the other listing is named beside it.
+---------------------------------------------------------------------+

+-- CALL 10 of 14 ---------------------------------------------------+
  **Filings text from EDGAR, numbers from Bloomberg?**
  Open since ~15:xxZ; Andrew ruled Bloomberg for the Robustness inputs only.
  --------------------------------------------------------------------
  **REC --** The filings analyzer reads the filings' text; every score input is a Bloomberg number.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Filing text (EDGAR, or the company's own site for a 20-F or home-market filer) feeds the Thesis and
  Management prose and the officer roster; the four scores read Bloomberg, with Lusha only where call 2 allows it.
+---------------------------------------------------------------------+

+-- CALL 11 of 14 ---------------------------------------------------+
  **Throttle the ~W fabric against the weekly model limit?**
  Open since ~15:xxZ; no measured shortfall this session.
  --------------------------------------------------------------------
  **REC --** No pre-emptive throttle; the issuer's stated fan-out stands; a limit hit is logged with its reset time.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) No throttle. On a 429 the affected seat writes the reset time into its log, heartbeat and final message, and
  this loop carries the stalled step to the next tick.
+---------------------------------------------------------------------+

+-- CALL 12 of 14 ---------------------------------------------------+
  **Who exercises the outcomes that name Adam (FWD-5, FWD-7), and when?**
  Their DONE WHEN is an exercise by a person, which no seat can perform.
  --------------------------------------------------------------------
  **REC --** Ask Andrew to schedule Adam's exercise once the round-12 page serves on the drain ref; until then those outcomes stay open.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) Carried; this lane puts the scheduling question to Andrew when the page is exercisable. If the close is
  otherwise reached first, the goal reads HELD-AT-STOP on these two outcomes.
+---------------------------------------------------------------------+

RESERVED (cards at Andrew; citation on each card)

+-- CALL 13 of 14 ---------------------------------------------------+
  **Promote the Security Analysis page to production?**
  Citation: project.json `blocking` (1), "PORTAL FROZEN both fabrics -- COMMIT YES / PROMOTE NO until Andrew names it".
  --------------------------------------------------------------------
  **REC --** Not yet: promote after round 12 serves the tab scores and Adam's exercise passes, as one named promote.
+---------------------------------------------------------------------+

+-- CALL 14 of 14 ---------------------------------------------------+
  **Activate recurring harvest collection for the pool?**
  Citation: PRD `AMGT_RESAPP_PRD.md:831`, "the collection MECHANISM and CADENCE stay RESERVED to Andrew".
  --------------------------------------------------------------------
  **REC --** Yes, daily on the existing session harvesters once the page is promoted; the pool holds 2 links for BA today.
+---------------------------------------------------------------------+

STRUCK: the rj-9 split card of ~15:xxZ (rj-9 drained and closed @5ae785828e; nothing left to decide).
```

## Acts this tick

Verdict ledger `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/ctoW_AMGT_RESAPP/VERDICTS.jsonl` (12 rows), tick log, one broadcast to
`2.0.0_SA_COO~W`, `3.0.0_SA_CVO~W`, `4.0.0_SA_CRO~W`, `0.0.0_AB_MSTR~Z`. Specification changes wait for the L10 addendum. Push state: LOCAL.
