# work_1838Z -- FIND_INSURE.005 Lambda packaging pre-apply (~A spawn cycle 1)

**Agent:** 0.7.0_AE_CloudOps~A
**Cycle:** /work cycle 1 (substantive)
**Authority:** ws COO `[SPAWN-WITH-DIRECTION]` 2026-05-27T18:08Z `/allocation #4` -- Phase 1 .005 Lambda packaging immediate-first; Phase 2A scaffold STANDBY-PREP

## Inbound context absorbed this cycle

| T | From | Subject | Disposition |
|---|---|---|---|
| 18:06Z | DS 0.1.0~A (prior session) | F1 SEAT CLAIM (YCharts) | MOOT-absorb (prior-session-context; DS clarified later) |
| 18:06Z | DS 0.1.0~A (prior session) | F1 SEAT FREE | MOOT-absorb (work complete; staged YCharts capture work dropped) |
| 18:07Z | DS 0.1.0 (current session) | Context-clarify (prior-session provenance) | ACK; no follow-on |
| 18:08Z | ws COO | SPAWN-WITH-DIRECTION ~A | ACK; primary execution authority |
| 18:15Z | ws COO | SYNC-CARVE-RATIFIED (file-split) | ACK; `phase1-parse-web-lambda.tf` adopted |
| 18:20Z | ws COO | CONCUR Option (a) on SUBSTRATE-GAP | ACK; layer creation proceeding |
| 18:24Z | ws COO | OWNED-PATHS-FIX (SHARED_CLOUD_OPS +~A) | ACK; per-tick logs unblocked |
| 18:24Z | DS 0.1.0~C | SISTER-LANE HANDSHAKE | ACK; Phase 2A coord at post-Phase-1-RAVC2-Accept |
| 18:32Z | DS 0.1.0~C | Phase 2A dep profile reciprocity | Banked for Phase 2A scaffold authoring |
| 18:35Z | ws COO | SYNC-STATUS pull | ACK + heartbeat refresh + status timeline |

## Outbound this cycle

| T | To | Subject | Class |
|---|---|---|---|
| 18:06Z | DS 0.1.0 | ACK-A4-recapture-dropped | peer-ack |
| 18:10Z | ws COO | [BLOCKED-ASK] capacity-available | pre-substrate |
| 18:13Z | ws COO | [ACK] SPAWN-WITH-DIRECTION absorbed | substrate-ack |
| 18:17Z | ws COO | [CARVE-ACK + SUBSTRATE-GAP] | sub-AC-discovery |
| 18:22Z | ws COO | [OWNED-PATHS-GAP] SHARED_CLOUD_OPS missing ~A | tilde-lane-gap |
| 18:24Z | DS 0.1.0~C | SISTER-LANE ACK | peer-ack |
| 18:36Z | ws COO | [STATUS] (a) executing timeline | status-pull-response |

## SUBSTRATE-GAP discovery + resolution

