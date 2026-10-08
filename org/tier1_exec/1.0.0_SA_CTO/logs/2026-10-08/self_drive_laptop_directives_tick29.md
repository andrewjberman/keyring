# /self-drive laptop directives -- tick 29 (2026-10-08 10:4xZ to 11:3xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`.
**Cadence:** 60m, cron `77f028d5`. **paired_with:** solo. **state: ARMED**. Since the tick 28 log (@850065bc45).

## Measurements (11:32Z)

- Trunk (ls-remote): origin CLOUD `45493f4afb`; local `7ea00153b1`.
- Sequence: no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 3 of 3 COO lanes: AT CAP.
- Inbox: 0 unread; every message through 106898 read and acked. Disk C: 38 GB free of 238 GB.

## The identity root, from the applier's own commits

| Step | State |
|---|---|
| A, the Denies first | APPLIED 09:19:39Z; EXERCISED by dell2 at ~11:05Z (its own `ssm get-parameter` succeeds, msg 106891); proof instance now VALID after the issuer's reference fix (@0f3dde670b) |
| B, the 66-secret read and the old Deny removed | ledger entry OPENED 11:30Z (@7ea00153b1); not yet reported applied |
| C, the Allow | half not yet written |

dell2's `2.0.0_SA_COO~Y2` is running its own release-1 apply of the report generator on dell2; no result yet.

## Calls ruled (the driver's own REC, each)

| # | Call | Ruling | Carrier |
|---|---|---|---|
| 1 | Does branch B of TO-HG-d3 wait on step B (106884) | no; this seat's line was wrong. It only invokes the function. Measured live after step A: dell1 allowed `lambda:InvokeFunction` on `cot-rebalancer-runner` (APPLIED plane; no control arm derived) | msg 10:53Z |
| 2 | The two facts left by the close of ADVI_INSURE and ADVI_49F (106887) | measured by `0.7.0_AE_CloudOps~E`: the insurance stage runs daily (18 stages); zero of 4 recent 09:4xZ logs abort. Appended to the close record | @179d274470 |
| 3 | Six serials read DEAD with open orders (106888, 106892, 106898) | none respawned; two are alive on other boxes and the tool cannot see them; one re-addressed by dell1; three parked. The tool prints ELSEWHERE for a serial placed on another box: a cell | msgs 11:03Z, 11:1xZ |
| 4 | The actor of the 06:08:46Z restore (106895) | the ledger says what is known: laptop credential, in window, not among the fabric's seats, operator's terminal inferred and unconfirmed | msg 11:13Z |

## MDPF_HEALGAP TO-HG-d3 (dell1's project; the order held by laptop `0.7.0_AE_CloudOps~F`)

Induced: three invokes 06:00:42Z to 06:03:46Z, each failing on the planted auth lapse, nothing written. Restored 06:08:46Z.
A targeted plan at 11:06Z reads no changes. Legs L2 and L3 closed. Owed: the 11:45Z heal read; AC1, AC2 and condition 4
after 13:00Z.

## Owed

- By this seat: the CTO half for step C; the LGIC_BLANKFIX round-5 analysis on the slug.
- To this seat: step B's applied time; dell2's release-1 result; the Teams handler's first-event read; site Z's merge.
- OPEN, owned by this seat to place: whether 49 Financial's insurance stage keeps running (put to Andrew); the trigger race,
  absent in four runs and of unknown state.

## Acts only Andrew can do

- Whether the insurance stage stays in 49 Financial's chain. His word at site Z for its merge. Whether he made the 06:08:46Z
  restore. Item 5, the deploy limit. The width of items 1 and 3. Python 3.12 on dell1. "Build it" for the cross-box map.
  Item 4 (IAM).

## Completion test

NOT DONE, read from the register at tick 28 and not re-read: 56 member projects, 5 complete. D10 UNMEASURABLE.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `comp-iam simulate` | dell1's invoke of the runner, live | PASS | allowed; APPLIED, not EXERCISED |
| `git log --author` on the deploy seat | applied states | PASS | step B's entry found open |
| `safe-commit.sh` | one record append, this log | PASS | |

- **What worked:** an issuer on another box correcting this seat's wrong line with its own measurement within minutes.
- **Gap found:** a liveness tool that reads one box and speaks for four.
