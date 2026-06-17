# Cold-start AE_CloudOps base — P1 GCONTR EC2-WRITES verify GREEN + D8-FP surface-scan FP diagnosed (AC1) + CVO Q2-attribution + §3 convergence

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Agent:** 0.7.0_AE_CloudOps · **Date:** 2026-06-17 · **Window:** ~1356Z (cold-start) -> ~1438Z

## Summary
Cold-start base lane. Ran the MSTR-queued morning artifact-review: **P1 GCONTR NNA EC2-WRITES verify = GREEN** on live/served state (RAVC-closed by CTO+COO). Ground-truthed that **P2 (GCONTR TO-2) and P3 (DEBTSCAN TO-D2) are both already COMPLETE** — the MSTR locked-batch framing was pre-completion stale; COO confirmed, no redo. Diagnosed the 06-17 derive's in-run **critical-surface SEV1/SEV2 SNS as a false-positive** (baseline provenance mismatch), CTO-confirmed AC1, landed the binding interim KNOWN-FP ledger entry, and got the **D8-FP fix TO** (GO'd). Surfaced a code-grounded **AC3 feasibility refinement** (AWS-scoped re-sign would BLIND the alarm) — AC2 now design-gated on CTO. Answered CVO's **Q2 writer-attribution** question (canonical_writer = role short-name) and converged the **§3 loader-hardening invariant** with CTO (signed off + one hash-shape strengthening).

## P1 — GCONTR EC2-WRITES verify (GREEN, RAVC-closed)
- iam:GetInstanceProfile APPLIED live on `opal-globgrph-derive-runner-task` (re-verified vs DEPLOYED policy, not the stale "awaiting-GO" framing).
- 06-17 02:00Z scheduled nightly derive (`opal-globgrph-derive-runner-nightly`, cron 0 2 * * ?) ran complete: nodes=1256 edges=2984, NESSIE_COMMIT main, MARKER_STAMPED, DERIVE_RUNNER_COMPLETE, no AccessDenied.
- Mechanism (grounded, not analogized): get_instance_profile now succeeds -> INSTANCE_PROFILE=11 + HAS_PROFILE=24 (were 0) -> **69 EC2-sourced WRITES edges (were 0 estate-wide)**. NNA path resolves: bd-gold-layer-runner (EC2) -HAS_PROFILE-> bd-exporter-profile -ASSUMES-> bd-exporter-ec2-role -WRITES-> opal-data-bd. comp-kuzu provenance=current.
- CVO independently re-verified GREEN -> lifted the held NNA policy limb.

## D8-FP — surface-scan SEV1/SEV2 FP (NFRA_GRAPHS.D8-FP, GO faded9893)
- AC1 (GATING): CONFIRMED FALSE-POSITIVE. Baseline `s3://opal-313476888478-globgrph/critical-surface-baseline.json` (== `.comp-graph/baseline.json`, built_at≈06-12T18:32Z, 2139 nodes/2691 edges) is a comp-graph MERGED build keyed `node_type:name` (gold:1294/lambda:303/s3:287/endpoint:166/eventbridge:62/component:27). In-derive scan diffs the AWS-only derive (ARN-keyed) -> key-spaces never intersect (+1239/-2139/~0); only portal endpoint:/component: removed-nodes matched watched surfaces -> the fire. AWS estate healthy (no real drop). CTO confirmed (142330Z).
- Interim KNOWN-FP ledger committed **79d999355**, pushed (d1dd0b02e). Binding no-re-trip note.
- AC2/AC3 design refinement raised to CTO (143654Z): AWS-scoped re-sign DE-NOISES but BLINDS — every AWS node has file_path="full-derive" (comp-kuzu n.source = {full-derive:1256}); watched surfaces are portal-source/chain-keyed; so no AWS node can match a surface -> 0 findings possible -> fails AC3. Options: A (AWS-backend per-surface attribution, recommended — keeps alarm live) vs B (retire in-derive Layer-1, lean on commit-time comp-surface-check). HELD for CTO scope call.