**Finding** (this cycle's primary lift contribution): TO `FIND_INSURE.005` AC5 + DS~A `parse_web_silver.py` module docstring both assumed an existing `find-insure-lambda` Lambda layer shipping BS4 + lxml for python3.9. Empirically false:

- `aws lambda list-layers --region us-east-1` -- no `find-insure-*` layer in account
- `aws lambda get-function-configuration --function-name find-insure-crawl-web` -- `Layers: null` (stdlib-only; uses urllib for Bright Data, NOT BS4)
- `extract_source_list.py` (referenced as proof of the existing layer) is a one-shot script, never deployed as a Lambda

**Resolution path:** Option (a) per CLAUDE.md Rule 3 ("Use existing layers or flag the need for a new one") -- author NEW `find-insure-deps` layer (BS4 + lxml; python3.9; manylinux2014_x86_64 wheels). ws COO explicit CONCUR 18:20Z (NOT silent-bind per LD-0090; explicit ratification with banking of the canonical pattern for future find-insure-* parser Lambdas).

**Cross-lane forward-pass:** DS~C reciprocated 18:32Z with Phase 2A `parse_linkedin_silver` + `score_linkedin_gold` + `crawl_linkedin_bronze` + `opt_out_webhook_receiver` dep profile. Recommends sibling layer `find-insure-parse-deps` (pyarrow + pandas + jsonschema; ~110MB) for Phase 2A. Saves Phase 2A discovery roundtrip. Banked for Phase 2A scaffold authoring (post-Phase-1-RAVC2-Accept).

## Substantive artifacts shipped (pre-apply)

| Artifact | Path | Notes |
|---|---|---|
| Layer source dir | `infra/aws/lambda/layers/find-insure-deps/` | requirements.txt + build-layer.sh + README.md |
| Layer zip (S3) | `s3://opal-313476888478-lambda-artifacts/layers/find-insure-deps.zip` | 4.9M; sha256 `NUMjNHfhgr8b2yW6v10+TIsvX2yuR/UqY+dpkE1lMIw=` |
| Layer TF | `infra/aws/terraform/imo-pipeline/layers.tf` | `aws_lambda_layer_version.find_insure_deps`; python3.9 + x86_64 compat |
| Lambda TF | `infra/aws/terraform/imo-pipeline/phase1-parse-web-lambda.tf` | `module.find_insure_parse_web` (yang-lambda wrapper); handler=`silver.parse_web_silver.lambda_handler`; timeout=600s; memory=1024MB; layers=[find-insure-deps]; EventBridge invoke perm `rule/find-insure-*` |
| Lambda zip (S3) | `s3://opal-313476888478-lambda-artifacts/imo-pipeline/find-insure-parse-web.zip` | 12K; sha256 `O2YZF8LcwYvxLc1J+NZ19ZWwyTj2NC+3yxgUSizfF5E=` |
| Source-map | `infra/aws/lambda/ci/lambda-source-map.json` | NEW entry `find-insure-parse-web` (between crawl-web and score-web alphabetically) |

## Concurrent-agent isolation

`phase1-score-web-lambda.tf` (base-lane stale WIP from ~14:22Z, awaits ~B handoff) temporarily moved to `.runtmp/ae-a-cycle-stash/` so terraform plan/apply does not 404 on the absent `find-insure-score-web.zip` S3 object. Restore to original location after my apply lands. Source-map score-web entry intentionally NOT in my commit (left for ~B to ship with their build).

## Plan output (pre-apply)

`terraform plan` (after re-init): **4 to add, 0 to change, 0 to destroy**:
1. `aws_lambda_layer_version.find_insure_deps` (find-insure-deps layer)
2. `module.find_insure_parse_web.aws_lambda_function.this` (parse-web Lambda)
3. `module.find_insure_parse_web.aws_cloudwatch_log_group.lambda` (parse-web log group, 14-day retention)
4. `aws_lambda_permission.events_invoke_parse_web` (EventBridge invoke perm)

## Next sub-steps (this cycle)

- Pre-apply commit (Rule 2) via `.tools/safe-commit.sh`
- safe-apply (HALTGT checkpoint per Rule 18)
- 0-diff plan verify
- Tag `imo-pipeline-v0.3.0` + push --follow-tags
- `record-terraform-deploy.sh imo-pipeline --version imo-pipeline-v0.3.0 --author "0.7.0_AE_CloudOps~A <0.7.0_AE_CloudOps~A@opal.agent>"`
- Restore `phase1-score-web-lambda.tf` from `.runtmp/ae-a-cycle-stash/`
- Cold-start verification (invoke parse-web with synthetic event; confirm BS4 import succeeds + structured response)
- `comp-pipescript deployed` MATCH on parse_web_silver.py
- `comp-iam service find-insure-parse-web` no-gaps
- RAVC2-Request to ws COO; CC ws CTO + DS~A + AE 0.7 base

## archetype

IMPLEMENT + DEPLOY + EMPIRICAL (mirror of base lane's .004 cycle).
