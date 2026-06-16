# NFRA_GCONTR TO-2b — benchmark row LIVE (BMKAUD-catch, both axes) + EC2-WRITES gap root-caused

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, IMPLEMENT, COORDINATE

**Agent:** 0.7.0_AE_CloudOps · **Date:** 2026-06-16 · **Window:** ~1543Z -> 1619Z (delta since the TO-2 log)
**TOs:** NFRA_GCONTR.TO-2b (COO-GO'd addendum) -> **complete** · EC2-WRITES derive fix -> RAVC1 filed (awaiting GO)

## Summary

Built the in-VPC contract row-writer (TO-2b), loaded the Andrew-ratified benchmark contract row, and
DEMONSTRATED NFRA_GCONTR's core thesis end-to-end: a benchmark source/period flip with no ratified
contract edit -> Q2 UNSANCTIONED (the BMKAUD-catch), verified on BOTH axes against the live in-VPC
table. Caught + fixed a period_defs-wipe bug in my own loader (StaticTable verify, not rc=0). Then
root-caused CVO's P1 (EC2-produced surfaces invisible to Q2) to a 1-line IAM gap and RAVC1'd the fix.

## What shipped

- **`derive_runner --load-contracts <yaml|s3://>`** (in-VPC row-writer): append-only + ensure-style;
  **safety gate** (a PENDING-ratified row is SKIPPED unless `--stamp-ratified <id>` -- refuses to land
  an unratified never-widen SEV1 contract); `--dry-run` readiness probe; `--overwrite` correction mode;
  `ratified_at` stamped = Nessie HEAD pinned at write time (single write, no read-back); a post-write
  `WRITE_VERIFY` re-reads + reports period_defs size. CVO authors YAML in repo -> S3 -> I run the in-VPC append.
- **Benchmark contract row LIVE** on Nessie main (Andrew-ratified, `ratified_at=6f21c75ca...` real hash,
  `ratified_by=[Andrew]`, 1 row). BMKAUD T1 replay: synthetic +smartx -> Q2 **UNSANCTIONED**; baseline=WATCH
  (no false-positive). period_defs = 11 keys byte-verified by CVO (incl `1M=trailing`). Both axes accepted.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-aws contract-diff | `comp-aws contract-diff` | PASS | now reads the live benchmark row (WATCH on the shared bucket; 12 co-tenant writers, forbidden absent) |
| comp-iam gaps | `comp-iam gaps` | GAP-not-flagged | Lambda-scoped -> did NOT cross-ref the ECS derive_runner_task role; missed the GetInstanceProfile gap. Direct policy read was conclusive. A comp-iam ecs-task mode would catch it |
| ds-commit-gate | `.tools/ds-commit-gate.sh derive_runner.py` (x2) | PASS | loader + the period_defs fix |
| StaticTable verify (manual) | pyiceberg StaticTable read of graph_contracts | PASS | caught period_defs=[] post-load (the bug); re-verified period_defs=11 post-correction. The SERVED-artifact evidence path (CVO can't read the in-VPC table) |

**What worked:** `--dry-run` proved the in-VPC path + the safety gate (PENDING row skipped) without writing;
the WRITE_VERIFY integrity check now makes a silent value-limb disarm structurally un-passable. **What
failed (fixed):** the ratified_at restamp read the row back from Iceberg (map -> list-of-tuples) + a naive
rebuild dropped period_defs -> wrote `{}`; root-fixed to a single pre-write stamp (no read-back) + defensive
`_map`. **Gap found:** comp-iam doesn't cover ECS task-role IAM (missed the derive perm gap that caused the
entire EC2-WRITES blind spot).

## Deployment Sequence + Verification (AE)

```
Loader:    11efd80ef + fix 48580c99f. Images: CodeBuild 2d457728 (loader) + 90cceb00 (fix), both SUCCEEDED.
Loads (in-VPC ecs run-task, log /ecs/globgrph/derive-runner):
  dry-run  b248af89 exit0 -> SAFETY GATE: PENDING row skipped, 0 writes
  real     26c9ce57 exit0 -> CONTRACTS_APPENDED, ratified_at=516a4da5 (then L5 verify caught period_defs=[])
  fix      1b49e9ab exit0 -> CONTRACTS_OVERWRITTEN, WRITE_VERIFY period_defs=11, ratified_at=6f21c75c, 1 row no dup
Ledger 5103dbfbc/... -> c98b87b58 CLOSED. SERVED/StaticTable-verified (not rc=0).
```

## EC2-WRITES P1 (CVO) -- diagnosed + RAVC1'd

- CVO P1: EC2-produced surfaces (NNA, platinum/firm) have no resolvable canonical_writer -> Q2 policy limb can't fire.
- My FIRST hypothesis (stopped EC2 excluded from live_ec2) was WRONG -- CVO operationally corroborated it, but `live_ec2()` (comp_aws_cli.py:330) does NOT exclude stopped. CORRECTED the record to COO+CVO before designing (verify-don't-assume; both owned the bad corroboration).
- **Root cause (confirmed):** `derive_runner_task` IAM lacks `iam:GetInstanceProfile` -> `derive_data_access_edges` (comp_aws_cli.py:1636) `get_instance_profile()` AccessDenies -> `except: prof_role[prof]=[]` (L1638) -> 0 EC2 consumers -> 0 EC2-sourced WRITES edges across the WHOLE estate.
- **RAVC1 filed (COO GO + CTO CC, 161852Z):** fix = +`iam:GetInstanceProfile` to item2a.tf derive_runner (1 line, additive read, no code) via safe-apply (HALTGT); optional companion = WARN the silent except-swallow. Verify on next nightly derive (EC2 WRITES > 0). TRIVIAL (was framed moderate).

## MCP traffic (significant)

~22 this window. RAVC2 TO-2b ACCEPTED (COO) -- both axes; CVO VALUE LIMB ACCEPTED (byte-verify 11/11). CVO P1 (EC2-WRITES) -> my correction -> COO+CVO accepted -> RAVC1 filed. DS TO-4 acked (reuse contract_engine).

## Blockers

None. EC2-WRITES fix is RAVC1-gated (awaiting COO/CTO GO), not blocked.

## Current State

- `globgrph.graph_contracts`: 1 live row (benchmark-model-portfolios, Andrew-ratified, both axes verified). Loader (`--load-contracts`) deployed in the derive image; CVO authoring the next-wave rows (model_portfolios.* Lambda surfaces + NNA value-limb) in `org/tier1_exec/3.0.0_SA_CVO/contracts/graph_contracts.yaml` -> S3 `s3://opal-313476888478-globgrph/contracts/graph_contracts.yaml` -> I load per-batch.
- EC2-WRITES fix staged in RAVC1: +`iam:GetInstanceProfile` to `infra/aws/terraform/globgrph/item2a.tf` derive_runner_task AccountWideReadOnly. On GO: safe-apply + ledger + verify next nightly.

## Next Steps

- [0.7.0_AE_CloudOps] On COO/CTO GO: apply the EC2-WRITES iam.tf 1-liner (safe-apply + ledger); verify next nightly derive emits EC2 WRITES edges; ping CVO to re-verify NNA + EC2 surfaces are Q2-resolvable.
- [0.7.0_AE_CloudOps] Per-batch `--load-contracts` as CVO ratifies the next-wave rows (SEV1 needs Andrew via COO; SEV2 CTO+COO).
- [3.0.0_SA_CVO] Author model_portfolios.headline/peers/aum (Lambda, Q2-resolvable now) + NNA value-limb; NNA policy-limb HELD til the EC2-WRITES fix.
- [1.0.0_SA_CTO] PRD §3.2/§7 fold (WATCH tier + advisory-ramp + create-mechanism); optional except-swallow WARN + comp-iam ecs-task mode.
