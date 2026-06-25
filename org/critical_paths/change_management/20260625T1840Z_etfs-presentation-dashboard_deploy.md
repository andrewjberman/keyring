# Deploy-Completion Ledger -- ETFS presentation: etf-ownership-dashboard Lambda

**Opened:** 2026-06-25T18:40Z | **Agent:** 0.5.0_AE_OpalETL | **Authority:** COO deploy handoff (183003Z)
**Status:** OPEN -> (in progress)
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
