# ETFS_RIVALS: peer groups per Opal fund, the IDVZ group, and income-clean trade detection

L1 BRIEF | MIDSTREAM (ETFS_RIVALS) | Author: 4.0.0_SA_CRO~Z | September 30, 2026

Andrew directed the expansion on September 30. Adam Muller named IDVZ's comparison funds, and Andrew's reply to Adam
names the views the research should present. It is "simply an expansion on the initial tracked group" (verbatim in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/ANDREW_DIRECT.md`, sections "IDVZ rival group"
and "IDVZ group: three decisions and the dividend question").

**Recommendation:** make the tracked universe a set of peer groups, one per Opal fund, each including the Opal fund
itself. Add the IDVZ group (IDVZ, TXUE, BIDD, CGIC, INEQ, SCHY) with Bloomberg as its primary daily source, and add PFOE
to its own group. Tighten trade detection so income and corporate actions never read as trades. Present the
analysis views Andrew named. The storage stays flat; grouping is a mapping.

## PART 0 — How the blind constraint was honoured, and where it bent

- **Not read:** ETFS_RIVALS task orders, the decomposition, and any `phase` or `blocking` field.
- **Read:** the ratified endpoint (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_RIVALFUNDS_20260930.md`,
  nine outcomes) and the PRD's C-NAMES section as quoted to this seat. Served reality was also read: the gateway route
  and the live S3 prefixes (Part VI).
- **Where it bent:**
  - This seat wrote the base brief and its specification, so this revision inherits its own framing.
  - To read the served route, it read one worker commit subject, which names a task-order id
    (`d70267f372`, "TO-RIV-w-1"). Nothing beyond that subject was opened.
  - Andrew's message to 2.0.0_SA_COO~RV was quoted to this seat; it names the grouping question.
- **The endpoint moves, it is not unchanged:** the universe becomes peer groups, the home funds join them, the trade
  schedule gains income and corporate-action handling, and the analysis views are named.

## PART I — THE OUTCOME TERRITORY

### O1 — Andrew opens one Opal fund's peer group and reads it, home fund included, on one analysis plane

**Candidate thread first:** Andrew selects IDVZ on the rival page and sees IDVZ and its five peers side by side: their
trade schedules, style reads and the views in O4-O7, with IDVZ measured by the same rules as the others. Selecting PFOE
shows its group the same way, with PFOE added. Amends the endpoint's FWD-1 journey, which is one fund, to one group.

### O2 — The IDVZ group's history and daily holdings arrive from Bloomberg with no issuer adapter required

Andrew reads, for each IDVZ-group fund, up to two years of daily holdings (or its full Bloomberg history), knowing which
days carry a fresh report. The group's daily collection runs from Bloomberg; a proven issuer file (TXUE's) may
supplement it but is not required. The PFOE group keeps issuer-first collection. The source policy is chosen per fund,
not per product. Extends FWD-2 and FWD-3.

### O3 — Income and corporate actions never read as trades

In every trade schedule, dividend and interest income, their currency conversion, stock splits, bonus issues, spinoffs,
stock dividends and rights issues are never shown as manager trades. Cash and currency lines are not traded positions;
they form the cash cross-check. When a manager spends income on securities, the purchase is a trade, labelled as funded
from income. Amends FWD-5.

### O4 — Andrew sees whether each manager trades with discretion or by system, and why

Andrew reads each manager's style read with its evidence: when its trading concentrates (for example, around a scheduled
reconstitution), how much of the book it touches, and how large its trades are. The index fund in the group (SCHY) must
read as systematic. A count of trades alone is never the evidence (Part IV.3). New.

### O5 — Andrew sees where each manager's trading helped or hurt, by sector and by security

Andrew reads, for each fund, which trades and trade clusters outperformed or underperformed afterwards, summarised by
sector and by security, with each result's window and denominator. This is the first view Andrew named: "trading
outperformance/underperformance by sector and security". Refines FWD-6.

### O6 — Andrew sees each manager's projected trading, drawn from its observed trends

