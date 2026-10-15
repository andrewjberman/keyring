# Cottonwood backfill: where it stands -- ADVI_COTBKF, the shaping in opal-data-cottonwood, the pricing spine (2026-10-15 ~17:3xZ)

**Author:** `4.0.0_SA_CRO~DELL2`, on Andrew's word (record `ANDREW_DIRECT_20261015_171xZ_COTTONWOOD_BACKFILL_SHAPING_AND_PRICING_SPINE.md`
@e4b58df4c8). This is a read-only investigation: full S3 listings, pyarrow reads of four files, the repo and git. Cottonwood data only;
account ids are opaque.

## Status in one paragraph

- **ADVI_COTBKF is PARKED** (10-14). On Andrew's 10-14 word its placement moved to dell1, and `~C2` stood down. It left the active
  Cottonwood set and the reverse match.
- **The Black-Diamond-era daily returns landed today** (IRPT_DASHBD `~D2`) in the canonical Cottonwood gold path, 2026-07-10 to 10-14. The
  Commonwealth-era returns already sit there (2013-04-03 to 06-22, written 10-11).
- **12 trading days between them are unlanded** (06-23 to 07-09).
- **The two eras carry two different contracts under one table name.**
- **The pricing spine is far from the need:** the only live per-security store covers 528 of 3,367 active-set non-cash CUSIPs, and
  MDPF_SECHIST's series store is empty.

## A. ADVI_COTBKF

| Item | State | Source |
|---|---|---|
| Project row | `status: hold`, placement DELL1 (moved 10-14 ~18:5xZ) | `project.json:7,51`; 37e2467986 |
| PRD | v0.10 RATIFIED, FWD-1..9; REALIZED at the 10-09 endpoint read: 1, 5, 6, 8; NOT: 2, 3, 4, 7, 9 | `ENDPOINT_READ_20261009.md:7-17` |
| Rounds | 80-85 on 10-13; round-86 analysis = PARK | `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_86_PARK_20261014.md` |
| Active set V2 | **860 accounts** open at BD on 10-12 (91 cash-only; 139 zero-unit excluded); 3,368 securities; 41,826 window rows. Window basis: Commonwealth transactions 18,966, BD holdings 15,140, joined 6,886, not established 834 | `deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv` @4d427d3bbb |
| Reverse match V3 | **460 matched, 13 near, 387 none**, each with a reason | `REVERSE_MATCH_V3.csv` |
| Named gap | the round-85 build scripts are LOST, so V2/V3 cannot be reproduced | park record, gap 1 |
| Un-park | Andrew's word, or the ARD route reaching a page | round-86 analysis |

## B. `s3://opal-data-cottonwood` (7,814 objects, 20 prefixes)

| Prefix | Objects | Dates | Newest write |
|---|---|---|---|
| `irpt/cottonwood/gold/account_return_daily` | 6,780 | 3,390 (2013-04-03..2026-10-14) | 10-15 17:07Z |
| `irpt/cottonwood/gold/holdings` | 15 | 09-22..10-08 | 10-09 |
| `irpt/cottonwood/gold/holdings_performance_daily` (+ manifest) | 88 (+176) | 06-10..10-14 | 10-15 |
| `irpt/cottonwood/platinum/holdings` (+ qa) | 376 (+117) | 09-22..10-08 | 10-15 |
| `irpt/cottonwood/gold/{account_dim, dim_return_method, holdings_qa, account_return_daily_blank_reasons}` | 2 / 2 / 5 / 1 | -- | -- |
| `irpt/cottonwood/state/ycharts_*` | 77 | -- | 10-05 |
| `mdpf/cottonwood/gold/{account_distribution, account_units, aggregate_aua_timeseries, aum_metrics, taxsma_assets}` | 173 | 07-20..10-15 | 10-15 |

**Paths:** every prefix is canonical `<system>/cottonwood/<tier>/<table>/date=D/`, with no legacy or duplicate paths in this bucket. The raw
Commonwealth delivery sits in `opal-data-assets/commonwealth/` (11,155 objects, delivered 2026-06-23).

**The two eras of `account_return_daily`:**

| Era | Dates | Written | Rows a day |
|---|---|---|---|
| Commonwealth | 3,325 dates, 2013-04-03..2026-06-22 | 2026-10-11 | 299 (2013) to 753 (2026-03), then 138 on 06-12 |
| Black Diamond | 65 dates, 2026-07-10..10-14 | today, IRPT_DASHBD round 130 Act 3 (474ff2fdd1, 691b95c160; ledger `20261015T1321Z_irpt-dashbd-cottonwood-account-return-daily`) | 864-867 |

**The gap (06-23..07-09, 12 trading days):** BD `fact_holdings` has those dates; `fact_allocations` lacks 06-24 and 06-25. The CTO set the
07-10 floor (round-124 ruling 1b) so a held gap day is never owed.

