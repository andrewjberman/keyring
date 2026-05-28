---
work-cycle: 0002
serial: 0.7.0_AE_CloudOps~B
date: 2026-05-28
tick_z: 0018Z
classification: substrate-authoring (no apply yet; pre-apply commit per Rule 2)
ravc: RAVC1-PLAN MCP to ws COO `20260528T001823Z` (Ship A + Ship B substrate ALL authored; apply gates pending)
---

# /work cycle 0002 — Ship A chassis + Ship B AC-T2 substrate (bundled)

## Substrate authored (Step 3)

7 files this cycle:

### Ship A — Phase 2B chassis (per ws COO 23:44Z option (b) ratify)

- `infra/aws/terraform/imo-pipeline/phase2b-secrets.tf` (new; 6 named per-board secret placeholders)
- `infra/aws/terraform/imo-pipeline/phase2b-eventbridge.tf` (new; header-comment chassis)
- `infra/aws/terraform/imo-pipeline/phase2b-lambdas.tf` (new; header-comment chassis)

Targeted plan validated cycle 2: `-target` on 6 secrets shows 6 to add no error.

### Ship B — AC-T2 scraping_browser1 v0.3.0 substrate (per ws COO 23:44Z §2 sister-coord)

- `infra/aws/terraform/imo-pipeline/phase1-scraping-browser-lambda.tf` (new; `find_insure_crawl_web_scraping_browser` module + EB permission; references existing source `40b18d724`)
- `infra/aws/terraform/imo-pipeline/secrets.tf` (amended; +`bright_data_scraping_browser_creds`)
- `infra/aws/terraform/imo-pipeline/layers.tf` (amended; +`find_insure_browser_deps` layer stub)
- `infra/aws/lambda/ci/lambda-source-map.json` (amended; +`find-insure-crawl-web-scraping-browser` entry with `_pre_stage: true` mirroring `find-insure-serving-consolidate` convention)

## Apply gates (3)

1. **Phase 3 contamination** — preexisting untracked `phase3-serving-consolidate-lambda.tf` references missing S3 artifact, breaks full-module plan. NOT MINE (AE 0.7~C / DS~E pre-stage with same `_pre_stage` flag in source-map). Cleared by either artifact upload OR my Rule-2 dispense + targeted apply.
2. **Ship A apply** — needs ws COO Rule-2 dispense per my 00:05Z RAVC1-PLAN ask (still pending).
3. **Ship B apply** — needs (a) build-layer.sh authoring for find-insure-browser-deps (b) layer-zip build + upload (c) Lambda-zip build + upload (d) blocker 1 clear.

## Sister-coord chain

- AE 0.7~A: Phase 1 Stage 1 RAVC2 23:32Z STAGE1-HALT; Stage 2 prep + W1-taxonomy-refinement re-grade pending ws CTO W1 refinement ship
- AE 0.7~C / DS~E: Phase 3 serving-consolidate W3 TO .023 pre-staged (TF + source-map; both `_pre_stage:true`); blocked on FIND_INSURE.008 AC7 RAVC2-Accept
- AE 0.7~B (me): Ship A chassis + Ship B AC-T2 substrate authored; apply gated
- DS~C: Phase 2A live-dispatch + .027 endpoint exploration
- DS~D: Phase 2B HAR + .028 multi-board manifest
- DS~A: Phase 1 silver Rule 17 fix landed `3ee6ee869`; (b)(ii) closed

All FIND_INSURE-prioritized per Andrew 22:49Z + 23:25Z.

## Commit + push (Step 5)

This cycle commits the 7 substrate files via safe-commit pathspec scoping (excludes Phase 3 contamination untracked file structurally per Rule 14a). work-cycle:0002 commit tag.

## RAVC1-PLAN dispatch (MCP `20260528T001823Z` to ws COO)

Full apply sequence proposed (10-step) once blocker 1 clears. Tags planned: `imo-pipeline-phase2b-v0.0.0` (Ship A) + `imo-pipeline-v0.6.0` (Ship B; sequential after v0.5.0).

## Standing posture

Cron next /work tick :27Z. Awaiting COO disposition on Rule-2 dispense + Phase 3 blocker-1 clearance.

— 0.7.0_AE_CloudOps~B — 2026-05-28T~00:18Z
