# ETFS_RIVALS -- Rival funds: daily holdings of six rival active ETFs, each fund's trade schedule, and a served research page

```json
{
 "project": "ETFS_RIVALS",
 "directive": "D5",
 "fabric": "dell1",
 "prd_version": "v0.21",
 "step": 4,
 "brief_ref": "docs/briefs/etf-holdings-research-20260929.md@77c891c869",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13", "FWD-14", "FWD-15", "FWD-16", "FWD-17", "FWD-18", "FWD-19", "FWD-20", "FWD-21", "FWD-22", "FWD-23", "FWD-24"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~Z` (L4), 2026-09-30.
**Brief:** `4.0.0_SA_CRO~Z`, revision 3 (trade schedule as the foundation), with the supporting specification
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md` and the feasibility probe
`TRADE_INFERENCE_FEASIBILITY.md` in the same folder.
**Andrew's words:** every word this PRD rests on is verbatim in that folder's `ANDREW_DIRECT.md`.
**Registered** @`ec6f31261c` (D4/ETFS), **moved to D5/ETFS** on Andrew's word (record `ANDREW_DIRECT_20260930_063xZ_ETFS_INCLUDED_IN_D5_MACROS_ETFS_RIVALS_TO_D5.md`), fabric site-z. **COO:** `2.0.0_SA_COO~RV`, seated by 0.0.0_AB_MSTR~Z (msg 26952).
**CVO:** `3.0.0_SA_CVO~RV` (since Andrew-direct 2026-10-07 ~05:30Z; before that `3.0.0_SA_CVO~Z`). **CRO:** `4.0.0_SA_CRO~Z`.
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
         and worst over the last 30 trading days and this quarter and year,
         then picks one rival and reads its rankings, its buying trend
         and the AI's account of it
         DONE WHEN  EXERCISED -- one live, signed-in read: the page opens on
                    IDVZ's ranking for the last 30 trading days (v0.14); Andrew
                    switches to quarter- and year-to-date (v0.15: no
                    month-to-date) and the tables change; he
                    picks one IDVZ rival and reads its ten best and ten worst
                    holdings, five best and five worst sectors, its buying
                    trend for the same period and the AI's two-part account;
                    he follows one
                    ranked figure back to the holdings and prices it came from
         ACCEPT     everything he reads comes from that morning's real run; a
                    figure built from sample data fails the outcome
         SOURCE     backend brief O1; frontend brief O1; transcript 2
                    ("default to IDVZ", "toggle MTD, QTD, YTD")

  FWD-14 (NEW) Andrew ranks any fund's best and worst holdings and sectors for
         the last 30 trading days and the quarter and year to date (v0.15), by
         the same rules for every fund
         DONE WHEN  EXERCISED -- for every fund in both groups, Opal's own and
                    each group's benchmark included, Andrew reads the ten
                    holdings that added most to the fund's return and the ten
                    that cost it most, and the five best and five worst sectors,
                    for each of the three periods (v0.15: 30 trading days,
                    quarter to date, year to date)
         ACCEPT     a figure Andrew checks agrees with what that fund's holdings
                    and their prices add up to over the period; each table says
                    which period, its first and last trading day, and how many
                    holdings it ranks, up front; a holding with no price shows
                    as missing, never dropped
         SOURCE     backend brief O2; transcript 1 point one; transcript 2
                    component 1
         RULED (v0.10, CTO on Andrew's release): CONTRIBUTION -- how much each
                    holding added to or took from the fund's return over the
                    period, weighted day by day by how much of it the fund held
                    (holdings rebuilt from its reports); this works for the
                    benchmarks too. The trading result stays in FWD-6.

  FWD-15 (NEW) Andrew reads each fund's tilts and bets: where its buying has
         trended over the period the page is set to, by holding and by sector
         DONE WHEN  EXERCISED -- for every fund Andrew reads a simple table,
                    over the page's period (the last 30 trading days by default,
                    v0.14), in the same shape as the rankings: the
                    ten holdings and five sectors its buying leaned into most,
                    and the ten holdings and five sectors it leaned away from
                    most, each line read as a tilt or a bet with a plain trend
                    mark
         ACCEPT     a trend is never presented as one that will continue; the
                    table states its period, its first and last trading day and
                    how many trading days it covers, up front; it never says
                    "year to date" for a window that is not year to date
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
                    portal: the same card style, the same period switch (v0.15:
                    the last 30 trading days first and selected by default, a
                    dividing line, then quarter, year; no month), and the same
                    light background; a fund picker lists each Opal fund with
                    its rivals and its benchmark; the period switch also sits
                    inside "What drove the return" and "Buying trend", and
                    switching it in any one place moves every one of them
                    together
         ACCEPT     someone used to the portal reads the page as part of it;
                    switching the period or the fund changes the tables and
                    nothing else; Andrew never has to scroll back up to change
                    the period
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

  FWD-21 (NEW, v0.16) Andrew clicks any stock named anywhere on the page and
         reads that security's holding modal with its history
         DONE WHEN  EXERCISED -- on the live page, every security named in the
                    rankings, the buying trend, the AI accounts and the detail
                    lists opens its holding modal when clicked, and the modal
                    shows the security's history (its price and the fund's
                    holding over time) as far back as the store holds it
         ACCEPT     no ticker on the page is dead text; a security whose
                    history is not yet backfilled says so in its modal, never
                    an empty chart; the page's no-script rule stands
         SOURCE     Andrew-direct 2026-10-05 ~03:3xZ at the COO~RV terminal
                    ("anytime a stock/ticker is mentioned, it should be
                    clickable to the modal, and we should be able to see
                    backfill on it")

  FWD-22 (NEW, v0.18) On a fund's security modal Andrew sees the security's
         price over time with that fund's buys and sells marked on it
         DONE WHEN  EXERCISED -- on the live page, the security modal opened
                    from a fund's section draws the security's price curve
                    for the last 30d, 90d or 365d (one switch, 30d first);
                    each of that fund's trades in the range is a hollow
                    marker on the curve, green for a purchase and red for a
                    sale, sized by the trade's share of the fund; pointing at
                    a marker reads the trade's date or window, its dollar
                    value, its size in basis points of the fund, and how many
                    trades the range holds
         ACCEPT     The modal reads as the Market Overview security modal
                    does. The largest marker is a trade of 5% of the fund or
                    more and the smallest is 20 bps or less. A trade known
                    only as a window between two reports is drawn across its
                    window, never on a guessed day. A stretch with no price
                    is a gap in the curve with its reason, never a drawn
                    line. The curve says where its prices come from.
         SOURCE     Andrew-direct 2026-10-07 ~04:5xZ at the COO~RV terminal
                    (record cooRV_ANDREW_DIRECT_20261007_045xZ_RIVALFUNDS_
                    SECURITY_MODAL_PRICE_SERIES_WITH_TRADE_MARKERS.md)
         HOVER      Pointing at any part of the curve reads that day's price
                    and date, as Market Overview does. Andrew asked for it;
                    it is part of this outcome, and FWD-22 is NOT REALIZED
                    without it.
         SCRIPT     The page may carry ONE script, for this modal's chart
                    and its any-day hover only (Andrew-direct 2026-10-07
                    ~05:2xZ: "Yes it can have script"; ADDENDUM F.7). Every
                    other part of the page still works with no script. The
                    Bloomberg backfill is answered YES (F.5).

  FWD-23 (NEW, v0.18) Every period on the page is 30d, 90d or 365d rolling
         DONE WHEN  EXERCISED -- every ranking, trend, account and modal on
                    the live page offers exactly 30d, 90d and 365d, opens on
                    30d, and shows no QTD, YTD or MTD; the QTD and YTD
                    figures are still computed and stored
         ACCEPT     90d sits where QTD sat and 365d where YTD sat. A period a
                    fund's history does not reach reads partial with its
                    reason. The AI accounts name the same three periods.
         UNIT       CALENDAR DAYS, for all three periods and the curve's
                    ranges (Andrew-direct 2026-10-07 ~05:2xZ: "let's make it
                    calendar days, we dont need that much lookback time").
                    30d, 90d and 365d each end on the page's as-of date and
                    reach back that many calendar days. This REPLACES the
                    2026-10-04 "last 30 trading days" for the 30-day period.
         AMENDS     FWD-14 and FWD-19 where they name the displayed periods
                    (30 trading days, quarter to date, year to date): the
                    displayed set is this outcome's. Nothing else in either
                    outcome changes.
         SOURCE     Andrew-direct 2026-10-07 ~04:5xZ at the COO~RV terminal
                    (record cooRV_ANDREW_DIRECT_20261007_045xZ_RIVALFUNDS_
                    PERIODS_30D_90D_365D_EVERYWHERE.md)

  FWD-24 (NEW, v0.19) Every security a tracked fund held in the last 365
         days has its year of daily closes in the store, and the daily
         sequence keeps it so without anyone running anything
         DONE WHEN  EXERCISED -- on a day's run, the sequence prints the
                    HISTORY OWED: for every security any tracked fund held
                    within the last 365 calendar days, the trading days of
                    that window with no stored close, with the denominator
                    of securities and days read; the same run asks for what
                    is owed, inside the day's budget, and carries the rest
                    to the next run; and a negative control shows it -- a
                    security planted as first traded today, with no stored
                    close, has its 365 days stored within 3 runs and the
                    owed count for it reads 0
         ACCEPT     A security a fund bought this week has a full year's
                    curve in its modal, not a curve that starts at the
                    purchase. A security a fund sold out of keeps its curve
                    current for 365 days after. A day with no close reads a
                    gap with its reason. The owed count is a number on the
                    run's record every day, and it falls.
         NOT THIS   A tracked fund's own HOLDINGS history (the collector's
                    backfill) and a fund's own share-price series. Neither
                    is asked by this outcome.
         SOURCE     Andrew-direct 2026-10-07 ~20:4xZ at the 4.0.0_SA_CRO~Z
                    terminal ("we kind of need to be storing 365d calendar
                    backfill per security AND *per tracked fund*, as those
                    securities appear in the daily transactions record ...
                    WE need a solution for that built into the ingestion
                    sequence")

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

**C-SECURITY-UNIVERSE (v0.17; the interface MDPF_SECCLASS reads, Andrew-direct ~03:3xZ items 3-4 and the 3-year cap @357e681ddf).**
- Gold `security_universe`: one row per security that any rival or Opal ETF held within the last 3 years, built from `canonical_shape`.
- Keys: `security_id`, `security_bloomberg`, `security_cusip`, `security_isin`, `security_ticker` and `security_name`, plus
  `first_seen`, `last_seen` and `funds`. `first_seen` is what lets the consumer's new-stock routine (MDPF_SECCLASS FWD-10) find
  new entries.
- Same cadence as gold (Mon-Fri ~07:10 ET, plus the 09:00 ET late sweep). Written once per as-of date, never overwritten.
- Its only consumer outside this project is MDPF_SECCLASS (laptop fabric), which reads it and never writes it. No work crosses
  fabrics. The consumer's read grant on this one prefix is the laptop's act.
- Until it lands, the interim source is `canonical_shape` (one object per report date, newest revision wins).

**C-HOMES (builder output, `lib/opal_naming.py address()` at the landed registry @`d451070fb1`; nothing here is typed).**

| tier | builder output |
|---|---|
| issuer bronze | `s3://opal-data-etfs/issuer-site/etfs/bronze/holdings/date=<D>` |
| Bloomberg bronze | `s3://opal-data-etfs/bloomberg/etfs/bronze/holdings/date=<D>` |
| issuer silver | `s3://opal-data-etfs/issuer-site/etfs/silver/holdings/date=<D>` |
| Bloomberg silver | `s3://opal-data-etfs/bloomberg/etfs/silver/holdings/date=<D>` |
| gold, the master shape | `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<D>` |
| gold, the trade schedule | `s3://opal-data-etfs/rivalfunds/etfs/gold/trade_schedule/date=<D>` |
| gold, the security universe (v0.17) | `s3://opal-data-etfs/rivalfunds/etfs/gold/security_universe/date=<D>` |
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

