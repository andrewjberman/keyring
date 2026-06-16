# Session log -- 0.7.0_AE_CloudOps~B -- NFRA_INFRPT: DR + P0(a+b+c) + DR2 COMPLETE

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, IMPLEMENT, COORDINATE
**date:** 2026-06-16
**window:** session start (~19:14Z GO) -> ~22:11Z
**lane:** 0.7.0_AE_CloudOps~B (NFRA_INFRPT lane)

## Summary
Launched on NFRA_INFRPT (Andrew-direct via CVO, CTO-signed). Delivered the DR active-failure fix,
all of P0 (a+b+c), and DR2 -- all verified-live + RAVC2-accepted by COO. 12 commits, 4 deploy
ledgers CLOSED, 0 stranded legs. Also diagnosed a fabric-wide git-push hang (Andrew root-fixed).

## Current State (handoff surface)
- **NFRA_INFRPT.DR (CLOSED):** the infrastructure-daily-snapshot Lambda (2 AM DR backup) had NEVER
  produced a restore point since deploy 2026-02-17 (~4mo, not "3 days" -- the report's 3/3 was its
  own lookback). 3 compounding bugs: (1) target bucket opal-infrastructure-snapshots never existed;
  (2) Lambda on the shared opal-portal-lambda-role missing 16/20 perms (live error = account-less
  snapshot-ARN scoping miss on ec2:CreateImage); (3) the purpose-built infrastructure-snapshot-role
  existed but was unused. Fixed via TF (s3.tf bucket + main.tf IAM). Verified: 9 AMIs +
  ec2-instances.json landed. Commit f6c905fdb; ledger 20260616T2001Z.
- **NFRA_INFRPT.P0 (COMPLETE, a+b+c live):** opal-infrastructure-monitor report generator.
  a) killed §3 fake AI-call tracker; b) §2 SmartX = real served-artifact freshness
  (json/portfolios/account-distribution.json + aum-metrics.json mtime vs daily cadence; ok/watch/
  stale) replacing the dead-EC2 false-STALE; c) §6 triage + §5 security-briefing re-homed to Claude
  via the Anthropic SDK (anthropic-sdk-deps layer + anthropic-api-key secret + claude-sonnet-4-6;
  runtime bumped 3.11->3.12). Monitor Lambda onboarded to TF (infra-monitor.tf). Commits 26a950431
  /1eb0ad881/57288ecb2; ledgers 20260616T2110Z + 2140Z. Invoke-verified: §3 gone, §2 real, §6/§5
  Claude-generated.
- **NFRA_INFRPT.DR2 (CLOSED):** repointed the snapshot Lambda to the dedicated infrastructure-
  snapshot-role + onboarded to TF (infra-snapshot.tf); REMOVED the temp EC2SnapshotPermissions +
  InfraSnapshotIO from the shared role (least-privilege restored, time-boxed exception closed); EBS
  scoped-fix (skip AMI'd-instance vols + non-fatal per-vol + all components non-fatal -> COMPLETE
  manifest lands). Commit 4cd7f74e5; ledger 20260616T2155Z. Verified: complete manifest (10
  artifacts) + 25 EBS snaps on the dedicated role; repoint live; grants gone.
- **Labeled-separate:** monitor role granted read-only CloudWatch Logs (MonitorLogsRead in
  infra-monitor.tf -- the §6 triage surfaced it lacked log-read). Commits b0254c1ed/bbf3adc72.
  All 4 logs-read actions IAM-sim allowed.
- **HEAD:** bbf3adc72, pushed origin/CLOUD.

## Files Modified
see commit messages: f6c905fdb, 26a950431, 1eb0ad881, 57288ecb2, 4cd7f74e5, b0254c1ed, bbf3adc72
(+ ledgers 17b4f08fc, 2d74aebca, a4872628d, 9ecccf228, 51a43ec25). Key files:
infra/aws/terraform/shared-infra/{s3.tf, main.tf, infra-monitor.tf, infra-snapshot.tf};
infra/aws/lambda/infrastructure_monitor/lambda_function.py;
infra/aws/lambda/infrastructure-daily-snapshot/lambda_function.py;
infra/aws/lambda/ci/lambda-source-map.json.

