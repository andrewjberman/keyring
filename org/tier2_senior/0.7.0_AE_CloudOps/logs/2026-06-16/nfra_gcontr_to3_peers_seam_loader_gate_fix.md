# NFRA_GCONTR TO-3 peers-load seam -> loader PENDING-gate bug found + fixed

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.7.0_AE_CloudOps - **Date:** 2026-06-16 - **Window:** ~1818Z -> 1824Z (event: CVO TO-3 seam-flag)
**TOs:** NFRA_GCONTR per-batch --load-contracts (CVO ratification cadence). No load run (peers PENDING-CTO-COO-SIGNOFF, held til CTO+COO sign).

## Summary

CVO flagged a TO-2<->TO-3 seam: the local authoring YAML now has 2 rows (benchmark + new peers
SEV2), and the benchmark row still shows the stale `ratified_at=PENDING-ANDREW-SIGNOFF` placeholder
even though benchmark is LIVE+ratified on Nessie (6f21c75ca..., my TO-2b close). Risk: a whole-file
`--load-contracts` could regress the live benchmark ratified_at. I ground-truthed the loader against
the code (not memory), answered the idempotency question, AND found a deeper latent defect the seam
surfaced: the PENDING-gate did not recognize the peers placeholder. Fixed prefix-aware, proven, pushed.

## What I found (ground-truth, not assertion)

- **Benchmark is DOUBLE-protected** -- a scoped peers load CANNOT regress it: the already-present
  guard (derive_runner.py:1030 `if cid in existing and cid not in overwrite_ids: skip`) fires BEFORE
  any ratified_at/PENDING logic. benchmark is in the live table -> skipped regardless of its stale
  YAML placeholder. Only an explicit `--overwrite benchmark-model-portfolios` could touch it (I never
  pass that on a peers load). Answers CVO's idempotency seam-flag structurally.
- **BUG (the real find):** PENDING-detection was an EXACT-match tuple `_PENDING_RATIFIED` knowing only
  `PENDING-ANDREW-SIGNOFF`. The peers row uses `PENDING-CTO-COO-SIGNOFF` -- NOT in the tuple -> two
  latent defects on a peers load:
  1. SAFETY GATE BLIND (L1033): the unratified peers SEV2 row would NOT be skipped -- it could land
     BEFORE CTO+COO sign-off. The exact failure the gate exists to prevent.
  2. ratified_at NOT STAMPED (L1071): even a deliberate `--stamp-ratified` load would write the literal
     string `PENDING-CTO-COO-SIGNOFF` as the pin instead of the real Nessie hash -> bogus
     existence-in-window pin (value-limb defect on a never-widen contract).

## What shipped

- **`_is_pending_ratified()`** (fe645e103): prefix-aware gate -- any `PENDING.../TBD/empty/None` reads
  as pending; real hashes do not. Future-proof vs `PENDING-CVO-SIGNOFF` etc. Both detection (L1029) and
  stamping (L1071) route through it. 17 ins / 2 del, infra/aws/globgrph/derive_runner.py.
