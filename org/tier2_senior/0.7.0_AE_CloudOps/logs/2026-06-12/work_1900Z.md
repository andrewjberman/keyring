# 0.7.0_AE_CloudOps — work tick 2026-06-12 ~1900Z

**archetype:** COORDINATE
**secondary_archetypes:** EXPLORE

## Window

Session start ~1855Z → ~1900Z. First tick of new session. Prior session closed at `74227f216`
(session_1812Z.md committed earlier today, full-day record). No new commits this tick.

## Startup protocol completed

- /watcher: killed orphan bash watcher PID 1019126 (prior session), armed fresh Monitor task
  `by6oog8od` (persistent). Registration re-registered (LIVE, PID 24696).
- /cloud-ops: loaded. org/XXX.md read.
- All startup steps complete (session-id file, owned-paths hook, headmove-guard, comp-graph
  context set, logs read).

## Inbox handled

- `20260612T182606Z` COO DRIVE: NFRA_OPLMCP.01 TO dispatched (573aa429f) + /log skill
  awareness. RAVC ACK sent. Priority confirmed: D8-AE Part B > NFRA_DEBTSCAN TO-D1 >
  NFRA_OPLMCP.01. /log 60m armed this tick.

## D8-AE Part B — reading + planning phase

Read all relevant source before implementing B1-B5:
- `org/modules/graph/surface_check_cli.py` — Part A implementation; SURFACE_ACK path at
  `_audit()` (L178-187). `cmd_scan()` (L258-363) has Layer-1 graph-diff + Layer-2 SHA-watch.
  `cmd_list_watched` (L235-255) is the DE handoff tool. Both layers fully implemented.
- `infra/aws/globgrph/derive_runner.py` — nightly Fargate task. `main()` flow: derive ->
  Nessie commit (commit_to_iceberg) -> F6 marker stamp -> Nessie tag -> archive. B2 scan
  step goes after `stamp_branch_head_marker()` call. Key architectural constraint: Fargate
  has NO git repo access -> Layer-2 (file-SHA-watch via `git hash-object`) NOT Fargate-
  feasible. Layer-1 (graph node-diff vs baseline.json) IS feasible if baseline available in S3.
- `infra/aws/terraform/globgrph/item2a.tf` — derive-runner ECS task + IAM. Need to add
  `sns:Publish` to `derive_runner_task` role + new `aws_sns_topic.critical_surface_alerts`.
- `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` — Item-2b Lambda.
  Already has marker-stamp flow; B4 adds SNS publish after marker stamp.
- `.tools/safe-commit.sh` — full read. B5 hook wires in at line ~270 (between contamination
  check pass and `git commit --only`). `IN_SCOPE` variable has the file list.
- `org/modules/graph/critical-surfaces.yaml` — full read. `watched_file_shas` block present
  (signed DE baseline, `portal_commit_at_sign=8b6a64666c`). 5 surfaces, 14 (surface,file) pairs.
- `org/critical_paths/`: directories `change_management/` + `stale_warning/` already EXIST
  (checked). `portal/.git/hooks/pre-push` already EXISTS (checked via `.git/modules/portal/hooks/`).

## Implementation plan (confirmed, ready to execute next tick)

**B1 (ledger wiring — surface_check_cli.py)**:
- Add `_write_ledger_entry(kind, surface_ids, context)` to surface_check_cli.py
- Call from `_audit()` (SURFACE_ACK bypass) -> writes `org/critical_paths/change_management/`
- cmd_scan() findings -> write from derive_runner scan step to S3 (Fargate can't write git repo)

**B5 (hooks — mechanical)**:
- safe-commit.sh: insert `comp-surface-check check --mode advisory` block after contamination
  check pass, before `git commit --only` (line ~270). Pass --file for IN_SCOPE files.
- portal pre-push: read existing hook at `.git/modules/portal/hooks/pre-push`, add surface check.

**B2 (SNS TF + derive_runner scan)**:
- New TF file: `infra/aws/terraform/globgrph/item2c_surface_alarm.tf`
  - `aws_sns_topic.critical_surface_alerts`
  - IAM: `sns:Publish` on derive_runner_task role
- derive_runner.py: `run_critical_surface_scan()` function; reads baseline from S3
  (`opal-313476888478-globgrph/critical-surface-baseline.json`); Layer-1 only (Fargate);
  publishes SEV1 findings to SNS; writes S3 ledger entries.
- Also: upload baseline.json to S3 via a pre-step (or separate tooling).

**B4 (incremental_updater marker-keyed)**:
- After `stamp_branch_head_marker()` in lambda_function.py: publish batch summary to SNS
  (what ARNs changed, new marker hash) — the "minutes-latency" signal for 2b-class changes.

**B3 (staleness routing)**:
- In the derive_runner scan step: check kuzu provenance header for F1 signals and write
  `org/critical_paths/stale_warning/` entries (S3) if present.

## Compiler Tools

No compiler tools run this tick — startup + pre-implementation reading/planning phase.
comp-blast and comp-iam gaps will run before any TF/code changes in the next tick (Rule 20 mandate).

| Tool | Invocation | Result |
|------|-----------|--------|
| (none this tick) | — | — startup/reading phase |

## Deployment Sequence

No deploys this tick.

## Current State

- D8-AE Part A: COMPLETE (e329623b0, RAVC3-PASS).
- D8-AE Part B: IN PROGRESS. Implementation plan confirmed. Starting B1+B5 next.
- /log 60m armed (cron pending creation this tick).
- NFRA_OPLMCP.01 TO acknowledged, queued after D8-AE Part B RAVC2 + DEBTSCAN TO-D1.

## Next Steps

- [0.7.0_AE_CloudOps] Execute B1 (surface_check_cli.py ledger wiring), B5 (safe-commit.sh +
  portal hook), B2 (SNS TF + derive_runner scan), B4 (incremental_updater), B3 (staleness).
- RAVC2 to [2.0.0_SA_COO] on B2-B5 completion.
