# DEPLOY LEDGER: MDLP_MONPUB.W8 force_publish plumbing -- opal-data-refresh-api + yang-model-portfolio-benchmarks

**Opened:** 2026-08-03T17:07Z by `0.2.0_DT_PortfolioAnalytics` (at deploy START, per NEVER#6)
**Status:** **OPEN -- deploy in progress**

## Authorization
- CTO GO 20260803T163903Z (W8; TO in DS task_orders/; my grounding report 163640Z accepted in full).
- Code: DS `4024664d71` -- ONE event-contract commit across both Lambdas:
  data_refresh fallback stamps archived manifest force_publish=true + rollback_execution_id,
  writes uploads/manifest.json LAST (drive-by: listing-order trigger race closed);
  yang reads top-level OR manifest-level, bypass log carries rollback_execution_id.
  Path 1 (version-based raw copy) OUT OF SCOPE and stated so in the TO.

## The change
- data_refresh: baseline (deployed W5) `Z3rt+Opu...` -> `E4944Imr7Y4S4//rTR6HN5sbwczbwLw5DcaH4IZ0D0E=`
  (carries W5+W8 both on HEAD; single deploy).
- yang-model-portfolio-benchmarks: baseline (deployed W2) `5EPfYG...` -> `Ml7okrOe6+2uT+hZScO6u3aSg8/lbacrD4Q1g8z74uY=`

## Legs
- [ ] data_refresh: map commit, plan=1, safe-apply, 0-diff, live sha, tag data-refresh-v2.6.0 verified
- [ ] yang: map commit, plan=1, safe-apply, 0-diff, live sha, deployment_map, tag yang-v2.4.18 verified
- [ ] Scratch end-to-end exercise (CVO witness; entry via handle_rollback, negative control separate)
- [ ] Ledger closed
