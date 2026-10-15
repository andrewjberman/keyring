# /self-drive dell2-box tick 20 (2026-10-15 20:2xZ to 20:4xZ, 1.0.0_SA_CTO~DELL2)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`. This log covers
the time since tick 19 (@1448f111f1).

## Andrew's words this tick
- **~20:3xZ (@b0e7715227, outcomes @b6500c175c):** a252 template path; c02c drafted to the desktop; deletes 2106, 53cb and d8ae approved.
- **~20:4xZ:** "T-1 is the correct terminology, let's just stick to that" (PRD v0.16 @a4af0e5bba).

## Acts since tick 19
- **Signed and ruled:**
  - CTO halves: the Scope feed IAM spelling addendum @672b1fea08; reporting-gold revision 2 @d7e774e05d; R42 re-signed @d82fd93048 and
    as a surgical zip @dfac94827f; the exemption pair and split addendum 1 @a937b9931c.
  - Rulings: round-118 ADDENDA 5 and 6; the runner start @57b25f40de; the backfill by day events @f9483b5322; the benchmark SPY and
    BIL @77c0e9fde2; the 49F lost account @9fef489152; PRD v0.16 (no price-date input, T-1).
- **Analyses:** B-49F r133-137 @93b8070c65; B-IN r123 @6f2c5c3f2d; the ~P lanes @6ecc65bb86.
- **Open calls:**
  - cf2a, b238 and 08fd CLOSED on site Z's cross-adjudications;
  - 53cb, d8ae and a252 CLOSED on Andrew's word;
  - 4608 HELD for Andrew (stopping EC2).
- **Deletes:** 53cb and d8ae are done (19 folders). `C:\c\dev\wk-cotbkf-56` was kept, since it is dell1's ADVI_COTBKF.
- **2106 was REFUSED by IAM** (an explicit Deny on `s3:DeleteObjectVersion` for `cloudops-dell2-agent-user`). Nothing was deleted, and the
  commands are on Andrew's desktop.

## Open calls
5 open: 4 `act` (2106, c02c, e260, 4608 held) plus the J4 read.

## ACTS ONLY ANDREW CAN DO
- **2106:** run the six commands in `C:\Users\Test\Desktop\RUN_AS_ANDREW_open_call_2106_s3_deletes.txt` with his own credentials (his
  approval stands; the agent user is denied).
- **c02c:** send `C:\Users\Test\Desktop\DRAFT_Inflection_Orion_account_start_dates.txt`, or not. It is outward-facing.
- **4608:** stop EC2 `i-0ed5afded2ebd4ed4` (CLAUDE.md: stopping EC2). This is cost only, and the 11:32Z chain uses it anyway.
- **e260:** the Opal_Terminal key. His hold: "let's not discuss the Opal_Terminal key further i will handle it".
- **J4:** the PROD Ticket Center read with his staff login.

## Completion test
NOT DONE. IRPT_DASHBD, IRPT_BCKEND and IRPT_ANLREQ are EXECUTING.

state: ARMED

## Compiler Tools
open-calls.py list, close and hold; xadj.py open and show; `aws s3api list-object-versions` and `delete-object` (refused); PowerShell
Remove-Item with LinkType checks; safe-commit.sh; MCP send_message and ack_messages.
