# ADVI_BDPRCE -- every served Black Diamond price and lot for 49 Financial comes from a written rule and an exact source

```json
{
 "project": "ADVI_BDPRCE",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v1.2",
 "step": 4,
 "brief_ref": "docs/briefs/bd-pricing-rules-brief-20261013.md@f2171cae6c",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~13:0xZ. **Placement:** DELL1, directive D8, macro ADVI. Registered @479cfafba1.
**Brief:** `docs/briefs/bd-pricing-rules-brief-20261013.md` @f2171cae6c (`4.0.0_SA_CRO~DELL1`), O1-O8. PART VIII is confirmed by Andrew as written.
**Endpoint:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_ADVI_BDPRCE_20261013.md`.
**Lineage:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/BD_SHARE_COUNT_LINEAGE_AND_EXACT_SOURCES_20261013.md`.

**Andrew's words this PRD executes (verbatim anchors):**
- DONE WHEN, "Yes as written" (2026-10-13 ~12:1xZ): `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_121xZ_BD_PRICING_RULES_DONE_WHEN_CONFIRMED_AND_CAP_CLARIFICATION.md`.
- The constraint: "any 'estimation' is highly risky for performance reporting that needs to be exact" (same record).
- Capped lots, "Agreed with this positioning" (~12:2xZ): they read UNVERIFIED until exact custodian units and cost are sourced.
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_CAPPED_LOTS_UNVERIFIED_SHARE_COUNT_SOURCES_PORTAL_SMOKE_WSJ_CREDS.md`.

**No COO is seated.** L5 and L6 wait on a `2.0.0_SA_COO` lane taking this project (one project per Tier-2 seat).

## ENDPOINT (step 2, /endpoint --forward)

Quoted from the endpoint record. The ids are permanent.

```
  FWD-1  One 49 Financial advisor sees one untickered holding valued by a stated rule, and an analyst traces that price to its rule and trades
         DONE WHEN  EXERCISED -- on the served T-1 object, a seat opens ONE 49F client account holding ONE untickered security, reads its served price,
                    and from the record alone names the rule that produced it and the trades (by trade id) behind it; the recomputed price from
                    those inputs equals the served price
         ACCEPT     an Opal analyst asking "where did this price come from?" gets the rule and its trades without reading code
         SOURCE     brief PART I thread; DONE WHEN 1-2; O1, O2

  FWD-2  Every served 49F price comes from a rule written in ONE place (DONE WHEN 1)
         DONE WHEN  EXERCISED -- a census of every writer of the served T-1 price (the measured writers plus the four-times-a-day canonical writer) shows
                    each one calling the one written rule, or retired; a planted rule change in that one place moves every writer's output
         ACCEPT     an engineer changes a pricing rule in one place and no older copy survives anywhere
         SOURCE     O6; DONE WHEN 1

  FWD-3  Any served price traces to its rule and inputs (DONE WHEN 2)
         DONE WHEN  EXERCISED -- for a sample spanning every price source (override, trade median, interpolation, vendor), the trace names the rule and
                    inputs and the recompute equals the served value; the sample is set in DEC-10
         ACCEPT     an analyst can trace ANY served price, not only the thread's
         SOURCE     O1; DONE WHEN 2

  FWD-4  An untickered holding is valued at the median of DISTINCT trades
         DONE WHEN  EXERCISED -- the T-1 median counts each transaction once however many portfolio groups repeat it (S32: 830 of 5,366 asset-days moved
                    at measurement), served under FWD-7
         ACCEPT     a price is not weighted by how many groups hold the asset
         SOURCE     O2; ADVI_FIRMBKTS-D1-S32

  FWD-5  The price shown for a date is the same on every run
         DONE WHEN  EXERCISED -- two runs over the same inputs serve byte-equal prices; a same-date tie between sources is decided by a written
                    precedence (S33), with a planted tie as the arm
         ACCEPT     an advisor never sees a price change because of a sort order
         SOURCE     O3; ADVI_FIRMBKTS-D1-S33

  FWD-6  A past date's figure reads that date's trades
         DONE WHEN  EXERCISED -- each served reader keys on trade_date, not the transactions file day (DEC-6),
                    with a moved trade as the arm (S34)
         ACCEPT     a past date's gain or price is built from the trades of that date
         SOURCE     O4; ADVI_FIRMBKTS-D1-S34

  FWD-7  Every price this project moves, moves under a fix Andrew saw first (DONE WHEN 3)
         DONE WHEN  EXERCISED -- for EACH fix, a named before/after list (asset, date, old, new, and the dollar effect on the latest snapshot) is put to
                    Andrew BEFORE the deploy, and the deploy's read-back equals that list
         STANDING WAIT, qualified (rule 27): REASON -- these are client-visible prices and values on partner-facing pages; DISCHARGING ACT --
                    Andrew's review of that fix's named diff. The wait is per fix, never open-ended, and no other FWD waits on it.
         ACCEPT     no client-visible price changed without Andrew having seen exactly what would change
         SOURCE     O5; DONE WHEN 3

  FWD-8  Every served per-lot gain compares value and cost on one consistent basis (DONE WHEN 4)
         DONE WHEN  EXERCISED -- no served lot shows a gain from a scaled market value against an unscaled cost; a capped lot's value and gain read
                    UNVERIFIED (never an estimate) until FWD-9 supplies exact units and cost; the 64,629 capped lots (13 pct, at measurement) are read
                    one by one
         ACCEPT     an advisor never sees a large loss that exists only because the market value was compressed
         SOURCE     O7; Andrew's ~12:2xZ ruling; DONE WHEN 4

  FWD-9  Each lot's units and cost come from an exact source
         DONE WHEN  EXERCISED -- with BD's Units and Cost Basis switched on in the 49F unrealized export and the silver de-duplication keyed on the
                    lot (cell 1, reversible), each served lot carries units and cost from BD's export or the custodian's lot file (Schwab ULN/RPS);
                    FIFO-only lots read UNVERIFIED; BD versus FIFO is measured per lot with the denominator printed before any served value moves
         ACCEPT     no served lot's units or cost is a reconstruction from transaction history
         SOURCE     O8; lineage record section 4
```

