# ADHC_ROUTER.T2 — comp-pipescript deployed audit vs WP-10b

**Date:** 2026-04-15 (EDT)
**Agent:** 0.4.0_DS_ClientPlatform~B
**TO:** `ADHC_ROUTER.T2.ds-b-test-comp-pipescript-deployed-vs-wp10b.md`

## Summary

Stress-tested `comp-pipescript deployed` against 4 scopes (gold script, two silver scripts, full sweep) and a deliberate AWS-env-break. Found one **correctness defect**: broken AWS credentials produced `MISSING_ON_S3` instead of an honest unreachable status — the tool was claiming parity failures it could not actually verify. Patched `pipeline_cli.py::cmd_deployed` with a new `AWS_UNREACHABLE` status + explicit remediation text. Commit below.

## Compiler Tools — Rule 7 Reproduction

**AWS environment at run time:** static creds from `~/.aws/credentials` (default profile), `AWS_EC2_METADATA_DISABLED=true` set via `.bashrc`, Windows WMI hang fix via `sitecustomize.py`. Standard shell.

### Phase 1 — Happy-path runs

| # | `<run>` | `<expect>` | Observed | Pass/Fail |
|---|---------|-----------|----------|-----------|
| 1 | `comp-pipescript deployed D_04` | MATCH/STALE/MISSING reporting, <30s, no aws-CLI-not-found | `[GOLD] D_04 MATCH`, summary line, <3s | **PASS** |
| 2 | `comp-pipescript deployed bd_price_update.py` | `[SILVER] bd_price_update.py: MATCH` | `[SILVER] bd_price_update.py MATCH`, <3s | **PASS** |
| 3 | `comp-pipescript deployed inject_scoped_overrides.py` | Same shape as above | `[SILVER] inject_scoped_overrides.py MATCH`, <3s | **PASS** |
| 4 | `comp-pipescript deployed` (full sweep) | All gold+silver reported; TIMEOUTs include guidance | 39 MATCH, 1 MISSING_ON_S3 (`upload_bd_assets_backfill.py` genuinely absent from S3, clear 404 from stderr), 0 TIMEOUT. Full sweep completed in ~40s. | **PASS** |

### Phase 2 — Adversarial runs

| # | `<run>` | `<expect>` | Observed | Pass/Fail |
|---|---------|-----------|----------|-----------|
| 5 | `AWS_PROFILE=nonexistent_profile AWS_ACCESS_KEY_ID="" AWS_SECRET_ACCESS_KEY="" AWS_SESSION_TOKEN="" comp-pipescript deployed D_04` (pre-patch) | Explicit unreachable message + no silent MATCH | **DEFECT FOUND.** Output: `[GOLD] D_04 MISSING_ON_S3` + `The config profile (nonexistent_profile) could not be found`. Summary: `0 MATCH, 0 STALE, 1 MISSING_ON_S3`. Tool claimed the file was absent from S3 when it could not even reach S3. | **FAIL** |
| 6 | Same command, **post-patch** | New `AWS_UNREACHABLE` status + remediation text | `[GOLD] D_04 AWS_UNREACHABLE` + stderr echo. Summary: `0 MATCH, 0 STALE, 0 MISSING_ON_S3, 0 LOCAL_MISSING, 0 TIMEOUT, 1 AWS_UNREACHABLE`. Footer: "AWS credentials/network could not reach S3; MATCH/MISSING is NOT verified. Fix: check AWS_PROFILE / credentials / VPN, then re-run. See `aws sts get-caller-identity`". | **PASS** |

### Phase 3 — Re-run originally-failing cases against patched code

Run 1-4 re-executed under default creds: all still PASS (no regression). Run 5 confirmed the defect is closed (see Run 6).

## Would this have helped WP-10b?

My WP-10b session log (`wp10b_gold_silver_recon_harness.md`) shows `comp-pipescript deployed` was NOT in my Phase 2 triad — the harness is a new node, so no S3 upload/deploy check was necessary. No workarounds needed there.

The AWS-adjacent workarounds I did use during WP-10b were:
- `aws s3 ls s3://opal-data-bd/diagnostics/...` to verify manifest upload — direct CLI, no compiler path involved.
- `aws s3 ls s3://opal-data-bd/gold/entities/clients/ --recursive` to probe JSON layout — direct CLI.

Both were raw AWS CLI, not comp-tool flows. Env-forwarding on `comp-pipescript deployed` did not gate any WP-10b step. **So: for WP-10b specifically, no workarounds would have been eliminated by the 0324142a fix. But the defect the fix was meant to close is only fully closed with today's AWS_UNREACHABLE patch** — without that, any future agent hitting a credentials issue would have been actively misled by `MISSING_ON_S3`.

## Critical lens

**TIMEOUT message quality (when triggered):** the existing footer prints `"Check caller credentials/network, or rerun with AWS_EC2_METADATA_DISABLED=true in the invoking shell."` — that's actionable even for an agent who hasn't seen the Windows WMI / IMDS fixes, because it both (a) names the remediation flag and (b) points to the invoking shell. Acceptable.

**MISSING_ON_S3 pre-patch:** **not acceptable.** Conflating "404 HeadObject" with "credentials broken" hid a real correctness signal. An agent running against broken creds would have (wrongly) concluded "the script isn't uploaded" and spent time chasing a phantom upload path instead of fixing their AWS env. Patched with a dedicated `AWS_UNREACHABLE` bucket.

**Remaining gap:** the patch detects credentials/auth/network errors via a string-match allowlist (`Unable to locate credentials`, `ExpiredToken`, `could not be found`, `AccessDenied`, etc.). Any novel error string AWS CLI adds in a future version would fall through to `MISSING_ON_S3`. Structural fix would be to parse the returncode + error response type from `aws s3api head-object --output json` and distinguish `NoSuchKey` (genuine 404) from everything else — but that's a larger refactor, backlog.

## Patch

| File | Change |
|------|--------|
| `org/modules/graph/pipeline_cli.py` | New `AWS_UNREACHABLE` status in `cmd_deployed::_check_one`; credential/network stderr signatures routed there; new `aws_unreach` bucket in summary; footer with remediation text. |

Pre-patch summary line would have shown `MISSING_ON_S3` for broken creds; post-patch shows `AWS_UNREACHABLE` with explicit remediation.

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Session log at specified path | **PASS** |
| 2 | Every run reproduced w/ observed output + AWS env state | **PASS** |
| 3 | "Would WP-10b have been helped?" paragraph | **PASS** |
| 4 | TIMEOUT message quality critical lens | **PASS** (no TIMEOUT triggered; existing footer adequate) |
| 5 | "NEVER seen tool before could diagnose" bar | **PASS** post-patch; pre-patch misled. |
