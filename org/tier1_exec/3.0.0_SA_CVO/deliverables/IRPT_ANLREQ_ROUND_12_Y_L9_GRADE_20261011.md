# IRPT_ANLREQ round 12, workstream Y -- L9 grade of AR121-y-AC3 (the queue list's elapsed age)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:17:19Z. Row IRPT_ANLREQ-D2-S61.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND12_Y_L8_COMPILE_20261011.md @3d9a1b2589 (msg 5732)`. Read: portal commit d16b5510, now on origin/DEV c2c6a8aedd.

**Verdict: AR121-y-AC3 MET.**

| limb | verdict | evidence |
|---|---|---|
| a reader learns how long each open ticket has waited without subtracting | **MET** | The created cell shows the created time and, beside it in brackets, the age in words: `under a minute`, `48 minutes`, `5 hours`, `3 days` |
| nothing else about the list reads differently | **MET** | One line of the list changes, the created cell. No column is added. A completed ticket shows the created time alone, as before |

The helper never prints a zero, a negative age or an invalid date: a missing, unparseable or future created time gives nothing,
and the cell then shows what it showed before. That is the right failure.

## Three things a reader of the list should know

1. **The age is rounded down to one unit.** A ticket that has waited 47 hours reads `1 day`. For a queue where a day matters, the
   second day is invisible until it is complete. It answers "how long" coarsely; it does not mislead.
2. **It is computed when the page draws and does not tick.** A page left open shows the age as of its last draw.
3. **The code shows the age for every status except completed**, which is wider than the packet's "open or in progress". If another
   status exists, its tickets show an age too.

Not looked at by this seat: a rendered page, the age text's contrast, a real ticket. The issuer looked at one built page with
five synthetic rows.
