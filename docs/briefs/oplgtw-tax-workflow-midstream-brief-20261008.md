# NFRA_OPLGTW v2.1 -- what the gateway must give Alyssa for the Tax SMA quarter (MIDSTREAM brief)

**Author:** `4.0.0_SA_CRO~Z`. **For:** `1.0.0_SA_CTO~O`, `/endpoint --forward` at L2 for the v2.1 addendum.
**Asked by:** CTO~O msg 32043, on Andrew-direct ~22:0xZ
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ALYSSA_TAX_WORKFLOW_SINCE_INCEPTION_GL_LOTS_LAST4_KEY_SCHWAB_AND_BD.md`
@618699ceeb), and his follow-up at this terminal (~22:4xZ): find the three documents Alyssa put in the shared PRD
folder, "particularly the Schwab one, and identify if there is anything we're not considering as far as the Tax OPLGTW
underlying data needs workstream goes."
**Measured:** 2026-10-08 22:10-23:05Z. Read-only throughout. No account number, client name or client dollar value
is written here; accounts are named by their slot (1-15) in the Tax SMA roster workbook.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

**Honoured.** I read no NFRA_OPLGTW task order and no `phase` or `blocking` field. I read the PRD's ENDPOINT section
(FWD-1 to FWD-13) and the v2.0 addendum's purpose and acceptance lines, Andrew's record, Alyssa's workbook and
documents, the Tax SMA roster, and the served data in S3.

**Where it bent, four places:**
1. **I wrote the frame I am now extending.** The v2.0 addendum's brief is my own assessment @139c8d018e. A brief that
   extends its author's earlier brief tends to ratify it. To counter that, Part IV.B tests FWD-10 to FWD-13 against
   the workbook's fields, not against my earlier list.
2. The CTO's ask names "Round 32's OG-sc-1", and the v2.0 addendum names round 32 items 3 and 4 and rulings R50-R55.
   So I know a round is in flight that lands silver column lists and a list-only run for master 08403355. Nothing
   below depends on either.
3. I read the sibling project MDPF_TAXSMA's contract and three of its gold modules as prior art. Its decomposition
   language (cells TX-m-1 to TX-m-4) came along with them. I used it only for what it says exists.
4. The data reads in Part VI are measurements, not the branch. They do make Part I concrete in places, which is
   intended.

**Is the endpoint unchanged?** No. FWD-10 to FWD-13 hold, but Andrew's tax workflow widens them on four axes they do
not reach: a third source (Black Diamond), a since-inception window anchored on a date the custodian does not hold, an
account key that does not resolve on its own, and a backfill of the new master. Part IV.B gives each with its evidence.

---

## PART I -- THE OUTCOME TERRITORY

The person throughout is **Alyssa**, preparing the quarterly Tax SMA client update. Andrew's scope bound, verbatim:
"We don't have to do the whole workflow for her. We just have to be able to give her the right information." Every
outcome is a read. None of them produces the report.

### O1 -- CANDIDATE THREAD: Alyssa reads one Tax account's quarter, end to end, from the gateway

One account (roster slot 1, on Schwab master 08335338, the default quarter Q3 2026). Alyssa asks for its quarter
reconciliation inputs and gets: the value at quarter start, contributions, withdrawals, the value at quarter end,
realized gain/loss for the quarter, and the change in unrealized gain/loss. Today the same numbers come from a monthly
statement PDF and two Schwab Advisor Center cost-basis exports in her browser. This becomes FWD-1 of the addendum; every
other outcome widens this thread.

### O2 -- Alyssa finds the account from what her sheets hold, and never gets the wrong one

Her client update keys each client by the account's last four digits ("XXX-nnnn"). A request by last four plus a name,
or by the full number, returns exactly one account. When the key is ambiguous, the answer says so and lists the
candidates; it never picks one silently.

### O3 -- Alyssa reads any account's since-inception record as of the date she picks

For each Tax account: the value at the strategy's inception date, every flow since (contributions, withdrawals,
securities transferred in or out at market value, advisory fees), and the value on the date she is looking at. The
inception date is the Tax SMA roster's, never the custodian's account-open date.

### O4 -- Alyssa reads realized gain/loss for any window, in the four buckets her report prints

Short-term gains, short-term losses, long-term gains and long-term losses, for the quarter and since inception, at lot
grain, with totals she can tie to Schwab's own totals line.

### O5 -- Alyssa reads cost basis and unrealized gain/loss AS OF quarter end

The lots actually held at quarter end, on that date, split gains from losses and short-term from long-term, including
short positions. Today she cannot get this: Schwab Advisor Center's unrealized screen has no date filter, so her script
reprices today's lots at statement prices and adds back lots closed after quarter end.

### O6 -- The same answers for a Black Diamond account, in the same shape

For a Tax account held through Black Diamond (the Cottonwood RIA's accounts), O1 to O5 answer in the same field shape
as for a Schwab account. Alyssa does not have to know which source holds the account before she asks.

### O7 -- The Tax SMA master's accounts answer like the others, back to their inception

Accounts on master 08403355 answer O1 to O5. Their history reaches back to the earliest inception date among them,
by backfill, not only from the day collection starts.

### O8 -- Alyssa holds the access, and only the access, this needs

Her grant carries account identity, enough history for every Tax account's inception, and all three sources. The
fields Andrew kept hidden at 17:4xZ stay hidden: tax identifiers, mailing address, email and phone.

### O9 -- (Andrew: "may potentially") Top-10 holdings and sector allocation as of quarter end

Holdings with portfolio weight as of quarter end, long and short. A sector for each holding, so she can roll up an
allocation. Benchmark weights are not asked for: Andrew said the benchmark "does not matter".

---

## PART II -- WHERE THE BOUNDARY SITS

| This brief OWNS (NFRA_OPLGTW, CTO `1.0.0_SA_CTO~O`) | It RELIES ON, and does not own |
|---|---|
| What the gateway serves Alyssa: datasets, fields, windows, grants, the account lookup | **MDPF_TAXSMA** (D8): the Tax SMA roster reader, account-identity normalization (`00` + eight digits; last-four is a REJECTED form), firm routing by the roster's RIA column (49 Financial to Schwab 08335338, Cottonwood to Black Diamond). Reuse; never re-derive |
| The cross-source answer shape (O6) | **The Schwab puller and silver** (AE CloudOps lane, `infra/aws/ec2/canonical-schwab-si2/`): collection, the 08403355 list-only run, its daily pull and its backfill (CLAUDE.md rule 13) |
| Which inception date the gateway honours (O3), read from the roster | **The Black Diamond Cottonwood feed** (`blackdiamond/cottonwood/silver/*`): its producer and freshness |
| | **Alyssa's report**: `TAX/Reporting/_ReportTemplate/generate_reports.py` and `schwab_quarter_end.py` stay hers. Not built here |

**Named not-in-scope:** computing returns (QTD, YTD, since-inception annualized). Andrew asked for "the right
information", and the inputs are in O3. Whether the gateway also computes a return is his call (Part VII).

---

## PART III -- THE QUALITATIVE BAR

- Alyssa fills a quarter's client update without opening Schwab Advisor Center or Black Diamond in her browser.
- Every figure she reads from the gateway is one she could tie to the custodian's own statement or totals line. Where
  it does not tie, the answer says why.
- A lookup she starts from her own sheet's key either lands on the right account or tells her it cannot.
- Yang Liu, reviewing, gets lots as of quarter end, not today's lots repriced. That is his open question in Alyssa's
  brief (section 8, question 1).

---

## PART IV -- THE SUBSTRATE: what exists, measured

### IV.A -- Where each workbook field lives

The workbook `Tax 3Q2026 Client Update - all accounts.xlsx` (Shared site, `TAX/Reporting`) has 30 tabs: one Summary
and one Tax & Holdings tab for each of 15 accounts. All 15 match the roster's 15 filled slots.

| Workbook field (row) | Schwab 08335338 silver | Black Diamond Cottonwood silver | Notes |
|---|---|---|---|
| Account number, last 4 (7) | `fact_acc.account_id` (10 digits, `00` + 8) | `fact_holdings."Account Number"` (`*****nnnn nnnnnnnn`) | Full numbers are in the roster and in the FactSet sector export (`CLIENT:/SCHWAB/<8>.ACCT`) |
| Client name (6) | `fact_acc.account_title_line_1-3` | `fact_transactions."Account Name"`, `"Client Name"` | |
| Inception date (7) | **none**: `date_opened` is the account's open date | `fact_transactions."Relationship Inception Date"` | Roster "Inception Date" is the authority (Part VI.4) |
| Beginning / ending market value (11, 15) | `dim_balance.eqty_incl_option` | `fact_holdings` SUM("Market Value") | 9 of 9 Schwab 9/30 values tie to `eqty_incl_option` within $1; `net_mv_plus_cash` ties 0 of 9 |
| Contributions, withdrawals (12, 13) | `fact_trn` / `dim_transaction` codes (`tr_cd`, `sb_cd`) | `fact_transactions."External Flow"` (`Contribution`, `Withdrawal`, `None`) | BD labels its flows; Schwab needs v2.0's `flow_label` table |
| Realized G/L (Summary right column; Tax tab ST/LT gains/losses) | `fact_rly` (realized YTD, lot grain, monthly) + `fact_rld` (daily closings) | `fact_realized` (lot grain: Open Date, Trade Date, Cost Basis, Proceeds, Short-Term and Long-Term Gain/Loss) | |
| Cost basis, unrealized G/L (Tax tab) | `fact_ult` (lot grain, daily, with `l_s`, `h_t`, `w_s`) | `fact_unrealized` (lot grain, ST/LT split) | Tax accounts sit in `fact_ult`, not `fact_uln` (11 of 11 vs 0 of 11 at 9/30) |
| Top-10 holdings (20) | `dim_position` / `fact_rps` | `fact_holdings` | |
| Sector allocation (33) | **none** | **none** | The report uses FactSet "RBICS Focus - Economy" from a file export |
| Strategy, benchmark (8) | -- | -- | Andrew: not needed |

### IV.B -- Gaps against PRD v2.0 FWD-10 to FWD-13

| # | Gap | Against | Evidence |
|---|---|---|---|
| G-1 | **Black Diamond is not served at all.** 2 of 15 Tax accounts (slots 12, 13; RIA Cottonwood) exist only there. BD silver already carries realized, unrealized, holdings and flow-labelled transactions | FWD-10 to FWD-13 are Schwab-only | Part VI.2 |
| G-2 | **Last four is not a key.** In 08335338, 1,831 of 5,320 distinct last-four values belong to more than one account. 8 of the 15 workbook keys hit 2 or 3 accounts there. One (slot 8) hits only a different client's account | FWD-10 offers lookup "by account number" and "by a name", not by the key her sheets hold | Part VI.3 |
| G-3 | **Since inception needs a date the custodian does not carry.** For all 11 Tax accounts on 08335338, `date_opened` precedes the Tax inception, by 6 to 145 days. A window from account open, or year to date, counts activity from before the strategy started | FWD-11 says "daily and year-to-date" only | Part VI.4 |
| G-4 | **The window's floor sits in the completion records, not in silver.** Silver holds 08335338 back to 2024-07-08. The addendum measured completion markers only from 2026-08-31. 5 of 15 accounts' inception dates (2026-04-08 to 2026-08-05) fall before that | FWD-12 assumes the metadata backfill lands | v2.0 addendum item 4; roster |
| G-5 | **The 08403355 backfill is not in the outcome.** FWD-13 collects "every business day" from now. Andrew: "we will have to do a backfill ... on whatever the contents are of this new Schwab master" | FWD-13 | Andrew's record; IV.C |
| G-6 | **"Value" is a named field, and the wrong one is in the estate.** The workbook's quarter-end value is `eqty_incl_option`. MDPF_TAXSMA's contract values Tax accounts on `net_mv_plus_cash` and rejects "gross short exposure" substitutes. These accounts hold shorts (1,816 of 4,959 Tax lots at 9/30 are short), so the two fields can diverge | FWD-11 names no balance field | Part VI.5 |
| G-7 | **As-of-quarter-end lots.** FWD-11 serves lots "for a date", and `fact_ult` is a daily snapshot, so this is likely already met. It is the one thing Alyssa's own method cannot do, and Yang's review question rests on it. It belongs in the acceptance, not left implicit | FWD-11 acceptance A22 | Alyssa's `schwab_quarter_end.py`; Part VI.6 |
| G-8 | **The four-bucket realized split, and ties to Schwab's totals line.** The report prints ST/LT x gains/losses separately; Alyssa's P0 item 4 asks that totals "tie to Schwab's own 'Total Known' line" | FWD-11 says "gain/loss, holding term" | Alyssa's brief section 5 |
| G-9 | **Flows the Tax SMA uses.** These accounts are funded by securities transferred in, so "securities transfer in/out with market value" and "advisory fee" must be labelled flows, not `unclassified` | v2.0 item 3 labels from the vendor code list, with no required members | Alyssa's brief section 3; roster "Divest Securities" column |
| G-10 | **Missing cost basis.** Schwab reports "Missing" basis for some lots. Her script counts the value and excludes the gain. A served lot with no basis must say so, never read as zero | FWD-11 | `schwab_quarter_end.py` `unrealized_asof` |
| G-11 | **Corporate actions.** Her script flags symbol changes after quarter end by hand. No corporate-actions dataset is served | Not in FWD-10 to FWD-13 | Alyssa's brief P1 item 9 |
| G-12 | **Sector.** No sector source exists in either custodian's silver | Not in FWD-10 to FWD-13 | IV.A |
| G-13 | **Statement PDFs.** The report's quarter-end value and flows are read from the monthly statement today; Alyssa asks for statements by account and period (P1 item 8) | Not in FWD-10 to FWD-13 | Alyssa's brief |

### IV.C -- Can the 08403355 history be backfilled?

- **The mechanism exists.** `infra/aws/ec2/canonical-schwab-si2/sdd-backfill-08335338.ps1` pulls every SDD file for
  one master, by specific-file fetch (the GUI flag is untouched). It is resumable, has an `enumerate` mode that
  downloads nothing, and takes a `-FromDate` (default 2023-01-01). The master is a constant in it (`$MASTER = 8335338`).
  A 08403355 copy or a parameter is a code change in the AE lane.
- **Schwab served years of history for 08335338.** One wide 2023-to-now search returned 6,933 files
  (`data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md:188`).
- **The depth needed is short.** The two roster accounts found in no pulled source (slots 7 and 8, RIA 49 Financial)
  incepted 2026-09-10 and 2026-09-17. If they are the 08403355 population, about four weeks of backfill covers their
  since-inception record.
- **What decides it** is the same list-only run FWD-13 already requires: whether it returns files for 08403355, and
  from which date. Whether Schwab serves that master's files from before the login was entitled to it is unknown
  (Part VII).

### IV.D -- Alyssa's three documents in `Product-Alyssa/PRD-004_gateway-data-feeds/`

1. `assets/Schwab Data Needs Brief.md` -- every Schwab workflow (W1 to W6), the field list, P0/P1/P2 asks.
2. `assets/External Chrome Workflows Brief.md` -- her non-Schwab browser workflows (read 2026-10-08 ~17:0xZ for
   @139c8d018e; not re-read here).
3. `PRD.md` -- the PRD-004 template, unfilled. The folder also holds two intake stubs and an empty `alyssas-notes`.
   A related file outside the folder, `Product-Alyssa/_handoff-andrew-2026-10-05/REPORT-SCRIPTS.md`, lists her report
   generators, the Tax SMA PDFs among them.

Items from her Schwab brief that **FWD-10 to FWD-13 do not cover**, beyond G-7 to G-13 above:
- W4, transition and tax-managed sell-down proposals: lot basis, ST/LT and a 30-day transaction history for the
  wash-sale review, for prospects' accounts. Prospect accounts are not in Opal's masters until they transfer. Once they
  are, FWD-11 and FWD-12 serve them.
- P2 item 11: one shared Modified Dietz return helper, so every report computes returns the same way (Part II, Part VII).
- P2 item 12: month-end AUM and account counts by master and partner, with history (W5, the board deck).
- Section 7: a view-only Schwab Advisor Center entitlement for any browser use that remains.
- Her open question 2, which other masters hold Opal-advised accounts: answered for the Tax population in Part VI.2.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The 08403355 list-only run returns files in the same shape as a control master (v2.0 item 5a).
- The completion-marker backfill for 08335338 reaches back to the earliest Tax inception date the grant must serve.
- **Andrew's word that Opal staff may read Cottonwood's Black Diamond data through the gateway.** Cottonwood is a
  separate firm. Today the gateway's Black Diamond tool is scoped to 49financial fees only. The Tax accounts under the
  Cottonwood RIA are Opal's strategy accounts, but the grant crosses a firm boundary the estate otherwise keeps.
- One identity rule shared with MDPF_TAXSMA (eight digits, `00`-prefixed; last four never a key on its own), not a
  second one.
- A sector source for O9, if O9 stays in. Today it is a FactSet file export. A vendor call needs Andrew's per-use word.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING (measured 2026-10-08 22:10-23:05Z)

1. **Workbook:** 15 accounts, 30 tabs. Strategies Tax SMA 145 (10) and Tax SMA 200 (5). Inception dates 2026-04-08 to
   2026-10-02 in the workbook; the roster has one more (2026-10-08) where the workbook's is blank.
2. **Source of each account, by full number (roster plus FactSet ids; all 15 last-fours agree with the workbook):**
   08335338 `fact_acc` 2026-10-07 holds 11 of 15; 08242234 holds 0 of 15; Black Diamond Cottonwood `fact_holdings`
   2026-10-07 holds 2 of 15 (the 2 Cottonwood-RIA slots); 2 of 15 (RIA 49 Financial) are in none of them. 08403355 is
   absent from `s3://opal-data-assets/schwab/` (children `08242234`, `08335338` only).
3. **Last-four collisions:** 08335338 `fact_acc`: 7,620 distinct accounts, 5,320 distinct last-fours, 1,831 shared
   by two or more. 08242234: 7,533 accounts, 1,789 of 5,287 shared. The two masters' account lists overlap on 7,512 ids.
4. **Inception vs account open:** all 11 accounts on 08335338 have a `date_opened` before their roster inception date,
   by 6 to 145 days (full-number join).
5. **Value field:** at 2026-09-30, `dim_balance.eqty_incl_option` equals the workbook's ending value within $1 for 9 of
   9 testable accounts (`eqty_excl_option` 2, `net_mv_plus_cash` 0). For 3 of 3 accounts tested, the workbook's
   quarter-start value equals `eqty_incl_option` on no date from 2026-06-26 to 2026-07-02. I do not know where that
   value comes from.
6. **Lots:** `fact_ult` 2026-09-30 holds 4,959 lot rows for the 11 accounts, 1,816 of them short (`current_quantity`
   below zero). `fact_rly` 2026-09-30 holds 6 of the 11. Those 6 are exactly the 6 whose workbook quarter realized is
   non-zero. Partitions: `fact_ult` 567 (2024-07-08 to 2026-10-07), `fact_rld` 815 (2023-07-12 to 2026-10-07),
   `fact_rly` 39 (month-ends, 2023-07-31 to 2026-09-30).
7. **Black Diamond Cottonwood:** `fact_holdings` 89 partitions (2026-06-09 to 2026-10-07), `fact_unrealized` 140
   (from 2026-04-22), `fact_realized` 116 (from 2026-05-22), `fact_transactions` 118 (from 2026-03-09). Every
   transaction row reads `Tax Lot Methodology` = FIFO. 916 of 14,267 transaction rows are custodied at Schwab.
8. **Workbook draft state** (it is in progress): one account's quarter reads "10/2/2026-9/30/2026"; one carries a $0
   quarter-start value with a non-zero unrealized change; one has a blank inception date.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **That the 2 unresolved accounts are on 08403355.** It fits the roster, Andrew's three sources and Alyssa's report
  that her search of both masters missed a client. It is inferred; the list-only run settles it.
- **Which Schwab master holds the 2 Cottonwood accounts.** Both are Schwab-custodied (the FactSet ids and the positions
  export say so), yet neither is in 08335338 or 08242234. They may also sit on 08403355.
- **That the lot tables tie to Schwab's totals.** I counted rows and matched values; I did not tie a lot sum to a
  statement or a "Total Known" line.
- **That Black Diamond's FIFO label and Schwab's lot method agree.** They may differ, and that would change realized
  splits between the sources.
- **That Black Diamond's realized and unrealized tables hold every lot.** I read their columns and account presence
  only. The `_s2` sibling tables hold 5 two-column rows each, which I did not open.
- **Where the workbook's quarter-start value comes from** (VI.5).
- **Whether Schwab serves 08403355 files dated before the login's entitlement.**
- **Whether the gateway should compute returns.** Andrew's words point to inputs only. Alyssa's P2 item 11 asks for a
  shared helper. This is his call.
- I did not re-read the External Chrome Workflows brief. Nothing in this brief rests on it.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/oplgtw-tax-workflow-midstream-brief-20261008.md
  PROJECT           NFRA_OPLGTW (D9); this is input to its v2.1 addendum
  EXISTING PRD      org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md (v2.0; FWD-10..13 at :129-167)
  SIBLING PROJECTS  MDPF_TAXSMA (D8): org/standards/MDPF_TAXSMA_DATA_CONTRACT.json v0.6.0 (identity, firm_routing);
                    data/mdpf/scripts/gold/taxsma_{sources,reconcile,assets}.py
  PRIOR ART         Schwab 08335338 silver: fact_acc, dim_balance, fact_ult, fact_rld, fact_rly, fact_rty, fact_trn
                    Black Diamond: s3://opal-data-assets/blackdiamond/cottonwood/silver/{fact_holdings,fact_realized,
                      fact_unrealized,fact_transactions}
                    Backfill: infra/aws/ec2/canonical-schwab-si2/sdd-backfill-08335338.ps1
                    Alyssa: SharePoint Shared/Product-Alyssa/PRD-004_gateway-data-feeds/assets/Schwab Data Needs Brief.md;
                      TAX/Reporting/_ReportTemplate/{schwab_quarter_end.py, README.md}
                    Roster: MDPF_TAXSMA_DATA_CONTRACT.json workbook.item_id (Shared site, Sheet1)
                    Sector: Shared site "Sector Allocation.xlsx" (FactSet RBICS Focus - Economy, 2026-09-30)
  ANDREW RECORDS    ANDREW_DIRECT_20261008_220xZ_... @618699ceeb; 174xZ four calls @116d52009d
  MEASURED AT       2026-10-08 22:10-23:05Z (every Part VI figure)
```