**C-FAST-RULINGS (v0.11).** These are the contract-level rules ruled by `4.0.0_SA_CRO~RV` during the 2026-10-02 FAST interval and
served under the A1 never-widen pair and addenda 1-11. The authoritative text of each is the ruling cited, in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`; this block lifts them into the ratified text, so the
L4-R signer reads the contract the code follows. Each value marked PROVISIONAL is a starting value that a named cell re-sets,
never silently.

- **Holding contribution: price source and priceability (CALL 1, as amended by CALLs 6, 7 and 8).**
  - **Source order:** per (security, day), the order is `g4_tri`, then `g4_close`, then `holding_implied`, else `missing`. A daily
    return uses ONE source at both endpoints.
  - **Priceable positions:** only a security holding with `quantity > 0` and a non-null `market_value` on both days is priced.
    Cash, derivatives, swaps, futures, options and forwards are `missing` with a reason. A future counts as
    `derivative_not_priced`. A zero or absent valuation is no price, never a -100% day.
  - **The guard,** with `out(x) := max(x, 1/x) > 1 + band`, `r` the price ratio, `k` the quantity ratio and `v = k x r`:
    - a day is refused `corporate_action_suspected` iff `out(r) AND out(k) AND NOT out(v)`, with band 0.25, PROVISIONAL;
    - otherwise it is refused `implausible_valuation` iff `max(r, 1/r) > 1.5` (band 0.5, PROVISIONAL), whether or not the quantity
      changed;
    - otherwise the day is priced.
  - **No gap filling.**
  - **`price_source` at row grain:** `g4_tri | g4_close | holding_implied | mixed | missing`.
  - **Disclosure:** implied returns are price-only, and the caption says so.
- **One as-of date per page (CALL 3).** `asof = prev_trading_day(page_day)` (`lib/trading_calendar.py`). There are no per-fund
  windows, and a fund short of `asof` reads `partial` with its reason. On early-month pages the caption names the prior month.
- **Refusal disclosure (CALL 6, condition 2).** `holding_contribution` carries `n_days_refused` and `refused_reasons`. The ranking
  caption states, per fund and period, the count and the reasons. The audit block lists each refused (security, day, ratio,
  reason).
- **Plausibility guard (CALL 13, C1).** A refusal is per fund x period, never the table. The refused fund-period reads
  "refused: <reason>", and the rest serve.
  - The bounds are structural:
    - (a) a period total below -100% is refused. This is a hard rule.
    - (b) one holding's absolute contribution |c| above 0.25 is refused. **The unit is contribution units: a fraction of fund NAV
      (0.25 = 25 percentage points of return), NOT a share of the fund's period total.** A fund total near zero must not refuse
      its correct rankings; for example ETFT, with TXN at +2.92% against a fund total of +0.56%. For scale: one holding at 10%
      weight tripling contributes about 0.20. Positive control: a planted single holding at 0.30 refuses. PROVISIONAL.
    - (c) where the NAV series is on file, |sum of contributions - NAV return| above a tolerance from the residual distribution
      is refused. PROVISIONAL.
  - The bounds are never drawn from the peer return distribution.
- **Bet versus tilt (CALL 4).** A line is a `bet` when its largest window carries at least 0.5 of its GROSS (the sum of
  |window net|), PROVISIONAL and inclusive. Otherwise it is a `tilt`. Sector lines apply the test to per-window sector nets.
  `buying_trend` carries `gross_notional_base` and `bet_share`.
- **Trend population (CALL 9; grade 6 G6-1).**
  - Derivative lines leave the trend.
  - A security's sector falls back to its GICS sector in any fund's file: security-keyed, `gics_sector` only, own sector first,
    date-sorted.
  - The trend row carries `sector_source` `own | other_fund | mixed`, with `mixed` at sector grain. A null means no sector,
    never `own`.
  - The ranking and the trend sector panels share ONE "Sectors not shown" rule: a panel is hidden when Unclassified exceeds 0.5 of
    its absolute sector measure.
- **Display population (CALL 12; the cash-equivalent rule of grade 2 F2).**
  - A G5 row whose shares go 0 -> 0 with no notional is not shown as a trade. It is counted per window with a note, and G5 keeps the
    row. A 0 -> 0 row with a non-zero notional is a data fault and stays visible.
  - Money-market lines leave the rankings, the trend, the trade log and the AI facts, each counted where it is hidden.
- **AI grounding (CALLs 10 and 11; extends C-AI-GROUNDING).**
  - A digit run written as a Bloomberg ticker (`6501 JP Equity`) is an identifier, not a figure. It passes only if it matches a
    security key in that fund's facts for the run; otherwise it FAILs as `unknown_identifier`.
  - A quoted ISO timestamp is a time, not figures.
  - A corrected grader **re-grades** the whole stored run, in both directions, once per grader defect. The superseded grade
    stays readable beside the new one, and no account is re-rolled.
  - A grounding FAIL is shown, not re-rolled (CALL 5).

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

### v0.12 -- the 2026-10-02 /rivalfunds UI and data walk: 33 issues, folded into `2.0.0_SA_COO~RV`'s work

**Andrew-direct ~14:1xZ**, at the `4.0.0_SA_CRO~RV` terminal, VERBATIM:
"...write a brief for listing out each issue, send to CTO with instruction that issue list must be included in their PRD and fold
it into COO~RVs existing work on ETFS_RIVALS."
- Record: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_141xZ_RIVALFUNDS_UI_WALK_BRIEF_TO_CTO_COO_RV_CANONICAL_DRIVE.md`.
- Brief: `docs/briefs/rivalfunds-ui-data-walk-20261002.md`. Register: `docs/briefs/rivalfunds-ui-data-findings-20261002.json`.
  Both are authoritative for each finding's full observation, cause and design rule. The table below is generated from the register.
