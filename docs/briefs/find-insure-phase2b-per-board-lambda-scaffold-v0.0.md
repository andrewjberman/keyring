# FIND_INSURE Phase 2B Per-Board Lambda Scaffold (v0.0 — pre-HAR-drop)

**Author:** 0.7.0_AE_CloudOps~B
**Date:** 2026-05-27 (STANDBY-PREP scaffold; per-board fill at Andrew HAR drop)
**Trigger:** ws COO `[SYNC-CARVE-RATIFIED]` 2026-05-27T18:15Z + `[CONCUR Option (a) SEQUENCE-AB]` 18:51Z parallel-fill ratification while ~A v0.3.0 tag lands
**Anchor:** DS~D endpoint-manifest-v0.0 (`docs/briefs/find-insure-job-board-endpoint-manifest-v0.0.md`) — DS-side per-board contract
**PRD:** `docs/architecture/FIND_INSURE.md` v0.4 (`a9b72b942`) §4 Phase 2 Part B
**Status:** **v0.0 SCAFFOLD — every per-board section is a Lambda-module STUB.** Per-board rows fill in at HAR-audit time once DS~D's manifest v0.1 lands with each board's `B-alpha-feasibility-verdict` + endpoint shape + auth class. Lambda code authoring fires per-board immediately after each board's manifest row finalizes.

---

## 1. Purpose + scope

This scaffold is the **AE 0.7~B-side per-board Lambda module structure** for FIND_INSURE Phase 2B (job-postings channel bronze tier). The per-board manifest authored by DS~D establishes WHAT each board's endpoint shape + auth + cost class is; this scaffold establishes HOW the per-board bronze crawler Lambda is wired (TF module + EventBridge fan-out + IAM + secret reference) before Andrew HARs land.

Locking the Lambda-module convention NOW lets the per-board ship cycle collapse to a pure mechanical fill-in (~30-60min wall per board × 6 = 3-6h total) instead of a design-then-fill cycle.

**OUT OF SCOPE (deferred to per-board ship cycles):**

- Lambda source code (Python `data/find/imo/scripts/bronze/crawl_job_posting_{board}_bronze.py`) — authored at per-board fill time
- Per-board Bα URL templates + auth headers — populate from manifest at fill time
- Per-board Bβ Bright Data collector-id values — populate from Bright Data console at fill time
- Per-board `find-insure/job-board/{board-slug}/api-key` secret values — Andrew/AE rotates at provision

---

## 2. File-split convention (binding per ws COO `[SYNC-CARVE-RATIFIED]` 18:15Z)

Phase 2B authored across 4 `~B`-owned files in `infra/aws/terraform/imo-pipeline/`:

| File | Contents | Authoring trigger |
|---|---|---|
| `phase2b-lambdas.tf` | 6 `module "find_insure_crawl_job_posting_{board}"` yang-lambda wrappers | First per-board fill |
| `phase2b-iam.tf` | Inline policies extending `find-insure-lambda-role` (read `find-insure/job-board/*` secrets; no IAM widening required for S3 — bronze writes already covered by base `find_insure_s3` `ObjectWriteScoped` policy) | First per-board fill |
| `phase2b-eventbridge.tf` | Per-board fan-out invoke permissions (one `aws_lambda_permission` per board mirroring crawl-web `events_invoke_crawl_web`); per-board EventBridge `aws_cloudwatch_event_rule` if Phase 2B per-board schedule required (default: fan-out from refresh-source-list orchestrator like Phase 1) | First per-board fill |
| `phase2b-secrets.tf` | 6 `aws_secretsmanager_secret` resources for `find-insure/job-board/{board-slug}/api-key` (one per Bα-feasible board where direct API auth is required; OR Bβ-feasibility class boards consume the shared `find-insure/bright-data/api-key` already in `secrets.tf`) | Per-board fill, only Bα-class boards needing custom auth |

Tag stream: `imo-pipeline-phase2b-v0.1.0` start (ws COO ratified per SYNC-CARVE; separate from Phase 1 `imo-pipeline-v0.X.Y` stream). Each per-board ship bumps `phase2b-v0.{N}.0`.

---

## 3. Per-board Lambda module template

The per-board module STUB (fill `{board-slug}` from manifest):

