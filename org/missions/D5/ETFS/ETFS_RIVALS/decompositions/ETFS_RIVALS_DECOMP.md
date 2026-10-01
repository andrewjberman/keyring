# ETFS_RIVALS -- DECOMPOSITION, ROUND 3 (ENRICHMENT): the home funds, identity, GICS, and the round-2 repairs

```json
{
 "project": "ETFS_RIVALS",
 "round": 3,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@01114ae8a8 (v0.7: C-SHAPES amended per row S1 reading (a))",
 "prd_version": "v0.7",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round2.md@01114ae8a8",
 "author": "2.0.0_SA_COO~RV",
 "cells": 6,
 "chains": 3,
 "join_cells": 1,
 "frozen": true,
 "revision": "1.0 at L5",
 "round2_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round2.md (blob fd1929706d of the round-2 file)"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-01 ~07:xxZ.

**Source:** `1.0.0_SA_CTO~Z` msg 27555, the round-2 analysis section 3 (ENRICHMENT LIST), items 1-5, plus rulings 1-6 and 10.

**Input state:**
- Round 2 is 9 of 9 terminal and CLOSED.
- The live join (RIV-d-3) has landed. Ledger `etfs-rivalfunds-round2` is CLOSED.
- Bloomberg bronze holds 937 captures. The page is served grouped by Opal fund, with 6 of 13 funds updated.
- The 08:03 rivalfunds leg is enabled. It waits on the Terminal sign-in.

## Issuer rulings at this cut (inside the decomposition)

1. **Analysis ruling 1 rests on a retracted premise (row Z-S4 @ea3a4c7636; decision record to the CTO, 06:14Z).**
   - W2-S4's `_capture_id` ordering fix is already live: 1faa6d4f8d, deployed by d-3 at 04:10Z.
   - What remains on the issuer side is the W5-S24 class: `silver_issuer` deletes the superseded object, but the build-silver
     role has no `s3:DeleteObject`. The hazard has not fired (1 object per date over 325 dates).
   - Item 1 therefore becomes a LOCAL repair (supersede without delete). It sits in the round's ONE repair cell, RIV-r-3. Its
     live positive control (a re-capture of one landed BASG date) is the act of RIV-d-4, under that cell's pair.
2. **Identity (analysis ruling 6) is built INSIDE ETFS_RIVALS, in the crosswalk's key grammar, and writes NOTHING into the AMGT
   pool.**
   - `lib/research/identity/` (the crosswalk object, `registrations.json`, `add_security`) belongs to AMGT_RESAPP. Its rounds are
     live (drain 78167bb8fc was merging as this cut began). A second writer there is a cross-project write surface this
     project does not own.
   - ETFS_RIVALS calls `crosswalk.resolve()` first, as today. On a miss it resolves by two MEASURED rules:
     - a Bloomberg row's own id (`'ABNB US Equity'`) in the key grammar (`ABNB_US_Equity`);
     - an issuer row joined to its fund's Bloomberg row at the same report date, by equal root ticker and shares within 2%,
       with a unique candidate.
   - Measured at the cut: the join resolves 34 of 34 BASG non-cash rows on 2026-09-28 with 0 ambiguous. Exact share equality
     resolves 0, because the two sources differ by about 0.1%. Nothing is minted by appending a suffix (the crosswalk's own law).
   - Registering the rivals' securities in the AMGT pool is the CTO's to place, if wanted.
3. **G4 GICS has two halves on two writers.**
   - RIV-s-4 builds the G4 producer on the terminal machine (scripted, R-21). Its import mode reads the Positioning pull's REAL
     Bloomberg responses in `bbg/<D>/characteristics.parquet` (GICS sector and industry group, with the 4-digit code) as
     QA-class input, with provenance.
   - RIV-g-6 joins G4 into `canonical_shape`. That file has one writer per round slot, so it is serialised on `~1` after
     RIV-hp-1 and RIV-i-1.
4. **GQGU is not cut.** Rows Z-S5/Z-S6 are filed. GQGU has a measured issuer route (SEI filepoint, 305 archived days) and is
   carried to the CTO for placement. It is not on the enrichment list.

## Rulings reaching every cell

- **Rounds 1 and 2's rulings stand**, verbatim in `ETFS_RIVALS_DECOMP.round1.md` and `ETFS_RIVALS_DECOMP.round2.md` under
  "Rulings reaching every cell": builder-only addresses and names, partition dates, the stage entry contract, batch-complete
  markers, real data on the seam, classification, snake-case state tables, the universe as the map, and the Bloomberg channel
  on the terminal machine.
- **Builder output, measured at this cut:** `address('rivalfunds','etfs','gold','security_market','date=<D>')` ->
  `s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=<D>`, generated at v0.3 with the other 13 gold tables.
- **No new stage name.** G4 is written under the existing `pull-enrichment` stage. No cell edits `homes.py`.
- **The Positioning pull is never edited** (Andrew-direct 2026-09-30, record
  `deliverables/2.0.0_SA_COO~RV/ANDREW_DIRECT_20260930_20xxZ_DO_NOT_MODIFY_POSITIONING_PULL.md`). Its landing is READ:
  - `s3://opal-data-etfs/bbg/<D>/constituents/constituents_issuer_fill.parquet` (holdings, for the home funds);
  - `s3://opal-data-etfs/bbg/<D>/characteristics.parquet` (GICS, QA import).
  - Nothing is written under `bbg/`.
