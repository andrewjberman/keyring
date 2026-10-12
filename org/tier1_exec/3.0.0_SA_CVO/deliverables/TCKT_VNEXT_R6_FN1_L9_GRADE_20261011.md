# TCKT_VNEXT round 6 -- L9 grade of TO-RUN-R6-fn1 AC2 (FWD-2's live proof for the ticket)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T23:10:27Z. Row TCKT_VNEXT-D2-S47.
**Input:** `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R6_FN1.md @31091d1eeb (msg 6047)`. Read: the applier's result file, arm by arm, and the function's live code hash.

**Verdict: AC2 MET for the ticket. FWD-2 is NOT yet realized: its sentence names "the request or its file", and the file's second
arm is owed. The issuer reads it the same way.**

| arm | constructed caller | answer | what it shows |
|---|---|---|---|
| A2 | a client of another firm, asking for the ticket | 403 | another firm's person cannot open it |
| A3 | the same caller, asking for the list | 403 | nor list it |
| A5 | the same caller, an id that does not exist | 403, the same fields | nor tell a real ticket from a missing one |
| A1 | a client of the ticket's OWN firm | 403, the same fields | the refusal is by class of caller, not by firm |
| A4 | an internal caller with no users row | 200 | the control: the instrument can read a served answer |

The refusing arms and the served control are both there, on the deployed function, by direct invocation with no identity minted.
That is the instrument this seat signed for NFRA_OPSWKF. Five reads wrote nothing (the applier's counts before and after).

## Three things the grade must carry

1. **The outcome is met by something stronger than it asks, and that should be said.** No client of any firm can open any ticket
   through this service. FWD-2's sentence is about another firm's person; the service refuses the ticket's own firm's client too.
   If a client is ever meant to see its own ticket, that is a change to this rule, and the firm fence would then be the only thing
   between two firms' clients. That fence was not exercised here.
2. **The firm fence between internal callers was not shown live.** A staff caller scoped to firm B asking for firm A's ticket
   needs a users row for the constructed caller, and none was written. It rests on tests and on the earlier runs' census.
3. **The control is itself a finding, already filed:** an internal caller with NO users row is served, unscoped (row D2-S20). And
   the instrument works because the function believes the caller in the event (row D2-S46, ARMED, owner the CTO): anyone holding
   the right to invoke this function can be any caller to it. A direct invoke proves the function's rule. It does not prove that
   nobody else can make one.

## The file

Not read by this act. One arm stands from the fifth run (other firms refused on the file's route as the one-firm filer); the
second, another firm's client asking for a real request's original, is owed by another seat. Until it is read, FWD-2 is met for
the ticket and open for the file.
