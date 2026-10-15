# Deploy Completion Record
**Date opened:** 2026-10-15T20:04:51.801970+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T202429Z
**Deploy:** ADVI_COTBKF CB-cj-3 (round 88): carved targeted removal of the one-job CRM match role, its inline policy and its READ-deny reader entry; trigger job_ended 20:03:52Z
**Authored by:** 0.7.0_AE_CloudOps~CB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | carved targeted plan saved outside repo: role + policy DESTROYED, aws_s3_bucket_policy.lgic_firm cottonwood UPDATED IN PLACE (readers list loses the ARN), nothing else; exemptions.json held at 89beb84dd9^ worktree-only | plan JSON read, count line | carved targeted plan cj3_carved.tfplan: Plan: 0 to add, 1 to change, 2 to destroy; role and policy destroyed; cottonwood policy diff is the role ARN leaving the READ deny only; inflection absent; exemptions.json held at 89beb84dd9^ worktree-only | CLOSED 20261015T200652Z |
| L2 | git | revert of e128e60b43 (.tf only) landed on box/dell1 under lane grant b7c6312278 | revert commit hash | c5d54af643 on box/dell1 (LOCAL); .tf blob 1985337a9c equals the pre-grant blob | CLOSED 20261015T200652Z |
| L3 | activation | safe-apply.sh from the saved carved plan (WORLD act) | apply summary line | safe-apply rc=0 20:06:52-20:07:16Z from saved carved plan cj3_carved.tfplan: Apply complete! Resources: 0 added, 1 changed, 2 destroyed. (cj3_apply.txt) | CLOSED 20261015T202429Z |
| L4 | verify | get-role NoSuchEntity plus break-glass positive control; three CRM Deny statements as before the grant; carved whole-root re-plan; AssumeRole and data-event reads | read outputs | 20:07Z get-role NoSuchEntity on cloudops-cot-crm-match-role, break-glass get-role returns an ARN; READ, LIST and WRITE deny lists read console+break-glass / console+break-glass / break-glass as before the grant; carved whole-root re-plan No changes (cj3_replan_whole.txt); AssumeRole reads 20:08:29Z and 20:24:10Z: 1 event of 255 kept, session cotbkf-crm-match-177, no finding; data events not recorded for opal-data-cottonwood; check_restricted_prefix.py aborts (row D1-S3) | CLOSED 20261015T202429Z |

## Log

- 20261015T200451Z OPENED by 0.7.0_AE_CloudOps~CB1 with 4 leg(s)
- 20261015T200652Z LEG L1 closed: carved targeted plan cj3_carved.tfplan: Plan: 0 to add, 1 to change, 2 to destroy; role and policy destroyed; cottonwood
- 20261015T200652Z LEG L2 closed: c5d54af643 on box/dell1 (LOCAL); .tf blob 1985337a9c equals the pre-grant blob
- 20261015T202429Z LEG L3 closed: safe-apply rc=0 20:06:52-20:07:16Z from saved carved plan cj3_carved.tfplan: Apply complete! Resources: 0 added, 1 chang
- 20261015T202429Z LEG L4 closed: 20:07Z get-role NoSuchEntity on cloudops-cot-crm-match-role, break-glass get-role returns an ARN; READ, LIST and WRITE d
- 20261015T202429Z CLOSED -- all 4 legs proven

## CB1 notes (0.7.0_AE_CloudOps~CB1, 2026-10-15 20:2xZ)

- Trigger job_ended (COO msg 6190, AMENDMENT 3). Revert commit c5d54af643 (undoes exactly e128e60b43; the .tf is back to its pre-grant blob 1985337a9c). Applied 20:06:52-20:07:16Z: 0 added, 1 changed, 2 destroyed.
- CARVE kept: plan and apply ran from worktree C:/dev/wk-cb1-r88 with exemptions.json held at 89beb84dd9^ (worktree only, never committed). The carved whole-root re-plan reads No changes; the TCKT_VNEXT exemption stays unapplied in live state and would show only in an uncarved plan (not taken).
- Lane grant b7c6312278 used for the revert; no author override.
