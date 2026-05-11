# DS~A 2026-05-11 session 3 — INFNNA.GOLD + INFNNA.SILVER status sweep (Proposal 2 of 2)

## TL;DR

Status sweep on the two remaining `active` INFNNA TOs per COO GO 12:50Z. **Neither closes cleanly** — real open ACs remain:
- **SILVER:** AC2 (performance historical) + AC4 (assets_v2/accounts_v2 historical) FAIL — these dims are snapshot-keyed with only 1-7 dates each vs the 2000+ per-date partitions tax/billing/positions_mv have. Not D-layer dtype work — genuinely missing silver builds.
- **GOLD:** AC4 FAIL — `platinum/firm/leaderboard.json` has only 3 entries (Patrick, Peter, IWM); **Joe Brandenburg is absent from leaderboard despite being present in canonical_nna parquets and in `nmec_nmnc_nna.json`**. AC2/AC3 PASS, AC5 needs verification.

Real D-layer bug routed at INF_D_00c (leaderboard publisher), not ACCOUNT-ID-COERCE territory.

## S3 state snapshot

### silver/api_dims/ partition counts

| Dim | Partitioning | Partition count | Coverage | TO AC |
|---|---|---|---|---|
| `transactions/` | per-date `{date}.parquet` | 1,510 | 2020 → 2026-05-08 historical | (covered by JOE-TXN-BACKFILL, closed) |
| `tax_realized/` | per-date | 2,022 | full historical | AC1 PASS |
| `tax_unrealized/` | per-date | 2,050 | full historical | AC1 PASS |
| `billing/` | per-month | 1,507 | full historical | AC3 PASS |
| `positions_mv/` | per-date | 2,177 | full historical | AC5 PASS (TO calls it positions_daily; positions_mv is the canonical name) |
| `performance/` | per-snapshot_date | **4 snapshot dates** (04-28, 05-09, 05-10, 05-11) | **FAIL** — historical not built | AC2 FAIL |
| `accounts_v2/` | per-snapshot_date | **7 snapshot dates** (04-28..05-11) | **FAIL** — historical not built | AC4 FAIL (TO calls it assets_v2; accounts_v2 is the relevant dim — assets_v2/ has only 1 snapshot date) |
| `activity/` | per-snapshot_date | 1 snapshot date | (not in TO scope but worth flagging) | n/a |

### Gold canonical_nna state

- **1,365 `canonical_nna_{date}.parquet` files** spanning 2020-05-26 → 2026-05-07.
- All written 2026-05-08 between 16:18:42Z and 16:21:13Z — full rebuild executed during E2E cascade.
- Joe presence verified at parquet level:
  - `canonical_nna_2025-12-15.parquet`: 21 rows, advisor_key counts = {peter_lee: 16, patrick_scanlan: 3, **joe_brandenburg: 2**}; Joe sum(net_nna) = +$11,500.
  - `canonical_nna_2026-05-07.parquet`: 8 rows, {patrick_scanlan: 4, peter_lee: 4} — no Joe activity that day (legitimate, not a bug).

### Platinum artifacts state