- Every item serves an existing FWD, so this is enrichment work, not an ENDPOINT change. The owner of every item is `2.0.0_SA_COO~RV`.
- **Coverage gate:** `python docs/briefs/irpt-ui-review-coverage-check.py --register docs/briefs/rivalfunds-ui-data-findings-20261002.json org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`
  exits 0 only at 33/33.
- **Order:**
  1. **RFW-D01 leads.** The A1 tables on today's served page were built before the G1 refresh.
  2. Then the data items (D), because the UI items on the same panels (U02, U03 on D03; U16 on D06) read their fixed data.
  3. Then the UI items.
- **Every acceptance below is graded on the SERVED page.** Each round-6 judgment criterion names its positive control (CALL 13 C2).

| id | side | FWD | observed (first sentence; the register holds the rest) | acceptance | status |
|---|---|---|---|---|---|
| RFW-D01 | data | FWD-20, FWD-14, FWD-9 | The 2026-10-02 page (republished 14:17:10Z, batch fast-a1-publish-1002f) serves A1 tables built at 11:03-11:04Z. | When a G1 or G4 object newer than an A1 table's newest input lands, the next publish rebuilds that A1 table, or refuses to show it as current. A planted newer G1 object forces the rebuild. | new |
| RFW-D02 | data | FWD-20, FWD-2 | The page contradicts itself. | On one page the fund-current headline and the census's holdings line agree (same G1 vintage), or the page names the vintage gap. | new |
| RFW-D03 | data | FWD-14 | Month to date and quarter to date rank 0 holdings for 12 of 13 funds (every fund but BASG, which ranks 32). | v0.15: MTD is no longer served (Andrew ~02:4xZ), so the MTD limb is void; QTD keeps the rule. After RFW-D01 lands, MTD ranks at least one holding for every fund whose 09-30 and 10-01 reports are both in G1; a fund-period with no priced day shows ONE line, not four empty tables (RFW-U03). | new |
| RFW-D04 | data | FWD-20, FWD-14, FWD-6 | Inputs that did not arrive: 'Security prices: 0 of 765 arrived' and 'GICS sectors: 0 of 765 arrived'. | G4 for the as-of date carries px_close and gics_sector for at least 95% of the universe's priced holdings, and the census reads that share. | known |
| RFW-D05 | data | FWD-14, FWD-15, FWD-5, FWD-18 | For all 9 Bloomberg-sourced funds (TXUE, BIDD, CGIC, INEQ, SCHY, WCMG, TSEL, ETFT, PCLG), holdings show raw Bloomberg tickers instead of names: '8306 JP Equity', 'TTE ... | Every holding on the face shows a security name. A raw ticker appears only as secondary text, and the count of nameless holdings is 0, or each is listed in the census. | new |
| RFW-D06 | data | FWD-6, FWD-14, FWD-15 | 'Unclassified' is ranked as a sector in the YTD sector tables of 10 funds, and is the single largest sector in 6: ETFT -6.59%, BASG -3.00%, TSEL -2.93%, BIDD -2.28%, T... | MEASURED (CRO~RV GICS census @308f982bb8, sections 2-4; replaces the walk's unmeasured 10%). Unclassified is never ranked as a sector (RFW-U16), and each fund's unclassified share is printed by weight of its latest report. After fix 1 (the CALL 9 cross-fund fallback in the rankings or in G1, with `gics_source` naming the other fund's file): INEQ >= 99% and TXUE >= 89% classified, and every other fund's unclassified share is at or below its section-4 level (IDVZ 78%, WCMG 58%, ETFT 42%, GQGU 38%, PFOE 27%, TSEL 15%, PCLG 13%). After fix 2 (CUSIP-keyed GICS in the scripted G4 pull) and fix 3 (G4 at universe scale): only the 7 not-eligible lines stay unclassified. Each level is graded on the served page beside its census denominator. | new |
| RFW-D07 | data | FWD-3 | At the 14:17Z publish, 4 funds' latest report is 2026-09-30 against an expected 2026-10-01: IDVZ (home producer), BIDD, CGIC and SCHY (Bloomberg). | By the 09:00 ET sweep, every fund's report for the prior trading day is in G1, or the page names the fund as late with its reason. | new |
| RFW-D08 | data | FWD-16, FWD-17 | Every AI account reads 'Demo read: written by a seat ad-hoc run (2.0.0_SA_COO~RV, 2026-10-02T11:04:45Z), a QA-class read, not the scheduled pipeline's output.' No sche... | The scheduled chain writes research_hypotheses for the page day with no seat act, and the footer reads the scheduled run. | known |
| RFW-D09 | data | FWD-16, FWD-17, FWD-9 | 2 of 24 accounts are served as 'Grounding FAIL' (IDVZ 'The last 30 days': '$1.6 million, $1.3 million' not in any cited row; CGIC 1). | 0 accounts FAIL at the scheduled run, or each FAIL is collapsed with its reason (RFW-U10). | new |
| RFW-D10 | data | FWD-5 | A full exit shows 'n/a' for est. | A full exit is priced from the prior report's valuation (or G4), with the source shown; 0 'n/a' notional on exits. | new |
| RFW-D11 | data | FWD-14, FWD-15 | IDVZ's home-producer names are cut at 30 characters: 'Kimberly-Clark de Mexico SAB d', 'International Container Termin', 'BB Seguridade Participacoes SA' (4 on the YTD... | No holding name on the page is a 30-character cut; a full name comes from G1/G4/the crosswalk. | new |
| RFW-D12 | data | FWD-15, FWD-2 | IDVZ's buying trend runs from 2026-08-21 (30 trading days) and PFOE's from 2026-08-24. | IDVZ and PFOE trend windows start at their inception or 2026-01-02; a line with 1 window reads 'single trade', not BET. | known |
| RFW-D13 | data | FWD-11 | The only benchmark on the page is SCHY (IDVZ peers). | ACWI and IWM appear as benchmarks with their own rankings and trend. | known |
| RFW-D14 | data | FWD-20 | The census lists all 765 securities as 'missing, no G4 row ... | The census reads three states (arrived / covered by fallback, naming the fallback / missing), each with its count. | new |
| RFW-U01 | ui | FWD-18 | '13 of 13 funds current' is printed twice: the stat tile and the sentence under it. | The current-funds count appears once; the sentence names only lagging funds, and is absent when none lag. | new |
| RFW-U02 | ui | FWD-18, FWD-14 | The page opens on Month to date, which is empty for 12 of 13 funds (RFW-D03). | v0.14 (Andrew ~21:0xZ, superseding the shortest-ranking-period rule and any "default YTD" reading): the default period is the last 30 trading days; an empty period's switch shows its state (for example, greyed with a tooltip). | new |
| RFW-U03 | ui | FWD-18 | An empty period renders four table shells, each saying 'No holding added to the return' or 'No sector took from the return'. | A fund-period with 0 ranked renders ONE empty-state line with the reason and the count without a price. | new |
| RFW-U04 | ui | FWD-18 | Every ranking block repeats a two-line method sentence ('Ranks N holding(s) by their contribution ... | Each block shows a one-line count chip ('39 ranked; 1 refused day'). The method text sits once behind an info icon or modal ('How this is computed'). | new |
| RFW-U05 | ui | FWD-15, FWD-19 | The month trend is ASCII marks ('0 0 0 0 + + + + + 0', '. | The month trend is a small bar or sparkline with month ticks, no legend sentence, and 0 overlap between the two tables at 1280-1920 px. | new |
| RFW-U06 | ui | FWD-15, FWD-19 | Net notional is printed to the dollar ('+22,973,442'), and holding names wrap to 3 lines in the narrow holding column ('SPACE EXPLORATION TECHN-CL A'). | Notional reads in $ millions with one decimal; names wrap to at most 2 lines. | new |
| RFW-U07 | ui | FWD-15, FWD-18 | The BET/TILT definition is a sentence in every trend block ('a BET is one window carrying at least half of everything traded in the line, a TILT is built across window... | The definition sits behind the pill's tooltip; the block caption carries dates and trading days only. | new |
| RFW-U08 | ui | FWD-16, FWD-17, FWD-18 | Each account carries, inline: a 'Cited rows' dump of system keys ('holding_contribution IDVZ/R30/71654V408 = 0.00340522; trade_schedule IDVZ/47215P106/2026-09-14 = -2.... | An account shows its text, Observed and Inferred, and 'What would prove this wrong'. Cited rows, grade history, inputs and run provenance open from one 'Sources and checks' control. | new |
| RFW-U09 | ui | FWD-16, FWD-17, FWD-19 | The AI text reads 'fear_greed/fear_greed_index sat at 28.09, with fear_greed/stock_price_strength at 0.4 and fear_greed/stock_price_breadth at 0.2'. | A reading shows a display label ('Fear & Greed index 28.09; stock price strength 0.4'), with the stored name kept as the label's tooltip so the claim survives; 0 raw-code hits in account text. | new |
| RFW-U10 | ui | FWD-16, FWD-9 | A Grounding FAIL account is rendered in full as normal prose. | The account's grade is a badge at its top. A FAIL account is collapsed by default with the reason in its summary line. | new |
| RFW-U11 | ui | FWD-20, FWD-18 | The three detail lists repeat one sentence per item: 765 x 'missing, no G4 row for 2026-10-01; the rankings price it from the fund's own reported valuation' and 765 fo... | Each list is grouped by reason with a count and a fund breakdown; the per-security list opens on demand (with RFW-D14's three states). | new |
| RFW-U12 | ui | FWD-18, FWD-5 | With the audit trail open, the page is 39,194 px tall with 13,473 visible words and 243 disclosures. | Consecutive empty windows collapse into one line ('6 windows, no trades'). The G6 exclusions show once per fund, as totals, with per-window detail on demand. | new |
| RFW-U13 | ui | FWD-18, FWD-19, FWD-1 | The trade log shows system words: 'CLEAN', 'key RESOLVED', '(security_id)', 'G6', 'canonical_shape', 'flow factor 1.0000', and bronze keys and SHA256 as wrapped columns. | Confidence and key resolution read in plain words with the code in a tooltip. Bronze key and SHA256 sit behind a copy control; the FWD-1 trace keeps both reachable. | new |
| RFW-U14 | ui | FWD-19, FWD-4 | The same security is cased differently across sections: 'INTUIT INC' in BASG's rankings and 'Intuit Inc' in its trend; issuer sources are ALL CAPS, others title case. | One display name per security across the page (G1 canonical name). | new |
| RFW-U15 | ui | FWD-19 | The console logs 'Error: <rect> attribute width: A negative value is not valid.' twice (-0.5, -0.4): a bar drawn with a negative width. | 0 console errors on load. | new |
| RFW-U16 | ui | FWD-14, FWD-6 | 'Unclassified' is ranked as if it were a sector ('1 Unclassified +3.83%' at the top of GQGU's Strongest sectors). | The no-sector bucket is never ranked. It shows as a footnote under the sector tables ('x% of this period's contribution has no sector'). | new |
| RFW-U17 | ui | FWD-2, FWD-19 | The freshness tag reads 'Latest report 2026-09-30 HOME; current' (a source chip mid-sentence and a semicolon). | The header reads 'Latest report 30 Sep' with a source chip and a separate current/late chip. | new |
| RFW-U18 | ui | FWD-16, FWD-17, FWD-18 | Each fund carries two accounts of about 120-180 words plus 5-7 Observed and 4-5 Inferred bullets each, all open. | Each account opens to its first two sentences; the rest and the Observed/Inferred lists expand on demand. | new |
| RFW-U19 | ui | FWD-1 | Walked: the platinum page bytes of 2026-10-02 (sha256 97162f5192bf..., served at 14:17:10Z), served locally. | A signed-in walk of the gateway route (the FWD-1 read) confirms the wrapper adds no further defect. | new |

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

- v0.21 (2026-10-08 ~22:3xZ, `1.0.0_SA_CTO~Z`), G.3 wording only: v0.20's R13 sentence was REFUSED by `3.0.0_SA_CVO~RV`
  (`org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_RATIFIED_TEXT_ETFS_RIVALS_v0.20_C_OWED_GRAIN_20261008_RV.md` @85542534a1).
  Only the top-up writer stamps `price_date`, 1 of 4 modes, and the shared reader keeps closes that have no `price_date`, so
  read literally the v0.20 sentence would drop them. It is replaced by the CVO's fix (A), with the C-S73 residual stated. G.2
  ANSWERED was accepted. The ENDPOINT is unchanged.

- v0.20 (2026-10-08 ~22:1xZ, `1.0.0_SA_CTO~Z`), CONTRACTS and G.2 only: `C-OWED-GRAIN` carries R13 (each close's trading
  date; a reader keeps a close only on its own date); G.2's open question is marked ANSWERED with Andrew's card-5 words and
  record. The ENDPOINT is unchanged. `prd-signoff.py status` still reads the ratified-text half SIGNED and current at @35b829a408:
  ADDENDUM G is not a hashed section, because the heading's first word decides the half. So the one contract sentence is put to
  `3.0.0_SA_CVO~RV` by message, and no half is re-opened mechanically.

- v0.17 (2026-10-05 ~04:0xZ, `1.0.0_SA_CTO~Z`), CONTRACTS only: **C-SECURITY-UNIVERSE**, a gold `security_universe` table, the
  interface laptop MDPF_SECCLASS reads (its PRD v0.3 FWD-9/FWD-10, placed by `1.0.0_SA_CTO`, relay msg 29469). The address is builder
  output (verified). The ENDPOINT is unchanged, so no half re-opens.

- v0.16 (2026-10-05 ~03:1xZ, `1.0.0_SA_CTO~Z`), an ENDPOINT addendum on Andrew-direct ~03:3xZ at the `2.0.0_SA_COO~RV` terminal
  (record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_BENCHMARKS_CLICKABLE_TICKERS_ETFCLASSIFIER_BACKFILL.md`),
  item 2, VERBATIM: *"anytime a stock/ticker is mentioned, it should be clickable to the modal, and we should be able to see backfill
  on it."*
  - **NEW FWD-21:** every security named on the page opens its holding modal with its history. A security not yet backfilled says
    so; it never shows an empty chart. The no-script rule stands.
  - Item 1 (ACWI for IDVZ, IWM for PFOE; SCHY is not a benchmark) serves the existing FWD-13/14 and rides round 8 (lg-1).
  - Items 3-4 (every Rival Funds stock backfilled into the ETFClassifier canonical table, with a routine for new stocks) belong to
    MDPF_SECCLASS, a laptop-fabric table. They are routed to `1.0.0_SA_CTO` for placement; ETFS_RIVALS supplies the security list.
  - **The ENDPOINT changed, so the ratified-text half RE-OPENS.** One `3.0.0_SA_CVO~Z` re-sign covers v0.15 and v0.16.

- v0.15 (2026-10-05 ~02:5xZ, `1.0.0_SA_CTO~Z`), an ENDPOINT addendum on Andrew-direct ~02:4xZ at the `2.0.0_SA_COO~RV` terminal
  (record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261005_02xxZ_RIVALFUNDS_30D_DEFAULT_DROP_MTD.md` @575e7d7250),
  VERBATIM in part: *"I think there should be a clear bifurcation of 30d as the default selection, and then there is a divider where
  the user can select QTD or YTD for more clarity. If we are centering around 30 rolling days as the default, there is no need for
  MTD."*
  - FWD-13, 14 and 19: the switch is "last 30 trading days" (default), a dividing line, then quarter to date and year to date. No
    month to date. FWD-14 ranks three periods, not four.
  - RFW-D03's MTD limb is void; its QTD rule stands.
  - **The ENDPOINT text changed, so the ratified-text half RE-OPENS** (`3.0.0_SA_CVO~Z` re-signs). His own words are the ENDPOINT
    confirmation for these lines.

- v0.14 (2026-10-04 ~21:1xZ, `1.0.0_SA_CTO~Z`), an ENDPOINT addendum on Andrew-direct ~21:0xZ, the signed-in smoke at the
  `2.0.0_SA_COO~RV` terminal (record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261004_21xxZ_RIVALFUNDS_SIGNED_IN_SMOKE.md`
  @1c31a5f6ce, items S3, S7 and S8). VERBATIM, in part: *"the way that the period should work is that the last 30 trading days is
  the default. We keep it on a rolling 30 day default, and then we have a dividing line between the year to date, quarter to
  date, month today ... that should really exist in the what drove the return component, and it should exist in the buying trend
  component ... when you click a toggle in any of those components, all the others move in tandem."* and *"if it is not year to
  date, we should not be saying year to date."*
  - FWD-13: the page opens on the last 30 trading days; the rival's buying trend follows the same period.
  - FWD-14: four periods (the last 30 trading days, then month, quarter and year to date); each table states its period and its
    first and last trading day up front.
  - FWD-15: the buying-trend table follows the page's period (default the last 30 trading days), states its window up front,
    and never says "year to date" for another window.
  - FWD-19: the switch reads "last 30 trading days" first and is selected by default, then a dividing line, then month, quarter,
    year (the portal's order, kept). The switch also sits inside "What drove the return" and "Buying trend", and any one moves
    them all.
  - RFW-U02's expected state is replaced. Any "default YTD" reading in earlier rulings is superseded by his word.
  - The CTO ruling "the page keeps working with no scripts" STANDS. The linked switches must meet it. The mechanism is the cell's;
    one shared set of inputs with a label in each place is one way.
  - FWD-16 and FWD-17 are unchanged: the AI's account is already the last 30 days.
  - **The ENDPOINT text changed, so the ratified-text half RE-OPENS** (`3.0.0_SA_CVO~Z` re-signs). His own words are the ENDPOINT
    confirmation for these lines. Items S1, S2, S4, S5 and S6 serve existing outcomes and ride round 8 under the issuer.

- v0.13 (2026-10-02 ~16:2xZ, `1.0.0_SA_CTO~Z`), on `4.0.0_SA_CRO~RV` msg 28560 (GICS census `docs/briefs/rivalfunds-gics-census-20261002.md` @308f982bb8, Andrew-direct ~15:4xZ "Do it now"):
  - RFW-D06's acceptance takes the census's measured levels in place of the walk's unmeasured 10%.
  - ENDPOINT and CONTRACTS are unchanged; coverage stays 33/33.

- v0.12 (2026-10-02, `1.0.0_SA_CTO~Z`), on Andrew-direct ~14:1xZ (record `ANDREW_DIRECT_20261002_141xZ_RIVALFUNDS_UI_WALK_BRIEF_TO_CTO_COO_RV_CANONICAL_DRIVE.md`):
  - The ENRICHMENT BACKLOG gains the 33-item /rivalfunds UI and data walk register (RFW-D01..D14, RFW-U01..U19), owned by
    `2.0.0_SA_COO~RV`.
  - ENDPOINT and CONTRACTS are unchanged (every item serves an existing FWD), so no L4-R half re-opens. Coverage gate 33/33.

- v0.11 (2026-10-02, `1.0.0_SA_CTO~Z`), on CVO~RV's round-5 review P2 (`ETFS_RIVALS_R5_REVIEW_20261002.md`; round-5 analysis
  @a059825ea9 section 3):
  - **CONTRACTS gains C-FAST-RULINGS.** It lifts the contract-level rulings of CRO~RV CALLs 1-13 (rulings file @6e3c94774a and
    earlier) into the ratified text, as served on 2026-10-02 under the A1 pair and addenda 1-11.
  - **The ENDPOINT is unchanged.** Only the CONTRACTS change, and that half's ratified-text sign-off re-opens to
    `3.0.0_SA_CVO~RV`.
  - **Nothing is ruled anew here.** Each clause cites its CALL, and where this text and a ruling differ, the ruling governs until
    the text is corrected.

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

## ADDENDUM F, v0.18, 2026-10-07 -- the price-and-trades modal (`FWD-22`) and the three rolling periods (`FWD-23`)

**L2 by `1.0.0_SA_CTO~Z`** on two Andrew-direct words of 2026-10-07 ~04:5xZ at the COO~RV terminal (both records are in
`org/tier1_exec/2.0.0_SA_COO/deliverables/`, named in the fences) and on COO~RV's scoping facts
(`deliverables/2.0.0_SA_COO~RV/round15_prep/MODAL_PRICE_SERIES_AND_PERIODS_SCOPING_FACTS.md` @82bb78106e). The definitions are in
the ENDPOINT section. This addendum holds the contracts and the reserved points.

### F.1 -- CONTRACTS for `FWD-22`

- **`C-MODAL-PRICE-SOURCE` (v1: no vendor call).**
  - The curve is drawn from prices this pipeline already holds: the market close in `gold/security_market` where a row exists,
    and otherwise the price implied by a universe fund's reported holding on that day (market value over quantity).
  - Each point's source is one of the existing `price_source` values, and the modal names the source in words.
  - A day with neither is a GAP, with its reason.
  - Measured at the cut: `security_market` holds 4 days (2026-09-29 to 2026-10-05), and `trade_schedule` holds 504 days. So v1's
    curve is the implied price where a fund held the security, with gaps elsewhere.
  - A Bloomberg history backfill is the enrichment. It is a vendor pull, and it is RESERVED to Andrew's word (F.3 card 2).
- **`C-TRADE-MARKER`.**
  - A marker's size is the trade's estimated dollar value over the fund's total reported market value at the trade's window
    end, in basis points.
  - The size is clamped: 20 bps or less draws the smallest marker, and 500 bps or more draws the largest.
  - A trade whose window is one trading day is a marker on that day. A wider window is drawn as a span over the window with
    the marker at its end, and it reads "between <start> and <end>".
  - Green is a purchase, and red is a sale. Colour is never the only carrier: the marker's text reads Bought or Sold.
- **`C-NO-SCRIPT` stands for v1** (the ENDPOINT's CTO rulings; `FWD-21`'s ACCEPT).
  - The curve is inline SVG.
  - The range switch is the page's existing no-script switch.
  - A trade marker's detail shows on pointing at it, without a script.
  - Pointing at an arbitrary day of the curve to read its price is NOT deliverable without a script inside the page's size cap.
    That one behaviour is F.3 card 1.
- **`C-PAGE-CAP`.** With every modal's curve on the page, the main page keeps at least 20% headroom under `DIALOG_SOFT_CAP`. The
  365d view may be drawn at a coarser step than the 30d view, and it says so. The over-cap FAIL line (round-10 ADDENDUM 3)
  covers it.

### F.2 -- CONTRACTS for `FWD-23`

- **Scope is the rivalfunds page.** That is the narrowest reading of "consistent everywhere", as COO~RV relayed it. A wider
  reach (the portal's pages) is Andrew's to say and is not inferred.
- **MTD is not displayed either.** He named QTD and YTD. The page's stated metrics are the three rolling periods, and a
  fourth, calendar period beside them breaks "consistent". MTD keeps computing, as QTD and YTD do.
- **90d and 365d are NEW calculations** in `gold_buying_trend` and `holding_contribution`, on the same price rule as today's
  periods (`C-MODAL-PRICE-SOURCE`'s sources). They are not relabels of QTD and YTD.
- **A fund whose history is shorter than the period reads `partial` with its reason** (the existing CALL 3 rule).
- **The AI accounts** are generated on the same three periods from the first sweep after the tables carry them. An account
  that still names QTD or YTD is not shown as current.

### F.3 -- RESERVED to Andrew (two cards; the build of everything else does not wait)

1. **May the rivalfunds page carry ONE script?** Andrew already asked for the price and date on pointing at any part of the
   curve ("just like in market overview"), and that hover is in FWD-22's fence. What is open is only the means: it needs one
   script on a page whose rule is no script. Until he answers, the build delivers everything else, and FWD-22 is graded NOT
   REALIZED (CVO~Z's condition, review @fe586ea2e2).
2. **Is a Bloomberg price-history backfill authorized for the securities and days the pipeline does not hold?** Without it,
   the curve has gaps wherever no universe fund held the security.

### F.4 -- L4-R

ENDPOINT lines and CONTRACTS are added, so the RATIFIED half re-opens to `3.0.0_SA_CVO~RV`. The brief half is Andrew's own
words, recorded verbatim, and no CRO brief is cut for a two-item addendum. `FWD-14` and `FWD-19` are AMENDED where they name the displayed
periods (FWD-23's AMENDS line; CVO~RV's finding @45abbdca53). Every other outcome of `FWD-1`..`FWD-21` and every existing contract
is unchanged.

### F.5 (2026-10-07 ~05:2xZ) -- Andrew's answers, and where the curves live (COO~RV msg 30612)

**Andrew-direct ~05:1xZ** (record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261007_051xZ_RIVALFUNDS_BBG_BACKFILL_YES_PAGE_ONLY_HIDE_MTD.md`
@96d0ab2f4b):
- **F.3 card 2 is ANSWERED YES:** "Yes for the rivalfunds funds only. Probably an ad hoc backfill for the selected funds that uses
  the existing BBG route".
  - Scope as he worded it: Bloomberg daily closes; the securities of the rivalfunds funds; about 365 days; ad hoc.
  - It is not a schedule. No file of the Positioning pull is changed.
  - `C-MODAL-PRICE-SOURCE` gains the backfilled market close as its first source. The holding-implied price stays as the
    fallback, and a gap stays a gap.
- **F.2 is CONFIRMED:** "rivalfunds page only"; "can hide MTD too, should be 30d, then | 90d and 365d".
- **Still open at Andrew:** F.3 card 1 (the script), and the day unit (calendar or trading days).

**The size finding** (scoping facts section 5 @8475c6b260): the served page holds 423 security dialogs with 671 fund sections.
Under `C-PAGE-CAP`, 280,216 B remain, which is 417 B a fund section. One three-range curve is about 1,500 B. **Curves in every
dialog do not fit the main page.**

**Ruling: the curves do NOT live in the main page. `C-PAGE-CAP` is unchanged, and `C-MODAL-PRICE-SOURCE` gains a carrier.**
1. **The chart data is its own daily platinum object family**: one object per fund, holding that fund's securities' price
   series and that fund's trade markers. The address is `lib/opal_naming.py address()` output. It is written by the publish
   stage beside `index.html` and `audit.html`.
2. **ONE gateway route serves it**, behind the same identity wall. It is released by NFRA_OPLGTW, as the audit route was
   (round-11 ADDENDUM 1's reasoning holds unchanged).
3. **How the modal reaches it depends on F.3 card 1, and both branches use the same object and route:**
   - **Card 1 YES (a script):** the modal draws its chart on open from that fund's object, with per-day hover, as Market
     Overview does. The main page grows by the script only.
   - **Card 1 NO:** the fund section of the modal carries ONE plain link, "Price and trades chart", to that fund's chart page.
     The page is rendered by the publisher with no script, and its curves are inline SVG. The modal itself keeps the trade
     list it has.
4. **So round 15 builds everything that does not depend on card 1 or on the day unit:**
   - the ad hoc Bloomberg backfill (under its own never-widen pair; bounded batches after the firm's 07:00 ET vehicle);
   - the price-series table;
   - the trade-marker computation (`C-TRADE-MARKER`);
   - the per-fund chart object and its size line;
   - the route's handler, for NFRA_OPLGTW's release.

   The modal's last step, and the 90d / 365d window lengths, are cut when Andrew's two answers are recorded.

### F.6 (2026-10-07 ~05:3xZ) -- the unit is CALENDAR DAYS (Andrew-direct)

Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261007_052xZ_RIVALFUNDS_PERIODS_ARE_CALENDAR_DAYS.md`
@69c7f24b44. Verbatim: "let's make it calendar days, we dont need that much lookback time".

- **`FWD-23`'s UNIT line carries it.** 30d, 90d and 365d are calendar days ending on the page's as-of date
  (`asof = prev_trading_day(page_day)`, the existing CALL 3 rule). A window's first day is `asof` minus N calendar days.
  The first and last TRADING days inside it are printed on each table, as FWD-14's ACCEPT already asks.
- **The existing 30-day period moves** from 30 NYSE trading days to 30 calendar days. That is about 21 trading days, so every
  30-day figure on the page changes on the first run. It is the ruled change. The run's record states the old and the new
  window for one fund.
- **The Bloomberg backfill is bounded at about 365 calendar days** before the as-of date ("we dont need that much lookback
  time").
- **The 90d and 365d cells are no longer waiting.** F.5 item 4's hold on the window lengths ends. Only the modal's last step
  still waits, on F.3 card 1 (the script).

### F.7 (2026-10-07 ~05:3xZ) -- F.3 card 1 is ANSWERED YES: one script, for the modal's chart (Andrew-direct)

Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261007_052xZ_RIVALFUNDS_PAGE_MAY_CARRY_A_SCRIPT_FOR_THE_HOVER.md`
@efc0acb127. Verbatim: "Yes it can have script". The question as put to him: one small script, for the any-day hover on the
price curve. It is applied at that reach, not as a general lift.

**`C-NO-SCRIPT` is AMENDED, narrowly (it replaces F.1's "stands for v1" and the first branch of F.5 item 3 is the one built):**
- **The page carries exactly ONE inline script block.** It has no external source, and it makes no network call except to
  this product's own chart route on the same origin. `render.py`'s refusal (`_BAD_CONSTRUCTS`) admits that one block and
  still refuses every other script, `src=`, `<link`, `@import` and `url(`. The render check counts the script blocks and
  fails on any number but one.
- **What the script does, and only this:** when a security modal opens from a fund's section, it reads that fund's chart
  object (F.5 item 1) through the gateway route (F.5 item 2). It draws the price curve for the chosen range, places the
  trade markers (`C-TRADE-MARKER`), and shows the price and date on pointing at any part of the curve and the trade's detail
  on a marker.
- **Everything else on the page still works with the script absent or failed:** the fund and period switches, the tables,
  the modals' trade lists, the audit link. A modal whose chart cannot load says so in words and shows its trade list. It is
  never an empty frame.
- **`FWD-21`'s ACCEPT clause "the page's no-script rule stands" and the ENDPOINT's CTO ruling of the same words are AMENDED
  by this line:** the rule stands for everything but this one script.

**Nothing on FWD-22 or FWD-23 is waiting on Andrew now.** Round 15 cuts all of it. The chart route is released by NFRA_OPLGTW,
and the page's script lands only after that route serves, as the audit link did.

## ADDENDUM G, v0.19, 2026-10-07 -- the year of closes is kept by the daily sequence (`FWD-24`)

**L2 by `1.0.0_SA_CTO~Z`** on Andrew-direct ~20:4xZ at the `4.0.0_SA_CRO~Z` terminal (record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261007_204xZ_RIVALFUNDS_365D_BACKFILL_PER_SECURITY_AND_FUND_IN_THE_INGESTION_SEQUENCE.md`)
and on that seat's measured analysis beside it (`RIVALFUNDS_365D_BACKFILL_IN_INGESTION_ANALYSIS_20261007.md` @180673413d), read
whole by this seat. The definition is in the ENDPOINT section. This addendum holds the contracts and the readings.

### G.1 -- what the analysis measured (its reads, not this seat's)

- `security_market` holds 5 trading days of closes. 761 securities appear in a fund's reports in the last year; 206 have no close
  at all and 555 have closes on under a quarter of the days.
- 355 times in the last year a security entered a fund after that fund's first stored report. For 354 of them the store holds no
  close on any day before the entry.
- Nothing in the sequence gives a new security its earlier days. The backfill tool is hand-run, and its "already held" test is
  per DATE: once a date holds any price object, a later run for a new security plans nothing for that date.

### G.2 -- the two readings this seat took of his words (each is one word from him to reverse)

1. **"Per security AND per tracked fund"** is read as: the closes are kept per SECURITY, for every security any tracked fund held
   in the window. A (fund, security) pair is then whole because its security is. It is NOT read as the fund's own holdings
   history (506 daily partitions are already stored) or the fund's own share price. `FWD-24`'s NOT THIS line says so.
2. **"Built into the ingestion sequence"** names no vendor, and his ~05:1xZ word covered an ad hoc backfill only. So it is NOT
   taken as his word for a standing Bloomberg request. **The build proceeds: the history-owed step, the grain change, the reader
   census and the leg's code, exercised with the request switched off. The first STANDING request of closes waits on his recorded
   answer to one question, put to him the same hour: may the daily rivalfunds leg ask Bloomberg each day for the closes it finds
   owed, inside the budget.** (Amended on `3.0.0_SA_CVO~RV`'s refusal of the first wording, msg 31400: CLAUDE.md, no vendor call
   without his explicit per-use word.) The ad hoc one-time backfill stays covered by his ~05:1xZ word.
   **ANSWERED (v0.20):** Andrew-direct 2026-10-08 ~17:1xZ at the `1.0.0_SA_CTO~Z` terminal, card 5 ("Rival Funds: the daily
   leg asks Bloomberg each morning for owed closes"), VERBATIM: *"Yes I like this strategy."* Record
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_171xZ_OPEN_CALLS_SIX_ANSWERED_AND_CELL_TRACKING_ASK.md` @e30fb3e610.
   The standing request is his word, capped at 20,000 returned records a run (R24, the cap the card named). It is set only after
   the writer's three fixes (currency, trading date, window end; RIV-tc-1) are merged, under its own pair (ADDENDUM 7, act 3).

### G.3 -- CONTRACTS

- **`C-HISTORY-OWED`.** The owed set is computed from stored tables only (`security_universe`'s `first_seen`, `last_seen` and
  `funds`, and `security_market`), with no vendor call. Its unit is one (security, trading day) with no stored close.
- **`C-OWED-GRAIN`: the held test is per (security, date), never per date.** A top-up for a date that already holds a price
  object lands as its OWN object in that date's partition. Nothing is overwritten and nothing is deleted. Every reader of
  `security_market` takes all objects of a date; the cell that changes the test first lists those readers, with the count.
  **(v0.21, R13 of ROUND_ANALYSIS.round22, binding `FWD-24`; worded on `3.0.0_SA_CVO~RV`'s fix (A), refusal @85542534a1.)**
  Every object the history-owed top-up adds carries `price_date`, the trading date of each close, and the shared reader keeps a
  close only where its `price_date` is absent or equals the partition date. An object written without `price_date` (the daily
  `market`, `import-market` and `market-range` modes) is read as closes of its partition date. Residual, owned here: a
  reference-data close stamped on the wrong partition (the 2026-09-29 object holding 2026-09-30's closes, row C-S73) is not
  caught by this rule. No year of closes is written by the top-up without `price_date`.
- **`C-OWED-IN-THE-LEG`.** The spend is inside the existing daily rivalfunds enrichment leg, which the vehicle already runs. No new
  scheduled task and no edit under `integrations/bloomberg/` (Andrew's no-modify order stands). The daily request list widens
  from "held today" to "held within 365 calendar days".
- **`C-OWED-BUDGET`.** Every request is checked against `bbg_budget` before it is sent and recorded after, as mode `market-range`
  does today. A per-run cap is a named constant; what is over it is carried, and the run's record prints owed, asked and carried.
  It is third in the pacer's order of claims on the day's allowance (`0.0.3_BG_BBGTerminal`, msg 31283).
- **The one-time backfill** (the round-20 analysis's step) is the first, largest spend of the same owed set. It is not a
  separate tool run once `C-OWED-GRAIN` holds: the leg's own carry does it over as many days as the cap needs.

### G.4 -- ORDER (the one time-sensitive point)

The reader census of `C-OWED-GRAIN` comes BEFORE any year of closes is written. If every reader already takes all objects of a
date (the table holds 8 objects over 5 dates today), the one-time load may be written under the present tool and later top-ups
still land. If any reader takes one object per date, that reader is repaired first. No year of closes is written before that
census is read.

### G.5 -- L4-R

An ENDPOINT outcome and CONTRACTS are added, so the RATIFIED half re-opens to `3.0.0_SA_CVO~RV`. The brief half is Andrew's
words, verbatim in the record, with the CRO's analysis as its measurement. `FWD-1` to `FWD-23` and every existing contract are
unchanged.