```hcl
# phase2b-lambdas.tf — FIND_INSURE Phase 2 Part B per-board crawl-job-posting Lambdas
#
# Source code: data/find/imo/scripts/bronze/crawl_job_posting_{board}_bronze.py
# Bronze emit: s3://opal-data-imo/corp/{slug}/bronze/job-posting-{board}/{run-date}/
#
# Per-board Bα-direct or Bβ-Bright-Data path determined at runtime by env var
# JOB_BOARD_FETCH_MODE = "B-alpha" | "B-beta"; manifest's B-alpha-feasibility-verdict
# binds the default at deploy time.
#
# File-split per ws COO SYNC-CARVE 2026-05-27T18:15Z.

module "find_insure_crawl_job_posting_{board}" {
  source        = "../modules/yang-lambda"
  function_name = "find-insure-crawl-job-posting-{board}"
  artifact_key  = "imo-pipeline/find-insure-crawl-job-posting-{board}.zip"
  role_arn      = local.imo_lambda_role
  runtime       = "python3.9"
  handler       = "bronze.crawl_job_posting_{board}_bronze.lambda_handler"

  # Sizing rationale per manifest row:
  #   - Bα-direct REST: timeout=300s (per-IMO 5-50 paginated pages * per-page 1-3s)
  #   - Bβ-Bright-Data: timeout=900s (one_shotter wait + per-IMO 5-50 pages)
  #   Memory=1024MB covers per-board structured-JSON buffering (~5-10MB working set).
  timeout     = 300  # raise to 900 if board's B-alpha-feasibility-verdict = NO-GO (Bβ)
  memory_size = 1024

  # Layers populate per-board basis:
  #   - boards using Bα direct REST + stdlib JSON parsing only: no layer
  #   - boards using HTML/JSON-hybrid (Glassdoor likely): find-insure-deps (BS4+lxml)
  #     -> `layers = [aws_lambda_layer_version.find_insure_deps.arn]`
  # layers = []  # uncomment + populate at per-board fill if HTML parsing required

  environment_variables = {
    OPAL_DATA_IMO_BUCKET     = aws_s3_bucket.imo_data.id
    JOB_BOARD_FETCH_MODE     = "B-alpha"          # B-alpha | B-beta — manifest-driven
    JOB_BOARD_NAME           = "{board}"
    BRIGHT_DATA_SECRET_NAME  = aws_secretsmanager_secret.bright_data_api_key.name
    JOB_BOARD_SECRET_NAME    = aws_secretsmanager_secret.find_insure_job_board_{board}.name  # only if Bα custom-auth
    JOB_BOARD_RATE_LIMIT     = "50"               # req/min — manifest "sustainable-rate"
    JOB_BOARD_PAGE_SIZE      = "25"               # manifest pagination.page-size default
    JOB_BOARD_MAX_PAGES      = "20"               # per-IMO ceiling; cost-budget enforced
    COST_BUDGET_SECRET_NAME  = "find-insure/cost-budgets/v0.1"  # DS~E config/cost-budgets-v0.1.json
  }

  system_tag = "IMOPipeline"
}

resource "aws_lambda_permission" "events_invoke_crawl_job_posting_{board}" {
  statement_id  = "AllowExecutionFromEventBridgeFanout"
  action        = "lambda:InvokeFunction"
  function_name = module.find_insure_crawl_job_posting_{board}.function_name
  principal     = "events.amazonaws.com"
  source_arn    = "arn:aws:events:${local.region}:${local.account_id}:rule/find-insure-*"
}
```

---

## 4. Per-board Secrets Manager template

Only for Bα-class boards requiring per-board API key / cookie:

```hcl
# phase2b-secrets.tf
resource "aws_secretsmanager_secret" "find_insure_job_board_{board}" {
  name        = "find-insure/job-board/{board}/api-key"
  description = "Phase 2B {board} job-board API key / cookie (Bα direct REST auth). Andrew rotates out-of-band; AE provisions placeholder at apply-time."
  tags = {
    Name   = "find-insure-job-board-{board}-api-key"
    System = "IMOPipeline"
  }
}
```

NB: Phase 1 already reserves the `find-insure/job-board/*` namespace via `secrets.tf` IAM (`find_insure_secrets` policy ARN pattern `find-insure/job-board/*`). No IAM widening needed — adding new secrets under the namespace is structurally permitted by the existing role.

---

## 5. Per-board sizing matrix (template — fill from manifest)

