# Deploy Completion Record
**Date opened:** 2026-09-12T11:49:37.940360+00:00
**Status:** OPEN
**Deploy:** MDPF_GLOBAL.TO-IAM1 amendment 1: 11 enumerated prefix grants on mdpf-daily-runner-ec2-role (8 source reads + 3 firm destination writes), prefix-CONDITIONED ListBucket, never bucket-wide
**Authored by:** 0.7.0_AE_CloudOps~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | comp-schedule --cursor START re-run owed BEFORE apply (prior run PARTIAL_OR_BLIND) | ANSWER-STATE line + whether any ARMED gate names this role or its prefixes | comp-schedule --budget 1500: WITHIN BUDGET, scanned 5 of 5 carriers (used 102.593s), REACHED-DENOMINATORS C1=138 C2=7 C3=12 C4=20 C5=335, rc=0 COMPLETE VIEW -- the first non-PREFIX run of this tool on record; the face's only prior run was PARTIAL_OR_BLIND with C2-C5 NOT-SCANNED and reported 7 armed gates, the complete view reports 26, so the partial understated by 19. GATES ARMED 26, and ZERO of them name this order's surface: case-insensitive counts over the complete output are mdpf-daily-runner=0, mdpf-runner-scoped=0, 49financial=0, opal-data-cot=0, investor-reporting=0, api_dims=0, against a positive control of owner==26 proving the grep reads this file. ABSENCE OF A SCHEDULE GATE ON THIS ROLE IS THEREFORE ESTABLISHED rather than inherited. METHOD NOTE: my first attempt grepped the 27-byte task-log instead of the redirect target and returned a meaningless 0 -- a wrong-OBJECT read; caught by measuring the file size before believing it. | CLOSED 20260912T115744Z |
| L2 | git | CLOUD commit of iam.tf + locals | commit hash, author 0.7.0_AE_CloudOps~C |  | OPEN |
| L3 | activation | safe-apply -target=aws_iam_role_policy.mdpf_runner | apply summary showing 0 destroyed + 0-diff re-plan |  | OPEN |
| L4 | verify | applied truth via aws iam get-role-policy | the new Sids present in the LIVE document with its statement count |  | OPEN |
| L5 | verify | IAM1-AC4 host-side sweep RE-RUN (the only arm reaching EXERCISED) | SSM command id + SOURCE/DESTINATION tallies with denominators and the positive control still firing |  | OPEN |
| L6 | verify | IAM1-AC5 re-designed negative control that FAILS if the grant is wider than its enumeration | per-control verdicts, ISOLATED invocations, one --resource-arns each, with a separate admin positive control |  | OPEN |

## Log

- 20260912T114937Z OPENED by 0.7.0_AE_CloudOps~C with 6 leg(s)
- 20260912T115744Z LEG L1 closed: comp-schedule --budget 1500: WITHIN BUDGET, scanned 5 of 5 carriers (used 102.593s), REACHED-DENOMINATORS C1=138 C2=7 C3
