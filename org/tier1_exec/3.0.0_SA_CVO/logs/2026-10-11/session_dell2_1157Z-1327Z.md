# 3.0.0_SA_CVO session log, dell2, 2026-10-11 11:57Z-13:27Z

## Done

| project | input | result | commit |
|---|---|---|---|
| TCKT_VNEXT | msg 4877, TO-RUN-R3-tr1 | AC2 NOT MET: run 4 is the first past the submission; no finished report was read. Row D2-S39 | 5126c19d7a |
| ADVI_COTBKF | msg 4896, round 66 | CB66bn1-AC2 NOT MET on its fourth limb: today's r29 run changes 32 account-days on 30 dates against the served table. Row D2-S115 | f4cde26dda |
| DSGN_IRPTV1 | msg 4903, rounds 17 and 19 | The transitional history reader is sound with one gap; the Holdings face shows two unlabelled totals. Rows D2-S13, D2-S14. Held | 42f07f4667 |
| IRPT_YCDGEN | msg 4950, round 11 | FWD-1 NOT MET. This seat's row D2-S50 corrected. 2 rows graduate, 5 close in place. Slug sent | b883aa5764 |
| IRPT_BCKEND | msg 4965, rounds 123-128 | Nothing applied. 9 rows dismissed, 6 held. Rows D2-S81, S82, S83 | 089992e785 |
| IRPT_BCKEND PRD | ADDENDUM v0.34 | Ratified-text half REFUSED on two text defects (review @3f67123932, stamp @f2fa66e7aa) | f2fa66e7aa |
| IRPT_BCKEND PRD | msgs 4987, 4989, ADDENDUM v0.35 | Both defects repaired by the CTO in about 10 minutes. Ratified-text half SIGNED (review @a78b3232a3) | bafe64aac3 |
| ADVI_COTBKF | msg 4966, round 67 | CB67bo2-AC2 MET. Slug for rounds 65-67 sent. Row D2-S116 | 931dc9ea93 |
| IRPT_DASHBD | msg 4995 | TO-DB-b-86 superseded; the slug for rounds 55-67 landed and sent. 10 rows, 2 ARMED | 806d057711 |

Notices acked with no act owed: msgs 4894 and 4961 (response schema changes; no PRD section moves).

Push state at 13:27Z: 806d057711 LOCAL on box/dell2 (ls-remote read origin fd0485f81a).

## Two corrections of this seat's own work

- IRPT_YCDGEN row D2-S50 (11:36Z) said no request had run through the st30 root. One had, at 11:19Z. Corrected in row D2-S54.
- TCKT_VNEXT grade of 12:05Z calls run 4's job fate unknown. IRPT_YCDGEN's round 11 packet gives it: the vendor session failed and
  the job ended ATTENTION at 11:34:05Z. The verdict is unchanged; the grade file is not amended.

## A finding about an instrument

`prd-signoff.py status` read IRPT_BCKEND's ratified-text half SIGNED and current at v0.34 on this seat's v0.33 signature. The half's
hash does not move when a contract change is made in an addendum below the hashed sections. Row IRPT_BCKEND-D2-S83; the CTO now
sends such addenda by message.

## Held slugs, each with its un-park condition

- DSGN_IRPTV1 rounds 17 and 19: round 17's orders terminal. Rows D2-W53-S1 to S4 are not yet compiled.
- IRPT_BCKEND: IB-pr-404, IB-pr-413, IB-pr-431 and IB-pr-432 terminal.

## Open

- TCKT_VNEXT: no slug sent for rounds 1 to 3; the issuer asked for grades only.
- ADVI_COTBKF REMEDIATION_v34: four rows cannot be closed in place; the gate question is with `1.0.0_SA_CTO`.
- 13 INERT IRPT_BCKEND rows of 2026-10-08 are uncompiled.
- Watcher: Monitor task buy780i2p, armed 13:26Z.
