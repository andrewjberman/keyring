# TCKT_VNEXT PRD v0.3 @201ed553c4 -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~22:5xZ, on `1.0.0_SA_CTO~DELL2` msg 1846. **Previous signature:** v0.2
@99eb4053c2, ENDPOINT hash cc5be01107eb.

## What changed since the signed bytes

A section diff of `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md`, v0.2 @99eb4053c2 against v0.3 @201ed553c4:
- **ENDPOINT:** one addition, FWD-9 (6 lines). Nothing else moved.
- **CONTRACTS:** byte-identical (4,726 characters in both).

## FWD-9 against Andrew's words

Andrew-direct ~22:3xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md`):
"the whole package (the report generation and a branded opal pdf with the investment commentary) needs to get attached to the open ticket
entry in addition to the initial excel file that the advisor included from the start." FWD-9's title, DONE WHEN and ACCEPT carry exactly
those three files on the still-open ticket. **Faithful.**

## Verdict: REFUSE, on two defects

1. **C-PACKAGE is not in the CONTRACTS section.** ADDENDUM 2 says "CONTRACTS and ENDPOINT both change". CONTRACTS did not change:
   C-PACKAGE lives only in the addendum's table, outside the half this signature binds. FWD-9's negative arms (refused for a non-analysis
   ticket, a closed ticket, a human caller) are that contract's rules. The contract's operative constraints are therefore absent from the
   ratified text:
   - `POST /api/scoped/tickets/{ticketId}/package`;
   - ONE service principal named in C-TYPE;
   - an open `analysis_request` ticket only;
   - pointers only, the `package` record shape.
   A signature asserts "every operative constraint present", and here it would not be true.
2. **A seat name inside ENDPOINT.** FWD-9's SOURCE line reads "...; CRO trace hop 8". The review rule bars seat names in the section. No
   other outcome's SOURCE line names a seat (this seat's scan of the section: 1 hit, this line).

**Fix:** move the C-PACKAGE row into `## CONTRACTS`, and drop "CRO trace hop 8" from FWD-9's SOURCE (the addendum already cites the trace).
On those bytes this seat signs; FWD-9's text needs no other change.
