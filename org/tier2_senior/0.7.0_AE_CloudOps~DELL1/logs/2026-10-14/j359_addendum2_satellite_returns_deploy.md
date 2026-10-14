# J359 addendum 2: the satellites' trailing returns become the models' realized returns blended with GLD -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-14 (UTC; 20:07Z - 20:2xZ)
**Task Order:** ADHOC.j359-addendum2-satellite-returns-deploy (risk WORLD)
**Status:** COMPLETE
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Rebuild the `cot-satellites-characteristics-producer` function at `7337fdfa6d`, upload it with one `model_portfolio_benchmarks.json`
read grant, run it once as a dry run and once for real, and read the served `characteristics.json` back against the table, the
Bloomberg-sourced windows and the partial-sleeve windows. The clock bound the whole order: start by 20:15Z, nothing open at 21:00Z.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| build_package.py | --pin 7337fdfa6d, --out scratch | PASS | only the producer differs from the prior package; the sidecar again landed in the repo root |
| own graders and tools | plan per attribute and policy set difference; before and after prints; served read | PASS | the served-read tool FAILED the pre-deploy bytes with 14 failures first, as a negative control |
| safe-apply.sh | saved planfile, two targets | PASS | 20:12:08Z-20:13:16Z |
| deploy_ledger.py | open, close-leg x6, close | PASS | CLOSED 6 of 6 at 20:19Z |
| terraform fmt -check -diff (copies) | HEAD vs patched .tf | PASS | the same 20 pre-existing lines flagged both times |

**What worked:** the first leg's pattern carried over whole, so the second ran in 11 minutes from the ledger open to the close;
this time the registry row meant the naming gate did not refuse and no amendment was needed.
**What failed:** my pasted patch script put a literal byte into a Python string (a syntax error, fixed in one edit); a large
heredoc was rejected by the shell, so the proof instance was written with the file tool instead.
**Gap found:** the windows probe the order names, `J359_evidence/bbg_windows_probe.py`, is on `wk-remote-J359`, not on the
`wk-remote-J359b` branch the order points to, so I used my own equivalent over the same calls and said so.

## Work Completed

1. **GO 5826 and preconditions:** both halves read (COO hash equals the one named); the clock (52 minutes to 21:00Z); the pin on
   origin; 5 of 5 members equal the column; sentinels across 35 worktrees (the same two stale copies of CLOSED ledgers).
2. **Ledger** `j359-addendum2-satellite-returns-deploy-dell1-20261014` opened 20:08Z; before print, rollback copy by hash, the
   served key's bytes and VersionId, the drift table (DIFFERS only for the producer).
3. **D1:** the zip uploaded (`GR8XrwBv...`, base64 metadata); the patch committed (`95cc4963a9`); plan 0/2/0 graded; applied; read back; unscoped re-plan clean.
4. **D2 and D3:** dry run rc 0 and the served key unchanged; the one driven invoke 20:15:10Z, served key `Qh56dS_I...` at 20:15:50Z.
5. **Served read:** 0 failures; 72 of 72 cells; controls; 63 of 63 unchanged cells; tickers equal; GLD windows 0 of 8 moved under two comparisons; 0 of 72 partial-sleeve windows.
6. **Report** to `2.0.0_SA_COO~J1` with the request ids, the new LastModified and VersionId, the three raw values, the windows and the partial-sleeve result.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Started at 20:08Z, not waiting for the re-seat | the GO allowed a start by 20:15Z and the first leg took 23 minutes; 52 minutes remained |
| Compared the GLD windows under three rule commits, not two | the order names 102b2b29d3 as the deployed rule, but efb3f6550f was what ran until this act; both are printed |
| Gave the three read values raw as well as rounded | 3.012256 and 1.928472 round to the table's 3.01 and 1.93; the ledger should hold what the object says |

## Open Items

- The read through the scoped route is the issuer's; the portal deletion waits on Andrew's word. DT was not messaged.
- `box/dell1`'s producer file is behind the deployed package until the issuer lands it.
- `C:/tmp/j359b/` is the rollback set for this leg; `C:/tmp/j359/` (the first leg's) can go once this leg is accepted.
