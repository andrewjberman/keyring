# Cottonwood "Supervised vs Unsupervised" — the field trace (Andrew-direct task, 2026-08-20 ~1555Z)

**Task (Andrew-direct at the CTO terminal, VERBATIM):** *"check the teams thread with Me, Manav, and
Yang... I have also recorded a HAR where i check out the Black diamond dashboard to see if i can
identify where this 'supervised' vs 'unsupervised' field might be. It seems to me that we should be
able to toggle this somehow, im just not sure in what data table in the Cottonwood process it would
appear that would facilitate that, but that is your task to go figure out."*
**Business ask (Teams, group 19:3a715f69...):** Manav 1452Z: Stephen says dashboard AUM looks off —
shift to BD's "Supervised assets/all billable" (~$455M). Manav 1458Z: the current figure includes
AUM outside Cottonwood that clients inputted into BD (~$30-40M). Andrew: BD aggregate ~487M, our
dashboard ~480M — find the ~30M that should NOT be covered.

## 1. The BD mechanism (from the HAR, 59 entries, bd3.bdreporting.com)

- **The toggle is a first-class BD filter**: `supervisedFilterType` in every Dashboard API body —
  enum from BD's own JS: **1 = All Assets, 2 = Supervised, 3 = Unsupervised** (advisor-view module,
  `pe=[{text:"All Assets",id:1},{text:"Supervised",id:2},{text:"Unsupervised",id:3}]`). It persists
  server-side via `POST /advisor/api/v1/Dashboard/{id}/experiencesettings`.
- **Every API row carries the split regardless of filter**: `bmv/supervisedBmv/unsupervisedBmv` and
  `emv/supervisedEmv/unsupervisedEmv`, at PortfolioGroup, Relationship, AND Account grain — i.e. BD
  decomposes a single ACCOUNT into supervised/unsupervised SLEEVES (one account can carry both).
- **Numbers reconcile with Manav**: the HAR's firm-wide totals read All=$2.903B / Supervised=$2.745B
  / Unsupervised=$158.2M; one PortfolioGroup row carries **supervisedEmv $458.35M ≈ Manav's ~$455M**;
  the drilled relationship scope shows $48.5M unsupervised across 102 account rows.

## 2. The Cottonwood pipeline answer (the actual task)

**Today the field does not exist anywhere in the cot pipeline — measured, not inferred:**
- `comp-find -i supervised data/` → 50 hits, **every SURFACED hit is 49F-side** (bd49f silver/gold),
  zero in `data/cot/`.
- The live holdings extract (`s3://opal-data-cot/forwardfill_v2/holdings/HOLDINGS_DAILY_2026-08-19.xlsx`,
  written this morning, T-1-healthy) carries **19 columns; supervised columns: NONE** (header read).
- So every downstream AUM sum (silver merge → gold canonical holdings → AUA/serving) counts
  supervised + unsupervised alike — the ~$30M of client-inputted outside assets is IN our figure by
  construction, matching 487-455 ≈ 32M.

**Where the field is AVAILABLE, one config away:** BD's DataMining dimension catalog (embedded in our
own captured `realized.json`/`unrealized.json` template bodies) exposes:
- **`Account Supervised`** (mappedColumn `accountSupervised`, enum {Supervised, Unsupervised}) — the
  Account-level dimension catalog (81 dims);
- **`Holding Supervised`** (`holdingSupervised`, same enum) — the Holding-level catalog (51 dims).
The cot ingest's own design says templates are CONFIG: *"a template updates by re-uploading its
JSON — no code change"* (`cot_bronze_ingest.py:21-24`). `holdings.json` is a THIN reference (persisted
templateId, body stored BD-side), so the act is: amend the persisted holdings template to select the
two columns (re-capture/re-provision), and the extract gains them the next scheduled run.

**Which table the toggle lives in (the direct answer to the question):**
| layer | table/home | field |
|---|---|---|
| bronze | `forwardfill_v2/holdings/HOLDINGS_DAILY_*.xlsx` | `Holding Supervised` (+ `Account Supervised`) — added at the template |
| silver | `cot_silver_merge` fact holdings (schema-tolerant: snake_cases whatever arrives → `holding_supervised`/`account_supervised` flow through) | same, snake_cased |
| gold | `B_00.canonical_holdings` (fact grain — **the primary toggle home**: filter/aggregate by `holding_supervised`) + `A_00.accounts_dimension` (`account_supervised` as an account attribute) | the toggle = supervised-only sum vs all-assets sum |
| serving | the AUM/AUA gold consumers (C_01 canonical_nna / C_01c role_aua / C_04 validate_aua chain) emit BOTH figures (`aum_supervised`, `aum_all`) so the dashboard can toggle — mirroring BD's own always-carry-the-split design | |

