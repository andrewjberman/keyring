# 2.0.0_SA_COO~E -- addendum 2026-09-14 03:10Z -> 05:25Z: two Andrew-direct words recorded; call 3's gate change landed; rows S6..S9; the lane is ready for Andrew's manual close

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT

This addendum covers the window after `session_close_2215-0245Z~E.md` (@251a4b4eba).

## Work

- **ANDREW-DIRECT ~03:xxZ** -- *"none of the legacy channels are quiet because they are the active channels for the
  firms now ..."* Recorded verbatim @d5975c9cda and broadcast (96479-96482; 4.0.0_SA_CRO~D QUEUED, not live).
  - It withdrew this lane's "cot is not quiet" framing from 96476.
  - 1.0.0_SA_CTO read it with no conflict (96486 @9819855eda): the window is 45 consecutive days after each
    firm's cutover, and the pre-cutover log is the census of readers to repoint.
  - A project memory was saved so the misframing does not recur.
- **/next-steps, then /open-calls** -- 4 options and 3 calls, in-chat only.
- **ANDREW-DIRECT ~04:xxZ** -- *"recs approved, then next steps approved leading into the close down of this lane,
  which i will handle manually."* Recorded @675eeec895, with the narrow reading stated, and broadcast
  (96499-96502, all DELIVERED).
  - **Call 1** (remove stale worktrees that pass a re-measure): a read-only census of 31 linked worktrees, and
    **0 passed**. Each exposed worktree holds tracked changes, an untracked `.scratch/`, a tip not in CLOUD, or an
    open task order (wk-irpt_fntend-5-4-fe-s-29 is live in round 5). **Nothing was removed.** Row S3's worktree
    exposure stands with the worktrees' owners.
  - **Call 2:** no gate built.
  - **Call 3:** `org/mcp/cvo_send_guard.py` now accepts a cited task-order PATH under the same `<issued_to>` test
    @ee9a6cf257. The commit-gate was clean.
  - **Option 1:** rows ADVI_FIRMBKTS-S6..S9 @5d7baa0793. The row gate graded the 4 new rows OK.

## Compiler Tools

| tool / invocation | result | class |
|---|---|---|
| `python org/mcp/cvo_send_guard.py --self-test`, BEFORE the edit | 0 failed of 44 | PASS (baseline) |
| the same, after the first cut | 1 failed of 49: the path-removed difference arm ADMITTED | FAIL (mine; see below) |
| the same, after the fix | 0 failed of 49 | PASS |
| `.tools/safe-commit.sh` commit-gate on cvo_send_guard.py (py_compile, ds-precommit, ruff) | "pre-commit gate clean for 1 of 1 file(s)" | PASS |
| worktree census (scratch script over `git worktree list --porcelain` + status + is-ancestor + open-TO scan) | 0 of 31 candidates; 147 non-terminal TO files scanned | PASS |
| surprise-row-gate on S6..S9 | 4 new rows OK; corpus 0 new failures | PASS |

**What failed:** my first self-test pair was VACUOUS. The difference arm's body ("Flip ... begin") carried no act
marker, so the gate admitted it as act-free, and the admitted arm passed for the same reason rather than because of
the path. The difference control caught it. Both bodies now carry a real act ("Apply S3 NOW."). **Lesson:** a pair
that tests an ADMISSION must first make the refusal reachable.

**Gap found:** the path form takes effect only at each MCP session's next server load and the broker's next
restart, so it is APPLIED on the record and not yet EXERCISED on a live send.

## Blockers

None. The lane's approved work is done; its close is Andrew's, by hand.

## Current State

- The order and its validation are unchanged (@231cd62ec5).
- The gate is at `org/mcp/cvo_send_guard.py` @ee9a6cf257: `TO_PATH_CITE_RE`, the path branch in
  `cited_orders_for`, and 5 self-test arms.
- The ADVI_FIRMBKTS surprise channel holds S1..S9; S6 is DISMISSED_WITH_REASON and the rest are
  UNDER_INVESTIGATION.
- **Push (ls-remote 05:25Z):** 50823af561, 231cd62ec5, 251a4b4eba, d5975c9cda, 675eeec895, ee9a6cf257 and
  5d7baa0793 are all LOCAL; origin/CLOUD is 37931439cf.

## Next Steps

1. [Andrew] Close this lane by hand (his word ~04:xxZ).
2. [0.0.0_AB_MSTR] Push the LOCAL commits above in the next push window (LD-0522).
3. [3.0.0_SA_CVO] L8 intake of rows S1..S9.
4. [owners named on S7, S8 and S9] deploy_ledger.py notes; record-terraform-deploy.sh; the CloudTrail node in the
   aws corpus.
