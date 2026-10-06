# Never-widen half, MDPF_SECCLASS row S27 -- one `SCGB1` ticker row (CTO rulings batch 266 (a))

**Author:** `2.0.0_SA_COO~M`, 2026-10-05 ~20:2xZ. **CTO half:** SIGNED in batch 266 (RULINGS.md, @cc5b1f3b5f), terms read.

## The act

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/write_scgb1_row.py --write`: one conditional put
(`attribute_not_exists(ticker)`) of key `SCGB1`, `multi_asset` / `Fixed Mix`, name `BALANCED FUND`, `classified_by scheduled`,
`updated_by mdpf-secclass-cusip-rows`, mirroring `CUSIP:808516306`.

## Reads owed by batch 266, both done before the write (2026-10-05 ~20:1xZ-20:2xZ)

1. `get-item` (consistent) on `SCGB1`: NO ITEM. Same call shape on `CUSIP:808516306`: ITEM, `multi_asset`.
2. Served nodes with `display.symbol` SCGB1 or `security_id` 808516306, latest revision at each firm, every part read:
   - cottonwood 2026-10-02: 0 nodes (27 of 27 parts).
   - inflection 2026-10-02: 0 nodes (51 of 51 parts).
   - 49financial 2026-10-02 (revision f8bf8dcb53cd): 9 nodes, $175,356.90, all `unclassified`, all with both the symbol and the
     CUSIP (188 of 188 parts, eight shards: 4, 0, 1, 3, 0, 0, 0, 1).

## COO half -- SIGNED

- **Blast radius:** one new key in `etf-classifications`; the readers of ticker `SCGB1` move from a miss to the row. Known
  effect: those 9 nodes at 49financial move `unclassified` to `multi_asset` at the next 49financial holdings build; no other
  firm holds the symbol.
- **Writers of the key:** 1. **Rollback:** delete the item (it did not exist before), on Andrew's word.
- **Both branches:** a build runs and the nodes move, or none runs before the read and they stay `unclassified`. Leg V reads
  after a build.
