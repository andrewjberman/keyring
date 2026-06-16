# NFRA_GCONTR.TO-2 — graph_contracts value-layer never-widen engine SHIPPED + table LIVE on Nessie main

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, COORDINATE

**Agent:** 0.7.0_AE_CloudOps · **Date:** 2026-06-16 · **Window:** session start (spawned 1319Z) -> 1543Z
**TO:** NFRA_GCONTR.TO-2 (COO GO 1321Z) -> **complete**

## Summary

Built + shipped all 4 limbs of the period-contracts value-layer never-widen machinery (TO-2,
the long pole), and created the foundation table in-VPC. The Q1/Q2 engine + the comp-surface-check
ADVISORY wiring are live on the dev box; `globgrph.graph_contracts` exists on Nessie main (empty,
RATIFIED §3 schema verified). CVO TO-3 (rows) + DS TO-4 (pipescript surface) are now unblocked.

## What shipped (4 limbs)

1. **Table — `globgrph.graph_contracts` on Nessie main** (`derive_runner.py`): `ensure_graph_contracts_table`
   (RATIFIED PRD §3 schema: NO `version` col, `+active BOOLEAN`) wired ENSURE-ONLY into `commit_to_iceberg`
   (the nightly never overwrites CVO's rows); `--ensure-contracts-only` surgical in-VPC bootstrap mode;
   marker stamp extended to carry `graph_contracts` for the dev-box read path.
2. **Q1 (structure)** — `contract_engine.py` (NEW) `q1_writes_diff` + `comp-aws contract-diff`: WRITES-edge
   snapshot diff into contracted buckets. Reads the full-fidelity derive SNAPSHOT (carries `via_role`; the
   stripped Iceberg `graph_edges` drops it). Reads `graph_contracts` via pyiceberg StaticTable (marker, else
   table-scoped mtime; in-VPC Nessie REST NOT required for READS). 3s/5s S3 timeouts; never raises/blocks.
3. **Q2 (policy)** — `q2_join`: contract JOIN -> CLEAN / WATCH / SANCTIONED / UNSANCTIONED. **WATCH tier**
   (CTO-endorsed + CVO-converged, divergence from the literal seed): UNSANCTIONED reserved for the curated
   `forbidden_writers` tripwire (low-FP, co-tenant-immune); shared-bucket non-canonical writers -> WATCH
   (advisory). Rationale: `opal-data-portal-v2` has ~12 legit non-canonical writer-roles (bucket-grain), so
   the seed's "any intruder -> UNSANCTIONED" would pin it permanently UNSANCTIONED + kill the hard-block ramp.
4. **comp-surface-check ADVISORY wiring** (`surface_check_cli.py`, CTO-RATIFIED gate): additive contract layer
   in `cmd_check` — a SEV1 contracted-surface touch runs Q2-at-HEAD; UNSANCTIONED WARNS but **NEVER changes the
   exit code** (file-gate non-regressed + rc-invariant). `+contract-selfcheck` = synthetic BMKAUD T1 replay
   (Phase-3 mandate). Uncontracted SEV1 reads LOUD unreviewed.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| (Phase-1) S3 warehouse table-list | `aws s3 ls .../warehouse/globgrph/` | PASS | net-new confirmed (only graph_nodes_*/graph_edges_* pre-create) — the TO-allowed alt to `comp-kuzu show_tables` (kuzu shows CloudNode/CloudEdge, not the Iceberg table-list) |
| (Phase-1) comp-iam (IAM check) | direct read of item2a.tf derive_runner_task role | PASS | `comp-iam service` is lambda-scoped; the create principal is the ECS derive task role. `GlobgrphWarehouseRW` (s3 RW on opal-313476888478-globgrph/*) covers the create — identical perm surface as graph_nodes/edges writes; NO iam.tf change -> Phase-2 `comp-iam gaps` N/A |
| comp-aws contract-diff (NEW) | `comp-aws contract-diff` | PASS | absent-path (pre-create, exit 0) -> EXISTS-0-rows (post-create); 1.9s after the scoped-prefix fix |
| comp-surface-check selfcheck | `comp-surface-check selfcheck` | PASS | file-gate NON-REGRESSED — ALL PASS (SEV1 rc=2, SEV2 rc=0, clean rc=0) |
| comp-surface-check contract-selfcheck (NEW) | `comp-surface-check contract-selfcheck` | PASS | Phase-3 BMKAUD T1 replay: +smartx -> UNSANCTIONED; ratified-in-window -> SANCTIONED; rc-invariance off=0/on=0 |
| ds-commit-gate | `.tools/ds-commit-gate.sh` (4 files) | PASS | py_compile + AST/future-annotations + ruff py39 all clean |

**What worked:** the dev-box StaticTable read path means Q1/Q2 work without the in-VPC Nessie REST; the WATCH
tier neutralizes the bucket-grain co-tenant FP by construction (CVO independently convergent). **What failed
(fixed):** first live `comp-surface-check check` HUNG — `_latest_table_metadata` paginated the full ~56k-object
warehouse to find the contracts table; fixed by scoping the S3 Prefix to the table dir + 3s/5s boto timeouts
(commit-time path must fail-fast, never stall a commit). **Gap found:** `comp-iam service` has no ECS-task-role
mode (only lambda) — IAM for an ECS-created table is verified by direct policy read; a `comp-iam ecs-task <role>`
mode would close it (logged, non-blocking).

## Deployment Sequence + Verification (AE)

```
code   730117858 (pushed CLOUD; safe-deploy: no deploy-scope scripts -> no auto-deploy)
ledger 5103dbfbc OPEN -> 7f9eb5acb CLOSED COMPLETE  (deploy-completion, all 4 legs in-session)
L1     zip (6 repo-root-rel files) -> s3://.../build-source/derive-runner-source.zip  [carries --ensure-contracts-only]
L2     CodeBuild globgrph-derive-build:5fdd33bf -> ECR opal-globgrph-derive-runner:latest = SUCCEEDED/COMPLETED
L3     ecs run-task globgrph-derive-runner --ensure-contracts-only -> task 797e5fc9 (+dup 42f413b8) STOPPED exit 0
       log: ENSURE_CONTRACTS_ONLY_START nessie=...local:19120 / GRAPH_CONTRACTS_ENSURED / GRAPH_CONTRACTS_READY(13 cols) / ENSURE_CONTRACTS_ONLY_COMPLETE
L4     SERVED-VERIFY (not rc=0): warehouse/globgrph/graph_contracts_bccbceec-941a-424e-be43-edd7d751a1cf/ exists;
       real Iceberg metadata.json; StaticTable read = RATIFIED §3 (13 fields, NO version, +active BOOLEAN,
       contract_id required, period_defs map / enforcement struct / list types), 0 rows; comp-aws contract-diff = EXISTS-0-rows
```
NOTE: an accidental 2nd `run-task` launched a duplicate bootstrap task; BOTH exited 0, idempotent `_ensure`
(create-409 -> load) converged on ONE table, 0 data impact. No full derive, no graph_nodes/edges overwrite.

## MCP traffic (significant only)

~14 messages. Sent: RAVC1 to CTO+COO (create-mechanism + lane + deploy-seq + Q2 WATCH fidelity); RAVC ACK +
addendum to CTO (PRD §3.2 fold); CVO 2-round convergence (4 field-usage confirms + co-tenant FP); RAVC2 COMPLETE
to COO+CTO; TO-3 unblock ping to CVO + TO-4 heads-up to DS. Received: CTO RULING 140717Z (gate RATIFIED + WATCH
endorsed + create-mech confirmed + BOOTSTRAP-NOW GO); COO lane-grant 67d4d3137 + GO 153252Z; CVO convergence
(closed, WATCH endorsed + §3.2-text-stale flag); 0.6.0_AE_PartnerETL caught + bounced CTO's mis-addressed ruling
(AE-serial conflation, CY-0017 class); DS TO-4 ack.

## Files Modified

See commit messages: `730117858` (the 4 code files + per-file detail), `5103dbfbc`/`7f9eb5acb` (ledger),
`368510a61` (TO status). Net: `org/modules/graph/contract_engine.py` (NEW, 343 lines), `comp_aws_cli.py`
(+contract-diff), `surface_check_cli.py` (+contract advisory layer + contract-selfcheck),
`infra/aws/globgrph/derive_runner.py` (+ensure_graph_contracts_table + --ensure-contracts-only + marker ext).

## Blockers

None. (TO-2 was gated, not blocked, on the CTO gate-review + COO lane-grant + deploy-seq GO — all cleared
in-session.)

## Current State

- `globgrph.graph_contracts` is LIVE on Nessie main (`s3://opal-313476888478-globgrph/warehouse/globgrph/graph_contracts_bccbceec-941a-424e-be43-edd7d751a1cf/`), EMPTY, RATIFIED §3 schema. Created via the in-VPC `--ensure-contracts-only` bootstrap; the nightly derive now also ensures it idempotently + the F6 marker carries it.
- The Q1/Q2 engine is `org/modules/graph/contract_engine.py` (dev-box read path; `load_contracts` / `q1_writes_diff` / `q2_join` / `contract_for_surface` / `run_contract_check`). Surfaces: `comp-aws contract-diff [--since <ref>]` (report) + the `comp-surface-check check` ADVISORY layer (warn-only, gated to SEV1 contracted surfaces, `GCONTR_SKIP_CONTRACT_CHECK=1` opt-out).
- The derive image in ECR `opal-globgrph-derive-runner:latest` is the new build (5fdd33bf) — tonight's nightly will run it (ensure-only contracts + marker ext are additive/safe).
- Advisory ramp only — nothing exits 2; the hard-block ramp-flip is a later CTO one-liner, gated on `forbidden_writers`-only proven low-FP OR Q2 gaining prefix/object-grain + ratified_at hash-in-window resolution.

## Next Steps

- [3.0.0_SA_CVO] TO-3: author SEV1 (benchmark/headline/advisor_intelligence-NNA) then SEV2 (peers/aum) contract rows to the WATCH-tier semantics + curate `forbidden_writers` COMPLETE (catch-power depends on it); SEV1 `ratified_by` needs [Andrew] (§9, via COO). Row WRITES need in-VPC compute — I offered a `derive_runner --load-contracts <yaml>` mode (YAML-in-repo -> in-VPC append, each row a Nessie commit); awaiting CVO's preferred authoring surface.
- [0.4.0_DS_ClientPlatform] TO-4: `pipescript --contract` / `--flipped` reusing `contract_engine.py` (don't re-derive the JOIN). Acked.
- [1.0.0_SA_CTO] fold WATCH tier + advisory-ramp + create-mechanism-not-terraform into PRD §3.2/§7 (CVO consistency note).
- [0.7.0_AE_CloudOps] next: NFRA_OPLMCP .01/.03 follow-on (CTO designated; via COO TOs) now that GCONTR TO-2 is closed.
