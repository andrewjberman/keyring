# /integrate -- the two devices on ONE TRUNK (`CLOUD`)

**Who runs it:** `0.0.0_AB_MSTR` (laptop) and `0.0.0_AB_MSTR~Z` (site Z). Both halves are shared-branch pushes
(LD-0367/LD-0368: only the MSTRs push a shared branch; no word from Andrew is needed, CLAUDE.md push law, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_044xZ_PUSHES_NEED_NO_APPROVAL_EXCEPT_CLIENT_FACING_PROD.md`). A lane agent invoking this stops at
Step 0 and routes to its MSTR.

## The model, as of 2026-09-24 (Andrew-direct "recs approved" ~01:4xZ at the laptop MSTR terminal, card 1 (a))

> ONE TRUNK -- retire SITEZ, site Z works on CLOUD.

There is no per-device branch any more. **Both fabrics commit locally to `CLOUD` and both MSTRs push `CLOUD`.**
Integration is therefore not a cross-branch merge; it is the ordinary discipline of a shared branch:
**fetch, merge `origin/CLOUD` into the local `CLOUD` (never rebase), push.** The whole of the 2026-08-12 ->
2026-09-24 two-branch protocol (base, overlap set, merge-tree, per-hunk classification, the parity fixed-point) is
retired with the branch. Its lessons that survive are below, because they were never about the branch.

The record of the retirement: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260924_014xZ_RECS_APPROVED_ONE_TRUNK_CURRENCY_FILE_NO_VETO_PORTAL_DEV_PUSH.md`,
LD-0613. The last `SITEZ` tip is tag `archive/SITEZ-20260924`. The portal has run this way on one `DEV` all along.

**What "properly synched" means now (Andrew, 2026-08-27, unchanged):** mutual updatedness on a practical cadence,
never a fixed point. Two live fabrics cannot be at the same commit for longer than it takes someone to commit; a
push-hold to manufacture equality is refused unless a real consumer asked for a frozen state.

## PER-BOX BRANCHES -- a box that has switched (Andrew-direct 2026-10-08 ~18:0xZ)

Design: `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/PER_BOX_BRANCH_DESIGN_20261008.md` (Andrew's answers verbatim in
section 9; cadence rules in section 10). Build placement: `1.0.0_SA_CTO` `PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md`.
A box has SWITCHED once its shared tree is on `box/<box>` (`git symbolic-ref --short HEAD`). Until then Steps 0-3
below apply to it unchanged. Once switched:

- **Its seats commit to `box/<box>`; its MSTR pushes only `box/<box>` and NEVER pushes `CLOUD`.**
- **`CLOUD` has ONE writer, the integrator: `0.0.0_AB_MSTR` (laptop).** `0.0.0_AB_MSTR~Z` takes over only on a
  handover recorded in a ledger entry. Two live integrators re-create the push race this model removes.
- **Slots** (`/govern`): laptop `:00`/`:30` (integrator pass, then its own box pass), site Z `:06`/`:36`, dell1
  `:12`/`:42`, dell2 `:18`/`:48`. A slot is load-spreading, never what makes a pass safe: boxes share no writable ref.
- **Skip, never overlap:** each pass takes `mkdir "$(git rev-parse --git-common-dir)/pass-<kind>.lock"` (kind = `box`
  or `integrator`) and removes it at the end. If it exists and the pid in it is alive, this slot is skipped and said
  so in one line. A dead holder's lock is removed and logged.

### THE PROGRAM: `.tools/box-sync.sh` (Andrew-direct ~19:5xZ: "I think this should be programmatic")

The two passes below run as ONE COMMAND each. Neither uses a worktree, and neither opens a merge in any shared tree.
Each merge is computed with `git merge-tree --write-tree`, graded on a private index pinned to its two parents (only
what the merge introduces), checked with `safe-merge.sh --verify-merge`, and written with `git commit-tree`.
- **Box pass** (each box's MSTR, at its slot): `bash .tools/box-sync.sh box`. The only shared-tree act is the land,
  under safe-commit's own lock: a compare-and-swap of `box/<box>`, plus `git read-tree -m -u` of the paths the trunk
  changed. It takes about half a second in the fixture. It refuses rather than overwrite a seat's uncommitted edit.
- **Integrator pass** (`0.0.0_AB_MSTR` only): `bash .tools/box-sync.sh integrate`. It touches no working tree, so it
  costs the laptop a fetch, the merges and a push. It may run more often than `:00`/`:30`.
- **Exit 4 = HELD** (a conflict, or a seat's dirty edit on a changed path). Nothing landed; it is logged as a
  `BOX-SYNC` row. A conflict is resolved by hand with the procedure below. `--dry-run` reports without acting.
- The manual procedures below stay as the fallback and the conflict path.

### BOX PASS (every switched box, at its slot): take the trunk FIRST, then push

```bash
BOX=$(bash .tools/agentbus-sqs.sh device | sed -n 's/^device: //p'); B=box/$BOX; TS=$(date -u +%Y%m%dT%H%M%SZ)
git fetch origin
if ! git merge-base --is-ancestor origin/CLOUD "$B"; then         # 1. take the trunk (F1 shape) only if it moved
  WT=<scratch>/drain-$TS; git worktree add "$WT" -b drain/$BOX/$TS "$B"
  (cd "$WT" && bash .tools/safe-merge.sh origin/CLOUD)            #    grade + the TREE-DROP CHECK (below) in the worktree
  (cd "$WT" && bash .tools/safe-merge.sh "$B")                    #    catch-up: this box's commits made during the grade
  git merge --ff-only drain/$BOX/$TS                              #    shared tree (on $B): a fast-forward, seconds
  git worktree remove "$WT"; git branch -d drain/$BOX/$TS
fi
git push origin "$B"                                              # 2. the deploy gate deploys THIS box's diff vs origin/CLOUD
git ls-remote origin "refs/heads/$B"                              #    the only landing oracle
```
Taking the trunk first means the branch the integrator merges next already holds `CLOUD`, so its merge carries only
this box's own new commits. The push is a fast-forward: nobody else writes `box/<box>`. The deploy gate deploys only
this box's own diff against `origin/CLOUD` (B2, `.tools/git-hooks/pre-push-safe-deploy.sh`).

### INTEGRATOR PASS (`0.0.0_AB_MSTR` only, at `:00` and `:30`, before its own box pass)

```bash
git fetch origin
AHEAD=$(for r in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin/box/); do
          git merge-base --is-ancestor "$r" origin/CLOUD || echo "$r"; done)
[ -z "$AHEAD" ] && { echo "integrator: no box ahead of CLOUD -- no-op pass"; exit 0; }
WT=<scratch>/drain-int-$TS; git worktree add "$WT" -b integrate/$TS origin/CLOUD
for r in $AHEAD; do (cd "$WT" && bash .tools/safe-merge.sh "$r") || HELD="$HELD $r"; done   # see below
#   TREE-DROP CHECK on every merge commit made, in the worktree, before the push
git -C "$WT" push origin HEAD:CLOUD                               # an INTEGRATION push: the deploy gate deploys nothing
git ls-remote origin refs/heads/CLOUD
git worktree remove "$WT"; git branch -D integrate/$TS
```
- **One box at a time today; one merge with one grade per pass is the target.** `safe-merge.sh` takes one head, so the
  pass merges the boxes that are ahead in turn. Each is small, because every box took the trunk before pushing. The
  single octopus merge with one grade (design section 10, rule 3) lands with build item B3 in `safe-merge.sh`.
- **A box that conflicts is HELD, not resolved under the clock:** abort that merge, carry on with the others, and send
  that box's MSTR one agentbus message naming the conflicting paths. That box resolves it in its next box pass, by
  taking the trunk, so the conflict is settled where the work was written.
- **ONE OWNER REPAIRS A TRUNK BREAK** (1.0.0_SA_CTO ruling 2, `CTO_RULINGS_GPT_FEEDBACK_AUTONOMY_BRIEF_20261009.md`
  @ba20ac668b; ledger LD-0640). A break in a trunk-shared file (a conflict, a bad merge, a broken schema) is repaired only
  by the seat that owns the file's lane, on its own box (`python .tools/owned-paths-validate.py --check-path <serial>
  <path>` names the lane). Every other box takes `CLOUD` at its next pass and does not repair it too. An unowned path
  (lane ANY) is repaired by the integrator's box. Two boxes repairing the same break is how a fix collides with itself.
- **Before the laptop itself switches:** its own commits are still on `CLOUD` with no box branch. Push them first,
  on their own (Steps 1-2: they deploy on that push), then run this pass. The deploy gate REFUSES an integration push
  that also carries commits from no box branch, because those would never deploy.

## MICROPRODUCTS -- portal, opal_ai, mcportal (Andrew-direct 2026-10-08 ~22:4xZ: "yes to the microproduct policy")

Policy and its measurement: `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ACTIVITY_STUDY_AND_MICROPRODUCT_POLICY_20261008.md`
(7 days: the monolith 2,718 landings, portal 160, opal_ai 4, mcportal 0). The microproducts get NO box branches:
1. **One trunk, `DEV`.** A seat lands its change on `DEV` itself: fetch, merge, push, never rebase. A rejected push is a fetch and retry.
2. **`PROD` only through `/prod-deploy`**, client-facing, unchanged.
3. **Another box delivers through a short-lived candidate branch** (`cand-*`, `q/<box>/...`). **The seat that lands it deletes it in the same act.**
4. **The workspace's pointers to these repos** move only by a deliberate commit (for example `/prod-deploy`'s pointer step),
   never as a side effect. When two box branches moved one pointer, `git merge-tree` already takes the descendant. Two
   diverged pointers are a real conflict: the box is HELD for a person.
5. A microproduct moves to box branches only when its own push contention shows in a record.

## Step 0 -- identity + the two questions every push answers

- You are an MSTR serial, or you stop here.
- **Which device am I?** `bash .tools/agentbus-sqs.sh device` -- by workspace path, never by branch (there is one
  branch) and never by serial suffix.
- **What am I about to carry?** A push carries every lane's committed work on this device, not just yours
  (`git log --format='%an' origin/CLOUD..HEAD | sort | uniq -c`). Say what you carried.

## Step 1 -- the pull, and why it is a merge

**DRAIN IN A LINKED WORKTREE, THEN FAST-FORWARD THE SHARED TREE** (GitOps F1; `1.0.0_SA_CTO`
`FAST_FIX_RULINGS_20261008_162xZ.md` item 6, Andrew-direct 2026-10-08 ~16:0xZ). `MERGE_HEAD` and the commit lock are
per WORKTREE, so a long merge grade in a linked worktree refuses no seat's commit in the shared tree.

```bash
TS=$(date -u +%Y%m%dT%H%M%SZ); BOX=$(bash .tools/agentbus-sqs.sh device | sed -n 's/^device: //p')
WT=<scratch>/drain-$TS                                  # the name MUST start drain- : the GC reaper never targets it
git worktree add "$WT" -b drain/$BOX/$TS CLOUD          # 1. drain worktree on a drain branch
git -C "$WT" fetch origin
(cd "$WT" && bash .tools/safe-merge.sh origin/CLOUD)    # 2. the long grade runs here; never --rebase (NEVER#7)
#    2b. TREE-DROP CHECK in the worktree, BEFORE anything moves (the Parents-and-tree bullet below), on its merge commit
(cd "$WT" && bash .tools/safe-merge.sh CLOUD)           # 3. catch-up: the minutes of local commits made during the grade
git merge --ff-only drain/$BOX/$TS                      # 4. shared tree: a fast-forward, no MERGE_HEAD, no hook, seconds
#    4 refused because CLOUD moved again -> repeat 3, then 4
#    5. push from the shared tree (Step 2), then: git worktree remove "$WT"; git branch -d drain/$BOX/$TS
```
- Step 4 fails safe: git refuses a fast-forward that would overwrite a local modification. If the drain path fails,
  fall back to a merge in the shared tree under the merge-window control below.
- A `drain-*` worktree is live integration state for as long as it exists. No reaper, `/cleanup` or `/kill` run
  removes one; the integrator that made it removes it after the push.
- **Overlap is still the whole job**, just measured against the trunk instead of a sibling branch:
  `git merge-tree --write-tree --name-only HEAD origin/CLOUD` before the merge tells you the conflict set without
  touching the tree. Andrew's separate-projects premise keeps it near zero; when it is not, that is a coordination
  finding to surface, not a merge problem to absorb.
- **`--unified=0` per-side ranges, not the conflict hunk**, decide whether a conflict is a real same-row collision or
  adjacency. Identical NONZERO-count ranges = one defect corrected twice (PICK, then audit the loser for content);
  identical ZERO-count ranges = an append collision (UNION, keep both). Same-row collisions on LAW text go to the
  law owner, never resolved by an MSTR alone.
- The **merge window in the shared tree** is a hazard on either device: announce `MERGE WINDOW OPEN` to live seats,
  merge `--no-commit`, run `git diff --cached --name-only` and reset anything staged outside the merge set (the
  control), commit, announce `CLOSE` with the ls-remote hash. (a) is courtesy; (b) is the control.
- The merge commit's hooks grade the whole merged index; on a large merge that is 15-45 minutes and it is the gate
  working, not a hang. **Never `| tail` the commit**: the pipeline's rc is tail's (site Z 2026-09-23, attempt 1
  reported exit 0 on a commit that had died). Capture to a file and read the file.
- **Parents and tree can disagree -- check the TREE before any push.** After every merge commit M:
  `git diff --name-only --diff-filter=D M^2 M` minus what our side deleted on purpose
  (`git diff --name-only --diff-filter=D $(git merge-base M^1 M^2) M^1`) must be EMPTY. Every parent-based check
  (ancestry, ahead/behind) reads green on a merge whose index was reset under it. Measured at site Z, 2026-09-24:
  merge 12177482b9 dropped 406 of 407 incoming files, and pushing it would have deleted 302 files from origin as a
  fast-forward. It was caught unpushed.
- **Resolve a CONFLICTED merge in your own linked worktree, never in the shared index**, where a peer's act can reset
  the index under the open merge (the same incident).

## Step 2 -- the push, and the deploy it is

```bash
git diff --name-only origin/CLOUD..HEAD -- 'data/*/scripts/**' | wc -l   # the CEILING, read in the same breath
git push origin CLOUD                                                     # the pre-push safe-deploy gate runs
git ls-remote origin refs/heads/CLOUD                                     # the only landing oracle
```
- **THE PUSH IS A DEPLOY EVENT.** The pre-push gate `aws s3 cp`s every deploy-scope `.py` in the pushed range
  UNCONDITIONALLY (a post-write verify, not a pre-write skip; `MATCH` means uploaded-and-verified). So whoever
  pushes carries the other device's pipeline scripts to S3. Measure the ceiling immediately before the push; a
  ceiling older than the push is a floor. The ceiling is an exposure count, never a deploy manifest -- the
  shared-home membership guard skips non-members loudly, and the gate's own per-file lines are the record.
- A push timeout says nothing about landing: `ls-remote` before any retry.
- **NEVER `git stash`** to clear the tree; never rebase; never force.

## Step 3 -- tell the other device

One agentbus message per push: the ls-remote hash, the commit count and per-author breakdown, the deploy ceiling
and what the gate actually wrote, and anything on the branch not ready to travel. The peer pulls when it next
pushes; nothing waits on the peer. A queued bus message is waiting, not lost (14-day FIFO retention). **Never a
second channel** (Andrew 2026-08-12: "no you should write them via agentbus").

## Invocation forms

| form | behaviour |
|---|---|
| `/integrate` | ASSESS: fetch; ahead/behind vs `origin/CLOUD`; conflict dry-run (`merge-tree`); deploy ceiling; the per-author payload. Writes nothing. Runs at MSTR launch. |
| `/integrate merge` | ASSESS then Step 1 (the merge window, the index control) -- no push. |
| `/integrate push` | Steps 1-3, at will (push law): merge, push, verify from the remote, tell the peer. |
| `/integrate parity` | RETIRED with the second branch. Both devices on one trunk have no parity fixed-point to drive; "is the peer updated" is answered by the peer's own pull. |

## What is NOT this skill

- `/prod-deploy` (portal DEV -> PROD); `/git-pull` (the in-session fetch cadence, absorbed into the launch assess).
- Retiring or recreating a shared branch. That is Andrew's word, recorded and ledgered (LD-0607, LD-0613).

## History that binds by reading

The two-branch era's measured incidents stay citable in git history of this file (@ the last two-branch revision):
the shallow-clone false divergence (2026-08-12), the 28-object leg-2 deploy (2026-08-12), the `LEG-OUTSTANDING`
redefinition (2026-08-27), the zero-count append-collision PICK hazard (2026-09-16), the vintage-move re-run rule
(2026-09-16), the R-13 explicit-direction rule (2026-09-24: name `CLOUD -> SITEZ` or `SITEZ -> CLOUD`, never
forward/reverse, in any report or commit subject). With one trunk the direction is always the same and the word
is `pull` or `push`.
