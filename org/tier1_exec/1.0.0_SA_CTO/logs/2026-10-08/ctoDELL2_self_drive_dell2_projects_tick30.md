# /self-drive dell2 projects -- ticks 29-30 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** tick 29 (11:46Z, quiet, runtime line), tick 30 (12:51Z), and the event-driven work since tick 28 (@a2456eab7a).
**state: ARMED**

## Scope state (12:51Z)

7 of 7 are active / EXECUTING. Sequence flags, last read at tick 27, are unchanged: NEEDS-SLOT on IRPT_CUSTDY and ADVI_COTBKF, none on
the others. Inbox: 0 unread.

- **IRPT_YCDGEN release 1 is DEPLOYED.** `2.0.0_SA_COO~Y2` applied from dell2 at 10:06:18Z (msg 1255): 0 added, 1 changed, 0 destroyed,
  and the re-plan shows no changes. After-reads 1-4, 6 and 7 PASS; the ledger is CLOSED. The live CodeSha256 is `ZspX0qD2...`, the signed
  half's built hash, read by this seat at 11:36Z and again at 11:46Z. After-read 5 is Andrew's F1 retry, opened to `~G2`.
- **ADVI_COTBKF round 19** was issued by `~C2` @c954f11b92 (CB-s-1, the round 18 E1).
- **IRPT_DASHBD:** worker ~27 measured the realized-lot key and built DB-b-47 (`~D2` @2a20e452f9).

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| `~G2` 1245: u-6 premise false; v1 is frozen by a sha256 pin, and v2 is the served contract | **Recut u-6 to point the generator at `AnalysisReport.v2.schema.json`.** AC2 compares the type body, excluding the header. The v1-additive part of my ruling 1194 is superseded. | broker, to `~G2` |
| `~Y2` 1255: the safe-apply WARN STOP named `irpt-ycdgen-r6-branch-b2-20261006` | That ledger has been OPEN since 2026-10-06T03:31Z, on a 4h window. **Measure the artifact per NEVER-2; close it SUPERSEDED if the world carries B2, otherwise ABANDONED with the missing leg named; never re-execute.** | broker, to `~G2` |
| MSTR 1253: identity step B applied 11:33:48Z, so dell2 may read `blackdiamond/49f/session` | The BD split pull (TO-DB-b-45) runs on dell2 under CTO half AMENDMENT 1 @1f0b2d2654; no new ruling. **`~K2`'s IRPT_CUSTDY E3 "BD Taildrop" gate is ruled superseded where its content is the BD session or the pull's output; anything else gets named back.** | broker, to `~K2` |
| MSTR 1257: step C (resource-policy changes) signed, NOT applied | Relayed to the 9 dell2 COOs (msgs 1262-1270, 9 DELIVERED / 0 QUEUED / 0 REFUSED). Policy changes stay refused until the applied time. **Changes to a firm bucket, the state bucket, a key another box uses or the shared assets bucket go to the laptop first; all others are reported after.** | broker |
| MSTR 1244: the laptop agrees not to apply `mail_pull` until `~T2`'s ledger closes | Acked; the ask is `~T2`'s. | broker |

## Acts only Andrew can do

- **The F1 retry**, which is release 1's after-read 5. It needs his own sign-in, per the IRPT_YCHARTS_GENERATE_RELEASE1 half @d2d2859a2a
  ("his login or MFA code", SKILL Step 1).
- Others unchanged from tick 19.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.
