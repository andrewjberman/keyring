# Disk-hygiene worktree verification -- 3.0.0_SA_CVO

**Date:** 2026-09-17, ~14:30Z-15:27Z. **Requested by:** `0.0.0_AB_MSTR` msg 97605, Andrew's word relayed.
**Re-measured fresh** (not the ~13:3xZ snapshot): `origin/CLOUD` @`881b419753`, `origin/SITEZ` @`c0aa291a17`,
matching `git ls-remote` at the time of this pass. All ahead-counts in the source message reproduced exactly
against both refs (identical vs CLOUD and SITEZ for every branch -- the two remotes are at parity on these
paths). Method throughout: diff each branch at its **merge-base** with CLOUD, never a raw tip-vs-HEAD diff
(a raw diff against far-future HEAD is polluted by everything the rest of the fabric shipped in the
meantime -- e.g. the naive diff on `feature/d13-visual-elevation` read 4,706 files / 2.3M deletions; the
merge-base diff reads 423 files / 44,712 insertions, the real number).

## Andrew's steer, addressed directly

Mid-review Andrew said: *"I'm inclined to believe all of these are approved for deletion because I have
visually smoked the entire live dashboard multiple times since DSGN_REBRND closed and everyone is using it
just fine"* (re: the four DSGN_REBRND-adjacent worktrees). **On the portal CODE specifically, this is
confirmed independently and precisely** -- see #4 below: every one of the four branches' `portal/` submodule
pointer is an ancestor of both portal `DEV` and `PROD`. The product he is looking at already carries this
work. **What his dashboard check cannot see, and what this review found underneath it,** is that the
*workspace-repo* side of the same branches -- the governance record of that work (worker deliverables,
surprise-channel rows, task-order completion flips, and one real content gap in the shipped design-system
doc) -- has no copy anywhere on `CLOUD` or `SITEZ`. That part is UNIQUE by the task's own test, not because
the product is in doubt, but because a record of *how it got there* exists nowhere else. Flagged per row
below; his call once he has this fuller picture, not overridden by it.

---

## 1. `C:/tmp/wk-dsgn-1j` (`wk-dsgn_rebrnd-1j`, 102 commits ahead)

**VERDICT: REDUNDANT WITHIN THE SET -- safe to delete regardless of #4's outcome.**
0 commits ahead of `feature/d13-visual-elevation` (`git rev-list feature/d13-visual-elevation..wk-dsgn_rebrnd-1j`
= 0) -- every commit on this branch is already an ancestor of #4. It carries no content #4 does not already
carry. Delete this one any time; it is not the copy of record.

## 2. `C:/tmp/wk-dsgn-1k` (`wk-dsgn_rebrnd-1k`, 114 commits ahead)

**VERDICT: REDUNDANT WITHIN THE SET -- same as #1.** 0 commits ahead of `feature/d13-visual-elevation`.

## 3. `C:/tmp/wk-dsgn-2c` (`wk-dsgn_rebrnd-2c`, 109 commits ahead)

**VERDICT: REDUNDANT WITHIN THE SET -- same as #1.** 0 commits ahead of `feature/d13-visual-elevation`.

## 4. `.worktrees/d13-visual-elevation` (`feature/d13-visual-elevation`, 121 commits ahead)

**VERDICT: MIXED.** This is the copy of record for #1-#3 (they are pure subsets of it). Splits cleanly by
which repo the content lives in:

- **`portal/` submodule pointer -- SUPERSEDED.** Tip's gitlink is `086371dd4980`.
  `git -C portal merge-base --is-ancestor 086371dd4980 origin/DEV` -> **YES**;
  same against `origin/PROD` -> **YES**. The actual portal product this branch built already ships on both.
  This is the part Andrew's dashboard check confirms directly.
- **`org/missions/D13/DSGN/DSGN_REBRND/deliverables/**` and `surprise-channel/**` -- UNIQUE.** These paths
  do not exist on `HEAD` at all (`git ls-tree -d HEAD -- .../deliverables` is empty). Worker completion
  evidence, adjudications and remediation rows for the whole round exist ONLY in this worktree.
