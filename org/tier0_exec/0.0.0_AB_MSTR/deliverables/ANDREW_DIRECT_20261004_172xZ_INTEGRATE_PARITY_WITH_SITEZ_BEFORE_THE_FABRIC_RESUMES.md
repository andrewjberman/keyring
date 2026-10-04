# ANDREW-DIRECT 2026-10-04 ~17:2xZ at the laptop 0.0.0_AB_MSTR terminal -- /integrate parity with site Z before the fabric resumes

## Verbatim

> "Before the fabric resumes, I want an /integrate parity between you and sitez MSTR~Z"

## How this seat reads it

- **Parity** means both devices' `CLOUD` and `origin/CLOUD` at ONE commit, read by `ls-remote` and by each device's
  `rev-parse`. `/integrate parity` as a skill form is retired with the second branch; the act is `/integrate push` on
  the laptop followed by site Z's fast-forward.
- **The word covers the push.** It is the laptop's shared-branch push on Andrew's word, and it also re-runs the merge
  of origin cd20da5996 that a low-memory reap stopped at 23:5xZ on 2026-10-03.
- **Steps:**
  1. Site Z pushes everything it holds and reports the hash.
  2. The laptop merges that hash in the linked worktree `wt-mstr-pull5` (never a rebase), tree-checks it, fast-forwards
     the shared `CLOUD` and pushes. The push is a deploy event; the pre-push gate runs as usual.
  3. Site Z fast-forwards to the laptop's hash. Both MSTRs report the same HEAD.
- **Measured at the word:** laptop `CLOUD` 77645a2835 is 128 ahead of and 245 behind origin cd20da5996; the
  merge-tree dry run shows 0 conflicts; the deploy ceiling is 4 files under `data/*/scripts/`.
- **NOT read into the word:** a stop order on any laptop seat. Seats that commit during the merge are carried by a
  second small merge, and the parity report states the commit both devices hold.
