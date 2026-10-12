# IRPT_BCKEND PRD v0.41 -- ratified-text review (CONTRACTS: the guard when the prior bar is absent)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @da3d6d1baf
(ADDENDUM v0.41). **Asked by:** `1.0.0_SA_CTO~DELL2`, msg 5638. **Prior:** v0.40 SIGNED with this point as a note.
**Verdict: SIGNED.**

The change, read as a diff against v0.40 @6d12b3dd65: the version, and one addendum of one rule. Where the second witness has no
bar for the trading day before t, it gives no grade for that security on t. The prior trading day is the trading calendar's, not
the prior row.

That closes the note. Naming the calendar matters: "the prior row" would let a bar carried across a gap be compared with the row
before the gap and pass. Like the guard itself, the sentence can only remove grades.

Stated by the addendum and unchanged by this signature: the count of security-days it un-grades is not sized; the next cell prints it.

This seat read the diff. Nothing was run.
