# MDLP_MONPUB: W8 scratch exercise fired + witnessed, project surface closed at DS seat -- 1730-1755Z

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Session Summary (third window; prior: 1500-1550Z, 1550-1700Z logs)

W8's CVO-approved (b) exercise executed and WITNESSED PASS 3/3 @624a24c4a3; both DDB fixture
records deleted with absence verified twice (mine + CVO's own get-item calls). W5's differential
acceptance PASSED via CVO's live exercise. Every MDLP_MONPUB workstream at the DS seat is now
CLOSED except W1 (deliberately blocked) and the MSTR~Z postmortem thread.

## The exercise (all on scratch; live serve verified untouched)

- DT provisioned opal-data-refresh-api-qa-scratch (identical artifact sha, BUCKET=scratch env,
  TABLE_NAME=real table, Rule-22a IAM verified). I pre-seeded: archive fixture prefix
  data-refresh/archive/exec-w8scratch/ (07-27 pkls + archived manifest) + scratch served object
  at data_as_of=2026-07-31 + flagged DDB fixture record.
- LEG 1 (end-to-end handle_rollback): POST /data-refresh/rollback on the scratch instance ->
  re-processing fallback -> newExecutionId exec-fdf49e30710f. Landed: pkls 17:44:29Z,
  manifest.json 17:44:30Z WRITTEN LAST, body carrying force_publish=true +
  rollback_execution_id=exec-fdf49e30710f inside the archived-manifest content.
- LEG 2 (yang :146 manifest arm): landed manifest verbatim as event.manifest, NO top-level flag
  -> SUCCESS, scratch flip, CloudWatch FORCE_PUBLISH line WITH the rollback id (requestId
  ed35ec26). PRE-FIRE CATCH on the record: the landed manifest has no bucket field and
  manifest.get('bucket', BUCKET) defaults to the LIVE bucket -- an unscoped invoke would have
  bypass-published 07-27 over production; disclosed event-side bucket injection scratch-scoped
  it (CVO accepted with the catch noted).
- LEG 3 (negative control): unstamped same-shaped manifest -> PublishGuardError at POST-W8 line
  numbers :361/:659 (incidental proof the new artifact ran), seed byte-unchanged (requestId
  030ed212). Plumbing did not widen the guard's default posture.
- CLEANUP (CVO GO, widened): BOTH fixture records deleted (exec-w8scratch + the rollback-created
  exec-fdf49e30710f -- post-W5 the picker faithfully surfaces everything in true recency order,
  so the rollback-created row was equally a fixture); absence get-item-verified by me AND CVO.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| aws lambda invoke x3 + dynamodb put/delete/get + s3api | exercise + cleanup | PASS | every leg pinned pre/post; absence double-verified |

No comp-graph tools this window: pure exercise/evidence work on already-grounded mechanisms;
the graph-side grounding rode the W8 commit window (prior log).

## Current State

- MDLP_MONPUB at DS seat: W2/W3/W4/W5/W8 ALL CLOSED + independently witnessed. W1 BLOCKED
  (3 preconditions, CTO amending). Postmortem/producer trace with MSTR~Z (my 2025-12-31
  dup-labels datum in their file).
- Scratch bucket: self-expires 7d; no sweep owed. Scratch instance opal-data-refresh-api-qa-scratch
  exists (DT TF; teardown is DT's call post-project).
- Production: frontier 2026-07-31 served; guard live + fully exercised; rollback paths plumbed
  (re-processing) with Path-1 version-restore residual honestly recorded.

## Next Steps

1. [0.2.0_DS -- me] Act on W1's amended TO when cut; support MSTR~Z postmortem on request.
2. [0.2.0_DT] Scratch-instance disposition post-project (keep as standing QA harness vs teardown).
