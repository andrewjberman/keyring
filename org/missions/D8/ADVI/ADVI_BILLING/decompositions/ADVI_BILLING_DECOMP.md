# ADVI_BILLING -- L5 decomposition -- round 1 (the FWD-1 thread) -- v0.1

**v0.1** (2026-10-09 ~05:xxZ, `2.0.0_SA_COO~B2`, on PRD v0.1 @aa3d5efaa5, ADMITTED: ratified-text half signed by `3.0.0_SA_CVO`,
brief half accepted by CRO authorship). Round 1 builds THE THREAD (PRD section THREAD): FWD-1 end to end for one 49 Financial
household and one already-billed quarter. FWD-2..FWD-6 are the enrichment backlog in their numbered order and are not cut here.

```json
{
  "project": "ADVI_BILLING",
  "directive": "D8",
  "fabric": "dell2",
  "issuer": "2.0.0_SA_COO~B2",
  "round": 1,
  "decomp_version": "0.1",
  "prd_ref": "org/missions/D8/ADVI/ADVI_BILLING/prd/ADVI_BILLING_PRD.md@d45dc8a52f",
  "prd_version": "v0.2",
  "brief_ref": "docs/briefs/q2-billing-buy-or-build-brief-20261006.md@cf7721ed30",
  "endpoint_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_Q2_BILLING_BUY_OR_BUILD_20261006.md",
  "endpoint_outcomes": ["FWD-1","FWD-2","FWD-3","FWD-4","FWD-5","FWD-6"],
  "round1_outcomes_in_scope": ["FWD-1"],
  "cells_round1": 3,
  "cell_id_shape": "AB-t-<n> (shape 1 of org/standards/DECOMP_CELL_ID_CONVENTION.md; t = thread)",
  "cell_status_vocabulary": ["NOT_EVALUATED", "CUT", "BUILT", "EXERCISED"],
  "thread_quarter": "2026 Q3 (Schwab TPFEE debit 2026-07-07) unless AB-t-1 measures that debit as an advance bill for Q3 rather than an arrears bill for Q2; the cell records which",
  "portal_ref_at_cut": "portal DEV dbeb6764 (re-read at the issuance and stated in its fanout data)",
  "cut_head": "stated in the issuance commit"
}
```

## 0. What the thread is, measured before the cut

Substrate read 2026-10-09 ~04:5xZ (research for this seat, read-only; every item below MEASURED unless marked):

- **The book is Schwab master 0833 ("49 FINANCIAL"), not 0824.** The six `opal-data-bd/schwab/silver/{acc,rps,trn,...}` tables of
  the `49-schwab-conv` skill are master 0824 (Model Portfolios) and end 20260723. The 0833 silver is
  `s3://opal-data-assets/schwab/08335338/silver/fact_{acc,rps,trn,fam}/date=YYYY-MM-DD/data.parquet`
  (`data/assets/scripts/silver/silver_registry.py:167-203`), 2024-07-08 .. 2026-10-07.
- **Value:** `fact_rps.market_value_settled_unsettled` by `account_id` (10-digit) and `business_date`.
- **Flows:** gold `s3://opal-data-49financial/gold/advi/canonical/flow_ledger/` (`runners_49f/c00_flow_ledger.py:87-98`), fees
  separated as `FEE-MANAGEMENT`.
- **The debit Schwab took:** 0833 `fact_trn` rows `tran_srcde = TPFEE` ("TO ADVISOR"), amount in `gross_amount`, on 2026-04-07 and
  2026-07-07. Neighbours that are NOT the advisory fee and stay out of round 1's comparison: `SMFEE` (separate-account manager),
  `ADRF`, `FEE`, `ABFEE`; `MGFEE`/`MGFEA` are read and reported if present on the chosen accounts.
