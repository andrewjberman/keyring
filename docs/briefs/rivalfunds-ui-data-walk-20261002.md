# /rivalfunds -- the UI and data walk of 2026-10-02: what the page still gets wrong (ETFS_RIVALS, midstream brief)

**Author:** `4.0.0_SA_CRO~RV`, 2026-10-02. **Mode:** `/brief-create --midstream ETFS_RIVALS`. **For:** `1.0.0_SA_CTO~Z` (L2-L4), then `2.0.0_SA_COO~RV`.

**Andrew-direct, verbatim** (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_141xZ_RIVALFUNDS_UI_WALK_BRIEF_TO_CTO_COO_RV_CANONICAL_DRIVE.md`): *"I want you to walk the mcp.opalinvest.dev/rivalfunds via /ui-walk mechanism and find issues unrectified on two sides 1.) The UI, where is it too wordy and not properly using progressive disclosure, modals, and other in-pattern fixtures? 2.) Where is data not arriving and where is data missing (anything "unclassified, stale, missing, etc). Then i want you to write a brief for listing out each issue, send to CTO with instruction that issue list must be included in their PRD and fold it into COO~RVs existing work on ETFS_RIVALS."*

**The issue list is the register** `docs/briefs/rivalfunds-ui-data-findings-20261002.json`: 33 findings, 14 data (`RFW-D01`..`RFW-D14`) and 19 UI (`RFW-U01`..`RFW-U19`). The tables below are generated from it. **Andrew's instruction: every id is included in the ETFS_RIVALS PRD** and folded into `2.0.0_SA_COO~RV`'s existing work. Coverage check: `python docs/briefs/irpt-ui-review-coverage-check.py --register docs/briefs/rivalfunds-ui-data-findings-20261002.json <PRD>` exits 0 only when every id is cited.

## PART 0 -- How the blind constraint was honoured, and where it bent

- **Honoured:** the findings come from the SERVED page only. They come from the platinum bytes of 2026-10-02, their manifest and S3 object metadata, walked and screenshotted. No task order was read to produce or rank a finding.
- **Where it bent, and badly:** this seat adjudicated CALLs 1-12 on ETFS_RIVALS today (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`). It knows the open round-6 cells (ROUND_ANALYSIS.round5.md section 4). Five findings are marked `known` against those cells (RFW-D04, D08, D12, D13), and the acceptance lines of several echo rulings this seat made (RFW-U09 and CALL 6/A1 ruling 5's stored names; RFW-U16 and CALL 9). The leak is where a ratifying outcome could enter. The guard is that every outcome below is written from what a reader of the page sees, not from what a cell builds.
- **Unchanged:** the endpoint does not move. FWD-1..20 stand, and every finding maps to an existing FWD. The page fails its own FWD-18 ('a presentation, not an audit log'), FWD-19 ('looks and behaves like the Opal portal') and FWD-20 (inputs dated and counted) on the served bytes. That is a DECOMPOSITION and EXECUTION gap, not a DIRECTION gap.

## PART I -- THE OUTCOME TERRITORY

Each outcome is something Andrew can do on the served page. The candidate thread is O1: one person (Andrew), one fund (BASG, the demo fund), the default window, on the morning after a trading day.

### O1 -- THE THREAD -- Andrew opens /rivalfunds the morning after a trading day, picks BASG, and every figure on the opening view is current to that trading day and agrees with every other figure on the page

The rankings, the trend, the input census and the 'funds current' headline read the same holdings vintage. The opening period shows ranked holdings, not empty tables.

Findings: `RFW-D01`, `RFW-D02`, `RFW-D03`, `RFW-D07`, `RFW-U02`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D01 | pipeline: A1 producers vs page publish | The 2026-10-02 page (republished 14:17:10Z, batch fast-a1-publish-1002f) serves A1 tables built at 11:03-11:04Z. That was BEFORE the G1 refresh at 11:11Z, which added the 2026-10-01 reports of 7 funds (ETFT, INEQ, PCLG, PFOE, TSEL, TXUE, WCMG), and before G4 date=2026-10-01 landed at 11:10Z. The manifest's a1_produced reads SKIPPED for holding_contribution, buying_trend and input_census: '1 object(s) already at date=2026-10-02'. | When a G1 or G4 object newer than an A1 table's newest input lands, the next publish rebuilds that A1 table, or refuses to show it as current. A planted newer G1 object forces the rebuild. | new |
| RFW-D02 | page header vs input census | The page contradicts itself. The header reads '13 of 13 funds current' (twice), while 'Inputs that did not arrive' reads 'Fund holdings files: 2 of 13 arrived, 11 missing or stale' and lists TXUE, PFOE, WCMG and others as 'no G1 report dated 2026-10-01'. The publish-time freshness check reads those same funds' latest report as 2026-10-01 (lag 0). | On one page the fund-current headline and the census's holdings line agree (same G1 vintage), or the page names the vintage gap. | new |
| RFW-D03 | What drove the return, MTD and QTD | Month to date and quarter to date rank 0 holdings for 12 of 13 funds (every fund but BASG, which ranks 32). Each shows four empty tables ('No holding added to the return'). The page OPENS on Month to date. | After RFW-D01 lands, MTD ranks at least one holding for every fund whose 09-30 and 10-01 reports are both in G1; a fund-period with no priced day shows ONE line, not four empty tables (RFW-U03). | new |
| RFW-D07 | holdings arrival, 2026-10-01 reports | At the 14:17Z publish, 4 funds' latest report is 2026-09-30 against an expected 2026-10-01: IDVZ (home producer), BIDD, CGIC and SCHY (Bloomberg). The page dated 2026-10-02 shows them at T-2 and still calls them current under the 1-trading-day allowance (PROVISIONAL). | By the 09:00 ET sweep, every fund's report for the prior trading day is in G1, or the page names the fund as late with its reason. | new |
| RFW-U02 | period switch default | The page opens on Month to date, which is empty for 12 of 13 funds (RFW-D03). The first thing a reader sees is four empty tables. | The default period is the shortest one that ranks at least one holding for the selected fund; an empty period's switch shows its state (for example, greyed with a tooltip). | new |

### O2 -- Andrew reads every holding by its company name, in one casing, wherever it appears

Rankings, trend, trades and the AI text name a security the same way. A ticker is secondary text at most.

Findings: `RFW-D05`, `RFW-D11`, `RFW-U14`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D05 | security names, Bloomberg-channel funds | For all 9 Bloomberg-sourced funds (TXUE, BIDD, CGIC, INEQ, SCHY, WCMG, TSEL, ETFT, PCLG), holdings show raw Bloomberg tickers instead of names: '8306 JP Equity', 'TTE FP Equity', '2330 TT Equity'. That is 26-40 per fund on the YTD view, and 496 distinct raw ids such as 'EOAN_GR_Equity' in the audit trail. The issuer and home funds (IDVZ, PFOE, GQGU, BASG) show names. | Every holding on the face shows a security name. A raw ticker appears only as secondary text, and the count of nameless holdings is 0, or each is listed in the census. | new |
| RFW-D11 | holding names truncated at source | IDVZ's home-producer names are cut at 30 characters: 'Kimberly-Clark de Mexico SAB d', 'International Container Termin', 'BB Seguridade Participacoes SA' (4 on the YTD view). | No holding name on the page is a 30-character cut; a full name comes from G1/G4/the crosswalk. | new |
| RFW-U14 | name casing | The same security is cased differently across sections: 'INTUIT INC' in BASG's rankings and 'Intuit Inc' in its trend; issuer sources are ALL CAPS, others title case. | One display name per security across the page (G1 canonical name). | new |

### O3 -- Andrew reads which sectors drove or dragged a fund, and how much of the fund has no sector, as two separate facts

A no-sector bucket is never ranked as a sector; its share is stated beside the sector tables.

Findings: `RFW-D04`, `RFW-D06`, `RFW-U16`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D04 | G4 security_market (prices and GICS) | Inputs that did not arrive: 'Security prices: 0 of 765 arrived' and 'GICS sectors: 0 of 765 arrived'. G4 date=2026-10-01 holds 32 rows against the 765 security-days the page needs, and G4 history otherwise holds one date (2026-09-29). | G4 for the as-of date carries px_close and gics_sector for at least 95% of the universe's priced holdings, and the census reads that share. | known (ROUND_ANALYSIS.round5.md section 4 cell 7 (S14 G4 price cell)) |
| RFW-D06 | GICS sector coverage | 'Unclassified' is ranked as a sector in the YTD sector tables of 10 funds, and is the single largest sector in 6: ETFT -6.59%, BASG -3.00%, TSEL -2.93%, BIDD -2.28%, TXUE -0.77% (weakest), and GQGU +3.83% (the STRONGEST). 'Sectors not shown' (most contribution unclassified) appears for IDVZ, INEQ, PFOE, ETFT and PCLG, and in GQGU's trend. 'No GICS sector in the source' is BASG's top trend sector away (-26,612,661 of 70,162,415 traded). | Unclassified carries at most 10% of any fund's absolute YTD contribution, with the share printed; until then it is never ranked as a sector (RFW-U16). | new |
| RFW-U16 | Unclassified as a ranked sector | 'Unclassified' is ranked as if it were a sector ('1 Unclassified +3.83%' at the top of GQGU's Strongest sectors). | The no-sector bucket is never ranked. It shows as a footnote under the sector tables ('x% of this period's contribution has no sector'). | new |

### O4 -- Andrew reads a fund's panel as a presentation: the answer at rest, the method and the audit one click away

At rest, each block shows its result and a count chip. Method sentences, legends, provenance, grade history and the trade audit open on demand (C14), and an empty period shows one designed empty state (C12).

Findings: `RFW-U01`, `RFW-U03`, `RFW-U04`, `RFW-U07`, `RFW-U08`, `RFW-U12`, `RFW-U13`, `RFW-U17`, `RFW-U18`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-U01 | header | '13 of 13 funds current' is printed twice: the stat tile and the sentence under it. | The current-funds count appears once; the sentence names only lagging funds, and is absent when none lag. | new |
| RFW-U03 | empty ranking tables | An empty period renders four table shells, each saying 'No holding added to the return' or 'No sector took from the return'. | A fund-period with 0 ranked renders ONE empty-state line with the reason and the count without a price. | new |
| RFW-U04 | method captions | Every ranking block repeats a two-line method sentence ('Ranks N holding(s) by their contribution ... Priced from the funds' own reported valuations where no Bloomberg price is on file: price-only returns, dividends excluded. 1 holding-day(s) were refused ...'). That is 39 fund-periods on the page. | Each block shows a one-line count chip ('39 ranked; 1 refused day'). The method text sits once behind an info icon or modal ('How this is computed'). | new |
| RFW-U07 | BET/TILT legend | The BET/TILT definition is a sentence in every trend block ('a BET is one window carrying at least half of everything traded in the line, a TILT is built across windows'). | The definition sits behind the pill's tooltip; the block caption carries dates and trading days only. | new |
| RFW-U08 | AI account: audit material on the face | Each account carries, inline: a 'Cited rows' dump of system keys ('holding_contribution IDVZ/R30/71654V408 = 0.00340522; trade_schedule IDVZ/47215P106/2026-09-14 = -2.8542e+06; ...'), 'Re-graded ... grounding_check/4 ... Superseded grade', 'Demo read: ...', and an 'Inputs as of:' dump of about 25 timestamped stored names. | An account shows its text, Observed and Inferred, and 'What would prove this wrong'. Cited rows, grade history, inputs and run provenance open from one 'Sources and checks' control. | new |
| RFW-U12 | audit trail volume and empty windows | With the audit trail open, the page is 39,194 px tall with 13,473 visible words and 243 disclosures. Every empty window is listed with its own G6 sentence ('Excluded before inference (G6): 2 cash line(s), 0 corporate action(s), 0 income event(s) ... No trades inferred in this window'). | Consecutive empty windows collapse into one line ('6 windows, no trades'). The G6 exclusions show once per fund, as totals, with per-window detail on demand. | new |
| RFW-U13 | system words in the trade log | The trade log shows system words: 'CLEAN', 'key RESOLVED', '(security_id)', 'G6', 'canonical_shape', 'flow factor 1.0000', and bronze keys and SHA256 as wrapped columns. | Confidence and key resolution read in plain words with the code in a tooltip. Bronze key and SHA256 sit behind a copy control; the FWD-1 trace keeps both reachable. | new |
| RFW-U17 | fund header freshness | The freshness tag reads 'Latest report 2026-09-30 HOME; current' (a source chip mid-sentence and a semicolon). | The header reads 'Latest report 30 Sep' with a source chip and a separate current/late chip. | new |
| RFW-U18 | AI account length | Each fund carries two accounts of about 120-180 words plus 5-7 Observed and 4-5 Inferred bullets each, all open. Observed bullets restate the prose. | Each account opens to its first two sentences; the rest and the Observed/Inferred lists expand on demand. | new |

### O5 -- Andrew reads the AI accounts in plain words, sees each account's grade before its text, and finds new accounts each morning with no seat awake

Readings carry display labels (the stored name in a tooltip). The grade is a badge at the top, and a FAIL is collapsed with its reason. The accounts come from the scheduled pipeline.

Findings: `RFW-D08`, `RFW-D09`, `RFW-U09`, `RFW-U10`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D08 | AI accounts in production | Every AI account reads 'Demo read: written by a seat ad-hoc run (2.0.0_SA_COO~RV, 2026-10-02T11:04:45Z), a QA-class read, not the scheduled pipeline's output.' No scheduled path produces accounts, so a page with no seat awake carries none. | The scheduled chain writes research_hypotheses for the page day with no seat act, and the footer reads the scheduled run. | known (ROUND_ANALYSIS.round5.md section 4 cell 1) |
| RFW-D09 | AI grounding | 2 of 24 accounts are served as 'Grounding FAIL' (IDVZ 'The last 30 days': '$1.6 million, $1.3 million' not in any cited row; CGIC 1). They are still shown in full. | 0 accounts FAIL at the scheduled run, or each FAIL is collapsed with its reason (RFW-U10). | new |
| RFW-U09 | AI prose: raw stored names | The AI text reads 'fear_greed/fear_greed_index sat at 28.09, with fear_greed/stock_price_strength at 0.4 and fear_greed/stock_price_breadth at 0.2'. The walker flagged 1215 raw-code hits. | A reading shows a display label ('Fear & Greed index 28.09; stock price strength 0.4'), with the stored name kept as the label's tooltip so the claim survives; 0 raw-code hits in account text. | new |
| RFW-U10 | AI account: FAIL presentation | A Grounding FAIL account is rendered in full as normal prose. The FAIL note comes after the text and cited rows, so the reader reads the account before learning it is not a pass. | The account's grade is a badge at its top. A FAIL account is collapsed by default with the reason in its summary line. | new |

### O6 -- Andrew reads a fund's buying trend and its trades as readable money and a month chart, with every exit sized

Notional in $ millions; the month trend as a small chart with month ticks; no overlap between the two trend tables; a full exit carries a money size; a one-window line is not called a bet.

Findings: `RFW-D10`, `RFW-D12`, `RFW-U05`, `RFW-U06`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D10 | trade log, exits | A full exit shows 'n/a' for est. price and est. notional (TXUE trim ATD_CN_Equity 138,182 -> 0; 6 n/a cells on the page). An exit's size in money is missing for every full exit. | A full exit is priced from the prior report's valuation (or G4), with the source shown; 0 'n/a' notional on exits. | new |
| RFW-D12 | trend history depth | IDVZ's buying trend runs from 2026-08-21 (30 trading days) and PFOE's from 2026-08-24. Every IDVZ line is 1 window and reads BET, so the tilt/bet reading says nothing for the two Opal funds. | IDVZ and PFOE trend windows start at their inception or 2026-01-02; a line with 1 window reads 'single trade', not BET. | known (ROUND_ANALYSIS.round5.md section 4 cell 4) |
| RFW-U05 | buying trend, BY MONTH | The month trend is ASCII marks ('0 0 0 0 + + + + + 0', '. . . . . . . 0 + 0') with a legend sentence. At 1440 px the column runs into the adjacent 'Leaned away from' table: the marks touch the next row's number ('0 1 ARTHUR J'). | The month trend is a small bar or sparkline with month ticks, no legend sentence, and 0 overlap between the two tables at 1280-1920 px. | new |
| RFW-U06 | trend table format | Net notional is printed to the dollar ('+22,973,442'), and holding names wrap to 3 lines in the narrow holding column ('SPACE EXPLORATION TECHN-CL A'). | Notional reads in $ millions with one decimal; names wrap to at most 2 lines. | new |

### O7 -- Andrew sees which inputs did not arrive, and tells a missing input from one a fallback covered

Three states (arrived / covered by fallback / missing), each counted, grouped by reason, and the per-item list opening on demand.

Findings: `RFW-D14`, `RFW-U11`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D14 | input census states | The census lists all 765 securities as 'missing, no G4 row ... the rankings price it from the fund's own reported valuation'. It counts an input that has a working fallback (CALL 1) as 'did not arrive', with no third state. | The census reads three states (arrived / covered by fallback, naming the fallback / missing), each with its count. | new |
| RFW-U11 | Inputs that did not arrive: lists | The three detail lists repeat one sentence per item: 765 x 'missing, no G4 row for 2026-10-01; the rankings price it from the fund's own reported valuation' and 765 for GICS. | Each list is grouped by reason with a count and a fund breakdown; the per-security list opens on demand (with RFW-D14's three states). | new |

### O8 -- Andrew compares each Opal fund's group against the benchmarks he chose

ACWI and IWM sit on the page as benchmarks beside SCHY.

Findings: `RFW-D13`.

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-D13 | benchmarks | The only benchmark on the page is SCHY (IDVZ peers). ACWI and IWM, the controls Andrew chose, are absent; the PFOE group has no benchmark at all. | ACWI and IWM appear as benchmarks with their own rankings and trend. | known (TO-RIV-l-1; ROUND_ANALYSIS.round5.md section 4 cell 4) |

### Not outcome-bearing (recorded so the PRD carries them)

| id | surface | observed | acceptance | status |
|---|---|---|---|---|
| RFW-U15 | chart render error | The console logs 'Error: <rect> attribute width: A negative value is not valid.' twice (-0.5, -0.4): a bar drawn with a negative width. | 0 console errors on load. | new |
| RFW-U19 | page chrome not walked | Walked: the platinum page bytes of 2026-10-02 (sha256 97162f5192bf..., served at 14:17:10Z), served locally. NOT walked: the gateway's sign-in, its route wrapper and any archive index at mcp.opalinvest.dev/rivalfunds. | A signed-in walk of the gateway route (the FWD-1 read) confirms the wrapper adds no further defect. | new |

## PART II -- WHERE THE BOUNDARY SITS

- **ETFS_RIVALS owns:** the page render (`render.py`, `page_theme`), the publish (`publish_page.py`), the A1 producers (`gold_holding_contribution.py`, `gold_buying_trend.py`, the input census), the AI chain (`ai_accounts.py`) and its scheduled wiring, G1-G6, and the rivalfunds Bloomberg pull worded under R-21 (the v0.8 leg, the G4 enrichment).
- **ETFS_RIVALS relies on, and does not own:**
  - the gateway route `mcp.opalinvest.dev/rivalfunds` and its sign-in (not walked; RFW-U19);
  - the Fear & Greed, RSI, trending and keyword stores (read-only);
  - Data Harvest chatter (`AMGT_HARVST`);
  - the IDVZ/PFOE home producer's source files;
  - `portal/DESIGN.md`, the contract FWD-19 adopts.
- **Sibling projects** (from `project.json` related): `ETFS_POSITIONING` (untouched by Andrew-direct), `ETFS_INGEST`, `OPAL_BBGTML`, `AMGT_HARVST`, `AMGT_RESAPP`, `LGIC_NAMING`/`LGIC_ENFORCE`/`LGIC_CANON`. No finding here assigns work to a sibling.

## PART III -- THE QUALITATIVE BAR

- On the opening view, Andrew never reads a table he must ignore: no empty period, no 'Unclassified' ranked as a sector, no raw ticker where a company name belongs.
- He never meets two numbers on one page that contradict each other about whether the data is current.
- He reads a fund's panel the way he reads a portal page: the answer first, and the method, provenance and audit only when he asks for them.
- An AI account he reads tells him its grade before he invests in its text.

## PART IV -- THE SUBSTRATE (findings, measured)

- **The page is one self-contained static HTML file**: 0 `<script>` tags, 0 external sources, 1,575,052 bytes. The fund and period switches are script-free radio inputs (`rf-fund`, `rf-period`), so at rest a reader sees about 1,900 words, not the 88,826 in the file. **Every disclosure fixture must be CSS or HTML only:** `<details>/<summary>` (already used 243 times), the `popover` attribute, or a `:target` dialog. The portal's React dialog and tooltip components cannot be imported. C14 names `<details>/<summary>` and a dialog as compliant vehicles.
- **`portal/DESIGN.md` C12 (four empty states), C13 (no clip without a recovery path) and C14 (progressive disclosure is portal law)** are the in-pattern rules Andrew's 'progressive disclosure, modals, and other in-pattern fixtures' maps to. FWD-19 adopts the portal's look.
- **`/ui-walk` cannot walk the gateway route.** `walk.mjs:67` refuses any non-localhost base. The walk served the platinum bytes on `localhost:5180` with `--no-login`. The walker's checks are portal-tuned: they flagged raw-code 1215 times and n/a once, and missed the data findings, which came from the page text, the manifest and S3.
- **The A1 producers are write-once per date** (manifest `a1_produced`: SKIPPED, '1 object(s) already at date=2026-10-02'). The publish has no vintage comparison between the A1 tables and the G1/G4 it reads itself (RFW-D01).

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- G4 carries prices and GICS at universe scale daily (RFW-D04).
- A name source exists for the Bloomberg-channel funds' holdings (RFW-D05): the BQL capture, G4 or the crosswalk.
- A GICS source covers the holdings no issuer file classifies (RFW-D06).
- An A1 rebuild runs when its inputs move (RFW-D01).
- The AI chain runs on the scheduled path with its own secret (RFW-D08; VEW-2 covers OpenAI).
- The IDVZ/PFOE backfills and the v0.8 leg (ACWI/IWM) land (RFW-D12, D13).
- Each of these is named, not sequenced. Sequencing is the COO's.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured on the served page `date=2026-10-02` (LastModified 2026-10-02T14:17:11Z, batch fast-a1-publish-1002f), read 2026-10-02 ~14:20-14:45Z.

| measure | value |
|---|---|
| words in the page file / visible at rest / visible with the audit trail open | 88,826 / ~1,889 / 13,473 |
| page height with the audit trail open | 39,194 px; 243 `<details>` |
| fund-periods ranking 0 holdings (MTD+QTD) | 24 of 26 (all but BASG) |
| funds whose YTD sector table ranks 'Unclassified' / ranks it #1 | 10 / 6 |
| distinct raw `*_Equity` ids in page text | 496 |
| input census: holdings / prices / GICS / market readings arrived | 2 of 13 / 0 of 765 / 0 of 765 / 23 of 23 |
| AI accounts served / grounding FAIL | 24 / 2 (IDVZ 1, CGIC 1) |
| walker: raw-code / unconnected-field / console errors | 1215 / 1 / 2 |

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The gateway wrapper, sign-in and archive index at `mcp.opalinvest.dev/rivalfunds` were not walked (RFW-U19).
- Causes marked `inferred` in the register were not checked in code: RFW-D05 (no name field in the BQL capture), D09, D10, D11 and U15.
- One viewport width (1440 px) was read. No narrow or mobile width was walked.
- The walker's 1215 raw-code hits are observations over repeated text, not 1215 distinct defects.
- Only the 2026-10-02 page was walked. The 10-01 page and the archive were not compared.
- Two numeric G1 `fund_id` values (`4823`, `5415`) were seen in G1 at date=2026-10-01. Whether they are the issuer funds' designed keys was not resolved, and no finding rests on them.

## Causes and evidence (from the register)

| id | outcome (PRD v0.10) | cause | claim | evidence |
|---|---|---|---|---|
| RFW-D01 | FWD-20, FWD-14, FWD-9 | The A1 producers skip when an object for the date already exists, so no later input refresh rebuilds them, and the publish does not compare the A1 tables' input vintage with the G1/G4 objects it reads itself. | measured | manifest.json a1_produced (SKIPPED x3); S3 LastModified: holding_contribution date=2026-10-02 11:03Z, input_census 11:04Z, canonical_shape date=2026-10-01 holdings-20261002T111038Z 11:11Z, security_market date=2026-10-01 11:10Z |
| RFW-D02 | FWD-20, FWD-2 | The census was produced at 11:04Z (RFW-D01); the freshness check runs at publish over newer G1. | measured | manifest checks.report_date_freshness vs the input_census text; RFW-D01 |
| RFW-D03 | FWD-14 | Page 2026-10-02 has asof 2026-10-01 (CALL 3), so MTD/QTD = one day. A day's return needs reports on both 09-30 and 10-01, and the A1 build at 11:03Z saw 10-01 reports for 2 funds only (RFW-D01). | measured | data-ranked/data-missing per fund-period: IDVZ 0/40, TXUE 0/49, BIDD 0/48, CGIC 0/193, INEQ 0/101, SCHY 0/104, PFOE 0/22, WCMG 0/47, GQGU 0/38, TSEL 0/27, ETFT 0/28, PCLG 0/28, BASG 32/1 |
| RFW-D04 | FWD-20, FWD-14, FWD-6 | The daily G4 Bloomberg enrichment (prices plus GICS) is not running at universe scale. Known as the round-6 S14 G4 price cell. | measured | S3 security_market date=2026-10-01 market-20261002T111038Z: 32 rows; census text |
| RFW-D05 | FWD-14, FWD-15, FWD-5, FWD-18 | The Bloomberg BQL capture carries no security name field into silver and G1, so the display falls back to the ticker (cause inferred; the capture's columns were not read). The symptom is measured. | inferred | YTD ranking rows per fund with raw-ticker names: TXUE 40, BIDD 40, CGIC 39, INEQ 40, SCHY 40, WCMG 26, TSEL 26, ETFT 34, PCLG 26; 496 distinct *_Equity ids in page text |
| RFW-D06 | FWD-6, FWD-14, FWD-15 | G4 GICS is absent (RFW-D04). Issuer files carry GICS for few lines, and the cross-fund fallback (CALL 9) cannot fill a security no fund's file classifies. | measured | YTD sector tables per fund; 8 'No GICS sector in the source' rows |
| RFW-D07 | FWD-3 | The Bloomberg leg and the IDVZ home producer had not delivered the 10-01 report by 14:17Z; the cause per fund was not read. | measured | manifest checks.report_date_freshness: IDVZ, BIDD, CGIC, SCHY latest 2026-09-30, lag 1 |
| RFW-D08 | FWD-16, FWD-17 | The AI chain is not yet wired into the scheduled Lambda path (CALL 5; round-6 cell 1). | measured | AI account footer text on every fund panel |
| RFW-D09 | FWD-16, FWD-17, FWD-9 | The model wrote rounded dollar figures that the facts do not carry in that form (inferred from the FAIL text). | inferred | manifest checks.analysis_grounding: IDVZ 1 FAIL of 2, CGIC 1 FAIL of 2 |
| RFW-D10 | FWD-5 | The implied price needs the later report's valuation, and an exited line has none (inferred). | inferred | 6 'n/a' cells in the audit trail |
| RFW-D11 | FWD-14, FWD-15 | The home producer's source field is 30 characters wide (inferred from the exact cut). | inferred | YTD ranking rows IDVZ: 4 names of exactly 30 characters |
| RFW-D12 | FWD-15, FWD-2 | The IDVZ/PFOE backfills have not landed (round-6 cell 4). | measured | IDVZ trend: WINDOWS = 1 on every line shown |
| RFW-D13 | FWD-11 | The v0.8 Bloomberg leg is built and inert (RIV-l-1); ACWI/IWM wait on the leg's request-cost measurement and preview. | measured | fund switch strip: 'SCHY Benchmark' only |
| RFW-D14 | FWD-20 | The census enum is arrived / missing/stale; there is no 'covered by fallback' state. | measured | census details text: the same sentence repeated per security |
| RFW-U01 | FWD-18 | The headline sentence duplicates the stat. | measured | 01-top.png |
| RFW-U02 | FWD-18, FWD-14 | The default is a fixed MTD. | measured | 02-fund1.png |
| RFW-U03 | FWD-18 | Each table renders its own empty row. | measured | 02-fund1.png |
| RFW-U04 | FWD-18 | The method text is rendered inline per block. | measured | 10-basg-ytd-a.png, 12-gqgu-ytd-a.png |
| RFW-U05 | FWD-15, FWD-19 | The marks are text in a fixed-width column without a gutter. | measured | 11-basg-ytd-b.png |
| RFW-U06 | FWD-15, FWD-19 | Raw float formatting and a fixed column width. | measured | 11-basg-ytd-b.png |
| RFW-U07 | FWD-15, FWD-18 | Inline legend text. | measured | 02-fund1.png |
| RFW-U08 | FWD-16, FWD-17, FWD-18 | render prints every provenance field inline. | measured | 03-fund1-b.png, 04-fund1-c.png |
| RFW-U09 | FWD-16, FWD-17, FWD-19 | A1 ruling 5 made the AI name a reading by its stored name, and the render shows it verbatim. | measured | walker check raw-code x1215 |
| RFW-U10 | FWD-16, FWD-9 | The grade renders as a footer. | measured | 03-fund1-b.png |
| RFW-U11 | FWD-20, FWD-18 | A per-security row with a repeated reason. | measured | census text |
| RFW-U12 | FWD-18, FWD-5 | Every window renders its exclusion line and empty state. | measured | rf-shoot2: scrollHeight 39194, visible words 13473 |
| RFW-U13 | FWD-18, FWD-19, FWD-1 | The render prints field names and values verbatim. | measured | 22-audit-trace.png |
| RFW-U14 | FWD-19, FWD-4 | Names pass through from each source. | measured | 10-basg-ytd-a.png vs 11-basg-ytd-b.png |
| RFW-U15 | FWD-19 | A bar width is computed from a signed value without abs or clamp (inferred). | inferred | walker console_errors x2 |
| RFW-U16 | FWD-14, FWD-6 | The no-sector bucket is a row in the ranking. | measured | 12-gqgu-ytd-a.png |
| RFW-U17 | FWD-2, FWD-19 | Concatenated status text. | measured | 01-top.png |
| RFW-U18 | FWD-16, FWD-17, FWD-18 | Both accounts and all bullets render open. | measured | 03-fund1-b.png, 04-fund1-c.png |
| RFW-U19 | FWD-1 | /ui-walk refuses any non-localhost base; the gateway route needs Andrew's sign-in. | measured | .claude/skills/ui-walk/walk.mjs:67 |

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/rivalfunds-ui-data-walk-20261002.md
  REGISTER          docs/briefs/rivalfunds-ui-data-findings-20261002.json (33 ids, coverage-checked)
  PROJECT           ETFS_RIVALS (D5/ETFS, site-z; COO 2.0.0_SA_COO~RV; CTO 1.0.0_SA_CTO~Z)
  EXISTING PRD      org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md v0.10
  SIBLING PROJECTS  ETFS_POSITIONING, ETFS_INGEST, OPAL_BBGTML, AMGT_HARVST, AMGT_RESAPP, LGIC_*
  PRIOR ART         portal/DESIGN.md C12-C14; the page's 243 <details>; CALLs 1-12 rulings; VEW-2
  ANDREW-DIRECT     org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_141xZ_RIVALFUNDS_UI_WALK_BRIEF_TO_CTO_COO_RV_CANONICAL_DRIVE.md
  MEASURED AT       2026-10-02 ~14:20-14:45Z, on the page served at 14:17:11Z
```
