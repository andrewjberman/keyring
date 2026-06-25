# Deploy Completion Record
**Date opened:** 2026-06-25T17:29:00.612768+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T172947Z
**Deploy:** SEV1 egress restore: re-create the auto-deleted email sub on opal-critical-surface-alerts (9 critical alarms incl portal SEV1 + SS4c had 0 deliverable subs)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply re-creates aws_sns_topic_subscription.critical_surface_alerts_email (andrew@opalinvest.com) on opal-critical-surface-alerts -- COO-authorized cross-lane (0.7.0 item2c, buried) | 0-diff plan + live list-subscriptions-by-topic shows the email sub PendingConfirmation | safe-apply 1-add/0-change/0-destroy (re-created the SNS-auto-deleted unconfirmed sub; TF refresh found it gone). 0-diff (No changes) on the targeted resource. Live list-subscriptions-by-topic: email andrew@opalinvest.com = PendingConfirmation present. | CLOSED 20260625T172947Z |
| L2 | verify | live SNS confirms the email sub present (PendingConfirmation); Andrew click-confirm is the human gate (COO surfacing) -> Delivered once confirmed | list-subscriptions-by-topic output | Live SNS verified: email sub PRESENT (PendingConfirmation) on opal-critical-surface-alerts. The TF resource is in + applied -- one Andrew click-confirm from Delivered (the human gate, COO surfacing to Andrew, explicitly outside the deploy). SMS sub retained (undeliverable sandbox) per item2c until email confirms. | CLOSED 20260625T172947Z |

## Log

- 20260625T172900Z OPENED by 0.6.0_AE_PartnerETL with 2 leg(s)
- 20260625T172947Z LEG L1 closed: safe-apply 1-add/0-change/0-destroy (re-created the SNS-auto-deleted unconfirmed sub; TF refresh found it gone). 0-diff 
- 20260625T172947Z LEG L2 closed: Live SNS verified: email sub PRESENT (PendingConfirmation) on opal-critical-surface-alerts. The TF resource is in + appl
- 20260625T172947Z CLOSED -- all 2 legs proven
