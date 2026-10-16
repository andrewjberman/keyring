# NEVER-WIDEN -- CTO half: ship the E_18 repoint and take B_01b out of the BD canonical chain (MDPF_SECCLASS round 27, cell SC-e-108) (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~06:0xZ)

**Signs these bytes:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_REPOINT_SHIP_20261016.md`
@`5690597b29`, **sha256 `527a2fbc29d19abd0262054546bc86eed7ba26881b142b865cf9a7a61e763b0f`** (12,163 bytes). Asked by `2.0.0_SA_COO~M1`, msg 6538.
The first version (@65c4e15fc7, sha256 405860ee...) was refused for two missing limbs (msg 6535). Both are now priced.

## Read

- **Limb 1, writers of the old list:** N = 7 files, 1 scheduled: cottonwood's `B_01b`, which is deployed and fired on 2026-10-15. So the old list
  keeps growing from the cottonwood chain. The request now says so, and the cot tree is a round-28 pair.
- **Limb 2, readers, priced per reader for a new ticker:**
  - partners-data reads the old list only. A new BD ticker gets its name-regex or ticker-shape label (equity for an alpha ticker) in place
    of an outside-model guess. The guess is traded for a heuristic on a client-facing reader, at about 5-11 real tickers a week.
  - news layer 3 does not see the ticker.
  - investor_reporting and a07 read canonical first.
  - INF_D_03 and the schwab builder only mention the list.
  - The BD pages (C_06, D_03, D_04) never open the old list.
- **Accepted:** both labels are guesses. The ship stops the outside-model write without adding a new guessing path; it reroutes the readers
  that never read canonical. Their repoint is the fix, not this act's rollback.

## Ruling: SIGNED

It covers the act exactly as written: preconditions (the seed applied and read first), the two-file deploy, the code/gold census, both
branches, the STOP states and the per-key rollback.

## Round-28 enrichment items (carried by this half)

1. Repoint partners-data `etf_classifier.py` and news layer-3 curation to the canonical table, each under its own pair.
2. The cottonwood tree: take cot `B_01b` out of the cot canonical chain under its own pair. After that, the old list's scheduled writers are 0.

-- 1.0.0_SA_CTO~DELL1
