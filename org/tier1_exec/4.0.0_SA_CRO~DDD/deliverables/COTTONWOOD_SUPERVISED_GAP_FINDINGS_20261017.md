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

## 5. Not captured

The BD Dashboard's per-relationship values (only the four group rows in the screenshots). The August HAR oracle
(`supervised_vs_unsupervised.har`) is not on this box. Raw exports and scratch scripts stay in the session scratchpad, not
the repo.
