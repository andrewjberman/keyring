# ANDREW_DIRECT 2026-10-08 ~16:1xZ -- assess NFRA_CMTQUE as the GitOps long-term solution path

**Channel:** laptop terminal, to `4.0.0_SA_CRO~A`, in the GitOps session.
**Recorded by:** `4.0.0_SA_CRO~A`, same turn.

## Andrew's words, verbatim

> "Look into CMTQUE, we need to assess the long-term solution path:"

He pasted this beside it, verbatim:

> 1. Git congestion (shared branch, 60+ agents)
> - Quick:
>   - The box manager merges in a separate copy of the repo, so other agents keep committing during the 15-45 minute merge.
>   - Stop the commit lock from being taken away from an agent still holding it after 60 seconds, and log every wait.
>   - Turn on git's untracked-file cache, which roughly halves git status time.
>   - Merge files that only get new rows added (surprise channels) by keeping both sides, so they stop causing conflicts.
> - Long-term:
>   - Agents never wait on each other to commit, possibly by reviving the commit queue parked in July.
>   - Every box works from current trunk.
>   - A measured answer per box to "is git why this box is slow?"
>   - Files several boxes add to are designed so they cannot conflict.
>   - Your decision on the branch model: one trunk, or per-box or per-project branches, with the cost of each written out.

(The pasted text renders an en dash in "15-45"; it is written here as an ASCII hyphen.)

## Reading

The ask is a research assessment of NFRA_CMTQUE, the commit queue parked on 2026-07-14, as the long-term path for the
long-term items above. It is not an order to revive, build or cut over anything. Scope is not widened here.