- `platinum/firm/leaderboard.json` (generated 2026-05-08T20:28:50Z): **3 entries** in each QTD/YTD/MAX window — Patrick Scanlan, Peter Lee, Inflection Wealth Management (firm bucket). **Joe Brandenburg absent.**
- `platinum/firm/nmec_nmnc_nna.json` (as_of 2026-05-08): **4 advisor rows** including `joe_brandenburg` with `nmnc_aua=$12,991,863.26` (13 new clients), `existing_aua=$3,469,426.76` (8 existing), `nna_qtd/ytd/mtd=$0`. IWM (rep_3) `existing_aua=$253,915.82` = 0.5% of firm AUA (well under AC3's 5% threshold).

## GOLD TO ACs — per-criterion verdict

| AC | Status | Evidence |
|---|---|---|
| AC1 canonical_nna rebuilt full historical range | **PASS** | 1,365 parquets, 2020-05-26 → 2026-05-07, all written 2026-05-08 |
| AC2 Q2 2026 canonical_nna shows Joe non-zero, IWM normalized | **PARTIAL** | Joe rows present in canonical_nna where he has activity (e.g. 2025-12-15 net_nna=$11.5K). IWM rep_3 has $253K existing_aua (0.5% < 5% threshold). Sum advisors = $202.9M ≈ firm $202.3M. PASS at parquet layer. |
| AC3 nmec_nmnc_nna.json Joe present + IWM ≤5% + advisors sum = firm | **PASS** | All 3 sub-criteria met (see above). |
| AC4 leaderboard.json 4 entries, Joe non-zero NNA | **FAIL** | Only 3 entries (Patrick, Peter, IWM); Joe absent. This is the real bug. |
| AC5 NMNC/NNA reconciliation Q2 within 10% | **NOT VERIFIED** | Q2 firm NNA = -$71K, Q2 firm NMNC AUA = $180M — these aren't apples-to-apples; needs proper reconciliation method. |

## SILVER TO ACs — per-criterion verdict

| AC | Status | Evidence |
|---|---|---|
| AC1 tax per-date INFLECTION_REP_IDS scoped | **PASS** | tax_realized + tax_unrealized cover historical (4,072 combined partitions) |
| AC2 performance per-date INFLECTION_REP_IDS scoped | **FAIL** | Only 4 snapshot dates (04-28, 05-09, 05-10, 05-11); historical backfill not done |
| AC3 billing per-month | **PASS** | 1,507 partitions |
| AC4 assets_v2 per-date INFLECTION_REP_IDS scoped | **FAIL** | assets_v2/ has 1 snapshot; accounts_v2/ has 7 snapshots — neither has per-date historical |
| AC5 positions_daily per-date | **PASS** | positions_mv has 2,177 partitions (positions_mv is the canonical name; positions_daily is empty) |
| AC6 No Guard B FAIL | **LIKELY PASS** | E2E cascade 2026-05-08 ran clean (modulo 6 D-layer parquet-write fails) |
| AC7 tax silver totals ~$203M for recent dates | **NOT VERIFIED** | Spot-check pending |

## Proposed work — surfacing to COO

### Real follow-up TOs (not consolidatable into ACCOUNT-ID-COERCE)

1. **`ADVI_INFNNA.LEADERBOARD-JOE-ABSENT`** (proposed): Joe present in canonical_nna + nmec_nmnc_nna.json but absent from leaderboard.json. INF_D_00c.portal_leaderboard.py filter logic to investigate. Possible causes: (a) D_00c queries snapshot-date-only canonical_nna rather than full history; (b) D_00c has a rep_id filter; (c) Joe's `rep_bucket` mapping in some upstream step. ~1-2h debug.

2. **`ADVI_INFNNA.SILVER-PERFORMANCE-HIST`** (proposed): Build `silver/api_dims/performance/snapshot_date={date}/` per-date historical 2020-03-11 → 2026-05-11. Mirror the per-date pattern used by tax_realized. ~30-60min depending on bronze coverage.

3. **`ADVI_INFNNA.SILVER-ACCOUNTS-HIST`** (proposed): Build `silver/api_dims/accounts_v2/snapshot_date={date}/` per-date historical (currently 7 snapshot dates, need backfill). Also reconcile assets_v2/ vs accounts_v2/ — clarify which is the TO's intended dim. ~30-60min.

### Keep both TOs `active` (do NOT close)

Both have real open ACs that block downstream correctness. Closing prematurely loses the work-tracking signal.

### What COO needs to decide

- (a) Author the 3 proposed follow-up TOs as new dispatches to DS~A?
- (b) Roll the work directly under the existing GOLD + SILVER TOs by updating their AC checklist with explicit sub-tasks?
- (c) Defer some/all to wait alongside SL-P2 + ACCOUNT-ID-COERCE for Andrew's broader direction?

## Files touched

- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_A_session3_gold_silver_sweep_2026-05-11.md` — this log.
- No TO files modified (neither closes).

## Compiler Tools section

- N/A: read-only S3 inspection + parquet reads only. No script edits or dispatches.

## Diagnostics retained

- `.runtmp/joe-verify/leaderboard.json`
- `.runtmp/joe-verify/nmec_nmnc_nna.json`
- `.runtmp/joe-verify/canonical_nna_2026-05-07.parquet` (no Joe rows — expected)
- `.runtmp/joe-verify/canonical_nna_2025-12-15.parquet` (Joe present — refutes upstream-canonical-missing hypothesis)
- `.runtmp/joe-verify/2026-05-07.parquet` (silver/transactions, 88 Joe rows)
- `.runtmp/joe-verify/2023-06-15.parquet` (silver/transactions, 6 Joe rows historical)

## Next

Send detailed proposal to COO. Standing by for routing decision.
