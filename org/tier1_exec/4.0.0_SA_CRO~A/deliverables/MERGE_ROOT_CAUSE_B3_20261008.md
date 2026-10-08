# Why merges take so long -- root causes and a size-invariant method (B3, 4.0.0_SA_CRO~A, 2026-10-08 ~19:1xZ)

**Asked by:** Andrew-direct ~18:3xZ, verbatim in section 11 of
`org/tier1_exec/4.0.0_SA_CRO~A/deliverables/PER_BOX_BRANCH_DESIGN_20261008.md`: long merges "usually are taking that
long because they are failing multiple times. This is why we need to figure out a method of doing this that is stable
and preferably size invariant." Build item B3 of `1.0.0_SA_CTO` `PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md`.
**Owner:** `4.0.0_SA_CRO~A` (`.tools/safe-merge.sh`, `.tools/safe-commit.sh`, per `1.0.0_SA_CTO` msg 107030).
**Vintage:** laptop records and code, read 18:4xZ-19:1xZ.

## 1. The answer in one paragraph

Andrew is right: a long merge is mostly a merge that ran more than once. Each run is slow because the checks start
thousands of short git processes and grade the same tree twice. Runs fail for reasons that grow with the size of
the merge: a hook hangs; a gate re-judges content both parents already passed; or, before today, a peer's act reset
the shared index under the open merge. The method that is stable and size-invariant does two things. It keeps every
merge small through the per-box cadence. And it judges a merge only on what the merge itself introduces, not
everything its parents carry. Section 4 is the one call that needs Andrew's word.

## 2. The causes, with evidence

| # | Cause | Evidence (READ unless marked) | Status |
|---|---|---|---|
| R1 | **Each grade starts thousands of git processes.** The row gate read every file through two git start-ups per read. | MSTR profile, 2026-10-05: one 743-path merge, 1,149 s, of which 1,125 s in 11,144 reads (21,962 git processes). A memo (change 1) cut it to 171 s, 1,274 reads at ~0.11 s each (`PROPOSAL_20261005_SAFE_MERGE_ROW_GATE_SPEED_CHANGES_2_AND_3.md`, LD-0613 Progress 88) | change 1 LANDED 10-05; **change 3** (one `git cat-file --batch` reader, est. under a few seconds) PROPOSED, not adopted |
| R2 | **The same tree is graded twice per merge:** `safe-merge.sh`'s own grade, then pre-commit step 9 runs the same gate on the same index. | Same proposal section 1: "first pass 12:34-12:51 local, second pass from 12:51" | **change 2** (skip the second run when the tree id and the gate's blob id match the first) PROPOSED, not adopted |
| R3 | **Gates re-judge what the parents already passed, and refuse, so the whole merge re-runs.** | mass-deletion gate refused a merge over 38 deletions site Z had already committed through safe-commit, one full re-run (2026-10-04; proposal section 5). Row gate refused rows already published elsewhere (fixed for `CLOUD` in batch 112; for `origin/box/*` today, `1394c97b72`). The union merge driver failed at its first use today (LD-0622) | partly fixed; the general rule is section 4 |
| R4 | **A pre-commit hook hangs inside the merge commit**; a retry limb kills it and runs again. | `org/mcp/hook-hang-capture.log`: 7 captures, all 2026-09-30 between 04:49Z and 07:15Z (`env.exe` at 0 CPU); no capture since | cause unknown; whether it stopped or stopped being captured is UNREAD |
| R5 | **A peer's act reset the shared index under an open merge**, dropping files; the merge was then redone. | 9e127d674f lost all 169 incoming paths; 12177482b9 dropped 406 of 407 (LD-0613; `/integrate` text) | REMOVED by fast fix F1: drains run in their own worktree (live on the laptop since ~17:1xZ) |
| R6 | **A merge killed mid-run blocked its worktree for good** (open merge, dead lock holder). | `safe-merge.sh` refused "A MERGE IS ALREADY OPEN" with no way out short of a hand abort | FIXED today, `2ee73e5a64` |
| R7 | **No record of attempts.** Every refusal went to stderr only, so "how many tries, and why" was unmeasurable. | `safe-merge.sh` wrote no audit row (read) | FIXED today, `2ee73e5a64`: one `MERGE-ATTEMPT` row per run (rc, seconds, args, first refusal line) |

**What scales with size:** R1 (reads grow with the files and task orders a merge touches), R2 doubles R1, and the
chance of an R3 or R4 failure grows with how much a merge carries. **What does not:** git's own merge, the tree-drop
check, and a gate that reads only what the merge introduces.

