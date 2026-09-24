# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 17-19 (~00:0xZ-00:4xZ 2026-09-22)

Arming record: carrier `c9ccd9f4e3`. Cron: `46e545b7`. **State: ARMED.**

## Scope

| Item | Reading |
|---|---|
| Projects | 2, both `active` / EXECUTING |
| Sequence | no flags |
| COO lanes | 2 of 3 live |
| Inbox | 0 unread |
| Read and acked since tick 16 | 99329, 99331, 99337 (plus the round-9 slug message from `3.0.0_SA_CVO~B`, which carries no id) |

## Driver acts

### IRPT_BCKEND round-9 L10 analysis @`9d4052728b`

- **The analysis CORRECTS this seat's own rti-6 park ruling @`4a773b6ae3`.** That ruling said un-park condition (1) was MET because the capture tool was published. Publishing did not mean the tool was FIXED. CVO~B's slug @`a62b69f6d3` found two defects:
  - C-S153, grade R91-AC7 FAIL: a redirect hop through a foreign origin still writes a session and reports success.
  - C-S156: the runbook would run the OLD bytes on the host.
- **Condition (1) is amended.** It now requires ALL of:
  - (a) the redirect diagnostic passes;
  - (b) a single-difference regression passes, with a positive control;
  - (c) the runbook delivers the fixed bytes and verifies their hashes BEFORE any credential entry.
- **The ask to Andrew is RE-HELD.** Msg 99333-99335 went to `2.0.0_SA_COO~B`, `0.0.0_AB_MSTR` and `3.0.0_SA_CVO~B`.

### The ask to Andrew had already gone out

- `0.0.0_AB_MSTR` reports (msg 99337) that the ask had already reached Andrew, at ~23:40Z and ~23:55Z. MSTR sent a STOP at 00:16Z, by terminal and by mobile push.
- Measured by this seat on the EC2 plane:
  - host `i-0167fd745ad906a66` is `stopped`;
  - last transition: User initiated, 2026-09-21 18:00:31 GMT;
  - so the host was not started in the window, and no credential can have reached the defective tool on the host.

### Other items

- **ycharts HAR, received from Andrew as a file path.** I read its STRUCTURE only:
  - 211 entries, a login plus the dashboard shell;
  - the POST /account/login/ carries the username and password in plaintext;
  - 49 requests carry cookies and 15 carry Authorization headers.
  - Nothing was copied into the repo. Andrew was told to delete the file or keep it private, and was asked what it is for.
- **Andrew's /open-calls:** three cards.
  1. The capture step. This card is now superseded by the re-hold.
  2. The unit held in column B of the Sensitivity Analysis upload.
  3. Deletion of the break-glass role.

## State

- **IRPT_BCKEND:** round 10 was ISSUED @`6b4951fdcb`, following the corrected analysis. C-S154 metadata was fixed @`809b35f48d`.
- **IRPT_FNTEND:** round 11 was ISSUED @`730c75ee87`: nine cells, FE-s-65..73.
- **Owed next by this seat:**
  - the rti-1-successor never-widen CTO half, when a new capture-tool packet arrives;
  - the L4 principal CTO half;
  - both round analyses, when their slugs arrive.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

- `.tools/aws` (`ec2 describe-instances`)
- a python HAR structural profile, read-only and printing no values
- `sequence-check.py`
- `git log`
