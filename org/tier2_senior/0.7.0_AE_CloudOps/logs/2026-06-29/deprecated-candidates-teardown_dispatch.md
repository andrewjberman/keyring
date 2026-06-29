# Deprecated-Candidates Teardown — CVO dispatch a47d169ef (Andrew-direct)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Agent:** 0.7.0_AE_CloudOps~A | **Date:** 2026-06-29 | **Window:** ~1955Z->2030Z
**For:** 3.0.0_SA_CVO (dispatch owner) · cc 2.0.0_SA_COO, 1.0.0_SA_CTO

## Summary
Executed the infra/TF + Lambda lane of CVO's Andrew-direct pre-monster-push teardown
dispatch (scan a47d169ef). 3 teardowns DONE + ledgered; 2 candidates HELD because live
cross-checks REFUTED a clean teardown (the do-er catching what the single-axis scan missed).

## Done (each via deploy-completion ledger; reversible-first)
1. **TIER-1 dead scaffold** — `c4dceebf7`. git rm `infra/aws/multi-account/terraform/`
   (0 tfstate/0 .terraform confirmed; no live .tf sources its modules; SOURCE of 6/10 comp-dups
   TF collisions) + `infra/aws/lambda/deprecated/` + `bd-pipeline/bd-price-update/lambda_function_v1_backup.py`.
   60 files, history-preserved. Ledger `20260629T2002Z_deprecated-teardown-tier1-files` (L2=CVO co-verify OPEN).
2. **bd-time-machine torn down** — `1ecaa1389`, tag `bd-v2.40.0`. CW Invocations 90d = 0
   datapoints + Andrew-confirmed dead. safe-apply = 0add/0change/**6 destroy** (lambda + log-group +
   role + 2 policies + attachment); 0-diff re-plan clean; get-function->ResourceNotFound;
   get-role->NoSuchEntity; artifact zip `s3://opal-313476888478-lambda-artifacts/bd-pipeline/bd-time-machine.zip`
   removed (0-residual). Verified the trigger `pipeline-complete.json->bd-portal-publisher` is
   owned by `bd-pipeline/s3-notifications.tf` (PortalPublisherTrigger), UNAFFECTED. Ledger CLOSED.
3. **opal_users_v2 AUTH-DDB twin de-duped** — `1f6fa344d`. Mechanism-grounded: shared-infra
   config carries `point_in_time_recovery=enabled` matching LIVE PITR=ENABLED (deliberate import
   CDRS_TFIMPT.006); the portal-auth twin LACKED the PITR block -> a portal-auth apply would have
   DISABLED PITR on the auth table. De-dup = `terraform state rm aws_dynamodb_table.opal_users_v2`
   from portal-auth (**LIVE TABLE NEVER TOUCHED**) + removed the config block; portal-auth/iam.tf
   hardcoded-ARN grants kept. portal-auth plan="No changes"; shared-infra opal_users_v2 plan="No
   changes". NEVER-WIDEN honored. Ledger CLOSED.

## Held — with findings (refuted by live check)
4. **SNS x3 — 0 deletions.** All 0-subscriber but with ACTIVE PUBLISHERS: astn-wsjft-alerts <-
   CW alarm `astn-wsjft-orchestrator-errors` AlarmAction; trade-pipeline-ses-bounces/-complaints
   <- SES config-set `trade-pipeline-notifications` event destinations (Enabled=true; CVO's SES
   caveat TRIGGERED). Deleting any dangles an alarm action / errors SES. Filed as a MONITORING-GAP
   (alerts publish into the void) — separate operational decision, not a teardown.
5. **bd-exporter twin — held.** Role ownership VALIDATED (bd-pipeline owns the live
   bd_exporter role+instance_profile+9 policies+ssm; `ec2/bd-exporter/terraform/main.tf` = 0-state
   dup). But `bd-pipeline/ec2.tf:103,143` read the LIVE uploader-EC2 user_data via
   `file("../../ec2/bd-exporter/terraform/scripts/uploader_user_data.sh")` — wholesale dir removal
   breaks bd-pipeline. Needs a scoped relocate-script + repoint follow-up (its own RAVC).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-blast bd-time-machine | pre-teardown blast | PARTIAL — flagged pipeline-complete.json edge; ran the source+freshness follow-up that cleared it |
| comp-freshness artifact | s3://opal-data-bd/gold/pipeline-complete.json | FAIL (83d stale) — surfaced the side-finding (not teardown-caused) |
| pipescript --resource | gold/pipeline-complete.json | PASS — 3 threads; confirmed bd-time-machine is not the live producer |
| comp-which | routed bd-time-machine + pipeline-complete + SES intents | PASS — routed to comp-blast / comp-pipescript io |

What worked: comp-blast's "treat producer as orphan only after checking dynamic consumers" warning
drove the s3-notifications.tf ownership check that confirmed the trigger survives teardown.
What failed: none. Gap: none new.

## Blockers
None. The 2 held items are not blockers — each routed to CVO/CTO with a concrete grounded finding
+ an offer to own the follow-up.

## Current State
- Branch CLOUD at/after `1f6fa344d` (concurrent agents advanced HEAD past it; my commits + tag
  bd-v2.40.0 pushed). bd-pipeline TF: bd-time-machine fully removed, 0-diff. portal-auth TF:
  opal_users_v2 block + state entry removed; shared-infra is sole canonical owner. lambda-source-map.json:
  bd-time-machine entry removed.
- 3 ledgers in org/critical_paths/change_management/ (2 CLOSED; tier1-files L2 open pending CVO co-verify).
- Reports delivered: CVO (20260629T202911Z), COO (202934Z), CTO (202943Z).

## Next Steps
- [3.0.0_SA_CVO] run the independent 0-residual co-verify on the 3 done teardowns (closes tier1-files L2);
  send the explicit "function teardown candidates" list for the CW last-run gate; rule on the SNS
  monitoring-gap + the multi-account non-terraform remainder sweep.
- [1.0.0_SA_CTO] decide whether/when to do the bd-exporter script-relocate (I can own it).
- [2.0.0_SA_COO] operational call on the SNS 0-subscriber alert paths + the bd gold pipeline 83d-stale
  pipeline-complete.json.
