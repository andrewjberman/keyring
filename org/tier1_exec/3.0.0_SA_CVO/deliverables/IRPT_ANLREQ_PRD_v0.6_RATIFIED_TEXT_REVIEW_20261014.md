# IRPT_ANLREQ PRD v0.6 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~15:3xZ. **Delivery:** msg 7706. **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @664ef68df1 (half_hash aff0ce61fa14). **Compared against:** v0.5
@68115f2d84, which this seat signed (9f59d6bcf5).
**Authority read:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_152xZ_OPAL_STAFF_MAY_FILE_TICKET_CENTER_INTERNAL_ONLY.md`
line 11. The verbatim quote in ADDENDUM v0.6 equals the record.

**Verdict: REFUSE. The ENDPOINT carries his word, but CONTRACTS still describes the old filer.**

## The ENDPOINT against his word -- carried

- **The filer.** FWD-1's driven arm is a synthetic Opal staff user. That carries "Opal staff should not be held from filing ... we
  should have that available for testing".
- **Who sees the Ticket Center.** It is shown to Opal users only, which carries "only opal users need to see it".
- **The firm.** The filer chooses the partner firm, and "every downstream hop binds to the chosen firm".
- **Unchanged.** The four attachments, the ACCEPT, and "nobody touches anything after Submit". FWD-2 to FWD-7 are unchanged from v0.5.

## Refusal -- CONTRACTS disagrees with the ENDPOINT

- **What C-FIRM still says.** The table row (line 104) reads: "Every principal on the journey reaches exactly the request's firm: ...
  the synthetic partner-firm advisor (FWD-1's filer) by its PROFILE row ...".
- **Why that is now wrong.** FWD-1's filer is no longer a partner-firm advisor bound by its PROFILE row. It is an Opal staff
  principal that chooses the firm.
- **What is missing from the ratified text.** How a staff principal is held to exactly the chosen firm: the choice is limited to the
  served partner tenants; every hop binds to the choice; and an Opal principal's wider reach (ALL) never stands in for the choice.
  This is stated only in ADDENDUM v0.6 item 2, which is history, not ratified text.
- **Why this decides the half.** FWD-5 ("another firm never sees the request") rests on C-FIRM. With a firm-choosing filer, that
  binding is the one rule FWD-5 is graded against.

**Fix (one row):** restate C-FIRM in the table as ADDENDUM v0.6 item 2 states it:
- an Opal staff filer chooses the firm from the served partner tenants, and every hop binds to that choice;
- ALL never admits and never substitutes for the choice;
- a partner-firm user's firm is the signed-in user's and is never a choice.

## Points to fix in the same bump (not reasons to refuse)

1. **A dated attribution inside DONE WHEN.** FWD-1's DONE WHEN reads "(shown to Opal users only, Andrew 2026-10-14 ~15:2xZ)". The
   attribution belongs in SOURCE, which already carries it. Keep "(shown to Opal users only)".
2. **"(1) the advisor's original upload".** The uploader is now the Opal staff filer. Use "the original upload".
3. **The organic arm cannot run.** "A partner-firm filing (Alyssa's first real request) grades it again", in FWD-1 and in
   C-ONE-JOURNEY, cannot run while the Ticket Center is internal-only. Say that it waits on the Ticket Center being shown to client
   users. It stays "never the gate".

## CONTRACTS against the counterpart PRDs

C-PACKAGE, C-ONE-DOOR and C-TYPE are cited to TCKT_VNEXT (v0.4, signed by this seat), and C-KIMI and C-WIPE-GATE to NFRA_TRNSPT. None
of those rows changed in v0.6. C-FIRM is the one row the addendum moved.

-- 3.0.0_SA_CVO~DELL2
