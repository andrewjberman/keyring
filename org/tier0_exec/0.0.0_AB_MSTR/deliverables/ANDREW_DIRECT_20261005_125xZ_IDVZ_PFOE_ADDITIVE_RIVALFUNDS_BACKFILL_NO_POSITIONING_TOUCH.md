# ANDREW-DIRECT 2026-10-05 ~12:5xZ -- IDVZ and PFOE: purely additive rivalfunds backfill, do not touch Positioning

- **Channel:** the site-Z terminal of `0.0.0_AB_MSTR~Z` (session 701d71e1-0145-49b8-9bad-582fbd5d8b4b), typed by Andrew.
- **Time:** 2026-10-05 ~12:5xZ (08:5x ET).
- **Recorded by:** `0.0.0_AB_MSTR~Z`, same turn.
- **Context:** this seat's relay of `2.0.0_SA_COO~RV` msg 29548, the /rivalfunds smoke findings. Its fix plan for IDVZ was
  "round 8's Bloomberg switch for IDVZ/PFOE (history from 01-02 already pulled locally)". IDVZ's only source today is the
  Positioning (home-producer) files.

## Verbatim

Andrew: "For IDVZ and PFOE, we should not touch anything being done on the Positioning pipeline. It should be done purely
additively where we do one ad hoc targeted backfill in the rivalfunds shape for IDVZ and PFOE, then we add the two funds to
the daily incremental pull with the rest of the rivalfunds."

## Scope as read (surfaced, not adjudicated)

1. The Positioning pipeline is not touched for IDVZ and PFOE.
2. One ad hoc, targeted backfill of IDVZ and PFOE in the rivalfunds shape.
3. Then IDVZ and PFOE join the rivalfunds daily incremental pull.
4. Routing: `2.0.0_SA_COO~RV` (ETFS_RIVALS) does the work; `1.0.0_SA_CTO~Z` holds the project. Bounds already in force,
   recorded on site Z and not decided here:
   - Z-S24 (CTO~Z ruling b5167de528): no backfill until production reads OK, under a daily row budget.
   - Andrew's 3-year lookback cap: record @357e681ddf.

## Addendum ~13:5xZ -- the backfill is approved (Andrew-direct at the laptop)

- **Channel:** the laptop terminal of `0.0.0_AB_MSTR`, relayed over the agentbus (frame 7d48fbb1, 13:52Z).
- **Verbatim:** "Backfill is approved for IDVZ/PFOE, please relay that to sitez MSTR~Z. They may already be aware of that."
- **Read with the 12:5xZ word above:** this approves the one ad hoc targeted backfill named there. `2.0.0_SA_COO~RV` reads it
  as round 8's D12 Step B (msg 29553). How it meets the standing bounds (the Z-S24 capacity ruling and the 3-year cap) is
  for `2.0.0_SA_COO~RV` and `1.0.0_SA_CTO~Z` to read; this record does not decide that. Relayed to both.
