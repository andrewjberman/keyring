# Deploy Completion Record
**Date opened:** 2026-10-15T16:26:10.861291+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-r-2: ONE added inline policy (s3:GetObject on opal-data-portal-v2/platinum/mdpf/*) on opal-assets-mdpf-egress-publisher-role by targeted safe-apply, ONE publisher run, unchanged branch proof (TO ADHOC.canon-r10-publisher-latest-read-deploy, GO msg 6066, pin 3df2f0851a, risk WORLD)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions 1a-1f: GO+halves, pin ancestry with control, checks 5/4/5, clean pre-plan, sentinel union, gap rule | printed reads |  | OPEN |
| L1 | verify | before print: role inline policies, comp-iam simulate probes with context and control, latest.json head, 22 served keys VersionIds | before_print files |  | OPEN |
| L2 | activation | targeted saved plan Plan: 1 to add 0 to change 0 to destroy, then safe-apply apply of the saved plan on aws_iam_role_policy.mdpf_egress_publisher_live_serve_read | Apply complete 1 added |  | OPEN |
| L3 | verify | after print: four inline policies, three byte-equal, probes flip DENIED to ALLOWED for latest.json and served keys, others stay DENIED control-proven, Put unchanged | after_print files |  | OPEN |
| L4 | verify | ONE publisher hand-run with the schedule input, published=0 unchanged=18 failed=0, prior_pointer_note null, 22 of 22 served VersionIds equal | run summary + manifest |  | OPEN |
| L5 | verify | ledger check, reported to 2.0.0_SA_COO~D1 | deploy_ledger check |  | OPEN |

## Log

- 20261015T162610Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)
