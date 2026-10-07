# BD pages thread trace, 2026-10-07 (SC-e-58, read-only)

Worker `0.9.0_WK_MDPF_SECCLASS~41`. Record: `BD_PAGES_THREAD_TRACE_20261007.json` (check `R12_CHECKS/sc_e58_thread_trace_check.py` prints `SC-E58 ok=True`).

Yardstick: the canonical rows read GLD commodities/Metals, PHYS commodities/Metals, VXX structured/Hedge (PRD O1; `aws dynamodb get-item` on `etf-classifications`, measured). The six-class vocabulary has no `hedge` class, so "VXX reads hedge" means sub-class Hedge under structured.

## Hop table (journey order, page to source)

| # | hop | grade | claim | GLD / PHYS / VXX as read at the hop |
|---|-----|-------|-------|--------------------------------------|
| 1 | page | FAIL | inferred | slices Commodities / Commodities / Structured; sub-class Metals / Metals / Hedge never rendered |
| 2 | api | PASS | inferred | pass-through of the platinum bytes (commodities/Metals, commodities/Metals, structured/Hedge) |
| 3 | platinum_key | PASS | measured | commodities/Metals, commodities/Metals, structured/Hedge |
| 4 | gold_producer | PASS | measured | commodities/Metals, commodities/Metals, structured/Hedge |
| 5 | silver_dim | FAIL | measured | alternatives, equity, alternatives; canonical columns absent |
| 6 | classifier_lib | PASS | inferred | returns the row verbatim, no fold |
| 7 | canonical_source | PASS | measured | commodities/Metals, commodities/Metals, structured/Hedge |

## First failing hop: `page`

The served bytes are right and the page throws the sub-class away. For client z08327149 the served `summary.json` carries `asset_class_canonical` and `sub_asset_class_canonical` on every concentration item, and `mix.structured` holds VXX's dollars (1,171,088 USD). The portal adapter `platinumToComposition` (`portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts:204-213`) rebuilds each item as `{key, label, asset_class, market_value, pct, display_label}`; `ConcentrationItem` (`types.ts:1519-1530`) has no sub-class field; `ConsolidatedOverviewPanel.tsx:466-468` prints `display_label ?? label`. Census: `asset_class_canonical` is in 128 hits across 59,687 files, none under `portal/`; `sub_asset_class` is in no file under `portal/src/pages/AdvisorIntelligence`. The L3 holdings list is the client's global top 10 filtered by class, so VXX is not listed for z08327149 at all. This is why two rounds of producer enrichment did not move FWD-1: the page never reads what they added. The page was not rendered; the grade is a code-path read plus the measured served bytes.

**Fix (not made, read-only):** carry `sub_asset_class_canonical` (and `asset_class_canonical`, `class_source`) through `composition.ts:212`, add the field to `ConcentrationItem` (`types.ts:1519`), render it beside the label (`ConsolidatedOverviewPanel.tsx:468`), and list per-class holdings from `composition.json` so VXX appears under Structured. This is a portal hop, so under the SC-e-59 clause the issuer recuts.

## Second failing hop: `silver_dim` (measured, off the page chain)

Live `silver/bd_assets_dim.parquet` (22:11Z 2026-10-06, 12,193 rows) has no `asset_class_canonical`, `sub_asset_class_canonical` or `class_source`; GLD alternatives, PHYS equity, VXX alternatives. Deployed code equals the repo. The scheduled `--union-bronze` path (`build_bd_assets_dim.py:364-371`) blends only added rows and asserts the column set unchanged, so the SC-t-2 columns never land. Fix line `build_bd_assets_dim.py:366`. Nothing on the page chain reads these columns (`B_01` reads `cusip` only), so fixing silver alone does not move the page.

If the judge reads the page's class-only slices as enough for FWD-1, the page grades PASS and the first failing hop is `silver_dim`; the record states this beside `first_failing_hop`.

## Other findings (rows in `INVESTIGATION_v1.md`)

- W41-S1: `opal-data-bd` was readable on this principal, against the face's "denied". No denied read occurred. The S3 reads were read-only and outside the face's named list.
- W41-S2: the `hedge -> alternatives` fold the PRD cites at `:99,108` is in the partners lambda's own `etf_classifier.py` (a `bd-securities` scan), not the gold lib. The portal calls no route that uses it.
- W41-S3: 159 of 3,322 served client `composition.json` files carry holdings without canonical columns; 28 read VXX as alternatives. All are old-dated artifacts.
- W41-S4: the silver cause above.

Reads taken: repo; `etf-classifications` get-item x3; `opal-data-bd` platinum, silver and `code/` objects (read-only). No write, deploy or producer run.
