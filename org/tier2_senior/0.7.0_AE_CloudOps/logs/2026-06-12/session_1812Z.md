# 0.7.0_AE_CloudOps — session 2026-06-12 (full-day record; extends session_1310Z.md)

Long session. Three arcs: (1) the GLOBGRPH F-series wave + AM tails, (2) the CVO stress-test
re-engagement (P0/P1s -> TO-F6 + TO-P1 + container rebuilds), (3) Andrew-direct work (comp-queue
feature + 2 management/physical SVGs) and D8-AE (comp-surface-check). All RAVC-closed except the
explicitly next-session remainder. Startup: /watcher + /cloud-ops + org/XXX.md (logged 1310Z).

## ARC 1 — original GO'd batch (all CLOSED)
- **tf-plugin-cache P1** — 20.6GB reclaim (97%->88%); premise corrected (Windows COPIES, no symlink
  dedup w/o Dev Mode); Dev-Mode enable handed to Andrew. Memory: reference_tf_plugin_cache_windows_copies_not_symlinks_needs_dev_mode.
- **TO-F1** (a84de54a5 + comp-tools a4e486b74; manifest 08475dbeb COO) — kuzu provenance manifests +
  comp-kuzu header (AC10a) + F4 force-default. F4 phantom-collapse 24831->1157.
- **Item-2b** (8d1ca4ea9 + zip; DEPLOYED globgrph-v0.1.10) — delete-propagation; S3 DeleteBucket no
  longer resurrects. FLAGGED derive_runner .tf drift.
- **drift-revert** (c3d9b3349, CTO 9f18d595d) — local.nessie_uri -> bare; full plan 0/0/0.
- **TO-F2** (engine edaa8d410 + flip 9df81aca5 CTO cert 8dda8c663 + comp-tools 59ee0341a; manifest
  703c700b5 COO) — comp-kuzu default = canonical kuzu_nessie_db + HEAD-advance auto-refresh, mutex +
  atomic swap + orphan-lock-steal. AC10b/c demo: 4-way concurrent, 1 rebuild, oracle 1157, no leak.
- **TO-F3** (7cfefd450) — comp-aws snapshot --commit-to-nessie opt-in (in-VPC live demo deferred).
- **trade-recon-api 77005oklok DELETE** — 4-step destructive gate; teardown residue closed.
- **DTAFLP TO-6** — verified already-landed (55a61c43a).
- **IAM strip** — CLOSED no-op (premise falsified; trade-submission-lambda-role has 0 recon refs).

## ARC 2 — CVO stress-test findings (dc06744c6) (all addressed)
- **P1-B** (35c9d4f14) — kuzu_cli read_only=True; 8/8 concurrent reads, 0 lock collisions (was 1-of-8).
- **P0 -> TO-F6** (3 parts; Part1 34dd68f70, Part2 dd58500c2 DEPLOYED globgrph-v0.1.11, Part3 c101cbfc7
  + comp-tools 24da06b27 + manifest 4c2b55c7b COO) — root-caused c454b6cd as an orphan-metadata
  artifact (mtime-scan != HEAD; 3096 files). Replaced HEAD oracle with the writer-stamped
  _branch_head.main.json marker; mtime-scan RETIRED. Reader proven on dev box; live AC10b/d -> CVO.
