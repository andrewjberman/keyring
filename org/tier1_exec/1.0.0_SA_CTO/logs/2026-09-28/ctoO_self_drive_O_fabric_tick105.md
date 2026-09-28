# /self-drive ~O fabric -- ticks 104-105 (1.0.0_SA_CTO~O, 2026-09-28 06:45Z-07:45Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **Z-S38** (`lib/` is lane BASE_EXEC): this seat COMMITTED `lib/silver_ids.py` (@88e4e69e69) after reading and
  exercising it. It has the same 8 ID columns and the same body as the inf original; account_id coerces to Int64 and
  asset_id is untouched. CVO~O declined as a non-acting seat.
  - DS~D landed the re-export, the bd builder and the tests (@9fb05bc6c1). Re-verified: 6/6 inf callers, s4.AC3 PASS.
- **Z-S37 CLOSED** by this seat, row Z-S40 @6343cfca2c.
- **MX-s-6 COMPLETE** (@8deec74988), gold untouched.
  - Dim: 12,141 rows; asset_id unique; 805/805 formerly-missing ids covered.
  - Disclosed deltas: 42 cusip, 342 name, 37 symbol, 35 ticker.
  - The rollback VersionId was recorded.
  - The cusip deltas reach served output only through MX-s-2, under its own sign-off.
- **Z-S42** (the asset-dim pull is unscheduled): RULED cut-now @bf94418eb8.
  - Re-point the EXISTING 22:10Z trigger / SSM document to the REST pull + rebuild. Port directly, no shadow.
  - Retire the portal and fees downloaders after a caller census. Terraform-only, with a NEVER-2 ledger.
  - Never-widen halves before the first scheduled fire.
  - COO~O issued MX-s-10 (@ed19b7b4e4).

**Cards at Andrew:**
- (1) URGENT: rotate the BD password.
- (2) The history-scrub scope.
- (3) The census as a commit gate.
- (4) The switchover sitting.

**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED
