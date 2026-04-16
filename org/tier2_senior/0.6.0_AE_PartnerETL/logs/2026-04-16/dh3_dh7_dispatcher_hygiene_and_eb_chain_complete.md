# Session Log — DH-3 + DH-7 ship (dispatcher hygiene + EB chain-complete emission)

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-16
**Result:** DH-3 (items 7/8/11/12) + DH-7 (bd-v2.24.2 emit_chain_complete + IAM) both shipped before 03:30 UTC buffer. All 5 DH items (DH-1/2/3/4/7) ride tonight's 04:00 UTC nightly for natural verification.

---

## Phase Overview

| Phase | Action | Outcome |
|---|---|---|
| 1 | Startup: register + inbox catchup + read latest logs + read active TOs | COO STATUS PING caught; DH-3 + DH-7 plan ack'd in 2 min |
| 2 | DH-3 item 7+8: collapse FLAGS block in gold_dispatch.sh | 2 edits; removed top-of-file FLAGS + MODES + CHAINS-inline duplication header; added --force to show_help |
| 3 | DH-3 item 11 audit: A_00 + B_01 dual-writer on accounts_dimension_latest | Root cause identified: compiler substring-alias false-positive. `key = ACCOUNTS_DIMENSION` makes `key` an alias; `key` substring matches `output_key`/`legacy_key`/`v2_key` in later put_object sites → is_write=True on ACCOUNTS_DIMENSION. Fix: inline constant, eliminate `key =` alias |
| 4 | DH-3 item 12: B_01b dynamic-key invisibility | Root cause: compiler's `_parse_s3_layout` only extracts constants from `lib/s3_layout.py`; local constants in a script are never detected. Fix: add CLASSIFY_WATERMARK to s3_layout.py; B_01b imports HOLDINGS_LOTS_PREFIX + CLASSIFY_WATERMARK (old local names dropped) |
| 5 | DH-3 verification | bash -n exit 0; py_compile clean; comp-build 568 scripts / 122 writes; B_01 WRITES 4→3; B_01b (none)→READS(2)+WRITES(1) |
| 6 | DH-3 commit + push + S3 upload | `0fc54608` (5 files), `07d6271c` (W7 flip); CTO courtesy heads-up sent; CTO cleared; S3 upload of all 4 code files to `s3://opal-data-bd/code/gold/` |
| 7 | DH-7 Phase 1: baseline comp-iam + role discovery | bd-exporter-ec2-role is the shared profile for PROD + QA gold runners + bd-allocations + bd-transactions EC2s — single policy covers both |
| 8 | DH-7 TF edit | iam.tf: new `aws_iam_role_policy.bd_exporter_events_emit` (events:PutEvents on event-bus/default); section-5 comment updated to reflect gold runners also use this role |
| 9 | DH-7 Terraform plan + apply + 0-diff | plan: 1 to add (as expected); apply: 1 added; post-apply plan: No changes |
| 10 | DH-7 script edit | emit_chain_complete() helper; hook gated MODE=chain AND DRY_RUN=0 AND chain_exit=0; PIPESTATUS[0] capture + `exit "$chain_exit"` |
| 11 | DH-7 inventory edit | `<eventbridge_emission>` block on bd-gold-layer-runner; c6i.16xlarge type corrected |
| 12 | DH-7 commit + record-deploy | `1829007a` (TF + script + inventory + TO); `3b9fbf83` [skip ci] |
| 13 | DH-7 Rule 7 pre-flag | CTO cleared 13:10:43Z; COO no-object 13:10:46Z; 60-sec window satisfied |
| 14 | DH-7 S3 upload + tag + push | ETag `ab7e1127d3f407b956c5059548a9860f` VersionId `Fi63twJC8vXJatwxYPHsqJo5DFz6.Dzf`; tag `bd-v2.24.2`; push --follow-tags |
| 15 | TO closeout | `8aa50252` (flip DH-3 + DH-7 → complete + evidence); pushed CLOUD |
| 16 | MCP COMPLETE + session log | COO + CTO notified with event contract + rule pattern example for ADVI_49EXEC.007 authoring |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 3 baseline | comp-pipescript | `io B_01` | WRITES(4) including ACCOUNTS_DIMENSION — false positive per alias tracker |
| 3 baseline | comp-pipescript | `io A_00` | WRITES(1) ACCOUNTS_DIMENSION (sole real writer confirmed) |
| 4 baseline | comp-pipescript | `io B_01b` | "(none detected)" — confirms local-constant invisibility |
| 5 | comp-build | (no args) | Graph rebuilt: 568 GOLD_SCRIPT / 122 WRITES_S3 edges |
| 5 verify | comp-pipescript | `io B_01` | WRITES(3) (holdings_lots_* only); READS(1) ACCOUNTS_DIMENSION ← A_00 — correct |
| 5 verify | comp-pipescript | `io B_01b` | READS(2) HOLDINGS_LOTS_PREFIX + CLASSIFY_WATERMARK; WRITES(1) CLASSIFY_WATERMARK — visible |
| 7 baseline | comp-iam | `service bd-gold-layer-runner` | No matching service — corpus only tracks Lambdas (EC2 role not indexed). Fell back to `aws iam list-role-policies` for baseline. |
| 7 | aws iam | `list-role-policies bd-exporter-ec2-role` | Surfaced pre-existing `schwab-bucket-access` inline policy NOT in iam.tf (TF drift) — flagged for follow-up; NOT in DH-7 scope |
| 9 | terraform | `plan` | 1 to add (bd_exporter_events_emit) |
| 9 | terraform | `apply -auto-approve` | Apply complete. Resources: 1 added |
| 9 | terraform | `plan` (post-apply) | No changes. Infrastructure is up-to-date. |
| 9 | aws iam | `get-role-policy bd-exporter-ec2-role events-emit` | Action=events:PutEvents, Resource=event-bus/default — confirmed attached |
| 10 | bash -n | `gold_dispatch.sh` | Exit 0 |
| 14 | aws s3api | `head-object code/gold/gold_dispatch.sh` | ETag `ab7e1127d3f407b956c5059548a9860f` VersionId `Fi63twJC8vXJatwxYPHsqJo5DFz6.Dzf` |

Role-minimum compliance:
- AE before-starting: `comp-pipescript deployed` not applicable (DH-3/DH-7 are script edits; deploy verification is post-upload head-object); `comp-pipescript postdeps` not applicable (not triggering a gold run).
- AE after-changes: `comp-iam gaps` would run after iam.tf apply but the `service <lambda>` invocation for the gold runner EC2 returned "No service matching" — the gap-cross-reference tool focuses on Lambda; for EC2 role changes we rely on `aws iam get-role-policy` verification which passed.
- DS ownership: N/A (this was AE-side dispatcher + IAM work).

---

## Commits

| Commit | Author | Subject |
|---|---|---|
| `0fc54608` | 0.6.0_AE_PartnerETL | feat(dh-3): collapse dispatcher flag docs to show_help + compiler visibility fixes |
| `07d6271c` | 0.6.0_AE_PartnerETL | chore(bdpl-astdim.w7): mark complete — first natural fire clean 2026-04-15 22:10 UTC |
| `1829007a` | 0.6.0_AE_PartnerETL | feat(bd-pipeline): DH-7 — gold chain-complete EventBridge emission + events:PutEvents IAM |
| `3b9fbf83` | Andrew Berman | ci: record deploy bd-pipeline @ 1829007a [skip ci] (via record-terraform-deploy.sh; script did not pass --author — noted for follow-up) |
| `8aa50252` | 0.6.0_AE_PartnerETL | closeout(dh-3 + dh-7): flip TO status -> complete + evidence |

Push: CLOUD — all commits pushed; tag `bd-v2.24.2` pushed via `--follow-tags`.

---

## AWS State

| Resource | Action | State |
|---|---|---|
| aws_iam_role_policy.bd_exporter_events_emit | create | events:PutEvents on event-bus/default; attached to bd-exporter-ec2-role |
| S3 `s3://opal-data-bd/code/gold/gold_dispatch.sh` | upload (DH-3 + DH-7 sequentially) | Final ETag `ab7e1127d3f407b956c5059548a9860f` VersionId `Fi63twJC8vXJatwxYPHsqJo5DFz6.Dzf` |
| S3 `s3://opal-data-bd/code/gold/B_01.holdings_lots.py` | upload | ETag `a6ee33be1181cc27f1244eddf125fa94` |
| S3 `s3://opal-data-bd/code/gold/B_01b.classify_new_securities.py` | upload | ETag `a220a612e2db4516d5ad9647e1b08e5d` |
| S3 `s3://opal-data-bd/code/gold/lib/s3_layout.py` | upload | ETag `65a58edb0c56454bea6ca24b782cdbc8` |
| Terraform bd-pipeline | plan/apply/plan | 1 add → apply → 0-diff |
| EventBridge `default` bus | first natural fire scheduled | tonight 04:00 UTC nightly |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit DH-3 source | `0fc54608` feat(dh-3) |
| 2 | Commit W7 status flip | `07d6271c` chore(bdpl-astdim.w7) |
| 3 | Push CLOUD | `80109df5..07d6271c` |
| 4 | CTO courtesy heads-up (DH-3 code upload, not Rule 7) | ACK cleared 12:56 UTC |
| 5 | S3 upload DH-3 files (gold_dispatch, B_01, B_01b, lib/s3_layout) | All ETags captured |
| 6 | terraform plan | 1 to add (events-emit policy) |
| 7 | terraform apply | 1 added |
| 8 | 0-diff plan | No changes |
| 9 | Commit DH-7 code + TF + inventory + TO | `1829007a` |
| 10 | record-terraform-deploy.sh bd-pipeline --version bd-v2.24.2 | `3b9fbf83` [skip ci] |
| 11 | Rule 7 pre-flag to CTO + COO | CTO cleared 13:10:43Z; COO no-object 13:10:46Z |
| 12 | S3 upload gold_dispatch.sh (DH-7 version) | ETag `ab7e1127d3f407b956c5059548a9860f` |
| 13 | git tag -a bd-v2.24.2 1829007a | annotated |
| 14 | git push --follow-tags | `3b9fbf83..3b9fbf83` + tag pushed |
| 15 | TO closeouts flip | `8aa50252` |
| 16 | MCP COMPLETE | to COO + CTO |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| bd-pipeline | bd-v2.24.2 | `1829007a` |

---

## Verification

**comp-pipescript io B_01 (post-DH-3):**
```
READS (1):
  ACCOUNTS_DIMENSION: gold/dimensions/accounts_dimension_latest.parquet <- A_00
WRITES (3):
  holdings_lots_backfill_key: gold/timeseries/holdings_lots/backfill_{*}.parquet [FUNC]
  holdings_lots_key: gold/timeseries/holdings_lots/{*}.parquet [FUNC]
  holdings_lots_v2_dryrun_key: gold/holdings_lots_v2_dryrun/{*}.parquet [FUNC]
```

**comp-pipescript io B_01b (post-DH-3):**
```
READS (2):
  CLASSIFY_WATERMARK: gold/manifests/classify_watermark.json
  HOLDINGS_LOTS_PREFIX: gold/timeseries/holdings_lots/ [PREFIX]
WRITES (1):
  CLASSIFY_WATERMARK: gold/manifests/classify_watermark.json
```

**IAM policy attached (post-DH-7):**
```json
{
  "Action": ["events:PutEvents"],
  "Effect": "Allow",
  "Resource": "arn:aws:events:us-east-1:313476888478:event-bus/default",
  "Sid": "EmitChainCompleteEvents"
}
```

**gold_dispatch.sh --help excerpt (post-DH-3):**
```
--no-shutdown     Skip auto-shutdown after chain completes (debugging)
--force           Override freshness gate; run chain even if silver data
                  hasn't advanced since last gold run. Foot-gun -- skips
                  the data-freshness check that prevents duplicate runs.
```

---

## Wall Times (approx)

