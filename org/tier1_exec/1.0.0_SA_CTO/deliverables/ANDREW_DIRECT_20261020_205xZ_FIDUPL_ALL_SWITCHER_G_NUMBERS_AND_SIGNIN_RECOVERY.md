# ANDREW-DIRECT 2026-10-20 ~20:5xZ at the 1.0.0_SA_CTO~DELL1 terminal: NFRA_FIDUPL covers every G number in the switcher, and the agent recovers the sign-in

**Recorded by:** 1.0.0_SA_CTO~DELL1.
**Context:** Andrew had just completed a sign-in by hand on the Fidelity box, through the text-message code, in the puller's profile.

## His words, VERBATIM (typos his)

> The agent needs to be able to orchestrate the daily pulls across all G Numbers attached in the G Number Switcher. They also need to
> be able to manage the full sign in over the browser in the event that trust token dies for whatever reason.

## What this sets (NFRA_FIDUPL)

1. **Coverage is every G number the login's G Number Switcher lists**, read from the switcher at each run, not from a fixed list.
   - Each G number is split to its own firm, as PRD v0.4.5 already rules.
   - A G number the switcher lists that has no firm attribution lands under `alongside` and is named in the run record.
   - The secret holding the per-G list becomes a check against the switcher, not the source.
2. **The sign-in recovers itself.**
   - When the stored session is no longer accepted, the agent runs the full sign-in in the box's own browser, end to end: username,
     password, "Text me the code", and the code read from Quo.
   - This is the dell1-driven browser path (FU-s-12, track B), with secrets kept on the box.
   - Each recovery is recorded in the run record. A recovery that fails stops the run and is reported. It is never retried in a
     loop.
3. **Unchanged:** Fidelity is used only as an authorized user (C-TOU, Andrew-direct 2026-10-19 ~19:0xZ); one password attempt per
   run; no new spend.

Routed to 2.0.0_SA_COO~P1 and 4.0.0_SA_CRO~FIDELITY as round-3 enrichment under PRD v0.4.6.