- **Who bills 49 Financial today: SMArtX, not Black Diamond** (read 2026-10-09 ~05:xxZ from the SharePoint `Shared` site,
  `Documents/Billing/`, 12 folders / 54 files, read-only, on Andrew's in-session pointer). `Opal Billing Master.xlsx`: 49F pays
  31.75 bps to Opal plus a 4.395 bps SMArtX platform fee, remitted by SMArtX. `49F/49 Financial Group Fee Statement <YYYYQn>.xlsx`
  and `49 Financial Group Deficit Report 2026Q3.xlsx` (SMArtX exports, one row per allocation/sleeve): billed IN ADVANCE; fee =
  `Current Period Estimate Valuation` x rate x `Days in Period` / 251 (trading days: 62 for Q2, 64 for Q3 2026); `Fee Debit` = Net
  SmartX + Net Advisor, and carries a prior-quarter TRUE-UP. Rates per quarter, uniform across rows read: Q2 2026 advisor 0.003000
  and UMA 0.000584178; Q3 2026 advisor 0.003175 and UMA 0.0004395 (= the Master). The "2026Q3" Fee Statement repeats Q2's rows;
  Q3's real rows are the Deficit Report's `49F Q3-26 Deficit Details` sheet. Not known from the files: the valuation date behind
  `Current Period Estimate Valuation`, the true-up method, any per-client exception. NO binary download path exists for a worker
  (the gateway returns no download URL; this box has no SharePoint sync), so round 1 carries the rates as constants on the face
  and the per-row SMArtX `Fee Debit` is read by the issuer through the gateway at the close for the thread household only.
- **Schedule (Black Diamond, a secondary reference, C-SHAPE):** `s3://opal-data-bd/silver/fees/YYYY-MM-DD.parquet` (2020-03-06 .. 2026-10-07): `basis_points`,
  `flat_fee`, `fee_schedule_type`, `fee_schedule_rate_type`, `account_fee_schedule`, `account_billable`, `billing_start_date`,
  `billing_end_date`, `account_fee`. The bridge to Schwab is `opal-data-bd/schwab/silver/account_xref/date=20260629/` (one
  partition; every row carries master 0824 -- INFERRED risk that 0833 accounts do not bridge; AB-t-1 measures it).
- **Household:** `s3://opal-data-49financial/gold/advi/dimensions/dim_relationship/date=` (`runners_49f/a01_dim_relationship.py`),
  `relationship_id` = `rel_` + md5(min account_id).
- **Where the advisor reads it:** `/advisor-intelligence` -> `_partners/49financial/index.tsx` -> `_shared/AdvisorBookClientDetail.tsx`
  (household). Today's household data comes through `opal-partners-data` (`.../platinum-summary`); a fee route is added under its
  OWN function, never inside that one's boundary (the W88-S1 trap, as IRPT_DASHBD DB-b-4).

**Builder output at the cut (rule 30, `lib/opal_naming.py` at HEAD, no refusal, no new registry row):**
`address("advi","49financial","gold","advi_billing","quarter=2026Q3")` -> `s3://opal-data-49financial/advi/49financial/gold/advi_billing/quarter=2026Q3`;
`name("advi","49financial","billing-read","lambda")` -> `advi-49f-billing-read-lambda`; `name(...,"billing-read","role")` ->
`advi-49f-billing-read-role`. Inputs are read at their live legacy keys (R19: existing pipelines are not migrated as a rider).

**Owned elsewhere and consumed, never built here:** the 0833 silver and the flow ledger (ADVI 49F runners); `dim_relationship`;
Black Diamond's fee silver (a reference, C-SHAPE); the portal shell and `AdvisorBookClientDetail.tsx` (the panel hookup is the
issuer's one line at the merge).

## 1. The seam contract (fixed at the cut; AB-t-1 writes it verbatim, AB-t-2 serves it, AB-t-3 renders it)

`org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json`, version `0.1.0`, one JSON object per (relationship, quarter) at
`address("advi","49financial","gold","advi_billing","quarter=<YYYYQn>","<client_key>.json")` (the builder admits one partition segment plus a filename):

```
contract_version, firm ("49financial"), relationship_id, client_key (the portal household key, `rel_z...`), quarter, billing_convention (ADVANCE | ARREARS | UNRESOLVED),
billing_convention_claim (measured | inferred | held | absent), period_start, period_end, valuation_date, as_of,
accounts[]: { account_id, billable_value, value_source, schedule: { label, rate_type, basis_points, flat_fee, tiers[] },
              schedule_claim (measured | inferred | held | absent), schedule_source,
              flow_adjustment, flows_in_period[], excluded_value, exclusion_reason, days_in_period, days_in_year,
              components[]: { portion (ADVISOR | PLATFORM), rate, debit_code (TPFEE | SMFEE),
                               computed_fee, debited_fee, debit_date, difference, reconcile_class, difference_reason } },
household: { billable_value, computed_fee, debited_fee, difference, reconcile_class, difference_reason },
steps[]: ordered plain-English lines an advisor reads ("why is my fee this number?")
```

**Rule 24 record for `reconcile_class`** (the one enum the thread mints):
- (i) MECE over the declared domain = one (account or household, quarter) pair after the fee is computed. Members by subtraction
  over the two facts {debit present?, |difference| <= tolerance?}: `NO_DEBIT` (no TPFEE row in the period's debit window),
  `MATCH` (debit present, |difference| <= 0.01 USD per account), `DIFFERS` (debit present, larger). Three members cover the
  2 x 2 grid because tolerance is undefined without a debit. `difference_reason` is required on `DIFFERS` and null otherwise.
- (ii) Same grain: every value is per (account|household, quarter). (iii) One axis: agreement with what Schwab took; it says
  nothing about which side is right. (iv) State coherence: a schedule correction moves `computed_fee` and may move the class;
  it never moves `debited_fee`, which only a new Schwab row moves.
- Word-boundary census at the cut: `reconcile_class` -- 0 prior uses in the corpus (the token is new; AB-t-1 re-runs the census
  and records the denominator).

`billing_convention_claim` and `schedule_claim` are the value-carries-its-claim fields (doctrine `A_VALUE_MUST_CARRY_ITS_CLAIM`):
a schedule read off Black Diamond's line is `measured` for what BD holds and the panel says so; nothing is `held` until FWD-4.

## 2. ROUND 1 (2026-10-09, issuer 2.0.0_SA_COO~B2, on PRD v0.1 section THREAD)

| cell | serves | status | risk | depends on | chain | placement |
|---|---|---|---|---|---|---|
| `AB-t-1` | FWD-1 hops 1-2: the fee recompute `data/assets/scripts/gold/advi_billing/fee_quarter.py` + the contract file of section 1. (a) Picks the thread household by rule, recorded: a 0833 `dim_relationship` household of 1-4 accounts with an EXACT row in the crosswalk `rel_to_z_mapping.json` that `runners_49f/d05_client_detail.py:72-84` reads (so the page's `client_key` reaches it), every account carrying a `TPFEE` debit on 2026-07-07 (Q3 2026, billed in advance). (b) Schedule = the SMArtX Q3 2026 rates carried as constants (advisor 0.003175 -> compared with `TPFEE`, debited 2026-07-07; SMArtX 0.0004395 -> compared with `SMFEE`, debited 2026-07-21 -- measured at the cut: 10,938 TPFEE rows on 07-07, 0 SMFEE; 5,864 SMFEE and 33 TPFEE re-debits on 07-21), `schedule_claim measured`, `schedule_source` naming the SharePoint file; Black Diamond's fee line for the same account, where the bridge reaches it, is printed beside as a secondary reference (a bridge miss is recorded, never blocking). (c) Computes per account and household: fee = billable value x rate x 64 / 251; the valuation date is MEASURED by testing the candidates (2026-06-30, 2026-07-01, the last business day before the debit) against the two debits and recording which reproduces them; then ONE comparison per portion with the actual debit (C-TRIAL-FIRST: a one-time check, never a standing comparator), `difference_reason` stated per `DIFFERS` (the prior-quarter true-up, which this round does not model, is the expected first reason and is named as such when the residual equals a Q2 estimate-vs-actual difference). No dollar figure of any client lands in the repo: per-account values live only in the gold object; records carry counts, classes and masked ids. (d) Writes ONE `fee_quarter.json` at the builder address for the thread household; ledger `advi-billing-fee-quarter-49f-r1-20261009` opened and closed. | NOT_EVALUATED | WORLD (new gold object; nothing reads it) | none | A | dell2 worker |
| `AB-t-2` | FWD-1 hop 3: the read route `advi-49f-billing-read-lambda` -- source `infra/aws/lambda/advi/billing-read/entry.py`, root `infra/aws/terraform/advi/billing-read/`, mirroring `infra/aws/terraform/investor-reporting/reporting-read/` and `infra/aws/lambda/investor-reporting/reporting/entry.py` -- serving `GET /api/scoped/partners/books/relationship/{clientKey}/fee-quarter/{quarter}` from AB-t-1's object; the viewer is scoped as `opal-partners-data` scopes its relationship routes (firm from the claims, the advisor's book, pseudonymization: `lambda_function.py:1853-1857`), so an advisor outside the household's book is refused, IAM read-only on `opal-data-49financial/advi/49financial/gold/advi_billing/*`. A local invoke against the REAL object proves the bytes and the refusal branch (an out-of-scope relationship refused). Terraform plan printed; NO apply in the cell. | NOT_EVALUATED | WORLD (a new served function planned; no apply) | AB-t-1 (reads its object) | A | dell2 worker |
| `AB-t-3` | FWD-1 hop 4: the advisor panel -- new `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.tsx` + new `portal/src/api/endpoints/advi-billing.ts` -- rendering section 1's contract: household fee, per-account lines (value charged on, schedule, flow adjustment, exclusions), computed vs debited with `reconcile_class` and reason, the `steps[]` lines, and each `*_claim` shown as a source note. Built against a fixture that is the contract's own example, until AB-t-2's route is served; the panel's hookup into `AdvisorBookClientDetail.tsx` is NOT the cell's (issuer adds it at the merge). | NOT_EVALUATED | LOCAL (portal DEV only; the page is client-facing, so PROD waits on Andrew's word per d92d08c448) | none (the contract is fixed here) | B | dell2 worker, `--portal-ref` |

**Chain read.** M = 2: chain A = `AB-t-1` -> `AB-t-2` (the route serves the object the recompute writes); chain B = `AB-t-3` (built on
the contract fixed in section 1, no data edge). N = 2, K = 8. Write sets are disjoint: A writes `data/assets/scripts/gold/advi_billing/`,
`org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json`, the one gold key, `infra/aws/lambda/advi/billing-read/`,
`infra/aws/terraform/advi/billing-read/`, `lambda-source-map.json` (new entry) and its ledger; B writes the two new portal files only.

**The close (the one real run of FWD-1).** After both chains drain: the issuer applies `infra/aws/terraform/advi/billing-read/` under
its own ledger (a new function and route; no existing served key moves), adds the panel hookup on portal DEV, and reads the thread
household's fee panel on the running DEV page with real served data (`/frontend-dev`, screenshot committed under
`deliverables/2.0.0_SA_COO~B2/`). WORLD cells add the CTO's exercised read.

