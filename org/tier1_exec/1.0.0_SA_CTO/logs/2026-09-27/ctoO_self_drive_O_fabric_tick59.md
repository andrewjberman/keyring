# /self-drive ~O fabric -- ticks 58-59 (09:16Z-10:16Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a driver act (the MX-s-8 CTO half) and the hourly floor.

## MX-s-8: both never-widen halves SIGNED

- **CTO half @f3030ae5e7** (`RULING_MX-s-8_SILVER_GUARD_SIGNOFF_20260927.md`). Signed only after tracing every DEPLOY
  INPUT, not just the code diff (the lesson of MX-r-3's two catches):
  - `build-and-upload.sh` zips the function folder and does NOT re-vendor from `data/assets` (the manifest gate at
    `:396-481` checks declared blobs only);
  - this seat diffed each folder against its sha-verified DEPLOYED zip (`C:/tmp/mx-s8-rollback/`): exactly one
    packaged file differs, `mirror_conversion.py`, and there only by 5 lines x4 (the two hunks), with no older unshipped
    change riding along;
  - the layer is pandas 2.3.2, so Z-S3 is DELTA = 0;
  - Z-S25 only ADDS partitions where a unit used to raise on `''`; successful inputs are unchanged by the producer's
    own rule;
  - writers N = 2 classes (4 Lambda copies + the source converters), both on the same rule after the act.
- **CVO~O half @88eb2af940** (row NFRA_MCPINDEX-Z-C-S20). Nothing added: it confirms 5 lines per function and no unit
  raised in the 14-day log window. It counts 5 writers where this seat counts 2 classes; the members are the same.
- Relayed SIGNED to `2.0.0_SA_COO~O` for CVO~O. GO is the issuer's, under the CTO half's guards (plan 0/4/0 on code
  attributes; CodeSha256 moves on exactly the 4; detailed-exitcode 0 after; the import smoke; the ledger).

## Calls, verdicts

No new call. At Andrew: call 1 BLOCKING (the OPLGTW re-seat, also carrying W3-S22), call 2 CARRIED (D9 device), and the
switchover sitting. 0 self-drive verdicts.

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE. Open orders: MX-s-4, MX-s-6, MX-s-8 (MCPINDEX); OA-t-1, OA-t-3
(OPALAI).

state: ARMED

## Compiler Tools

A python zip-vs-folder sha256 diff over the 4 rollback zips; difflib on the deployed vs patched `mirror_conversion.py`.
