# /self-drive laptop directives -- tick 15 (2026-10-07 21:3xZ to 22:3xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`.
**Cadence:** 60m, cron `77f028d5`. **paired_with:** solo. **state: ARMED**. Covers the acts since the tick 14 log (author time by
`git log`: 2026-10-07T16:46:56 -04:00) and the cron's fifteenth fire.

## Measurements

- Trunk (fetch, 21:33Z): origin CLOUD `01090722e8`; the shared laptop tree 11 ahead, 673 behind. Later reads by other seats:
  `2e2a71aa78`.
- Sequence: no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 3 of 3 COO lanes (`~C`, `~G`, `~R`): AT CAP.
- Inbox: 0 unread files at 21:33Z; ten messages arrived during the tick, all read and acked.
- Active commitments, last 24 hours: 1 line in 1 of 69 ledgers (this seat's, tick 11).
- Laptop memory: 6.1 GB free at 21:35Z, 5.8 GB at 22:20Z, of 31.7 GB.
- `cot-rebalancer-runner-daily` target input, read at 21:34Z and 22:20Z: `{"mode":"pull","induce":"auth-lapse"}`.
- Three deploy lanes ended with no kill record, by `0.0.0_AB_MSTR`'s read of the process table at 22:06Z (msg 106602):
  `0.7.0_AE_CloudOps~E`, `~F`, `~S`. Cause not known. `~S` was respawned at 22:11Z for the 23:00Z read.

## Andrew-direct words this tick

| Where | Words | Carrier |
|---|---|---|
| this terminal, ~20:5xZ | close ADVI_INSURE and ADVI_49F | record + both rows @d5da993e5e |
| `2.0.0_SA_COO~C`, ~21:1xZ | that seat makes sure the seat-roles demands are met | its record @0faf18f318 |
| dell2, ~21:1xZ | "go with your rec": two portal candidates to DEV | landed, DEV `d1b21c970c` (MSTR's read) |
| `2.0.0_SA_COO~R`, ~21:4xZ | inbound for both Teams and Outlook; an `andrew_voice.md` | its record @4f53112d76; PRD v0.19 @6a24dd7db4 |

## Calls ruled (the driver's own REC, each)

| # | Call | Ruling | Carrier |
|---|---|---|---|
| 1 | Who issues the seat-roles work (106582) | `~C` issues SEATS, `~R` issues INBOUND; this seat's earlier scope to `~R` narrowed | msgs 106584, 106585 |
| 2 | Where the voice file enters (106595) | FWD-26 of NFRA_CTLPLN, workstream INBOUND; C-SEATS clause 10 | PRD v0.19 @6a24dd7db4 |
| 3 | dell2's run (A), the offline generate suite (106592, 106596) | run by this seat from a clean checkout of `1b5afe6a49`: 431 passed, 30 skipped, 32 subtests passed, offline_rc=0 | @3f344dc917 |
| 4 | dell2's run (B), a test pinned to three package versions | cannot run on the laptop today (it carries pandas 2.3.3, numpy 2.4.2, pyarrow 18.1.0); waits on the kit | msg 22:27Z |
| 5 | dell2's Python 3.12 kit (106596) | to `~C`'s package route; dell2's own review accepted as clause 7's; versions from the served layer's build file | msg 22:27Z |
| 6 | The pace of dell1's vendor run (106598) | the second order stays queued as cut; a re-cut is its issuer's call | msg 22:26Z |
| 7 | Respawn `~F` (106602) | no, on memory; owners (2) and (3) carry the restore; dell1's issuer assigns the ledger legs after 06:20Z | msg 22:27Z |
| 8 | When `~I` and `~E` may be closed (106574) | `~I` once its two hashes are landed; `~E` moot, it is gone | msg 21:41Z |

## Open items this seat owns

- **Two facts about 49 Financial's gold chain**, left by the close of the two projects: whether the insurance stage still runs,
  and whether the 09:46Z trigger race still occurs. Asked of `0.7.0_AE_CloudOps~E` at 21:41Z; that lane ended before an answer.
  PARKED on the close record. Un-parks when a laptop deploy lane is free of an order.
- **The 06:17Z restore check**, as written in the tick 14 log. dell1 measured user Test active for its 06:11Z task (MSTR 106592).
- **L4-R:** PRD v0.19's ratified-text half is owed by `3.0.0_SA_CVO`.

## Acts only Andrew can do

- The Python 3.12 installer, elevated, on each Dell when delivered (C-INTAKE, his word: "I can run admin on the Dell boxes").
- One line to re-arm the first restore timer is moot: that lane is gone.
- The walk-through of the two Dell reports; the naming exception for MDPF_HEALGAP HG-t-2; LGIC_BLANKFIX's DONE WHEN lines.

## Completion test

NOT DONE, read from the register: 9 laptop directives of 15 live; 56 member projects: 5 complete, 14 closed, 3 merged, 34 active.
D10 has no member projects: UNMEASURABLE.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `sequence-check.py` | capacity | PASS | AT CAP |
| `directives-check.py --json` | the completion test | PASS | 56 projects |
| `pytest` + `run_offline_suite.py` in a detached worktree | dell2's run (A) | PASS | worktree removed after the copy |
| `safe-commit.sh` | four commits | PASS | |

- **What worked:** running a read-only test for another box directly, in a throwaway checkout, in the time one relay takes.
- **Gap found:** seats end without a kill record and the fabric learns of it from a process-table read an hour later.