## CVO Q2-attribution + §3 convergence
- CVO Q2 seam: Q2 (`writes_into`) keys on the WRITES edge's **via_role** read from the RAW derive graph (kuzu drops via_role). Derive sets via_role = ROLE short-name (`rarn.split('/')[-1]`); source = instance. => canonical_writer for NNA = **bd-exporter-ec2-role** (matches the peers-row convention). Answered CVO 142125Z -> NNA row authorable without seam re-open.
- §3 loader-hardening invariant: CTO SIGNED OFF (converges PRD v0.2.2 §3, 518017f96). Strengthening to fold: WRITE_VERIFY does POSITIVE Nessie-hash-SHAPE validation (allowlist), not just PENDING-* denylist; NOT a snapshot.parent CAS guard (null by design). Lands folded into the TO-3 GO-time --load-contracts rebuild (zero extra image builds, COO-approved).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-kuzu | EC2 WRITES edges / node-type census / provenance header / n.source distribution / instance->profile->role chain (~8 queries) | PASS | provenance=current (pin==marker HEAD), 06-17 vintage; 69 EC2 WRITES, source={full-derive:1256} (the AC3 blind-risk evidence). Quirk: `profile` is a Kuzu keyword -> alias collisions (use `prof`). |
| aws iam get-role-policy | derive_runner_task DeriveRunnerAccountDescribe | PASS | iam:GetInstanceProfile present live (fix applied). |
| aws logs / events | derive-runner nightly stream + schedule | PASS | 06-17 02:00Z run complete; leading-/ args need PowerShell (MSYS pathconv mangles Bash). |
| safe-commit.sh | ledger 79d999355 | PASS | surface-check: 0 critical surfaces touched. |
**What worked:** grounding fix-status against the DEPLOYED policy + the live graph (not the stale "awaiting-GO" log framing) — caught that the fix had already landed. Reading the Q2 + derive edge-builder code answered CVO definitively. **What failed:** nothing. **Gap found:** the in-derive surface-scan's file_path->watched matching is portal-source-oriented and cannot fire on the AWS-only derive (file_path="full-derive") — the deeper design issue behind the FP (raised to CTO).

## Deployment Sequence + Verification (AE)
```
No infra deploy this window. P1 = read-only verify (live IAM + ECS log + comp-kuzu). D8-FP AC2 deploy HELD on CTO scope call.
Committed + pushed: 79d999355 (interim KNOWN-FP ledger) -> origin CLOUD d1dd0b02e (safe-deploy: no deploy-scope files; .md only).
```

## Blockers
None. AC2 is design-gated on a CTO scope decision (Option A vs B — a feasibility refinement with options+rec, not a blocker). TO-3 contract-row load gated on CVO TO-3 (planned dependency). Both event-driven.

## Current State
- GCONTR: TO-2 complete (graph_contracts live; benchmark+peers+aum rows). My remaining lane = the per-batch --load-contracts row LOAD, stand-ready for CVO's "YAML on S3, load ON". At GO-time: dry-run-discriminate the image (S3-ZIP stale trap, resolvedSourceVersion=null), then ONE rebuild carrying fe645e103 + the §3 loader hardening (fail-closed stamp + WRITE_VERIFY positive-hash-shape gate) + scoped --stamp-ratified + WRITE_VERIFY + ledger.
- D8-FP: AC1 done; interim ledger landed (79d999355). AC2 awaiting CTO Option A/B scope call. If A: carve AWS-backend subgraph per surface from the 06-17 derive (no ad-hoc derive) + re-sign + egress-test synthetic backend-node removal + AC4 served-state confirm of MP/ADVI.
- Queued (no cadence pressure): review CTO deploy-tooling pass (safe-destroy.sh + deploy_ledger --red, 131532Z).

## Next Steps
- [1.0.0_SA_CTO] D8-FP AC2 scope call: RULED **Option A** (AWS-backend-membership attribution) at 143835Z. Proceeding: carve per-surface AWS-backend subgraph from 06-17 derive (no ad-hoc) -> re-sign ARN-keyed baseline -> AC3 egress-test (synthetic backend-node removal must fire the right surface). COO resizing the formal TO to Option-A size.
- [3.0.0_SA_CVO] author NNA SEV1 row (canonical_writer=bd-exporter-ec2-role; Andrew via COO per §9) + value limb; ping me for GO-time --load-contracts when YAML on S3.
- [0.7.0_AE_CloudOps] on TO-3 GO: the folded load+hardening rebuild sequence. On CTO AC2 call: implement D8-FP. When gated: the CTO deploy-tooling review.