## 3. The method: stable and size-invariant

1. **Small merges by construction** (per-box design, section 10): each box takes the trunk before it pushes, so an
   integration merge carries only that box's new commits since its last pass.
2. **Judge a merge only on what it introduces** (section 4): the paths where the merge result differs from EVERY
   parent. That covers conflict resolutions, and a file both sides changed that git auto-merged into content neither
   parent had. Plus the tree-drop check. A clean merge of separate work introduces almost nothing, so its grade cost
   stays near-constant whatever the merge's size.
3. **Grade once, read cheaply** (changes 2 and 3): one grade per tree, one long-lived git reader.
4. **Measure attempts** (R7, live now): success is "the first attempt lands", read from the `MERGE-ATTEMPT` rows, not
   a faster single run.

## 4. The call that needs Andrew's word

**May a merge be graded only on the paths it introduces (the result differs from every parent), plus the tree-drop
check, instead of re-running every gate over everything its parents already passed?** Each parent was graded when it
was committed (two-phase safe-commit on every box). REC yes, with one guard: a gate that checks a rule ACROSS files
(for example, two task orders minting one id) still reads the merged tree, but only for files that BOTH sides
changed.

## 5. Next acts and owners

| Act | Owner | When |
|---|---|---|
| Read the first `MERGE-ATTEMPT` rows from real drains and integrator passes (laptop; then site Z after its switch) | 4.0.0_SA_CRO~A | at the first integrator pass after site Z switches |
| Change 2, `safe-merge.sh` half (export the graded tree id and gate blob id) | 4.0.0_SA_CRO~A | after Andrew's word on section 4, since the two change one path |
| Change 2, hook half (pre-commit step 9 skips on a matching pair) | owner of the installed pre-commit hook | with the above |
| Change 3 (one `git cat-file --batch` reader in the row gate) | 1.0.0_SA_CTO (LOOP_MECHANISM lane) | the CTO's call |
| Section 4's rule in `safe-merge.sh`, with the cross-file guard | 4.0.0_SA_CRO~A | on Andrew's yes |
| Find whether R4's hook hangs still happen (capture still armed?) | 4.0.0_SA_CRO~A | next |

## 6. Not checked

- No merge was profiled today; the R1 and R2 numbers are MSTR's of 2026-10-05.
- The other pre-commit gates' share of a merge commit was not measured (the proposal says the same).
- Site Z and the Dells: no merge record read. Their tooling is assumed equal to the laptop's at the trunk.

## 7. Andrew's answer, 2026-10-08 ~19:1xZ (laptop terminal, to 4.0.0_SA_CRO~A), VERBATIM

On section 4 ("May a merge be graded only on the paths it introduces ... plus the tree-drop check?"): "Sure, yes"

**Correction to the guard's example, same turn.** The card's example of a rule that spans files, two task orders
minting one id, spans DIFFERENT files. "Only files both sides changed" would not catch it. Today's merge path does
not run that task-order check at all (it runs in `safe-commit.sh`, at each side's own commit), so the rule loses
nothing there. The guard as built: the row gate grades the introduced paths PLUS every surprise-channel file that BOTH
sides changed since the merge base, because rows inside one channel file are the cross-row domain that gate checks.

## 8. Built, 2026-10-08 ~19:2xZ

- **Section 4's rule is in `.tools/safe-merge.sh`.** The grade covers paths that differ from both parents plus paths
  both sides changed. An empty set is a stated SKIP. `SAFE_MERGE_FULL_GRADE=1` grades everything as before. Each
  `MERGE-ATTEMPT` row now carries `graded=<n>/<staged>`.
- **Change 2, `safe-merge.sh` half:** it exports `SAFE_MERGE_GRADED_TREE` and `SAFE_MERGE_GRADED_GATE` for its
  commit. The hook half is per box: `sc2p/HOOK_CHANGE2_ROW_GATE_SKIP_SNIPPET.md`, asked of `0.0.0_AB_MSTR`.
- **Exercised (scratch repos, real script, real row gate, 19:20Z):** separate work, 0 of 2 graded, SKIP, merged; a
  both-sides auto-merge plus a conflict finished with `--continue`, 2 of 4 graded (exactly those two), merged. A
  fixture hook confirmed the exported ids match the tree committed, both times. `--self-test` 27 of 27.
- **Not run:** `.tools/exercise-safe-merge-continue.sh` (30 arms). It builds a full worktree of the repo, about
  2.8 GB, and the laptop read 9.7 GB free at 18:2xZ.
