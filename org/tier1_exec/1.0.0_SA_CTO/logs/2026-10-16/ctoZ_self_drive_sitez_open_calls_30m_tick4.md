# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 2-4 (2026-10-16 ~03:29Z to 04:2xZ)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Calls ruled, routed or closed since tick 1

| call / message | ruling or act | record |
|---|---|---|
| COO~O 34688: v3.13 item 2 assumed `served/*` | my error: "served" is the catalog layer; the rows sit under `json/*`, already granted. Item 2 WITHDRAWN; no IAM | @7656f484ab |
| XB-ae75 (laptop COO~C): a package absent from requirements.txt? | NONE, acked on file and bus | bus ae015f0d |
| COO~O 34697: OG-cl-7 AC2 naming-gate refusals | `name_rulings.json` `none_owed` rows; `orion/4698` deleted; no new class, no R20 | @d97ea3ae82 |
| MI2 34698: ai_classified_securities | out as `provenance_input`; the etf-classifications table is OPLGTW's named next increment | @d97ea3ae82 |
| sitez-...-f643: integration channels on /gateway | XA-7afb RULED (a) KEEP by the laptop cluster lead; **CLOSED** | XA file synced |
| Andrew ~03:4xZ "all recs approved" (relay 34706) | 3b41 **CLOSED** ruled-by andrew, into def4 | ANDREW_DIRECT_20261016_034xZ_ALL_19_CALLS_RECS_APPROVED_C02C_POSTPONED.md |
| COO~O 34707: naming-gate.py never reads name_rulings.json | call sitez-...-115c; XA-28da RULED (a) fix the gate (site Z cell under COO~O, scope the gate plus selftest, no override); **CLOSED**; MSTR~Z parked the four-box announcement on the merge hash | @0a775f4f7b submission |
| CVO~Z 34708: MCPORTAL PF round-3 slug | round-N analysis: ruling 4 WITHDRAWN (the writer history holds no grants); R3 = a raw scan under the CloudOps credential vs the People view | @0a775f4f7b |
| MI2 34711: last 2 RESEARCH rows | ratified out with reopen conditions | @e4a5d0d18c |

## Scope state

Open calls on site Z: **6**, all acts only Andrew can do, already escalated with their citations:
- a519: one Teams message from his own account;
- 21c5, f0d2, 8ed7, 21d9: one MC Portal sitting, including his login as Opal Bloomberg;
- def4: one sitting with Alyssa.

Owned elsewhere:
- **The 22:00Z gateway finish:** OG-ap-23's gate fix (COO~O cell), ap-24 Phase B (COO~O half owed), MX-r-15 (MI) and the
  MCPORTAL S1 served read.
- **The MCPORTAL PF round-4 drain packet** (COO~MP, b6df0af57c) is with the CVO for L8.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| open-calls.py | add 115c; close f643, 115c, 3b41 | 3 CLOSED once the ruling files synced (box-sync @5a5c3b48ee) |
| xadj.py | open XA-7afb and XA-28da; show | both ruled by the laptop within about 5 minutes |
| crossbox-call.py + agentbus-sqs.sh | ack XB-ae75 and answer NONE | ACKED; bus SENT |

- **What failed:** I wrote an IAM claim into a PRD from a grep for a catalog layer name. The rows' `prefix` field was the
  right instrument, and the COO caught it.
- **Gap:** closing a cross-box row waits on box-sync carrying the ruling file (about 30 minutes here). It is harmless,
  but the scan re-nudges meanwhile.
