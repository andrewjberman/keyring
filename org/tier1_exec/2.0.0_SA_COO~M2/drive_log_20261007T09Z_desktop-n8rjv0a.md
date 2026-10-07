# /canonical-drive IRPT_BCKEND workstream M -- 2.0.0_SA_COO~M2 (dell2), hour 2026-10-07 09Z

## tick 3 -- 2026-10-07 09:02Z
| IRPT_BCKEND (M) | L6 R30 ~M: IB-mr-301 decomposed @56673dbea2, NOT issued (S352 BLOCKING) | M R30 | 0 open / 203 | 0/1 (blocked) | held LIVE | NO-OP: waiting on the laptop 3.0.0_SA_CVO read (decision 106087, relay msg 220); reader 8258fed480 LOCAL, not on origin; no result FILE yet. Lease FULL. |
## tick 4 -- 2026-10-07 09:35Z
| IRPT_BCKEND (M) | L6 R30 ~M: IB-mr-301 amended (AMENDMENT 1 @d6a3e7b04b), NOT issued | M R30 | 0 open / 203 | 0/1 (blocked S352) | held LIVE | NO-OP: first laptop read @e9993e95fa not gradable (row S356); second read relayed (msg 262); reader d6a3e7b04b LOCAL, not on origin. Lease FULL. |
## tick 5 -- 2026-10-07 10:02Z
| IRPT_BCKEND (M) | L6 R30 ~M: IB-mr-301 AMENDMENT 1, NOT issued | M R30 | 0 open / 203 | 0/1 (blocked S352) | held LIVE | NO-OP: second laptop read first in the laptop CVO queue (106139, msg 292); reader d6a3e7b04b on origin branch r3/r4; no FILE yet. Round 61 analysis (msg 278): M has no new items. Lease FULL. |

Decisions closed: first laptop read @e9993e95fa graded not-gradable (row S356); issuer AMENDMENT 1 to IB-mr-301 (c2 over SPYI or PSLV; c3 reads the platinum header, absent = FAIL) with the amended reader, @d6a3e7b04b; second read relayed (msg 262). Round 61 analysis @aae1ed7781 gives M no new item.
