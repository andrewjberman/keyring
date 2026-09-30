# ANDREW-DIRECT 2026-09-30 ~20:2xZ -- ETFS_RIVALS: leave the existing Positioning pull alone

**Seat:** `1.0.0_SA_CTO~Z` terminal (site Z). **Recorded by:** `1.0.0_SA_CTO~Z`, same turn.
**Context:** `2.0.0_SA_COO~RV` msg 27360 asked this seat to narrow C-HOME-PRODUCER's stop of the old pull. The same word reached
COO~RV's terminal (msg 27361): *"do not modify the existing daily etfs pull for Positioning"*. COO~RV's record is
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/ANDREW_DIRECT_20260930_20xxZ_DO_NOT_MODIFY_POSITIONING_PULL.md`.

## His words, VERBATIM (at this terminal)

> Ignore RVs comment about ETFS pull for positioning, their idea is stupid, we're leaving the existing pull alone.

## What it binds (verbatim scope; nothing added)

- `integrations/bloomberg/pipeline/etf_constituents_pull.py` is NOT modified. No stop and no narrowing.
- C-HOME-PRODUCER's "the old pull stops writing that fund in the same window" is superseded for IDVZ and PFOE. The PRD reconciles in
  v0.4.
- COO~RV's 20:20Z recommendation (narrow the stop) is not adopted.

Broadcast: `2.0.0_SA_COO~RV`, `3.0.0_SA_CVO~Z`.
