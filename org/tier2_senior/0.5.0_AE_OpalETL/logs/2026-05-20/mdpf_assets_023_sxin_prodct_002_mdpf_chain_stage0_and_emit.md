# MDPF_ASSETS.023 + SXIN_PRODCT.002 — mdpf-daily-dispatch.sh Stage 0 + Stage 3.5

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TOs:** `MDPF_ASSETS.023.ae-orion-composition-bronze-chain-stage0` + `SXIN_PRODCT.002.ae-legacy-emit-in-chain-step`
**Combined edit pass** per CTO~B/COO~B (both edit the same file `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`).
**Tag:** `mdpf-pipeline-v1.0.2` | **Commits:** `afa53a952` (edit) + `27402328e` (record-deploy)

---

## Current State

- **Code + infra SHIPPED; Phase 3 chain-re-trigger verification PENDING.** Both TOs'
  chain-script edits are committed, the dispatch script is S3-deployed, and the
  MDPF_ASSETS.023 IAM grant is `terraform apply`'d + 0-diff verified + tagged.
- **MDPF_ASSETS.023 is blocked for full completion** on a DS-lane dependency:
  `pull_orion_model_composition.py` is NOT yet on `s3://opal-data-mdpf/code/scripts/bronze/`
  (Rule 13 — DS owns bronze-script S3 deploy). MCP'd to DS 0.4. Until it lands, Stage 0
  WARN-skips (non-fatal by design); the chain is unaffected.
- **SXIN_PRODCT.002** code is fully shipped; only the Phase 3 chain re-trigger remains —
  best bundled with .023's (one re-trigger verifies both, after the DS bronze upload).

## Phase 0 probe (MDPF_ASSETS.023)

- `s3://opal-data-mdpf/code/scripts/bronze/` is **empty** — `pull_orion_model_composition.py`
  is not S3-deployed. The 5/18 partition was the one-time manual pull. -> DS-lane upload
  needed (MCP'd DS 0.4).
- `pull_orion_model_composition.py` (read locally): authenticates with the Orion JWT —
  SM `orion/jwt/current` primary, `s3://opal-data-inf/orion/jwt/current.json` fallback;
  no ROPC, no new auth surface. Hits `api.cloud.orionadvisor.com` (HTTPS egress — the
  runner SG already allows all outbound).
- Runner role `mdpf-daily-runner-ec2-role` / policy `mdpf-runner-scoped` had **no Orion
  JWT access** (only `smartx/credentials/*` SM + the eclipse/BD/platinum S3 scopes).
  -> Phase 1 (Terraform grant) IS in scope; done — see below.

## What shipped

**`mdpf-daily-dispatch.sh`** (one coherent edit pass):
- **Stage 0** (MDPF_ASSETS.023) — prepended before Stage 1: runs
  `pull_orion_model_composition.py --date <RUN_DATE> --upload`. **Best-effort / NON-FATAL** —
  a failed pull *or a not-yet-S3-deployed script* logs a `WARN` and the chain continues
  (the WS-C feeder roll-forward, DS Base `7d41d28cd`, is the Layer-1 safety net). The
  `-f` guard means shipping this ahead of the DS bronze upload is safe.
- **Stage 3.5** (SXIN_PRODCT.002) — appended after Stage 3, before Stage 4: runs
  `build_legacy_compat_emit.py --upload`. Reached **only** when Stage 3 succeeded (the
  chain fail-fasts on a WS-A failure) -> the Stage-3 platinum write is the gate; a
  Stage-3 failure correctly skips the emit. Placed before Stage 4 -> independent of the
  rollup outcome (AC2). Emit failure logs `ERROR` (not swallowed) but does not abort.
- `telemetry total_steps` 6 -> 9 to keep `pct_complete` accurate with the two added
  `record_step` calls.

**`mdpf-pipeline/iam.tf`** (MDPF_ASSETS.023 Phase 1) — new `OrionJwtReadStage0Bronze`
statement on `mdpf-runner-scoped`: `secretsmanager:GetSecretValue` on `orion/jwt/*` +
`s3:GetObject` on `opal-data-inf/orion/jwt/*` (both JWT paths the script uses). Tight
prefix scope, consistent with the existing eclipse/BD-scoped statements.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Combined edit of `mdpf-daily-dispatch.sh` (Stage 0 + Stage 3.5 + telemetry) | bash -n clean |
| 2 | `iam.tf` — Orion JWT grant | terraform fmt OK |
| 3 | `safe-commit.sh` | `afa53a952` (2 files, 67 ins / 2 del) |
| 4 | `git push origin CLOUD` | `63ffef0ed..afa53a952` |
| 5 | `terraform apply` mdpf-pipeline | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff replan | "No changes." |
| 7 | `comp-iam gaps` | No gap on `mdpf-daily-runner-ec2-role` — the Orion grant is clean. (2 pre-existing gaps on `mdpf-daily-trigger` — SSM-body `aws s3 cp` false positives, not my scope.) |
| 8 | `record-terraform-deploy.sh` + `git tag mdpf-pipeline-v1.0.2` + push --follow-tags | `27402328e` + tag `mdpf-pipeline-v1.0.2` |
| 9 | `aws s3 cp mdpf-daily-dispatch.sh s3://opal-data-mdpf/code/` (Rule 12) | uploaded, 10910 bytes |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 0 — `aws s3 ls .../bronze/` + read `pull_orion_model_composition.py` + read `mdpf-pipeline/iam.tf` | OK | bronze script absent on S3 (DS dep); runner role lacked Orion JWT access (Phase 1 in scope). comp-* N/A — the mdpf chain scripts are not graph-modeled (documented PRD-section-5 gap). |
| Phase 2 — `bash -n mdpf-daily-dispatch.sh`; `terraform fmt -check iam.tf` | OK | shellcheck not installed (env gap, CTO~B-accepted substitute for the sequence); bash -n clean; Stage 0 control flow verified non-fatal. |
| Phase 2 — `comp-iam gaps` (iam.tf changed) | clean for my scope | No gap introduced on the runner role. |
| Phase 3 — chain re-trigger | **PENDING** | See Next Steps — bundled with the DS bronze upload. |

## Next Steps

- `[0.4.0_DS_ClientPlatform~B / DS 0.4]` Upload `pull_orion_model_composition.py` to
  `s3://opal-data-mdpf/code/scripts/bronze/` (DS-lane, Rule 13). MCP sent.
- `[0.5.0_AE_OpalETL~B]` Phase 3 — after the DS bronze upload, re-trigger the mdpf daily
  chain once: verifies (a) Stage 0 produces + uploads the run-date orion bronze and the
  WS-C feeder consumes it fresh (MDPF_ASSETS.023 AC4), and (b) Stage 3.5 runs post-Stage-3
  and refreshes `non_model_assets.json` (SXIN_PRODCT.002 AC4) — plus the simulated-failure
  paths (AC3 both). One re-trigger covers both TOs.
- `[2.0.0_SA_COO~B]` RAVC2 — code/infra shipped; Phase 3 verification pending the DS
  upload. Both TOs stay in-flight until the chain re-trigger confirms AC3/AC4.
