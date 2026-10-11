# IRPT_ANLREQ rounds 8 and 9, workstream Y -- L9 read

**From:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:07:52Z. Row IRPT_ANLREQ-D2-S55.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND9_Y_L8_COMPILE_20261011.md @70070b3a69 (msg 5416)`. No judgment criterion. The packet asks two things of a reviewer.

## 1. Should "LIVE" carry "and unexercised by any product path" wherever it is repeated?

**Yes.** The function runs the new build and its role holds the grant; this seat read both live. But no event source feeds the
commentary drafter, so the only requests that have passed the gate are the release's own three after-reads. "Live" alone will be
read as "working for users". The honest short form is: released, and reached by no product path yet.

## 2. Is A1 equal to G2 on one request enough to call two unexercised members inert?

**No. It is enough to say that one path through them did not change.** The release moved three files. One is the gate, which the
after-reads exercised both ways (a READY request answers as before; a request whose job reads RECEIVED is now refused). The other
two, the repository and retention members, are called inert on a read of their diff and on one request returning the same bytes
before and after. One request shows one path. The census itself marks "inert" as inferred, which is the right word. They stay
inferred until a request that takes their changed lines is read, or the changed lines are shown unreachable.

## What this seat read live

- The function's hash is the build the packet names, modified 16:41:35Z.
- The role's read grant names two tables, the requests table and the jobs table. Without the second, the gate would refuse every
  read; that was the hazard of row D2-S53 and it is disarmed.
- irpt-status is still revision 6. Nothing from rounds 3 to 7 is on it.
- The portal's generated reason set on DEV holds the new reason, so row D2-W52-S7 is disarmed. The round-7 portal candidate that
  sends the ticket's id is still not on DEV, so the ordering hazard of row D2-S51 stands as it was: armed, held by a message.

## Read against the outcome

The gate refuses a composition for a request whose job is not READY. That narrows what the drafter can be asked to write about, to
finished reports only. It serves the journey's promise and removes nothing a reader was promised.
