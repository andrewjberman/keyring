# 2026-07-23 — Cottonwood MDPF FE Promote (DEV->PROD) — EXECUTED + LANDED

**archetype:** DEPLOY

## Session purpose
Respawned by MSTR ~0133Z on Andrew's direct word ("use 0.2.0_DT") to own the portal DEV->PROD
promote for the Cottonwood MDPF page go-live — the LEGACY-family serve amendment, NOT the revamp
cutover (LD-0330 flip gates untouched). CTO stood down from self-execute at 013340Z.

## What happened (chronological)
1. **Startup:** /watcher armed FIRST per MSTR (Monitor task bpnz2e4zb, no orphans; registered
   PID 32300; LD-0290 serial file written; XXX.md steps complete). Spawn-arrival acked to CTO.
2. **Pre-stage (before DE's commit):** delta origin/PROD..origin/DEV verified = 8 commits, all
   MDPF-surface, matching CTO's package; portal tree on DEV in sync; DE's 4 in-flight modified
   files identified and left untouched; gh auth confirmed; /prod-deploy loaded.
   Flagged: Temp/claude/reland-prestage worktree held PROD (clean, exactly at origin/PROD
   885b76c2). CTO approved removal 013937Z on the grounded state (stateless by definition).
3. **GO (CTO 014410Z):** DE's f8ace4f8 gated in + pushed (delta -> 9). Promote-begin signaled to
   COO; freeze window active.
4. **Execution (/prod-deploy, no deviations):**
   - Step 1: tree clean of tracked changes (untracked scratch dirs only — other lanes', cannot
     ride into an origin-ref merge), local DEV == origin/DEV f8ace4f8.
   - Step 2: tsc -b --noEmit clean.
   - Step 3: update-ref PROD -> origin/PROD 885b76c2; reland-prestage removed (prune; physical
     dir persists on the Filename-too-long class, inert).
   - Step 4: ephemeral worktree .runtmp/portal-promote-20260723T014559Z; bun install FOREGROUND
     (99s, 420 pkgs); merge --no-ff clean (6 files +602/-120, rollback SHA in message); parity
     gate EMPTY; push accepted 885b76c2..5ef8bc63 (VALGATE D-1 PASS, push-time tsc PASS).
   - Step 5: CI run 29972762013 conclusion: success via gh run view --json (background
     until-loop, never gh run watch). Tag portal-v2.1.142 peeled ^{commit} == PROD head.
   - Step 6: pointer commit CLOUD c91595d7b via safe-commit under my author line, pushed.
   - Step 7: worktree pruned; main tree verified DEV; ended at workspace root.
   - Step 8: RAVC artifact-table reports to COO (freeze released) + CTO; DE triggered 015252Z
     for the through-auth live render check (final gate leg — DE's evidence closes go-live).
5. **Records:** deploy-completion ledger entry
   org/critical_paths/change_management/20260723T0145Z_cottonwood-mdpf-fe-promote_deploy_completion.md
   (CLOSED; NEVER#5/#7 satisfied — begun and finished in-session).

## Current state
- Live PROD = 5ef8bc63 (portal-v2.1.142), carrying the Cottonwood MDPF page.
- Workspace CLOUD = c91595d7b (portal pointer -> f8ace4f8).
- Awaiting DE's render evidence (their leg, triggered, ground truth named).

## Do NOT
- Do not conflate this legacy-family FE promote with the MDPF revamp cutover — LD-0330 flip
  gates are a separate machine, untouched tonight.
- Do not re-run/close anything on the reland-prestage physical dir in Temp — inert, tracking pruned.

## Compiler Tools
| Tool | Run? | Result |
|---|---|---|
| (none) | — | No comp-tool run: this session was a pure portal-repo git promote per the /prod-deploy skill — no estate search/inspection, no infra/IAM/data-pipeline surface touched; every verification was on the live primitive the skill names (git refs, gh run view --json, peeled tag). |

## Blockers
None. Mission complete on my leg; DE's render evidence is the residual (theirs).

## Next steps
- [0.2.0_DE_PortfolioAnalytics] through-auth live render on served domain, report evidence.
- [me] event-driven standby; broker summary kept accurate.

---

# ADDENDUM 13:0xZ — Second promote same day: corrected band FE (v2.1.143)

**archetype:** DEPLOY

COO dispatch 124649Z (co-sign complete, Andrew asking) + CTO NO-STOP 125422Z (live unlabeled-estimate
exposure since 12:03Z). Executed /prod-deploy again: delta 5 commits all 3F-BF2, head 58a38078;
tsc clean; merge parents d270acc9 == 5ef8bc63 + 58a38078 exactly; parity EMPTY; provenance guard +
VALGATE + tsc PASS at push; CI 30009240873 success; tag portal-v2.1.143 peeled-verified; pointer
CLOUD 525a7296b; worktree pruned; main tree DEV; DE triggered 130150Z for yellow-dash live check.

**CORRECTION on the record:** 525a7296b's message says pointer -> 58a38078 but the gitlink recorded
0a261c74 (DE's Global-prep commit landed on DEV mid-promote). Pointer VALUE correct (== origin/DEV);
message wrong; authoritative correction in the deploy-completion ledger
(20260723T1247Z_cottonwood-band-fe-promote_deploy_completion.md). Verified 0a261c74 NOT in PROD.
DE's freeze-window DEV push surfaced to COO (zero operational impact, post-PROD-push).

Compiler Tools: none run — same rationale as the main entry (pure portal git promote; verifications
on live primitives: git refs/parents/merge-base, gh run view --json, peeled tag).

---

# ADDENDUM 13:4xZ — P1 fix-forward promote (v2.1.144): 49F/Inflection crash

**archetype:** MIXED (DIAGNOSE + DEPLOY)

Andrew-direct at my terminal ~1332Z: Inflection + 49F dropdowns crash (TypeError null.date).
DIAGNOSIS (mine, source+artifact-grounded): pairedProvenanceRead.ts:100 length-only guard vs
pre-contract cohort_provenance in the 07-18 artifacts (inflection 429/429 null; 49f 347 null +
82 date-less old-schema). Cottonwood clean (same-day re-emit) = why v2.1.143 acceptance missed it.
Dispatched DE (0.4.0 -- corrected addressing, channel-push confirmed) + CTO + COO with fix shape.
CTO ratified fix-forward 133702Z w/ 4 conditions; DE gated 5bb54ecf 1341Z (mutant-controlled on
real bytes); promote fired 1341Z -> PROD ffc022ed (portal-v2.1.144) -> CI 30012584835 SUCCESS
1347Z. Pointer ff1254d9b, gitlink VERIFIED pre-commit (v2.1.143 lesson). ~15 min report-to-live.
Residual: DE condition-3 three-firm live verify (triggered). Ledger:
20260723T1341Z_p1-provenance-read-fix-forward_deploy_completion.md.
Also this window: answered Andrew's Global-$1.78B question grounded (cottonwood absent from served
platinum aggregate -- not CloudFront; Global re-emit chain is COO's, in flight).

Compiler Tools: none run -- diagnosis grounded on live primitives (served S3 artifact bytes via
rail-checked aws cp/ls, git show on the introducing commits, source read of the throw site); the
crash path was FE-local (no estate coupling a comp-tool would add).
