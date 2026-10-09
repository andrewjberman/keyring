# Deploy Completion Record
**Date opened:** 2026-10-09T10:11:58.780279+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1: irpt-status RELEASE 1 (ticket-binding read side AR-y-11 + original-file reader AR-y-22) PLUS one API route, PINNED to 3a6d021e4a, built WTGCJPiSEWSack1XvAMRyTGSVLX84VSm+3eC3eSPgsQ=, over live E7VKvhg3E9D5euWO+S649/iyAJ05xUmFPqHEAKDTFxA= with rollback source S3 version 2R.qpR7BQnBXtBgcR87_keqLT5Tg96Jl
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 pre-checks in the detached pin worktree /c/dev/anl-r1-pin | the pin is an ancestor of origin/box/dell2 with a behaving positive control; the census at the pin reads changed_members=5 and they are acceptance, entry, owned_report, pdf_link, submission; live is E7VKvhg3...; the rollback S3 version is recorded | ALL FOUR STEP-0 PRE-CHECKS PASS, measured in the detached pin worktree /c/dev/anl-r1-pin at 3a6d021e4a (0 uncommitted), which the order requires for build, plan and apply -- never at HEAD. (a) git merge-base --is-ancestor 3a6d021e4a origin/box/dell2 rc 0, with a POSITIVE CONTROL (HEAD~80) also rc 0, so the zero is the world and not a dead command. (b) release-census.py irpt-status --pin HEAD: built_members=49 live_members=49 changed_members=5, and the five ARE the five the order names -- acceptance.py, entry.py, owned_report.py, pdf_link.py, submission.py -- with nothing added and nothing removed. The pin own drain message independently states the same five, so the census and the drain record agree. (c) live CodeSha256 E7VKvhg3E9D5euWO+S649/iyAJ05xUmFPqHEAKDTFxA= EQUALS the order declared live/rollback value, LastModified 2026-10-09T07:43:46Z (IB-pr-395). (d) ROLLBACK SOURCE RECORDED: S3 object version 2R.qpR7BQnBXtBgcR87_keqLT5Tg96Jl, whose OWN content-sha256 metadata reads E7VKvhg3..., i.e. that version is self-consistently the one carrying the live bytes rather than one believed to. | CLOSED 20261009T101216Z |
| L2 | s3-prefix | build and upload irpt-status from the pin worktree | the uploaded sha256 is WTGCJPiS... or STOP, AND symbol_closure on the uploaded zip downloaded back BY VERSION reads missing=0 or STOP |  | OPEN |
| L3 | activation | two safe-applies, OPS FIRST then API | ops -target=module.irpt_status touches s3_object_version and source_code_hash ONLY; api untargeted is 1 to add, the single route GET /api/scoped/investor-reporting/analysis/requests/{requestId}/original; ANY other line in either plan is a STOP, and both plan texts are committed before either apply |  | OPEN |
| L4 | verify | after-reads 1 to 5 in order | live == WTGCJPiS and both re-plans 0; the route census reads EXACTLY ONE and the filer GET answers 200; read 3 three arms with the signed link NEVER logged or written (sha256 and expiry only); read 4 returns ticket_id and meets OwnedAnalysisRequest; read 5 analysis-request-pdf behaves as before. read3_objects recorded with deleted_on_andrews_word false |  | OPEN |
| irpt-status | tf-lambda | irpt-status | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T101158Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)
- 20261009T101216Z LEG L1 closed: ALL FOUR STEP-0 PRE-CHECKS PASS, measured in the detached pin worktree /c/dev/anl-r1-pin at 3a6d021e4a (0 uncommitted), 

## HOLD -- no upload, no apply -- recorded 2026-10-09T10:4xZ by 0.7.0_AE_CloudOps~DELL2

Authority: 2.0.0_SA_COO~Y2 msg 3141, on 1.0.0_SA_CTO~DELL2 msg 3140 (row IRPT_BCKEND-D2-S43). The
release-1 CTO half gains a condition: the _authz unguarded-route census must PASS at the release
pin, and at 3a6d021e4a it FAILS on the /original route. A re-pinned amendment follows.

STATE WHEN THE HOLD ARRIVED, which is why this costs nothing to honour: leg L1 was closed on the
step-0 pre-checks and NOTHING ELSE had run. No build, no upload, no plan, no apply, no route
change. L2, L3 and L4 are open-unapplied. There is no half-landed state to unwind and no rollback
owed -- the rollback source S3 version 2R.qpR7BQnBXtBgcR87_keqLT5Tg96Jl is still the live bytes
because nothing displaced them.

WHAT STAYS TRUE from L1, so the re-pinned amendment need not re-measure it: the pin was an
ancestor of origin/box/dell2 with a behaving positive control; the census at the pin read
changed_members=5 and they were the five the order names; live was E7VKvhg3...; and the rollback
version carries those same live bytes by its own metadata.

The ledger is left OPEN-UNAPPLIED rather than closed, because the order is expected to return by
amendment on a new pin and its L1 evidence is worth keeping attached to this entry.