- **No Bloomberg call by any worker in a build cell.** The Terminal is signed out. The live G4 pull runs in the enabled vehicle
  leg, via `enrichment_bloomberg` daily mode, after Andrew's sign-in (analysis section 5).
- **No alert, monitor or notifier.**

## 1. THE DOMAIN, BY SUBTRACTION

Domain = the analysis's enrichment list plus rulings 1-6 and 10. Printed denominator: **5 items + 2 placed rulings
(ruling 1's premise retracted, ruling 10's row) = 7**.

| item | source | cell(s) | residue |
|---|---|---|---|
| 1 W2-S4 / Z-S4 issuer-side retain | ruling 1 (premise retracted) | RIV-r-3 (code), RIV-d-4 (live control) | 0 |
| 2 W5-S23 narrowed gate + W5-S28 trading-day freshness | ruling 2, 3 | RIV-r-3 | 0 |
| 3 W1-S8 home-producer reader | ruling 4 | RIV-hp-1 | 0 |
| 4 W1-S4/S5 identity, floor, marker | ruling 6 | RIV-i-1 (identity), RIV-r-3 (marker), RIV-d-4 (floor) | 0; AMGT pool registration is not this project's write |
| 5 G4 GICS under C-SHAPES v0.7 | ruling 5 | RIV-s-4 (producer), RIV-g-6 (G1 join) | 0 |
| GQGU row | ruling 10 | rows Z-S5, Z-S6 | the adapter is not cut (not on the list) |
| the live join of 1-5 | the round's served outcome | RIV-d-4 | 0 |

**NOT this round, by subtraction:**
- Analysis ruling 7, round 4: W1-S11, W3-S11, W3-S12, W5-S21.
- Ruling 8 (S2): fabric.
- G7-G13 and the prompts: not on the list.

## 2. THE RECTANGLE -- 6 cells

| cell | serves | status at the cut (evidence) | risk | class |
|---|---|---|---|---|
| `RIV-r-3` | FWD-2, FWD-5, FWD-9 | PARTIAL: r-3.AC1-AC3 FAIL at base (superseded issuer silver is deleted; the round-2 gate skips the whole batch; a 1-trading-day Bloomberg lag fails at threshold 0; no marker on a not-updated page) | LOCAL | worker |
| `RIV-hp-1` | FWD-1, FWD-2, FWD-3 | ABSENT: hp-1.AC1/AC2 FAIL at base (IDVZ 0 of 41 and PFOE 0 of 25 landing rows in G1; the placeholder text is served) | LOCAL | worker |
| `RIV-i-1` | FWD-4, FWD-5 (C-TRADE-SCHEDULE: resolved identity) | PARTIAL: i-1.AC1 FAIL at base (BASG issuer 0 of 33 resolved; WCMG 8/48, TSEL 15/28, ETFT 14/29, PCLG 19/29) | LOCAL | worker |
| `RIV-s-4` | FWD-4 (C-SHAPES GICS), FWD-6 (G4) | ABSENT: s-4.AC1/AC2 FAIL at base (no G4; no market plan) | LOCAL | worker |
| `RIV-g-6` | FWD-4 | ABSENT: g-6.AC1 FAIL at base (no G4, GICS UNRESOLVED) | LOCAL | worker |
| `RIV-d-4` | the live join of 1-5 | ABSENT: d-4.AC1-AC3 FAIL at base (no act record) | WORLD | worker |

## 3. THE CELLS -- 6 (round 3)

### `RIV-r-3` -- the round's repair cell: issuer retain, narrowed gate, trading-day freshness, the not-updated marker

