# /self-drive AMGT_RESAPP -- re-arm ticks 7-8 (1.0.0_SA_CTO~Z)

**State:** ARMED, cron `5f951462`. **Why this log:** a driver act (a routed finding) and a correction to the tick-6 log.

## Tick 7

Quiet. No AMGT commits in 35 minutes; the five first-issuance workers had written files within three minutes of the read.

## Tick 8

**Moving:** worker commits `25de748042` (rk-21), `c91d424de8` / `c9816ba669` (rk-28), `2577f1db86` (rk-19 adapter, wip).
Rows filed by others: `Z-S152` (`3.0.0_SA_CVO~Z`, `2f3840fc21`: round 13 executes in pre-re-cut worktrees, chain CK written twice)
and `Z-S153` (`4.0.0_SA_CRO~Z`, `9da4e113f9`: the 15 round-13 orders carry no `<status>` tag). Both INERT, both owned by the issuer.

**Finding, measured at 16:00Z and routed (msg 23541 to `2.0.0_SA_COO~Z`, 23542 to `3.0.0_SA_CVO~Z`):** on THREE orders, two
workers write the same files at once. The first worker sits in the first-issuance worktree (`Temp/wk-amgt-13-NN`, base
`da2c3c479a`), the second in the re-cut worktree (`.claude/worktrees/wk-amgt-13-NN-*`, base `67168eba8c`).

| order | first-issuance worktree | re-cut worktree |
|---|---|---|
| rk-19 producer | `13-26`, last write 15:36Z | `13-26-fpA`, last write 15:49Z |
| rk-21 identity | `13-28`, committed `25de748042`, last write 15:53Z | `13-28-id`, last write 15:52Z |
| rk-28 checker | `13-30`, committed `c9816ba669` | `13-30-ck`, committed `e56b59fa22` 15:56Z, 52 dirty |

Not duplicated at this read: rk-19 adapter (`27-chainB` clean), rk-30 producer (`29-sp` clean), `31-portal`, `33-fpB`. Which
copy survives is the issuer's call and is not ruled here.

## CORRECTION to the tick-6 log (`8c2e506522`)

Tick 6 said the post-spawn face changes "cannot misroute work", because they were queue order only. **The diff was right; the
conclusion was too narrow.** It checked what changed in the faces the running workers held. It did not check whether the re-cut
spawned SECOND workers onto the same orders while the first ones kept running, and it did: at 16:00Z three orders have two live
writers. The domain was the running workers' faces, and the population was every worktree on those orders.

## Scope state

AMGT_RESAPP active / EXECUTING. Calls in scope: 0. RESERVED at Andrew: CARD 5; FWD-2 consumer cadence; FWD-14 list owner;
collection for FWD-4/FWD-11. Completion test: NOT DONE.

## Compiler Tools

git log; git worktree list --porcelain; per-worktree git status + file mtimes; broker get_agent_status, send_message.

Push state: LOCAL on SITEZ.