Andrew reads, for each fund, where its trading appears headed across sectors and securities if the observed trends
persist, and what would contradict each projection. This is the second view: "forward projected trading activity based
on observable trends across sectors/securities". Refines FWD-7.

### O7 — Andrew gets a "wildcard" read from the AI, grounded in the same tables

Andrew reads a short, clearly labelled section in which the AI surfaces anything unusual it finds in a fund's or group's
trading, the third view: "Hand-on-the-door wildcard analysis from the AI to see if there's any miscellaneous interesting
calls". Every wildcard cites its rows and says what would disprove it. Refines FWD-7.

### O8 — Andrew compares an Opal fund with its rivals on the same measures

Because home funds join their groups, Andrew reads IDVZ against its peers, and PFOE against its peers, on the style read,
trading results and projections, with no separate method for Opal's own fund. New, from Andrew's point 3.

### O9 — Opal adds a peer group without a new pipeline

A new Opal fund's peer group is added as a mapping entry (the Opal fund, its rivals, each fund's source policy), and it
flows through the same collection, tables, page and archive. New.

## PART II — WHERE THE BOUNDARY SITS

This expansion stays inside ETFS_RIVALS and its existing homes (`opal-data-etfs`, the `rivalfunds` source key and the
`/rivalfunds` route). It owns the peer-group mapping, the per-fund source policy, the income and corporate-action
handling in trade detection, the style read and the named views.

**Home funds are also collected elsewhere:** IDVZ and PFOE holdings are already pulled by
`integrations/bloomberg/pipeline/etf_constituents_pull.py` (DIVZ/IDVZ/PFDE/PFOE), and the TrueShares route collects
IDVZ. A second producer of the same holdings would be the duplicate output path the estate refuses. Whether ETFS_RIVALS
reads the existing producer's output or includes the home funds in its own Bloomberg request is the CTO's to settle at
the PRD, stated explicitly.

It relies on OPAL_BBGTML (the morning Bloomberg vehicle), LGIC (names and homes), the research identity layer, and
ETFS_POSITIONING's classification vocabulary, as before.

## PART III — THE QUALITATIVE BAR

- **One clear signal per fund:** what the manager did, whether it worked, where it is heading, and whether it trades by
  judgment or by rule. A view that no reader uses is not built.
- An index fund's creation-basket adjustments and income never read as a manager's decisions.
- Opal's own fund is judged by exactly the rules its rivals are.
- A projection says what would falsify it; a wildcard cites its evidence; neither invents a return, a trade or a motive.
- Adding a group changes a mapping, not code.

## PART IV — THE SUBSTRATE: measured findings

