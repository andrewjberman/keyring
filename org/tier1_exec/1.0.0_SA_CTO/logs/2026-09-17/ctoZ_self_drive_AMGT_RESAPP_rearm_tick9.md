# /self-drive AMGT_RESAPP -- re-arm tick 9 (1.0.0_SA_CTO~Z)

**State:** ARMED, cron `5f951462`. **Why this log:** a correction to the tick-8 log, owed and promised.

## CORRECTION to the tick-8 log (`178ae271ff`), from `3.0.0_SA_CVO~Z` msg 23546

The tick-8 rk-28 row was WRONG. `.claude/worktrees/wk-amgt-13-30-ck` had already been drained and removed. Its directory was an
empty husk, so `git -C` into it read the SHARED TREE ("e56b59fa22, 52 dirty"). In fact the RE-CUT copy `c9816ba669` merged to
SITEZ at `e56b59fa22` (15:55Z). What stays open for rk-28 is the undrained first-issuance branch `wk-amgt-13-30` @`c91d424de8`.
Every read this tick prints `rev-parse --show-toplevel` equal to the worktree path (11 of 11 match).

## Tick 9 read, 16:23Z (last file write per worktree, toplevel verified)

| order | first-issuance worktree | re-cut worktree |
|---|---|---|
| rk-19 producer | `13-26` @`9a8c79df9b`, 16:20Z | `13-26-fpA`, 16:23Z |
| rk-19 adapter | `13-27` @`2577f1db86`, 15:43Z | `13-27-chainB`, 16:19Z |
| rk-21 identity | `13-28` @`0169c3667e`, 15:56Z | `13-28-id`, 16:22Z |
| rk-30 producer | `13-29` @`7e143af81d`, 16:13Z | `13-29-sp`, 16:05Z |
| rk-28 checker | `13-30` @`c91d424de8`, 15:12Z | drained @`e56b59fa22` |

**Four orders still have writers in both copies inside the last hour.** The issuer has already named the re-cut canonical
(`2.0.0_SA_COO~Z` row `Z-S154` @`2f60a07edc`). It records that it cannot TaskStop the first-issuance workers and will not
continue them past their current order. So this is a known cost with a ruling on which copy survives, not a stalled owing
seat, and it is not routed to `0.0.0_AB_MSTR~Z`: that seat cannot stop another session's subagents either.

## Scope state

AMGT_RESAPP active / EXECUTING. Calls in scope: 0. RESERVED at Andrew: CARD 5; FWD-2 consumer cadence; FWD-14 list owner;
collection for FWD-4/FWD-11. Completion test: NOT DONE.

## Compiler Tools

git log; git worktree list --porcelain with a per-worktree `rev-parse --show-toplevel` equality check; per-worktree status +
file mtimes; broker check_inbox.

Push state: LOCAL on SITEZ.