1. **`silver_issuer.py` supersedes WITHOUT deleting** (row Z-S4; the W5-S24 remedy, as `silver_bloomberg.py` @e622b2fef9 does
   it):
   - remove the `_delete` of the earlier captures' silver;
   - record each one in `dropped` with `was_in_silver: True, retained: True`;
   - a re-capture of a landed report date returns OK WITH a marker.
   - `gold_canonical_shape` already reads the newest issuer object per date (`max(..., key=_revision)`), so no reader changes.
2. **The narrowed enrichment gate** (W5-S23, ruling 2). The round-2 `enrichment_gate` holds a whole canonical batch until a
   pull-enrichment marker covers its newest report date. Instead:
   - a fund is HELD only if its trade window `(prior report date, report date]` contains the ex-date of a corporate action, in
     the latest landed G3, on a security the fund holds in that window;
   - every other fund builds its G5 now, BASG included.
   - `sweep.run_gold_chain` passes the held set to `build-trade-schedule` as `event["hold_funds"]` and reports it as
     `detail["held_funds"]` (fund -> reason).
   - `build-trade-schedule` is SKIPPED only when every fund is held.
   - A held fund builds once its pull-enrichment marker arrives, as a NEW G5 object whose revision sorts after the partial one
     and carries every fund. Nothing is overwritten. The page reads the newest revision per date, as today.
