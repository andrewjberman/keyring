# PRODUCT LANE -- status

<!--
/closer STATUS template. Owner: the implementing seat. Home: its base role's deliverables/PRODUCT_LANE/STATUS.md.
OVERWRITE THIS FILE IN PLACE at each meaningful change and before every handoff. It is the CURRENT STATE, not a
journal: no timestamped entries, no history. Git history is the journal. Target: about 5 KB.
Worked example: org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/STATUS.md
Replace every CAPS placeholder. Delete this comment before committing.
-->

Seat `SERIAL` (CLAUDE | CODEX). Contract CONTRACT_PATH version V. Reviewer `CVO_SERIAL`.
As of YYYY-MM-DDTHH:MMZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | BRANCH at `../WORKTREE` |
| Workspace candidate pin | COMMIT |
| Portal candidate pin | COMMIT or n/a |
| Deployed artifact pin | NAME digest DIGEST, or NOT DEPLOYED |
| Push state | LOCAL / on origin @COMMIT (ls-remote read HH:MMZ) |

## Live thread

State: NOT LIVE | LIVE AT HOP N | LIVE END TO END. Last trace: PATH@COMMIT, or none. First failing hop: N. A -> B.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| P1 | NOT STARTED / OFFLINE ONLY / CANDIDATE @PIN / CVO PASS / CVO FAIL | path@commit |
| S1 | ... | ... |

Offline-only work grades nothing until the live thread is live.

## Write claims

Exact files or functions this seat is editing now, including any claim inside another owner's row (with that owner's
agreement): `path`, `path::function`.

## Next proof

The ONE next thing this seat will prove, and how (the trace or test that will show it).

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| WHAT | SERIAL | S1 @ PIN | CONSUMED / AWAITED / BLOCKED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|

## Limits

What is not proven, not deployed, not exercised live, and which reserved gates (egress, deploy, provisioning) are
still ahead. No product ID is PASS until the CVO says so on a pinned candidate.
