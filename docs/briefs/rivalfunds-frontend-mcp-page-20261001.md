# BRIEF -- rivalfunds FRONTEND: the MCP landing page as a presentation (midstream, ETFS_RIVALS)

**Author:** `4.0.0_SA_CRO~RV`, 2026-10-01. **Mode:** `/brief-create --midstream`.
**Andrew-direct:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261001_194xZ_RIVALFUNDS_NEXT_CHALLENGES_TWO_BRIEFS.md`
(the directive plus both dictated transcripts, verbatim).
**Sibling brief (backend):** `docs/briefs/rivalfunds-backend-data-ai-synthesis-20261001.md`. It owns every number and
every AI paragraph this page shows.
**Consumer:** `1.0.0_SA_CTO~Z`, `/endpoint --forward` at L2.

---

## PART 0 -- How the blind constraint was honoured, and WHERE IT BENT

- **Read, admissible:**
  - the PRD v0.7 (C-SERVING, C-GUARDRAILS);
  - the served page of 2026-10-01 (manifest and HTML);
  - the page renderer's read-back rules;
  - the portal components Andrew named.
- **Where it bent:** in the same session I read the round-4 decomposition and task-order statuses for the `/closer`
  trace. The page work in that branch is guardrail floors and revision picks. None of it is an outcome here.
- **Leak risk:** O5, the audit material leaving the reading path, sits near the existing "Data status" and trace panels.
  It is phrased as what Andrew reads first, not as a change to those panels.

**Finding: this is a NEW direction for the page, not a sharpening.** PRD FWD-1 makes the page a trace from a trade back
to the issuer bytes, and the page does that today, which is why Andrew reads it as "an audit log ... scrolling from
miles". The transcript makes the landing view a three-component presentation and keeps the trace reachable underneath.
The PRD's FWD-1 should be re-read at L2 against this.

---

## PART I -- THE OUTCOME TERRITORY

### O1 -- THE CANDIDATE THREAD: Andrew opens the page and reads IDVZ's best and worst this month, then this quarter and this year

**Who and journey:** Andrew opens `/rivalfunds` and lands on one wide ranking component, set to IDVZ. It shows the ten
best and ten worst securities and the five best and five worst sectors for month-to-date. He toggles to quarter-to-date,
then year-to-date, and the tables change.

**Coarse grain:** one fund (IDVZ), three windows, no other component. It crosses the served ranking artifact, the
toggle and the rendered table once.

Source: transcript 2, component 1 ("it should maybe default to IDVZ"; "toggle MTD, QTD, YTD, and see those tables
change"; "in order ... month to date, quarter to date, year to date").

### O2 -- Andrew switches the ranking to any fund in either group, the benchmark included

A dropdown lists IDVZ, every IDVZ peer and its benchmark (ACWI), and likewise PFOE, its peers and its benchmark (IWM,
the Russell 2000). Choosing one shows that fund's ranking under the same toggles.

Source: transcript 2 ("a little dropdown that has IDVZ and all of the IDVZ comparisons, including the benchmark. And
the same for PFOE, where we have their Russell 2000 IWM benchmark").

### O3 -- Andrew reads each fund's buying trend for the year in one plain table

Component 2 is a naive year-to-date trend of buying activity. It has the same shape as component 1: ten best and ten
worst securities, five best and five worst sectors. It has no toggles, and it reads as a simple table with an intuitive
trend line.

Source: transcript 2, component 2 ("a very simple table"; "year-to-date is enough for this ... There's no toggles").

### O4 -- Andrew reads the AI's two-part account of each fund, rivals and Opal funds, never the benchmark

Component 3 holds, per fund:
- the recent-activity account: the rolling 30 days, the unusual, the big wins and losses;
- the direction verdict: corroborate, refute or enrich the trend, and what the AI expects.

Each paragraph shows where its figures came from and when its inputs were taken. The benchmark has no AI section.

Source: transcript 2, component 3 ("We do not need to apply any analysis to the benchmark"); the two prompts.

### O5 -- The page reads as a presentation: the three components first, the audit material out of the way

Andrew reads the three components without scrolling past trade-by-trade trace panels, holdings dumps or check tables.
The trace and the data status stay reachable, and the dated archive stays.

Source: transcript 1 ("more of an audit log than a presentation"; "the user is scrolling from miles"); transcript 2
("how the presentation works by just coming down very simply from these views"); PRD C-SERVING (archive by day).

### O6 -- It looks like Opal's portal because it reuses what the portal already has

The ranking layout uses the portal's existing card pattern, "the philosophy fixture cards" (the shared graphic-card
pattern), and the existing period-toggle logic. No new widget family is invented. The page follows the portal's design
contract.

Source: transcript 2 ("You should not be reinventing the wheel. We have all of the toggle logic. We have all of the
components ... rely on the philosophy fixture cards").

### O7 -- A component with missing or failed data says so, in place

If a fund's ranking, trend or AI section could not be built or failed its checks, that component says what is missing.
It never shows a quietly empty or quietly wrong table.

Source: PRD FWD-9 and C-GUARDRAILS (carried; the transcript does not restate it).

---

## PART II -- WHERE THE BOUNDARY SITS

- **This brief owns:**
  - the layout of `mcp.opalinvest.dev/rivalfunds` and its archive pages: the three components, the toggles, the fund
    selector and the default;
  - placing the trace and data-status material out of the reading path;
  - how a missing input reads on screen.
- **The backend brief owns** every value and every AI paragraph, the windows' computation, and the served artifact
  this page renders. The seam is that artifact.
- **Relied on, not owned:**
  - the gateway's `/rivalfunds` routes (`infra/aws/ec2/opal-gateway/app/rivalfunds_view.py`), which serve the page
    byte for byte behind sign-in;
  - the portal's design contract (`portal/DESIGN.md`, `design/systems/portal/DESIGN_SYSTEM.md`);
  - the portal components named in Part IV.
- **Not this brief:** a dashboard. Andrew: "There's no dashboard function yet." No portal route is created here unless
  the Part IV tension is settled that way.

## PART III -- THE QUALITATIVE BAR

- Andrew answers "where has this manager been winning and losing this quarter" from the first screen, without
  scrolling.
- Switching the window or the fund changes the tables and nothing else. A table never shows another window's figures
  under the new label.
- Someone used to the portal reads the page as part of it: the same cards, the same toggle behaviour and the same
  light canvas.
- An empty or failed component is distinguishable at a glance from a component reporting "no notable activity".

## PART IV -- THE SUBSTRATE (findings, each with what was measured)

1. **The page is static HTML that forbids scripts.**
   - `data/etfs/scripts/rivalfunds/render.py` writes one self-contained HTML file per day. The gateway serves it
     unchanged (`rivalfunds_view.py`, CSP `frame-ancestors 'self'`).
   - The renderer's read-back REFUSES a page containing `<script`, `<link`, ` src=`, `@import` or `url(`
     (`render.py:391`, `:412`).
   - The 2026-10-01 page has 0 `<script` tags.
   - **So MTD/QTD/YTD toggles and a fund dropdown cannot be the portal's React components dropped in.** They must be
     one of:
     - (a) script-free, with every window and fund pre-rendered and switched by CSS (radio inputs with `:checked`);
     - (b) the read-back rule relaxed to admit one inline script, a decision for the CTO;
     - (c) rendered by the portal instead of the MCP page, which Andrew's "no dashboard function yet" argues against.

     This brief names the tension and does not choose.
2. **Why it reads as an audit log, measured on the served page.**
   - 2026-10-01 `index.html` is 903,331 bytes.
   - Its three sections are "Most recent trades, by Opal fund", "Latest holdings by fund" and "Data status".
   - Every trade carries its own `<details class="trace">` panel, capped at 200 trade rows per fund (provisional
     threshold), and per-fund check tables and holdings dumps follow.
3. **"The philosophy fixture cards" are a portal React pattern.**
   - `portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx` uses the shared
     `ui/components/graphic/GraphicCard` and `HeroGraphic` (eyebrow, navy graphic panel with an indigo top rule, title,
     tagline, "Read more").
   - Model Portfolios wears the same pattern.
   - In a static page it can be reused as anatomy and tokens, not as code (see finding 1).
4. **The period toggles exist, but not as one three-way MTD/QTD/YTD control.**
   - `portal/src/components/BenchmarkHeatmap.tsx` carries `1D, WTD, TTW, MTD, 1M, QTD, 1Q, YTD, 1Y, SI`.
   - `Attribution/components/StylePolicyComparison.tsx` toggles `QTD, YTD, 1Y, SI`.
   - InvestorReporting's `period.ts` presets are `YTD, 1Y, 3Y, SI`.
   - `api/endpoints/market.ts` types `WTD|MTD|QTD|YTD|...`.
   - The closest existing toggle to Andrew's is BenchmarkHeatmap's period set.
5. **The design law is the portal's light canvas.** `portal/CLAUDE.md` and `DESIGN.md` C3 set the canvas to `#F4F6FA`,
   white panels with a hairline, and navy ink, with light text illegal on canvas and panels. Whether the current MCP
   page follows it is unmeasured.
6. **The archive and dated pages already work by route:** `/rivalfunds`, `/rivalfunds/archive` and `/rivalfunds/{day}`
   (`server.py:997-1001`), with a `revisions/` trail per day. The new layout keeps this; nothing in the transcript
   removes it.

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The backend brief's O2 (rankings for MTD/QTD/YTD for every fund), O3 (YTD trends), O4 (style read) and O5/O6 (AI
  sections) exist as served artifacts. This page has nothing to show until they do.
