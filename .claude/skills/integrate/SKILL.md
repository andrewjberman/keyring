# /integrate -- the two devices on ONE TRUNK (`CLOUD`)

**Who runs it:** `0.0.0_AB_MSTR` (laptop) and `0.0.0_AB_MSTR~Z` (site Z). Both halves are shared-branch pushes
(LD-0367/LD-0368: only the two MSTRs push a shared branch, on Andrew's word). A lane agent invoking this stops at
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

## Step 0 -- identity + the two questions every push answers

- You are an MSTR serial, or you stop here.
- **Which device am I?** `bash .tools/agentbus-sqs.sh device` -- by workspace path, never by branch (there is one
  branch) and never by serial suffix.
- **What am I about to carry?** A push carries every lane's committed work on this device, not just yours
  (`git log --format='%an' origin/CLOUD..HEAD | sort | uniq -c`). Say what you carried.

## Step 1 -- the pull, and why it is a merge

```bash
git fetch origin
git merge --no-ff origin/CLOUD        # never --rebase, never pull --rebase (NEVER#7, hook-enforced)
```
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
| `/integrate push` | Steps 1-3 on Andrew's word: merge, push, verify from the remote, tell the peer. |
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
