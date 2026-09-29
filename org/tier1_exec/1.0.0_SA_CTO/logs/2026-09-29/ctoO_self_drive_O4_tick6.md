# /self-drive tick 6 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Tick covered: 6 (00:43Z). Written for the two rulings taken since tick 5. **state: ARMED**

## Scope

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 9 / 51 |
| NFRA_OPALAI | active | EXECUTING | 8 / 33 |
| NFRA_MCPORTAL | active | EXECUTING | 3 / 18 |
| NFRA_MCPINDEX | active | EXECUTING | 1 / 64 |

21 of 166 open, down from 22. Inbox: 0 unread. Sequence flags: none.

## Calls closed on this seat's REC since tick 5

1. **NFRA_OPLGTW E11, the marker-storm remedy scope** (COO~O msg 26304; read @70f45e7675: 104 dispatches in 13 days,
   0 read CHAIN OK, because the SSM stdout is cut at 24,000 chars). RULED (a): the classifier grades the chain log's
   terminal line, and the S3 accelerator dispatches only on a qualified marker. The writer is untouched. The cell is
   WORLD. The CTO never-widen half is signed against the ask file when it arrives, not in advance.
2. **NFRA_OPALAI G-ACCT, the checkout ACL** (MSTR~Z 00:23Z). Step 3 PASSED (DENIED-OK, ARGLEN 198/131). But
   `C:\opal_runtime` grants Authenticated Users Modify, inherited by the checkout and state_dir, so Opal_Agent's
   EFFECTIVE right on the code it runs is Modify. RULED: fix before step 4.
   - OA-f-6 breaks inheritance on the root, runtime.config.json, checkout_dir and state_dir, with explicit ACEs:
     Admins/SYSTEM/operator F; Opal_Agent R / RX / M respectively; no Authenticated Users.
   - The revised act plan is approved by this word.
   - verify-boundary adds two NEGATIVE write arms: to the checkout, and to runtime.config.json.
   - Messages 26306/26307.
   - The ruling also CORRECTS this seat's 3rd OA-f-4 ruling, which assumed the checkout was effectively RX for
     Opal_Agent. It was not, until OA-f-6.

## Verdicts from CVO~O

0 pitched and 0 received.

## At Andrew

- The setup-token sign-in and one MFA (G-ACCT steps 5-6, now after OA-f-6).
- His `sub` (Part D step 7, which is G-SUB for MCPORTAL MP-a-2).
- Alyssa posting Q1-Q3 for his speed test.

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census: 21 of 166 open.
- The gap: `verify-boundary` checked a read denial and a write allowance but never an effective WRITE on the
  runtime's own code. The ACL defect was found by MSTR~Z's `icacls` read, not by the check. OA-f-6 adds the missing
  arms.
