# OPAL_BBGTML Z6 repairs -- drain-end record (`2.0.0_SA_COO~ZB`, 2026-10-14 ~09:4xZ)

Ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPAL_BBGTML_Z6_REPAIR_DISPOSITIONS_20261013_Z.md` @61e3067f5c, plus
CTO msgs 33741 (R4 amended), 33761 (R4 withdrawn, Andrew), 33851 (R6), 34002 (no hold, Andrew).

## Orders, 6 of 6 dispositioned

| order | seat | state | evidence |
|---|---|---|---|
| TO-Z6-R2 P0 gate: listener up, not entitled | 0.7.0_AE_CloudOps~ZS | COMPLETE; stays (Andrew ~09:0xZ "There should be no hold") | deploy f6cc68d6bf on origin; AC1/AC2/AC3 PASS; ledger opal-bbgtml-z6-r2-p0-gate-20261013 CLOSED |
| TO-Z6-R3 focus re-assert + one bounded re-fill | ~ZS | PARKED on branch zs-bbgtml-z6-r3 @7ab72b201a (LOCAL, worktree C:/tmp/zs-z6-r3 locked) | exercise needs a signed-out Terminal; dapi_check read UP at 09:25Z and 09:30Z, so no fill, no AC, nothing landed. Un-park: a dapi_check DOWN read outside 10:30Z-12:30Z |
| TO-Z6-R4 intake re-mint + backlog read + pin | 0.7.0_AE_CloudOps~ZT (released) | CANCELLED (Andrew ~20:5xZ: not a priority, TCKT is dell2's) | @ed9719f0b4; nothing ran; both pair halves WITHDRAWN |
| TO-Z6-R5 [TEAMS-ARMED] stdout receipt | ~ZT | COMPLETE | cell fab731853e on origin; AC1 ARM leg FAIL->PASS, RUNNER leg 0 bytes; ledger CLOSED; launcher census clean |
| TO-Z6-R6 portal_lookup quotes the data vintage | ~ZS | COMPLETE | b195dc14fe on origin + 31566aa49d (twin doc); AC1/AC2 PASS |

## Rows Z-S14..S20 (channel `org/surprise_channel/OPAL_BBGTML/INVESTIGATION_v1.md`, 20 rows)

| row | standing | what the CVO / CTO should know |
|---|---|---|
| Z-S14 | ARMED -> disarmed by Z-S20 | intake fetch JWT expired 2026-09-19; parked by Andrew; re-arms only if TCKT (dell2) re-opens the intake fix -- the re-mint and the pin must be one act behind a backlog read |
| Z-S15 | INERT | contradictory "transport sustained-down" line on the listener-up path; the one-line guard is on R3's branch (AMENDMENT 1), so it lands with R3 |
| Z-S16 | INERT | wintrv.exe is not a signed-out oracle: four reads over 12h show an entitled session with wintrv=0. R2's new branch has been exercised only under -ForceDown, never against a genuinely un-entitled session |
| Z-S17 | ARMED -> disarmed by Z-S20 | answered by Andrew: no hold on the sign-in scripts |
| Z-S18 | INERT | NFRA_OPALAI round-2 e7.AC1 freezes teams-watch.py by AST equality and reads FAIL from fab731853e on. Route to NFRA_OPALAI's issuer (2.0.0_SA_COO~AI, not live; project on hold) |
| Z-S19 | INERT, closed in the world by 31566aa49d | the twin doc PORTAL_RETRIEVAL.md:43 now carries the vintage order |
| Z-S20 | INERT | the disarm record for Z-S14 and Z-S17 |

## Instrument notes

- R6's multi-date ("oldest") branch is exercised on 7 stubbed shapes only; no live object carries two source vintages yet.
- The TIER0_UTILITY author override writes TWO OVERRIDE lines per act (two acts, four lines): count act ids, never lines.
- Today's 07:00 ET pull should need no sign-in: dapi_check read UP at 09:30Z.

## Owed after this round

- R3's exercise and landing, on the un-park condition (seat 0.7.0_AE_CloudOps~ZS while live; the branch is LOCAL).
- Z-S18 routing to NFRA_OPALAI's issuer.
- Open call 763e (Terminal sign-in) reads as met by the entitled reads above; it is the CTO's to close.
