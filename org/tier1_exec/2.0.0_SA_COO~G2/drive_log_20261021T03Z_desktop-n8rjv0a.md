# Drive log 2026-10-21 03Z -- 2.0.0_SA_COO~G2 (host desktop-n8rjv0a)

Scope: IRPT_ANLREQ workstream G (FWD-10 Core) and IRPT_YCDGEN. Leases read FULL for both.

| time (Z) | limb | act | result |
|---|---|---|---|
| 03:2x | L7 release | r34q rehearsal refused on a moved policy hash of `irpt-dashbd-x10-v1` | builder and checker amended (21cb4e857d): tolerate that one revision only while PENDING_ENFORCEMENT in both trees; any ACTIVE revision that moved still refuses |
| 03:3x | L7 release | rehearsal at 21cb4e857d in `C:/dev/irpt-trial-r34q4` | R34Q-BUILD-OK, 323 members, 7 changed, 0 added, builds identical 323 of 323, tar sha256 f757171891f3924458123168abe2ccbba87d4b5bc12821cfa0f59b0f38b9266b |
| 03:3x | L5 checker | `ar_release_q_checks.py` calibrated | record OK, tree OK, scripts OK on the rehearsal; tree FAIL on the r34p tarball (delta empty, five movers not pinned, audit revision absent, admission replay fails at step 3) |
| 03:3x | rule | IB2 DLQ delete report (msg 11829) | run 7H's one message deleted by receipt handle; DLQ 11 to 10; source 0/0; acked |
| 03:4x | L6 issue | AR-g-181 cut (3f4ea4e4ec), slot 354, workstream ~GREL5 | fanout: 1 of 1 chains, cap 8; AC1 to AC3 base FAIL as expected; worker 354 spawned (haiku/high) in `C:/dev/wk-irpt-anlreq-354` |
| 03:4x | rule | CTO msg 11843 | r34q ships with the dashbd move tolerated; the packet carries the shipped dashbd state, an IB2 census of rows under dashbd and the audit revision (both expected 0) and the checker rule |
| 03:4x | L6 order | IB2 read-only census cut (21c26e6921), GO sent (msg 11844) | pending IB2 report |

Open: worker 354 report (verify and merge); IB2 census report; then the r34q never-widen packet (COO half), CTO half, the IB2 apply order and GO; then the Multi-Comp filing rerun and the PDF read. Gateway restart window 06:00Z to 06:55Z: no gateway-calling runs in it.
