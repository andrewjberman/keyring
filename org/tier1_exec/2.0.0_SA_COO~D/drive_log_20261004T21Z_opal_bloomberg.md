# Drive log -- 2.0.0_SA_COO~D -- 2026-10-04 19Z to 21Z (host opal_bloomberg), after the 18:58Z site-Z crash

| time (Z) | project | limb | round | TOs | act |
|---|---|---|---|---|---|
| 19:32-19:45 | -- | startup | -- | -- | Relaunch: registered, watcher armed, 48/48 mail READ, state report @0938b4fbef read. The crashed session's round-35 authoring agents (18:46Z) left nothing on disk; round 35 re-made from L5. |
| 19:54 | DSGN_AMGTV1 | -- | -- | -- | Andrew's yes to restarting the AMGT drive loops (@3166fec43e, msg 29204): `/canonical-drive DSGN_AMGTV1` 30m re-armed off the live LIVE_ARMS row. |
| 19:45-20:50 | DSGN_AMGTV1 | L5 | r35 | -- | Timeline captured read-only on FcVBPafw (40 terms on 6 of 6 names). Three check authors; every check re-run by the issuer at base 055ba370 (changed35 2/5, payload35 2/4, cloud35 2/5; green 5/5, 4/4, 5/5). |
| 20:54 | DSGN_AMGTV1 | L6 | r35 | 0/3 | ISSUED @f7ad5dc777: AV-zm-1 (~94), AV-zm-2 (~95), AV-zm-3 (~96); fanout 3 of 3, cap 8. FWD-20 instrument re-anchor not cut (its check had no base reading at the cut) -> round 36. |
| 20:56 | DSGN_AMGTV1 | -- | r34 | -- | Andrew's yes to the 055ba370 DEV push (MSTR~Z msg 29229). Told MSTR~Z condition 1 was met @de215bcd50. DEV 2c792c27 carries it, CI green (msgs 29239/29241). |
| 21:05-21:16 | DSGN_AMGTV1 | L7 | r35 | 3/3 | Each worker's AC1 re-run by the issuer: 5/5, 4/4, 5/5. Drained b3b711eab6, 4e56f98b2f, 67615038c1. Candidate d60a0f90 = DEV 2c792c27 + r35: battery29 ALL PASS, r34/r35 checks full. |
| 21:20-21:32 | DSGN_AMGTV1 | real run | r35 | -- | Close walk read-20261004T212050Z on 5174 (ARMED 21:20:51Z, DISARMED 21:31:59Z, login after REFUSED): 20 PASS / 2 FAIL / 1 ERROR, graded in ROUND35_CLOSE.md (the BA "-100.0%" is a real move; the fwd5 tooltip FAIL is pre-existing). |

**State:** candidate portal d60a0f90 goes to the CTO's product-file review. Round 36 is named in ROUND35_CLOSE.md section 4: the FWD-20
instrument re-anchor (its check reads 0/4 at base, 4/4 green), the list-state font sizes and radii it sees, the FWD-5 tooltip's
loading headline, and the "-0.00%" moves.