## Deployment Sequence + Verification (DT/AE)
- DR: safe-apply 6/1/0 (HALTGT clear); IAM-sim all-allowed; invoke -> 9 AMIs + ec2-instances.json.
- P0 a+b: import opal-infrastructure-monitor + safe-apply 0/1/0; invoke -> §3 absent, §2 "ok" 9.8h,
  archived 21-16-54.json.
- P0 c: safe-apply 1/1/0 (runtime->3.12 + anthropic-sdk-deps:1 layer + MonitorAnthropicSecretRead);
  invoke -> §6 real Claude triage + §5 real briefing.
- DR2: import infrastructure-daily-snapshot + safe-apply 0/1/2 (repoint + 2 grant destroys); invoke
  -> complete manifest (10 artifacts) + 25 EBS snaps on the dedicated role; comp-manifest-check clean.
- logs-read: safe-apply 1-add then 1-change (DescribeLogGroups->Resource=*); IAM-sim all 4 allowed.
- All HALTGT clear; all targeted 0-diff re-plans = No changes.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-iam service | infrastructure-daily-snapshot; opal-infrastructure-monitor | PASS | enumerated boto3 ops -> root-cause + Phase-1 |
| comp-iam gaps | after each iam.tf change (P0c, logs-read) | PASS | "No MISSING-permission gaps" each time |
| comp-blast | opal-infrastructure-monitor; opal-portal-lambda-role | PARTIAL | no graph-edged consumers (role not a node -> used aws list-functions for Phase-1 instead) |
| comp-manifest-check | post-DR2 | PASS | snapshot Lambda no longer console-orphan (rc=0) |
| ds-commit-gate | both Lambda .py edits | PASS | py_compile + ruff (fixed pre-existing F401/F541/E722 + added future-annotations on monitor) |
| (IAM policy simulation) | repeated (aws iam simulate-principal-policy) | PASS | the authoritative perm-verification throughout |

**What worked:** IAM policy-sim + reading the LIVE error (not guessing) root-caused the DR account-less-ARN
bug + every gap; the proven orphan-import pattern (CI-zip->S3->s3_key->import) ran 3x clean; false-clean
discipline (verify the EMITTED report, not rc=0) caught the EBS 2nd bug + the Claude triage's real logs-perm
finding.
**What failed:** comp-blast doesn't node IAM roles (used aws list-functions for the role-consumer Phase-1).
The aws launcher prints a benign "File association not found for .py" on every PowerShell call (cosmetic).
**Gap found:** the AMI step isn't idempotent same-day (date-stamped name -> InvalidAMIName.Duplicate on a
same-day re-run; handled non-fatally; prod daily never collides). git push hangs fabric-wide on GCM
interactive-prompt (workaround surfaced; Andrew root-fixed via GCM refresh).

## MCP traffic
~20 messages handled (COO GO/sync/accept cycle for DR/P0/DR2 + the [STOP] on leg-c-Bedrock + MSTR GCM-resolved).
Significant: COO DR GO 191458Z; COO [STOP] leg-c-Bedrock 203618Z (Andrew ground-truth); Andrew AskUserQuestion
-> leg-c = Anthropic SDK; COO RAVC2-ACCEPT P0 a+b, leg-c, DR2; COO GO P1 + DS-spawn requested.

## Blockers
None. P1 (freshness+drift) is GO'd but GATED on the DS co-assignee spawn (COO->MSTR, in flight) -- a planned
dependency, not a blocker. Checkpointed at a clean boundary per COO's "don't leave P1 half-built" guardrail.

## Next Steps
- [0.7.0_AE_CloudOps~B] P1 (freshness + drift report sections) with [0.4.0_DS_ClientPlatform] co-assignee:
  (a) generalize the leg-b §2 served-freshness into a per-pipeline Freshness section (DS wires comp-freshness
  /pipescript; AE renders+thresholds); (b) DRIFT section (stale-architecture detection; must NOT flag the 2
  now-in-TF Lambdas). Land increment-by-increment, RAVC2 each.
- [event-driven] 06-17 ~07:00Z: verify the scheduled snapshot run produces a clean complete restore point +
  the EBS skip-AMI'd logic exercises (fresh date, no name collision). 13:00Z: the report emits the corrected
  P0 output (standing confirmation; NO ad-hoc re-invoke).
- [follow-up, opportunistic] AMI-name dedup/suffix for same-day idempotency (low priority).