- The Part IV finding 1 tension is settled (script-free CSS toggles, one permitted script, or a portal route) before
  the toggles are built.
- The benchmark instruments are confirmed: ACWI for IDVZ, and IWM for PFOE, as Andrew named it in transcript 2.
- The page's checks (C-GUARDRAILS) are re-pointed at the new components, so a failed component still marks itself
  (O7).
- Verification by looking, per the portal law: a rendered screenshot read against `DESIGN.md` (`/frontend-dev` or the
  `/ui-walk` path for the MCP page), and Andrew's signed-in read as the live thread.

## PART VI -- STATUS, MARKED NOT OUTCOME-BEARING

**NOT OUTCOME-BEARING. Measured 2026-10-01 between 17:30Z and 20:05Z; it ages.**
- The 2026-10-01 page is published: 12 of 13 funds, 903,331 bytes, 0 scripts, three sections.
- No ranking, trend or AI component exists, because the backend tables do not (backend brief Part IV, finding 1).
- No signed-in read of the page is on record.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **The fund selector's grain.** Transcript 2 says both "you can select by fund ... default to IDVZ" and "choose if we
  want to look at IDVZ and their competitors/benchmark or PFOE and their competitors/benchmark". One fund at a time, or
  one group at a time, is left to L2 or Andrew.
