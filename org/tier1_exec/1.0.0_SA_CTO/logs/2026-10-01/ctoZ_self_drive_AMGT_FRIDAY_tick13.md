# /self-drive AMGT_FRIDAY -- tick 13, `1.0.0_SA_CTO~Z`, 2026-10-01 15:46Z-15:56Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`.
**Placement:** `CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md`. **state: ARMED.**

## Scope state (measured at 15:46Z)

- **Projects (5 of 5 `active`, 0 `complete`):**
  - AMGT_CORPUS: the Friday face is complete; idle until the freeze.
  - AMGT_RESAPP: the Friday feed is complete (r60); idle.
  - DSGN_AMGTV1: round 21 (AV-y-1, the tooltip) is drained to portal DEV `9ccab761`, and the walk is pending.
  - AMGT_HARVST: round 35 is issued (`33bace02e0`, ah-1/2/3).
  - ETFS_RIVALS: round 4, with d-5 running.
- **Inbox:** 0 unread after this tick. Read and acked: 27926, 27930, 27933.
- **Push state (ls-remote):** origin CLOUD `0abf99fcd4`. Origin portal DEV has moved to `2bb367ef`: 13 laptop COO~D FAST commits (DSGN_IRPTV1) landed under that seat's lease. Local DEV is 41 ahead and 13 behind. `git merge-tree` returns rc=0, and 0 files are changed on both sides (31 on origin, 30 local). Nothing has been pushed from site Z.
- **Completion test:** NOT DONE. 0 of 5 are complete; all 5 are REACHABLE.

## Calls closed

| call | ruling | why |
|---|---|---|
| COO~D 27926: FWD-13's text says the tooltip "carries the mnemonic", but ruling 27914 takes the code off the face | **The reconciliation is ACCEPTED; no addendum.** The mnemonic stays in `data-mnemonic` verbatim, and the face shows the label, definition and full value. The close walk adds one Model-tab figure, because FigureTooltip is shared with CORPUS's face. | The DONE WHEN text and the ACCEPT traceability both still hold, so the CVO half stays closed. |
| MSTR~Z 27930: no seat claims the 14:01Z `inf-etf-ownership-daily` invokes | **CLOSED UNATTRIBUTED, harmless.** CloudTrail at 13:55-14:10Z shows only Lambda's AssumeRole at 14:01:24Z. Invoke is a data event that this trail does not log, so that instrument cannot name the caller. | The writes are the function's own keys, and the 09-28 slice is already held. A chase would not change the demo. |
| COO~D 27933: move 5174 to `9ccab761` | **DONE.** The walk tree is at merge `aa53016b`, diff against the target is 0 lines, and the server returns HTTP 200. | The walk is the round-21 close. |
| The HARVST r34 ruling 4 requires gold rebuild #3 before 22:00Z, but none of round 35's orders carries it | Asked COO~H for the run time (target 20:30Z or earlier) and the census commit. It runs under the signed CTO half NEVER_WIDEN_ROUND32_GOLD_REBUILD. | The walk reads the newest gold. |

## Acts only Andrew can do

1. **Push portal DEV and CLOUD, then promote to PROD** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word). The leg is a pull-merge of origin DEV `2bb367ef`, then the push; it is never a rebase. The promote will also carry the 13 laptop DSGN_IRPTV1 commits.
2. All other items are unchanged from tick 10.

## Compiler Tools

`git ls-remote`, `git merge-tree --write-tree`, `.tools/aws cloudtrail lookup-events`, `curl` (5174), broker `send_message`/`ack_messages`.