3. **Trading-day freshness per source** (W5-S28, ruling 3). `report_date_freshness` counts trading days with
   `lib/trading_calendar.py`, as it already does, but the allowance is per source and measured:
   - `bloomberg` and `home_producer`: 1 trading day (Bloomberg reports one trading day late, measured in row W5-S28; the home
     producer is the Positioning pull, which runs on Bloomberg's T-1);
   - `issuer`: 0.
   - The allowance is a named constant, citing its row. The reason string names the source, the lag and the allowance in
     trading days.
4. **The not-updated publish marker** (W1-S5). When the page publishes with some funds marked not updated, `publish_page`
   still writes its marker. The marker record carries `not_updated: {fund: reason}` per fund for that batch, so the sweep does
   not re-run publish-page for the batch forever.
   - A page that publishes NOTHING (every fund failing, or a render failure) still writes no marker.

### `RIV-hp-1` -- the home-producer reader (C-HOME-PRODUCER v0.5; row W1-S8)

- **`home_producer.py` (new):** reads `s3://opal-data-etfs/bbg/<D>/constituents/constituents_issuer_fill.parquet` for the
  `home_producer` funds of the map (IDVZ, PFOE).
  - The report date is each row's `date`. The address is the producer's own (`etf_daily_pull.PREFIX` / `BUCKET`), read, never
    rebuilt.
  - Columns used: `fund_ticker`, `holding_ticker`, `cusip`, `security_name`, `shares`, `price`, `market_value`,
    `weight_pct`, `is_cash`, `date`.
- **`gold_canonical_shape.py`:** the `home_producer` policy now has a reader.
  - Each home fund's rows for the report date land in G1 with `source_used = 'home_producer'`.
  - Every row of the landing is kept (cash included, `is_cash_line` from the landing's `is_cash` or the vocabulary's
    sentinel).
  - Identity goes through the existing crosswalk path on CUSIP/ticker.
  - The report dates a replay considers include the landing dates.
- **`gold_holdings_coverage.py`:** the home funds get G2 rows from the same landing, with `source = 'home_producer'` and
  `selected = true`.
  - A trading day with no landing reads `gap`, with the cause: capture-forward from 2026-08-21, the C-HOME-PRODUCER limit.
- **The page needs no edit:** a home fund with G1 data renders through the normal fund view, and the placeholder appears only
  when G1 has none.
- **No second copy:** nothing is written under `bbg/` or any silver prefix for the home funds.

### `RIV-i-1` -- identity: measured resolution in the crosswalk's key grammar (rows W1-S4/S5; issuer ruling 2)

- **`identity.py` (new):** `bloomberg_key(bbg_id)` maps a `'<ROOT> <CC> <YELLOW>'` Bloomberg id to `'<ROOT>_<CC>_<YELLOW>'`. Any
  other shape returns None.
- **`issuer_join(...)`:** for one issuer non-cash row, the unique Bloomberg silver row of the SAME fund at the same report date
  (or the nearest Bloomberg report date within 1 trading day) whose root ticker equals the issuer `security_ticker` and whose
  `POSITION` is within 2% of the issuer `quantity`.
  - Zero candidates means a miss. Two or more means AMBIGUOUS: UNRESOLVED, with a note naming every candidate.
- **`gold_canonical_shape.py`:** after `crosswalk.resolve()` misses, it uses:
  - for a Bloomberg row: `bloomberg_key(id)`, with `resolution_method = 'bloomberg-form'` and `resolution_source` stating it is
    not in the AMGT pool;
  - for an issuer row: `issuer_join`, with `resolution_method = 'issuer-bloomberg-join'` and the share delta in
    `resolution_note`.
  - `security_bloomberg` is set from the joined or own Bloomberg id.
- **The measured fraction per fund** is reported in the cell's deliverable (`i1_identity.json`). RIV-d-4 sets the publisher's
  `identity_coverage` floor from it.

### `RIV-s-4` -- G4 `security_market`: the producer (C-GOLD-MODEL G4; scripted Bloomberg, R-21)

`enrichment_bloomberg.py` gains three modes, all writing G4 at
`address('rivalfunds','etfs','gold','security_market','date=<D>','market-<revision>.parquet')`, never-overwrite, under
stage `pull-enrichment`:
- **`plan-market`:** offline, no session. It returns the distinct non-cash Bloomberg securities of G1 at `date` and the field
  list: GICS_SECTOR_NAME, GICS_INDUSTRY_GROUP_NAME, GICS_INDUSTRY_GROUP, GICS_INDUSTRY_NAME, GICS_INDUSTRY, GICS_SUB_INDUSTRY_NAME,
  GICS_SUB_INDUSTRY, PX_LAST, CRNCY, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS.
- **`market`:** the live scripted reference pull of that plan through `integrations/bloomberg/mcp/blp_client.py`. It is wired
  into daily mode after the dividends pull, so the enabled vehicle leg runs it with no vehicle edit.
- **`import-market`:** reads a Positioning `characteristics.parquet` as QA-class input, with provenance
  `import:bbg/<D>/characteristics.parquet`.

G4 columns:
- `security_id` (the key grammar of `security_bloomberg`) and `security_bloomberg`, `date`;
- `px_close`, `total_return_index`, `currency`;
- `gics_sector`, `gics_industry_group`, `gics_industry_group_code`, `gics_industry`, `gics_industry_code`, `gics_sub_industry`,
  `gics_sub_industry_code`;
- `source`, `as_of`, plus the C-GOLD-MODEL columns, with `claim = MEASURED`.

A field the response lacks is NULL, never guessed.

### `RIV-g-6` -- `canonical_shape` joins G4: GICS, and sub_asset_class IS the GICS sector for equities (C-SHAPES v0.7)

- For each non-cash G1 row with a `security_id` present in the newest G4 dated on or before the report date:
  - `gics_sector`, `gics_industry_group` and their codes, and `gics_industry`/`gics_sub_industry` where G4 has them;
  - `gics_status = RESOLVED` and `gics_source` naming the G4 revision.
- For an equity row with `gics_status = RESOLVED`: `sub_asset_class = gics_sector`, with `sub_asset_class_status = RESOLVED`
  (the ratified vocabulary, `etf_positioning_gold.SUB_ASSET_CLASS_VOCAB`).
- A row outside G4 stays UNRESOLVED. A finer GICS level never stands in for a sub-asset class.

### `RIV-d-4` -- the live join of round 3 (WORLD)

Under a NEVER-2 ledger entry opened and committed first, and a never-widen pair signed by `1.0.0_SA_CTO~Z` and this seat
(written by the issuer at d-4's cut, after cells 1-5 are merged):
1. Update the five Lambdas' code in place (`safe-apply`; the plan is `source_code_hash` updates only).
2. Set the publisher's `identity_coverage` floor from RIV-i-1's measured fraction. That is a one-constant hookup.
3. The issuer-retain positive control: one live re-capture of a LANDED BASG report date through the deployed fetch-holdings
   Lambda in `backfill` mode for that one date. Then silver and G1 by marker.
4. G4 import from the newest Positioning `characteristics.parquet` (QA-class).
5. Replay G1, G2, G5/G6 for the window the home landings cover, then publish the page.
6. Read the page back. Record `d4_live.json`.
7. If the Terminal reads signed in, also run the live `market` pull and one scripted GQGU holdings request (row Z-S6's
   measurement).

The next trading day's 08:03 leg and the 09:00 sweep are the acceptance, read at the close. They are never waited on.

## 4. PLACEMENT AXIS

- Package code: `data/etfs/scripts/rivalfunds/`.
- New modules: `home_producer.py`, `identity.py`. G4 lives inside `enrichment_bloomberg.py`.
- Terraform: only RIV-d-4's in-place code update.

## 5. DEPENDENCY EDGES AND CHAINS (cut by write set)

```
~1  RIV-hp-1 --> ~1 RIV-i-1 --> ~1 RIV-g-6 --+
~3  RIV-s-4 --------------------^            +--> ~4 RIV-d-4 (join, WORLD)
~2  RIV-r-3 ---------------------------------+
```

**Write sets** (each `<paths>` is disjoint from every concurrent order's):

| cell | writes |
|---|---|
| r-3 | `silver_issuer.py`, `sweep.py`, `gold_trade_schedule.py`, `publish_page.py` |
| hp-1, i-1, g-6 (serial on `~1`) | `gold_canonical_shape.py`; hp-1 also `home_producer.py`, `gold_holdings_coverage.py`; i-1 also `identity.py` |
| s-4 | `enrichment_bloomberg.py` |
| d-4 | infra, the source map, the ledger, the one floor constant in `publish_page.py` (after r-3 is merged) |

- **Edges:** g-6 consumes s-4's G4 and i-1's keys. d-4 consumes all five.
- **Wave 1 spawns 3 slots:** `~1` hp-1, `~2` r-3, `~3` s-4.
  - `~1` continues with i-1, then g-6. Each is handed after its predecessor is MERGED, and the issuer syncs CLOUD into `~1`
    first.
  - d-4 takes `~4` after every other cell is merged and the pair is signed.

## 6. BATTERY DISPOSITION

- **comp-schedule** (RUN at this cut, `--drift`): 2 armed gates fabric-wide, none naming `rivalfunds/`, `bloomberg/etfs/` or
  this round's files. The moratorium binds (no notifier).
- **comp-iam:** no IAM change in a build cell.
  - The build-silver role's lack of DeleteObject is the REASON for r-3 item 1, and is not widened.
  - G4 is written by the terminal machine's identity (as G3 is). RIV-d-4 measures that writer on `gold/security_market/`
    with the IAM simulator before the first landing.
- **comp-adversary:** DECLARED on RIV-i-1. The identity join is this round's highest-consequence inference, because every
  trade matches by resolved identity. Its check plants an ambiguous second candidate (the refusal arm). The tolerance and the
  denominators are measured at the cut.

## 7. RULE 24 FOUR-POSTULATE RECORD (new or amended enums this round)

- **`resolution_method` gains `bloomberg-form`, `issuer-bloomberg-join` and `issuer-bloomberg-join:ambiguous`.**
  - (i) MECE over a non-cash row's resolution path: crosswalk hit / own Bloomberg form / measured issuer join / ambiguous /
    miss. The existing `crosswalk:*`, `not-applicable-cash`, `no-identifier` and `crosswalk:miss` keep their meaning.
  - (ii) Per row. (iii) One intent: which rule produced the key.
  - (iv) A later pool registration moves a row from `bloomberg-form` to `crosswalk:*`. It never moves an ambiguous row to
    resolved.
- **`report_date_freshness` allowance by source** {issuer 0, bloomberg 1, home_producer 1} trading days.
  - (i) Total over G1's `source_used` enum. (ii) Per fund-day. (iii) One intent.
  - (iv) A source change moves the allowance. It never moves the lag measurement.

## 8. GATES, WRITE SETS AND THE CLOSE RUN

- **Build orders carry at most three mechanical criteria.** The package suite, py_compile and ruff run at the drain.
- **Every check is a file under `deliverables/2.0.0_SA_COO~RV/round3/checks/`, dry-run at base 78167bb8fc.** All 13 FAIL there,
  as build or live checks must.
- **The close run** (the issuer's, after d-4):
  - the served page shows IDVZ and PFOE with data beside their rivals;
  - BASG's issuer rows are resolved at or above the floor;
  - G1 carries GICS where G4 has it, and every equity `sub_asset_class` equals its sector;
  - the live re-capture control reads both objects and the new revision.

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

- It does not claim the Terminal is signed in, nor any live G4 value beyond the QA import.
- It does not claim GQGU coverage (rows Z-S5/Z-S6).
- It does not claim that the identity join's 2% tolerance holds for every fund and day. The check measures BASG on one real day
  and plants one ambiguity; RIV-i-1's deliverable prints the fraction per fund.
- It does not claim any FWD-6, -7, -10 or -11 value.
