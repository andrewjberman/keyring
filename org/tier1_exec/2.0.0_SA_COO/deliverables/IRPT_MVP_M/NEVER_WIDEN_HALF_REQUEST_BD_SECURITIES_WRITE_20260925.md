# Never-widen half requested -- the bd-securities write from Andrew's one classification run

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO`, 2026-09-25 ~15:5xZ. Asked by CTO msg 100951: "The write to bd-securities
comes to me as a never-widen half, naming the flipped securities and their readers, before it lands."
Recommendation: **sign batch A now; hold batch B** until the readers named below admit `other`.

## The act

- **Write:** a conditional `PutItem` per key into DynamoDB `bd-securities`, with `ConditionExpression
  attribute_not_exists(ticker)`, so no existing item is ever overwritten.
- **Item shape:** B_01b's own (`B_01b.classify_new_securities.py:330-340`): ticker (the PK), asset_class,
  sub_asset_class, confidence, needs_review, classified_by `gpt-5.4-mini`, rationale, asset_name_raw, last_updated.
  One more attribute, `classified_run = irpt-m-once-20260925`, lets the rollback select exactly these keys.
- **The keys:** a literal list in `BD_SECURITIES_WRITE_SET_20260925.json` (this directory), built from
  `CLASSIFY_ONCE_RESULTS_20260925.json` @9c769fba15. The act writes nothing outside that list.
  - **Batch A (`A_NOW`):** 207 keys; sha256 of the ordered key list 119852f326e06303...
  - **Batch B (`B_HELD_OTHER`):** 37 keys, every one classed `other`.
- **Excluded:** 41 of the run's 285 keys already exist in the table. B_01b writes net-new keys only (`:155`), so they
  are not written, and the run's answer does not replace the table's. 8 are `cash` in the table where the run said
  fixed_income; 2 are fixed_income where it said equity; 2 are equity where it said other.
- **Key form:** all 244 new keys are `NAME::` keys (0 are ticker-shaped). A reader reaches them only through the
  loader's name index (`etf_classifier.py:69-71`, asset_name_raw), by an exact normalised name match.

## Which values move (state coherence)

These are the loader's answers for the same ticker and name, read from the table as it is today and after the write
(`classify()`, `etf_classifier.py:81-129`). The effect was read from the producer's code, not predicted.

| Today -> after | Batch A | Batch B |
|---|---|---|
| fixed_income -> fixed_income (no change; Layer 3 name patterns already say so) | 112 | 0 |
| NONE -> equity | 66 | 0 |
| NONE -> fixed_income | 16 | 0 |
| NONE -> alternatives | 9 | 0 |
| NONE -> other | 0 | 37 |
| **fixed_income -> alternatives** | 2 | 0 |
| **fixed_income -> equity** | 2 | 0 |

The 4 real flips, all in batch A:
- `Ft Unit 9273 Int Rate Hedge Port Ser 135` becomes alternatives.
- `VORNADO REALTY 5.4% PFD PFD SER L` becomes alternatives. That is Andrew's rule: investment real estate is
  alternatives.
- `GLADSTONE CAP 6.25% PFD PFD SER A` and `MORGAN STANLE 4.25% PFD PFD SER O` become equity. A preferred-stock call;
  the CTO may strike these two from batch A.

What the write does NOT move:
- the 41 existing items;
- the `etf-classifications` table, and with it the whole Positioning family (`etf_positioning_publisher.py`,
  `positioning_chain.py`, `satelliteAdapter.ts`), which reads that table and not this one;
- INF composition (`INF_D_03`, `INF_D_07a`), which is Orion-native;
- Schwab composition (`build_gold_firm_composition.py`), which uses Schwab's own dim_asset.

## The readers (census of the 69 paths, Explore agent, 2026-09-25)

Writers of the property: ONE rule, the loader's `classify()`. Two copies are byte-identical,
`data/black_diamond/scripts/gold/lib/etf_classifier.py` and `data/cot/scripts/gold/lib/etf_classifier.py`. 0 of the
69 readers RAISE on a new value. The readers that can see these firms' securities:

| Reader | Batch A effect | Batch B (`other`) effect |
|---|---|---|
| `data/cot/scripts/gold/C_06.client_mix_timeseries.py:172-182, 473-474` (COT client mix, served) | Today NONE falls back to `equity` (:182). After the write, $21.18M moves equity -> alternatives and $0.41M equity -> fixed_income in the mix of the COT clients holding them (the Eiger and Saxum LPs and the rest). A correction, on the next scheduled run. | **HARM:** `MIX_ASSET_CLASSES` (:169) lacks `other`, so $48.51M drops out of the published mix; the fractions stop summing to 1 for those clients. Must not land before C_06 admits `other`. |
| `data/cot/scripts/gold/D_03.composition_artifacts.py:102-129` | passes through | Already labels `other` "Other", but also uses `other` as its own unknown sentinel, so the two meanings merge |
| `data/cot/scripts/gold/D_04.client_portal_summary.py:1340-1345, 2971` | passes through | Uses the literal `other` as its fallback for unclassified. A real `other` becomes indistinguishable from unknown; no visible change today |
| `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:230-239` (49F/INF/COT union dim) | passes through | passes `other` through into the dim |
| Holdings (`holdings_snapshot.classify_security`) | classes 207 securities from NONE on the next publication | **Refuses** a class outside ASSET_CLASS_VALUES (no `other` today); the Holdings enum and the v1 contract must admit it first |
| IR portal `contracts/adapt.ts:1001` (DEV 8242412d) | n/a | an unknown class reads `unclassified` (graceful); ~D maps and colours `other` |
| `B_01b` (BD/COT) and INF `classify_assets.py:67` VALID_ASSET_CLASSES | not re-read (new keys only) | lack `other`; write-side filters only |

## The half's two branches

- **Batch A lands:** the 207 keys exist with `classified_run` set. C_06 moves $21.6M of COT mix out of equity at its
  next run, and Holdings classes the securities at its next publication. No other reader's output changes.
- **A write refuses** (a condition failure on a key that appeared since the census): that key is skipped and counted.
  The act never overwrites. Before writing, the census re-runs against a fresh scan, and the act refuses if the list's
  sha differs.

## Rollback per key

`DeleteItem` on each written key, with the condition `classified_run = irpt-m-once-20260925`, from the same literal
list. That is a table delete, so it takes a human confirmation per the autonomy rules. No key existed before, so a
delete restores the prior state exactly: the loader then reads NONE and falls back as today.

## Order for batch B (`other`)

1. C_06 admits `other` in MIX_ASSET_CLASSES (COT DS lane).
2. D_03 and D_04 separate their unknown sentinel from a real `other` (COT DS lane).
3. Holdings ASSET_CLASS_VALUES plus the v1 HoldingsSnapshot contract admit `other` (~M, and the contract's owner).
4. ~D maps and colours `other` on the IR portal.

Then batch B comes back to the CTO as its own half.

## The ask

Sign batch A (207 keys; strike the two preferreds if the CTO rules them fixed_income), or refuse it, naming what is
missing.
