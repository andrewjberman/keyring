# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 16 (~23:4xZ 2026-09-21)

- **Arming record:** carrier `c9ccd9f4e3`.
- **Cron:** `46e545b7`.
- **State:** ARMED.
- **Projects:** 2, both `active` / EXECUTING.
- **Sequence:** no flags.
- **COO lanes:** 2 of 3 live.
- **Inbox:** 0 unread. Read and acked since tick 15: 99316, 99317, 99321, 99323, 99325.

## Driver acts since tick 15

- **Never-widen CTO half for IB-rti-1 (capture-tool publish): SIGNED @`93dda7a939`.**
  - Signed against packet blob `56ad3283`.
  - Before signing I fetched the live S3 bytes and hashed them. They equal the pre-repair blobs.
  - Versioning is Enabled. The sync has no `--delete`.
  - The typed-and-cited origin is accepted; its drift risk goes to round 10 as a row.
  - `2.0.0_SA_COO~B` published and read the objects back. The ledger entry is closed. The host was never touched.
- **IRPT_FNTEND round-10 L10 analysis: @`3020f2a580`** (msg 99318/99319).
  - No PRD addendum.
  - FWD-12 is NOT_REALIZED.
  - Round 11 has 7 cells, A-G.
  - A 4-part visual criterion rule: wire match, named content, wrong-state control, and ground measured on the route container.
  - CTO-owned rows W11-S4 and W12-S2 are ruled in scope, fixed at the shared component.
  - C-S129: no invented backend route. `2.0.0_SA_COO~B` informed (99320).
- **Round-11 shape accepted** (99323 -> reply).
  - Nine cells, FE-s-65..73, with the instrument cell FE-s-65 first.
  - Condition on D2: fix `CategoryViewTree`'s default if Model Portfolios also violates C3.
  - `surfaceBase` font-medium across 13 importers is PARKED out of IRPT scope. Owner is this seat; it un-parks when the IRPT-only priority lifts.
- **IB-rti-6 PARKED for the round-9 close: @`4a773b6ae3`** (msg 99327/99328).
  - Wave 1 is terminal: 1 open of 91, and that one is rti-6, staged.
  - Un-park owner is Andrew, for the human step.
  - Of the 4 un-park conditions, condition 1 is already MET.
  - `2.0.0_SA_COO~B`'s held session-capture ask to Andrew is UNBLOCKED.
- **Ferry 99321** (lib/ has no `__init__.py`; pytest loads each module twice): QUEUED behind IRPT. The lean is toward an explicit pytest import mode, after a census.

## State

- **IRPT_BCKEND:**
  - Round 9 is at the L8 compile, to `3.0.0_SA_CVO~B`.
  - Next from this seat: the round-9 analysis on CVO~B's slug.
- **IRPT_FNTEND:**
  - Round 11 is being cut by `2.0.0_SA_COO~F`.
  - Next from this seat: the round-11 analysis on CVO~F's slug.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Open calls in scope

0.

## Compiler Tools

`.tools/aws` (s3 cp, get-bucket-versioning), `git hash-object`, `sequence-check.py`, `git log`.
