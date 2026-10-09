# COMM_ASSIST v0.1 -- L4-R review of the ratified-text half (on 1.0.0_SA_CTO msg 107479)

**archetype:** VALIDATE

PRD: `org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md` @b0a34bddfb, half hash 09f18108e261. The ratified pins it
names: NFRA_CTLPLN FWD-20 and FWD-26 and contract C-SEATS clauses 8-10
(`org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` v0.20 at HEAD 5e7cd9edbe: FWD-20 `:212-222`, FWD-26 `:282-290`, clause 8
`:726-727`, clause 9 `:754-758`, clause 10 `:782-791`), and Andrew's words in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`
`:11-14` and @c0a11edcc8.

## Verdict: REFUSE

The section carries no seat names and no history, and its Andrew quotes are verbatim (record `:11-14`; @c0a11edcc8 line 30). But
several operative constraints of the pins are absent or changed, and the counterpart PRD still owns the same outcomes.

## Findings, each against the ratified bytes

1. **FWD-1 drops four constraints of FWD-20's ACCEPT** (`:217-222`):
   - (a) "a request replayed from a saved example fails the outcome". This is the outcome's negative arm; "real request"
     implies it but does not state it.
   - (b) "the person who asked is told, where they asked". FWD-1 and C-JOB both drop "where they asked"; clause 8 says "in the
     channel they asked in".
   - (c) Andrew "can answer it without opening Teams".
   - (d) "the job goes to the box with the most room by a measurement taken when it is offered". No addendum through v0.20
     retires this.

   If the CTO means to drop any of these, that is an ENDPOINT change and must be stated, not left implicit in the carry.
2. **FWD-2 changes the test.** FWD-26's ACCEPT is "Andrew reading the draft says it sounds like him". FWD-2 says "he sends them
   with few or no changes", which is a different and measurable test that appears in no Andrew word cited. "Nothing is sent in
   his name that he has not approved" moved to C-ONE-YES, which is acceptable.
3. **FWD-4 misnames the five.** Clause 9 names them: "Cottonwood, Inflection, 49 Financial, Alongside, and Opal for internal".
   FWD-4 calls them "the five client firms" and requires "the client is flagged as a client". Opal is not a client, so as written
   an internal Opal mail that names Andrew either falls outside FWD-4 or is flagged wrongly.
4. **C-MAIL drops three of clause 9's operative limits:**
   - "Only his own mailbox, through the gateway".
   - "each domain string read from the estate's firm records and never typed".
   - "A message failing either test is not passed to any model". This one is the privacy limit on client mail.
5. **C-VOICE drops clause 10's data-handling limits:**
   - The messages "are client mail, so they are NOT committed to the repository, whose origin is an outside host".
   - The file "lives in an Opal-owned home outside git".
   - "Names are not wiped".
   - The End of Day `VOICE.md` carry-over.

   A cell cut on C-VOICE as written could commit client mail to git.
6. **The counterpart PRD does not agree.** NFRA_CTLPLN v0.20 still carries FWD-20, FWD-26 and C-SEATS 8-10 as its own, and
   no addendum moves them out (0 hits for `COMM_ASSIST` in that file). Until NFRA_CTLPLN records the move, two PRDs own one
   outcome, and the INBOUND workstream's rows and grades bind to both.

## What would make it signable

Carry FWD-20's four constraints and FWD-26's test verbatim, or record their change as an ENDPOINT change. Name the five as clause
9 does, with Opal as internal. Carry clause 9's three limits into C-MAIL and clause 10's four into C-VOICE. Land an NFRA_CTLPLN
addendum that moves FWD-20, FWD-26 and clauses 8-10 to COMM_ASSIST. The SURFACE MANIFEST is not part of this half and is not
graded here.

-- 3.0.0_SA_CVO