- **What the ranking ranks** (trade outcome, holding return or contribution) is open in the backend brief, Part VII.
  The column labels follow that answer.
- **The "intuitive trend line" form** for component 2 (a sparkline, an arrow, a slope figure) is not specified. Andrew
  asked for "a very simple table".
- **Not measured:** the MCP page's conformance to `DESIGN.md`; how the page renders at phone width.
- **No layout drawing, pixel sizes or component code.** Those belong to the PRD and the decomposition.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/rivalfunds-frontend-mcp-page-20261001.md
  PROJECT           ETFS_RIVALS (D5/ETFS); workstream registration is the CTO's call
  EXISTING PRD      org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.7; FWD-1, FWD-9, C-SERVING, C-GUARDRAILS)
  SIBLING BRIEF     docs/briefs/rivalfunds-backend-data-ai-synthesis-20261001.md
  SIBLING PROJECTS  the opal-gateway (route owner), the portal design system (DSGN_REBRND lineage)
  PRIOR ART         data/etfs/scripts/rivalfunds/render.py, publish_page.py; infra/aws/ec2/opal-gateway/app/rivalfunds_view.py;
                    portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx;
                    portal/src/ui/components/graphic/{GraphicCard,HeroGraphic}.tsx;
                    portal/src/components/BenchmarkHeatmap.tsx (period set); portal/DESIGN.md;
                    trace org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_END_TO_END_GAP_BRIEF_20261001.md @381bec5549
  MEASURED AT       2026-10-01 17:30Z-20:05Z (Part VI)
```