**Battery.** `comp-iam` -- RUN at the issuance against the planned `advi-49f-billing-read-role` (the thread touches IAM).
`comp-schedule`, `comp-adversary` and every catalog lens -- DECLARED-NOT-APPLICABLE: thread round; the lens runs on the enrichment
round that touches its surface. `comp-blast` -- RUN as a reading: every write is a NEW key, function or file; 0 existing readers of any
written key (the `advi_billing` prefix is new).

**Seating.** Chain A -> `0.9.0_WK_ADVI_BILLING~1`; chain B -> `0.9.0_WK_ADVI_BILLING~2` (worker subagents of `2.0.0_SA_COO~B2`, one
worktree each from the current branch).

**Carried, not cut (enrichment backlog, PRD order):** an SMArtX statement ingest (the per-allocation export into bronze; needs a
download path the gateway does not offer today) and the true-up model; FWD-2 (firms' answers, held by Andrew -- the sequence's
WAITING flag; the SharePoint read answers part of it for 49F: SMArtX bills, in advance, the checklist's preparer is recorded, no
approver field exists); FWD-3 for
every client (round 1 shows one household); FWD-4 the effective-dated agreement record; FWD-5 the Schwab fee file (no upload,
C-NO-UPLOAD); FWD-6 buy-or-build comparison (public sources only, C-NO-VENDOR-YET); Cottonwood (no BD fee table); the 0833 bridge if
AB-t-1 measures it missing.

