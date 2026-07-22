# MDPF_REVAMP.S5 exact-9 cutover -- FLIP ROLLED BACK (P0). SUPERSEDES the flip-LIVE log.
**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-22 ~02:59Z -> ~04:05Z (since @1c9a8236e)

## !! CURRENT TRUE STATE (supersedes mdpf_exact9_flip_LIVE_rollback_armed.md) !!
**The exact-9 flip was applied LIVE, then ROLLED BACK on a P0. The 9 /api/general/{mdpf,portfolios}/* paths serve LEGACY portal-v2 again (NOT opal-data-assets).** Do NOT treat the flip as live. Distro EVTSA9VEHNZVH = 24 behaviors / 7 origins / no assets origin / catch-all /api/general/* -> S3-opal-data-portal-v2-json. portal-auth TF 0-diff (== pre-flip). Revert @9a5936060 (pushed).

## What happened
1. Flip applied live (all gates passed, Andrew sovereign GO). Post-flip: revert-plan HARD GATE clean-inverse (rollback armed), wiring verify 9->401.
2. **P0 found by Andrew on the LIVE serve:** (a) global aggregate-aua-timeseries data inconsistency -- opal_aggregate_aua != model_aua + non_model (excludes Inflection non-model), CTO-grounded; (b) the revamp FE was HALF-LANDED (DE's FE local-unpushed, never promoted to PROD). Two defects.
3. **ROLLBACK (Andrew + CTO + COO GO):** revert the portal-auth SERVING only.
   - Attempt-1 FAILED: `terraform` ordered the OAC DESTROY before the distro update -> DeleteOriginAccessControl 409 OriginAccessControlInUse -> apply errored, distro NOT reverted (grounded still-33-behaviors -- did NOT report success on an errored apply).
   - FIX: `safe-apply --target aws_cloudfront_distribution.portal` ONLY -> reverts the distro (remove 9 behaviors + assets origin), SKIPS the OAC destroy that deadlocked -> 24/7/Deployed, serving on portal-v2. P0 CLEARED.
   - OAC E31ME0INK9BJE1 cleaned up after (distro no longer references it -> `--target` destroy succeeded -> NoSuchOriginAccessControl). portal-auth 0-diff.
4. Ledger 20260722T0100Z CLOSED = completion-by-rollback (all 8 legs proven; NOT stranded).

## KEPT in place (CTO scope ruling -- benign, staged for the FE-FIRST re-land)
opal-assets: the bucket-policy `AllowMdpfPortalCloudFrontOACRead` (9 keys, SourceArn=EVTSA9VEHNZVH) + the published json/{mdpf,portfolios}/* keys + the publisher json/ retarget. Nothing routes to them post-rollback (no CF behavior) -> inert. NOT reverted.

## Re-land (FE-FIRST, a NEW deploy + NEW ledger, on CTO GO)
1. [DS] fix global aggregate-aua-timeseries so opal_aggregate_aua == model_aua + non_model (incl Inflection non-model); re-stage gold/mdpf_revamp/*.
2. [DE] promote the revamp FE to PROD (the half-landed defect).
3. [0.7.0_AE_CloudOps] re-populate the 9 json/ keys (publisher invoke) -> re-apply the portal-auth CF flip (diffs committed @803f8b1e7; the flip is just re-adding the 9 behaviors + assets origin + OAC) -> re-run the SAME gate battery (revert-plan HARD GATE, wiring, C-pre-flight optional, Andrew live-render). I am STAGED to re-fire on CTO GO.

## Compiler Tools
| tool | run | result | note |
|---|---|---|---|
| terraform safe-apply (--target) | rollback distro revert | PASS (after fix) | --target distro-only breaks the CF OAC-destroy-first 409 ordering race. |
| aws cloudfront get-distribution / curl | live-state grounding | PASS | grounded still-flipped after the errored attempt-1 (did NOT report success on rc=1). |
| deploy_ledger.py | close-leg L8 + close | PASS | hold REFUSED (no open legs) -> close = the correct completion-by-rollback disposition. |

- **Learning banked:** (1) CF OAC + distro revert deadlocks -- terraform may destroy the OAC before the distro drops the reference (409 in-use); fix = `--target` the distro update first, clean the OAC after. (2) On an errored apply, GROUND the live state -- never report the intended outcome; attempt-1 rc=1 left the distro still-flipped and I caught it live. (3) deploy_ledger HELD requires OPEN verify legs; a fully-proven-by-rollback ledger is CLOSED (completion-by-rollback), not held.

## Blockers
None. The flip is stood down (portal-v2 known-good serving). Re-land is gated on DS + DE (FE-first) -- a future new deploy, not a blocker.
