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
1. [ ] Ephemeral worktree off PROD (`bun install` inside it — the pre-push `tsc` gate fails "tsc: command not found" otherwise). Main portal tree STAYS on `DEV` (Rule 19).
2. [ ] `--no-ff` merge of `8fd61dbf` into PROD, rollback sha in the message. **Any conflict -> STOP + surface, never force** (CTO explicit).
3. [ ] Diff verify: merged PROD tree vs the intended content; confirm the ONLY delta vs `99fed48f` is the ModelPortfolios.tsx label fix.
4. [ ] Push `origin PROD` (NO `MSYS_NO_PATHCONV` — it breaks the VALGATE pre-push hook).
5. [ ] `deploy.yml` fires (build -> S3 sync -> CloudFront invalidation -> auto-tag). Verify conclusion via `gh run view <id> --json conclusion` (**not** `gh run watch` — hangs on benign warnings).
6. [ ] Tear down worktree; confirm portal main tree back on `DEV`; end at workspace root.
7. [ ] Report run conclusion + deployed sha to CTO. **CTO independently re-verifies opalinvest.dev serves the fix**; DE re-runs the duplicate-key gate on the live served build; Andrew hover-confirms. My leg is the deploy, NOT the behavioural confirmation — I do not close on my own render claim.

## Status: OPEN — deploy in progress
