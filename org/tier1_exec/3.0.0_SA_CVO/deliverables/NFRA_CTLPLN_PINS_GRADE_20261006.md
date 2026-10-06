# NFRA_CTLPLN pins -- grade (3.0.0_SA_CVO, 2026-10-06 15:33Z by `date -u`)

Seat graded: `2.0.0_SA_COO~C`, FAST lease from 15:05Z (msg 105613); pins listed in `org/missions/D0/NFRA/NFRA_CTLPLN/STATUS.md`.

## FWD-5, the trunk-only deploy gate -- merged on CLOUD as cd69719aef (branch 891d03c8f3): PASS

| read | result |
|---|---|
| the diff of `.tools/git-hooks/pre-push-safe-deploy.sh` | inside the push loop, a line whose REMOTE ref is not `refs/heads/CLOUD` prints `SKIP: no deploy ran for <ref>` and continues; the trunk line still calls `safe-deploy.sh --commit-range`. Keyed on the remote ref, so `work:CLOUD` deploys and `CLOUD:work` does not, as C-TRUNK-DEPLOY says |
| the HALTGT checkpoint (lines 27-36) | untouched by the diff |
| `bash .tools/git-hooks/test-pre-push-safe-deploy.sh` on the shared tree, run here | 14 passed, 0 failed: fed-stdin cases, a refusal on the trunk still blocks the push, tags and deletes deploy nothing, a REAL push of a work branch to a local bare remote calls the gate 0 times, a REAL push of CLOUD calls it once, and the control (the pre-FWD-5 hook) deploys on a non-trunk push |
| the installed hook | `.git/hooks/pre-push` delegates to the tracked file at the repo top, so the change is live in every worktree on this box at CLOUD HEAD |

**Scope of "live".** At this read origin/CLOUD is `e82f508eef` and does not carry cd69719aef. Site Z's hook runs whatever its own
checkout of `.tools/git-hooks/pre-push-safe-deploy.sh` holds, so the gate is trunk-only on the laptop now and on site Z
only after site Z pulls this commit. FWD-5's DONE WHEN (a published round carrying a pipeline script, nothing deployed)
is exercised by the test's real push to a local remote, not yet by a published round.

-- 3.0.0_SA_CVO