**Not in scope:**
- MDPF valuation;
- IRPT performance math, which is a READER of these lots and is named in every FWD-7 blast radius;
- the exec-summary slots, which are ADVI_FIRMBKTS's and stay off until FWD-8 serves.

## CONTRACTS

| contract | direction | shape | consumer / producer |
|---|---|---|---|
| **the price rule** | **produced** | ONE module, imported by every writer of a served 49F price (FWD-2). It holds the T-1 trade-observed median over DISTINCT `transaction_id` (FWD-4); the source precedence `SOURCE_RANK` as it stands today (`data/black_diamond/scripts/silver/bd_price_update.py:65-71`: `scoped_override` -2, `yahoo_finance` -1, `transaction_observed` 0, `linear_interpolation` 2, `carry_forward` 3), with a STABLE secondary key on a same-date tie (FWD-5); and the date key (FWD-6, DEC-6). No writer keeps a private copy. | every writer of `silver/prices` and `canonical_prices.parquet`; B_01 |
| **the lot units-and-cost record** | **produced** | per open lot: `units`, `cost_basis`, and the source of each (`schwab_uln`, `bd_unrealized`, `schwab_rps_units`, or `none`), plus `verification` = `VERIFIED` or `UNVERIFIED`. A lot whose units or cost has no exact source is UNVERIFIED. Its served `market_value` and `accrued_gain` are then NOT an estimate: they are absent, with the status, and never scaled (FWD-8). | B_01 and every reader of its lots |
| **account totals** | **consumed, unchanged** | an account's served total value stays BD's own account value (`silver/allocations`), never a sum of lots. That is what keeps totals exact while some lots read UNVERIFIED. A reader that SUMS lots into an account figure is named by the C3 census and changed under FWD-7 before any lot reads UNVERIFIED. | BD's export (producer); every account-level reader |
| **the BD unrealized export (qt4)** | **consumed, configuration changed** | template `data/black_diamond/scripts/bronze/templates/unrealized.json`, measures 15 (Units) and 16 (Cost Basis) switched ON. The runner reads its S3 copy `s3://opal-data-bd/code/bronze/templates/unrealized.json`, measured 2026-10-13 equal to the repo (sha256 equal, 14,419 bytes), VersionId `VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE`, LastModified 2026-06-30T17:15:38Z, with 15 and 16 both `isSelected: false`. | Black Diamond DataMining (producer); this project's silver step |
| **the legacy silver unrealized table** | **consumed, BYTE-UNCHANGED** | `silver/unrealized/<date>.parquet` keeps its rows, columns and values exactly. Its `(account_id, asset_name)` keep-first de-duplication (`data/black_diamond/scripts/silver/merge-daily-incremental.py:1205-1210`) is NOT changed in place, because B_01's veto set, injections and cap classes read it today. The lot-level data goes to the NEW table below. | B_01 and its other current readers |
| **the lot-level unrealized table** | **produced, NEW** | every lot row of the qt4 export, with Units and Cost Basis, de-duplicated on the LOT (`relationship_id`, `account_id`, `asset_id`, `open_date`, `unit_cost`), or on the export's own lot identifier where one exists (v1.1), never on the position. **Address, builder output (Rule 30):** `lib/opal_naming.py address("blackdiamond", "49financial", "silver", "unrealized_lots", "date=YYYY-MM-DD")` returns `s3://opal-data-assets/blackdiamond/49financial/silver/unrealized_lots/date=YYYY-MM-DD` (run 2026-10-13). Source `bd` is REFUSED by the builder ("not a systems.json key"), so the registry key `blackdiamond` is used; nothing is typed. | C2's measure; C4's unit authority |
| **the never-widen pair per served move** | **consumed** (law) | each fix that moves a served price, lot value or gain is its own act under a CTO and COO pair. The pair names every asset, date and client-facing figure that moves, and the rollback per key. FWD-7 adds Andrew's review of the named before/after list BEFORE the deploy. | every fix cell |
| **inherited law** | **consumed** | Rule 30 for any NEW address; R19 (the legacy pipeline's own migration is not a rider here); the push law for any client-facing PROD page; the alert moratorium (no new monitor). | the law surface |

## THE DECISIONS -- CLOSED AT L4

- **DEC-1 Unit and cost authority, in order.** Per lot:
  1. the Schwab ULN lot file (`schwab/silver/uln`: `quantity`, `cost_basis`, `adjusted_cost_basis` per lot), where the account is Schwab and the lot is present;
  2. the BD unrealized export's Units and Cost Basis (the new lot table);
  3. Schwab RPS quantity, for units ONLY, never cost (today's RPS cost is set to the current price, B_01:1662, which is not a cost).
  FIFO reconstruction is NEVER an authority for a served value. It stays as a reconciliation figure. Where 1 and 2 both exist and disagree, the disagreement is a row and
  the lot reads UNVERIFIED until it is ruled.
- **DEC-2 No estimation in a served lot figure** (Andrew's constraint):
  - A capped lot, and any lot without an exact source under DEC-1, reads UNVERIFIED: its value and gain are absent, with the status.
  - The 2026-04-17 cap's SCALING stops being a served figure once C4 lands. Whether lots are capped at all remains B_01's approved design (brief PART II); this project
    changes only what is SERVED for them.
  - Synthetic-injection lots (B_01:1985-2050: units from value divided by our price, cost set equal to value) are estimates under the same rule. They read UNVERIFIED unless
    DEC-1 supplies exact data.
- **DEC-3 The template change and the new table are one reversible configuration act, with no served move.** Switching measures 15 and 16 on changes the qt4 export's columns.
  The legacy silver step therefore DROPS the two new columns from `silver/unrealized` (byte-unchanged, proved on the first export: rows, columns and values equal against the
  previous run's construction), and routes them only to the lot table. Rollback: restore template VersionId `VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE`.
- **DEC-4 S32:** the T-1 median counts each `transaction_id` once. The loader de-duplicates on `transaction_id` before the median (`bd_price_update.py` per-date loader
  :263-271). Measured effect at brief time: 830 of 5,366 asset-days move (max delta 753.5). Served under FWD-7.
- **DEC-5 S33:** a same-date tie is decided by `SOURCE_RANK` as written (adopted, not re-decided), then by a stable secondary key (`asset_name`, then the source label), with a
  STABLE sort (`kind="mergesort"`). The pandas version on the gold runner is read and pinned before FWD-5 is claimed on the live host (brief V.6).
- **DEC-6 S34, ruled here from the outcome's own text:** FWD-6 ACCEPT says "a past date's gain or price is built from the trades OF THAT DATE". The reading is
  **trade date**: every served reader keys transactions on `trade_date`, never the file day (`B_03.account_gains.py:327`, `bd_price_update.py:265` and its Lambda twin :143).
  At brief time the measured effect is 2 of 12 served 2026-08-20..23 objects under the instant reading and 0 under the strict reading. The cell re-measures under
  trade-date keying and serves under FWD-7.
- **DEC-7 FWD-7's diff, per fix:** a named list (asset, date, old, new, and the dollar effect on the latest snapshot) PLUS the downstream readers it moves (MDPF_SECCLASS's BD Mix,
  IRPT_DASHBD, IRPT performance, any ADVI page). It is put to Andrew BEFORE the deploy, and the deploy's read-back must equal the list. The wait is per fix and never
  open-ended, and no other FWD waits on it.
- **DEC-8 Preconditions from the brief, each a gate on the FWD it names:**
  - the four-times-a-day `canonical_prices.parquet` writer is identified before FWD-2 (V.3);
  - the 603-of-1,610 trace gap (PART VI.3) is explained or bounded before FWD-1 and FWD-3 (V.7);
  - ADVI_FIRMBKTS's act-4 read-back is complete (V.1). It is MET 2026-10-12, edge applied 15:15:10Z (FIRMBKTS act-4 half ADDENDUM 8).
- **DEC-9 Cross-project:**
  - ADVI_FIRMBKTS's served 49F home is `opal-data-49financial` since act 2. Every served read and write here goes to the canonical home, never the legacy one.
  - The exec-summary position slots stay disabled until FWD-8 serves (FIRMBKTS sample read ADDENDUM 1).
  - Any restatement of past client-facing figures reaches a PROD page only on Andrew's word (brief V.5).

- **DEC-10 FWD-3's sample:** drawn from the served 49 Financial price objects of the latest frontier date and four earlier trading dates (five dates,
  each read from `lib/trading_calendar.py`).
  - **Per price source:** at least 30 prices from each of override, trade median, interpolation and vendor. If a source holds fewer than 30 across the five dates,
    ALL of them are taken and the shortfall is printed.
  - **Total:** at least 150 prices.
  - **The draw is DETERMINISTIC:** rows ordered by `sha256(asset_id|date|"ADVI_BDPRCE-FWD3")` and the first N taken per source, so any seat reproduces the same sample.
  - **Plus every price of FWD-1's thread holding.**
  - The trace PASSES only on 100 pct: every sampled recompute equals its served value to the cent. Any miss is named with its rule and inputs, and FWD-3 stays NOT
    REALIZED until it is fixed or explained.

## PROJECT ARC AND DEFINED OUTCOME

**Defined outcome:** every served 49 Financial price comes from one written rule, traced to its trades. Every lot's units and cost come from an exact source, or the lot says
UNVERIFIED. Nothing client-visible moved without Andrew seeing the list first.

**Arc (round 1 builds the thread, FWD-1; later rounds enrich):**
1. The censuses and the reversible exact-data switch (C1, C3, C5), plus the measure (C2). These are reads or reversible configuration only.
2. The thread: one untickered holding traced end to end (C9, C10).
3. The rule fixes, each under FWD-7 (C6, C7, C8).
4. Unit authority and UNVERIFIED (C4) under FWD-7, after C2's measure and C3's reader census.

## CELL CANDIDATES

The decomposition at L5 is the COO lane's, and it may split, merge or re-sequence these.

| cell | serves | brief | contracts C / P | acceptance draft |
|---|---|---|---|---|
| **C1 exact-data switch** | FWD-9 | O8; V.10 | C the qt4 export; P the lot-level table | the S3 template is re-read equal to the repo before the change; measures 15 and 16 are on; the first export after it yields `silver/unrealized` BYTE-UNCHANGED (rows, columns, values) and the lot table at the builder address, carrying units and cost per lot; rollback names the template VersionId |
| **C2 the measure** (read-only) | FWD-9, FWD-8 | V.11 | C the lot table, Schwab ULN, B_01 lots | for the capped lots (64,629 of 492,998 at brief time, re-counted and printed), BD units and cost against FIFO, and Schwab ULN against FIFO, per lot. The denominator and the exact-source coverage are printed per source, and so is the residue with no exact source |
| **C3 reader census** (read-only) | FWD-8, FWD-7 | O7 | -- | every reader of B_01 lot `market_value` and `accrued_gain` is named, with whether it SUMS lots into an account or firm figure; each is classed client-facing or internal |
| **C4 unit authority and UNVERIFIED** | FWD-8, FWD-9 | O7, O8; DEC-1, DEC-2 | P the lot units-and-cost record | under a FWD-7 pair: lots take DEC-1's authority; a lot without one reads UNVERIFIED with value and gain absent; account totals are unchanged against BD; no served lot gain compares a scaled value to a whole cost |
| **C5 writer census and the rule's home** | FWD-2 | O6; V.3 | P the price rule | every writer of the served T-1 price is named, the four-times-a-day writer included; each imports the one rule or is retired; a planted rule change in the home moves every writer's output |
| **C6 S32 distinct median** | FWD-4 | O2; DEC-4 | C the price rule | under a FWD-7 pair: the median counts each `transaction_id` once; the asset-days that move are re-measured and listed before the deploy |
| **C7 S33 ties** | FWD-5 | O3; DEC-5 | C the price rule | two runs over the same inputs serve byte-equal prices; a planted same-date tie resolves by `SOURCE_RANK` and then the stable key; the runner's pandas version is read |
| **C8 S34 trade-date keying** | FWD-6 | O4; DEC-6 | C the price rule | under a FWD-7 pair: the three readers key on `trade_date`; a moved trade is the arm |
| **C9 trace instrument and the 603/1,610 gap** | FWD-1, FWD-3 | O1; V.7 | -- | the trace reproduces the served price from its rule and inputs; the gap is explained or bounded with its denominator |
| **C10 the thread** | FWD-1 | PART I thread | -- | on the served T-1 object, one 49F account holding one untickered security: its served price, rule and trade ids named from the record, and the recompute equal to the served value |

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| edit (configuration) | `data/black_diamond/scripts/bronze/templates/unrealized.json` and its S3 copy `s3://opal-data-bd/code/bronze/templates/unrealized.json` | C1 | measures 15 and 16 on |
| edit | `data/black_diamond/scripts/silver/merge-daily-incremental.py` (`process_unrealized_xlsx_to_parquet`, :1138-1215) | C1 | the legacy output byte-unchanged; the lot rows routed to the new table |
| new | `s3://opal-data-assets/blackdiamond/49financial/silver/unrealized_lots/date=YYYY-MM-DD` (builder output, above) | C1 | the lot-level table |
| edit | `data/black_diamond/scripts/gold/B_01.holdings_lots.py` (`_apply_silver_noncash_cap` :2291; RPS cost :1662; synthetic :1985-2050) | C4 | unit authority and UNVERIFIED |
| edit | `data/black_diamond/scripts/silver/bd_price_update.py` (:65-71, :263-271, :265, :344) and its Lambda twin | C5-C8 | the one rule, imported |
| edit | `B_03.account_gains.py:327` | C8 | trade-date keying |
| new | the one rule module (its location is chosen at L5 within `data/black_diamond/scripts/`) | C5 | the single home |
| new | `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/` | C2, C3, C5, C9, C10 | censuses, measures, traces |

## BRIEF COVERAGE

**Denominator:** the brief @f2171cae6c has 8 outcomes (O1-O8) and Parts II, V and VIII as binding text.
- O1 -> FWD-1, FWD-3
- O2 -> FWD-4
- O3 -> FWD-5
- O4 -> FWD-6
- O5 -> FWD-7
- O6 -> FWD-2
- O7 -> FWD-8
- O8 -> FWD-9
- PART V items 1-11 -> DEC-8 (1, 3, 7), DEC-7 and the pairs (4), DEC-9 (5), DEC-5 (6), DEC-2 (8), DEC-9 (9), DEC-3 and C1 (10), DEC-1 and C2 (11).
- PART II boundary -> CONTRACTS, DEC-2 (the cap's existence is not owned) and DEC-9.

## SURFACE MANIFEST

| surface | kind | cell | owner |
|---|---|---|---|
| the qt4 template (repo and S3 copy) | APPLIED configuration, reversible | C1 | ADVI_BDPRCE |
| `s3://opal-data-assets/blackdiamond/49financial/silver/unrealized_lots/` | NEW table | C1 | ADVI_BDPRCE |
| `silver/unrealized` | byte-unchanged (proved) | C1 | its current owner |
| B_01 lots (`market_value`, `accrued_gain`, units, cost, verification) | SERVED change under FWD-7 | C4 | ADVI_BDPRCE |
| served T-1 prices (`silver/prices`, `canonical_prices.parquet`) | SERVED change under FWD-7 | C5-C8 | ADVI_BDPRCE |
| `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/` | documents | C2, C3, C5, C9, C10 | ADVI_BDPRCE |
| other firms' buckets; vendors; the Bloomberg queue; the cap's existence | excluded | -- | untouched |

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM v1.1 (2026-10-13 ~21:3xZ) -- the lot key gains the relationship id (contract row only)

**Call** `dell1-20261013T212600Z-239a`, ruled by this seat under `/self-drive` on the dell1 box (Andrew ~20:3xZ, the box CTO adjudicates every open call).
- **The measurement:** BP-b-6 (merged @e33999e30b), on the 2026-10-09 export of 500,000 rows. The v1.0 lot key (`account_id`, `asset_id`, `open_date`, `unit_cost`) folds
  15,553 rows, and 14,514 of the 14,696 colliding groups differ on Relationship ID (row ADVI_BDPRCE-D1-W10-S2, ARMED). Applying the export-template change under that key
  would DROP distinct lots, the opposite of FWD-9's exact units.
- **RULING:** the lot key becomes (`relationship_id`, `account_id`, `asset_id`, `open_date`, `unit_cost`), or the export's own lot identifier where it carries one.
  - BP-b-6's fixture proof re-runs on the new key as ONE small cell before any apply. It prints the rows folded and the colliding groups that still differ on any column.
  - The template apply stays under its own never-widen pair.
- **Not changed:** every ENDPOINT outcome. This is a CONTRACTS wording change, so under proportionate sign-off it withholds no delivery; the CVO reads it at the next signing.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM v1.2 (2026-10-14 ~01:1xZ) -- CONTRACTS wording correction (row W10-S1)

The CONTRACTS claim that the 49 Financial unrealized template is "sha256-equal" to Cottonwood's is FALSE as bytes: CRLF 14,419 bytes against LF 13,920. The two are equal only after
line-ending normalisation. **Corrected:** "equal after LF normalisation (sha256 of the LF-normalised bytes); the committed bytes differ by line endings only". Any check that
compares the templates normalises first and prints that it did. Not changed: every ENDPOINT outcome.

-- 1.0.0_SA_CTO~DELL1
