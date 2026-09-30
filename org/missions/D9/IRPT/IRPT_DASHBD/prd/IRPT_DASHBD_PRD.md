# IRPT_DASHBD -- the client reporting dashboard (Opal-shape reporting gold, total return, a served series, the views)

```json
{
 "project": "IRPT_DASHBD",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.3",
 "step": 4,
 "brief_ref": "docs/briefs/reporting-dashboard-backend-brief-20260930.md@0ee065b116",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10"],
 "status": "RATIFIED"
}
```

Author: `1.0.0_SA_CTO`. D9 / IRPT / laptop. Register row `org/missions/D9/IRPT/IRPT_DASHBD/project.json` @7ae82f3532 (workstream B
on `2.0.0_SA_COO~P`, workstream F on `2.0.0_SA_COO~D`, Andrew's seating).

Briefs: the header's `brief_ref` is the CRO's BACKEND brief; the FRONTEND brief `docs/briefs/reporting-dashboard-frontend-brief-20260930.md`
@0ee065b116 is read as the second brief and covered in section 8. Neither is complete without the other (both briefs, line 3). Andrew's words:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md` (six messages) and
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_052xZ_PRECOMPUTED_GZIP_JSON_REPORTING_UNDER_2S_AND_PUSH_MANAGED.md`. Endpoint:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_REPORTING_DASHBOARD_20260930.md` @9a3afb2f9c. The section below carries its
outcomes verbatim.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An advisor opens one 49 Financial account on the live portal, sees its daily total-return
         history, picks any start and end date, and the answer is on screen in about two seconds,
         with nobody having run anything that day
         DONE WHEN  EXERCISED -- one live trace: custodian file -> silver -> the Opal-shape gold ->
                    the served series file -> the signed-in page -> the drawn curve and headline number
         ACCEPT     Andrew picks an account and two dates the next morning and sees the curve without
                    waiting; changing the dates makes the page wait on nothing; every hop is the real
                    thing (a hop fed by a fixture fails this outcome)
         SOURCE     backend brief O1 and Part VI; frontend brief F1 and Part VI; Andrew "49 Financial
                    should be the first", COO~P record "under 2 s"

  FWD-2  Any account of any firm the gold covers loads the same way, and nothing on the page or in
         the file says which firm's plumbing produced it
         DONE WHEN  EXERCISED -- an Inflection account and a Cottonwood account each shown on the same page
         ACCEPT     a reader cannot tell from the page or the file which firm the account came from;
                    where a firm lacks a piece of data the page says so in words, never with a
                    firm-specific layout
         SOURCE     backend brief O2, Part V.1-2; Andrew message 3 ("gold is the adapter layer")

  FWD-3  A person sees how each asset class performed over the window and how the mix moved
         between two dates, in Opal's canonical classes
         DONE WHEN  EXERCISED -- a real account's window read by a person
         ACCEPT     a person says in one sentence which class drove the window and how the mix moved,
                    without reading a table; the classes add up to the account; unclassified holdings
                    show as their own class and are never folded away
         SOURCE     backend O3, Part V.4; frontend F2, F3; Andrew "asset allocation relying on Opal
                    canonical ETF-Classifier asset classes"

  FWD-4  A person sees realized gain, unrealized change and income for a window, and an activity
         summary whose figures agree with the transactions for the same window
         DONE WHEN  EXERCISED -- summed by hand from the transactions list and matched
         ACCEPT     beginning value, contributions, withdrawals, gain split three ways, and ending value
                    are on one screen beside a chart of value against contributions, and a deposit
                    reads as a deposit, not as performance; an account whose custodian gives no lot
                    detail says so instead of showing zero
         SOURCE     backend O4, Part V.4; frontend F4, F5; Andrew "unrealized gain + realized gain
                    over the given period", "activity summary view"

  FWD-5  A person browses the transactions for any account and window, filters, sorts and exports them
         DONE WHEN  EXERCISED -- a real window browsed and exported
         ACCEPT     date, asset, action, type, symbol, units, price, amount and custodian are shown in
                    Opal's own words for the action and type, not the custodian's codes; a long window
                    scrolls without the page stalling
         SOURCE     backend O5; frontend F6; Andrew "we should be able to show transactions"

  FWD-6  At the deepest drawdown in the chosen window, a person sees the topics that were trending
         then, as a cloud they can read at a glance
         DONE WHEN  EXERCISED -- Andrew reads one
         ACCEPT     the topics around the trough are ones a person who lived that week recognises; the
                    view says plainly they are market-wide, not filtered to the portfolio; a drawdown
                    before the news history begins says there is no topic history, never an empty cloud
         SOURCE     backend O6, Part V.7; frontend F7; Andrew "wherever the biggest drawdown is should
                    absolutely have a snapshot of the topic cloud phrases", "a signature view"

  FWD-7  A household or a client is the same page over more accounts, built from the account grain
         DONE WHEN  EXERCISED -- one real household shown
         ACCEPT     an "all accounts" choice shows the household with no new concept on the page; its
                    figures follow the same rules as one account's; accounts with different histories
                    are shown honestly, not averaged into a longer one
         SOURCE     backend O7, Part V.6; frontend F9; Andrew "Account level is all that matters, I
                    don't mind aggregating for household/client level"

  FWD-8  A return figure a person can defend: total return, before advisory fees and labelled so,
         and a day the data cannot support says so instead of showing a plausible wrong number
         DONE WHEN  EXERCISED -- the 49 Financial figure tied out against Black Diamond's own return
         ACCEPT     for an account and window the two returns agree within a tolerance Andrew accepts
                    and every day they disagree carries a stated reason; a misdated or missing deposit
                    can never show up as a huge gain or a total loss; the old "time-weighted, net of
                    fees" label is gone everywhere the new figures show
         SOURCE     backend O8, Part V.3 (the guard against hyper-exaggeration), Part IV.4; frontend
                    F8, Part IV.7; Andrew messages 4-6 (conservative GIPS, gross of fees, "avoid flows
                    having hyperexaggerated effects")

  FWD-9  The reporting gold is one Opal shape for every firm, with a written contract per table and
         one adapter per firm, and the fee rail is reserved and unused
         DONE WHEN  APPLIED -- the tables, their contracts and the three adapters exist and agree
         ACCEPT     the same table from any two firms has the same columns and meanings; the only place
                    a firm's own codes appear is inside that firm's adapter; a fee field exists,
                    carries nothing, and no net-of-fee figure is produced anywhere
         SOURCE     backend Part V.1, V.2, V.5; Andrew message 3 and message 5 ("a rail for fees")

  FWD-10 A person can always tell what they are looking at: where the data starts, which days could
         not be measured, when a figure is a fallback, and how current the data is
         DONE WHEN  EXERCISED -- read from the screen alone
         ACCEPT     a partial-history account, a day that could not be measured, a fallback day and a
                    window before the news data starts are each explained on screen in a sentence;
                    no state is hidden inside an average
         SOURCE     backend Part V.1 (the coverage vocabulary), V.3; frontend F8, Part V.3
```

## ENDPOINT PROVENANCE (outside the ratified section)

- FWD-1..FWD-8 come from the backend brief's O1..O8 and the frontend brief's F1..F9, merged one to one where both briefs
  name the same capability (F2+F3 -> FWD-3; F4+F5 -> FWD-4; F9 -> FWD-7). FWD-9 is the backend's Part V.1-2 and V.5 as an
  APPLIED outcome. FWD-10 is F8 and the backend's coverage vocabulary as an EXERCISED outcome. Net worth, held-away
  accounts and liabilities are OUT (Andrew: "scratch it", "forget this view") and no outcome carries them.
- **The narrowing this endpoint records (Andrew, messages 4-5):** external flows enter the return as a weighting input
  under conservative GIPS-style rules, never as an unguarded term. This narrows his 2026-09-28 holdings-only ruling FOR
  THIS PROJECT ONLY. IRPT_BCKEND's holdings-basis performance gold (its PRD v0.19-v0.21) is unchanged and becomes this
  project's guard rail (C-GUARD). IRPT_BCKEND's next addendum cites this section rather than restating it.
- Andrew's DONE WHEN confirmation was not separately asked (the /self-drive rule, record
  `ANDREW_DIRECT_20260929_022xZ_NOTHING_WAITS_ON_ANDREW_SELF_DRIVE_RESOLVES_CALLS.md`); the six messages are his word for
  the outcomes. A word of his that amends an FWD is an addendum under the next unused id or an in-place amendment, never a
  cell's choice.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-TIERS: the medallion | law (CLAUDE_ANNEX 17, 17a, 17b, 17c; `infra/logic/02_DOCTRINE.md`) | Bronze holds each custodian's raw shape; silver is typed, de-duplicated parquet still in the source's shape; GOLD is parquet in ONE Opal shape, the adapter layer; PLATINUM is the only JSON producer and the served files live in the FIRM's bucket (client-confidential). Nothing else serves JSON. |
| C-SHAPE: one gold shape | this project; annex 17c | Eight account-grain tables (section 1 of the backend brief's Part V): `account_return_daily`, `account_class_daily`, `account_activity_daily`, `account_transaction`, `account_lot_realized`, `account_lot_unrealized_daily`, `account_dim`, `market_topic_daily`. Every table carries `firm`, `account_id`, `method_version`, `coverage`. ONE contract file per table under `org/standards/` named `IRPT_DASHBD_<TABLE>_CONTRACT.json`, authored by the round that first writes the table (round 1: `account_return_daily`). A firm-specific column is a contract violation; a firm that lacks a field carries null plus a `coverage` value that says why. The conformance check is the schema hash: the same table from any two firms hashes the same. |
| C-COVERAGE: the closed vocabulary | this project; rule 24 | `coverage` is one axis with the members `FULL`, `PARTIAL_HISTORY`, `NO_LOTS`, `FLOW_UNRECONCILED`, `UNCLASSIFIED_HOLDINGS`, `SOURCE_LAG`, `FEE_RAIL_UNUSED`, `MISSING_HISTORY` (topics only). Adding a member is a contract addendum with its four-postulate record, never an ad-hoc string. The frontend maps each member to one plain-English sentence (C-HONESTY). |
| C-ADAPTERS: firm knowledge lives in one place | this project | One adapter per firm (49 Financial from Schwab silver `dim_position`, `dim_balance`, `fact_trn` with the 187-code table, `fact_uln`, `fact_rld`, the household dimension; Inflection from Orion positions, `accounts_v2`, transactions by the ratified `orion_cashflow_taxonomy.yaml`, lots `NO_LOTS` until Eclipse tax lots are shown populated; Cottonwood from Black Diamond holdings, transactions, `fact_realized`/`fact_unrealized`). Schwab `sb_cd` codes, Orion type ids and Black Diamond `Transaction Type` appear ONLY inside their adapter. Black Diamond's `performancePeriod` and `activitySummary` are TIE-OUT oracles (C-TIEOUT), never a source of gold. |
| C-METHOD: total return | Andrew-direct 2026-09-30 messages 4-6; this project fills the GIPS detail | Daily valuation of the WHOLE account, cash included; `r_t = (V_t - F_t) / V_(t-1) - 1` with `F_t` the net EXTERNAL flow valued at market on its date; daily returns geometrically linked so any window is a product of days; income counts on CASH RECEIPT (a declared departure from GIPS accrual, written in the method contract); reinvested dividends count once; corporate actions are their own class and are neither flow nor income; in-kind transfers valued at quantity times same-day close, an unpriced leg `FLOW_UNRECONCILED`; GROSS of advisory fees, labelled "before advisory fees"; no annualization under one year; since-inception annualized only past a year. Daily TWR is the ONE headline; Modified Dietz is computed from the same columns as the per-window cross-check and the labelled fallback, never a second headline. This is GIPS-ALIGNED methodology, not GIPS compliance (no composites, no verification), and the label says so. One row per `method_version` in `dim_return_method` (flow convention, income basis, fee basis, tolerance, large-flow share, plausibility band, day-count); any change is a new version and the served files carry it. |
| C-FLOWTIME: the flow-timing convention is measured | this project, round 1 | End of day is the default (the custodians' end-of-day values; the retiring engine). The round-1 tie-out scores start, end and midpoint conventions against Black Diamond's own time-weighted return on the 49 Financial sample and writes the winner into the method contract. No sub-period valuation is claimed. |
| C-GUARD: no hyper-exaggerated return | Andrew message 4; backend Part V.3 | Every day the flow-adjusted return is compared with IRPT_BCKEND's holdings price return (`holdings_price_return`, carried in `account_return_daily`) plus the day's income return; a difference beyond the method's tolerance marks the day `FLOW_UNRECONCILED` and `total_return_daily` falls back to price return plus income with `return_basis = HOLDINGS_INCOME_FALLBACK`. A large external flow marks `LARGE_FLOW`. A prior value at or below zero or a return outside the plausibility band is `NOT_MEASURABLE` and breaks the link with a stated gap. The tolerance, the large-flow share and the band are set in round 1 FROM the 49 Financial data's own distribution and written into `dim_return_method`; they are not invented in this PRD. |
| C-VALUE: the whole-account value contains cash | this project | `V` includes the cash that income produces, taken from each firm's balance table (Schwab `dim_balance`, Orion's custodial-cash flag, Black Diamond allocations). Round 1 verifies `V` per firm before any figure is served; a firm whose value excludes sweep or cash cannot serve a total return, only `PARTIAL` with the reason. |
| C-FEERAIL: reserved, unused | Andrew message 5 | `fee_amount` in `account_return_daily` and `account_activity_daily` (null, `FEE_RAIL_UNUSED`); `fee_basis = GROSS_ONLY` in `dim_return_method`; `FEE` as a flow class. Nothing computes a net return; a later fee project fills the fields under a new `method_version` and changes no column name. |
| C-GAINS: realized, unrealized, income | this project | Realized gain is the sum of `account_lot_realized.gain_loss` by closing date (49F from `fact_rld`, the RLD vintage; the PRD confirms the vintage in round 3 against RLU/RLW/RLY and the RT* set); unrealized change is the difference of `account_lot_unrealized_daily.unrealized_gl` over the window; income is separate. All three feed `account_activity_daily` so a window's activity summary is a sum over one file's slice. `NO_LOTS` where the custodian gives no lot detail. |
| C-CLASSES: canonical asset classes | consumed; MDPF_SECCLASS (D8) | Each holding maps through `etf-classifications` (DynamoDB, key `ticker`): fixed_income, equity, commodities, structured, alternatives; the portal adds cash, unclassified, other. No row means UNCLASSIFIED; nothing is guessed. `class_return_daily` is the class's contribution to the account's daily return, so classes sum to the account. This project adds no classification. The Cottonwood gold host's missing read on the securities table (IRPT_BCKEND S173) is a coverage state here, not a workaround. |
| C-SERVE: platinum, precomputed | COO~P's recommendation adopted; Andrew "under 2 s" | A platinum publisher reads gold parquet and writes per account: `series.json.gz` (columnar arrays: date, value, daily total return, basis flag, external flow, income, per-class value and weight by day, the drawdown episode list, method version, data as-of, first data date), `manifest.json` (method version, as-of, coverage summary, byte sizes), and `transactions/page=N.json.gz` newest first. The browser computes any window from `series`; no per-window request exists. Household and client files are built by the same publisher with the same rules. Size and time to paint are MEASURED in round 1, never estimated in a criterion. |
| C-SEAM: the one seam between B and F | this project | The `series` and `manifest` field list is a section of `IRPT_DASHBD_SERIES_CONTRACT.json` under `org/standards/`; workstream B is its ONLY writer and the page its only reader. A field the page needs and the file lacks is a change request across the two workstreams through the COO, never a page-side derivation from another source. FWD-1 owns this seam. |
| C-TOPICS: the signature view | this project; news pipeline consumed | Drawdown episodes are detected with the `irpt-narrative` peak, trough, recovery logic (trough at least 50 bp and 2 days; rolling 5-point moves of at least 50 bp) by the PUBLISHER, which writes the episode list into `series`. Topics for an episode merge `market_topic_daily` over the seven days before the trough; they are MARKET-WIDE (ticker tagging is empty after 2025-12) and the view says so; a window before 2025-11-21 (curated) or 2025-12-01 (phrases) is `MISSING_HISTORY`. `market_topic_daily` is general, non-client data and lives in the general platinum home, not a firm bucket. |
| C-NAMES: rule 30 | consumed; LGIC | Every S3 address is `lib/opal_naming.py address()` output and every resource name is `name()` output. Builder output at L4 (printed 2026-09-30 13:5xZ): gold `address("irpt","49financial","gold","account_return_daily","date=2026-09-29")` -> `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-29`; the same for `inflection` and `cottonwood` under their own buckets; platinum `address("irpt","49financial","platinum","reporting","account=0010498003","series.json.gz")` -> `s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=0010498003/series.json.gz` and `.../manifest.json`; names `name("irpt","49financial","reporting-adapter","lambda")` -> `irpt-49f-reporting-adapter-lambda`, `name("irpt","49financial","reporting-publish","lambda")` -> `irpt-49f-reporting-publish-lambda`, `name("irpt","49financial","reporting-publish","daily")` -> `irpt-49f-reporting-publish-daily`. A partition with a slash is refused by the builder (READ, brief Part IV.2), so the account partition and the date partition are two tables, never one nested key. |
| C-SOURCES: registry rows | LGIC lane; this project's L3 policy step | No table named `reporting` or any of the eight is registered in `infra/logic/registry/reporting_policies.json` (ABSENT, brief Part IV.2); `address()` accepts the names, so registration is a policy row this project adds in round 1 with the first contract. The topics home REFUSED at L4: `address("news","opal","platinum","market_topic_daily",...)` -> `scope 'opal' resolves to no scopes.json row`. So the general platinum home for `market_topic_daily` is a scope row to add (or an existing shared scope to cite by `lookup()`), decided in the round that builds FWD-6; nothing is typed around it. |
| C-TIEOUT: the parity oracle | this project; Andrew "which would be more accurate" | The 49 Financial total return is tied out against Black Diamond's own time-weighted return for the sample accounts; agreement within the tolerance Andrew accepts is FWD-8's bar; every disagreeing day carries a stated reason (flow timing, missing price, income date). The oracle is read through IRPT's existing per-account Black Diamond calls behind their per-use gate; no new vendor pull without Andrew's per-use word. The existing price-only figure sits a median of about 1.6 points below (READ, `TO-IB-er-302`); closing that gap is what "total" means here. |
| C-LABEL: the honest label | frontend F8; backend Part IV.4 | The portal's "Time-weighted, net of fees" (`MethodAndSources.tsx:32-63`, `holdings_gold.py:259` `TIME_WEIGHTED`/`NET`) is wrong for a price-only, fee-less figure and is replaced everywhere the new figures show by "Total return, before advisory fees" with the method version in the popover. Where the OLD figure still shows (IRPT_BCKEND's page until this project's switch), the label is corrected by IRPT_BCKEND under its own order; this project does not edit that page. |
| C-HONESTY: coverage on screen | frontend Part V.3 | Each `coverage` member maps to one sentence shown where the number is; a window before the first data date is clipped and says so; excluded days are counted on the window return; a fallback day is footnoted. No state is hidden by an average, and no skeleton state looks like data. |
| C-DESIGN: the portal's law | consumed; `portal/CLAUDE.md`, `portal/DESIGN.md`; DSGN_IRPTV1 | Light canvas, white containers with the hairline and navy ink, one dark band per page, tabular numerals, chart colours from `chartColors.ts` `ASSET_CLASS`, status and data colours disjoint; verification is `/frontend-dev` screenshots read against the clause cited; dev builds on port 5174 only. Asset-class display order: Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, Other, Unclassified. |
| C-LEASE: F's rounds beside DSGN_IRPTV1 | this PRD, ruling 6.7 | While a DSGN_IRPTV1 FAST lease is live on `2.0.0_SA_COO~D` over `portal/src/pages/InvestorReporting`, F's items are built by that seat under `/closer-drive` reading this PRD's FWD-1 and C-SEAM, and graded by the CVO after the fact as DSGN_IRPTV1 pins; F's TASK ORDERS (FULL mode) name paths under `portal/src/pages/InvestorReporting/tabs/reporting/` and the new `portal/src/pages/InvestorReporting/dashboard/` only, and the next DSGN_IRPTV1 lease arm excludes those two paths or holds. One seat, two projects, no two writers of one path. |
| C-MORATORIUM: no alerts | law (CLAUDE.md section 5) | No alarm, SNS, SES send, freshness checker or monitor. The publisher runs on its own schedule (`irpt-49f-reporting-publish-daily`), never on "success of upstream" alone. A stale day is a `SOURCE_LAG` coverage state on the page, not a notification. |
| C-FIRM: firms | law (CLAUDE.md section 5) | Each firm's gold and platinum live in that firm's bucket; no pipeline tree references another firm's bucket or key prefix; `cot` is a separate firm from `bd` and is never mirrored. Household files never cross a firm. |
| C-SHADOW: no shadow path | law (CLAUDE.md section 5) | This project extends IRPT_BCKEND's gold and retires nothing in it without that project's word; it opens no second performance figure on the same page: when this project's figure serves, IRPT_BCKEND's page reads it (C-LABEL) or the old one, never both. The retiring flow engine (`c02_twr_engine.py`, retired by IB-pr-201) is prior art, not imported. |

## 1. The arc

Start: a per-account price-only daily return gold (49 Financial, 557 trading days; Inflection and Cottonwood marked complete) served as
"time-weighted, net of fees" with no fees, no income and no flows; a report that takes a median 6.7 s and re-fetches every account on a
period change; no transactions view, no per-class performance, no activity summary, no allocation change; a draft return spec from July
never ratified; a drawdown-and-news print page; a topic cloud that renders empty under test.

End: for every account of every firm, one Opal-shape reporting gold with a written contract per table and a defensible total return; one
served series file per account that answers any window in the browser in about two seconds; a page with the curve, the classes, the
allocation change, the gains and activity summary, the transactions and the topic snapshot at the deepest drawdown; households and clients
as the same page; every number labelled and every gap explained on screen.

## 2. THREAD -- FWD-1, one 49 Financial account end to end (round 1; B builds hops 1-4, F builds hop 5, the trace crosses the seam)

1. Schwab silver for one account (`dim_position`, `dim_balance`, `fact_trn`) -> the 49 Financial adapter -> gold `account_return_daily`
   at the builder's address, under its contract file (C-SHAPE), with `holdings_price_return` carried from IRPT_BCKEND's gold and the
   C-GUARD comparison applied (tolerance and band set from the data, written to `dim_return_method`).
2. Gold -> the platinum publisher (`irpt-49f-reporting-publish-lambda` on `irpt-49f-reporting-publish-daily`) -> `series.json.gz` and
   `manifest.json` at the builder's addresses, with the field list of C-SEAM; size and build time printed.
3. The served file -> the signed-in portal page on DEV (real login, real backend): one fetch of `series` and `manifest`.
4. The page -> the cumulative total-return chart with the headline number, presets and two date fields plus a brush, the label "Total
   return, before advisory fees" with the method version, and the coverage sentences the file can produce (C-HONESTY).
5. Trace -> Andrew opens the account the next morning, changes the dates, sees the curve move with no network request; time to painted
   chart is measured and printed beside the file size. Any hop fed by a fixture fails the outcome.

Round 1 builds only this thread. B's round-1 cells: the adapter and the first gold table with its contract and the C-GUARD; the publisher
and the series file with its contract; the tie-out harness (C-TIEOUT) run once on the sample. F's round-1 cell: the Performance chart
reading `series`, with the honest label and the coverage states, under C-LEASE. Nothing outside this project blocks round 1.

## 3. ENRICHMENT BACKLOG (ordered, one line each; each later round enriches)

**Workstream B (backend, `2.0.0_SA_COO~P`)**
1. `account_class_daily` and the class contribution (FWD-3).
2. `account_activity_daily`, `account_lot_realized`, `account_lot_unrealized_daily` from `fact_rld` and `fact_uln`, the RLD vintage confirmed (FWD-4).
3. `account_transaction` with the Opal action and type vocabulary and `flow_class`, paged platinum files (FWD-5).
4. `market_topic_daily` in the general platinum home (its scope row first, C-SOURCES), drawdown episodes written into `series` (FWD-6).
5. The Inflection adapter (lots `NO_LOTS` until Eclipse tax lots are shown populated; whether Orion's returns include dividends is measured, not assumed), then the Cottonwood adapter with Black Diamond as tie-out (FWD-2).
6. `account_dim` and the household and client files from the account files; the household union-find's home decided (FWD-7).
7. The C-LABEL switch of IRPT_BCKEND's page to this figure, under IRPT_BCKEND's own order and halves (FWD-8).
8. The first use of the fee rail: a later project, not this backlog.

**Workstream F (frontend, `2.0.0_SA_COO~D`)**
1. Asset-class performance rows and the allocation-change view (FWD-3).
2. The activity summary with the value-against-contributions chart and the gains block (FWD-4).
3. The transactions table: sort, type filter, symbol search, export, virtualised (FWD-5).
4. The drawdown markers and the topic panel, reusing `TopicCloud.tsx` or its pattern, rendered as DOM under test (FWD-6).
5. Inflection and Cottonwood accounts: no frontend change expected, verified by screenshot (FWD-2).
6. The account picker's "all accounts" and the uneven-history indication (FWD-7).
7. Print of a window's chart, summary and classes through the existing print route; the export file (FWD-5).

## 4. Engines (one row per engine)

| Engine | Serving shape | Role here | Deploy mechanics |
|---|---|---|---|
| the three adapters (`irpt-<firm>-reporting-adapter-lambda`, or a gold script under `data/assets/scripts/gold/` where the estate's gold pattern already runs on EC2) | scheduled Python, pyarrow | silver in the firm's shape -> the eight gold tables in the Opal shape | Rule 13 (DS lane commit -> QA-deploy) for gold scripts; Terraform only for a Lambda; the choice is a round-1 cell's stated reading of where IRPT_BCKEND's producer runs today |
| the platinum publisher (`irpt-<firm>-reporting-publish-lambda` on `irpt-<firm>-reporting-publish-daily`) | a scheduled Lambda writing gzipped JSON to the firm bucket | the served files; the drawdown episodes; household files | Terraform; its own schedule (C-MORATORIUM) |
| IRPT_BCKEND's holdings performance gold (`data/assets/scripts/gold/irpt_holdings_performance/`) | per-account price-only daily return | the guard rail (C-GUARD) | IRPT_BCKEND's project; consumed |
| `etf-classifications` (DynamoDB) | the canonical class per ticker | C-CLASSES | MDPF_SECCLASS's project; consumed |
| the news tables (`opal-news-trending-daily`, `trending_reports/`) | curated topics and weighted phrases per day | C-TOPICS | the news pipeline; consumed |
| the portal (`portal/src/pages/InvestorReporting/`) | React on DEV, port 5174 | the views | the F seat lands on DEV itself under a live FAST lease; VALGATE on every push; PROD is gated |
| Black Diamond `performancePeriod` (through IRPT's existing per-account call) | a vendor return per account and period | the tie-out oracle only | per-use gate; Andrew's word for any new pull |

## 5. WORKSTREAMS AND OWNERS

- **Andrew's seating (record, message 1):** "COO~P on the backend and bucketing and COO~D on the frontend, so we could run this whole
  function in concert." `2.0.0_SA_COO~P` issues workstream B; `2.0.0_SA_COO~D` issues workstream F. Each holds another project
  (IRPT_BCKEND; DSGN_IRPTV1); the one-project-per-instance seating check is overridden by his word for this project, and the register row
  says so. One issuer per round per workstream; the two workstreams are scopes with disjoint write surfaces (C-SEAM is the boundary).
- **Write surfaces.** B: the contract files under `org/standards/IRPT_DASHBD_*`, the adapters, the publisher, the gold and platinum keys
  under each firm's `irpt/<firm>/gold/` and `irpt/<firm>/platinum/reporting/`, the `reporting_policies.json` rows. F:
  `portal/src/pages/InvestorReporting/tabs/reporting/` and `portal/src/pages/InvestorReporting/dashboard/` (new), plus
  `portal/src/lib/chartColors.ts` only additively. Neither writes the other's surface.
- **Owned elsewhere, named in the decomposition and NOT built here:** the canonical classes (MDPF_SECCLASS); the holdings price return
  (IRPT_BCKEND); the news tables; the C-LABEL correction on IRPT_BCKEND's page until the switch; the household union-find's migration
  (ADVI_FIRMBKTS's tree); registry rows (LGIC lane).
- **The CRO** signs the BRIEF half by authorship (spine v3.19 L4-R); the CVO (`3.0.0_SA_CVO`) signs the ratified-text half.

## 6. Rulings closed at L4 (no decide-first question enters L5)

1. Total return is C-METHOD; daily TWR is the one headline, Modified Dietz the cross-check and labelled fallback. GIPS-ALIGNED, never
   "GIPS compliant" in any label.
2. The flow-timing convention is measured (C-FLOWTIME), default end of day; the tolerance, large-flow share and plausibility band come
   from the 49 Financial data in round 1 and live in `dim_return_method`.
3. Day-count: Account365 for annualization past a year (the July draft spec's default), recorded in `dim_return_method`; a change is a
   new method version, not a re-sign.
4. The retiring flow engine's parity work is NOT reused as a module; its classification tables (the 187-code Schwab table, the flow
   ledger's classes) are read as DATA by the 49 Financial adapter. No import of `c02_twr_engine.py`.
5. Schwab bank-sweep interest: only clearly classified interest counts as income; the rest is `UNRESOLVED` and is not income. Schwab
   foreign-tax `WD` is withholding, not a withdrawal.
6. The household union-find stays where it is until ADVI_FIRMBKTS moves it; `account_dim` reads it through the adapter with the address
   printed, and a change of home is that project's, not a rider here.
7. C-LEASE governs F beside DSGN_IRPTV1: under a live FAST lease the seat builds F's items as closer-drive items reading this PRD; under
   FULL, F's orders name the two paths only. The benchmark overlay is a later enrichment, not round 1. The Holdings tab's Allocation
   panel (AD-03 removes it) is not replaced by this project's allocation-change view; that view lives on the reporting surface.
8. Presets: 1M, 3M, YTD, 1Y, since inception, plus the custom pair and the brush; the design closer may re-order, never remove the custom
   pair.
9. Nothing in this project sends a notification, builds a monitor, or opens a second performance figure beside IRPT_BCKEND's on one page.
10. Any new capability (a benchmark, a money-weighted view, fees) is a PRD addendum with the next unused FWD id.

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim` names the evidence class of the address. `measured` means read at L4 (2026-09-30 ~13:5xZ) by this seat; paths and line numbers
cited from the briefs are `held` from the CRO's subagent reads unless stated. NEW surfaces are `unmeasured`.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S01 | FWD-1, FWD-9 | the 49 Financial adapter (NEW) reading Schwab silver `dim_position`, `dim_balance`, `fact_trn`, `fact_uln`, `fact_rld` | unmeasured; the silver names are held (register brief `irpt-holdings-basis-silver-inventory-brief-20260928.md:75-97`) | -- | B / DS | wire | S03 | FWD-1 | firm codes stay inside it |
| S02 | FWD-1, FWD-8 | gold `account_return_daily` at `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=<D>` (builder output) with C-GUARD | unmeasured | `address()` printed at L4 | B / DS | wire | S01, S04 | FWD-1 | contract file first |
| S03 | FWD-9 | contract files `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`, `..._SERIES_CONTRACT.json` (NEW), then one per table | unmeasured | C-SHAPE, C-SEAM | B | wire | -- | FWD-9 | schema hash equal across firms |
| S04 | FWD-8 | `holdings_price_return` from IRPT_BCKEND's gold (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py:12-29`) | held | brief Part IV.3 | IRPT_BCKEND | consume | -- | FWD-8 | the guard rail |
| S05 | FWD-1 | the platinum publisher `irpt-49f-reporting-publish-lambda` on `irpt-49f-reporting-publish-daily` (NEW) writing `series.json.gz` and `manifest.json` at the builder's addresses | unmeasured | `name()` and `address()` printed at L4 | B / AE | wire | S02, S03 | FWD-1 | its own schedule |
| S06 | FWD-1 | the Performance page reading `series` (`portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx:450-484` is today's per-window fetch) | held | frontend brief Part IV.2 | F | wire | S05 | FWD-1 | no per-window request |
| S07 | FWD-8, FWD-10 | the method label and the coverage sentences (`MethodAndSources.tsx:32-63` is the wrong label today) | held | frontend Part IV.7 | F | wire | S06 | FWD-10 | C-LABEL, C-HONESTY |
| S08 | FWD-8 | the tie-out harness against Black Diamond `performancePeriod` for the sample accounts (NEW; IRPT's existing per-account call) | unmeasured | brief Part IV.6 | B | measure | S02 | FWD-8 | per-use gate; no new pull |
| S09 | FWD-3 | gold `account_class_daily` at `.../gold/account_class_daily/date=<D>` and the `etf-classifications` read | unmeasured; the table is held (`assetClass.ts:30,66-76`) | `address()` printed at L4 | B | wire | S02 | FWD-3 | classes sum to the account |
| S10 | FWD-4 | gold `account_activity_daily`, `account_lot_realized`, `account_lot_unrealized_daily` (NEW) | unmeasured | C-GAINS | B | wire | S01 | FWD-4 | RLD vintage confirmed |
| S11 | FWD-5 | gold `account_transaction` at `.../gold/account_transaction/date=<D>` and its paged platinum files | unmeasured | `address()` printed at L4 | B | wire | S01 | FWD-5 | Opal vocabulary |
| S12 | FWD-6 | `market_topic_daily` in the general platinum home (its scope row first; builder REFUSED `scope 'opal'` at L4) and the episode list in `series` | unmeasured; the news tables measured live by the CRO 2026-09-30 | C-SOURCES, C-TOPICS | B | wire | S05 | FWD-6 | market-wide, labelled |
| S13 | FWD-2 | the Inflection and Cottonwood adapters (NEW) | unmeasured | C-ADAPTERS | B / DS | wire | S03 | FWD-2 | same schema hash |
| S14 | FWD-7 | `account_dim` and the household and client platinum files (NEW); the household union-find (older bucket tree, held) | unmeasured | brief Part IV.6 | B | wire | S05 | FWD-7 | never crosses a firm |
| S15 | FWD-3..FWD-7 | the views: class rows, allocation change, activity and gains, transactions, topic panel, account picker (NEW under `tabs/reporting/` and `dashboard/`) | unmeasured; prior art held (`TopicCloud.tsx`, `PeriodInContextPage.tsx`) | frontend Part V.2 | F | wire | S06 | FWD-3..7 | C-DESIGN, C-LEASE |
| S16 | FWD-1 | the time-to-paint and file-size measurement on the real page (NEW) | unmeasured | Andrew's target | F + B | measure | S05, S06 | FWD-1 | printed, never estimated |
| S17 | FWD-9 | `reporting_policies.json` rows for the eight tables (`infra/logic/registry/reporting_policies.json`; ABSENT today) | measured (file); rows unmeasured | brief Part IV.2 | LGIC / B | wire | -- | FWD-9 | policy rows, not typed keys |
| S18 | FWD-1..FWD-10 | NEW journey test across S01-S17 | unmeasured | the ten ACCEPT lines | verification | verify | S05, S06 | all | reads served artifacts and the real page |

MECE check: outcomes 10 of 10 have at least one row. Every dependency named in section 5 has a row or is named as owned elsewhere (S04,
S09's table, S12's news tables, S14's union-find). Relied-on work has no row by design.

## 8. BRIEF COVERAGE -- content carried, not just cited

| Brief heading | Carried content | Consuming sections / surfaces |
|---|---|---|
| Backend Part I (O1-O8, out of scope) | the thread and the territory; net worth out | ENDPOINT; provenance |
| Backend Part II (boundary) | owns the gold, contracts, adapters, method, publisher; relies on IRPT_BCKEND, MDPF_SECCLASS, news, LGIC, silver, the portal | section 5; C-CLASSES, C-GUARD, C-TOPICS, C-NAMES |
| Backend Part III (the bar) | O1, O2, O8, O6 pass conditions | ENDPOINT ACCEPT lines; S08, S16 |
| Backend Part IV.1-2 (tiering, builder) | platinum is the only JSON; builder addresses; no `reporting` policy row; slash partitions refused | C-TIERS, C-NAMES, C-SOURCES; S05, S17 |
| Backend Part IV.3-5 (existing gold, label, latency) | price-only columns, no flows or income; wrong label; 6.7 s median, per-date reads | C-GUARD, C-LABEL, C-SERVE; S04, S06 |
| Backend Part IV.6 (data by firm) | Schwab, Orion, Black Diamond inventories; lots by firm; BD endpoints not ingested | C-ADAPTERS, C-GAINS; S01, S13, S14 |
| Backend Part IV.7 (return machinery) | retiring engine; July draft spec; code table; flow ledger classes | ruling 6.4; C-METHOD |
| Backend Part IV.8 (news) | curated topics from 2025-11-21, phrases from 2025-12-01, empty ticker tags, 14-day drilldown, narrative episode logic | C-TOPICS; S12 |
| Backend Part IV.9-10 (classes, DQ rows) | the class vocabulary; S184, S189, S212, S173, S152 | C-CLASSES; C-GUARD; coverage states |
| Backend Part V.1 (tables, coverage) | the eight tables; the closed vocabulary | C-SHAPE, C-COVERAGE; S02, S09-S12, S14 |
| Backend Part V.2 (adapters) | one per firm; BD as tie-out not source | C-ADAPTERS, C-TIEOUT |
| Backend Part V.3 (total return) | the method, flow timing, Dietz, cash in V, income on receipt, fees, the three guards, periods, in-kind, corporate actions, the method row, open items | C-METHOD, C-FLOWTIME, C-GUARD, C-VALUE; rulings 6.1-6.5 |
| Backend Part V.4-5 (gains, fee rail) | lots and activity; the rail | C-GAINS, C-FEERAIL |
| Backend Part V.6-7 (serving, topics) | series, manifest, pages, household files; episodes in series; market-wide topics; MISSING_HISTORY | C-SERVE, C-SEAM, C-TOPICS |
| Backend Part VI-VIII | round structure; decisions carried; not claimed | sections 2-3; ruling 6; provenance |
| Frontend Part I (F1-F9) | the views; net worth out | ENDPOINT |
| Frontend Part II-III | boundary; the bar | section 5; ACCEPT lines; S16 |
| Frontend Part IV | route and tabs; per-window fetch; absent views; recharts and visx; colour law; class order; wrong label; narrative prior art; older briefs and ADs | C-DESIGN, C-LABEL, C-LEASE; S06, S07, S15 |
| Frontend Part V | one load, browser compute; the views; coverage states; loading; print and export | C-SEAM, C-HONESTY; backlog F; S15 |
| Frontend Part VI-VIII | round structure; calls; not claimed | sections 2-3; rulings 6.7-6.8 |
| Andrew messages 1-6 | the request; five answers; gold is the Opal shape; GIPS rulings; the rail; the two-methodology question | provenance; C-TIERS, C-METHOD, C-FEERAIL, ruling 6.1 |

## ADDENDUM v0.2 -- the L4-R review's four items ruled (L4; outside the ENDPOINT section, so no half re-opens)

**Source.** `3.0.0_SA_CVO`'s review `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_IRPT_DASHBD_v0.1_20260930.md@14d5546fb8`
(SIGN @9914eab4f4; W1, Q1-Q4). Ruled by `1.0.0_SA_CTO` 2026-09-30 ~14:3xZ under the self-drive rule (nothing waits on Andrew).

11. **Q2, the tie-out tolerance (FWD-8 "a tolerance Andrew accepts") is NOT a wait.** The tie-out tolerance is a second number,
    distinct from C-GUARD's daily guard tolerance. Round 1 of workstream B MEASURES the 49 Financial sample's agreement
    distribution against Black Diamond's own return (per account and window: median, p90, max of the absolute difference, with
    each disagreeing day's stated reason) and PROPOSES the tolerance from it; `1.0.0_SA_CTO` rules it on read of the measurement
    and it lands in `dim_return_method` as `tieout_tolerance` with the ruling's record cited. Andrew's word, when he gives one,
    is recorded and supersedes the ruling; the ENDPOINT text is unchanged (an ENDPOINT edit would re-open the half for a
    wording gain of nothing), and its ACCEPT line is read with this ruling.
12. **Q1, the coverage vocabulary is decided in the contract file, with its record.** `IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`
    (round 1, workstream B) carries the rule-24 four-postulate record and word-boundary census for every enum it declares. The
    CVO's finding is accepted: C-COVERAGE's list mixes three intents. The contract splits them: `history_scope` (FULL,
    PARTIAL_HISTORY, MISSING_HISTORY), `day_quality` (MEASURED, FLOW_UNRECONCILED, LARGE_FLOW, NOT_MEASURABLE, SOURCE_LAG) and a
    per-column null reason (NO_LOTS, UNCLASSIFIED_HOLDINGS) as `<column>_reason`; `return_basis` is closed (TWR, HOLDINGS_INCOME_FALLBACK,
    NOT_MEASURABLE); the fee-rail fact lives ONLY in `dim_return_method.fee_basis` and is not a row marker. C-COVERAGE's text is
    read as superseded by the contract file once it lands; the frontend maps each member of each axis to one sentence (C-HONESTY).
13. **Q3, the asset-class vocabulary's authority.** Until MDPF_SECCLASS lands a class value list in
    `org/standards/MDPF_SECCLASS_CONTRACT.json`, the authority is the portal's `HoldingAssetClass` type in
    `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts` (eight values, the IV-e-115 order); the `account_class_daily`
    contract cites that file and its pin, and a later MDPF_SECCLASS list supersedes it by addendum, never silently.
14. **Q4, the general platinum home for `market_topic_daily`.** The round that builds FWD-6 applies `02_DOCTRINE.md` R6 (line 397,
    `opal-data-portal-v2/platinum/` as general platinum) unless the topics source gains a general-tenancy scope row, in which case
    line 409 applies; the cell prints which rule it applied and the builder's `address()` output beside it.
15. **W1.** The endpoint's FWD-1 SOURCE line names "COO~P record"; the record path is
    `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_052xZ_PRECOMPUTED_GZIP_JSON_REPORTING_UNDER_2S_AND_PUSH_MANAGED.md`
    (cited in the PRD header); the ENDPOINT bytes are not edited for it.

## ADDENDUM v0.3 -- C-SOURCES and S17 corrected for gold (L4; outside the ENDPOINT section, so no half re-opens)

**Source.** Row `IRPT_DASHBD-S1` @85863e9b5a (0.4.0_DS_ClientPlatform~S, measured: `lib/opal_naming.py`'s validator admits a
`reporting_policies.json` family only at tier {state, platinum} with extension {csv, json, pdf}; tier gold refuses on every
extension, a nine-way matrix), raised by `2.0.0_SA_COO~P` as 103354. Ruled by `1.0.0_SA_CTO` 2026-09-30 ~18:0xZ.

16. **The reporting-policy register does not cover gold, and this PRD was wrong to say it did.** `reporting_policies.json` records
    the retention and disposal of CLIENT-FACING artifacts (state and platinum), not of an internal parquet table. So: the eight gold
    tables need NO policy row; rule 30 is satisfied for them by `address()` and `name()` output alone (both answer for
    `account_return_daily` and `dim_return_method`, measured by the row). The round-1 policy rows are for the PLATINUM served files
    only (`series.json.gz`, `manifest.json`, and later the transactions pages), which the register admits. C-SOURCES's sentence "a
    policy row this project adds in round 1 with the first contract" and S17's surface "`reporting_policies.json` rows for the eight
    tables" are read as superseded by this ruling: S17 becomes "policy rows for the platinum served files". No request goes to the
    LGIC lane to widen the register to gold. `2.0.0_SA_COO~P` amends DB-1-AC1 to drop its gold policy-file half; the emit was never
    blocked.

