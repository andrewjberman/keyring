# Deploy Completion Record
**Date opened:** 2026-06-12T21:45Z (deploy start)
**Status:** OPEN
**Deploy:** NFRA_GLOBGRPH TO-MAINT -- nightly Iceberg maintenance (mark+sweep, dry-run first)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-rule gate, e38cc2b16)

---

## Manifest (all legs must verify before CLOSE)

| leg | kind | target | proof required | state |
|---|---|---|---|---|
| L1 commit | git | derive_runner.py + item2a.tf on CLOUD | commit hash pushed | pending |
| L2 tf-apply | activation | ECS task def env GLOBGRPH_MAINT_MODE=dry-run (new revision) | safe-apply + 0-diff plan | pending |
| L3 container | activation | ECR opal-globgrph-derive-runner:latest carries new derive_runner.py | CodeBuild SUCCEEDED + ECR imageDigest newer than build start | pending |
| L4 tag | git | globgrph-v0.1.15 | tag pushed --follow-tags | pending |
| L5 wiring | verify | EventBridge nightly (02:00Z) -> task def revision targeting :latest | describe task def + rule state ENABLED | pending |

## Activation note

First EXECUTION of the maintenance step = tonight's scheduled 02:00Z nightly
(dry-run mode: mark + would-delete log, ZERO deletes). That execution is the
designed activation point, not a stranded leg -- morning artifact-review item
(no-overnight-watcher doctrine): read the derive-runner log for
MAINT_SWEEP_PLAN / MAINT_DRY_RUN_COMPLETE + verify marker pin advance +
comp-kuzu post-smoke. Live-flip (GLOBGRPH_MAINT_MODE=live) is a SEPARATE
deploy after that log review.

## Pre-deploy captures (for the post verify)

- warehouse census 21:30Z: 59,537 objects (graph_nodes: 28,645 avro / 26,999 parquet / 3,821 json)
- F6 marker pin PRE: 59b0a6a9a98d7d2e @ 2026-06-12T16:15:51Z
- comp-kuzu pre-smoke: current (pin == marker HEAD), 1157 nodes
- AC-c restore drill: snapshots/20260612 tarball -> 1,159 nodes / 2,488 edges usable (PASSED 21:43Z)
