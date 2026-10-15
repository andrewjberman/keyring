# Deploy Completion Record
**Date opened:** 2026-10-15T18:42:14.437727+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-600: ONE new resource aws_iam_role_policy.inf_gold_layer_scope_feed (scope-account-feed-assets-put) on inf-gold-layer-ec2-role, root infra/aws/terraform/inf-pipeline, packet blob cea5395ee7; rollback = the one-resource destroy (plan 0/0/1)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates: packet blob, both halves, ledgers and markers naming the root or role, address() prefixes equal the HCL ARNs, live inline policy names | the printed reads | packet blob cea5395ee7 equal, both halves GIVEN/SIGNED; ledgers read 1949 and markers 39 worktrees 665 files: none OPEN names the root or role (one HELD-SOVEREIGN-GATED ledger, advi-firmbkts-fb-l-5, names inf-pipeline for its schedule resources, apply legs proven, named not a stop); address() prefixes equal the HCL ARNs; role carries 12 inline policies, none named scope-account-feed-assets-put | CLOSED 20261015T184644Z |
| L2 | git | iam.tf gains the resource verbatim, committed on box/dell2 | commit hash | no edit by this seat: iam.tf blob 419a7760bd at HEAD equals the blob at 3c4d117b57 (IB-pr-603, merged); addendum blob f22b13a991 equal, COO half GIVEN @83add5e3df, CTO half SIGNED @672b1fea08; policy name orion-inf-scope-account-feed-policy absent from the role's 12 inline policies | CLOSED 20261015T194157Z |
| L3 | verify | plan reads 1 to add, 0 to change, 0 to destroy at the one address only | plan line | validate Success; saved plan 19:41Z: Plan: 1 to add, 0 to change, 0 to destroy, address aws_iam_role_policy.inf_gold_layer_scope_feed only; rendered ARNs opal-data-assets/orion/inflection/{bronze,silver}/scope_account_returns/* equal address() output; 2 statements, no Delete, no KMS | CLOSED 20261015T194157Z |
| L4 | activation | ONE safe-apply of the saved plan, re-plan No changes, get-role-policy two statements no Delete no KMS, policy sha256 | apply line and read-back | ONE safe-apply of the saved plan 19:42:19Z-19:44:25Z rc 0: 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.'; re-plan No changes rc 0; get-role-policy orion-inf-scope-account-feed-policy: 2 statements, actions GetObject ListBucket PutObject, no Delete, no kms, policy sha256 4b023e123d06.. | CLOSED 20261015T194539Z |
| L5 | verify | simulation: 4 allowed arms, 4 denied arms, 2 controls | the 10 decisions | simulation on inf-gold-layer-ec2-role: ALLOWED put bronze feed key, put silver feed key, get feed key, list with prefix orion/inflection/silver/scope_account_returns/; implicitDeny put fact_positions sibling key, delete feed key, put unrelated bucket, list sibling prefix; controls opal-data-inf put allowed, unrelated bucket denied | CLOSED 20261015T194540Z |
| L6 | verify | feed's S3Ops.exists run on the runner through SSM read only against a known-absent date=1900-01-01 silver key reads ABSENT | the answer | ONE start of i-0ed5afded2ebd4ed4 at 19:53:40Z by the RUNBOOK procedure (CTO ADDENDUM 2, msg 8597), SSM Online 19:54:00Z, ONE SSM command 15e9f811 Success 19:54:06Z (feed's own S3Ops.exists, read only): bronze ABSENT (raw HEAD 404:404, exact-prefix listing 0 keys status 200), silver ABSENT (raw HEAD 404:404, listing 0 keys status 200); runner NOT stopped by 20:25Z (31 min after the command ended): recorded, not stopped by this seat; the stop is Andrew's act | CLOSED 20261015T202554Z |

## Log

- 20261015T184214Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261015T184644Z LEG L1 closed: packet blob cea5395ee7 equal, both halves GIVEN/SIGNED; ledgers read 1949 and markers 39 worktrees 665 files: none OPEN 
- 20261015T194157Z LEG L2 closed: no edit by this seat: iam.tf blob 419a7760bd at HEAD equals the blob at 3c4d117b57 (IB-pr-603, merged); addendum blob f2
- 20261015T194157Z LEG L3 closed: validate Success; saved plan 19:41Z: Plan: 1 to add, 0 to change, 0 to destroy, address aws_iam_role_policy.inf_gold_lay
- 20261015T194539Z LEG L4 closed: ONE safe-apply of the saved plan 19:42:19Z-19:44:25Z rc 0: 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.'
- 20261015T194540Z LEG L5 closed: simulation on inf-gold-layer-ec2-role: ALLOWED put bronze feed key, put silver feed key, get feed key, list with prefix 
- 20261015T202554Z LEG L6 closed: ONE start of i-0ed5afded2ebd4ed4 at 19:53:40Z by the RUNBOOK procedure (CTO ADDENDUM 2, msg 8597), SSM Online 19:54:00Z,
