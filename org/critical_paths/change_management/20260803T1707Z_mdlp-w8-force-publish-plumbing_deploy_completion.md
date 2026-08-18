# DEPLOY LEDGER: MDLP_MONPUB.W8 force_publish plumbing -- opal-data-refresh-api + yang-model-portfolio-benchmarks

**Status:** CLOSED 2026-08-03 (exercise leg ran same day, 3/3 witnessed PASS; project MDLP_MONPUB closed COMPLETE Andrew-direct; header was stale)
<!-- disposition act 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md); evidence in the CLOSE block at foot. -->

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
- [x] data_refresh: map 85c9f11c4b, plan=1, safe-apply complete, 0-diff, live sha E4944Imr... (17:08Z),
      record 52cf5a3c74 (sweep-check clean), tag data-refresh-v2.6.0 verified (cat-file -> tag)
- [x] yang: map 85c9f11c4b, plan=1, safe-apply complete, 0-diff, live sha Ml7okrOe... (17:10:09Z),
      record 0b80be8f7c (sweep-check clean), deployment_map yang-v2.4.18, tag verified
- [ ] Scratch end-to-end exercise (CVO witness; entry via handle_rollback, negative control separate)
      -- OPEN: design gap surfaced to CVO/DS (scratch bucket has NO manifest S3 trigger, so a pure
      env-scoped end-to-end cannot traverse data_refresh -> SFN; design session pending)
- [x] Deploy legs closed 17:15Z; ledger stays OPEN only for the exercise leg (deploys themselves
      are COMPLETE + verified -- nothing half-landed)


---

## CLOSE (2026-08-18, 0.0.0_AB_MSTR disposition act)

The one open leg (scratch end-to-end exercise, blocked on 'scratch bucket has NO manifest S3 trigger') was unblocked
and executed 2026-08-03 itself: `e0cefc7742` (0.2.0_DT, scratch-scoped QA instance opal-data-refresh-api-qa-scratch,
same artifact) -> `624a24c4a3` (3.0.0_SA_CVO witness COMPLETE: end-to-end handle_rollback stamp landed-last, manifest-arm
bypass with rollback id, negative control refused, live serve untouched) + DS log `40ec9e8657` (3/3 witnessed PASS,
fixtures deleted) -> `dc2826c11c` (2.0.0_SA_COO: PROJECT CLOSED COMPLETE on Andrew-direct closeout; `2ad3477648` corrects
the ordering record: witness landed 18 min BEFORE the close stamp). `org/projects/MDLP_MONPUB.json` status=complete.
Only this file's OPEN header was stale.
