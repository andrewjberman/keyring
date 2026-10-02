# Never-widen half, MDPF_SECCLASS -- BD thread r3 RE-LAND: every class in the mix and the identity read (CTO batches 117 item 4, 144, 156)

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 12:1xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status: COO half SIGNED; CTO half asked; NOT RUN.** Code on branch `coo-m-bd-mix-classes` @29747a2ecb (worktree `coo_m_r30`), NOT
on CLOUD. CLOUD's r3 bytes of the four producers are serve-held @056e9f0a74 (row S13).

## Why a re-land, and what changed since r3

r3 (2026-10-01) put Black Diamond's gold on the canonical table alone; its first real compute (2026-10-02 04:00Z) served a 49
Financial firm mix missing 445.7 M of 1,843.1 M and was rolled back (batches 117-118; row S9, disarmed S12). This act re-lands r3
with the two ruled conditions met: (i) **no ticker leaves the mix** -- fix 1 (C_06, D_03, D_04, `lib/mix_views.py`: eight classes,
an unknown reads `unclassified`, never `other`; `comp-constants.config.yaml` re-canonized) -- and (ii) **unclassified at or under
5.0 pct with the residual listed by name** -- the identity read for a blank ticker (`lib/etf_classifier.py`, additive; batch 156:
the position's own CUSIP row, else the exact name through `ticker_resolution.parquet`, else the name's one CUSIP, its row or its one
ticker's row; unique at every hop and both ways). Since 09:5xZ the table also gained 86 rows (fixes 2, 3 and the first act).

## The act, by leg

| leg | what |
|---|---|
| P | **precondition, not this seat's:** the portal reader commit `eb90f2ad` (renders commodities, structured, unclassified, cash) on portal PROD -- the CTO's condition on the Cottonwood re-point (batch 113) holds here for the same readers; PROD today `b3a1d8a6` lacks it. A PROD promote is Andrew's act. |
| M | merge `coo-m-bd-mix-classes` into CLOUD (`.tools/safe-merge.sh`); the four files' DEPLOY-SERVE-HELD lines come off in the same act under a `SERVE-RELEASE-ACK` commit naming this half. Stop: the merged tree differs from CLOUD in any file but the ten the branch carries |
| G | `safe-deploy` of the five Black Diamond gold files (C_06, D_03, D_04, `lib/etf_classifier.py`, `lib/mix_views.py`) to `opal-data-bd/code/gold/`; prior VersionIds recorded first (today's rollback copies, 8b1f012c / 346e7b0f / a4b867d4 / 884889c0 / mix_views d4467d4a) |
| W | C_06's watermark keys set back one partition, so the next run recomputes the latest day on the new code (as the restore run did) |
| R | ONE ad hoc QA run (`bd-gold-trigger {"mode":"incremental"}`), read before any scheduled fire: acceptance 1 below |
| S | the next scheduled fire: acceptance 2 below |

## Blast radius, measured

**49 Financial's firm mix, 09-30 positions** (`gold/canonical/holdings/2026-09-30.parquet`, 113,579 valued positions,
1,866,381,354.90 USD), the branch's C_06 `classify_series` with the real resolver loaded from S3 and the live table (2,805 rows):

| class | today served (old library) | after the re-land |
|---|---|---|
| equity | 76.86 pct | 73.66 |
| fixed_income | 21.03 | 20.29 |
| **unclassified** | 0 | **4.63** (86,480,584.86 USD) |
| structured | -- | 1.22 |
| alternatives | 2.11 | 0.01 |
| cash | -- | 0.11 |
| commodities | -- | 0.07 |

Every class is in the mix's list; the shares sum to 100. **Residual by name:** `R8_CHECKS/R8_BD_RELAND_RESIDUAL_BY_NAME_20260930.csv`
(767 names); the largest: VANGUARD MORNINGSTAR GROWTH ETF 35,784,712.98 (refused by the guard: VUG carries three CUSIPs in the feed,
row S14), Waldrop Donor Advised Fund 5,842,785.00, EXXONMOBIL HOLDINGS CORP COM SHS 3,354,778.97, CLIFFWATER CORPORATE LENDING I
2,608,883.37, two "6 Year Shield" buffer notes 4,468,314.61, AQR TA DELPHI PLUS FUND LLC 2,243,578.73, a Barclays 0% note
2,025,375.07, the target-date and balanced funds batch 145 left unwritten. Identity hops on the 09-30 names: 1,119 resolution
table, 88 name -> CUSIP row, 73 name -> CUSIP -> ticker; refused 464 CUSIP carries no ticker, 107 name not in the feed, 84 ticker
has no row, 23 ticker carries several CUSIPs, 13 name carries several CUSIPs.

**Served keys and writers:** the r3 half's families unchanged (`gold/views/mix_daily_summary.json`, `gold/artifacts/firm_mix_views*`,
`platinum/firm/mix_summary.json`, `platinum/clients/{rid}/composition.json`, the advisor and account summaries). Live lineage
(`comp-clobber --sweep opal-data-bd`): gold/views/ 10 keys, gold/artifacts/firm_mix 2, platinum/firm/ 15 -- 0 interleaved. The
fleet emitter `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` names the firm mix family (:44) but is not a writer of
the served key: it reads it from S3 (:243) and writes a local file (`--out`, :293), classing from its own A_07 table (:60), which
this act does not touch.

**Not moved:** the Holdings tab (its producer classes by its own canonical-first rule); Cottonwood; Inflection; E_18, the silver
builder, `lib/_shared`, SSM v5 (on r3 since 10-01, batch 129). D_04's advisor-positions list groups lots by ticker string, so every
blank-ticker lot shares one group there (pre-existing; named, not changed).

## Both branches

The QA run reads unclassified at or under 5.0 pct, the shares summing to 100, every class listed: the scheduled fire is read the
same way, and the ledger closes on it. **Or** it does not (any of those fails, or a reader drops a class on the page): roll back
by the rollback below in the same window, as this morning.

## Rollback per key

Code: copy-object of the recorded prior VersionIds (today's rollback copies) onto the five keys; both watermark keys to their
pre-run versions; one ad hoc run on the old code (batch 118's path). Served keys rewrite on that run. Nothing is deleted.

## Acceptance

1. Leg R: `platinum/firm/mix_summary.json` lists every class, sums to 100 pct, unclassified at or under 5.0 pct; the run's log prints
   the identity-read hop counts; `platinum/clients/z08327149/composition.json` carries VXX under structured / Hedge and ties.
2. Leg S: the scheduled fire reads the same; one walked 49 Financial page (firm mix, one client) on PROD readers.

**Ledger:** `secclass-bd-thread-r4-reland-m-<date>`, opened before leg M; legs P, M, G, W, R, S.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-02 12:1xZ)

Signed on the blast radius above: 49 Financial's mix gains structured, cash, commodities and unclassified as lines, unclassified
4.63 pct with its residual listed; no other firm moved; a measured rollback. Read at signing: the branch at 29747a2ecb (87 tests,
the negative controls), the real run on 09-30, the lineage sweeps, the residual list. NOT read: a page walk (PROD readers absent).
