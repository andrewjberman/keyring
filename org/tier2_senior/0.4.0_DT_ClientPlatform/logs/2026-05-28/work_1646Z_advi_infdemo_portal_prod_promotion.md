# ADVI_INFDEMO IWM-demo — portal DEV push + full DEV->PROD promotion (Andrew direct)

**archetype:** DEPLOY
**date:** 2026-05-28
**worker:** 0.4.0_DT_ClientPlatform
**trigger:** Andrew direct sovereign instruction — "get all the portal edits from today committed and pushed to DEV, and then merge/deploy PROD"

---

## Current State

**SHIPPED — ADVI_INFDEMO IWM-demo bundle LIVE on PROD.**

| Step | Result |
|------|--------|
| 1 — typecheck (tsc -b --noEmit) | exit 0, zero TS errors (Andrew asked explicitly; re-run also in pre-push hook) |
| 2 — push origin/DEV | `4bdb844e..c50a58b9` (VALGATE D-1 PASS/WARN) |
| 3 — PROD scope decision | Andrew chose FULL DEV->PROD sync (vs demo-only cherry-pick) via AskUserQuestion |
| 4 — synthesize merge commit | `0b3fdba3` — tree IDENTICAL to origin/DEV, parents (b7b201a6 PROD + c50a58b9 DEV) via `git commit-tree` |
| 5 — push origin/PROD | `b7b201a6..0b3fdba3` (hook: D-1 PASS/WARN + typecheck OK) |
| 6 — CI deploy | run `26588484619` GREEN — Build + Deploy-S3/CloudFront + Tag all success |
| 7 — deploy tag | `portal-v2.1.100` |
| 8 — parent CLOUD pointer bump | `04c6a67a5` (gitlink 4bdb844e -> c50a58b9) via safe-commit.sh; pushed CLOUD |

## Final state

- origin/portal **DEV** = `c50a58b9`
- origin/portal **PROD** = `0b3fdba3` (LIVE on CloudFront)
- parent CLOUD HEAD = `04c6a67a5`, portal gitlink = `c50a58b9`
- DEV/PROD divergence ELIMINATED — PROD == DEV exactly

## Key decisions / discipline

- **Pre-flight ground-truth:** DEV was 53 commits ahead of PROD; PROD had 10 "PROD-only" commits but ALL were cherry-picks whose content lives on DEV (SSCN confirmed on DEV; TradeSubmission had zero PROD-only commits — PROD just older). DEV proven a clean content-superset of PROD => full sync drops nothing of substance. Verified before touching PROD.
- **Scope confirmed with Andrew** (not assumed): full-sync promotes 17 today ADVI_INFDEMO + 36 accumulated DEV commits since 5/15 (other pages/pods) — broader than the demo; was Andrew's explicit call. Surfaced the blast-radius tradeoff before acting.
- **Rule 19 honored** without an ephemeral worktree: merge synthesized via `git commit-tree` (tree=origin/DEV, parents=PROD+DEV) — no checkout ever happened, main tree never left DEV. Cleaner + safer than the worktree dance for a "PROD==DEV" end state; no force-push, no history rewrite.
- **Pointer recorded as DEV HEAD `c50a58b9`** (content-identical to live PROD `0b3fdba3`) to keep parent status clean + use mandated safe-commit.sh; live PROD merge SHA + tag documented in commit message.
- **F4 data-side OUT of scope** (DS INF_B_02 per-year-attribution + CF invalidation) — separate, post-demo, on COO flag.

## Compiler Tools

No comp-* tools fired — pure portal deploy (TS frontend, no Lambda IAM / data-pipeline / portal schema-graph change). VALGATE D-1 adapter-threading gate ran in the pre-push hook (PASS/WARN, non-blocking) on both DEV + PROD pushes.

## Inbox / MCP this tick

| Time | Dir | Subject |
|---|---|---|
| ~1614Z | -> COO | DT deploy-partner LIVE + ready (pre-positioning) |
| ~1616Z | <- COO | CONFIRM DT owns PROD promotion; "F4 push"=F4-suppress in same bundle |
| ~1616Z | -> COO | ACK scope locked |
| ~1642Z | -> COO | [ANDREW-DIRECT-CC] executing full DEV->PROD sync, CI in flight |
| ~1646Z | -> COO | SHIPPED — live on PROD, evidence |
| ~1646Z | -> RD 0.4.2 | FYI bundle live |

— 0.4.0_DT_ClientPlatform / archetype DEPLOY / work-cycle: INFDEMO-prod-ship