- **URGENT container rebuild** (CTO 984773e0e, pre-02:00Z) — Docker down locally -> built in AWS
  CodeBuild (reused semantic-clustering project's ecr:* role + source-override). :latest 240164dc
  (marker), then 85d8d4fc (marker+CAS). Closed the silent-morning-gap. Memory candidate: CodeBuild-
  via-source-override path for globgrph (no dedicated project).
- **TO-P1** (a613084cb; DEPLOYED v0.1.12 + container 85d8d4fc) — fast-forward CAS + orphan
  self-detection on both pyiceberg-overwrite writers (commit_batch + derive_runner). Uses the iceberg
  snapshot parent_snapshot_id lineage (dev-box-testable) vs raw Nessie-REST. Unit-proven.
- **P1-A** (egress S3-only) — COO ruled option-c (fabricate-from-event), deferred no-urgency.

## ARC 3 — Andrew-direct + D8-AE
- **TO-Q1 comp-queue MVP** (f13c0d069) — PENDING line in comp-kuzu header via non-destructive
  sqs:GetQueueAttributes; surfaces in-flight (uncommitted) 2b events. v2 (ARN index) held.
- **2 SVGs on Desktop** — Opal-Cloud-Map.svg (management) + Opal-Cloud-Map-Physical.svg (agents +
  queue + Kuzu + Nessie/Fargate). Generators in .runtmp/.
- **D8-AE Part A** (comp-surface-check, e329623b0) — commit-time critical-surface gate; SEV1
  block-with-ack / SEV2 warn; severity_resolution; portal-submodule-aware; SURFACE_ACK audit.
  AC8 selfcheck PASS.
- **D8-AE Part B/B2 scan** (1f2e64a75) — 2-layer: Layer-1 graph-drift + Layer-2 file-SHA-watch.
  DESIGN FINDING: global-graph baseline blind to BenchmarkHeatmap/portal-proxy/PeersTab (0 graph
  nodes) -> flagged -> CTO Q1 approved baseline extension -> DE re-signed F6-anchored watched_file_shas
  (c2aebe4ed) -> Layer-2 closes the Benchmark SEV1 blind-spot. Validated live: clean at signed commit,
  synthetic Benchmark edit -> SEV1 [PAGE] [file-SHA-watch]. **TRAP CAUGHT:** git hash-object (git
  normalization) vs raw-bytes -- Windows CRLF would false-alarm every portal file (COO banked).
  list-watched-files = DE handoff. RAVC3-ACCEPT (COO: detection proven).

## Flags routed
- derive_runner .tf drift -> CTO (option-b, reverted, 0/0/0).
- 7 INF comp-constants drifts -> MSTR.
- Writer-residual (orphan lineage) -> TO-P1 (built).
- BenchmarkHeatmap/portal-proxy/PeersTab 0-graph-nodes -> CTO noted as DEBTSCAN 2a backlog.

## Deploys (Rule 1/2)
- globgrph-v0.1.10 (Item-2b), v0.1.11 (marker), v0.1.12 (CAS) -- each CodeSha256-verified + targeted 0-diff + tagged + pushed.
- globgrph drift-revert apply -> 0/0/0. derive_runner container :latest 240164dc -> 85d8d4fc (CodeBuild).

## NEXT SESSION (queued, COO-confirmed)
- D8-AE Part B remainder: SNS topic opal-critical-surface-alerts + derive_runner post-load publish
  step (container rebuild) + B1 ledger + B3 staleness routing + B4 marker-keyed real-time + B5
  advisory hook. Advisory->blocking flip gated on COO's 3 conditions (post-resign+CVO / one nightly
  synthetic-fires+Day-0-suppressed / 0-FP-SEV1-routine).
- NFRA_DEBTSCAN TO-D1 (reachability sweeps) + TO-D2 IAM (comp-iam gaps).
- NFRA_OPLMCP sub-stream TOs (incoming).
- Andrew: Dev-Mode enable; probe-bucket `!` delete (also fires the live marker proof).

## Compiler-tools evidence (key <run> rows)
- comp-kuzu provenance: UNKNOWN-VINTAGE / populated headers (tarball/nessie/stitch) / age-WARN /
  BEHIND-by-N / post-F6 marker oracle (current/BEHIND/UNKNOWN) / PENDING line.
- comp-surface-check: list (5 surfaces) / selfcheck (SEV1 block / SEV2 warn / clean) / list-watched-files
  (8 files) / scan (Layer-1 graph-drift + Layer-2 file-SHA-watch, clean + synthetic SEV1).
- comp-manifest-check selfcheck: PASS after each manifest/comp-tools edit.
- ds-commit-gate: clean on every .py.
- comp-iam: trade-submission-lambda-role policy read (no recon refs).

Inbox Monitor b74y18fub armed throughout. Standing down event-driven at session end.
