# work 2147Z — Portal v2.1.119 DEV->PROD promote: SHIPPED, PROD LIVE

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Current State — SHIPPED, PROD LIVE; Cottonwood serving route active

MSTR GO LD-0169 (ADVI_PRTORG PRTORG.03 RAVC2-ACCEPTED): promoted DEV 00f70f2d
(Cottonwood _partners/ module + dispatcher + firmAccess wiring) to PROD. Rule-19
ephemeral-worktree promote executed cleanly. Portal v2.1.119 LIVE. Signaled
DE + COO + MSTR.

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `00f70f2d` (feat ADVI_PRTORG.04: Cottonwood _partners/ + dispatcher + firmAccess wiring) |
| PROD base | `f8b1a6a9` (v2.1.117) |
| MERGE SHA | `b742e252` (--no-ff) |
| PARITY GATE | `git diff origin/DEV HEAD` = EMPTY (byte-identical to Andrew-confirmed 00f70f2d) |
| VALGATE D-1 | PASS (no-op — no api/endpoints/*.ts changed) |
| TYPECHECK | PASS (tsc -b --noEmit via PROD push pre-push hook) |
| TAG | `portal-v2.1.119` → b742e252 (CI auto-tag) |
| CI run | 27237703259 SUCCESS — Build (1m39s) + S3/CF deploy (8s) + Tag (7s) |
| CF invalidation | CI-managed (Deploy to S3 + CloudFront job) |
| ROLLBACK | `git push origin f8b1a6a9:PROD` (v2.1.117) |

## TAG NOTE
CI auto-tagged our promote as `portal-v2.1.119` (not v2.1.118). The June 8 CI run
(27144827328) created `portal-v2.1.118` → `f8b1a6a9` retroactively (Andrew had also
annotated that commit as v2.1.117 manually). Our promote tag is v2.1.119 → b742e252.
No action needed — both tags are on origin, no version gap in the actual deploy.

## Bundle (origin/PROD f8b1a6a9..origin/DEV 00f70f2d, 3 commits)

1. `00f70f2d` feat(ADVI_PRTORG.04): Cottonwood _partners/ module + dispatcher + firmAccess wiring
2. `7c6099d4` fix(MDPF_CADENCE): stamp Model Portfolios footer (cherry-pick already in PROD as f8b1a6a9 — merged cleanly, no conflict)
3. `03d719d4` feat(frontend-dev/auth): wire firm-entitled smoke creds + surface-coverage matrix (.frontend-dev/auth/ dev tooling only, not app code — MSTR GO authorized full DEV merge)

## Deployment sequence (Rule-19 ephemeral worktree)

- Phase 0 PRE-SHIP GATE: origin/DEV 00f70f2d (local DEV 1 ahead of origin/DEV — needed push), origin/PROD f8b1a6a9, main tree DEV.
- Phase 0 STEP-0: `git update-ref refs/heads/PROD refs/remotes/origin/PROD` in portal/ → f8b1a6a9.
- Phase 1: Push local DEV → origin/DEV (7c6099d4..00f70f2d). VALGATE D-1 PASS no-op.
- Phase 2: `git worktree add .runtmp/portal-promote-v2118 PROD` → f8b1a6a9.
- Phase 3: bun install (backgrounded by Bash tool runtime, exit 0 confirmed via task completion notification).
- Phase 4: `git merge --no-ff origin/DEV -m "..."` in worktree → b742e252 (10 files, 432 insertions, no conflicts).
- Phase 4b: Parity diff EMPTY; inbox HALTGT check = clear.
- Phase 5 PUSH: `git push origin PROD` (NO MSYS_NO_PATHCONV) → VALGATE D-1 PASS + typecheck PASS → f8b1a6a9..b742e252.
- Phase 5 CI: deploy.yml 27237703259 SUCCESS.
- Phase 6 CLEANUP: `git worktree prune` (physical .runtmp removal blocked by filename-too-long — left gitignored, same as v2.1.116 session). Rule-19 intact (main tree DEV c6f12701; note DE committed c6f12701 locally during promote — separate promote).

## Signals sent

- `0.4.0_DE_ClientPlatform` — SHIPPED notice + c6f12701 awareness
- `2.0.0_SA_COO` — SHIPPED notice + full promote params
- `0.0.0_AB_MSTR` — RAVC2-CLOSE evidence + GO LD-0169 discharged

## Compiler Tools

| Tool | When | Result |
|------|------|--------|
| VALGATE D-1 | DEV push (pre-push hook) | PASS (no-op) |
| VALGATE D-1 | PROD push (pre-push hook) | PASS (no-op) |
| tsc -b --noEmit | PROD push (pre-push hook) | PASS |
| CI typecheck | deploy.yml Build job | PASS |
| comp-pipescript | N/A — portal promote, no gold scripts | N/A |
| comp-transform | N/A — portal promote | N/A |

No gold scripts or Lambda changes in this promote. Compiler tools mandate satisfied via VALGATE + tsc gate.

## Pending

- DE c6f12701 (fix MDPF_CADENCE: per-source timestamps + divergence guard) — local DEV, not pushed to origin/DEV. Separate promote required.
- Worktree physical cleanup: `.runtmp/portal-promote-v2118` left (gitignored). Would need Windows long-path fix or elevated PowerShell to remove.
