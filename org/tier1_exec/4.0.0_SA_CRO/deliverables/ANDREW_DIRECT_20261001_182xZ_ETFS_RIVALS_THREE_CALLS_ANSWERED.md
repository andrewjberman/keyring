# ANDREW-DIRECT 2026-10-01 ~18:2xZ -- ETFS_RIVALS: the trace's three calls answered

**Channel:** terminal, session of `4.0.0_SA_CRO~RV` (site Z), received 2026-10-01 ~18:22Z.
**Answers:** the three "Calls only Andrew can make" in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_END_TO_END_GAP_BRIEF_20261001.md` @381bec5549:
1. a history source for IDVZ and PFOE;
2. a passive control for the PFOE group;
3. written peer-selection criteria.

## Verbatim

> 1.) We should be able to pull all this through the same bloomberg methodology that we do for all the other bbg-data
> pulls for the rivalfunds. Just add them to the same queue on the job that does that. 2.) Use Russel 2000 for PFOE,
> ACWI for IDVZ. 3.) Dont need peer selection criteria, those are pre-decided by the asset management team.

## What each answer touches (surfaced, not adjudicated)

1. **IDVZ and PFOE through the rivalfunds Bloomberg pull.** They join the same queue as the other Bloomberg-sourced
   funds (`rivalfunds.collector_bloomberg`, the box task's `:rivalfunds_bbg_leg`).
   - This is the opposite of PRD v0.7 C-HOME-PRODUCER, which says "IDVZ and PFOE leave this pipeline's Bloomberg
     request" and "never two producers of one fund's holdings".
   - The PRD amendment and its two-producers answer belong to `1.0.0_SA_CTO~Z`.
   - Open for the CTO to read from these words or ask Andrew: whether the queue covers the history backfill only, or
     the daily pull as well.
2. **Controls:** Russell 2000 for the PFOE group, ACWI for the IDVZ group.
   - Both enter the peer-group map as `index_control` entries, data rather than code (FWD-12).
   - Open for the CTO to read from these words or ask Andrew:
     - Today SCHY is the IDVZ group's `index_control`. Does ACWI replace it or join it?
     - "Russell 2000" names an index, while the style control reads a fund's published holdings. Which listed
       instrument carries it?
3. **Peer selection criteria:** not needed; the peer sets are pre-decided by the asset management team. The brief's
   call 3 and the hop-1 "undeclared peer selection" finding are withdrawn.
