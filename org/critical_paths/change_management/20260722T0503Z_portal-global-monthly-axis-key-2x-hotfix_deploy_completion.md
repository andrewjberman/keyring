# Deploy-completion ledger: portal-global-monthly-axis-key-2x-hotfix

- **Opened:** 2026-07-22T05:03Z by `0.2.0_DT_PortfolioAnalytics` at DEPLOY-START (CLAUDE.md NEVER#5: a begun deploy FINISHES in-session or rolls back + escalates loud).
- **Authorization:** Andrew GO ~0455Z (relayed CTO 045718Z) -> CTO **DEPLOY GO** 050225Z after his manual surface-ack verify PASSED on `8fd61dbf`.
- **Scope:** Portal PROD promote of the standalone Global "2x" label fix. `ModelPortfolios.tsx` monthly Period-End XAxis `dataKey` `period` -> `fullDate` + tick formatted for display. **BINDING-ONLY — bar dataKeys untouched, zero value change.**
- **Root cause being fixed (DE's, quoted not re-derived):** the monthly `period` label omits the year; the GLOBAL view alone renders the full since-inception window (21 month-end bars) while per-firm views keep a rolling ~13. Global therefore produced **duplicate recharts category keys** ("Mar 31"/"Apr 30" for BOTH 2025 and 2026). Duplicate categories break the bar<->row binding — recharts resolves the tooltip to the FIRST row with that category, so hovering the 2026 bar reported the 2025 row (Apr 30: $963.5M vs $1,608.9M = 1.67x — Andrew's "almost double").
- **SEPARATE from the MDPF re-land**, which stays gated on its 6-item battery. This deploy does not touch, unblock, or substitute for that.

## Pre-deploy verification (mine, before touching a worktree)
- **Commit identity:** `8fd61dbf6493d032e117f3f08d0b4b85601c032a`, author `0.4.0_DE_ClientPlatform`, parent `2c802d1379f35b82ac9e5e3235a3f71b59b03aa4` — confirmed PROD-base+1 as CTO stated.
- **Diff scope:** 1 file, `src/pages/ModelPortfolios.tsx`, +16/-2. Read the actual diff: XAxis `dataKey` + a tick-label formatter. No dataKey on any bar touched. Matches CTO's description exactly.
- **SURFACE_ACK anchor CHECKED, not assumed** — ran the CI checker's own extraction (`sed -n 's/^[[:space:]]*SURFACE_ACK:[[:space:]]*//p'`); it returns the reason string, so the token genuinely STARTS its line. A mid-line mention would not have acked and would have been invisible to a casual read.
- **⚠ BRANCH NOT ON ORIGIN AT GO TIME.** `git ls-remote origin 'refs/heads/hotfix/*'` returned EMPTY; the branch `hotfix/global-monthly-axis-key` does not exist on the remote. The **commit object is present in the local shared portal repo** (`git cat-file -e` PRESENT) because agents share this host's clone. **Decision: promote the exact verified sha `8fd61dbf` directly** rather than wait for a branch push — this deploys precisely the object CTO read, which is strictly safer than a branch that could still be amended before it lands. The PROD push carries the object. **Flagged to CTO; DE should still push the branch for the record.**
- **PROD baseline:** `origin/PROD` = `99fed48f6de3dd8a47b4fee11953943163c29a49` (v2.1.140, already contains `2c802d13`).
- **ROLLBACK SHA: `99fed48f6de3dd8a47b4fee11953943163c29a49`** — recorded here BEFORE the merge, and carried in the merge-commit message.

## Legs
1. [x] Ephemeral worktree off PROD at `/c/Users/ANDREW~1/AppData/Local/Temp/claude/prod-promote-2xhotfix`. Local `PROD` re-asserted from `origin/PROD` first (`update-ref`) to avoid dry-run pollution. `bun install` inside it: 420 packages, 99.92s, `node_modules/.bin/tsc` confirmed present BEFORE the push (the gate fails "tsc: command not found" otherwise). Main tree verified on `DEV` throughout.
2. [x] `--no-ff` merge of `8fd61dbf` -> `885b76c2fdcac13f1975fb527b4295f805842515`. **Clean, zero conflicts.** Rollback sha carried in the merge message. Message authored via `-F` (never `-m` — a commit message is an execution vector).
3. [x] Diff verify **before** pushing: `git diff --stat 99fed48f HEAD` = 1 file, `src/pages/ModelPortfolios.tsx`, +16/-2 — the label fix and nothing else. Cross-check `git diff 8fd61dbf HEAD -- src/pages/ModelPortfolios.tsx` = EMPTY, i.e. the merged file is byte-identical to the sha CTO verified.
4. [x] Pushed `origin PROD`: `99fed48f..885b76c2`. VALGATE D-1 PASS (no `api/endpoints/*.ts` touched); pre-push `tsc -b --noEmit` PASS. No `MSYS_NO_PATHCONV` (it breaks the VALGATE hook).
5. [x] `deploy.yml` run **29893042948** — **conclusion: success** (read via `gh run view --json`, NOT `gh run watch`). All 3 jobs green: Build Production Assets / Deploy to S3 + CloudFront / Tag Deployment. headSha `885b76c2` == pushed sha.
6. [x] Auto-tag `portal-v2.1.141` — **peel-verified**: `git rev-list -n1 portal-v2.1.141` = `885b76c2…` == `origin/PROD` (annotated tags must be peeled; comparing the tag object would be a false check).
7. [x] Worktree torn down (deregistered + directory removed — `git worktree remove` hit a Windows MAX_PATH failure deleting `node_modules`, cleaned with a long-path `\\?\` delete). `git worktree list` clean. **Portal main tree confirmed on `DEV` @`aa8c0420` (Rule 19 held end-to-end).** Ended at workspace root.
8. [x] Reported run conclusion + deployed sha to CTO.

## Deployed
- **PROD `885b76c2fdcac13f1975fb527b4295f805842515`**, tag `portal-v2.1.141`, run `29893042948` success.
- Previous PROD / **rollback target: `99fed48f6de3dd8a47b4fee11953943163c29a49`** (tag `portal-v2.1.140`).

## NOT closed by me — behavioural confirmation is someone else's leg
My leg is **the deploy**. I verified the deploy MECHANISM (merge scope, push, CI conclusion, tag peel), not that the page renders correctly. **CI success is not a render check.** Open, and deliberately not mine:
- **CTO** independently re-verifies opalinvest.dev serves the fix.
- **DE** re-runs the duplicate-key gate against the LIVE SERVED build (the negative control was on the unmodified base; the positive must be re-run on what production actually serves).
- **Andrew** hover-confirms the 2026 bars report 2026 values.

## Residual noted, not actioned
- **Hotfix branch never reached origin.** `refs/heads/hotfix/global-monthly-axis-key` was absent at GO time and I promoted the verified commit object directly. The commit is now permanently reachable from PROD, so nothing is lost — but the branch ref itself is still unpushed. Cosmetic; DE's to push if wanted.
- **Workspace submodule pointer NOT bumped.** It records `2c802d13` while the portal main tree sits on `DEV` @`aa8c0420`. That drift PRE-DATES this deploy and bumping it would record the stranded MDPF re-land commit in the workspace — unrelated to this hotfix and entangled with a gated change. Left deliberately for whoever lands the MDPF re-land.

## Status: CLOSED 2026-07-22T05:15Z — 8/8 deploy legs complete, verified, nothing stranded
