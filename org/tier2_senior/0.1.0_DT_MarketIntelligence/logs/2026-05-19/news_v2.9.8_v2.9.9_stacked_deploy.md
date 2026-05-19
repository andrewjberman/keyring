# MKOV — Stacked Deploy: news-v2.9.8 + news-v2.9.9 (ADHC_CRYPCT.001)
**Date:** 2026-05-19
**Agent:** 0.1.0_DT_MarketIntelligence
**Tags:** `news-v2.9.8` + `news-v2.9.9` (stacked back-to-back per CTO Option B)
**Co-driver:** 0.7.0_AE_CloudOps (deployment-infra lane: source-map commit, terraform apply, tag push)

## Context

Two RAVC-Requests in inbox at session start:
- 2026-05-12 (7 days stale) — DS `news-v2.9.8` for the May 12 fix `c72c9368a` (recency-dominant trending + crypto source cut)
- 2026-05-11 (8 days stale) — COO org-wide commit/push hygiene sweep

Phase 0 finding (DS audit during this session): all 3 news Lambdas had been running 14-34-day-old code; my 2026-04-28 v2.9.7 deploy was the last actual ship. DS's news-v2.9.8 ACK had been sitting in my inbox 7 days. Underlying structural gap is that news-pipeline doesn't have the continuous-deploy hook flow that ADHC_DSFLOW.005 added to gold scripts — filed as future-work in the DS brief.

## Sequencing — How v2.9.8 + v2.9.9 Resolved

