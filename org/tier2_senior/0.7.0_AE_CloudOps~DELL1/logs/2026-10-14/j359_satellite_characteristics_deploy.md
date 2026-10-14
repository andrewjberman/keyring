# J359: the satellite characteristics producer moves to the Models' method, and the served key is refreshed -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-14 (UTC; 18:38Z - 19:0xZ)
**Task Order:** ADHOC.j359-satellite-characteristics-deploy (risk WORLD)
**Status:** COMPLETE
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Rebuild the `cot-satellites-characteristics-producer` function at `efb3f6550f`, upload it to its artifact key with one
`registry.json` read grant, run it once as a dry run and once for real, and read the served
`platinum/satellites/characteristics.json` back against the spec table and the old-versus-new return windows. No portal promote.
The whole order had to finish well before tonight's 21:00Z restart.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| build_package.py | --pin efb3f6550f, --out scratch | PASS | 5 members equal the COO column; the sidecar lands in the CURRENT directory |
| own graders and tools | plan per attribute and policy set difference; before and after prints; served read | PASS | the served-read tool FAILED the old object with 40 failures first, as a negative control |
| safe-apply.sh | saved planfile, two targets | PASS | 18:50:16Z-18:51:25Z |
| deploy_ledger.py | open, close-leg x6, close | PASS | CLOSED 6 of 6 at 19:00:59Z |
| safe-commit.sh naming limb | the one-file cherry-pick of efb3f6550f | REFUSED | LGIC_ENFORCE DEC-6; no override; the issuer amended the order |
| terraform fmt -check -diff (copies) | HEAD vs patched .tf | PASS | the same 20 pre-existing lines flagged both times |

**What worked:** the issuer answered the naming refusal inside two minutes; building at the pair's own named pin kept the
deploy identity exactly what both halves signed. Running the served-read tool against the old object first showed it can
fail, so its pass on the new object means something.
**What failed:** the cherry-pick commit (refused, working tree restored); my first read of the positioning file (it is stored
gzipped with `ContentEncoding: gzip`, which boto3 does not undo); the builder dropped its sidecar at the repo root.
**Gap found:** a second scheduled invoker, the hourly reattempt rule, targets the function and the order names only the daily
one; read, timed around, and its 18:55:11Z fire on the new code logged SKIP-COMPLETE and wrote nothing.

## Work Completed

1. **GO 5688 and preconditions:** both halves read; the clock (139 minutes to 21:00Z); the producer at `efb3f6550f` on origin;
   5 of 5 members equal the column; sentinels across 34 worktrees (the two that name the producer are stale copies of CLOSED ledgers).
2. **Ledger** `j359-satellite-characteristics-deploy-dell1-20261014` opened 18:41Z; before print, the rollback copy by hash,
   the served key's bytes and VersionId, and the drift table (exactly the four members the pair names).
3. **The naming refusal and the amendment** (msgs 5690, 5695): built at `efb3f6550f` itself; only the `.tf` patch committed (`2182fe47ee`).
4. **D1:** the zip uploaded (`3yaAgYL1...`, base64 metadata, the form the module uses); plan 0/2/0 graded; applied; read back; unscoped re-plan clean.
5. **D2 and D3:** dry run rc 0 and the served key unchanged; the one driven invoke 18:56:26Z, served key `6z8c7qDD...` at 18:57:08Z.
6. **Served read:** 0 failures; 36 of 36 cells; controls; tickers 24 of 24; GLD windows 0 of 8 moved.
7. **Report** to `2.0.0_SA_COO~J1` with the amendment's fields (msg 5722): request id, new LastModified and VersionId, the three values.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Built at `efb3f6550f` instead of forcing the cherry-pick | the naming limb is not mine to waive; the issuer agreed and amended scope 2c |
| Held D3 until after the 18:55 reattempt | so the served key's write is attributable to the one driven invoke alone |
| Moved the unfiled "surprises" into declared exclusions | no hazard was armed and no row exists; listing them as surprises claimed something unfiled |

## Open Items

- The read through the scoped route and the Positioning Satellites mode is the issuer's (amendment 5722); no portal promote was touched.
- `box/dell1`'s producer file is behind the deployed package until the issuer lands `efb3f6550f` through the naming law.
- `C:/tmp/j359/` (prior zip, both served versions' bytes, the old sidecar, plans, invoke outputs) is kept as the rollback set.
