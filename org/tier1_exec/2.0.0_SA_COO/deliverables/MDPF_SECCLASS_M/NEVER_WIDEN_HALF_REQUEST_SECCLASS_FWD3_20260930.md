# Never-widen half, MDPF_SECCLASS.TO-SC-e6 (cell SC-e-6) -- the first FWD-3 correction: seeding VNQI to fix its wrong scheduled row

**Author:** 0.9.0_WK_MDPF_SECCLASS~7, 2026-09-30. **For:** the issuer (2.0.0_SA_COO~M) to sign and send, per the
"never widen without a named blast radius + rollback per key" discipline (CLAUDE.md HARD STOPS section 5) and the
precedent format used for `NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_FIELDS_20260929.md`.

**Status of the act described here: NOT YET RUN.** This task order is a LOCAL build + record: the seed-source edit
(`infra/aws/lambda/v2_portal/_shared/etf_classification.py`, adding `VNQI`) was made and the live table was read
read-only to confirm the current wrong row; nothing was written to `etf-classifications`. This half covers the FIRST
real run of `seed-etf-classifications.py` that lands this correction (any other net-new module tickers added between
now and that run ride the same run; this half's blast-radius claims are scoped to the one ticker this cell names,
VNQI, and the seed run's general mechanics already signed by the SEED_FIELDS half).

## The act

One write, against the live DynamoDB table `etf-classifications` (2,309 rows at this build):

`python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py --region us-east-1` -- merges the module
(`etf_classification.py`, now carrying `VNQI`) into the table. `merge_item` sets `classified_by = "seed"`
unconditionally (PRD C-WRITER: seed always wins over scheduled), so this run REPLACES the live VNQI row:

- Before (live read, this build): `{"ticker": "VNQI", "asset_class": "equity", "sub_asset_class": "International",
  "classified_by": "scheduled", "last_updated": "2026-09-30T02:23:47.350920+00:00"}`.
- After (candidate write, computed from the module, not yet applied): `{"ticker": "VNQI", "asset_class":
  "alternatives", "sub_asset_class": "International Real Estate", "instrument_kind": "fund", "management_style":
  "passive", "sector": "Real Estate", "name": "Vanguard Global ex-U.S. Real Estate ETF", "classified_by": "seed",
  "updated_by": "seed-script"}`.

Evidence: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_FWD3_PLAN_20260930.json` -- the live item read,
the VNQ precedent row (`alternatives`/`Real Estate`, `classified_by=seed`) that shows the table's own established
convention for this fund family, and the census rows (bd, 49financial) confirming the wrong scheduled value.

**Andrew's word governs this class of write:** 2026-09-29 ~21:4xZ, "yes, bd-securities values can seed new rows. They
just don't overwrite existing rows" -- read together with PRD C-WRITER's `seed` always winning over `scheduled` (the
row VNQI carries today), this act is the SEED path overwriting a `scheduled` row, which is the one case the ruling and
the contract both name as the intended path (a `scheduled` row is provisional pending the seed source's own correction,
never the canonical table's last word). It does not touch a `seed`-classified row.

## Blast radius

**Readers of `etf-classifications`, the one ticker this act changes (VNQI: `equity`/`International` ->
`alternatives`/`International Real Estate`):**

1. **`a07_dim_asset_classification.py` (49F data, PRD surface S11).** `classify()` (`:220-255`) reads
   `item.get('asset_class', '')` from a live scan-built `ticker_map`. A 49F position in VNQI, previously tagged
   `equity`, is tagged `alternatives` after the next 49F gold-layer run. No other 49F-held ticker's row changes.
2. **`yang-generate-positioning` / `yang-generate-holdings-attribution` (Positioning, PRD surface S13).**
   `ETFClassifier.get_asset_class()`/`get_sub_asset_class()` read the item's named keys directly. A client holding
   VNQI shows `alternatives`/`International Real Estate` in the attribution hierarchy after the next report run,
   instead of `equity`/`International`. No other ticker's value changes (this act's write set is VNQI alone).
3. **Portal `HoldingsBreakdownTable.tsx` (PRD surface S16).** `subAssetBg(holding.asset_class,
   holding.sub_asset_class)` (`:368`) renders the served fields; a VNQI row re-tints from its equity color to its
   alternatives color on the next page load/API refresh, for any client whose holdings the portal shows VNQI in.
4. **`find_by_asset_class` / `find_by_sub_asset_class` callers.** VNQI moves OUT of an `equity`/`International` query
   result and INTO an `alternatives`/`International Real Estate` one. This is the same class of effect the SEED_FIELDS
   half already signed for other net-new/corrected tickers (query-result membership, not a value a caller stored).

**Every listed class change: exactly one ticker, VNQI.** No other row's `asset_class`, `sub_asset_class`,
`instrument_kind`, `management_style`, `sector` or `name` changes: the seed source edit in this cell touches only the
five `VNQI` dict entries added (`ETF_CLASSIFICATIONS`, `ETF_MANAGEMENT_STYLE`, `ETF_SUB_ASSET_CLASS`,
`ETF_SECTOR_MAPPING`, `ETF_NAME_OVERRIDES`); the module's other 137 tickers are byte-unchanged (verified: `git diff`
on this cell's commit touches only the five new lines/blocks named in `R2_FWD3_PLAN_20260930.json`
`seed_source_edit`).

**What every OTHER live row gets:** nothing from this act specifically; this half covers the VNQI candidate write only.
A concurrent full seed run also carries whatever else is in the module at run time, which is the SEED_FIELDS half's
own scope, not re-opened here.

## Rollback per key

DynamoDB `etf-classifications` is NOT S3-versioned; rollback is per-attribute, per-ticker, using this build's own
PRE-READ (the live item captured above) as the "before" snapshot:

- **To undo VNQI's reclassification:** `UpdateItem` on `Key={"ticker": "VNQI"}` with `SET asset_class = :ac,
  sub_asset_class = :sac, classified_by = :cb` where `:ac = "equity"`, `:sac = "International"`, `:cb = "scheduled"`,
  and `REMOVE instrument_kind, management_style, sector, name` (attributes this act adds that the PRE-READ item did
  not carry) restores VNQI to its exact PRE-READ state.
- No other ticker needs a rollback entry: VNQI is the only row this act's write set touches.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-09-30 ~07:2xZ)

Signed on the blast radius above, against TO-SC-e6 drained @dbef8063b3. The issuer re-ran the criteria on CLOUD at
@bc13447e97: FWD3-PLAN VNQI on 3 surfaces, HALF-READY, proof VALID.

**Measured at signing (the producer's own rule, both branches read, not predicted):** `seed-etf-classifications.py
--dry-run` against the live table at 07:15Z: PRE-READ 2,309 rows; 138 module tickers; 137 already correct, 1 to write.
The only CONFLICT is VNQI asset_class (equity -> alternatives) and sub_asset_class (International -> International
Real Estate). VNQ management_style is PRESERVED (the module has none). Since release step 1 (@ad921b0c47) the module
changed in one commit only, bd7b65f1dc (VNQI).

**The act, exactly (the issuer runs it):**
- `seed-etf-classifications.py --region us-east-1 --accept-module-truth`. The flag's scope is every CONFLICT, and at
  signing that is VNQI alone. The run is refused unless a fresh `--dry-run` taken immediately before still lists VNQI
  as the ONLY conflict and 1 row to write; any other conflict stops the act for a new half.
- **Writers of VNQI's class: 3** (the seed path, the scheduled path and E_18, both of the latter conditional on
  absence). Three rules read: the seed path's merge writes the module value and sets classified_by = seed; the other
  two never write an existing row. After this act, no scheduled run can move VNQI back.
- **Both branches.** VNQI moves to alternatives / International Real Estate on S11, S13 and S16 at their next runs. No
  other row moves (137 are skipped as already correct).
- **Ledger.** Opened before the write with the PRE-READ of VNQI saved beside it; closed at the read-back of VNQI.
- **Rollback.** The per-attribute UpdateItem above, from the PRE-READ.

## CTO half -- see below


## CTO half -- SIGNED (1.0.0_SA_CTO, 2026-09-30 ~08:0xZ)

Signed on the blast radius above; I read the request and its COO half and re-ran nothing. Writers of VNQI's class counted: 3 (seed, scheduled, E_18); the seed path's replacement of a `scheduled` row is the case the contract and Andrew's 09-29 word both name as the intended path, and after it no scheduled run can move VNQI back.
Both branches covered: VNQI moves to alternatives / International Real Estate on S11, S13 and S16 at their next runs; the other 137 rows are skipped as already correct. Conditions (each a stop): (1) a fresh `--dry-run` immediately before the write still lists VNQI as the ONLY conflict and 1 row to write, printed with its denominator; any other conflict stops the act for a new half;
(2) the PRE-READ of VNQI is saved beside the ledger before the write; (3) the read-back of VNQI is printed against the candidate row and any difference is explained before the ledger closes; (4) the act is `--accept-module-truth` scoped to that one conflict only.
