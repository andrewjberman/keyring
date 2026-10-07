# ANDREW-DIRECT 2026-10-07 ~05:3xZ -- `3.0.0_SA_CVO~Z` handles AMGT; ETFS_RIVALS is `3.0.0_SA_CVO~RV`'s; NFRA goes to `3.0.0_SA_CVO~O`

Channel: typed by Andrew at the `3.0.0_SA_CVO~Z` terminal (Claude Code session), ~05:30Z (1:30 AM ET). He interrupted this seat's
read of the ETFS_RIVALS sign-off state.

## VERBATIM

> you do not deal with ETFS_RIVALS further, that is why we have CVO~RV. Your job is to handle the rest of the AMGT-related fabric, as NFRA projects go to CVO~O for validation.

## As written (not adjudicated here)

- `3.0.0_SA_CVO~Z` does no further ETFS_RIVALS work. `3.0.0_SA_CVO~RV` is the validator for it.
- `3.0.0_SA_CVO~Z`'s work is the AMGT-related fabric.
- NFRA projects go to `3.0.0_SA_CVO~O` for validation.

## State this seat leaves on ETFS_RIVALS (measured before the word; nothing further is done)

| artifact | state |
|---|---|
| v0.18 ratified-text sign-off @`fbabb6319c` (review @`fe586ea2e2`), bound to the bytes at `e0e0c3cf78` | committed. The PRD has moved twice since (`1fe8dd0132`, `d18b424454`), so that sign-off is stale |
| review of the corrected bytes at `1fe8dd0132`, `L4R_REVIEW_ETFS_RIVALS_v0.18_CORRECTED_RATIFIED_TEXT_20261007_Z.md` @`2c11259602` | committed as a record. **Its stamp did NOT land:** `prd-signoff.py sign` returned rc 3 and the sign-off file is unchanged |
| the bytes at `d18b424454` (the calendar-days unit) | not reviewed and not signed by this seat |

So the ratified-text half of ETFS_RIVALS v0.18 at its current bytes is unsigned. The sign-off record and the L4 notifier still
name `3.0.0_SA_CVO~Z` as the seat that owes it. Re-routing that half to `3.0.0_SA_CVO~RV` is `1.0.0_SA_CTO~Z`'s act.

## What does not follow from this word

- It does not withdraw the two ETFS_RIVALS review records this seat already committed. They stand as records.
- This seat holds one non-AMGT project in its handoff, NFRA_SPRINTWIN (round 1 graded @`fafbb9b482`). By this word NFRA validation
  is `3.0.0_SA_CVO~O`'s. This seat takes no further NFRA_SPRINTWIN packet and surfaces that to `1.0.0_SA_CTO~Z`.

-- 3.0.0_SA_CVO~Z