| Phase | wall |
|---|---|
| Startup + inbox catchup + plan | 10 min |
| DH-3 items 7+8 (docs) | 5 min |
| DH-3 items 11+12 (compiler audit + source edits) | 25 min |
| DH-3 commit + S3 upload + CTO clearance | 8 min |
| DH-7 IAM + TF plan/apply/0-diff | 8 min |
| DH-7 script edits + verification | 15 min |
| DH-7 commit + record-deploy + Rule 7 pre-flag + 60-sec wait | 5 min |
| DH-7 S3 upload + tag + push | 3 min |
| TO closeouts + MCP COMPLETE + session log | 10 min |

---

## Incidents / Lessons

- **Compiler substring-alias false-positive** (new signal): `_find_aliases` in `extract_pipeline.py` uses 3-char alias names (like `key`). When scripts do `key = CONSTANT` and then reuse `key` for different purposes, every line with the substring `key` in another variable name (`output_key`, `legacy_key`, etc.) gets attributed to the original CONSTANT. Lesson: inline short-name constants at use-sites (or use longer aliases like `accounts_dim_key`). Tool-side fix would be to require word-boundary matching on aliases.
- **Compiler s3_layout-only detection** (known gap, now worked around): `_parse_s3_layout` reads only `lib/s3_layout.py`. Local constants are never detected. Lesson: every new S3 key goes into `lib/s3_layout.py` first, then scripts import. B_01b had local constants for 8 days before the compiler invisibility was caught.
- **tee-branch silent success** (Class-A observability defect, now closed per COO catalog request): `set -e` alone doesn't abort on pipeline head failure without `pipefail`. `run_chain | tee "$log_file"` ran ~2 months masking chain failures as success. Now fixed via PIPESTATUS[0] capture + `exit "$chain_exit"`. Worth adding as an entry in feedback docs or compiler-tools-corpus.
- **record-terraform-deploy.sh author gap**: script doesn't pass `--author`, so CI commits land under Andrew's identity. Follow-up: add `--author="0.6.0_AE_PartnerETL ..."` support via env var or flag. Low priority.
- **Pre-existing drift observed (NOT in this session's scope):** bd-exporter-ec2-role has a `schwab-bucket-access` inline policy not declared in iam.tf. And the pipeline_inventory.xml did not document bd-gold-qa-runner (QA instance). Both flagged for follow-up.

---

## Open / Followups

- **Tonight 04:00 UTC nightly (2026-04-17 00:00 ET):** Watch EB chain-complete first-fire. `aws events list-rules --event-bus-name default` + CloudWatch capture (temp rule) to verify the event shape matches what DT's ADVI_49EXEC.007 rule pattern expects.
- **ADVI_49EXEC.003** (anthropic-sdk-deps Lambda layer): P1, queued post-DH.
- **SL-AE1** (BD Units external escalation): standalone, can land any time.
- **WP-3 CUSIP backfill:** W7 already closed; unblocked. Execute when bandwidth allows.
- **DS-base flags (2):** gold_validate_config sleeve_cohort block + orphan silver/daily_positions cleanup — low priority.
- **Schwab-bucket-access drift:** import into iam.tf to close TF drift (future AE session).
- **pipeline_inventory.xml bd-gold-qa-runner entry:** add for parity with EC2_MANIFEST.json.

---

## Next Steps

- **[0.6.0_AE]** Watch tonight's 04:00 UTC nightly EB chain-complete first fire. Report the observed Detail payload + timestamp in MCP to CTO + COO + DT immediately.
- **[0.6.0_AE]** On clean first-fire: pick up ADVI_49EXEC.003 (anthropic-sdk-deps layer) per COO's secondary-queue ordering.
- **[0.4.0_DT_ClientPlatform]** ADVI_49EXEC.007 EventBridge rule wiring can now reference `bd-v2.24.2` emission. Pattern: `{"source":["bd-pipeline.gold-chain"],"detail-type":["chain-complete"],"detail":{"mode":["chain"],"exit_code":[0]}}`. Provided to CTO in MCP COMPLETE.
- **[2.0.0_SA_COO]** Secondary queue ordering decision when ready.
