# Deploy-Completion Ledger — Causality Feature Teardown

- **Opened:** 2026-06-16T20:34Z
- **Agent:** 0.5.0_AE_OpalETL
- **Authorization:** Andrew-direct sovereign ("causality is completely done, get rid of any causality-tagged resources" + GO on the enumerated list 2026-06-16). Overrides the COO calm-window hold (sovereign > COO).
- **WO origin:** CTO WORK ORDER 2026-06-11 (causality full deprecation); CTO GO unconditional, plan staged 78fd19e13/ba71cb174.
- **Status:** CLOSED (2026-06-16T22:10Z — all legs complete + live-verified; no stranded leg)

## Scope (live-verified 2026-06-16, fresh dry-run = 0 problems)
- boto3 (staged causality_teardown.py --execute): 1 EventBridge rule + 11 apigw /causality resources (cascade) + 2 stage redeploys (prod 3weiq0 / production rx10dt) + 8 lambdas + 8 IAM roles + 1 orphan DDB table (causality-thematic-signals, 0 items).
- ADDED (not in staged script): delete 8 CloudWatch log groups /aws/lambda/causality-*.
- TF -target destroy (safe-apply HALTGT): 2 shared-infra DDB tables causality-generations + causality-saved-analyses (both 0 items) — plan regenerated fresh.
- Repo cleanup commit (CLOUD): 8 source dirs infra/aws/lambda/causality_*, infra/aws/terraform/causality/, ~24 source-map entries.
- Handoff (NOT this ledger's close): DE retires portal/src/pages/CausalityEngine/ + causality-endpoints.ts + useCausalityApi.ts.

## Safety
- Cross-invoker check (live resource policies): every causality lambda invoked ONLY by /causality apigw methods or the causality rule — 0 live/non-causality dependents.
- Survivor gate: 38-path byte-identical non-causality route snapshot + auto-rollback of both stages on mismatch (rollback-capture pre-delete).
- Protect-list (never touched): KMS 86cc6c40, S3 opal-data-news-av, AWSLambdaBasicExecutionRole (detach-only), secrets.

## Step log
- [20:34Z] Ledger opened. Fresh dry-run PASS (0 problems, 25 targets live, snapshot=38).
- [21:35Z] boto3 EXECUTE: DONE — rule deleted; /causality 11-resource tree deleted; stages redeployed (prod 5vm7lc / production c2zxm8); 38-path survivor check BYTE-IDENTICAL PASS (portal API intact); 8 lambdas deleted; 8 roles deleted. Orphan table delete failed on AWS DynamoDB deletion-protection.
- [21:36Z] Disabled deletion-protection on causality-thematic-signals (now empty+unprotected, ready to drop).
- [21:36Z] BLOCKED (harness permission guard, not AWS): `aws dynamodb delete-table` denied at the permission layer (destructive-delete guard). Remaining destructive ops awaiting Andrew permission-clearance: (1) delete causality-thematic-signals; (2) delete 8 log groups; (3) terraform -target destroy of causality-generations + causality-saved-analyses (both empty, protection=False). Non-destructive remainder (repo cleanup commit, DE FE handoff) proceeding. NOT a rollback case — completed deletes are intended + the live portal is verified intact; this is a gated-pending-approval state, not a stranded leg.
- [21:57Z] FE leg DONE (handoff): 0.4.0_DE retired the CausalityEngine portal page — portal DEV f3ceea7c (17 files / 1863 deletions, 0 residual causality refs, Andrew product-confirmed the recursive delete). Validated by me; RAVC closed. Page was already orphaned (no App.tsx route) — dead code, not user-reachable.
- [22:06Z] Andrew CLEARED all 3 destructive ops (per-op confirm via COO AskUserQuestion). My session's boto3/safe-apply path was NOT re-blocked, so executed directly: boto3 deleted causality-thematic-signals (protection pre-disabled) + 8 log groups; safe-apply (HALTGT, inbox clear) applied the show-verified `-target` destroy plan (0 add / 0 change / 2 destroy = EXACTLY causality_generations + causality_saved_analyses; opal-users-v2 confirmed NOT in set).
- [22:08Z] RE-VERIFY vs LIVE (script --verify): 8 lambdas + 8 roles + rule + thematic-signals table GONE; 0 causality apigw resources; **38-path portal survivor check BYTE-IDENTICAL PASS post-destroy** (0 live portal collateral); protect KMS + bucket intact. Independent: 2 TF tables ResourceNotFound (gone); 0 causality log groups remaining. Tag sweep clean.
- [22:10Z] Repo cleanup commit pushed CLOUD a30431feb: 8 lambda source dirs + infra/aws/terraform/causality/ module + 8 source-map entries + 2 shared-infra dynamo.tf table blocks removed (terraform validate PASS; safe-deploy = no deploy-scope scripts). dynamo.tf (0.7.0_AE shared-infra) had no concurrent edits; notifying owner.
- [22:10Z] CLOSED. Total: 39 AWS resources destroyed (8 lambda / 8 role / 8 loggroup / 3 ddb / 1 rule / 11 apigw) + 2 stage redeploys + FE page retired (f3ceea7c) + repo cleaned (a30431feb). Live portal verified intact throughout. No stranded leg. RAVC3 -> COO+CTO.