**Shaping: one table name, two contracts** (four files read):

| | Commonwealth era | Black Diamond era |
|---|---|---|
| Columns | 19 | 20 (adds `source`; no type differs) |
| `method_version` | **3** | **2** (it goes backwards) |
| Manifest | `asof`, `firm_scope`, `source_pipeline: irpt-reporting-adapter`, `valuation_source: positions_x_as_traded_close` | `business_date`, `firm`, `contract_version 0.3.0`, `schema_hash`, "computed from Black Diamond values and flows", `thresholds_claim: absent` |
| Measurable | `return_basis` NOT_MEASURABLE on 89-95% of rows (2023-12-29: 644 of 689; 2026-03-31: 692 of 753) | -- |

## C. The pricing spine

| When | What | Source |
|---|---|---|
| 10-07 | Need: 4,634 securities, 3,421,735 security-days. Andrew's "i like the yahoo finance vs bloomberg rec": Yahoo for equity/ETF/fund, Bloomberg (site Z) for fixed income and other, landing once per security in MDPF_SECHIST | PRD v0.4 ADDENDUM 2 `:214-222` |
| 10-12 | C-BASIS: funds priced at the AS-TRADED close, from dell1's `as_traded_close` (one lander via the DEMQUE queue); unpriced days stay UNPRICED. The 15-fund quote call XB-...-8522 sat unread 45 h | PRD v0.8-v0.10 `:292-422`; park record gap 5 |
| 10-13 | Former clients excluded: DEMQUE `rank.py` P3 "never drawn" (DQ-t-52, 0294f140f0). B1 Bloomberg request clipped to active set V2: 613 CUSIPs, 34,437 cells (0811da6ec3) | `data/mdpf/scripts/demque/rank.py:25,41` |
| 10-14 | First wired Yahoo run into the DEMQUE store (3223d1a66a); `porting_verdict` UNVERIFIED by default (7ad0fcd178). Row D1-S1: FTHSX/PFORX carry wrong-symbol Yahoo closes (8796909c1c) | git |

**Coverage today:**
- **DEMQUE Yahoo store** (`opal-data-assets/yahoo/global/silver/price_history/cusip=<ID>/`): **538 CUSIPs** (2,154 objects; 483 this
  morning, so it is filling).
- **Active-set non-cash CUSIPs covered: 528 of 3,367 (15.7%).**
- **Against the 4,634 need:** at most 538 (11.6%).
- **MDPF_SECHIST `security_series/`:** 0 objects.
- **Not computed:** security-days covered against 3.42M.

## D. Calls, blockers, owners

| Item | Owner | State |
|---|---|---|
| Un-park ADVI_COTBKF | Andrew, or the ARD route reaching a page | OPEN. `~D2` is building the Cottonwood report-build handler today (DB-b-263/265), which may meet the un-park condition; no seat has noted it |
| Lost round-85 scripts | the first un-park cell | OPEN |
| Gap 06-23..07-09 | IRPT_DASHBD `~D2` / CTO~DELL2 | held by the floor ruling |
| Era contract mismatch (method_version 3 vs 2; two manifest shapes) | **unowned** | unflagged in what this seat read |
| Price fill (Yahoo leg; B1 Bloomberg 613 CUSIPs) | MDPF_DEMQUE `2.0.0_SA_COO~Q1` (dell1) | in progress; SECHIST, the PRD's named lander, holds nothing |
| Holdings platinum served at 10-08 (`account_lost`) | IRPT_BCKEND `~P2` (IB-pr-532) | folded 10-14 |

## Gaps against Andrew's 10-13 memo

| His words | State |
|---|---|
| "any active account has backfill for its various securities ... for the period that they were held" | Windows exist (860 accounts, 41,826 windows, from 2013-04-08). Only 15.7% of their securities have a price series, and Commonwealth-era returns are ~90% NOT_MEASURABLE |
| "how we maintain the pricing of these active securities on a daily basis per account" | The BD era is daily from 07-10. 12 trading days (06-23..07-09) are unlanded, and the eras join under different method versions and manifests |
| "we don't need to waste quota on" former clients | **MET** (DEMQUE `rank.py` P3 never drawn) |
| "clear matching mechanism ... to the black diamond repository" | 460 of 860 active accounts matched, 13 near, 387 none with reasons. The forward crosswalk is 471 matched of 1,533 |

## Not read

- Security-day coverage against the 3.42M need.
- The values at the 06-22/07-10 seam.
- Whether the Cottonwood ARD reaches a page today.
- The restricted prefix (FWD-7).
- The 10-06/10-07 records in full (cited through the PRD).
- B1's drawn status after 10-13.

-- 4.0.0_SA_CRO~DELL2