| Board | Verdict (manifest) | Timeout | Memory | Layer | Secret | Concurrency cap |
|---|---|---|---|---|---|---|
| linkedin-jobs | _PENDING_ | _300 if Bα / 900 if Bβ_ | 1024 | _BS4+lxml if hybrid_ | _find-insure/job-board/linkedin-jobs/api-key if Bα custom_ | 2/board |
| indeed | _PENDING_ | 300 (Bα expected) | 1024 | _none if Bα-JSON_ | _Bα-JSON: none; Bβ: shared bright-data_ | 2/board |
| glassdoor | _PENDING_ | _900 if Bβ likely_ | 1024 | _BS4+lxml likely_ | _Bα: glassdoor cookie; Bβ: bright-data datadome zone_ | 1/board (lower; aggressive bot-defense) |
| ziprecruiter | _PENDING_ | 300 | 1024 | _none if JSON_ | _Bα: none custom; Bβ: shared bright-data_ | 2/board |
| wellfound | _PENDING_ | 300 | 1024 | _none if JSON_ | _Bα: none custom; Bβ: shared bright-data_ | 2/board |
| builtin | _PENDING_ | 300 | 1024 | _none_ | _Bα: none custom; Bβ: shared bright-data_ | 2/board |

(Per-board row final values bind at HAR-audit time when DS~D fills manifest v0.1 `B-alpha-feasibility-verdict` + `bot-defense` + `sustainable-rate`.)

---

## 6. EventBridge fan-out shape

Two options for per-IMO crawl trigger; ws COO ruling at per-board fill time:

**Option A — orchestrator-driven (Phase 1 pattern, recommended for v0.1):** `refresh-source-list` orchestrator Lambda fans out per-IMO + per-board events to a single `find-insure-job-posting-fanout` rule; per-board Lambda permissions in `phase2b-eventbridge.tf` mirror crawl-web `events_invoke_crawl_web`. Concurrency cap enforced by orchestrator emission rate (manifest `sustainable-rate`).

**Option B — per-board scheduled (independent):** Each board gets its own `aws_cloudwatch_event_rule` with a cron schedule; per-IMO fan-out happens inside the per-board Lambda via SQS or direct invocation. Higher cost (per-board scheduler infra) + parallel-fan-out independence.

v0.1 default: Option A (Phase 1 parity). Phase 2B revisits at v0.2 if per-board cadence diverges.

---

## 7. Cost-budget enforcement (DS~E `cost-budgets-v0.1.json` integration)

Per-board cap enforcement at Lambda entry point:

1. Lambda cold-start reads `s3://opal-data-imo/config/cost-budgets-v0.1.json` (env `COST_BUDGET_SECRET_NAME`).
2. Per-board `per_board_caps` default = 100 postings/IMO/board (per DS~E `6ee4c7eb2`).
3. Per-IMO cap check: if today's cumulative scraped postings for `{slug, board}` >= cap → emit blocked-reason `"cost-budget-exhausted"` to bronze + early-return (Bα or Bβ).
4. Global daily/monthly cap check: query telemetry/cost-{date}.json (Phase 0 emit by orchestrator); blocked-reason `"global-budget-exhausted"`.

Cost-budget cross-cutting infrastructure (telemetry emit + daily-rollup) authored by orchestrator (Phase 0 follow-on) NOT per-board Lambda — per-board Lambda only CONSUMES the budget config + emits per-invocation telemetry rows.

---

## 8. Per-board ship cycle (mechanical fill)

For each board's manifest-v0.1-finalized row:

1. **Source authoring** — DS authors `data/find/imo/scripts/bronze/crawl_job_posting_{board}_bronze.py` consuming manifest endpoints + Bα/Bβ branching logic per `JOB_BOARD_FETCH_MODE` env var.
2. **TF authoring (~B)** — Append per-board module + permission to `phase2b-lambdas.tf` + per-board secret to `phase2b-secrets.tf` (if Bα custom-auth).
3. **Source-map entry (~B)** — Add `find-insure-crawl-job-posting-{board}` row to `infra/aws/lambda/ci/lambda-source-map.json` mirroring score-web pattern.
4. **Comp-graph register (~B)** — `comp-pipescript` registration of bronze script per CLAUDE.md Rule 4.
5. **Pre-build commit (~B)** — `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~B <...>" -m "..." -- phase2b-lambdas.tf phase2b-secrets.tf lambda-source-map.json` per Rule 14a.
6. **Build-and-upload (~B)** — `bash infra/aws/lambda/ci/build-and-upload.sh imo-pipeline find-insure-crawl-job-posting-{board}` per Rule 13.
7. **Safe-apply (~B)** — `.tools/safe-apply.sh` per Rule 18; HALTGT checkpoint clears.
8. **Record-deploy (~B)** — `bash infra/aws/lambda/ci/record-terraform-deploy.sh imo-pipeline --version imo-pipeline-phase2b-v0.{N}.0 --author "0.7.0_AE_CloudOps~B <...>"`.
9. **Tag + push** — `git tag -a imo-pipeline-phase2b-v0.{N}.0 + git push --follow-tags`.
10. **RAVC2-Request to ws COO** — per-board ship with empirical-test evidence (3-5 IMO spot-check bronze emit + manifest endpoint round-trip success).

