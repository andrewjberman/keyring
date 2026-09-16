# ANDREW-DIRECT 2026-09-14 ~17:0xZ -- remove the 16 finished worktrees to free disk

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** AskUserQuestion at this terminal, one card · **Recorded:** the same turn
it was given.

## VERBATIM -- the question and the option he chose

> Q: "C: is at 11 GB free and falling; COO~G has stopped creating worker worktrees until it's back over 10 GB. Your
> standing instruction keeps the Investor Reporting round 4-6 worktrees on disk. Which finished worktrees may I remove?
> Branches are kept in every option, so no commit is lost."
>
> **A: "Remove 16 finished (~22 GB) (Recommended)"** -- option text: "Investor Reporting rounds 4-5 plus FE-s-37, all
> drained (13 of 14: FE-s-32 stays because it holds one uncommitted file), and the 3 worktrees of the closed
> ETFS_GUARDRAIL. Plus the 720 MB temp-junk sweep. Round 6's live worktrees are untouched."

It answers `2.0.0_SA_COO~G` msg 96637 (C: at 9.6 GB free, under that lane's 10 GB line) and lifts, for these
worktrees only, his earlier standing instruction that every IRPT_FNTEND round-4/5/6 worktree pair under C:/tmp stays
standing (relayed by `2.0.0_SA_COO~F`, msg 96617).

## WHAT IT RULES, NO WIDER

Remove these 16 worktrees and their portal worktree pairs. **Branches are kept** in both repositories, so every commit
survives:

| set | worktrees | measured |
|---|---|---|
| IRPT_FNTEND round 4 | `C:/tmp/wk-irpt_fntend-4-1-fe-s-25`, `-4-2-fe-s-26`, `-4-3-fe-s-27`, `-4-4-fe-s-28`, `-4-5-fe-s-18` | 6,539 MB |
| IRPT_FNTEND round 5 | `C:/tmp/wk-irpt_fntend-5-1-fe-s-30`, `-5-1-fe-s-31`, `-5-2-fe-s-33`, `-5-3-fe-s-34`, `-5-4-fe-s-29`, `-5-4-fe-s-36`, `-5-5-fe-s-35` | 9,561 MB |
| IRPT_FNTEND round 6, drained | `C:/tmp/wk-irpt_fntend-6-4-fe-s-37` (drained @13a3e28b95) | 1,475 MB |
| ETFS_GUARDRAIL (closed) | `C:/tmp/wk-etfs-3-21`, `-3-30`, `-3-31` | 4,367 MB |

Plus the `/kill storage` sweep: allowlisted user-temp and stale Claude scratch only, 720 MB at the dry run.

NOT RULED, AND KEPT: `C:/tmp/wk-irpt_fntend-5-2-fe-s-32` (one uncommitted deliverable file), every live round-6
worktree (FE-s-38..41), every `2.0.0_SA_COO~G` LGIC_NAMING slot, every DSGN_REBRND worktree, the `krny/*` and
`staudt_layerD_*` trees, and `wk-irpt-2-2c` (IRPT_BCKEND round 2, not closed).

## BROADCAST

`2.0.0_SA_COO~F` (owner of the IRPT_FNTEND worktrees), `2.0.0_SA_COO~G` (the 10 GB line) and `1.0.0_SA_CTO`, with the
freed space once measured.
