# Leg V, 49financial -- the SCGB1 row read in a local --dry-run build (CTO rulings batch 266 / msg 105360)

**Author:** `2.0.0_SA_COO~M`, 2026-10-05 ~20:2xZ. Nothing served was written.

- **Command:** `python data/assets/scripts/gold/investor_reporting/holdings_snapshot.py --firms 49financial --dry-run --local-out .scratch/legv_dry49`, rc 0.
- **Build:** business_date 2026-10-02, 153,918 nodes, 7,587 accounts, reconcile True (1,804,791,631.40 both sides), schema valid.
- **Result, read from the local output:** the SECURITY nodes with `display.symbol` SCGB1 or `security_id` 808516306 number **9 of 9**,
  all `multi_asset`, `asset_class_basis` TABLE, `sub_asset_class` Fixed Mix, $175,356.90 (the same 9 nodes and amount as row S27).
- **Control:** the served build read these nine as `unclassified`, basis NONE (leg V merge, @b218075200).
- **Whole-build class counts (SECURITY nodes):** equity 79,246; fixed_income 36,051; structured 6,508; unclassified 165;
  multi_asset 34; alternatives 29; commodities 23.
- **Leg V stays open** until the served 2026-10-06 14:15Z fire is read (the acceptance, per batch 266 and msg 105360).