- **Proof:** 10/10 local cases incl `PENDING-CTO-COO-SIGNOFF`->True (gate fires) + real Nessie hashes
  ->False (no false-positive re-stamp of a live ratified row). Tested against the REAL function source
  (full module import needs comp_aws_cli on PYTHONPATH; fallback exec'd the verbatim fn body).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| ds-commit-gate.sh | `.tools/ds-commit-gate.sh infra/aws/globgrph/derive_runner.py` | PASS | py_compile + AST + ruff py39 clean |
| safe-commit.sh | commit fe645e103 (AE author, pathspec-scoped) | PASS | surface-check: 0 critical surfaces touched |
| safe-deploy (push hook) | `git push origin CLOUD` | PASS (no-op) | "no deploy-scope script files" -- derive_runner.py is infra, NOT gold/silver/bronze -> push shares commit only, image unchanged |

**What worked:** reading the loader code instead of answering CVO's idempotency question from memory
surfaced a bug the seam-flag only gestured at. **What failed:** nothing this window. **Gap found:** the
exact-match placeholder allow-list -- a recurring anti-pattern (a new sign-off variant silently defeats
the gate); prefix-match is the durable form.

## Deployment Sequence + Verification (AE)

```
code fe645e103 (prefix-aware PENDING gate) -> ds-commit-gate PASS -> safe-commit -> push CLOUD (8f3953bc7..fe645e103)
  safe-deploy: no deploy-scope scripts -> image NOT rebuilt on push (correct; infra path).
GO-GATED (CTO+COO sign the peers SEV2 row), NOT done now:
  CodeBuild rebuild :latest (carries fe645e103) + ledger open
  in-VPC --load-contracts <s3 yaml> --dry-run            (PROVE: benchmark SKIP already-present; peers per gate)
  in-VPC --load-contracts <s3 yaml> --stamp-ratified peers-model-portfolios   (NO --overwrite; peers stamped real hash)
  WRITE_VERIFY peers period_defs + StaticTable 2 rows + benchmark ratified_at UNCHANGED -> ping CVO byte-verify
```

## MCP traffic

3 sent: CVO (seam CLOSED + bug/fix/proof + GO-time sequence), COO + CTO (CC -- value-limb fix, GO-gated).
1 received: CVO TO-3 peers-row staged heads-up (load held til CTO+COO sign).

## Blockers

None. The peers LOAD is GO-gated on CTO+COO sign-off (not a blocker -- expected governance hold). The
code fix is complete + pushed; the image rebuild is deferred to the load (no stranded leg -- nothing to
strand until the load deploy opens).

## Current State

- `infra/aws/globgrph/derive_runner.py` @ fe645e103 (CLOUD): `--load-contracts` PENDING-gate is now
  prefix-aware (`_is_pending_ratified`). Live ECR `opal-globgrph-derive-runner:latest` is still
  e6d47d7b (EC2-WRITES fix) -- does NOT yet carry fe645e103; the nightly derive doesn't use the
  --load-contracts path so this is fine. The loader fix images in at the GO-time peers-load rebuild.
- `globgrph.graph_contracts`: 1 live row (benchmark-model-portfolios, Andrew-ratified,
  ratified_at=6f21c75ca...). Peers row staged in CVO YAML (org/tier1_exec/3.0.0_SA_CVO/contracts/
  graph_contracts.yaml @ 3cb8faeb1, contract_id=peers-model-portfolios, canonical_writer=
  yang-pipeline-lambda-role, ratified_by=[CTO,COO], PENDING-CTO-COO-SIGNOFF) -- NOT yet on S3, NOT loaded.

## Next Steps

- [0.7.0_AE_CloudOps] On CTO+COO peers sign-off + CVO's "YAML on S3, load ON" ping: run the GO-time
  sequence above (rebuild + dry-run + scoped --stamp-ratified peers load + WRITE_VERIFY + ledger).
- [0.7.0_AE_CloudOps] 06-17 morning (event-driven, separate): verify the scheduled nightly derive emits
  EC2-WRITES edges (comp-kuzu EC2 WRITES > 0; bd-exporter-ec2-role -> opal-data-bd); ping CVO to lift
  the held NNA policy limb. NO ad-hoc derive.
- [3.0.0_SA_CVO] Upload the CTO+COO-signed 2-row YAML to s3://opal-313476888478-globgrph/contracts/
  graph_contracts.yaml; ping AE to load (peers only). aum/account-distribution = smartx-ingestion-
  lambda-role, its own later batch.
- [1.0.0_SA_CTO] Optional PRD §3.2 note: sign-off placeholders must be `PENDING-*`/`TBD` tokens (never a
  partial hash) -- the gate is prefix-on-PENDING by design now.
