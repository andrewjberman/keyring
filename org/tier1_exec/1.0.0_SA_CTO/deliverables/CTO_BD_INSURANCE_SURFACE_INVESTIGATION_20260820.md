# The BD insurance/annuity surface — what is exposed, and the prior art (Andrew-direct, 2026-08-20 ~1845Z)

**Task (Andrew-direct, VERBATIM):** *"I see these are the insurance plans. I need you to go
investigate the insurance endpoint and see what data is exposed there. We should have investigated it
before there should be HARs and prior art on the subject in the DATA_PLATFORM and maybe
DATA_ANALYTICS project content."*
**Predecessor:** `CTO_COT_BD_PLANE_GAP_ACCOUNT_LEVEL_DIAGNOSIS_20260820.md` — the 91 outside-feed
accounts carrying 100.0% of the $8,617,838.30 supervised gap.

## 1. Andrew's read is confirmed, and the estate already classified this cohort

`docs/briefs/derisk2_census/census_fully_non_schwab.csv` — a prior census of **FULLY_NON_SCHWAB**
accounts, each typed `INSURANCE_ANNUITY` or `INSURANCE_OTHER`, each carrying the marker
**`NO_BD_TXN_EVER`** (Lincoln structured, SLAT structured, unnamed carrier policies; individual
accounts at $1.7M–$3.7M). Sibling censuses: `census_held_away_in_schwab.csv`, `census_non_schwab_all.csv`.
**We measured this cohort before and named its defining property: these accounts have NO transaction
history in Black Diamond at all** — consistent with today's finding that they carry no custodial
position rows and therefore never appear in a positions/transactions export.

Second, independent piece of prior art: **`data/cot/scripts/gold/insurance_accounts.json`** (109
account ids, mirrored on the 49F side) exists precisely because *"Insurance and annuity accounts
report on monthly or quarterly statement cycles… the standard 45-day AP gate incorrectly excludes
them during inter-statement gaps"* — so they get a **180-day gate**. **The estate has already
encoded, in production, that this cohort updates on a statement cycle rather than daily.**

## 2. THE ANSWER TO THE OPEN QUESTION: the surface exists, and it is qt6

`data/black_diamond/API/domains/datamining/QUERY_TYPES.md` (2026-07-08, DATA_PLATFORM D2b) catalogs
six BD DataMining query types. Five are ingested by the Cottonwood ETL (qt1 holdings, qt2
transactions, qt3 realized, qt4 unrealized, qt5 allocations). The sixth:

> **qt6 — "BI Billing" — Account × Month grain — 8 levels — 158 dimensions — measures BMV, EMV,
> Additions, Withdrawals, Net Flows, Fees, Net Gain, Income. Ingested by cot ETL: NO — "the gap".**

**qt6 is the BI dashboard's own query type.** Its measures (BMV/EMV) are exactly the fields the BI
dashboard renders and exactly the fields my account-level diff pulled today. Verified in the
committed catalog sample (`qt6_dimensionsfacts_response_sample.json`, 174 items) that qt6 exposes the
full account identity and both supervision flags:

| dimension | mappedColumn | id |
|---|---|---|
| Account Number | `accountNumber` | 36425 |
| AccountID | `accountExternalID` | 198 |
| Account Name | `accountName` | 24 |
| **Account Supervised** | `accountSupervised` | 33 |
| **Holding Supervised** | `amrSupervised` | 46939 |
| Portfolio Group | `portfolioGroup` | 1140 |
| Relationship Name | `relationshipName` | 1142 |
| Account Billable, Account Category, Billing Configuration/Discount/Team, Rep Fee Split | (billing family) | — |

**So the remedy for the $8.6M is almost certainly a QUERY-TYPE gap, not a vendor limitation:** the
accounts BD's dashboard values are reachable through the same DataMining machinery we already
operate, under a query type we have never ingested.

## 3. Two paths, both live-exercised today

- **PATH A (architecturally correct): ingest qt6.** Same persisted-template mechanism as our other
  five tables (`/datamining/request/v1/template/` → `/v1/run` → export). The catalog, the field
  inventory, a create-request sample (`qt6_template_create_request.json`) and a full fee-probe trace
  (`qt6_fee_probe_full_trace.md`) are all already committed from the D2b work. Grain is Account ×
  Month — the right grain for an AUM/billing figure, and it carries the supervision flags natively.
- **PATH B (proven working, today): the BI dashboard API.** `POST /advisor/api/v1/Dashboard/data`
  at `levelType: "Account"` returns all 923 accounts with `emv`/`supervisedEmv`/`unsupervisedEmv` —
  this is what I used to build the diff, and it reconciled to the cent. It is a serving API rather
  than an export API (no per-holding detail), so it is a good *validation oracle*, not a good
  pipeline source.

**Recommendation:** Path A for ingest, Path B retained as the standing tie-out oracle (it is the
only source that reproduces the dashboard's own number by construction).

## 4. Findings surfaced along the way (no action taken)

1. **The July sweep's query-type catalog is EMPTY and nobody noticed.**
   `s3://opal-data-cot/code/bronze/endpoint_catalog/querytype_catalog.json` is **2 bytes — `{}`**,
   written 2026-07-08 beside a 75KB endpoint-sweep result. The QUERY_TYPES.md prose was authored
   from other evidence, so the *doc* is right while its *machine artifact* is empty — a silent-empty
   that a future consumer reading the JSON (not the prose) would read as "no query types exist."
   Same class as the day's other silent-empty findings; routes to the DATA_PLATFORM D2b lane.
2. **qt1's server-side selection has never been dumped** (QUERY_TYPES.md calls it *"the one
   persistent gap"*, D2 spec §7, open since 2026-06-26) — which is exactly why nobody could see that
   our holdings template's population excludes the outside-feed accounts. Today's diff is, in effect,
   the first measurement of what qt1's persisted selection actually covers.
3. **The insurance cohort's statement-cycle nature is already production-encoded** (180-day AP gate)
   — so any qt6 ingest must respect monthly/quarterly refresh semantics: a daily freshness check
   over insurance accounts will false-alarm exactly the way the 45-day gate did.

## 5. What I did NOT do

No template was created or mutated on the vendor system; all live calls were read-only (token mint,
dashboard data reads, catalog reads). The qt6 live exercise — create a scoped qt6 template, run it
for 2026-08-19, and confirm the 91 missing accounts appear with their supervised flags — is the
decisive next act and is a ~30-minute lane task, not a CTO act.
