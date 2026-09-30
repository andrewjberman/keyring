# ANDREW-DIRECT 2026-09-29 ~22:0xZ -- COO edict: wipe a closed agent's committed worktree; relaunch CTO and COO~P

**Channel:** Andrew at the `0.0.0_AB_MSTR` terminal (laptop), during a `/cleanup` disk check (C: 18.3 GB free,
falling ~2 GB/h since 16:00Z; RAM 4.5 GB free of 31.7 GB).

## Verbatim

> I suspect we are choking this drive out, the COOs need an edict that as they have agents close out, those worktrees
> (if all committed) also need to be wiped. WE can't keep getting in these scenarios where we find we have 2gb left
> on C drive. I also need you to bring CTO back online because they and COO~P crashed on what i presume was a memory
> overload if not disk. Bring them back and brief them on status.

## The edict, as MSTR relays it (scope: COO lanes; the wording above governs)

When a COO closes out an agent (a worker drains, or a seat ends its round), the COO removes that agent's worktree
and branch in the same act, provided everything in it is committed and landed:
- `git -C <wt> status --porcelain` is empty;
- the branch is an ancestor of CLOUD, or its commits are drained.

Removal is `git worktree remove <path>` (never `--force`, never a raw `rm`), then `git branch -d <branch>`. A worktree
with uncommitted or unlanded work is NOT wiped; the COO drains it or names why it stays.

MSTR relays it to every live COO lane. The law text in CLAUDE.md, if any, is 1.0.0_SA_CTO's to land. MSTR does not
edit CLAUDE.md.

## Relaunch

`1.0.0_SA_CTO` and `2.0.0_SA_COO~P`, spawned by MSTR, each briefed by
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAUNCH_BRIEF_20260929_220xZ_CTO_COO_P.md`.

Other seats also down at 21:59Z (4.0.0_SA_CRO base, 0.4.0_DS_ClientPlatform~E, 0.2.0_DT_PortfolioAnalytics~P,
0.6.2_AE_PartnerETL~S) are NOT named in the word and are not relaunched by it.
