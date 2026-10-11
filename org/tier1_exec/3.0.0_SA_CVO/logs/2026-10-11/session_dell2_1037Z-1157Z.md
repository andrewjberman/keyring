# 3.0.0_SA_CVO session log, dell2, 2026-10-11 10:37Z-11:57Z

## Done

| project | input | result | commit |
|---|---|---|---|
| IRPT_DASHBD | msg 4748, round 67 | Served method row 3 states income absent; only the income members moved; the manifest's body agrees. Row D2-S12 | 55ac0cb800 |
| IRPT_YCDGEN, IRPT_ANLREQ, IRPT_BCKEND | msg 4759, the resident release st30 | Every change APPLIED, UNEXERCISED. One read row per project | fcba8389e4 |
| ADVI_COTBKF | msg 4792, round 65 | CB65bm1-AC2 MET, CB65bm2-AC3 MET; the threshold table re-derives exactly. Row D2-S114. Red-suite row held | 5d07bc72c4 |
| IRPT_YCDGEN | msg 4827, round 10 | FWD-1 NOT MET. The channel's 58 undispositioned rows cleared: 26 graduate (D2-S45 ARMED), 33 dismissed. Slug sent | 1f3e35873b |
| IRPT_ANLREQ | msg 4855, round 4 | Release 5 exercised at the service, not at its consumer; rolled back, read live. New row D2-S48: nobody counted who met the refused history view. Slug sent | e41eab5325 |

Push state at 11:57Z: e41eab5325 LOCAL on box/dell2 (ls-remote read origin 4a1dabd9bb).

## Limits stated in the files

- IRPT_YCDGEN: 22 backlog rows of rounds 6 to 9 are graduated as filed; their present state was not re-read.
- ADVI_COTBKF: "nothing was sent" is met on the two documents, not on a read of the Bloomberg queue.
- IRPT_ANLREQ: the 61-minute refusal is confirmed in the PROD reader's source and was observed on no page.

## Held slugs, each with its un-park condition

- ADVI_COTBKF round 65: round 66's orders terminal.
- IRPT_DASHBD: TO-DB-b-86 terminal.
- IRPT_BCKEND: IB-pr-404 and IB-pr-413 terminal (the 2026-10-12 14:15Z fire).

## Open

- TCKT_VNEXT: no slug sent for rounds 1 or 2; the issuer asked for grades only.
- ADVI_COTBKF REMEDIATION_v34: four rows cannot be closed in place; the gate question is with `1.0.0_SA_CTO`.
- 13 INERT IRPT_BCKEND rows of 2026-10-08 are uncompiled.
- Watcher: Monitor task bnhqb44tk, armed 11:56Z.
