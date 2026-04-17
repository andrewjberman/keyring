# Session Log -- 2026-04-16 -- Install polars on bd-gold-layer-runner + bd-gold-qa-runner

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date | 2026-04-16 (ET) / 2026-04-17 UTC |
| TO | CTO MCP 20260417T002810Z (ad-hoc; no task_orders/ file) |
| Parallel GO | COO MCP 20260417T003447Z (resend of same TO) |
| Authorization | CTO direct + GO on flex 20260417T003457Z |

---

## Objective

Install polars on bd-gold-layer-runner (PROD, EventBridge-only) and
bd-gold-qa-runner (QA, manual dispatch) so DS ~B's C_00 polars port
(staged at local commit `f177240b`) can run against 11.5M rows.

DS ~A's research confirmed: x86_64 Ubuntu 22.04, system python3 (no venv),
manylinux prebuilt wheel, no pandas/pyarrow conflicts. First-boot +30-60s
(wheel fetch + install), subsequent +2-3s (idempotent cache hit).

No TF change (CLAUDE.md rule 9: TF manages EC2 infra, not code).
No runner start (per TO: deploy-only; Andrew controls chain dispatch).

---

## Implementation

### Edit — `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh`

Added polars install after the network-wait `sleep 10`, before the
S3 script sync:

```bash
# Install polars (manylinux x86_64 wheel; idempotent cache hit on subsequent boots).
# Base deps (pandas/pyarrow/boto3/...) are installed first-boot by setup-instance.sh L20-21.
# polars added here so every boot picks it up without re-imaging. +30-60s first-boot, +2-3s after.
log "Ensuring polars is installed..."
pip3 install polars --quiet 2>&1 | tee -a "$LOG_FILE" || log "WARN: polars install failed (continuing; gold scripts using polars will error explicitly)"
```

Placement rationale:
- After self-update re-exec (L30-42): install runs only once per boot, not twice.
- After `sleep 10` network wait: pip needs network up.
- Before `aws s3 sync` of gold scripts: polars available before any gold script runs.
- WARN-and-continue on failure: gold scripts using polars will error loudly with ImportError; this keeps non-polars runs working even if PyPI is transiently down.

### Both runners updated from one edit

`bd-gold-qa-runner/setup-instance.sh` L41 pulls from
`s3://${S3_BUCKET}/code/runner/run-gold-layer.sh` -- SHARED with PROD.
Confirmed via `aws s3 ls s3://opal-data-bd/code/runner-qa/` which
contained only setup-instance.sh + user-data.sh (no runner script).

One edit + one S3 upload serves both runners.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Baseline verify-ec2.sh | No drift reported for bd-gold-layer-runner. Note: script has pre-existing jq quoting bug on Windows (reports "No source_path" for most services despite manifest being intact). Manually diff'd local vs S3 `code/runner/run-gold-layer.sh` = IDENTICAL pre-edit. |
| 2 | FLEX PRE-FLAG to CTO + FYI to COO | 003430Z / 003433Z. Narrow-scope upload (targeted cp) vs full deploy-to-ec2.sh sync. Reason: avoid --delete sweep on bronze/silver/gold/ while DS is in-flight on gold perf. |
| 3 | Edit run-gold-layer.sh + commit | `4a6173db` feat(bd-gold-runner): install polars on every boot via run-gold-layer.sh |
| 4 | aws s3 cp to code/runner/ | Upload 5.7 KiB; verified LOCAL == S3 post-upload. |
| 5 | CTO GO received 003457Z | Explicit approval, not silence. "Ship it." |
| 6 | Update EC2_MANIFEST.json (both runners) | deployed_commit = 4a6173db, deployed_at = 2026-04-17T00:35:36Z, deployed_by = 0.4.0_DT_ClientPlatform for both bd-gold-layer-runner and bd-gold-qa-runner. Also last_deploy/last_deploy_commit/last_deploy_note on PROD entry. |
| 7 | Commit manifest | `f4c69463` deploy(bd-gold-runners): record polars install |
| 8 | ASCII fix (em dash -> --) | `5afaed67` fix(EC2_MANIFEST): ASCII-only in last_deploy_note (CLAUDE.md rule 13) |
| 9 | Push CLOUD | `1aef359b..5afaed67  CLOUD -> CLOUD` |

No tags pushed (EC2 code deploy, not Terraform apply).

---

## Verification

**S3 object (post-upload):**
```
2026-04-16 20:35:15       5824 s3://opal-data-bd/code/runner/run-gold-layer.sh
```

**Local vs S3 parity:** `diff` exit 0, `LOCAL==S3` confirmed.

**Manifest state (post-commit 5afaed67):**
```
bd-gold-layer-runner.deployed_commit: 4a6173db836ebfc0c8a0a8d026d8b1d97892cfc2
bd-gold-layer-runner.deployed_at:     2026-04-17T00:35:36Z
bd-gold-layer-runner.deployed_by:     0.4.0_DT_ClientPlatform
bd-gold-layer-runner.last_deploy:     2026-04-17
bd-gold-layer-runner.last_deploy_commit: 4a6173db
bd-gold-layer-runner.last_deploy_note: polars install on every boot (run-gold-layer.sh) -- unblocks C_00 polars port

bd-gold-qa-runner.deployed_commit:    4a6173db836ebfc0c8a0a8d026d8b1d97892cfc2
bd-gold-qa-runner.deployed_at:        2026-04-17T00:35:36Z
bd-gold-qa-runner.deployed_by:        0.4.0_DT_ClientPlatform
```

**CLOUD push:** `1aef359b..5afaed67` pushed to origin/CLOUD.

---

## Compiler Tools

| Tool | Run | Result | Notes |
|------|-----|--------|-------|
| `verify-ec2.sh bd-gold-layer-runner` | Baseline | "0 checked" -- pre-existing jq quoting bug on Windows (reports "No source_path" for most services). Not caused by this change. Manifest is intact (verified via direct `jq -r '.services["bd-gold-layer-runner"].source_path'`). | Logged to CTO as informational; out of scope for polars TO. |
| `aws s3 cp` + `diff` | Post-upload parity check | LOCAL == S3 exact match | Manual equivalent of verify-ec2.sh --ssm for just the runner file. |

No comp-iam, comp-blast, comp-routes runs -- this TO touched one bash script
(bootstrap) and one manifest JSON. No new boto3 calls, no IAM changes,
no CloudFront, no Lambda, no Terraform.

---

## Blockers / Open Items

- None for this TO.
- ~B's `f177240b` C_00 polars port is staged locally and ready to ship once
  DS is unblocked by this COMPLETE signal.
- `verify-ec2.sh` jq quoting bug on Windows should be tracked as a tool-level
  fix (not urgent; existing tool works via direct jq calls).

---

## Current State

- polars install line live in `s3://opal-data-bd/code/runner/run-gold-layer.sh`
- Both runners will pick up polars on next boot via self-update from S3.
- EC2_MANIFEST.json records the deploy under both runner entries.
- CLOUD pushed (HEAD = 5afaed67).
- No runner was started. Andrew controls chain dispatch.

## Next Steps

- [0.4.0_DS_ClientPlatform ~B] Ship f177240b C_00 polars port to S3 (`code/gold/`); polars is installed on both runners.
- [Andrew] When QA chain dispatch is desired, boot bd-gold-qa-runner; run-gold-layer.sh self-updates from S3 and installs polars in +30-60s (first boot) or +2-3s (subsequent).
- [self] Standby. No further action on this TO. ADVI_49EXEC.004 remains paused on DS TO 2 (unchanged from earlier session log).
