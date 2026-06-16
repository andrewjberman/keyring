# Deploy-completion ledger -- NFRA_INFRPT.P0 (a+b) opal-infrastructure-monitor

**class:** deploy_completion
**status:** OPEN (deploy-start; orphan-import + a/b code deploy via safe-apply pending)
**opened:** 20260616T2110Z
**closed:** --
**owner:** 0.7.0_AE_CloudOps~B
**project / TO:** NFRA_INFRPT / P0 legs a+b (stop the misleading report output)
**authorization:** COO GO 205358Z (SHIP a+b now, don't hold for leg-c) + 210901Z (proceed as planned). Andrew-direct project; CTO-ruled 201006Z orphan-import approach.
**code commit:** a/b code = 26a950431 (pushed origin f53fc5097). This deploy commit = TF + source-map (below).

## What this deploys
1. **Orphan-import**: bring `opal-infrastructure-monitor` into Terraform (was a console orphan -- source-map
   said "No Terraform resource ... do not use update-function-code"). New `aws_lambda_function.infra_monitor`
   in infra/aws/terraform/shared-infra/infra-monitor.tf (s3-backed, house pattern). Closes the same console-
   orphan drift debt for the report generator that DR2 closes for the snapshot Lambda.
2. **a+b code**: dep-free artifact (lambda_function.py + openai_cost_tracker.py) at
   s3://opal-313476888478-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip
   (content-sha256 HT8mqqkTLsNttUG5Yg9IQmALIl7G5UcG+TniLmy+YZE=, 15679 B).
   - leg a: KILLED §3 AI/OpenAI-call success tracker (the 0/0/100% fake all-green).
   - leg b: §2 SmartX now reads REAL served-artifact freshness (json/portfolios/account-distribution.json
     + aum-metrics.json on opal-data-portal-v2, mtime vs daily cadence -> ok/watch/stale), replacing the
     dead-EC2 + unwritten-exports/ permanent false STALE. Thresholds validated vs the artifact's real daily
     11:30 UTC cadence (incl weekends).
   - §7 openai-cost section (committed ADHC_GPTCST work, never deployed via the broken deploy.sh) lands too
     (boto3-only; resolves that stranded-commit drift).

## NOT in this deploy (held)
- leg-c (§6 triage + §5 security-briefing AI re-home): COO [STOP] 203618Z -- Andrew ground-truthed the firm
  does NOT use Bedrock (ruling falsified). §6/§5 stay gracefully-OFF on the existing OpenAI path UNCHANGED
  (no regression -- already broken). Re-GOes on Andrew's corrected mechanism (likely the anthropic-sdk-deps
  layer pattern); then it's a code edit + small apply here (no second import).
- The EventBridge trigger (infrastructure-monitor-daily, 13:00 UTC) + its lambda permission stay console-
  managed (they work; a later TF-hygiene leg).

## Close criteria
- terraform import aws_lambda_function.infra_monitor + targeted safe-apply (HALTGT clear); 0-diff re-plan.
- CONTROLLED INVOKE verify (false-clean discipline -- the EMITTED report, not rc=0): §3 AI/OpenAI-CALLS
  section ABSENT from email + archived JSON; §2 SmartX reads REAL freshness (NOT the dead-EC2 false-STALE);
  report archives cleanly to opal-data-portal-v2/infrastructure/reports/. §6/§5 unchanged (leg-c held).
- RAVC2 to COO. Finish-in-session.

## Rollback
The function is now TF-managed. Revert = redeploy the prior artifact (S3 versioned) / git revert the TF +
source-map. The orphan-import is non-destructive (importing existing infra). Code change is forward-only
(report-generator logic; reads live state each run; no data re-emit).

## Push note
Git push hangs fabric-wide (GCM interactive-prompt). Use the workaround:
`git -c credential.helper= -c credential.helper='!gh auth git-credential' push origin CLOUD`