fanout: 2 of 2 chains, cap 8.

## 3. ROUND 2 (2026-10-09 ~08:2xZ, issuer 2.0.0_SA_COO~B2, on the CTO's round-1 analysis @ed0aad9538 + ADDENDUM 1 @e5371f3e39)

**Source:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_BILLING_ROUND_1_20261009.md` (msg 2815; ADDENDUM 1 msg
2825), its enrichment list read as this round's rectangle. Round 1 closed MAY-CLOSE, ARMED 0 (CVO msg 2814); FWD-1 EXERCISED on DEV.

**Measured before the cut (read-only research, 08:0xZ):**
- **E1 -- the book check exists at the edge.** CloudFront `EVTSA9VEHNZVH` behaviour `/api/scoped/partners/*` runs `auth-validator-edge:22`
  (viewer-request), which refuses with 403 a `/books/relationship/{id}/*` id absent from `s3://opal-data-bd/platinum/49financial/ownership_map.json`
  under the JWT `advisorId`; `role`/`firmRole` admin bypasses (`infra/aws/lambda-edge/auth-validator-edge/index.mjs:120,466-539`). The authorizer
  `opal-portal-authorizer` refuses a request that skips CloudFront (`infra/aws/users/lambda/portal-authorizer/index.mjs:340-351`). Gap: 5 of the 11
  `advisorKey`s in `opal-partner-49financial` are absent from the map. The map's producer is
  `data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py`. ADDENDUM 1: four live probes plus one out-of-book JWT straight at execute-api;
  a Lambda-side check is cut only if that bypass probe is admitted; the gap is fixed at the producer under a pair naming the 5 advisorIds.
- **E2 -- no SMArtX fee data in Opal.** The daily SMArtX API pull (`infra/aws/lambda/smartx_assets_pull/`) has no fee/billing endpoint; no fee
  file in S3. The statements exist only as SharePoint `.xlsx`. The gateway can read a site item's bytes only under the caller's Graph token
  (`infra/aws/ec2/opal-gateway/app/tools.py:699-730`); nothing copies a site file to S3.
- **E3 -- a durable crosswalk source exists.** `s3://opal-data-bd/silver/allocations/<date>.parquet` carries BD `account_id`, custodian
  `account_number`, `relationship_id` (z): 3,146 of 3,353 z-keys reach a 0833 account; 5,149/5,149 agreement with the stale xref; newest
  partition 2026-10-02 (lag to measure). BD `gold/dimensions/accounts_dimension_latest.parquet` is the household spine.

**Builder output at the cut (rule 30, no refusal):**
`address("advi","49financial","gold","household_crosswalk","date=<d>","household_crosswalk.parquet")` ->
`s3://opal-data-49financial/advi/49financial/gold/household_crosswalk/date=<d>/household_crosswalk.parquet`;
`address("smartx","49financial","bronze","fee_statement","quarter=<q>","<file>.xlsx")` ->
`s3://opal-data-assets/smartx/49financial/bronze/fee_statement/quarter=<q>/<file>.xlsx`;
`address("advi","49financial","silver","smartx_fee_statement","quarter=<q>","data.parquet")` ->
`s3://opal-data-assets/advi/49financial/silver/smartx_fee_statement/quarter=<q>/data.parquet`.

| cell | serves | status | risk | depends on | chain | placement |
|---|---|---|---|---|---|---|
| `AB-e-1` | E1 (ADDENDUM 1; minted and run by `0.7.0_AE_CloudOps~DELL2` per ADDENDUM 2 @abbf204c7e): five live probes for `z08219260` -- through `opalinvest.dev`: an advisor whose map entry holds it (expect 200), an advisor whose entry does not (expect 403), a `firmRole=admin` viewer (expect 200), another firm's viewer (expect 403); and the out-of-book JWT straight at the execute-api URL (expect refusal). Real JWTs minted the way the auth handler mints them. A Lambda-side check is cut next round only if the bypass probe is admitted. THE ISSUER'S ACT (identity material), not a worker order. | NOT_EVALUATED | WORLD (identity; reads only) | none | C | issuer |
| `AB-e-2` | E1 gap: in `d08_firm_ownership_map.py`, find why 5 `advisorKey`s of `opal-partner-49financial` are absent from the map, fix it in the producer, test it, and print the regenerated map's membership DIFF (advisors added, relationships per added advisor; no other advisor's list may change) WITHOUT writing it. The served regeneration is the issuer's act under a never-widen pair naming the 5 advisorIds. | NOT_EVALUATED | SERVED (prep only; nothing served moves in the cell) | none | D | worker |
| `AB-e-3` | E2 path: a gateway capability that copies ONE SharePoint site item's bytes to the builder's `smartx/49financial/bronze/fee_statement/quarter=<q>/` prefix and nowhere else (refuses any other destination), with its tests (mocked Graph and S3). Built and tested; the tool's registration line is the issuer's hookup at the merge; the gateway deploy and its IAM grant are a later served act. | NOT_EVALUATED | WORLD (gateway code under infra/; no deploy in the cell) | none | E | worker |
| `AB-e-4` | E2 content: the SMArtX fee-statement parser -- bronze `.xlsx` (the 33 measured columns: AllocationID, Brokerage Account Number, Sleeve Type, Fee Period Start/End, SmartX/Advisor Prior Quarter Estimate/Actual/True-Up, UMA/APM/Model/Advisor/Client Fee Rate, Current Period Estimate Valuation, Days in Period, Days in Year, Net SmartX Fee, Net Advisor Fee, Fee Debit, ...) -> silver `smartx_fee_statement` at the builder address, with its contract; built and tested on a SYNTHETIC workbook carrying those columns (no real file exists in Opal yet). | NOT_EVALUATED | LOCAL | none | F | worker |
| `AB-e-5` | E3: the gold `household_crosswalk` producer (one row per Schwab 0833 account: `schwab_account_number`, `bd_account_id`, `bd_relationship_id`, `opal_relationship_id`, `match_method`, `claim`) from BD silver allocations + the BD household spine + `dim_relationship`, its contract, coverage denominators both directions and the allocations lag stated; ONE write at the builder address. | NOT_EVALUATED | WORLD (new gold key; nothing reads it) | none | F | worker |
| `AB-e-6` | E2+E3 consumer: `fee_quarter.py` v2 takes the household from `household_crosswalk` (AB-e-5) and, where a silver fee statement exists for the quarter (AB-e-4 contract), the per-allocation rates and the true-up (`schedule_claim measured`, source SMArtX); BD fee line stays the fallback. Tested; a dry run for `z08219260` printed, NO write (the re-emit is served: next round or the issuer's act). | NOT_EVALUATED | LOCAL (code; no write) | AB-e-4, AB-e-5 | F | worker |

**E4 -- FWD-3's grade** is the close act, not a cell: the issuer's real render of one client's panel, graded by `3.0.0_SA_CVO` at L9.

**Chain read.** M = 4: C = `AB-e-1` (the issuer's act), D = `AB-e-2`, E = `AB-e-3`, F = `AB-e-4` + `AB-e-5` -> `AB-e-6` (e-6 consumes both).
N = 3 workers, K = 8: slot ~3 takes chain F in order (e-4, e-5, e-6), slot ~4 takes D, slot ~5 takes E. Write sets are disjoint: D writes
`data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py` + one new test; E writes a new gateway module + test; F writes
`data/assets/scripts/silver/advi_billing/`, `data/assets/scripts/gold/advi_billing/`, two `org/standards/ADVI_BILLING_*` contracts and the
crosswalk key.

**Battery.** `comp-blast` -- RUN as a reading: e-5 writes ONE new gold key under a new table; e-2 writes no served key in the cell; e-3/e-4/e-6
write code only. `comp-iam` -- RUN as a reading: e-3's deploy will need `s3:PutObject` on the bronze prefix for the gateway's role -- not in this
round. `comp-routes`, `comp-cache`, `comp-schedule`, `comp-adversary` -- DECLARED-NOT-APPLICABLE: no route, cache or schedule moves in a cell.

fanout: 3 of 4 chains, cap 8, reason: chain C is the issuer's act; three worker chains.
