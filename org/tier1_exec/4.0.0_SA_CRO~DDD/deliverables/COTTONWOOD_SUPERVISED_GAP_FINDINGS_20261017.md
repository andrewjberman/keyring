# Cottonwood: why Opal reads $554.63M against BD's $563.56M, and what Supervised-only serves

**Author:** 4.0.0_SA_CRO~DDD (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO~DDD/
**Order:** `ANDREW_DIRECT_20261017_010xZ_COTTONWOOD_SUPERVISED_ONLY_MATCH_BD.md` (same folder)
**Value date:** 2026-10-15 (both sides). **Risk class of the fix:** SERVED.

## 1. Answer

**It is not a one-day lag, and we are not missing accounts.** BD's own Dashboard values the same accounts, on the same
day, about $8.9M higher than BD's own DataMining exports (holdings and allocations). We ingest the exports. The gap is
inside BD. It was measured before, at -$8,697,205.48 on 2026-08-19, ~99% supervised-side, and parked as a vendor question
(`data/cot/scripts/gold/D_05.supervised_split.py:57-68`, `PLANE_GAP_DECLARATION`). It never closed.

Separately, **the Opal Model Portfolios page serves Cottonwood's WHOLE book**, including $33.07M of Unsupervised
(held-away / position-only) accounts. That contradicts Andrew's 2026-08-25 ruling (Supervised-only for Cottonwood). The
supervised filter exists only on the ADVI/COT plane (`D_05`). It was never applied to the MDPF slice.

## 2. Evidence (every figure measured this session from s3://opal-data-assets)

| Figure | All assets | Supervised | Unsupervised |
|---|---:|---:|---:|
| BD Dashboard, 10/15 (screenshots) | 563,559,898 | 530,421,988 | 33,137,910 |
| BD holdings export 10/15, relationship grain collapsed (= Opal served total) | 554,632,228.45 | 521,561,158.83 | 33,071,069.62 |
| Gap (Dashboard - export) | 8,927,669.55 | 8,860,829.17 | 66,840.38 |

- **Same day, not lagged.** `HOLDINGS_DAILY_2026-10-15.xlsx` was created 10/16 07:30:59 ET, End Date 10/15. Its prices
  are 10/15 closes (SPY 769.60 -> 771.79, MSFT 533.69 -> 539.44 vs the 10/14 file). Day-over-day moves are +/-0.4%, too
  small to make a 1.6% gap.
- **Positive control: one BD Dashboard cell ties to the dollar.** "No Portfolio Group", Supervised: BD 2,631,739; ours
  2,631,739. Unsupervised ties within $5K-$28K in every group.
- **The gap is in Supervised accounts of the three advisor books, ~1.4-1.6% each.**
  Christa Bass +559,318 (1.38%); Jay Rubottom +4,429,136 (1.53%); Stephen Shipley +2,966,024 (1.56%); No Portfolio
  Group +0.
- **Two independent BD exports agree to the cent.** Allocations `Account Market Value` = holdings = 554,632,228.45; 0 of
  860 accounts differ by more than $1.
- **Account universe is complete.** Account-attributes 1,004 accounts = holdings 1,004 accounts; 0 missing either way.
- **Ruled out:** external flows (10/15 net -$1.01M); unpriced holdings (0 rows with units and no value); negative
  cash/short positions (removing them overshoots by $2-3M); relationship double-count (the dashboard-style pair count gives
  $555.44M); accrual (already in Market Value; Aug test: 2.5% of the gap); alt/manual revaluation (Christa has $100K of
  alts but is $559K short).

## 3. What would close ask 2 ("matches that number")

**The Supervised filter alone yields $521.56M, not $530.42M.** The $8.86M remainder is the BD Dashboard-vs-export gap. No
act on our side reaches it from the exports; only BD can say what the Dashboard's ending market value includes that the
DataMining holdings template does not. Two routes, in order:

1. **One BD export, from Andrew's Dashboard login (fastest; no vendor wait).** Dashboard -> Supervised, 10/15 -> group by
   Relationship Name (or Account) -> Export. With the per-relationship ending values I can diff all 225 relationships
   against the export in minutes and name the accounts or assets carrying the $8.86M. Then the template change is
   specific.
2. **Vendor question to BD**, already quantified: "Dashboard ending market value for Cottonwood on 10/15 is $563,559,898;
   the Assets_Dim holdings template (id 226355) and the allocations template sum to $554,632,228.45 for the same 1,004
   accounts. Which holdings or valuations does the Dashboard include that DataMining does not?"

## 4. The build (PROPOSAL -- the CTO rules it; a COO cuts it)

- **Where:** `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` `holdings_total_by_date` (:566-609). Read
  `Account Supervised` with the other columns and keep `== "Supervised"` before the collapse and sum.
- **Effect on 10/15:** Total 554,632,228.45 -> 521,561,158.83; Client 341,358,334.98 -> 308,287,265.36. Models
  (205,049,392.06) and SMA (8,224,501.41) are unchanged: 0 of the 130 Unsupervised accounts in the Rebalancer carries a
  model (`fact_model_assignment` 2026-10-16, all `strategy_name = "--"`).
- **Scope guard:** Cottonwood only. 49financial stays whole-book by the same 08-25 ruling (`mdpf_category_registry.py`
  :818-858); an estate-wide "make the firms consistent" edit is the defect that comment warns about.
- **History:** apply the current flags to history (the `D_05` today's-flags caveat), declared in meta.
- **Served move:** needs the never-widen sign-off (CTO + COO). The blast radius is the Cottonwood and Global MDPF artifacts.
  Global's total falls by the same $33.07M.
- **Not in this fix:** the $8.86M plane gap (section 3). Until it is resolved, the served figure is the export-plane
  supervised value. The page's source line should say so, rather than imply a tie to the BD Dashboard.

## ADDENDUM 1 (2026-10-17 ~01:5xZ) -- the $8.86M is located, to the cent

Input: Andrew's BD export "BI Dashboard Export - Relationship_Account - 10_15_2026.xlsx" (Supervised, 10/15, by
relationship and account). Its Executive Summary total is 530,421,988.14, the screenshot figure. The file holds client
names and addresses and is NOT committed. The scratch copy was deleted after the diff.

- 849 distinct account numbers in the export. One is in two relationships: +205,070.77, the known relationship-grain
  double-count, which the BD total row already collapses.
- **753 of them match our supervised accounts with $0.00 difference. 96 are ABSENT from every DataMining export we
  ingest** (holdings, allocations and account attributes all hold 1,004 accounts). They total **8,860,829.31**, the whole
  supervised gap. The other way round: 0 of our supervised accounts is missing from the export with a value, and 0 of our
  Unsupervised accounts shows in it.
- **The 96 are insurance and annuity carrier-feed accounts**, by their account-number prefix:

| Prefix | Accounts | Ending MV 10/15 | With a YTD BD mgmt fee |
|---|---:|---:|---:|
| DTCCR_ (DTCC insurance feed) | 78 | 4,890,211.59 | 78 (5,300.70 total) |
| ASLAA_ | 13 | 2,527,925.27 | 0 |
| AEGON_ | 3 | 1,060,666.07 | 0 |
| LNANN_ | 1 | 226,189.95 | 0 |
| EQUIT_ | 1 | 155,836.44 | 0 |
| **Total** | **96** | **8,860,829.31** | 78 |

  They sit in 47 relationships across all three advisor books, which is why the gap looked spread evenly.

**Two causes, two remedies:**
1. **Ingest (mechanical).** BD's DataMining templates do not return these accounts, while the Dashboard does. Remedy:
   widen the Cottonwood DataMining account set, or the holdings, allocations and attributes templates, to include the
   insurance-feed accounts. Owner: the COT ingest (0.7.0_AE_CloudOps on the cot-bd session pipeline). Proof: the
   10/15-equivalent export ties to 530,421,988.14 supervised.
2. **Display (sovereign).** Andrew ruled on 2026-08-24 that Insurance is excluded from the MDPF view ("we don't take fees
   on it"). Matching BD's 530.42M means counting these 96 annuities in Cottonwood's supervised total. 78 of them DO carry a
   BD management fee, so the ruling's stated reason does not hold for them. **This is Andrew's call:** count Cottonwood's
   insurance in its total to match BD (530.42M), or keep the exclusion and serve 521.56M with "excluding $8.86M insurance"
   stated on the page.

## ADDENDUM 2 (2026-10-17 ~02:3xZ) -- CORRECTION: the 96 are IN our pull; their values arrive after we pull

Addendum 1 said the 96 insurance-feed accounts are "ABSENT from every DataMining export we ingest". **That is wrong.** My join
keyed on BD's displayed account number (`DTCCR_04003450617`, `AEGON_000000150828TAL`). DataMining's `Account Number` drops the
carrier prefix (`04003450617`, `150828TAL`). So the 96 sat among our 1,004 accounts at $0, and the 127 supervised "$0, not in
allocations" accounts in section 2's custodian table were them.

**The real cause is timing, so Andrew's lag hypothesis was half right.** The holdings export carries the carrier rows every day.
Their Market Value is null when the export runs at the scheduled 07:30 ET (`cot_bronze_ingest.py`, `schedule-et.tf:90-91`),
because BD posts the carrier-feed values later. Later pulls carry them. Measured:
- `HOLDINGS_DAILY_2026-10-09.xlsx` was re-landed 10-12 11:45Z. 106 accounts read $0 in silver and $11,058,624.83 in that
  bronze, all `Supervised`.
- Silver for 10/09 was never rebuilt from the re-landed bronze. The silver/bronze total delta is exactly 11,058,624.83.
- The completeness check passes these files (share of positions with a value 0.633 against a 0.5 floor), so nothing
  retries them.

**Remedy, replacing Addendum 1's ingest remedy (no BD template change):**
1. **Now:** re-pull T-1 holdings and allocations after BD posts carrier values, then rebuild silver, gold (MDPF and ADVI) and
   publish. This writes Cottonwood silver, so it waits for 2.0.0_SA_COO~C1's written agreement after the R106 read.
2. **Durable:** fail the holdings completeness check when carrier-shaped accounts are present but all null, so the retry
   sweep re-pulls. Pair it with a later re-pull slot so the retry lands the same day, not the next. Silver also rebuilds
   whenever bronze is re-landed.
3. **Backfill:** re-pull and rebuild the null dates, most weekdays since 2026-08-13.

Source: a scoping read of the bronze ingest by this seat's research agent, verified here on 10/09.

## ADDENDUM 3 (2026-10-17 ~02:4xZ) -- what is landed, and the runbook to 530.42M

**Landed tonight:**
- **MDPF.** `mdpf-gold-lambda` runs f09a6a3adb, the supervised switch (ledger
  `mdpf-gold-fwd10-cottonwood-supervised-20261017`, CLOSED; CTO half @a047cb0922). The 10-17 13:30Z run serves Cottonwood
  at the supervised value. Global is unchanged: its Client leg is 49F only.
- **ADVI.** C_03 switch @9a3a0e5605, producer half @62badadb7b, waiting on the CTO half before `safe-deploy --tree cot`.
- **Not landed.** The mix leaves (D_03 is COO~M1's lane; C_06 is incremental).

**Why the pages will read ~521.5M, not 530.42M, until step 2 below:** the carrier-feed accounts are $0 at the 07:30 ET pull.

**Runbook to 530.42M** (each step waits only on the one before it):
1. 2.0.0_SA_COO~C1 posts "fire read done" after the R106 read (~13:00Z 10-17) and agrees in writing to a Cottonwood silver
   write. It needs the write time, the partitions, and whether any of the 122 multi-book accounts gain rows. Answer: no new
   accounts, values only on existing rows.
2. After BD posts carrier values, re-run bronze holdings and allocations for the latest date (`opal-cot-bronze-run`
   RunDate). Each must carry non-null carrier values: check the 106/96-account set. Then run the silver merge for that date.
3. Re-run the MDPF gold Lambda and publisher once (a scheduled-equivalent production run, CTO-gated), and let the ADVI gold
   chain run. Read: Cottonwood supervised equals BD's Dashboard Supervised for that date, within the ~$51K
   canonical-collapse delta.

**Durable fix (spec for the CloudOps COT lane; not this seat's to build):**
- Mark carrier-feed accounts. Use the transactions `Original Account Number` prefix (DTCCR_/ASLAA_/AEGON_/LNANN_/EQUIT_), or
  an account-attributes column if BD has one.
- Fail `_table_complete("holdings")` when marked accounts are present and all null, so the existing bounded late-publish
  retry (3 x 900 s) re-pulls the same morning.
- If BD posts later than that window, add a same-day re-pull slot that also rebuilds silver. Today a re-landed bronze file
  never re-runs silver; 10/09 shows it.
- Backfill the null dates since 2026-08-13.

## 5. Not captured

The BD Dashboard's per-relationship values (only the four group rows in the screenshots). The August HAR oracle
(`supervised_vs_unsupervised.har`) is not on this box. Raw exports and scratch scripts stay in the session scratchpad, not
the repo.
