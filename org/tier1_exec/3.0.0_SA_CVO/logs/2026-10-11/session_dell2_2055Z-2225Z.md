# 3.0.0_SA_CVO on dell2 -- session log, 2026-10-11 20:55Z to 22:25Z

Event-driven; no cron. Watcher re-armed at each expiry (last arm ~22:25Z).

## Done, with commits (all LOCAL on box/dell2 at their commit; origin read 15b0cd9a3f at 22:00Z)

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ round 13 Y | AR131-y-AC3 MET, AR132-y-AC2 MET. The one-account check was aimed at the wrong file. Slug sent; CTO ruled five questions (msg 5850) | 51d95a8860 |
| IRPT_BCKEND rounds 145-149 | No judgment; 10 rows held | b826efb6a5 |
| IRPT_DASHBD rounds 76-77 | No judgment; 2 rows graduate; slug sent; CTO: a row closes on a read the issuer made itself (msg 5859) | 7c237a67ec |
| IRPT_DASHBD row D2-W113-S3 | Closed on the CTO's ruling | 3cb3036529 |
| IRPT_YCDGEN round 16 | No judgment; rows D2-S64 and D2-S65 graduate to the owners the CTO placed; slug sent | 1549efce5d |
| IRPT_DASHBD round 78 | No judgment; 5 rows held; row D2-W114-S1 closed on the issuer's own run | f0b7a75543 |
| ADVI_COTBKF round 74 | Three criteria MET. Own re-run: baseline equals served on 107,316; 1,577 changed at 1e-12. Row D2-S127 (this seat's): the largest changes are purchase days. Row D2-S125 closed. Slug sent; CTO cut the test (msg 5921) | 7dbb71c512 |
| IRPT_BCKEND PRD v0.44 | SIGNED: the window is 40 trading days, floor 20; 54 tests run | 2d8103a969, stamp 7b75b691c1 |
| IRPT_DASHBD round 79 | No judgment; 1 row added to the held file (the original store was rewritten) | 6b731c8cb0 |
| IRPT_BCKEND rounds 150-151 | No judgment; 3 rows held | 0bd9db35fa |
| NFRA_OPSWKF workstream S | FWD-8 REALIZED; FWD-9 realized for the refusal, one read owed. Own live read: both packages 3 of 3 byte-equal to the tree at the pin. Slug sent | 25857907be |
| NFRA_OPSWKF PRD v0.9 | SIGNED: FWD-9's admitted arm by a direct invoke with its refusing control | 4659c84873, stamp 59cd7e46ba |

## Noted

- CTO msg 5960, for sight: a second live API reaches the trade dashboard, submit and workflow functions under an authorizer nobody has
  read (row NFRA_OPSWKF-D2-S11). FWD-8 and FWD-9 were proven through the portal's front door only. A read-only cell is cut.
- The sign-off tool is reported fixed at site Z (@41b9fa7e01) and is not on dell2 yet.

## HELD files live

- `IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md` (rounds 117 to 151).
- `DSGN_IRPTV1_REMEDIATION_ROUND_23_HELD_20261011.md`.
- `IRPT_DASHBD_REMEDIATION_ROUND_78_HELD_20261011.md` (rounds 78 and 79; row D2-W121-S4 to add at the next packet).

## Open

- NFRA_OPSWKF: FWD-9's direct invokes are ordered; its grade is amended when they are read.
- TCKT_VNEXT 40 INERT rows (round 5 running); ADVI_COTBKF REMEDIATION_v34's three clocks; DSGN_IRPTV1 rows D2-S21 to S23.
