# Never-widen half, MDPF_SECCLASS -- Cottonwood's classify_position reads the canonical NAME:: row when the cash flag, the ticker row and the CUSIP: row all miss (FWD-16, cell SC-e-84, row MDPF_SECCLASS-D1-W66-S2, CTO ruling R1)

**Author:** `0.9.0_WK_MDPF_SECCLASS~74` for `2.0.0_SA_COO~M1`, 2026-10-09. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed or written to any bucket or table. Spec: PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`
FWD-16; measure `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/COT_NAME_SHARE_20261009.json`; order `MDPF_SECCLASS.TO-SC-e84.cot-name-key-port`.

## What is wrong

Black Diamond's classifier reads `NAME::<normalized name>` when a position's identity chain cannot place it. Cottonwood's `classify_position(ticker, cusip, cash_equivalent)` ran the cash flag,
the ticker row and the `CUSIP:` row, then returned `('unclassified', 'none')`. Round 16 measured (partition `s3://opal-data-cot/gold/canonical/holdings/2026-10-07.parquet`, 21,024 positions,
$553,031,383.86): 1,311 unclassified positions ($84,275,714.93); a `NAME::` row places 1,060 of them, $17,769,409.83 (3.21 pct of COT market value).

## The fix (staged, LOCAL, not deployed)

- `data/cot/scripts/gold/lib/etf_classifier.py` `classify_position` gains `asset_name=None`. Only when the cash flag, the ticker row and the `CUSIP:` row ALL miss, and the name is non-blank
  (None, NaN, empty, whitespace are blank), it reads `'NAME::' + normalize_name(name)` and returns `(asset_class, 'table name')` when the row carries an `asset_class`. `normalize_name`
  is the existing byte-identical port of BD's (uppercase, non-alphanumeric-except-hyphen to space, collapse whitespace, 80 chars); no cross-firm import. Every other answer is unchanged.
- `C_06.client_mix_timeseries.py`: `classify_holding` and `classify_series` (a `name` key column joins the distinct-tuple memo) pass the position's name; `reclass_retired_holdings` passes `h.get('asset_name')`.
- `D_03.composition_artifacts.py`: `classify_series` passes the name from the parallel `name_series` it already receives.
- Tests: `data/cot/scripts/gold/tests/test_cot_position_rule.py` (6 pass: the 3 existing, plus the name-placed arm, the ticker/CUSIP/cash control that keeps its answer under a conflicting `NAME::` row, and the no-row / blank-name control).

## The act (by the issuer, after both halves sign)

1. Deploy EXACTLY three files to `s3://opal-data-cot/code/gold/`, with `.tools/safe-deploy.sh` naming the three paths (the deploy core ships only named files; no `_shared` artifact rides it):
   `data/cot/scripts/gold/lib/etf_classifier.py` -> `code/gold/lib/etf_classifier.py`;
   `data/cot/scripts/gold/C_06.client_mix_timeseries.py` -> `code/gold/C_06.client_mix_timeseries.py`;
   `data/cot/scripts/gold/D_03.composition_artifacts.py` -> `code/gold/D_03.composition_artifacts.py`.
   Under a change-management ledger, before a COT gold fire. The three ship together: C_06 or D_03 deployed without the lib would pass `asset_name=` to a lib that rejects it.
2. The next COT gold fire runs C_06 and D_03 on the new lib; both classify the name-placeable positions through the name key.
3. Read back (leg G): the COT unclassified share in the served mix, beside the candidate diff below.

## Blast radius

**Objects the act writes:** three code objects. No table, no data key. **Objects the next fire writes:** the set the nightly COT fire already writes from C_06 (`gold/client_timeseries/...`
and `gold/entities/clients/{rid}.json`) and D_03 (composition artifacts); the change is CONTENT only. **Not touched:** `etf-classifications` (read-only), the BD twin, any position placed by
the cash flag, a ticker row or a `CUSIP:` row (AC1: 0 overridden), any position with no name or a name with no `NAME::` row (stays `('unclassified', 'none')`).
**Writers of the served COT class counted: N = 2** (C_06 and D_03), each calls `classify_position`. `classify` and `get_sub_asset_class` are unchanged; this worker did not enumerate other callers of `classify_position` beyond the three call sites the order names.

**Local candidate diff** (the worker ran the staged `classify_position` locally over the SC-e-82 partition, live read-only `etf-classifications` reads, no write; AC1 reads
`COT-PORT ok=True positions=21024 placed=1060 placed_mv=17769409.83 floor=1060 overridden=0 wrong_rule=0`):

| class | before | after | change |
|---|---|---|---|
| alternatives | $286,108.23 | $10,521,389.36 | +$10,235,281.12 |
| cash | $19,616,280.14 | $19,783,914.10 | +$167,633.96 |
| commodities | $20,551,538.37 | $20,592,847.47 | +$41,309.10 |
| equity | $225,696,827.19 | $232,627,110.84 | +$6,930,283.65 |
| fixed_income | $196,707,747.34 | $197,102,649.33 | +$394,901.99 |
| structured | $5,897,167.65 | $5,897,167.65 | $0.00 |
| unclassified | $84,275,714.93 | $66,506,305.10 | -$17,769,409.83 |

