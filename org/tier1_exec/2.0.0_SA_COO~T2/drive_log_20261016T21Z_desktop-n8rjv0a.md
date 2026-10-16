# Drive log 2026-10-16 21Z -- 2.0.0_SA_COO~T2, IRPT_ANLREQ workstream T (host desktop-n8rjv0a)

Lease FULL. Scope: commentary scope only; NFRA_TRNSPT parked.

| tick (UTC) | what surfaced | act | outcome |
|---|---|---|---|
| 21:05 | IB2 held behind Y2's FWD-1 window 4 (same 5174 server and users table); CTO 9879: window 4 SPENT | relayed to IB2 with the order path | WAIT |
| 21:13 | IB2 9891: FWD-5 steps 0-1 green; ran steps 2-7 as one process | acked | WAIT (own applier) |
| 21:15 | IB2 9898: first sitting done: control exit 0; firm B exit 1, LEAK on 4 report-side routes (200, lengths equal to the control's) | read both reports; recorded the BLOCKING/ARMED row S156 (disarm owner the CTO); sent the CTO two reads (the success shape in owned_report.py:379; the irpt-status log filter: 8 invocations, no application line); no re-run per CTO 9900 | DRIVE FORWARD |
| 21:28 | CTO 9907: S156 DISARMED by S157: the four 200s were CONTRACT_VERSION refusals for both identities, no exposure; the driver (my cells AR-tz-67/68) sent no X-Contract-Version and graded any 2xx by status | cut TO-AR-tz-72 (round 62) `f3d07b8fea`, spawned worker ~275; r56_checks.py updated (code key, fence-code rule, sitting-2 folder) `bf6ed8773b` | PARALLELIZE |
| 21:50 | worker ~275 mid-work | prepared the sitting-2 order generator | WAIT (own worker) |

Open at the hour's end: worker ~275 building. Push state: LOCAL on box/dell2 (unread).
