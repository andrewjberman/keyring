# /self-drive ticks 4-5 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Ticks covered: 4 (23:43Z) and 5 (00:13Z). This log is written at the one-hour floor, plus rulings taken since tick 3.
  **state: ARMED**

## Scope at tick 5

| project | status | dep_stage | open TOs (t3 -> t5) |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 14/50 -> 11/50 |
| NFRA_OPALAI | active | EXECUTING | 11/31 -> 7/32 |
| NFRA_MCPORTAL | active | EXECUTING | 3/18 -> 3/18 |
| NFRA_MCPINDEX | active | EXECUTING | 3/64 -> 1/64 |

Open orders fell from 31 of 163 to 22 of 164. Inbox at tick 5: 0 unread. At tick 4 the one message was 26291, a
duplicate of 26290. Sequence flags: none.

## Calls closed on this seat's REC since tick 3 (no design or governance fork)

| call | ruling | carrier |
|---|---|---|
| NFRA_MCPINDEX closer candidate (obligation 8) | DECLINED. MX-r-4 is signed and only sequenced behind OA-r-1 on the same gateway base. On the re-cut, G-A is re-signed as a DELTA review of `git diff 2dedae93df <new-pin>`. | msg to ~MI 23:39Z |
| G-ACCT step 3, 2nd failure (the -Command quoting made the child echo the script) | OA-f-4 re-cut with -EncodedCommand. A row is filed on the stored-credential use (COO~AI self-disclosed: row Z-S41, files removed). | msg 26294; COO~AI @57f04d3a6f |
| G-ACCT step 3, 3rd failure (-EncodedCommand is about 1150 chars against CreateProcessWithLogonW's 1024 cap) | The arm scripts ship as FILES in the opal_ai provision folder (Opal_Agent: RX) and run via `-File`, never written into the writable state_dir. The AC3 self-test drops -Credential, so it is NOT a control for this path. The acceptance is MSTR~Z's real-credential step 3, plus a unit assert that the command line stays under 1024 characters. | msg 26297 |

## Standing

- NFRA_OPALAI OA-r-1 (gateway release) was deploying at 23:53Z, and NFRA_MCPINDEX MX-r-4 holds behind it.
- G-ACCT waits on the third OA-f-4 re-cut. Opal_Agent exists (no groups, logon proven), and steps 4-6 are not run.
- At Andrew: the setup-token sign-in and one MFA (steps 5-6); his `sub` (Part D step 7, which is G-SUB for MCPORTAL
  MP-a-2); and Alyssa posting Q1-Q3 for his speed test.

## Verdicts from CVO~O

0 pitched and 0 received.

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census (last `<status>` tag): 22 of 164 open.
- Runtime tick lines: `org/mcp/drive_ticks/1.0.0_SA_CTO~O.md` (gitignored), tick 4.
- The gap: none new.
