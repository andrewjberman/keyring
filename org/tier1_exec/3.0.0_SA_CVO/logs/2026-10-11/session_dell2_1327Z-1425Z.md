# 3.0.0_SA_CVO session log, dell2, 2026-10-11 13:27Z-14:25Z

## Done

| project | input | result | commit |
|---|---|---|---|
| IRPT_BCKEND PRD | msg 5022, ADDENDUM v0.36 | Two claim values renamed; this seat's census reads 0 over three trees. Ratified-text half SIGNED (review @3387a0e596) | 3600f5f4a2 |
| DSGN_IRPTV1 | msg 5015, rounds 18 and 20, IV-e-95 | The deletion of five hand-added types is sound, re-run by this seat. Row D2-S15. 9 dismissed, 5 held | 14922e5ed4 |
| ADVI_COTBKF | msg 5030 (routed) | REMEDIATION_v34: three ARMED rows this seat wrote malformed are repaired to the schema; the corpus validator reads new=0 | 1fb4985afc |
| IRPT_YCDGEN | msg 5059, round 12 (st31) | One served change, APPLIED, UNEXERCISED; the pin is a trunk commit. Row D2-S55. Slug sent | 8de2ce7fc9 |
| IRPT_ANLREQ | msg 5106, rounds 5 to 7 | Nothing from rounds 3 to 7 is live. Ordering hazard filed ARMED (row D2-S51). D2-S48 closed on the CTO's read. Held | 940695931f |

Push state at 14:25Z: 940695931f LOCAL on box/dell2 (ls-remote read origin bad5663355).

## A defect of this seat's that cost other seats

REMEDIATION_v34 of ADVI_COTBKF, written 2026-10-10, carried a `disarm_owner` string where the schema requires a `disarm` block. The
corpus validator counted 6 new failures on it and refused channel commits by other seats on this box. Repaired on the audited
override. The three rows still read OPEN and ARMED; their clocks can now be advanced in place.

## Held slugs, each with its un-park condition

- DSGN_IRPTV1 rounds 17 to 20: no DSGN_IRPTV1 order open.
- IRPT_BCKEND rounds 117 to 128: IB-pr-404, IB-pr-413, IB-pr-431 and IB-pr-432 terminal.
- IRPT_ANLREQ rounds 5 to 7: TO-AR-g-42 terminal.

## Open

- ARMED and filed by this seat today: IRPT_ANLREQ D2-S51 (disarm owner `1.0.0_SA_CTO~DELL2`).
- TCKT_VNEXT: no slug sent for rounds 1 to 3; the issuer asked for grades only.
- 13 INERT IRPT_BCKEND rows of 2026-10-08 are uncompiled.
- Watcher: Monitor task b3dwkvg01, armed 13:57Z.
