# work 1840Z — v2.1.114 RE-VERIFY on 7-commit head (COO drive)

**archetype:** DEPLOY-READINESS (re-confirm; still Andrew-GO-gated, NOT promoted)

## Current State — RE-CONFIRMED on 7-commit head, builds clean, RAVC2'd

COO `[DRIVE]` `20260603T183141Z`: origin/DEV gained a 7th commit (13618900, RD~B's
comment-only PMTRDX TradeSecurity note) AFTER my 6-commit pre-stage attestation. Since the
promote re-creates the worktree + merges origin/DEV AT GO TIME, 13618900 rides v2.1.114.
Re-verified so the attestation matches ship-state. RAVC2 sent `20260603T184021Z`.

## Re-verify result (7-commit head)

| Check | Result |
|-------|--------|
| origin/DEV head | 13618900 (docs(trade-submission): PMTRDX.001 canonical-unit note) |
| origin/PROD | unchanged 9f890e0f (v2.1.113) |
| commit count origin/PROD..origin/DEV | 7 (13618900 + prior 6) |
| merge dry-run (worktree from PROD, --no-ff origin/DEV) | CLEAN, zero conflicts |
| 13618900 in merge | YES (merge-base --is-ancestor PASS) |
| parity `git diff --stat origin/DEV HEAD` | EMPTY = byte-identical to 7-commit DEV head |
| tsc -b | PASS |
| full vite build | clean, exit 0, 23.3s (chunk-size advisory only), 419 pkgs |
| worktree teardown | removed + pruned + dir cleaned; Rule-19 intact (main on DEV @ 13618900) |
| rollback target | unchanged 9f890e0f (v2.1.113) |

## Operational catch — local PROD pollution (matters for GO-time)

`git worktree add ../.runtmp/portal-promote-prod PROD` checks out the LOCAL PROD branch. Last
tick I committed a throwaway dry-run merge ON that local PROD branch (to verify parity without
pushing), which advanced local PROD to 47b3d5d7. After teardown the local PROD ref STAYED at
47b3d5d7 (stale junk), so this tick's worktree-add started from the polluted base, not
origin/PROD.

**Fix:** `git update-ref refs/heads/PROD refs/remotes/origin/PROD` — moved local PROD back to
9f890e0f (origin/PROD), discarding only my never-pushed dry-run commit (no destructive reset on
real work). Re-ran the verify clean from 9f890e0f.

**GO-time lesson:** before the real promote, ensure the worktree bases on origin/PROD — either
reset local PROD ref first (done; it's clean now) OR `git worktree add <path> origin/PROD`
(detached) + fresh PROD branch. Real promotes push (so local PROD = origin/PROD afterward);
this pollution is specific to the verify-without-push dry-run pattern. Flagged to COO.

## Disposition of the PMTRDX note (per COO)

COO's prior accept froze the 6-commit bundle and said NOT to add the trade-submission.ts note —
but RD~B then committed it as 13618900 on origin/DEV directly, so it now rides v2.1.114 as the
7th commit by the merge-at-GO-time mechanism. COO acknowledged this in the 7th-commit drive
("frozen-as-staged only holds if origin/DEV doesn't move"). It's comment-only, no impact —
verified clean. Bundle is now effectively 7 commits, all green.

## Next Steps

- **[Andrew]** GO gate = authenticated pixel smoke (creds wall).
- **[DT]** on GO: one-step ship from origin/PROD base (local PROD now clean at 9f890e0f).
- Rollback: `git push origin 9f890e0f:PROD` (v2.1.113).
