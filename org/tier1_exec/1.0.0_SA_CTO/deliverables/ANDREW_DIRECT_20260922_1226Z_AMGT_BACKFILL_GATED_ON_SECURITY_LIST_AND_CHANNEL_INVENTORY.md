# ANDREW-DIRECT 2026-09-22 ~12:2xZ -- AMGT_RESAPP backfill gated on a confirmed security list and a channel inventory

**Where:** the `1.0.0_SA_CTO~Z` terminal (site Z). **Answering:** this seat's `/open-calls` frame at 12:23Z (3 cards:
B2 backfill, B4 pre-approval, the PROD look and the Lusha profile URL).

## VERBATIM

> "I agree with your recs, but I want to lock in a confirmed security list prior to backfill. There is also the matter of
> identifying every channel we are backfilling through, the bronze form of those files, the silver form of those files, the
> gold parquet/gold json form of those files, and the various ingestion cycles for each. I think this needs to be covered
> first before running any backfill operation."

## WHAT IT RULES (the narrow reading, stated as such)

1. **The recs are agreed.** That covers card 1 (B2 backfill), card 2 (B4 pre-approval) and card 3 (the PROD look after
   B2 lands, and keeping the Lusha profile URL). The two words that concern the backfill **do not take effect until the
   two preconditions below are met and Andrew has confirmed them.** Card 3's URL half (keep) takes effect now: it is
   not a backfill operation.
2. **PRECONDITION A: a CONFIRMED SECURITY LIST.** The list of securities the backfill covers is locked by Andrew's
   confirmation before any backfill runs. The seat proposes it; Andrew confirms it.
3. **PRECONDITION B: a CHANNEL INVENTORY.** It covers every channel the backfill runs through. For each channel it
   gives:
   - its bronze form;
   - its silver form;
   - its gold form (parquet and/or JSON);
   - its ingestion cycle.
4. **No backfill operation of ANY kind runs before A and B are covered.** This binds B1-B4 at every scope.
5. **Not ruled.** Round 27 (code and read-only cells: filing_attempt SKIP-HELD/supersede, and the B4 roster/domain
   diagnosis) is not a backfill operation and continues. Whether his list replaces the 3 validation names or sets the
   wider scope is for his confirmation of A, not this seat's inference.

## ACTS

- This record, committed; broadcast to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z` and `0.0.0_AB_MSTR~Z` the same turn.
- `1.0.0_SA_CTO~Z` builds A (proposed list) and B (inventory) from the code and the PRD at HEAD, lands both as a PRD
  section (contracts C-BACKFILL-SECURITIES and C-CHANNEL-INVENTORY) for Andrew's confirmation, and re-cards him.
- The held B-run drafts (`.scratch/r27_held/`) stay held. They are re-cut against the confirmed list and inventory.

-- `1.0.0_SA_CTO~Z`
