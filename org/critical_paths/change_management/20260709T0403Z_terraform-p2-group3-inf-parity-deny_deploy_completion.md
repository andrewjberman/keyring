# Deploy Completion Record
**Date opened:** 2026-07-09T04:03:41.561597+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T040924Z
**Deploy:** NFRA_TERRAFORM-P2 BATCH C group 3: inf-parity cross-firm Deny belt (27 roles, additive) -- dual GO: CTO 035928Z + COO 040050Z
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit + push cross-firm-deny.tf | hash pushed | 7d7cb42c4 pushed to CLOUD (6dc083d3b..7d7cb42c4) | CLOSED 20260709T040356Z |
| L2 | activation | safe-apply(HALTGT) inf-pipeline -- 27 aws_iam_role_policy adds | apply complete 27-add/0-change/0-destroy | safe-apply(HALTGT) passed checkpoint; Apply complete! Resources: 27 added, 0 changed, 0 destroyed (from saved gated plan, commit 7d7cb42c4) | CLOSED 20260709T040515Z |
| L3 | verify | live get-role-policy: Deny LANDED on ALL 27 inf roles (applied truth) | 27/27 cross-firm-bucket-deny present with Sid=DenyCrossFirmBuckets | live get-role-policy swept all 27 inf roles (bug-fixed loop, in-loop count asserted): 27/27 carry inline policy cross-firm-bucket-deny with Sid=DenyCrossFirmBuckets + Effect=Deny + exactly 2 bd ARNs + 2 cot ARNs + ZERO opal-data-inf. missing=none, wrong-scope=none. | CLOSED 20260709T040923Z |
| L4 | verify | DENY-TEST exercised: simulate-principal-policy -- an inf role is ACTUALLY denied s3 on bd/cot | explicitDeny verdict from simulate (behavior, not config-read) | DENY-TEST EXERCISED via aws iam simulate-principal-policy (behavior, not config-read). s3:GetObject+s3:PutObject vs opal-data-bd/probe.txt AND opal-data-cot/probe.txt: explicitDeny on BOTH actions x BOTH buckets for inf-gold-layer-ec2-role, inf-exporter-ec2-role, inf-bronze-runner-ec2-role, inf-eventbridge-ssm-role. explicitDeny (not implicitDeny) proves the BELT is the deciding control -- incl. on inf-eventbridge-ssm-role which has no S3 Allow (implicitDeny -> explicitDeny = the Allow-drift defense working). | CLOSED 20260709T040923Z |
| L5 | verify | INF-OWN-ACCESS-INTACT: simulate inf role vs opal-data-inf | allowed verdict (proves no over-restriction) | INF-OWN-ACCESS-INTACT, exercised. (i) inf-gold-layer-ec2-role s3:GetObject+PutObject on opal-data-inf/gold/probe.json = allowed,allowed; ListBucket opal-data-inf = allowed. (ii) inf-gold-qa-runner-ec2-role on a GENUINELY-allowed ARN: GetObject gold/canonical/* = allowed, PutObject qa/* = allowed (an initial implicitDeny on gold/probe.json was my probe ARN falling outside that role's pre-existing prefix-scoped Allow -- implicit, not explicit, so not belt-caused; ran it down + re-tested). (iii) OVER-RESTRICTION SENTINEL across ALL 27 roles: s3:ListBucket vs arn:aws:s3:::opal-data-inf returned explicitDeny for 0/27 -- the belt over-restricted NO inf role on its own bucket. | CLOSED 20260709T040923Z |

## Log

- 20260709T040341Z OPENED by 0.5.0_AE_OpalETL with 5 leg(s)
- 20260709T040356Z LEG L1 closed: 7d7cb42c4 pushed to CLOUD (6dc083d3b..7d7cb42c4)
- 20260709T040515Z LEG L2 closed: safe-apply(HALTGT) passed checkpoint; Apply complete! Resources: 27 added, 0 changed, 0 destroyed (from saved gated plan
- 20260709T040923Z LEG L3 closed: live get-role-policy swept all 27 inf roles (bug-fixed loop, in-loop count asserted): 27/27 carry inline policy cross-fi
- 20260709T040923Z LEG L4 closed: DENY-TEST EXERCISED via aws iam simulate-principal-policy (behavior, not config-read). s3:GetObject+s3:PutObject vs opal
- 20260709T040923Z LEG L5 closed: INF-OWN-ACCESS-INTACT, exercised. (i) inf-gold-layer-ec2-role s3:GetObject+PutObject on opal-data-inf/gold/probe.json = 
- 20260709T040924Z CLOSED -- all 5 legs proven
