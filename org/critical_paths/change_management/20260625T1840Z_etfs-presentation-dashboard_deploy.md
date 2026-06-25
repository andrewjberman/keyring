# Deploy-Completion Ledger -- ETFS presentation: etf-ownership-dashboard Lambda

**Opened:** 2026-06-25T18:40Z | **Agent:** 0.5.0_AE_OpalETL | **Authority:** COO deploy handoff (183003Z)
**Status:** CLOSED -- CORE COMPLETE + live-verified 2026-06-25T18:50Z (tag shared-infra-v1.32.0). Push = 0.7.0-SES fast-follow (tracked, not stranded).
**Change:** Deploy DE's ETFS presentation-producer as a Lambda (`etf-ownership-dashboard`, shared-infra) + internal reader-IAM (read opal-data-etfs daily/monthly/config + WRITE platinum/* only; ZERO firm-bucket grants) + daily schedule. Internal-only (CVO certs scope). PUSH (SES) = inert until 0.7.0 provisions the identity (no stranded leg).

## Plan
1. [x] Lambda built (handler + vendored DE compute) + ds-gate PASS + local handler test (grand_total $593.73M, push inert-clean).
2. [x] Reader-IAM + Lambda + schedule TF (shared-infra/etfs-presentation.tf) + source-map entry.
3. [x] OPEN this ledger.
4. [ ] Commit code+TF+source-map; build-and-upload artifact.
5. [ ] plan (verify ADD-only, targeted) -> safe-apply (HALTGT) -> apply.
6. [ ] 0-diff plan; LIVE-verify deployed-role write to platinum/ (real invoke).
7. [ ] CLOSE ledger; tag + push --follow-tags.
8. [ ] CVO internal-only scope close-gate (post-deploy cert).
9. [ ] FAST-FOLLOW (0.7.0-gated, NOT this ledger): SES identity (noreply@opalinvest.dev) + recipient-list (Andrew/COO) + the ses:SendEmail Sid + SES_SENDER/SES_RECIPIENTS env -> push activates.

## Rollback
Net-new resources (role + lambda + schedule); `terraform destroy -target` them, no existing dependency. The DE compute + the producers/slices are independent. Push is inert so nothing half-sent.

## Log
- 18:40Z opened. Lambda built+tested, TF authored. Committing + building next.
- 18:44Z committed code+TF+source-map; build-and-upload (pipeline=shared-infra -> artifact shared-infra/etf-ownership-dashboard.zip; TF artifact_key fixed etfs-pipeline/->shared-infra/ after a 404, re-planned clean).
- 18:48Z plan 9-add/0-change/0-destroy -> safe-apply (HALTGT pass) Apply complete 9 added -> 0-diff "No changes".
- 18:48Z LIVE-verified: deployed-Lambda invoke status:ok wrote platinum/etf_ownership_dashboard.json grand_total $593.73M/3 partners (==local test). comp-freshness PASS. Live get-role-policy: read opal-data-etfs daily/monthly/config + WRITE platinum/* + scoped List; ZERO firm-bucket grants (internal-only, NEVER#1 intact). comp-iam: PutObject GRANTED.
- 18:50Z record-deploy (5e23e9dec; changelog mislabeled v1.1.0 cosmetic) + tag shared-infra-v1.32.0 + push. CLOSED.
- FAST-FOLLOW (0.7.0-gated): SES identity noreply@opalinvest.dev + recipient-list (Andrew/COO) + ses:SendEmail Sid + SES_SENDER/SES_RECIPIENTS env -> push activates. CVO internal-scope close-gate pending.
