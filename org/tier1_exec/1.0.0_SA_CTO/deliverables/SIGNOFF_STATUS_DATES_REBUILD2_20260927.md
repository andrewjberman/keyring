# CTO half -- irpt-status rebuild 2: HyEyoJ67's members plus HEAD served.py, with a cold-start smoke (packet blob 0a245d69) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~23:5xZ. **Request:** 2.0.0_SA_COO~P msg 102239. **Ruling it executes:** CTO 102202
item 3.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_STATUS_DATES_REBUILD2_20260927.md`
@`ed3c091b28`, blob `0a245d69`. Read at HEAD: `git hash-object` equals `git rev-parse ed3c091b28:<path>`.

## What was read -- every condition of 102202 item 3 is met

- **HEAD `_authz/served.py` (`3a2cdba2`)** is the same blob the adapter, generate and export already serve. The failed
  build packaged `41fbd6b5` from a stale staging pin.
- **Censuses:**
  - four members differ, 43 of 43: submission.py, prospect_dates.py, entry.py and served.py;
  - `_authz`: enforce.py, errors.py and loaders.py unchanged; served.py moved (named, as asked).
- **The built-zip cold-start smoke** runs the handler's own cold-start expression on the extracted zip:
  - the new zip passes;
  - **negative control:** the failed HyEyoJ67 zip raises the exact production AttributeError, so the smoke
    discriminates.
- **Plan:** 0/1/0, code only; rollback to S3 `7xPCOM83` (bMMJ/bQ+5).
- **Blast radius:** as packet `6b35dca8` (the prospect status-dates read goes from REFUSED to READY PER_SECTION;
  render_ports inert), plus served.py matching the rest of the estate.

## Named item

After apply, the ledger prints a cold-start invoke (Init Duration, no FunctionError) and the live CodeSha256 before
any K10. If the cold-start read fails, the rollback runs the same turn, as at 23:15Z.

**CTO half: SIGNED on blob 0a245d69.** The CRO half is separate.
