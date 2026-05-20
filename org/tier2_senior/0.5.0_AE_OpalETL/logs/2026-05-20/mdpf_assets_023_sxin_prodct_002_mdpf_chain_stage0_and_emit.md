# MDPF_ASSETS.023 + SXIN_PRODCT.002 — mdpf-daily-dispatch.sh Stage 0 + Stage 3.5

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TOs:** `MDPF_ASSETS.023.ae-orion-composition-bronze-chain-stage0` + `SXIN_PRODCT.002.ae-legacy-emit-in-chain-step`
**Combined edit pass** per CTO~B/COO~B (both edit the same file `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`).
**Tag:** `mdpf-pipeline-v1.0.2` | **Commits:** `afa53a952` (edit) + `27402328e` (record-deploy)

---

## Current State

- **BOTH TOs COMPLETE.** Code + infra shipped AND Phase 3 verified on a clean chain
  re-trigger (run `mdpf_daily_20260520_193329`, status=complete). DS~B uploaded the
  bronze script; the IAM grant works; Stage 0 + Stage 3.5 both ran clean. See the
  Phase 3 Verification section below.

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
| Phase 3 — chain re-trigger | **PASS** | See Phase 3 Verification below. |

## Phase 3 Verification (chain re-trigger `mdpf_daily_20260520_193329`)

DS~B uploaded `pull_orion_model_composition.py` to `s3://opal-data-mdpf/code/scripts/bronze/`
(md5 MATCH). I re-triggered the mdpf daily chain (invoked `mdpf-daily-trigger` Lambda,
runner `i-02448edb624a7a7cf`, SSM `29a5ce5f-...`). Run completed `status=complete`.

`steps_done`: `STAGE0-BRONZE ok 12s` -> `WS-E ok` -> `WS-A ok` -> `LEGACY-EMIT ok 18s`
-> `ROLLUP ok` (the 4 Stage-1 feeders run backgrounded so their `record_step` lands in a
subshell and is not in the parent telemetry — a PRE-EXISTING chain quirk, not introduced
here; the feeders did run, WS-E/WS-A depend on their output).

- **MDPF_ASSETS.023 — Stage 0 PASS (AC2/AC4).** Stage 0 S3-pulled the bronze script,
  read the Orion JWT from Secrets Manager `orion/jwt/current` (the `OrionJwtReadStage0Bronze`
  IAM grant works), pulled all 9 Opal models, wrote 9 `model_*.json` + `_meta/pull_complete.json`
  to `s3://opal-data-mdpf/mdpf/bronze/orion_model_composition/2026-05-20/` — `overall=success`,
  `errors: []`. AC3 (best-effort/non-fatal) — control flow has no `exit` on a Stage-0 failure;
  the earlier WARN-skip runs (script-absent) already exercised the non-fatal path with the
  chain completing. AC1 probe + AC5 terraform-0-diff/tag + AC6 documented above.
- **SXIN_PRODCT.002 — Stage 3.5 PASS (AC1/AC2/AC4).** `LEGACY-EMIT` ran after `WS-A`
  (Stage 3) and before `ROLLUP` (Stage 4) — exactly the designed placement, independent of
  Stage 4. `non_model_assets.json` refreshed: `generated_at 2026-05-20T19:35:27Z`,
  `latest.date 2026-05-20`, enterprise_total $1,898,213,922.32, non_model_aum $457,606,190.54.
  AC3 (Stage-3-fail skips the emit) is structural — the chain fail-fasts at the WS-A
  `RC_WSA` check before the emit step is reached; verified by placement + code-read.

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 — both TOs COMPLETE, Phase 3 verified on run
  `mdpf_daily_20260520_193329`. mdpf-pipeline-v1.0.2.
- `[follow-up, non-blocking]` Pre-existing chain quirk: the 4 Stage-1 feeders' `record_step`
  is lost to the `&`-subshell so they are absent from the telemetry `steps_done` (and the
  final `LAST_OUTPUT` still reads "All 4 stages complete" — cosmetically stale vs the now
  6-stage chain). Neither is introduced by this work; flagged for an opportunistic cleanup.