Positions moved out of unclassified, by new class: alternatives 46 ($10,235,281.12); equity 87 ($6,930,283.65); fixed_income 44 ($394,901.99); cash 879 ($167,633.96); commodities 4 ($41,309.10);
total 1,060 positions, $17,769,409.83. Dollars are the 2026-10-07 partition (total $553,031,383.86); a later partition moves the dollars, not the rule. For the signers: 879 of the 1,060 positions
place as `cash` through a `NAME::` row (small dollars), and $10.2M places as `alternatives`; the rows are the canonical table's, not this change's, so a wrong row serves its class here as it does in BD
(the SC-e-83 TWCUX precedent). This worker did not audit the 1,060 rows' contents.

## Rollback per key

The three code objects are versioned. Read-only `head-object`, 2026-10-09:

| key under `s3://opal-data-cot/` | VersionId | ETag | LastModified | size | role |
|---|---|---|---|---|---|
| `code/gold/lib/etf_classifier.py` | `MYI0nB3zRKMU17aCIQiM6fqYv8U3F.ia` | `2fef39d1373a20f40e2a0fb4c0cae0fa` | 2026-10-02T17:44:24Z | 7840 | CURRENT served: rollback target |
| `code/gold/C_06.client_mix_timeseries.py` | `55IsnYrr1xiWSvXliMNSM4mQ3bDXGTQ7` | `ea7e6700509611a1866701f4f8e0984e` | 2026-10-09T02:32:34Z | 39751 | CURRENT served: rollback target |
| `code/gold/D_03.composition_artifacts.py` | `vHHfV5NdKUY1t4Z8P1mv3vdtnacLHGrJ` | `6f48eaf3b54c63519c379d26793cc5e0` | 2026-10-07T04:16:46Z | 40329 | CURRENT served: rollback target |

Code rollback: copy each VersionId back over its key (`s3api get-object --version-id`, then deploy it); all three together, since the new C_06 / D_03 need the new lib and the old ones need the old.
It does not restore content a fire already rewrote. Data rollback per key: the issuer records, before the fire, the VersionId of each served COT mix / entity / composition key the fire rewrites
(not enumerated by this worker); any is restored to its pre-fire version.

## COO half -- SIGNED, with conditions

`2.0.0_SA_COO~M1`, 2026-10-09 ~11:5xZ, after the round-17 drain (@6ac1a94afe). The issuer re-ran the three criteria on the worker's tree:
- AC1: `COT-PORT ok=True positions=21024 placed=1060 placed_mv=17769409.83 floor=1060 overridden=0 wrong_rule=0`;
- AC2: `PYTEST-OK 6 passed`;
- AC3: `HALF-READY`.

The whole COT gold test directory reads 27 passed and 1 failed. The failure is the pre-existing retired-rule test, row D1-S24,
which this cell does not touch.

**Writers of the served COT class: N = 2.** C_06 and D_03, through `classify_position`. Both branches of the new hop were read in the
lib and the tests:
- a live `NAME::` row serves its class with rule `table name`;
- a blank name, or no row, stays `('unclassified', 'none')`;
- a cash-flag, ticker or `CUSIP:` placement is never overridden (the control arms, and AC1 `overridden=0`).

**The C_06 rollback target is e67's shipped bytes** (ea7e6700, VersionId `55IsnYrr...`). e67's leg G closed clean at the 2026-10-09
COT run, so a rollback of this act keeps e67's retired-class fix.

**Conditions:**
1. **Named files only.** The deploy names exactly the lib, C_06 and D_03, which ship together. The issuer prints the shipped member list,
   and any fourth member is a STOP.
2. **Data rollback is enumerated before the fire.** Record the VersionIds of `platinum/firm/mix_summary.json`,
   `gold/views/mix_daily_summary.json` and every `gold/entities/clients/{rid}.json` the fire rewrites, in the ledger, before the next COT
   fire.
3. **Leg G after the next COT fire:**
   - unclassified falls by the candidate diff's amount, give or take that day's market moves, with the moved positions carrying rule
     `table name`;
   - a census of every class outside the six (plus `unclassified`) in the served mix is printed, and anything new is a STOP;
   - e67's 0-`multi_asset` scan (`R17_CHECKS/e67_cot_post_fire_read.py`) still reads 0.
4. **Not audited here, and stated for the CTO:** the content of the 1,060 `NAME::` rows was not audited. 879 positions ($167,634) land on
   cash and $10.2M on alternatives, and both follow those rows' existing classes. The rows are the same canonical rows BD's name path
   already serves.

## CTO half -- UNSIGNED