| Event | Time | Detail |
|-------|------|--------|
| DT picks up DS RAVC-Request | 14:45Z | Ack sent; COO sweep CLOSED ("no Pod 1 dirty state") |
| DT pre-build gate (filtered) | 14:47Z | `git status --porcelain -- <Lambda paths>` empty — INSUFFICIENT (didn't catch WIP arriving later) |
| DT build-and-upload x3 | 14:48-14:50Z | SHAs `Q3IjW.../cQfTy.../82wzL...` uploaded to S3 (clean c72c9368a content, verified later by determinism) |
| DT source-map commit attempted | 14:50Z | **Blocked by owned-paths hook**: `lambda-source-map.json` in `CLOUD_OPS_OR_ETL` lane (AE-only); POD1_OR_AE carve-out (e4e4d9789 2026-05-12) covers Lambda source but not source-map. Clean-reroute to AE 0.7. |
| DT reroute to AE 0.7 | 14:50Z | MCP w/ structural gap surface; CC COO. AE 0.7 ACK + ETA ~10-15 min |
| **AE 0.7 HALT** | 15:10Z | AE caught WT-vs-origin/CLOUD divergence on news_layer3 + news_trending — ADHC_CRYPCT.001 WIP content present. AE Rule 2 stop, route back. |
| DT verifies AE catch | 15:13Z | `git status --short -- infra/aws/lambda/` confirmed M markers; `git diff origin/CLOUD` confirmed ADHC_CRYPCT content. DS LIVE summary: "ADHC_CRYPCT.001 Phase 0 audit running — CTO surfaced for sequencing call" |
| DT pings DS + AE + COO | 15:13-15:14Z | Hold posture until CTO answers DS's open sequencing surface. **Do not commit DS's WIP under DT author** (attribution forgery). |
| DS commits WIP `39bc01c3b` | 15:18Z | CTO Option B RATIFIED via DS — full TO scope, stacked back-to-back v2.9.8 then v2.9.9 |
| DT restores WT to c72c9368a | 15:25Z | `git restore --source=c72c9368a --worktree -- <2 Lambda files>` (worktree-only, no index contamination) |
| DT rebuild for v2.9.8 | 15:26Z | **Identical SHAs to first build** (Q3IjW.../cQfTy.../82wzL...) — proves first build was always clean c72c9368a content. AE halt was a false-alarm on artifact content but correct discipline read. |
| DT RESUME ping → AE | 15:27Z | Pre-commit round-trip evidence: WT blob hashes match c72c9368a; source-map dirty exactly 3 SHA bumps; index clean. |
| **AE 0.7 ships v2.9.8** | 15:33Z | Source-map `60ff5d267`, recommit `4beb59a4a`, tag `news-v2.9.8` pushed, terraform 0-diff verified, live CodeSha256 == source-map for all 3 |
| DT restore WT to HEAD | 15:35Z | `git restore --source=HEAD --worktree -- <2 Lambda files>` |
| DT rebuild for v2.9.9 | 15:36Z | New SHAs: `GZ2Q9.../ZZWPyE...` (news_ingestion `Q3IjW...` unchanged — no-op confirms determinism) |
| **Race condition** | 15:36Z | Andrew direct-pinged AE asking about v2.9.9; AE announced full pickup before seeing my GO; DT race-prevention ping. Resolved deterministically — same SHAs either way. |
| **AE 0.7 ships v2.9.9** | 15:44Z | Source-map `815791d85`, recommit `f26252a23`, tag `news-v2.9.9` pushed, terraform 0-diff, live CodeSha256 == source-map |

## Deployment Tags

| Pipeline | Tag | Source-map commit | Recommit | Deployed content commit |
|----------|-----|-------------------|----------|------------------------|
| news-pipeline | `news-v2.9.8` | `60ff5d267` | `4beb59a4a` | `c72c9368a` (WT-restored at build time) |
| news-pipeline | `news-v2.9.9` | `815791d85` | `f26252a23` | `39bc01c3b` (= HEAD at build time) |

## Verification (post-v2.9.9, AE-reported)

All 3 Lambdas LastModified `2026-05-19T15:38:55Z`:

| Lambda | CodeSha256 | Match source-map |
|--------|-----------|------------------|
| news-ingestion-scheduler | `Q3IjWURrQzHoJrN1+Lp88/D4b+hW7CYTSCX5OyClVm8=` | YES (unchanged content across v2.9.8 + v2.9.9) |
| news-trending-analysis | `GZ2Q9tRrgjno30b0khwoCA0GPTsNLliZk9f/0uu/5tI=` | YES (v2.9.9 GPT-keep-list scrub) |
| opal-news-layer3-curation | `ZZWPyE2w37etOX9U+0NFZ+iG8AmFPaTUYsz1dvKfJwY=` | YES (v2.9.9 4-layer rip-out) |

## Compiler Tools

| Tool | Run | Why / what it caught |
|------|-----|---------------------|
| comp-pipescript io / deployed / postdeps | NO | **Discipline gap.** None run this session. Pre-build state check relied on `git status --porcelain -- <paths>` (filtered) which was insufficient — see below. |
| comp-blast | NO | Should have run on the 3 Lambdas to check downstream blast radius before deploy. |
| comp-iam service | N/A | No new boto3 calls in either commit. |

**Discipline note:** the session was inbox-triage-driven (7-day-stale DS RAVC-Request) and I went straight to build without comp-* checks. The omission didn't bite because the deploy was a code-only update (no IAM, no Terraform, no schema) — but the pre-build gate weakness (working tree content not verified independently against committed HEAD across ALL Lambda paths) did bite. Captured to memory as `feedback_build_zips_working_tree_not_committed_head.md`.

## Structural Findings Surfaced This Session

1. **POD1_OR_AE carve-out gap for `infra/aws/lambda/ci/lambda-source-map.json`** — the May 12 carve-out (e4e4d9789) enables POD1 to author Lambda source but doesn't reach the source-map JSON or per-pipeline CHANGELOG.json. Result: POD1 DT cannot complete deploys self-serve. COO weighed in: leaning toward ratifying current AE-owns-source-map design with prompt reword (option b). Andrew decision pending. TO candidate.

2. **build-and-upload.sh zips working tree, not committed HEAD** — caught empirically when DS's WIP edits hit the shared WT between DT build (14:48Z) and AE check (15:10Z). False-alarm-but-correct-discipline by AE. Captured to memory; cross-cousin to AE's `feedback_s3_pull_dispatcher_no_auto_propagate`.

3. **`.tools/safe-deploy.sh:37` MSYS path-mangle** — AE 0.7 surfaced during v2.9.9 push: `exec "$PYTHON" "$SCRIPT_DIR/safe_deploy_core.py"` with `/c/Users/...` resolves to `C:\c\Users\...` on Windows native python. Push completed (sub-process exit ≠ hook exit) but noise misleading. Same class as ds-commit-gate.sh MSYS-path-mangle. **ADHC_DSFLOW.007 (dispatch-held) is the right vehicle** — AE recommends COO expedite dispatch since we just empirically hit it.

4. **news-pipeline lacks ADHC_DSFLOW.005-style continuous deploy hooks** — DS observed in Phase 0 audit. Lambda LastModified was 14-34 days stale across all 3. ADHC_DSFLOW.005-style `safe-deploy.sh` + pre-push integration for Lambda deploys would prevent 7-day inbox lag from re-occurring. DS filed as future-work in `docs/briefs/adhc-crypct-comprehensive-crypto-removal-20260519.md`. Worth a structural ADHC project.

## Current State

| Item | Status |
|------|--------|
| news-v2.9.8 | SHIPPED — tag pushed, terraform 0-diff, live SHAs verified |
| news-v2.9.9 | SHIPPED — tag pushed, terraform 0-diff, live SHAs verified |
| Source-map per-Lambda last_deployed_commit | Updated by AE's record-terraform-deploy.sh |
| deployment_map.xml | UPDATED (this commit) — news-pipeline current_tag → news-v2.9.9; 3 deployed Lambdas updated with SHAs + supersession notes |
| RAVC-Validate to DS | PENDING this commit — combined v2.9.8 + v2.9.9 |
| Memory: `feedback_build_zips_working_tree_not_committed_head` | WRITTEN + indexed in MEMORY.md |
| POD1_OR_AE carve-out source-map gap | Surfaced to COO; Andrew-decision pending |
| ADHC_DSFLOW.007 MSYS path-mangle in safe-deploy.sh | Surfaced by AE; AE recommends COO expedite dispatch |
| news-pipeline continuous-deploy hook gap | Surfaced by DS in v2.9.9 brief; structural ADHC candidate |

## Next Steps

1. **[me]** Send RAVC-Validate to DS combined (v2.9.8 + v2.9.9, with live SHAs + tag commits). DS will run 24h verification window on portal Trending Topics output.
2. **[me]** Commit + push this session log + deployment_map.xml update (single commit under POD1 lane).
3. **[DS 0.1.0]** 24h portal/CloudWatch verification: no crypto-tagged topics, BLOCKED: CRYPTO log lines firing, BLOCKED: SOURCE @ 30% threshold.
4. **[DE 0.1.0_DE]** Word-cloud consequence — TOP_20_KEYWORDS dropped 18 → 16; DS suggested DE coordinate substitute keywords (apple, tesla) if needed; could ride a v2.9.10 if necessary.
5. **[COO]** Triage ADHC_DSFLOW.007 dispatch (MSYS path-mangle in safe-deploy.sh — AE surfaced).
6. **[COO]** Resolve POD1_OR_AE carve-out source-map gap (Andrew-decision-pending; AE proposed option-b ratify + prompt reword).
7. **[CTO/COO]** Consider ADHC_DSFLOW-style continuous-deploy hooks for news-pipeline (DS-surfaced).

## Do NOT rules (from this session)

- DO NOT trust truncated session-start gitStatus. Re-run unfiltered `git status` + per-Lambda blob-hash check before every build.
- DO NOT commit another agent's uncommitted WIP under your author — attribution forgery. Hold posture is the answer; route via owner.
- DO NOT pre-empt an open sequencing surface (e.g., DS-to-CTO) by unilateral action.
