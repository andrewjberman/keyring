# BRIEF (midstream) -- IRPT_ANLREQ report engine: Comparison and Multi-Comp on Opal's own math, Core first, then full parity

Author: `4.0.0_SA_CRO~TCKT` (dell2), 2026-10-20.
Mode: `--midstream`.
Consumer: `1.0.0_SA_CTO~DELL2`, `/endpoint --forward`, as a PRD addendum to
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (v0.24). FWD-7 already holds the price chain; this brief adds
what the report must SHOW.

Authority (verbatim records, in `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/`):
- `ANDREW_DIRECT_20261020_14xxZ_TCKT_WALKTHROUGH_VOICE_MEMO.md` @9de85135f0: "this is actually the largest issue".
- `ANDREW_DIRECT_20261020_15xxZ_TCKT_SYNTHESIS_ANSWERS.md` @f2581e90b9, quoted:
  - "We can start with Core to get a functioning chart out, but as soon as we get that done, the build for the full
    parity version should get started";
  - "the agent-built one on October 3 is likely fine, I just need to see that export in a sample run to gauge whether it
    looks correct and has the right information";
  - "the more important part is that we have the sample y charts output so you can see what they provide".

Reference output: the 2026-09-16 YCharts Comprehensive Overview (No Benchmark) sample Andrew supplied. It is held
locally and not committed. This seat's page inventory of it is local only, because it holds client values.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

**Not read:**
- IRPT_ANLREQ task-order files, decompositions, `phase` and `blocking` fields.

**Read:**
- the PRD's FWD-7 and C-PRICES;
- the IRPT_YCDGEN element maps;
- the 2026-10-05 feasibility brief;
- the 2026-09-30 endpoint census;
- the producer source at `origin/CLOUD`;
- the YCharts sample;
- one live run record from 2026-10-17 (REQ-d6231c013ae90519c67d18e9).

**Where it bent:**
- This seat's prior-art read used `git log` on `ycharts/research/`, so cell ids reached it as provenance. AR-g-163,
  AR-g-164 and AR-g-165 add OWN_SERIES elements to the Overview map.
- The run record's numbers come from earlier session reads, not from this brief's own read.

**"Unchanged" finding:**
- FWD-7 (Opal data, Yahoo then YCharts per symbol for prices only) does not move.
- What moves is the report's CONTENT for variants 2 and 3, which no outcome names today.
- The failure is in scope, not direction: the comparison and multi maps were never re-pointed to Opal math.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread.** An Opal staff user files a Multi-Comp on DEV:
- one firm, one holdings file;
- two Opal models plus one ETF as comparables;
- the request then opens a report PDF on the ticket.

The thread's first visible proof is ONE comparison chart: the portfolio's cumulative return beside each comparable's,
over one common window, on the Opal-branded page.

### O1 -- Andrew judges the Opal Overview on a sample run before anything else changes
- An Opal person files an Overview (no comparables) and opens the Opal-generated PDF from the ticket.
- Andrew reads it beside the YCharts Overview sample.
- He says whether the Opal Overview "looks correct and has the right information".
- His verdict decides what, if anything, Core and Parity must fix on the Overview pages too.
- This is the gate on the generator's base, not a build.

### O2 (CORE, first) -- A person reads how the portfolio did against each comparable
On the comparison pages of a Comparison or Multi-Comp report, every comparable the filer picked (an Opal model or an ETF)
shows, beside the portfolio:

| What | Content |
|---|---|
| Cumulative return chart | One line per comparable plus the portfolio, over a common window |
| Periodic total returns | The windows the YCharts report uses |
| Risk figures | Standard deviation, Sharpe, Sortino, drawdown, alpha and beta, each against the stated reference |
| Asset allocation | Side by side |

Every figure is computed by Opal from prices and held data. None is a vendor-computed figure.

### O3 (PARITY, starts as soon as O2 is done) -- A person finds every kind of information the YCharts comparison and multi reports carry
For the portfolio and each comparable:
- region and country exposure;
- stock style and market cap;
- sector exposure;
- bond sector, credit quality and maturity;
- fundamentals (yield, expense, PE, P/S, P/B, ROE, ROA, market cap, D/C; bond yield, duration, coupon, credit, price);
- the risk/reward scatter;
- standardized returns;
- the holdings tables.

In all, the full component set of `comparison_map.json` and `multi_map.json`.

### O4 -- A component Opal cannot fill says so, in words, on the page
- A component with no Opal source shows a plain "not available for <comparable>: <reason>" line. It is never left blank
  or hidden.
