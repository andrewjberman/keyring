# ANDREW-DIRECT 2026-09-30 ~02:37Z -- remove the round-49 and round-50 worker checkouts

**Channel:** Andrew, in the 2.0.0_SA_COO~Z Claude Code session (site Z). **Recorded by:** 2.0.0_SA_COO~Z, same turn.

## Verbatim

> "you have my permission"

## What it answers (scope, verbatim from the ask it replies to)

The seat's last message asked for his go on "deleting the local worker copies from rounds 49 and 50 (`C:/tmp/r49-173` to `-175`
and `C:/tmp/r50-176` to `-179`). Their branches are all merged." That is the whole scope: seven checkouts. Branches are kept.
Not in scope (not named in that ask): `C:/tmp/ae-a-vv4` and the other checkouts on the post-crash disposal lists.

## Pre-removal measurement (02:37Z)

| checkout | branch | HEAD | merged into CLOUD | uncommitted (excl. portal gitlink, .scratch) | staged |
|---|---|---|---|---|---|
| C:/tmp/r49-173 | wk-AMGT_RESAPP-173 | 6168c710fe | yes | 0 | 0 |
| C:/tmp/r49-174 | wk-AMGT_RESAPP-174 | 1a794837f0 | yes | 0 | 0 |
| C:/tmp/r49-175 | wk-AMGT_RESAPP-175 | 9aa98b4330 | yes | 0 | 0 |
| C:/tmp/r50-176 | wk-AMGT_RESAPP-176 | 64fbda07dd | yes | 0 | 0 |
| C:/tmp/r50-177 | wk-AMGT_RESAPP-177 | 57c2deac82 | yes | 0 | 0 |
| C:/tmp/r50-178 | wk-AMGT_RESAPP-178 | 3980017af6 | yes | 0 | 0 |
| C:/tmp/r50-179 | wk-AMGT_RESAPP-179 | 8134f03726 | yes | 0 | 0 |

Mechanism: `.tools/wk-provision.sh remove <path>` (tears down the nested portal worktree too). Result appended below after the act.

## Result

All seven removed with `.tools/wk-provision.sh remove` (rc 0 each, nested portal worktrees torn down), verified after the act: `git worktree list` lists 0 of the seven; 7 of 7 directories absent on disk; 7 of 7 branches `wk-AMGT_RESAPP-173..179` kept. Linked worktrees on this device now 36 (including the main tree).