- **`org/missions/D13/DSGN/DSGN_REBRND/task-orders/*.md` status flips -- UNIQUE.** E.g. `TO-RB-s-9` reads
  `<status>pending</status>` on `HEAD`, `<status>complete</status>` on the branch. The task orders
  themselves landed at L6 issuance (they're on `HEAD`); the completion record of the round never drained
  back.
- **`design/brand/*.json` (6 new files: `inversion-rule.json`, `light-ground-semantics.json`,
  `portal-layer-map.json`, `portal-opaque-ladder.json`, `portal-routes.json`,
  `portal-surface-inventory.json`) -- UNIQUE.** None exist on `HEAD`.
- **`design/systems/portal/DESIGN_SYSTEM.md` -- UNIQUE, and this is the one that matters most.** `HEAD`'s
  copy is dated 2026-07-15 (`210f70a9`) -- the pre-DSGN_REBRND "silver-canvas" archetype CLAUDE.md itself
  says was superseded by Andrew's 2026-09-11 inverted-bands ruling. The branch's copy is dated 2026-09-14
  (`edfc97ed`), 453 lines different. **CLOUD's own governing design-system document does not describe the
  design system that is actually live.** This is a real, content-level gap, not a process formality.

**Recommendation:** do not delete #4 until `2.0.0_SA_COO~D` (the project's own lead, DSGN_REBRND) either
lands `DESIGN_SYSTEM.md`'s update and the completion records, or explicitly abandons them on the record.
Given Andrew's steer, the likely fast path is: land the one doc (worth minutes, not a round), let the rest
go. That is his call to make with this split in front of him, not mine to default either way.

---

## 5-8. The four `krny-c3-*-20260910` worktrees (KRN_WORKSPACE / `1.7.0_SA_KRN`)

**VERDICT: DO NOT TOUCH -- these are not stale. At least one is confirmed live input to open work.**

`org/tier1_exec/3.0.0_SA_CVO/task_orders/` currently holds **six PENDING** ADHOC task orders from
`1.0.0_SA_CTO~Y` to `3.0.0_SA_CVO~Y` (a lane of this same seat), under a direct Andrew commission
("Anatomy02", explicitly off the tree-project governance surface -- `docs_abcdeg`/`scratchpad_tmp` under
`Downloads`, per this seat's own standing memory that Anatomy work stays off `ajb_workspace`). Two of them
name `.worktrees/krny-c3-report-admission-20260910` **explicitly, by exact path and exact commit hash**:

- `c3-report-admission-implementation-review~Y`: `<workspace_repository>
  C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/krny-c3-report-admission-20260910</workspace_repository>`,
  `<handback_commit>87c0533527d0...</handback_commit>` -- this is `87c0533527` exactly, the branch's own
  second-newest commit (`git log` confirms it: *"Record committed retained-report I1-I16 implementation
  evidence"*).
- `c3-report-admission-repair-review~Y`: same worktree path, `<workspace_repository>` tag present again.

Both TOs read `<status>pending</status>` on `HEAD` right now -- **the review this worktree feeds has not
happened yet.** Deleting it would destroy the only copy of the evidence lane `~Y` is supposed to review.

The other three worktrees (`krny-c3-access-pair-fixture-20260910`, `krny-c3-kernel-design-20260910`,
`krny-c3-offline-fixture-20260910`) share the identical author, commission, and 2026-09-10 date, and their
commit messages ("hand back reviewed... successor evidence", "hand back C3 offline fixture and CVO95381
correction") read as the same review pipeline. I did **not** find an equally explicit path citation for
these three in the four remaining pending TOs (`c3-access-pair-implementation-review~Y`,
`c3-access-algebra-review~Y`, `c3-admission-traversal-design-review~Y`,
`c3-admission-traversal-spec-review~Y` reference `Downloads/docs_abcdeg` and `Downloads/scratchpad_tmp`
product repos, not these workspace worktree paths by name) -- so I cannot make the SAME strength of claim
for those three individually. But given one of the four is now proven live and in-use, and the disk audit's
"nobody has drained" framing was wrong for that one, treating the other three as presumptively safe on the
strength of a generic staleness heuristic would repeat exactly the mistake this review exists to catch.
**Route all four to `1.0.0_SA_CTO~Y` / `3.0.0_SA_CVO~Y` for confirmation before anyone acts on any of them** --
not to a tree-project COO, since this commission is explicitly outside that structure.

---

## 9. `C:/tmp/wk-taxsma-1` (`wk-mdpf_taxsma-1-1`, 3 commits ahead) -- MDPF_TAXSMA, held project

**VERDICT: UNIQUE -- real, finished, unlanded work.**

The three commits implement `MDPF_TAXSMA.TO-TX-g-1` (GET `/ms/taxsma-workbook`) in full:
`infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` (533 lines) is **absent from `HEAD`**; its test file
(1,163 lines) likewise. The task order itself reads `<status>pending</status>` on `HEAD` -- the completion
never drained. This reads as finished work sitting ready for whenever Andrew lifts the MDPF_TAXSMA hold, not
disposable scratch. Route to the project's owner (`2.0.0_SA_COO~T` per the register) for a hold-aware
drain-or-park call -- explicitly not a delete candidate.

## 10. `C:\Users\AndrewBerman\Desktop\scty-build` (`scty-mcpguard-deploy-build`, 2 commits ahead, untouched since July)

**VERDICT: SUPERSEDED.** Both commits target `infra/aws/ec2/m365-mcp-gateway/**`, a path that **no longer
exists on `HEAD` at all** (`git ls-tree -d HEAD -- infra/aws/ec2/m365-mcp-gateway` is empty -- the whole
surface was consolidated into `opal-gateway`). The substantive content of the roster-grant commit is present
on `HEAD` under the new path, byte-for-byte on the values that matter:
`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:170` currently writes
`MASTER_ADMIN_EMAILS=andrew@opalinvest.com` and
`WRITE_CAPABLE_EMAILS=alyssa@opalinvest.com,opalbloomberg@opalinvest.com` -- the exact grant this branch's
`8b24cd2bbf` added (`MASTER_ADMIN_EMAILS=andrew@opalinvest.com` / `WRITE_CAPABLE_EMAILS=alyssa@opalinvest.com`,
opalbloomberg added later independently). The other commit (`507bd7e1e6`, a YCharts-stripped build variant)
has no live target to apply to. **Note, not verified here:** MSTR's message also flagged 43 *uncommitted*
files in this worktree -- out of this review's scope (the task is about unlanded commits); if those matter,
they need their own look before this one is removed.

## 11. `.claude/worktrees/agent-acc852ec7d8dbfdc5` (1 commit ahead, untouched since Sep 3)

**VERDICT: SUPERSEDED.** Its one commit is a duplicate attempt at `NFRA_COMPEFFICACY.TO-CE-T-2` under
assignee `0.9.0_WK_NFRA_COMPEFFICACY~1`. That task order's **actually assigned** worker,
`0.8.0_AE_CloudComp~A`, already completed it on `HEAD` (`<status>complete (self-marked,
2026-09-03T05:33:58Z) -- proof-of-spec VALID (rc=0)>`). This worktree's own proof file for the same
criterion was never the assignee's and never landed; the task order it addresses is already satisfied by a
different, official completion. Old Agent-tool isolation worktree by naming convention; safe.

---

## Summary table

| # | Worktree | Verdict | Action |
|---|---|---|---|
| 1 | `wk-dsgn-1j` | Redundant (subset of #4) | Delete any time |
| 2 | `wk-dsgn-1k` | Redundant (subset of #4) | Delete any time |
| 3 | `wk-dsgn-2c` | Redundant (subset of #4) | Delete any time |
| 4 | `d13-visual-elevation` | MIXED -- code SUPERSEDED, one real doc gap + record UNIQUE | Hold for `COO~D`; portal code alone changes nothing live |
| 5-8 | `krny-c3-*` (4) | DO NOT TOUCH -- one confirmed live TO input, other three unconfirmed | Route to `CTO~Y`/`CVO~Y` |
| 9 | `wk-taxsma-1` | UNIQUE -- finished, unlanded, project on hold | Route to `COO~T` |
| 10 | `scty-build` | SUPERSEDED | Safe (commits only; 43 uncommitted files unreviewed) |
| 11 | `agent-acc852ec7d8dbfdc5` | SUPERSEDED | Safe |

Net immediately safe by this review: **#1, #2, #3, #10, #11** (5 of 11) -- none require a further owner call.
**#4** needs `COO~D`'s five-minute doc-landing call before its record half goes. **#5-9** are NOT disk
hygiene at all: four are live task input, one is real finished work waiting on a hold.

-- 3.0.0_SA_CVO
