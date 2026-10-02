# ETFS_RIVALS -- Rival funds: daily holdings of six rival active ETFs, each fund's trade schedule, and a served research page

```json
{
 "project": "ETFS_RIVALS",
 "directive": "D5",
 "fabric": "site-z",
 "prd_version": "v0.10",
 "step": 4,
 "brief_ref": "docs/briefs/etf-holdings-research-20260929.md@77c891c869",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13", "FWD-14", "FWD-15", "FWD-16", "FWD-17", "FWD-18", "FWD-19", "FWD-20"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~Z` (L4), 2026-09-30.
**Brief:** `4.0.0_SA_CRO~Z`, revision 3 (trade schedule as the foundation), with the supporting specification
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md` and the feasibility probe
`TRADE_INFERENCE_FEASIBILITY.md` in the same folder.
**Andrew's words:** every word this PRD rests on is verbatim in that folder's `ANDREW_DIRECT.md`.
**Registered** @`ec6f31261c` (D4/ETFS), **moved to D5/ETFS** on Andrew's word (record `ANDREW_DIRECT_20260930_063xZ_ETFS_INCLUDED_IN_D5_MACROS_ETFS_RIVALS_TO_D5.md`), fabric site-z. **COO:** `2.0.0_SA_COO~RV`, seated by 0.0.0_AB_MSTR~Z (msg 26952).
**CVO:** `3.0.0_SA_CVO~Z`. **CRO:** `4.0.0_SA_CRO~Z`.
**The ENDPOINT is confirmed by Andrew** (2026-09-30 ~01:5x ET, *"1.) Yes approved."*, record @`77c891c869`).
**Sign-off:** proportionate (CLAUDE.md rule 27). The CVO signs the ratified-text half; the brief half is accepted because the
CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

Landed verbatim from `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_RIVALFUNDS_20260930.md` @`33c1d096a3`, as Andrew
approved it.

```
  FWD-1  Andrew opens one rival fund's day on the live page, reads what it
         traded, and traces a trade back to what the fund itself published
         DONE WHEN  EXERCISED -- one live trace: Andrew opens the rival-funds
                    page on the Opal site, picks BASG, reads its most recent
                    trades first, and follows one trade back through the two
                    holdings reports it was inferred from to the fund's own
                    published files
         ACCEPT     every step Andrew takes shows real holdings the fund
                    published; the page he reads is the one kept for that day,
                    and the list of past days shows it; a step fed by made-up
                    or sample data fails the outcome
         SOURCE     brief O1 (the candidate thread); Part V H1-H7 (each hop
                    crossed once for BASG); ANDREW_DIRECT item 4 (/rivalfunds,
                    archive by day)

  FWD-2  Andrew sees how much real history each fund has, and never mistakes
         an old report for a fresh one
         DONE WHEN  EXERCISED -- Andrew reads, for each of the six funds, which
                    days carry a genuinely new report, which are weekly or
                    quarterly, which are gaps and which repeat an older report,
                    back up to two years or the fund's own start
         ACCEPT     for any fund and day Andrew can tell whether the holdings
                    were actually published that day or carried over from an
                    earlier report; a fund's start as an ETF is not blurred
                    with any earlier fund it came from
         SOURCE     brief O2, IV.2; ANDREW_DIRECT scope clarification ("as much
                    as we can up to that threshold ... weekly, fine")

  FWD-3  Fresh holdings arrive every trading morning with nobody downloading
         anything, and Bloomberg is used only when the fund's own site fails
         DONE WHEN  EXERCISED -- over several consecutive trading days, each
                    fund's holdings are collected from its own site each
                    morning; on a day a fund's site fails, Bloomberg fills it
                    if it carries that fund, and the page says plainly when it
                    cannot (GQGU)
         ACCEPT     Andrew does nothing by hand on an ordinary day; on any day
                    he can see which source supplied each fund, and a fund that
                    was covered from its own site shows that Bloomberg was not
                    asked
         SOURCE     brief O3, Part V H6; ANDREW_DIRECT items 9 and 12

  FWD-4  Andrew compares any fund against any other in one common format,
         without learning six different file layouts
         DONE WHEN  EXERCISED -- Andrew reads two funds that came from
                    different sources side by side in the one master format,
                    with each position's source and dates shown
         ACCEPT     every position a fund disclosed appears, including cash,
                    derivatives and anything that could not be identified; a
                    detail the fund published but the master format has no
                    place for yet is kept, not thrown away
         SOURCE     brief O4, Part III (cash and unidentified visible);
                    ANDREW_DIRECT item 14 and L1 direction point 1

  FWD-5  Andrew reads each rival fund's trade schedule: what the manager
         actually bought and sold, and when
         DONE WHEN  EXERCISED -- for each of the six funds Andrew reads its
                    trades (entries, adds, trims and exits) with the shares
                    traded, the window they happened in, an estimated price and
                    size, and how sure the inference is
         ACCEPT     a price move, a dividend, a change of identifier or the
                    fund simply growing or shrinking never shows up as a trade;
                    a trade too small to tell from noise is not shown as one;
                    where reports are days apart the trade is placed in that
                    wider window, never invented on a single day
         SOURCE     brief rev 3 O5 (the foundation); ANDREW_DIRECT "reverse
                    engineer their actual trades ... a gold table for each
                    active etf that is effectively their trade schedule";
                    trade floor 0.2% and dividends from Bloomberg (same file)

  FWD-6  Andrew sees where a manager's holdings and choices helped or hurt
         DONE WHEN  EXERCISED -- Andrew reads, for one fund and period, its
                    best and worst holdings by return and by contribution, and
                    how the trades in its trade schedule have done since,
                    including positions it has since sold
         ACCEPT     every ranking says what it ranks, over what window and out
                    of how many holdings; a holding with a missing price is
                    counted as missing, not quietly left out
         SOURCE     brief O6, Part III (rankings state their window and
                    denominator)

  FWD-7  Andrew uses the AI to form views about a manager's behaviour, and
         can later check those views against what the manager actually did
         DONE WHEN  EXERCISED -- one AI account of a fund's process, built
                    from its trade schedule, is saved, and a later account
                    grades it against trades inferred after it was written
         ACCEPT     every claim in the AI account points to the figures it came
                    from, separates what was seen from what is guessed, and
                    says what would prove it wrong; a later grading cannot
                    rewrite what the earlier account said
         SOURCE     brief rev 3 O7 (starting from the trade schedule), Part III
                    (the AI does not manufacture returns or intent; one clear
                    signal, not a data dump); ANDREW_DIRECT L1 direction point 3

  FWD-8  An Opal researcher can rebuild the research from the kept raw files
         and add a new fund without changing what anything means
         DONE WHEN  EXERCISED -- a rebuild from the kept raw files reproduces
                    the published figures for one day, and running the same
                    day again adds no duplicate positions
         ACCEPT     a researcher can show where every figure came from, and a
                    rerun never silently replaces an earlier day's record
         SOURCE     brief O8, Part V H2-H3 (backfill by replay)

  FWD-9  A day's page never publishes figures that failed their checks
         DONE WHEN  EXERCISED -- on a day where a check is made to fail on
                    purpose, the page either says what failed or is not
                    published, and it never shows the failed figures as normal
         ACCEPT     Andrew can never read a quietly wrong page; when something
                    is missing or failed, the page tells him what
         SOURCE     brief Part III ("nothing publishes past a failed
                    guardrail"); Part V H7; ANDREW_DIRECT item 10

  ===== ADDENDUM A, v0.3, 2026-09-30 -- peer groups, the IDVZ group ========
  From docs/briefs/etfs-rivals-idvz-expansion-20260930.md (midstream) and the
  endpoint addendum ENDPOINT_FORWARD_RIVALFUNDS_ADDENDUM_A_PEER_GROUPS_IDVZ_20260930.md,
  DONE WHEN confirmed by Andrew with one change to FWD-1 ("fwd 1 should include
  idvz and pfoe right as the two opal etfs, with their respective peer groups.
  otherwise, yes, all of these are fine"). The lines below SUPERSEDE FWD-1, 2,
  3, 5, 6 and 7 above; FWD-4, 8 and 9 stand as above.

  FWD-1  (AMENDED) Andrew opens each of the two Opal ETFs' peer groups on
         the live page and reads it, the Opal fund included, on one plane
         DONE WHEN  EXERCISED -- one live trace per Opal ETF: Andrew selects
                    IDVZ and reads IDVZ and its peers (TXUE, BIDD, CGIC, INEQ,
                    SCHY) side by side, then selects PFOE and reads PFOE and its
                    peers (WCMG, GQGU, TSEL, BASG, ETFT, PCLG) the same way:
                    trade schedules, style reads and the FWD-6/7 views; in each
                    group he follows one rival's trade back to the holdings
                    reports it was inferred from and to where they came from
         ACCEPT     every step shows real published holdings; a step fed by
                    sample data fails the outcome
         SOURCE     brief O1; Andrew point 3 and his FWD-1 confirmation
  FWD-2  (AMENDED: every fund in every group) Andrew sees how much real
         history each fund has, and never mistakes an old report for a fresh one
         DONE WHEN  EXERCISED -- for every fund in both groups, Andrew reads
                    which days carry a genuinely new report, which repeat an
                    older one, and which are gaps, back up to two years or the
                    fund's own start
         ACCEPT     as before; a fund that is in two groups is shown once, with
                    one history
         SOURCE     brief O2, IV.1
  FWD-3  (AMENDED: the source is chosen per fund) Fresh holdings arrive every
         trading morning with nobody downloading anything, from each fund's
         chosen source
         DONE WHEN  EXERCISED -- over several consecutive trading days, every
                    fund is collected each morning by its own source policy:
                    the IDVZ group from Bloomberg, the PFOE group from each
                    fund's own site with Bloomberg as the fallback; the page
                    names the source per fund and day
         ACCEPT     Andrew does nothing by hand; a fund's policy is a setting,
                    not code; a day a source fails says so plainly
         SOURCE     brief O2, IV.1-IV.2; Andrew "bbg is better for this group"
  FWD-5  (AMENDED: income and corporate actions) Andrew reads each fund's
         trade schedule: what the manager actually bought and sold, and when
         DONE WHEN  EXERCISED -- for every fund Andrew reads its trades
                    (entries, adds, trims, exits) with shares, window, estimated
                    price and size and confidence; on a fund and window that
                    contain a dividend, a split and a cash/currency line, none
                    of the three appears as a trade, and a purchase funded from
                    income reads as a trade labelled as income-funded
         ACCEPT     dividend and interest income, their currency conversion,
                    splits, bonus issues, spinoffs, stock dividends and rights
                    issues never read as a manager's decision; cash and
                    currency lines are the cash cross-check, not positions
         SOURCE     brief O3, IV.3; Andrew "did we already account for
                    dividend/interest income? That should be covered"
  FWD-6  (AMENDED: by sector and security) Andrew sees where each manager's
         trading helped or hurt, by sector and by security
         DONE WHEN  EXERCISED -- for one fund and period Andrew reads which
                    trades and trade clusters out- or under-performed afterwards,
                    summarised by sector and by security, each with its window
                    and denominator, including positions since sold
         ACCEPT     a holding with a missing price or sector is counted as
                    missing, never left out
         SOURCE     brief O5; Andrew view 1
  FWD-7  (AMENDED: projections and the wildcard) Andrew uses the AI to form
         views about a manager's behaviour, and can check them later
         DONE WHEN  EXERCISED -- for one fund Andrew reads (a) its projected
                    trading by sector and security if the observed trends
                    persist, each with what would contradict it, and (b) a short,
                    labelled wildcard section in which every item cites its rows
                    and says what would disprove it; a later account grades the
                    earlier projection against trades inferred after it
         ACCEPT     nothing invents a return, a trade or a motive; a later
                    grading cannot rewrite the earlier account
         SOURCE     brief O6, O7; Andrew views 2 and 3
  FWD-10 (NEW) Andrew sees whether each manager trades with discretion or by
         system, and why
         DONE WHEN  EXERCISED -- Andrew reads each fund's style read with its
                    evidence (timing concentration, breadth of the book touched,
                    trade size), and each group's index control (v0.8: ACWI
                    for the IDVZ group, IWM for the PFOE group) reads as
                    systematic on that same evidence
         ACCEPT     a count of trades alone is never the evidence; a label is
                    shown only after the control reads correctly
         SOURCE     brief O4, IV.3; Andrew "at a 20bps tolerance it's
                    immediately clear who is discretionary and who is
                    systematic"
  FWD-11 (NEW) Andrew compares an Opal fund with its rivals on the same
         measures
         DONE WHEN  EXERCISED -- Andrew reads IDVZ against its peers and PFOE
                    against its peers on the style read, the trading results and
                    the projections, computed by the same rules
         ACCEPT     Opal's own fund has no separate method and no special
                    treatment
         SOURCE     brief O8; Andrew point 3
  FWD-12 (NEW) Opal adds a peer group without a new pipeline
         DONE WHEN  EXERCISED -- a third group is added as a mapping entry
                    (the Opal fund, its rivals, each fund's source policy) and
                    flows through collection, the tables, the page and the
                    archive with no code change
         ACCEPT     a fund rivalling two Opal funds is stored once; adding a
                    group changes a mapping, not code
         SOURCE     brief O9, IV.4

  ===== ADDENDUM B, v0.9, 2026-10-01 -- the presentation and the AI synthesis ====
  From docs/briefs/rivalfunds-backend-data-ai-synthesis-20261001.md and
  docs/briefs/rivalfunds-frontend-mcp-page-20261001.md (4.0.0_SA_CRO~RV, midstream,
  on Andrew-direct @52eb8a5dc7, his two dictated transcripts verbatim).
  STATUS: CONFIRMED by Andrew 2026-10-02 ~02:2xZ ("release the hold on the Rivalfunds
  outcomes ... we need that work driving now"), record
  ANDREW_DIRECT_20261002_022xZ_RIVALFUNDS_ADDENDUM_B_RELEASED_DRIVE_NOW.md.
  FWD-1..12 stand. FWD-1's trace stays reachable, and FWD-13 is this workstream's
  thread.

  FWD-13 (NEW, THE THREAD) Andrew opens the rival-funds page, reads IDVZ's best
         and worst this month, quarter and year, then picks one rival and reads
         its rankings, its buying trend and the AI's account of it
         DONE WHEN  EXERCISED -- one live, signed-in read: the page opens on
                    IDVZ's ranking for month-to-date; Andrew switches to
                    quarter-to-date and year-to-date and the tables change; he
                    picks one IDVZ rival and reads its ten best and ten worst
                    holdings, five best and five worst sectors, its year's
                    buying trend and the AI's two-part account; he follows one
                    ranked figure back to the holdings and prices it came from
         ACCEPT     everything he reads comes from that morning's real run; a
                    figure built from sample data fails the outcome
         SOURCE     backend brief O1; frontend brief O1; transcript 2
                    ("default to IDVZ", "toggle MTD, QTD, YTD")

  FWD-14 (NEW) Andrew ranks any fund's best and worst holdings and sectors for
         the month, quarter and year to date, by the same rules for every fund
         DONE WHEN  EXERCISED -- for every fund in both groups, Opal's own and
                    each group's benchmark included, Andrew reads the ten
                    holdings that added most to the fund's return and the ten
                    that cost it most, and the five best and five worst sectors,
                    for each of the three periods
         ACCEPT     a figure Andrew checks agrees with what that fund's holdings
                    and their prices add up to over the period; each table says
                    which period and how many holdings it ranks; a holding with
                    no price shows as missing, never dropped
         SOURCE     backend brief O2; transcript 1 point one; transcript 2
                    component 1
         RULED (v0.10, CTO on Andrew's release): CONTRIBUTION -- how much each
                    holding added to or took from the fund's return over the
                    period, weighted day by day by how much of it the fund held
                    (holdings rebuilt from its reports); this works for the
                    benchmarks too. The trading result stays in FWD-6.

  FWD-15 (NEW) Andrew reads each fund's tilts and bets: where its buying has
         trended this year, by holding and by sector
         DONE WHEN  EXERCISED -- for every fund Andrew reads a simple
                    year-to-date table in the same shape as the rankings: the
                    ten holdings and five sectors its buying leaned into most,
                    and the ten holdings and five sectors it leaned away from
                    most, each line read as a tilt or a bet with a plain trend
                    mark
         ACCEPT     a trend is never presented as one that will continue; the
                    table says how many trading days it covers
         SOURCE     backend brief O3; transcript 1 point two ("just because
                    there is a trend does not mean it is expected to continue
                    indefinitely"); transcript 2 component 2

  FWD-16 (NEW) Andrew reads what each fund has done in the last 30 days:
         anything unusual, its big wins and its big losses
         DONE WHEN  EXERCISED -- for every rival and both Opal funds (never
                    a benchmark) Andrew reads the AI's account of the fund's
                    last 30 days
         ACCEPT     every figure in it points to where it came from; what was
                    seen is kept apart from what is guessed; a benchmark has no
                    such section
         SOURCE     backend brief O5; frontend brief O4; transcript 2
                    ("rolling 30-day view", "We do not need to apply any
                    analysis to the benchmark")

  FWD-17 (NEW) Andrew reads the AI's verdict on each fund's direction, weighed
         against the wider market from Opal's own data
         DONE WHEN  EXERCISED -- for every rival and both Opal funds (never
                    a benchmark) Andrew reads a second account, written after
                    and building on the 30-day account: whether the rankings
                    and trends are borne out, contradicted or added to, given
                    whether the manager trades by system or by discretion (the
                    FWD-10 read); what the manager is getting right and wrong;
                    what it expects the manager to do next and what would prove
                    that wrong; it draws on Opal's own market readings (the fear
                    and greed measures he named, global RSI, the news scanner,
                    the trending topics and Data Harvest) before anything outside
         ACCEPT     each market reading it uses shows the date it was taken; a
                    stale reading is never turned into a trend; a later account
                    never rewrites an earlier one; a benchmark has no such
                    section
         SOURCE     backend brief O6, O7, O8; transcript 1 point three;
                    transcript 2 prompt two ("corroborate, refute, or
                    otherwise enrich", "cached ... run one after another")

  FWD-18 (NEW) The page reads as a presentation, not an audit log
         DONE WHEN  EXERCISED -- Andrew reads the rankings, the buying trend and
                    the AI accounts first, without scrolling past trade-by-trade
                    detail, holdings lists or check tables; those stay one step
                    away, and the dated archive stays
         ACCEPT     Andrew can answer "where has this manager been winning and
                    losing this quarter" from the first screen; a section with
                    missing or failed data says so in its own place
         SOURCE     frontend brief O5, O7; transcript 1 ("more of an audit log
                    than a presentation", "scrolling from miles")

  FWD-19 (NEW) The page looks and behaves like the Opal portal
         DONE WHEN  EXERCISED -- a rendered page read side by side with the
                    portal: the same card style, the same period switch in the
                    order month, quarter, year, and the same light background;
                    a fund picker lists each Opal fund with its rivals and its
                    benchmark
         ACCEPT     someone used to the portal reads the page as part of it;
                    switching the period or the fund changes the tables and
                    nothing else
         SOURCE     frontend brief O2, O6; transcript 2 ("You should not be
                    reinventing the wheel", "philosophy fixture cards",
                    "a little dropdown")

  FWD-20 (NEW) Every price, sector and market reading the rankings and the AI
         need arrives each trading morning with nobody fetching it
         DONE WHEN  EXERCISED -- over several consecutive trading days, every
                    held security's price and sector, both benchmarks and every
                    market reading the AI uses arrive on schedule
         ACCEPT     Andrew does nothing by hand; an input that did not arrive is
                    named on the page, never silently skipped
         SOURCE     backend brief O9; transcript 1 ("locked in bronze
                    ingestion for all relevant funds", "the operations as well")

  CTO RULINGS ON THE BRIEFS' OPEN POINTS (Andrew may overrule any):
  - The fund picker shows one fund at a time, grouped under its Opal fund, and
    opens on IDVZ.
  - The period and fund switches are built so that the page keeps working with
    no scripts, as it does today. The page's no-script rule stands.
  - The AI reads Opal's own data FIRST: the news scanner and Data Harvest, then the
    sentiment measures. Web search is AUTHORISED as a fallback (Andrew 2026-10-02 ~02:2xZ:
    "Web search is ok, but shouldnt really be necessary"), used only where the internal
    sources hold nothing for the question, and every web read is labelled as such.
  - "Concentration of the market" is read as the stored strength measure (52-week
    highs vs lows) and "breadth" as the breadth measure. The AI names each by its
    stored name, so Andrew can correct the mapping from one output (v0.10).
```

## CONTRACTS

**C-SEPARATE-PIPELINE.** `etfs-rivalfunds-daily` is its own pipeline. It never reads, extends or migrates `etfs-netassets-daily`,
and it never touches the client-ownership products already in `opal-data-etfs` or the bucket's existing tier-first keys
(`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`). Andrew, gap-pass item 1: *"This is a separate function ... conflating the
two would be messy."*

**C-HOMES (builder output, `lib/opal_naming.py address()` at the landed registry @`d451070fb1`; nothing here is typed).**

| tier | builder output |
|---|---|
| issuer bronze | `s3://opal-data-etfs/issuer-site/etfs/bronze/holdings/date=<D>` |
| Bloomberg bronze | `s3://opal-data-etfs/bloomberg/etfs/bronze/holdings/date=<D>` |
| issuer silver | `s3://opal-data-etfs/issuer-site/etfs/silver/holdings/date=<D>` |
| Bloomberg silver | `s3://opal-data-etfs/bloomberg/etfs/silver/holdings/date=<D>` |
| gold, the master shape | `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<D>` |
| gold, the trade schedule | `s3://opal-data-etfs/rivalfunds/etfs/gold/trade_schedule/date=<D>` |
| platinum, the served page by day | `s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=<D>` |
| run state and batch-complete markers | `s3://opal-data-etfs/rivalfunds/etfs/state/<stage>/date=<D>` |

Every other gold table is `address('rivalfunds','etfs','gold','<table>', ...)`. A builder REFUSAL is a missing registry row to add
(`infra/logic/registry/`), never a hand-typed key (CLAUDE.md rule 30).

**C-NAMES (builder output, `lib/opal_naming.py name()`, graded CONFORMANT).**
- `etfs-rivalfunds-daily`, from `name('etfs', None, 'rivalfunds', 'daily')`: the daily schedule and event rule.
- `etfs-rivalfunds-daily-lambda`, from `name('etfs', None, 'rivalfunds', 'lambda', 'daily')`.
- `etfs-rivalfunds-fetch-holdings-lambda`, from `name('etfs', None, 'rivalfunds', 'lambda', 'fetch-holdings')`.
- `rivalfunds-build-canonical-shape-lambda`, from `name('rivalfunds', None, 'build-canonical-shape', 'lambda')`.
- `rivalfunds-publish-page-lambda`, from `name('rivalfunds', None, 'publish-page', 'lambda')`.

- Further stage resources are named by `name()` when a cell names them.

**C-SOURCE-POLICY (brief S1; Andrew items 9 and 7).**
- **Issuer-first:** the issuer collector runs at 7:00 AM ET from AWS.
- **Bloomberg fallback:** the existing 8:03 AM ET morning run requests only funds still uncovered that Bloomberg carries. A
  covered fund records a skip. GQGU has no Bloomberg fallback, and the page says so on a GQGU miss.
- **Backfill, ad hoc from the outset:** issuer archives for GQGU and BASG; Bloomberg Excel BQL for WCMG, TSEL, ETFT and PCLG.
  A backfill is QA-class data landing, not production evidence.

**C-VENDOR (Andrew 2026-09-30, answers 2 and 3).**
- **Bloomberg pulls run under R-21 @`b390c36444`, scripted only:** the backfill script, the 8:03 fallback leg, and the dividend
  and price enrichment. No agent-turn call, ever.
- **No Bloomberg support correspondence.** The unattended-Excel route stays: *"im fine with 'fragile', just need to run the
  tests and see how it goes day over day."*
- **OpenAI writes the analyses** (Andrew, gap-pass item 4), from computed tables only.

**C-SHAPES.**
- Bronze keeps each channel's bytes as obtained, with a metadata sidecar (capture time, claimed report date, date evidence,
  hash).
- Silver is typed, deduplicated Parquet, one shape per source, keeping every source column and row, dated by REPORT date.
- Gold `canonical_shape` is the one Opal-defined master shape coalescing every silver shape, with every disclosed position.
  **Cash, derivatives and unidentified positions stay visible.** A raw field the master shape has no column for yet is kept.
- An undated payload stays in bronze with a status. It never acquires a guessed report date.
- **`canonical_shape` carries, per position, Opal's classification and the GICS hierarchy as SEPARATE fields**, per the
  supporting spec `GOLD_TABLES_AND_PROMPTS.md:88-97`:
  - Opal's classification: `asset_class` and `sub_asset_class`;
  - the GICS hierarchy: sector, industry group, industry and sub-industry;
  - each field with its source and as-of date.

  Andrew's L1 point 3: *"a denormalized base table with all info that we'd want. Every holding, every sub asset class and GICS
  industry tag in fields, anything we can get, put it all in there."* **A finer GICS level (industry group, industry, sub-industry) never stands in for a sub-asset class; for an equity row the `sub_asset_class` IS its GICS sector, per the ratified vocabulary (`etf_positioning_gold.py` `SUB_ASSET_CLASS_VOCAB`), both fields carried and agreeing by construction** (v0.7, CTO ruling on row ETFS_RIVALS-Z-S1, round-2 analysis ruling 5)
  (the spec's own `:97` warning, and the grain defect DSGN_AMGTV1 rounds 8-9 fixed). A value that cannot be resolved is
  carried with a status, never guessed.

**C-TRADE-SCHEDULE (the foundation; brief rev 3 O5, S6; feasibility probe).** For each fund and each pair of consecutive
GENUINELY dated reports, over securities matched by RESOLVED identity (`lib/research/identity/`) with corporate actions applied:
- the window's flow factor `f` = the median of `q_t / q_{t-1}`;
- discretionary shares = `q_t - f * q_{t-1}`;
- a trade is a residual of at least **0.2% of prior shares** (Andrew: *"Trades can be 0.2% or more, not 0.5%"*), plus every
  entry and exit.

Each trade carries:
- its window (prior report date, report date];
- an estimated price: the issuer's implied close, with the Bloomberg day range as the band;
- a notional and a confidence.

It is never placed on a day finer than its window. An identifier change or corporate action never reads as an entry plus an
exit. Dividends enter from Bloomberg's per-holding dividend calendar (Andrew). The per-issuer trade-date lag (T vs T-1) is
measured before any single trade date is stated.

**C-ONE-SIGNAL (brief rev 3 Part III).** *"one really, really clear signal on competitive intelligence"*: the page LEADS with what
each rival traded and what that says about its process. **A gold table that no page view or prompt consumes is not built.** The
S5 tables beyond `canonical_shape` and `trade_schedule` enter only when a cell names their consumer.

**C-AI-GROUNDING (brief S6 "deterministic before AI", S7).**
- Prices, returns, ranks and numeric changes are computed by table producers.
- The model explains; it never calculates.
- Every figure in AI text cites a versioned table row, and the pre-publish check fails a figure that does not match its row.
- A saved hypothesis is later graded against newer trades, and a grading never rewrites it.
- The model and prompt versions and the input manifest are stored beside the page.

**C-TRIGGERS (brief S9, approved by Andrew: *"S9 looks fine"*).**
- Each stage writes a batch-complete marker, and the next stage fires on it. Silver is event-triggered (R10).
- The bucket carries ONE notification configuration and it gets ONE owner, this pipeline. The configuration is empty today.
- A daily scheduled sweep after the Bloomberg window runs any stage whose input marker has no output marker, then publishes
  the day's page. The page says so when nothing new arrived.
- **The chain is scheduled, never success-of-upstream alone** (CLAUDE.md). The scheduled fire is the acceptance.

**C-GUARDRAILS (brief S9; Andrew item 10).**
- The publisher runs, before writing the served file:
  - report-date freshness;
  - content repeat;
  - completeness;
  - identity coverage;
  - analysis grounding;
  - render and read-back.
- A failed check either publishes the page with the affected fund marked "not updated" and the reason, or publishes nothing.
  It never publishes a quietly wrong page.
- **The thresholds are set from the first days of real data by a named cell**, never guessed in this PRD.

**C-SERVING (brief S9; Andrew items 4 and answer 4).**
- The page is written by day to the platinum prefix, read back before success is reported, and never overwritten silently.
- The gateway gains `/rivalfunds`, `/rivalfunds/<day>` and `/rivalfunds/archive`, modelled on `sprint_view.py`, with a read grant
  scoped to that prefix.
- **Viewers: any signed-in account** (*"any signed in account"*).

**C-NO-NOTIFIER.** No alert, monitor or freshness checker is built (the standing moratorium). A failed guardrail is carried by the
page itself.

**C-PEER-GROUPS (Addendum A; Andrew points 1-3).**
- The universe is a set of peer groups, one per Opal fund, each containing the Opal fund itself:
  - IDVZ: IDVZ, TXUE, BIDD, CGIC, INEQ, SCHY;
  - PFOE: PFOE, WCMG, GQGU, TSEL, BASG, ETFT, PCLG.
- **Storage stays flat, keyed by fund; grouping is a mapping** (`peer_group_map`, below). A fund in two groups is stored once. A new
  group is a mapping entry, never code (FWD-12).
- **Source policy is per fund**, a field of the mapping (supersedes C-SOURCE-POLICY's single rule):
  - `bloomberg_primary`: the IDVZ group;
  - `issuer_first`: the PFOE group, as C-SOURCE-POLICY states.
- **Index controls (v0.8, Andrew-direct 2026-10-01 ~18:2xZ, record @`19c5277a57`: "Use Russel 2000 for PFOE, ACWI for IDVZ";
  "Dont need peer selection criteria, those are pre-decided by the asset management team").**
  - Each group carries ONE `index_control` entry in `peer_group_map`:
    - the IDVZ group: **ACWI** (iShares MSCI ACWI ETF);
    - the PFOE group: **IWM** (iShares Russell 2000 ETF). Andrew named the Russell 2000 index, and the style control reads a
      listed fund's published holdings, so the instrument is the index's largest listed tracker.
  - **Both controls are `bloomberg_primary`.**
  - **SCHY stays a member of the IDVZ group**, because the asset management team set the group, but it is no longer that
    group's `index_control`.
  - Every control is a mapping entry, never code (FWD-12).
  - The peer sets are the asset management team's and are not re-derived. No selection criterion is written.

**C-HOME-PRODUCER (one writer per fund's holdings).** IDVZ and PFOE are already pulled by
`integrations/bloomberg/pipeline/etf_constituents_pull.py`.
- The first Addendum-A cell MEASURES that producer's output against FWD-2/3's grain: daily, share counts, and history depth.
- If it meets the grain, this pipeline READS it into silver as a named source.
- **(v0.5, Andrew-direct 2026-09-30 ~21:0xZ: "1b", on `3.0.0_SA_CVO~Z`'s v0.4 refusal (b); ~20:2xZ: "we're leaving the
  existing pull alone")** For IDVZ and PFOE, this pipeline READS the Positioning pull's landing as a named source. It lands no
  second copy.
  - The Positioning pull is not modified.
  - The grain shortfall RIV-m-1 measured is a stated LIMIT on FWD-2/3 for the home funds, never engineered around:
    capture-forward from 2026-08-21, 22 of 27 days. Missing days read ABSENT with their cause.
  - IDVZ and PFOE leave this pipeline's Bloomberg request.
- **Never two producers of one fund's holdings** (CLAUDE.md, no duplicate output path). This stands; v0.4's striking of it is
  withdrawn.
- **SUPERSEDED IN PART by v0.8 (Andrew-direct 2026-10-01 ~18:2xZ, record @`19c5277a57`, VERBATIM: "We should be able to pull all
  this through the same bloomberg methodology that we do for all the other bbg-data pulls for the rivalfunds. Just add them to
  the same queue on the job that does that.").**
  - IDVZ and PFOE JOIN this pipeline's Bloomberg request (`rivalfunds.collector_bloomberg`, the box task's
    `:rivalfunds_bbg_leg`). They join on the daily queue AND its history backfill to each fund's launch, because "the same
    queue on the job" is the daily job.
  - **One producer per fund inside this pipeline.** The Bloomberg leg becomes IDVZ's and PFOE's ONE producer here, and this
    pipeline stops reading the Positioning landing for them.
    - The read of `positioning-landing:constituents_issuer_fill` retires, and the `home_producer` source with it.
    - The RIV-m-1 grain limit lifts, along with its "capture-forward from 2026-08-21" bound.
    - Rows already served keep their `source_channel`, because history is never rewritten in place. The replay writes new
      revisions under a pair.
  - **The Positioning pull is still not modified** (Andrew 2026-09-30, "leave the existing pull alone"; "Anything ... additive").
    This pipeline neither reads it nor writes it.
  - Both the Positioning pull and this leg request the two funds from Bloomberg. **They serve two data shapes for two use
    cases**, so this is not two producers of one shape. Andrew-direct ~18:3xZ, VERBATIM: "We have two different data shapes
    needed for IDVZ and PFOE. On one side there is the existing Positioning page shape. That should not be touched at all.
    Now, there is a rivalfunds angle. This is separate for separate use case." The second request is admitted for IDVZ and
    PFOE ONLY, on that word. It is not a general rule that a second shape licenses a second producer. Any other fund or
    surface needs its own word from Andrew.
  - **Bloomberg budget:** before the first scheduled fire with the four new names (IDVZ, PFOE, ACWI, IWM), the issuer
    measures the leg's request cost per `integrations/bloomberg/READ_HERE.md`. A measured breach STOPs and is rowed, and no
    name is silently dropped.

**C-INCOME-CLEAN (Addendum A FWD-5; Andrew: "did we already account for dividend/interest income? That should be covered").**
- Before any residual reads as a trade, trade inference:
  1. excludes cash and currency lines from the position set;
  2. applies corporate actions from `corporate_actions` (splits, bonus issues, spinoffs, stock dividends, rights issues);
  3. reconciles income: dividend and interest receipts and their currency conversion.
- What is removed is RECORDED in `flow_reconciliation`, never discarded.
- A purchase whose funding the cash cross-check attributes to income is a trade, labelled `income_funded`.

**C-GOLD-MODEL (Andrew-direct 2026-09-30 ~15:5xZ: "establish in detail what the gold table structure is, and how that table
structure feeds these served insight deliverables").**

Every gold table's home is `address('rivalfunds','etfs','gold','<table>', 'date=<D>')`, and all 14 below were generated by the
builder at v0.3. Every table:
- is Parquet, never-overwrite, one revision per write;
- carries `revision`, `produced_at`, `producer_version` and `input_manifest` (the upstream revisions read);
- **carries its claim** on every derived value (`claim` in {MEASURED, INFERRED}, with `confidence` on INFERRED values;
  CLAUDE.md "a value must carry its claim").
**No table is built without a named consumer in the lineage matrix** (`C-ONE-SIGNAL`).

**The tables:**

| # | table | grain (one row per) | key | columns | claim | producer / trigger |
|---|---|---|---|---|---|---|
| G0 | `peer_group_map` | group x fund x mapping version | (group_id, fund_id, map_version) | group_id, home_fund_id, fund_id, ticker, role {home, rival, index_control}, source_policy {bloomberg_primary, issuer_first}, effective_from, map_version | MEASURED (a declared mapping) | a mapping change under a pair; read by every stage |
| G1 | `canonical_shape` | fund x report date x position | (fund_id, report_date, position_id) | as C-SHAPES, plus is_cash_line, source_used {issuer, bloomberg, home_producer}, corporate_action_adjusted | MEASURED (published holdings) | on silver's batch-complete marker |
| G2 | `holdings_coverage` | fund x expected report date x source | (fund_id, expected_date, source) | actual_report_date, status {new, repeat, gap, periodic}, row_count, weight_sum, selected, selection_reason | MEASURED | after G1 |
| G3 | `corporate_actions` | security x event | (security_id, event_type, ex_date) | event_type {cash_div, interest, split, bonus, spinoff, stock_div, rights}, ratio, amount, currency, pay_date, source (DVD_HIST_ALL), as_of | MEASURED | scripted Bloomberg enrichment (R-21) |
| G4 | `security_market` | security x trading date | (security_id, date) | px_close, total_return_index, currency, gics_sector, gics_industry_group, source, as_of | MEASURED | scripted Bloomberg enrichment (R-21) |
| G5 | `trade_schedule` | fund x security x trade window | (fund_id, security_id, window_end) | window_start, window_end, action {entry, add, trim, exit}, shares_delta, flow_factor_f, discretionary_shares, residual_pct_prior, est_price, price_band_lo, price_band_hi, est_notional_base, income_funded, corporate_action_ref, confidence | INFERRED | after G1 and G3 (C-TRADE-SCHEDULE, C-INCOME-CLEAN) |
| G6 | `flow_reconciliation` | fund x trade window | (fund_id, window_end) | flow_factor_f, cash_line_delta_base, income_received_base, fx_conversion_base, corporate_action_count, income_funded_trade_count, unexplained_residual_base | MEASURED inputs, INFERRED residual | with G5 |
| G7 | `trade_outcomes` | trade x horizon | (fund_id, security_id, window_end, horizon_td) | horizon_td {21, 63, 126}, fwd_security_tr, fwd_benchmark_tr (the fund's own holdings-weighted book), excess_tr, outcome {helped, hurt, flat}, price_coverage {full, partial, missing} | MEASURED returns, INFERRED attribution | after G5 and G4 |
| G8 | `outcome_rollup` | fund x period x axis x bucket | (fund_id, period, axis {sector, security}, bucket) | n_trades, n_missing, hit_rate, mean_excess, sum_notional_base, window, denominator | INFERRED | after G7 |
| G9 | `style_read` | fund x research window | (fund_id, window_end) | **the gate (v0.6, `4.0.0_SA_CRO~Z` style-read preview @9fc7430875):** peak_book_share_days (every report pair touching at least 50% of the book, with dates) and recurrence (those days fall on a quarterly or monthly calendar grid, at least 3 occurrences across at least 2 years); label systematic when recurrence holds, discretionary when trading is present without it, undetermined below the minimum history. Descriptive context, not the gate: timing_concentration (share of trade notional in the top 4 weeks), reconstitution_share, breadth, median_trade_size_pct, trade_count. label {discretionary, systematic, undetermined}, control_passed (the group's `index_control` must read systematic: ACWI for IDVZ, IWM for PFOE, v0.8) | INFERRED | after G5; the label shows only when control_passed |
| G10 | `trend_projection` | fund x axis x bucket x horizon | (fund_id, axis, bucket, horizon) | trailing_net_flow_base (3 windows), direction {accumulating, reducing, flat}, persistence, projected_direction, falsifier (deterministic template), confidence | INFERRED | after G5 |
| G11 | `peer_comparison` | group x fund x measure x period | (group_id, fund_id, measure, period) | value, rank_in_group, group_median, is_home | INFERRED (from G8-G10) | after G8-G10 |
| G12 | `research_hypotheses` | fund x analysis run x item | (fund_id, run_id, item_id) | kind {projection_note, wildcard, process_account}, text, cited_rows (table, key, revision), invalidation, model_version, prompt_version | INFERRED (AI) | the analysis step, after G8-G11 |
| G13 | `hypothesis_grades` | hypothesis x grading run | (fund_id, run_id, item_id, graded_at) | graded_against_window, verdict {held, broke, undetermined}, evidence_rows | INFERRED; append-only, never rewrites G12 | a later analysis run |

**The lineage matrix (every served insight -> the tables it reads -> what is deterministic, and what is AI):**

| served insight | outcome | reads (tables and columns) | deterministic | AI (the prompt reads ONLY these) |
|---|---|---|---|---|
| peer-group page, both groups | FWD-1, FWD-11 | G0 (members, roles); G11; the header from G1 | group layout, ranks, home fund highlighted | none |
| history and freshness | FWD-2 | G2 status per fund-day | new/repeat/gap calendar | none |
| source per fund per day | FWD-3 | G0.source_policy; G2.selected and selection_reason; G1.source_used | the source badge | none |
| master shape side by side | FWD-4 | G1 | the position tables | none |
| trade schedule | FWD-5 | G5; G6 (income, cash, corporate actions); G3.event_type | trade list, income-funded label, excluded-event count | P1 (activity summary) reads G5, G6 |
| helped or hurt, by sector and security | FWD-6 | G7, G8; G4 for price coverage | rollups with window and denominator; missing counted | P2 reads G8, G7 |
| projected trading | FWD-7a | G10 | direction, persistence, falsifier | P3 reads G10, G9, G5 (explains, never calculates) |
| wildcard | FWD-7b | G12 (kind = wildcard), with G5-G11 as its citable rows | the citation check (every figure matches its cited row) | P4 reads G5-G11 and writes G12 |
| later grading | FWD-7 | G12, G13, newer G5 | the grading window | P3/P4 grade into G13 |
| style read | FWD-10 | G9 with control_passed | metrics and the label gate | P3 may explain G9 |
| home vs rivals | FWD-11 | G11 (is_home) with G8, G9, G10 | the same measures for all funds | P4 reads G11 |
| rebuild and no-duplicate rerun | FWD-8 | every table's input_manifest and revision | the replay | none |
| guardrails | FWD-9 | G2, G1, G12 citations | the C-GUARDRAILS checks | none |

- **The prompts are the supporting spec's P0-P4** (`GOLD_TABLES_AND_PROMPTS.md` S7), each restricted to the tables its row names.
- **An AI figure that does not match its cited row fails the analysis-grounding guardrail** (C-AI-GROUNDING).
- **Horizons (21/63/126 trading days), the 4-week timing window and the 3-window trend are starting values.** A named cell re-sets
  each from the first real data, never silently.
- The spec's S5 tables not listed here (`fund_snapshot`, `holdings_changes`, `allocation_changes`, `holding_performance`,
  `performance_rankings`, `manager_behavior`) are NOT built until a served insight names them (C-ONE-SIGNAL). `trade_outcomes`,
  `style_read` and `trend_projection` are this model's narrower versions of `decision_evaluation` and `manager_behavior`.

## THE THREAD (FWD-1) -- round 1 builds it end to end, for BASG

One person: Andrew. One journey, live, for **BASG** (the brief's O1 candidate; its issuer archive has daily history since
2025-06-13). Each hop is a real call; a hop fed by a fixture fails FWD-1.

1. **H1 homes:** the addresses above exist as builder output. The registry change is landed.
2. **H2 backfill:** BASG's issuer archive lands in issuer bronze through the collector, with the raw bytes and the sidecar. This
   is a served write under a never-widen pair.
3. **H3 silver:** typed BASG silver from that bronze, fired by the bronze marker, or by replay for the backfill.
4. **H4 gold:** `canonical_shape` for BASG, then `trade_schedule` for BASG, identity resolved through the layer.
5. **H5 page:** the publisher renders BASG's latest trades first, with the trade traced back through its two reports to the
   issuer bytes. It writes the day's page to platinum with read-back, and the gateway serves `/rivalfunds` and
   `/rivalfunds/archive`.
6. **H7 guardrails:** the pre-publish checks run before the write. A planted failure publishes a "not updated" page.
7. **H6 daily:** `etfs-rivalfunds-daily` fires the issuer collector at 7:00 ET from AWS. **The first test is AWS reachability of
   BASG's issuer site** (Andrew item 11).

A build cell carries at most THREE mechanical criteria; repo-wide hygiene runs at the drain. The round-1 analysis ends in the
enrichment list.

## ENRICHMENT BACKLOG (off the thread, in order)

- The other five funds through both channels.
- FWD-2: the coverage view, and the inception vs first-source distinction.
- FWD-3: several consecutive trading days live, the Bloomberg fallback, and the GQGU miss stated.
- FWD-4: side-by-side funds in the master shape.
- FWD-5 for all six, with the trade-date lag measured per issuer.
- FWD-6: `decision_evaluation` over the trade schedule.
- FWD-7: `manager_behavior` and the saved-and-graded hypotheses.
- FWD-8: a rebuild from raw files and the no-duplicate rerun.
- FWD-9: each guardrail exercised on a planted failure.
- The guardrail thresholds from the first days of real data.
- The unattended-Excel validation for the Bloomberg leg, run as day-over-day tests (Andrew, answer 3).

## PATHS (the write surface)

**Owned:**
- a new collector package and stage producers for this pipeline, homed by the repository's language conventions (named by the
  decomposition);
- the Lambda and schedule Terraform for the five names above;
- the gateway route module for `/rivalfunds` and its grant;
- the Bloomberg holdings leg added to the existing morning vehicle as a SCOPED new leg, which touches no other leg's status.

**Read, never edited:** `lib/research/identity/**` (resolution through its public API; a new name registers through
`add_security`'s scripted path), `lib/trading_calendar.py`, `data/etfs/scripts/gold/etf_positioning_gold.py` (the vocabulary),
the `/sprint` precedent files.

**Never:** `etfs-netassets-daily` and its homes, the bucket's existing tier-first keys, any client-ownership product,
`opal-data-assets`.

## FIXTURES AND EVIDENCE

- The trace for FWD-1 is live: a signed-in read of `/rivalfunds` for BASG.
- Every served write (bronze, silver, gold, platinum, the notification configuration, the gateway grant) goes under a
  never-widen pair and a NEVER-2 entry, with its expected diff read from the producer's rule at signing.
- The CVO grades JUDGMENT criteria at L9, citing the contract clause.

## PROVENANCE AND AMENDMENT HISTORY

- v0.10 (2026-10-02, `1.0.0_SA_CTO~Z`), on Andrew's release (record `ANDREW_DIRECT_20261002_022xZ_RIVALFUNDS_ADDENDUM_B_RELEASED_DRIVE_NOW.md`):
  - Addendum B (FWD-13..20) is CONFIRMED.
  - FWD-14 is ruled CONTRIBUTION.
  - "Concentration" is mapped to the stored strength measure.
  - Web search is authorised as a labelled fallback, after the news scanner and Data Harvest.
  - This is an ENDPOINT change, so the ratified half re-opens to `3.0.0_SA_CVO~Z`.

- v0.9 (2026-10-01, `1.0.0_SA_CTO~Z`), `/endpoint --forward` on `4.0.0_SA_CRO~RV`'s two briefs (msg 28050, record @`52eb8a5dc7`):
  - The ENDPOINT gains **Addendum B, FWD-13..20, PROPOSED** and awaiting Andrew's confirmation.
  - **Read:**
    - the two briefs (18,838 and 12,827 bytes);
    - this PRD's ENDPOINT.
  - **NOT READ:** the task-order register, the round-4/5 decomposition, and the project JSON (Phase 0 reads the brief only).
  - No CONTRACT changes yet. Contracts follow confirmation, and then the ratified half re-opens to `3.0.0_SA_CVO~Z`.

- v0.8 (2026-10-01, `1.0.0_SA_CTO~Z`), on Andrew's three answers to `4.0.0_SA_CRO~RV`'s closer trace (record @`19c5277a57`, brief
  @`381bec5549`):
  - C-HOME-PRODUCER is superseded in part: IDVZ and PFOE join the Bloomberg leg, daily and backfill, as the one producer
    inside this pipeline, and the Positioning pull is untouched.
  - C-PEER-GROUPS gains the index controls (ACWI for IDVZ, IWM for PFOE), with SCHY a member but no longer the control.
    No selection criterion is written.
  - FWD-10's control and G9's `control_passed` follow.
  - The hop-9 method rulings are recorded separately (`ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` @`4baf852611`).
  - This is an ENDPOINT (FWD-10) and CONTRACTS change. Andrew's word names the controls, so the ratified half re-opens to
    `3.0.0_SA_CVO~Z`.
  - Round 4 (d-5) finishes as cut. These are round-5 cells.

- v0.7 (2026-10-01, `1.0.0_SA_CTO~Z`), the round-2 analysis ruling 5 on row ETFS_RIVALS-Z-S1:
  - the C-SHAPES classification bullet now follows the ratified vocabulary the PRD names. For an equity row,
    `sub_asset_class` IS its GICS sector, and a finer GICS level never stands in for a sub-asset class.
  - This is a CONTRACTS change with no ENDPOINT change, so the ratified half re-opens to `3.0.0_SA_CVO~Z`.
- v0.3 (2026-09-30, `1.0.0_SA_CTO~Z`): **Addendum A.**
  - The ENDPOINT gains the peer groups: FWD-1/2/3/5/6/7 amended, FWD-10/11/12 new. Andrew confirmed it via `4.0.0_SA_CRO~Z`
    (msg 27241, record @`2bc18b60a5`), with FWD-1 covering both Opal ETFs.
  - CONTRACTS gain C-PEER-GROUPS, C-HOME-PRODUCER, C-INCOME-CLEAN and **C-GOLD-MODEL** (Andrew-direct ~15:5xZ, record @`fdc881a489`).
  - The endpoint lines landed @`5bababb75b`; that commit's message named C-GOLD-MODEL, which it did not yet carry. The
    contracts land in the next commit.
  - This is an ENDPOINT and CONTRACTS change, so the ratified half re-opens to `3.0.0_SA_CVO~Z`.
- v0.2 (2026-09-30, `1.0.0_SA_CTO~Z`), on `3.0.0_SA_CVO~Z`'s ratified-text REFUSE @`2506e39cee`:
  - C-SHAPES gains the classification bullet (Opal asset/sub-asset class and the GICS hierarchy as separate fields,
    Andrew's L1 point 3);
  - the brief-name correction note moves here out of CONTRACTS.
  - No ENDPOINT change.
- **The brief-name correction (moved from C-NAMES):**
  - The brief listed `rivalfunds-etfs-build-canonical-shape-lambda` and `rivalfunds-etfs-publish-page-lambda`.
  - `grade()` passes both as CONFORMANT, but `name()` cannot produce them: it refuses scope `etfs` in that slot ("a PRODUCT
    scope; this slot takes FIRM/GLOBAL/MASTER").
  - C-NAMES uses the builder's output, and the grader-builder disagreement is an LGIC finding for its owner.
  - The CRO restaged the brief's names to `name()` output @`9d550730e2`.
- v0.1 (2026-09-30, `1.0.0_SA_CTO~Z`):
  - the ENDPOINT landed verbatim from @`33c1d096a3`, approved by Andrew ("1.) Yes approved.");
  - the CONTRACTS come from brief rev 3 Parts II-V, supporting spec S1-S9, the feasibility probe, and Andrew's rulings
    (gap-pass items 1-14, the five answers, the S9 approval, the 0.2% floor, dividends);
  - addresses and names are builder output, generated by this seat. The brief's two `rivalfunds-etfs-*` names are corrected
    to `name()`'s output.

## SURFACE MANIFEST

**WRITES:**
- `opal-data-etfs`: the eight builder prefixes above;
- the bucket's notification configuration (one owner);
- the five named resources;
- the gateway's `/rivalfunds` route and grant.

**READS:**
- the issuer sites (from AWS);
- Bloomberg through the morning vehicle's Excel BQL (scripted, R-21);
- the identity layer;
- the trading calendar;
- the ETF positioning vocabulary;
- OpenAI for the analyses.

**NEVER:**
- `etfs-netassets-daily`;
- `opal-data-assets`;
- the bucket's other products and prefixes;
- any agent-turn vendor call;
- any notifier.
