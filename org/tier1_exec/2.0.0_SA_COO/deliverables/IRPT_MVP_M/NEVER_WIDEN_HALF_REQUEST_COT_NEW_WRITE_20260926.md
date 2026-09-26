# Never-widen half requested -- the bd-securities write from the ONE COT classification run, with batch B re-cut

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO`, 2026-09-26 ~03:3xZ. The CTO's CALL-2 terms (msg 101072, @37025a10e9): "The
bd-securities write comes to me as a never-widen half naming the class flips and their readers, the same shape as
batch A." The half is built under Andrew's rules of ~02:3xZ (@c3dde578b9) and REPLACES batch B act 2 (@4fdc4284c9), whose
37 keys held securities under the older wording.

**Recommendation:** sign Part 1 now. Sign Part 2 to land after the act-1 read-back on Monday.

## The act

- **Write:** a conditional `PutItem` per key into DynamoDB `bd-securities`, with `attribute_not_exists(ticker)`. No existing
  item is overwritten. The item shape is B_01b's (ticker, asset_class, sub_asset_class, confidence, needs_review,
  classified_by `gpt-5.4-mini`, rationale, asset_name_raw, last_updated), plus `classified_run = irpt-m-cot-new-20260926`
  for the rollback.
- **The keys:** a literal list, `COT_NEW_WRITE_SET_20260926.json` (this directory), from the builder
  `build_cot_new_write_set.py` over `CLASSIFY_COT_NEW_RESULTS_20260926.json` @c3dde578b9. The ordered key list's sha256
  is b5ec3d9decb7d195...
  - **Part 1:** 941 keys (sha256 of the sorted list c96398886f143f54...): 500 equity, 403 fixed_income,
    38 alternatives.
  - **Part 2:** 26 keys (389f0e6674545567...), all `other`: the Investor Manual Asset rows (home, primary residence,
    car, jewelry, credit card, mortgage, bank account, savings, insurance, IRA, 401K, 529, HSA, pension, trust, LLC,
    brokerage, investment property, joint investment, annuity, alternatives, other asset), plus Voya, Gilder Gagnon
    Howe and Leader Bank IRA.
- **Key form:** 210 of the 967 keys are ticker-shaped, and 757 are `NAME::`. A ticker key is reachable from ANY firm's
  holdings through layer 1, which is why BD appears below.

## The rules applied (Andrew @c3dde578b9; ~M on its REC under the self-drive arm @ce6aa15a17)

- **R2a** `other` only for a personal or held-away asset. ~M decided the held-away accounts (Voya, Gilder Gagnon Howe,
  Leader Bank IRA) as `other` on its REC. No key needed an override.
- **R2b** A security the model called `other` is EXCLUDED, 35 keys, and keeps C_06's answer today (equity). They are
  listed in the JSON: coins, escrow and bankrupt shares, SBR, INVESCO LTD SHS, AST and TA portfolios, CUSIP stubs.
- **R1** An established equity never moves: 7 keys that the table already says are equity, which the model moved to
  alternatives. They are EXCLUDED: CMRF, NLOP, WP CAREY, VANGUARD REAL ESTATE INDEX ADMIRAL, ALERIAN MLP, SPROTT
  URANIUM MINERS, VANECK OIL SERVICES. Rule 1 outranks the REIT-is-alternatives rule for the three REITs.
- **R3** (~M's REC) No move to equity from fixed_income or alternatives that C_06 already assigns by name: 10 keys
  EXCLUDED. The model's "ETF -> equity" line would have sent a 1-3 month T-bill ETF, a 25-year zero-coupon Treasury
  fund and a REIT to equity.

## Which values move (read from the producer's rule)

Before and after are `classify_holding` over every row of the partition, with the new items added to a loader built
from the live table. They are not predicted from the class column.

| Reader (served) | Part 1 | Part 2 |
|---|---|---|
| COT C_06 client mix, 2026-09-22 partition | $12,112,208.72 equity -> fixed_income; $878,523.96 equity -> alternatives; 90 relationships | $48,406,121.35 equity -> other; $317,000.00 alternatives -> other; 20 relationships (largest z09305589, $19,653,063.27) |
| BD C_06 client mix, 2026-09-23 partition | $6,852,900 equity -> fixed_income (STATE STREET SPDR PORTFOLIO HIGH YIELD BOND $6.79M, bond ETFs); $456,856 equity -> alternatives (gold and silver trusts; VANGUARD REAL ESTATE ETF $5,487); 656 rows, 652 accounts | none (0 BD rows reach a Part-2 key) |
| a07 dim_asset_classification (49F/INF/COT union dim; runs on the ENABLED advi-49f-gold-floor schedule) | NOT MEASURED. It is a verbatim port of the same 4-layer classify, materialised from this table at build, so the same keys move by the same rule at its next build | same |
| Holdings (IRPT served snapshots) | Not moved by this act. The classes change at the next publication, itself a separate signed act (R4 enable) | same; `other` is admitted in the Holdings enum (~P @3d5a590ad0) |

What the write does NOT move: the 9,936 existing items; the `etf-classifications` table (Positioning); INF Orion-native
composition; Schwab composition.

Every Part-1 move is a correction, checked by name on the 25 largest (municipal funds, bank CDs, bond ETFs to
fixed_income; gold and silver to alternatives). 5 of the 967 carry `needs_review` (confidence below 0.7); they are
written with the flag, as batch A did.

## Writers of the property (N = 3, each read)

1. `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py` on BD writes net-new keys only (`attribute_not_exists`
   in intent; it skips existing keys). It never overwrites these.
2. `data/cot/scripts/gold/B_01b.classify_new_securities.py` serves the empty-prefix no-op on S3 (S141, restored
   nSr3.NM7H...). CLOUD's fixed version does not deploy before this half is signed.
3. This act, once per key, conditional.

## The half's two branches

- **The part lands:** every key exists with `classified_run` set. C_06 moves the amounts above at the next scheduled
  run, COT on Monday 2026-09-28 and BD on its next trading-day run. a07 follows at its next build.
- **A key refuses** (a condition failure on a key that appeared since the census): that key is skipped and counted,
  never overwritten. The census re-runs on a fresh scan first, and the act refuses if the list's sha differs.

## Rollback per key

`DeleteItem` on each written key with the condition `classified_run = irpt-m-cot-new-20260926`, from the same literal
list, under a human confirmation. No key existed before, so a delete restores the prior state exactly.

## Order

- **Part 1:** on signature, under ledger `bd-securities-cot-new-p1-m-20260926`. The read-back is get_item for every key,
  and a fresh loader classifying the ten largest movers as signed.
- **Part 2:** after (1) the act-1 read-back (ledger cot-other-admission-m-20260925 R1, Monday's first COT run: `other`
  in the mix at 0) and (2) ~D's IR `other` mapping on origin DEV. The CTO-added render condition is MET (PROD 36a37afc,
  msg 101054). Read-back: z09305589 shows its Other slice at $19,653,063.27 on the portal, read by ~D.
- **B_01b deploy:** a separate act, after Part 1. The COT prompt is first amended to rule 2 (the `other` wording is
  narrowed), with a dry run.

## The ask

Sign Part 1 now and Part 2 on its two conditions, or refuse, naming what is missing. Batch B act 2 (@4fdc4284c9) is
withdrawn in favour of Part 2.