**HOLDING grain is the correct primary field, not Account** — the HAR proves accounts carry BOTH
supervised and unsupervised sleeves simultaneously, and the estate already learned this on 49F:
`bd49f_dim_portfolio_group.py:197-209` — *"`account_supervised` splits an account into Supervised and
Unsupervised sleeves"*, book key (group, account, supervised), 29,926/29,926 keys clean. The 49F
silver (`bd49f_fact_allocation.py:112`) already ingests "Account Supervised" — the in-estate
precedent for both naming and handling.

## ADDENDUM ~1635Z — Andrew's two follow-up legs, investigated (VERBATIM: *"there should be a way to
do this retroactively through some kind of filter, also it appears that cottonwood uses the
'portfolio_group' key to split advisors, i need CTO to investigate these"*)

### A. RETROACTIVE — Andrew's intuition is CORRECT, and the HAR proves the design

**The decisive measurement:** at Account grain, **0 of 102 accounts** in the HAR's unsupervised drill
carry both supervised and unsupervised value — in the Cottonwood book, supervised/unsupervised is
CLEAN AT THE ACCOUNT LEVEL (unlike 49F's sleeve-split book). The unsupervised accounts are dedicated
held-away/client-inputted entries — the names say it: "Greenbrier - Joseph Clark", "19 Watertree Dr",
"Richwoods Home" (properties, not custodied positions).

**Therefore the retroactive filter is a DIMENSION JOIN, not a history re-pull:** one pull of the
current account→`Account Supervised` mapping, joined onto ALL existing historical holdings by
`AccountID` (already one of the extract's 19 columns), reproduces BD's split for every historical
date. Tie-out oracle from the HAR (2026-08-19): firm $488,753,694 all / **$458,351,400 supervised /
$30,402,295 unsupervised**; named-books subtotal $455,532,550 = Manav's "$455M" exactly.
**Caveats, named:** (1) the join applies TODAY'S flags to history — an account that flipped
supervision status in the past misclassifies before its flip (acceptable for dashboard AUM; BD's own
dashboard history behaves the same way); (2) the 0/102 measurement is one-sided (the HAR has no
supervised-side account drill) — closed going forward by adding `Holding Supervised` to the daily
holdings template, which makes the account-clean assumption a DAILY-TESTED invariant instead of a
one-shot observation.

### B. PORTFOLIO_GROUP = THE ADVISOR BOOKS — confirmed, and the pipeline gap located to one line

**Confirmed from the HAR:** the PortfolioGroup rows ARE the advisor books — Jay Rubottom $289.9M /
Stephen Shipley $135.2M / Christa Bass $45.0M / "No Portfolio Group" $18.8M (of which $12.1M
unsupervised — the strays and the held-aways overlap heavily). Same BD firm convention as 49F's
`dim_portfolio_group`.

**The pipeline gap, mechanism at source:** `A_00.accounts_dimension.py` DECLARES `portfolio_group`
in its output columns (:95, :591) — and the served dim (943 rows, 23 cols, read live) DOES NOT
CARRY IT. The drop is `:599`: `available = [c for c in output_cols if c in accts.columns]` — a
SILENT-DROP filter; the transactions extract never carries "Portfolio Group", so the silver never
has it, so the gold drops it without a word (also dropped the same way: implementor, consultant,
local_ops, manager, investment_strategy_name). A declared output column silently missing from the
served artifact is its own small defect class — the fix TO should add a loud print for dropped
declared columns.

### C. ONE FIX SERVES BOTH LEGS

**A single account-attributes pull** (small DataMining template at Account level, or the holdings
template extended): `AccountID, Account Supervised, Account Billable, Position Only, Portfolio
Group` → lands as/joins into `A_00` accounts dimension →
1. retroactive supervised filter = the dim join above, tie-out against the HAR oracle;
2. `portfolio_group` populates the declared-but-dropped column — advisor books keyed the BD-native
   way (complementary to A_01's transaction-role fee-split model: roles = fee economics, group =
   book membership);
3. `Holding Supervised` added to the daily holdings template as the forward belt.
**Data-hygiene finding for Manav/Cottonwood:** the "No Portfolio Group" bucket ($18.8M, 12.1M of it
unsupervised) is real book-assignment hygiene on their side — worth a line back to them.

## 3. Caveats + routing

- **History**: the supervised flag is a CURRENT attribute in BD; a backfill re-pull applies today's
  flags to past dates. Fine for the dashboard-AUM purpose; named so nobody reads a backfilled split
  as point-in-time truth.
- **Verification against BD**: after the template change, one tie-out — our supervised-only sum vs
  BD's `supervisedFilterType=2` total on the same date (the HAR gives the exact API shape).
- **Execution routing** (Andrew's/COO's call, not taken here): template amendment + silver/gold legs
  sit in the cot lane (bronze fetch owner `0.6.2_AE_PartnerETL`; gold/silver per Rule 13). The change
  is small: one BD template amendment (config), zero silver code (schema-tolerant), one gold leg
  (carry the split + emit both AUM figures).
