# ANDREW-DIRECT 2026-08-24 ~17:0xZ (base CTO terminal) -- 49 FINANCIAL, finding 2 of 3: we HOLD all the Black Diamond historical data (needed for backfill + SI stitching), but BD data quality is not trusted across the Schwab migration -- no clarified STABLE ACCOUNT KEY -- so a "STITCHING" project must classify every legacy account (migrated / stayed / dropped) and the BD history must move from opal-data-bd backfill/forwardfill into opal-data-assets by a methodical design

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** the second of three findings from the 49 Financial meeting (Mike), delivered at the terminal
after finding 1 (`ANDREW_DIRECT_20260824_49F_ADVI_STRUCTURE_0833_INGESTION_FIDELITY_INSURANCE_SPLIT.md`
@dbf4e493eb). Quoted exactly as typed. **DISTRIBUTION RESTRICTION (his ~16:1xZ word) binds: nothing on this
subject to `4.0.0_SA_CRO`.**

## VERBATIM

> "Second finding from the meeting: we do have all the black diamond historical data, which is important
> to have for the purpose of backfill and stitching (in the case of SI performance attribution and
> reporting specifically). However, because we do not really trust the BD data quality, specifically that
> during the migration to Schwab (which is evident by Schwab account data only starting in 2024) we have
> not yet truly clarified whether there is a stable key for account migration, to track what accounts
> migrated to new accounts, stayed in their same account, or were dropped. Accordingly, there will
> ultimately need to be a project done whereby we do a "stitching" where we assess what accounts existed
> in the legacy 2024 and pre-2024 data, and try to cross-reference what of those three eventualities
> occurred per account so we can create a basis for reliably and explainably showing what we know and
> what we don't/can't know. All this historical BD data is currently in the opal-data-bd bucket in the
> backfill/forwardfill downloads, so we will have to figure out how we want to migrate this to the
> opal-data-assets bucket and how we want to methodically design and handle that stitching process."

## WHAT IT BINDS (surfaced, unwidened; the phrasing is the ruling)

1. **We HOLD the full Black Diamond history.** It matters for **BACKFILL and STITCHING -- specifically
   since-inception (SI) performance attribution and reporting.** This sharpens finding 1's "limited history
   is fine for now": the pre-2024 tail is NOT abandoned -- it is a distinct, later project with its own
   trust problem, not a feed and not a promote condition. (Consistent with this morning's run R8: the
   legacy 2020-01-02 series is BD-derived and lives in our own bucket.)
2. **BD data quality is NOT trusted across the Schwab migration** -- the migration is *"evident by Schwab
   account data only starting in 2024"* (measured today, R4/R5: 0824 masters from 2024-01-12/16;
   08335338 from 2024-07-08). **The unresolved question is a STABLE KEY for account migration.**
3. **The STITCHING project (future, "ultimately"):** assess every account that existed in the legacy
   2024 and pre-2024 data and cross-reference which of **THREE EVENTUALITIES** occurred per account --
   **MIGRATED to a new account / STAYED in the same account / DROPPED** -- producing *"a basis for reliably
   and explainably showing what we know and what we don't/can't know."* The output is a per-account
   classification with an explicit UNKNOWN class, not a smoothed series. (Rule 24 binds the enumeration:
   the three eventualities + the unknowable residue must be MECE against the legacy account population,
   denominators printed -- the pre-registration/parity-classification discipline already in the estate
   is the template.)
4. **Data placement:** *"All this historical BD data is currently in the opal-data-bd bucket in the
   backfill/forwardfill downloads"* -> it must be **MIGRATED to `opal-data-assets`** (the canonical
   `{vendor}/{firm}/{medallion}` grammar; `blackdiamond/49financial/{bronze,silver}` is the in-pattern
   candidate, joining the `blackdiamond/49f/silver/*` join dims already there -- naming is the decomp's
   to fix; Rule 17a: the raw downloads land as BRONZE bytes, parquet is a silver act) **and the stitching
   process must be methodically DESIGNED** before it is run -- *"figure out how we want to migrate this ...
   and how we want to methodically design and handle that stitching process."*
5. **Sequencing, from his words:** "ultimately" -- this is a project to be REGISTERED and PRD'd through the
   Rule 27 pipeline, not started now; it pends nothing on the ADVI 08335338 route (finding 1) and gates
   nothing on it. It is the correct home for every history question this morning's run priced (the
   frozen-tail option becomes a stitching OUTPUT, not a copy act). The ADVI_49FSRC project's history
   section is SUPERSEDED-BY-SPLIT: the blend stays (value plane, both Schwab masters); the pre-2024 history
   moves to this stitching project.

## BROADCAST
MCP to MSTR + the queued seats that will hold cells (COO, CVO, DS, DE, AE, DT, 0.6.0_AE_PartnerETL --
the BD vehicle owner). **NOT to 4.0.0_SA_CRO.** Same turn; push state stated on the commit.