- The report stays a report: no audit-trace cards in the PDF.
- The internal trace belongs to the audit record (the separate brief's audit JSON), not to the reader.

## PART II -- WHERE THE BOUNDARY SITS

**Owner:** IRPT_ANLREQ's engine workstream (`~G2`, C-ABSORB b) owns:
- `ycharts/research/opal_producer.py`, `layout_overview.py`, the comparison and multi maps' re-pointing;
- the comparable-side computation.

**Relied on, not owned:**
- IRPT_DASHBD's daily TWR engine. C-PRICES says variants 2 and 3 overlays use it "ported with zero flows" for the Opal
  models. IRPT_DASHBD owns the engine; this project owns the port.
- The price chain, FWD-7 / C-PRICES (unchanged).
- The held-data tables: the Bloomberg characteristics parquet and `etf-classifications`, plus MDPF_SECHIST.

**Prior art, not a live project:** IRPT_YCDGEN's maps, endpoint census and `map_pdf.py` parser.

**Out of scope:**
- the Ticket Center form;
- the attachments;
- the audit record (separate items in the same project);
- the commentary (FWD-3), except that it reads this report.

## PART III -- THE QUALITATIVE BAR

- A person reading the Opal Overview beside the YCharts Overview sample finds the same kinds of information in each
  section. This is graded by Andrew (O1).
- A person reading an Opal Multi-Comp can answer "did this portfolio beat each model I picked, and with how much risk"
  without opening YCharts.
- No page of a Comparison or Multi-Comp report reads "Not available in this version" for a figure Opal can compute from
  prices it already holds.

## PART IV -- THE SUBSTRATE (findings, measured at `origin/CLOUD` 2026-10-20)

**F1. The three maps exist** (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/`, made by `map_pdf.py` @fcd1393acf):

| Map | Pages | Elements | Composition |
|---|---|---|---|
| Overview | 23 | 254 | 156 OPAL_HELD, 26 OWN_SERIES, 65 builder-only, 7 vendor-call |
| Comparison | 32 | 574 | 223 builder-only, 351 vendor-call, 0 re-pointed |
| Multi | 34 | 424 | 280 builder-only, 144 vendor-call, 0 re-pointed |

**F2. The vendor-call elements of the two unported maps, by call (Core / Parity split):**

| Map | Core calls (level_series, returns, risk_stats, key_stats, allocation, net_allocation, standardized_returns, scatter, info), portfolio + comparison | Parity calls (region, equity, bond exposure, fundamentals), portfolio + comparison |
|---|---|---|
| Comparison | 60 | 291 |
| Multi | 61 | 83 |

The two columns sum to each map's vendor-call count (351 and 144).

**F3. Today's producer.** It drops every vendor call (`opal_producer._opal_map`). On a Multi-Comp it fills only the
classified holdings and allocation tables and the price table. Run REQ-d6231c013ae90519c67d18e9 (2026-10-17) had 427
elements with 3 values.

**F4. The comparable-side TWR port named in C-PRICES has not been built.** No commit in `ycharts/research/` carries it
(prior-art read).

**F5. Alyssa's branded script is not in the repo.** Andrew ruled it unneeded. The base is the agent-built generator
(`layout_overview.py` @a567954d10 plus `render_pdf.cjs`, 2026-10-03).

**F6. The YCharts Overview sample** (21 pages) carries these sections:
- cumulative return and basic info, periodic and annual returns, key stats;
- asset allocation, market cap, style, region and country, stock and bond sector, credit, maturity;
- drawdown, risk info, risk/reward scatter, fundamentals;
- top, all and top-25 holdings, standardized returns;
- disclosures and definitions.

Each section has a counterpart group in the Overview map. The map has 2 more pages than the sample: it was made from a
different sample.

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- Held data for each comparable ETF and each Opal model is reachable by symbol: exposures, fundamentals, allocation.
  For the Opal models that means their holdings as of the window.
- A model's return series exists for the comparison window. That is the TWR port, or a held model series.
- The common window and its rule (first common date, or each comparable's own inception) are stated in the report.
- Any new S3 address or name for intermediate series is LGIC builder output (rule 30).

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-20:
- The submission-guard fix is on portal PROD (4546cee0, 10:16 ET).
- Run 7 (the PROD page filing, four attachments) was GO'd at 14:31Z and had not reported when this was written.
- No Opal Overview PDF from a 2026-10-20 run has been opened by Andrew.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not open any Opal-generated PDF; Overview quality is O1's question.
- It did not check that the held-data tables cover every comparable ETF or Opal model.
- The Core / Parity split in F2 is this seat's grouping by call name; the CTO may regroup it.
- It names no deadline, no element-count target and no new store.

## REFS

```
  BRIEF PATH        docs/briefs/irpt-anlreq-report-engine-core-then-parity-brief-20261020.md
  PROJECT           IRPT_ANLREQ (D9/IRPT, fabric dell2)
  EXISTING PRD      org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md (v0.24)
  SIBLING PROJECTS  IRPT_DASHBD (TWR engine), IRPT_YCDGEN (maps, prior art), MDPF_SECHIST (prices)
  PRIOR ART         maps/{overview,comparison,multi}_map.json; docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md;
                    org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/YCHARTS_GENERATION_ENDPOINT_CENSUS_20260930.md;
                    ycharts/research/{map_pdf,opal_producer,layout_overview}.py
  MEASURED AT       2026-10-20 ~15:0xZ (maps and producer at origin/CLOUD; sample read locally)
```