Sizing per board: ~30-60min wall once manifest row finalized + source authored. 6 boards = 3-6h total per-board waterfall. Parallel-feasible across boards if 2-3 ~B-class workers active (single-~B serial waterfall acceptable per Andrew sovereign HAR-cadence pacing).

---

## 9. Pre-fill checks at HAR-audit moment

Before authoring per-board module:

1. **Manifest v0.1 row complete** — verdict + endpoints + auth-mechanism + sustainable-rate + bot-defense + Bα-cost / Bβ-cost all populated for the board.
2. **Source author present** — DS~D or sister-lane has authored `crawl_job_posting_{board}_bronze.py` (or scheduled to).
3. **comp-pipescript io** check on the source — verify column gaps / portal consumers (if applicable) before authoring TF per CLAUDE.md "About to edit a gold script" pattern adapted for bronze.
4. **comp-iam service** check — flag any new boto3 calls (SSM / SQS / etc.) requiring IAM widening beyond the existing `find_insure_*` policies.
5. **Empirical-probe layer dependency** — verify Python imports against existing layers (per ~A's SUBSTRATE-GAP find 18:13Z); avoid duplicating BS4/lxml stack.
6. **Cost-class sign-off** — if board's manifest verdict = Bβ → AE 0.7 base + ws COO sign-off explicit per PRD §4 Phase 2 Part B Stage Bα cost-gate (Bright Data spend per board × 99 IMOs × monthly cadence).

---

## 10. Cross-references

- **DS-side per-board manifest:** `docs/briefs/find-insure-job-board-endpoint-manifest-v0.0.md` (DS~D `97c32ffa4`)
- **DS-side parser-base util:** `data/find/imo/scripts/_util/job_board_parser_base.py` (DS~D `97c32ffa4`)
- **Phase 2B DS scaffold brief:** `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_phase2_part_b_jobs_scaffold.md` (DS~D `05e987f9b`)
- **Cost-budgets-v0.1:** `s3://opal-data-imo/config/cost-budgets-v0.1.json` (DS~E `6ee4c7eb2`)
- **Phase 1 .004 ship precedent:** `infra/aws/terraform/imo-pipeline/lambdas.tf` `find_insure_crawl_web` module (base) + `eventbridge.tf` `events_invoke_crawl_web` (base) + `lambda-source-map.json` `find-insure-crawl-web` entry (commit `672066fa3`).
- **Phase 1 .005 ship precedent (file-split sibling):** `infra/aws/terraform/imo-pipeline/phase1-parse-web-lambda.tf` (~A `69ba19ee3`).
- **Phase 1 .006 ship precedent (~B-owned file-split):** `infra/aws/terraform/imo-pipeline/phase1-score-web-lambda.tf` (~B `4228754a9`).
- **ws COO ratifications:** `[SYNC-CARVE-RATIFIED]` 2026-05-27T18:15Z; `[CONCUR Option (a) SEQUENCE-AB]` 2026-05-27T18:51Z (parallel-fill ratification).
- **PRD:** `docs/architecture/FIND_INSURE.md` v0.4 §4 Phase 2 Part B.

---

## Authoring lineage

- **v0.0** 2026-05-27 — STANDBY-PREP scaffold ship while ~A v0.3.0 tag lands per ws COO Option (a) parallel-fill ratification. Locks file-split convention + per-board module template + per-board ship cycle + pre-fill checks. Each per-board section is a template stub; fill is mechanical at HAR-audit time when DS~D's manifest v0.1 lands.
