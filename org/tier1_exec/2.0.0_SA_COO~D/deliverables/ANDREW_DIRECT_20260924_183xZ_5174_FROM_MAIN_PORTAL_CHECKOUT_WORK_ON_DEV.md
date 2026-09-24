# ANDREW-DIRECT 2026-09-24 ~18:3xZ -- 5174 from the main portal checkout; work on DEV

Channel: the `2.0.0_SA_COO~D` terminal, mid-turn, during DSGN_IRPTV1 FAST item 1 (row DSGN_IRPTV1-S6).
Context: this seat had served `localhost:5174` from its own portal worktree `C:/tmp/dsgn-irptv1-fast`.

Verbatim:

> You need to build localhost:5174 from the actual main portal checkout, otherwise it misses gitignored local dev
> config and I can't smoke things. I already parsed out all frontend work on this box so that it only goes to you and
> no other projects should be interfering with the files youre touching. I need your work to be on the main DEV branch
> and when you build it build it in the standard places so that i can smoke at wwill

What it binds (this seat only; no other seat's work changes):
- `localhost:5174` is served from `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal` (the main checkout), branch DEV.
- This seat's frontend work is committed on DEV in that checkout and pushed to origin DEV under the FAST lease; no
  side worktree for the build.