Evidence: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/IDVZ_GROUP_SOURCE_CENSUS.md`, with its
scripts beside it.

### IV.1 — Bloomberg covers the IDVZ group daily, with share counts

A daily Excel BQL census from 2024-09-30 to 2026-09-29 made 501 requests with 0 errors. Every fund's book carries a
quantity on every row, and weights sum to 100%.

| Fund | Days with a report dated that day | Longest repeated-report run |
|---|---|---:|
| SCHY | 501 / 501 | 0 |
| INEQ | 498 / 501 | 1 |
| CGIC | 496 / 501 | 4 |
| BIDD | 464 / 470 (from 2024-11-12) | 1 |
| IDVZ | 438 / 439 (from 2024-12-27) | 1 |
| TXUE | 417 / 419 (from 2025-01-29) | 1 |

### IV.2 — Issuer files for this group are mostly not scriptable today

TXUE's daily xlsx works: it has an as-of date and shares, but no archive. SCHY answered HTTP 403 to a scripted request;
INEQ and CGIC render their holdings client-side; the iShares CSV endpoint returned a web page for BIDD.

### IV.3 — Trade detection needs income and corporate-action handling; counts alone mislead

The pro-rata flow model holds for all six funds.

- **Cash and currency lines:** at the 0.2% floor they carried 59.2% (SCHY), 21.8% (BIDD), 21.3% (INEQ), 14.9% (CGIC),
  7.4% (TXUE) and 4.7% (IDVZ) of detected adds and trims. That is where dividend and interest income and its conversion
  land.
- **Corporate actions and scrip:** a scripted `DVD_HIST_ALL` pull for 738 held securities (695 with rows) reclassifies
  13 events (splits, bonus, spinoff). Small adds show no clustering on cash-dividend ex-dates, so scrip take-up is not
  material in this group.
- **Style:** the index fund still trades on every day through small basket adjustments. Its signature is timing:
  entries and exits concentrate in March. The discretionary managers (TXUE, IDVZ) make fewer, larger, narrower trades.

### IV.4 — The storage is already flat; grouping is a mapping

Trade and holdings tables are keyed by fund under builder addresses (`rivalfunds/etfs/...`, `issuer-site/etfs/...`,
`bloomberg/etfs/...` in `opal-data-etfs`). A peer group adds no key segment; a fund that rivals two Opal funds is stored
once.

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- A versioned peer-group mapping (Opal fund, its rivals, each fund's source policy), read by collection, the tables and
  the page. Its home and name come from the builder.
- The Bloomberg daily leg requests every Bloomberg-primary fund; the fallback leg is unchanged for issuer-first funds.
- Trade detection excludes cash and currency lines and applies corporate actions from `DVD_HIST_ALL` before reading a
  residual as a trade; the cash cross-check labels income-funded buying.
- Total returns and sector classification for every held security, for O5 (Bloomberg, scripted, R-21).
- The style read uses timing, breadth and size, with the group's index fund as its control.
- Home-fund holdings come from one producer (Part II).
- Two readings are checked before they drive a style label: CGIC's very high breadth of trading, and INEQ's 657 entries
  and exits against about 104 names.

## PART VI — STATUS — NOT OUTCOME-BEARING

As measured on September 30, 2026:

- ~11:05-11:40 ET: the census and issuer probes ran.
- ~12:0x ET: the dividend history was pulled.
- 15:4x UTC, served reality (read with a positive control), in `opal-data-etfs`:
  - BASG issuer bronze for 2026-09-30 (written 11:00 UTC);
  - `canonical_shape` and `trade_schedule` gold history from 2025-06-13;
  - a published page at `rivalfunds/etfs/platinum/page/date=2026-09-30/` (latest revision 12:33 UTC);
  - no `bloomberg/etfs/` bronze.
- The gateway `/rivalfunds` route exists in the repository; its deployment was not checked.
- No IDVZ-group data has been written anywhere but this seat's local research folder.

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

- Legal inception dates for BIDD, IDVZ and TXUE.
- The causes of CGIC's and INEQ's patterns.
- Issuer publication times.
- Whether the round-1 page already excludes cash lines (not read).
- Quota cost of adding the group to the morning run.
- The correctness of any style label before O4's control is exercised.
- Whether PFOE's own holdings are best taken from the existing producer.

## References for the next consumer

- **BRIEF PATH:** `docs/briefs/etfs-rivals-idvz-expansion-20260930.md` (midstream to
  `docs/briefs/etf-holdings-research-20260929.md`)
- **PROJECT:** ETFS_RIVALS (`org/missions/D5/ETFS/ETFS_RIVALS/`)
- **EXISTING PRD:** `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`; endpoint
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_RIVALFUNDS_20260930.md`
- **SIBLING PROJECTS:** OPAL_BBGTML; LGIC; ETFS_POSITIONING; the home-fund producers `etf_constituents_pull.py` and the
  TrueShares route
- **PRIOR ART:**
  - `IDVZ_GROUP_SOURCE_CENSUS.md`, `TRADE_INFERENCE_FEASIBILITY.md`;
  - scripts `bbg_daily_coverage_census_multi.py`, `dividend_history_pull.py`, `dividend_trade_match.py`,
    `trade_inference_probe.py` (all under `.../AMGT_RECONN_SOURCES_20260929/`);
  - Andrew's email of 2026-09-30 14:42 UTC, quoted in `ANDREW_DIRECT.md`.
- **MEASURED AT:** Part VI clocks; the evidence file carries the per-measurement times.
