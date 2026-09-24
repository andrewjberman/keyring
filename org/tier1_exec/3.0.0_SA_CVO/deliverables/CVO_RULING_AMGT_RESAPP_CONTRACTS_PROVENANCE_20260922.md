# CVO ruling -- AMGT_RESAPP: what the CONTRACTS section may carry about its own provenance (governance fork)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22 ~10:4xZ at HEAD after `752b2f0881` (SITEZ, LOCAL).
**Routed here by:** `1.0.0_SA_CTO~Z` msg 24185, as a governance fork (what the ratified text may contain).

## The conflict

Two texts disagree, and both bind the ratified-text half:
- The L4-R delivery checklist: "no annotation, history or seat name inside the section".
- The CONTRACTS section's own preamble: "Each one names its owner and the record it comes from."

The CTO's census: 50 of 369 CONTRACTS lines carry dates, seat serials, commits or row ids. Some of it is incidental
history. Some of it is the AUTHORITY for the rule -- e.g. C-PEER-SET-SA's *"Yes use SA thats fine"*, the vendor lift.
This seat's v0.17 carry-item asked for the cleanup without separating the two.

## Ruling

**The CTO's recommendation is adopted, with one amendment that fixes where the binding pointer lives.**

1. **No pure deletion.** Stripping a vendor lift or a sovereign word from the contract it authorises makes an
   Andrew-reserved decision read as self-granted, and separates a permission from its audit trail. Rejected.
2. **Each contract keeps exactly two provenance items, both inside the ratified text:**
   - **ONE owner** -- the seat that holds the contract's remedy. The checklist's "no seat name" is read as "no
     incidental seat history"; the preamble's owner field is a requirement of the ratified text, not an annotation.
   - **ONE source pointer to an IMMUTABLE record at its commit** -- the Andrew-direct record, CTO ruling or
     adjudication row that authorises the contract, as `path@commit` (e.g. `ANDREW_DIRECT_..._.md@<hash>`). The commit
     is the vintage, so no separate date is written.
3. **Everything else incidental is stripped from the section:** measurement narratives, lane suffixes (`~W`, `~Z`),
   intermediate commit trails, and "measured on" asides.
4. **The long verbatim authority quotes MAY move to a "CONTRACTS SOURCES" appendix in the brief half, keyed by
   contract id -- as a convenience copy, never as the authority.** THIS IS THE AMENDMENT: under the recommendation as
   written, the contract's pointer would lead to the appendix, which sits in the BRIEF half. That half is signed by
   the brief reviewer, and an edit to it does not re-open the ratified text -- so the quote that authorises a
   ratified contract could change without the ratified-text reviewer ever seeing it. Pointing the contract at the
   immutable record itself keeps the authority inside what this seat signs, and makes the appendix harmless to edit.

## Scope and non-application

- The bump is graded on a straight diff: every removed line is incidental history, every contract ends with one
  owner and one `path@commit` pointer, and no operative sentence changes. A diff that changes a rule's substance is
  refused, however small.
- A contract whose only authority is the PRD's own ratification (no external record) carries its owner and no pointer.
- This rules the CONTRACTS section only. ENDPOINT is already free of provenance and stays so.
- Not a gate. It is the ratified-text reviewer's reading rule, the same class as R4.

COST: one pointer per contract, written once. NON-APPLICATION: a contract with no external authority (above).

-- `3.0.0_SA_CVO~Z`
