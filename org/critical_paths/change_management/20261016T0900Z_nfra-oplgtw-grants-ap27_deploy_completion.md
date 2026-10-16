# Deploy Completion Record
**Date opened:** 2026-10-16T09:00:48.863500+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T090814Z
**Deploy:** NFRA_OPLGTW TO-OG-ap-27 Phase B: two read-only policies (etfs-gap-read, mdpf-gap-read) on gateway-global-internal-reader-role for four catalog prefixes (2 add, 0 change, 0 destroy), safe-apply targeted, read back and simulated; .tf sha256-16 be09d3dd3aaebdd9, ask 38817328cc91; halves CTO c18e2e007c, COO b5652f6db9, CVO b121849fbe; GO msg 34868
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | apply the two policies then get-role-policy for both on the internal reader | both present on gateway-global-internal-reader-role and equal to the file | safe-apply targeted at the two policies: plan 2 add 0 change 0 destroy, Apply complete 2 added 0 changed 0 destroyed; get-role-policy on gateway-global-internal-reader-role for both: 2 statements each (GetObject on the prefix objects, ListBucket on the bucket under an s3:prefix StringLike confined to the same prefixes), both Allow, shape equal to the file; sha256-16 etfs 26a2516dd78db96a mdpf 66b10f940ba482ae; internal reader inline policies 7 -> 9; neither new name on opal-gateway-role | CLOSED 20261016T090814Z |
| S1 | verify | simulate-principal-policy one resource per call, four prefixes plus negative control and a positive control | GetObject allowed 4 of 4, ListBucket allowed 4 of 4, negative control not allowed 2 of 2 and 2 of 2 | simulate-principal-policy as the internal reader, one resource per call: GetObject on a probe key under each of the 4 prefixes allowed 4 of 4; ListBucket with each prefix as s3:prefix allowed 4 of 4; negative control GetObject on ap27-negative-control/probe in each bucket implicitDeny 2 of 2, ListBucket with s3:prefix ap27-negative-control/ implicitDeny 2 of 2; positive control (caller principal) GetObject and ListBucket on the same out-of-scope key and prefix allowed, each in its own invocation | CLOSED 20261016T090814Z |
| V1 | verify | targeted re-plan of the two policies | No changes | terraform plan -lock=false targeted at aws_iam_role_policy.etfs_gap_read and aws_iam_role_policy.mdpf_gap_read: No changes. Your infrastructure matches the configuration. | CLOSED 20261016T090814Z |

## Log

- 20261016T090048Z OPENED by 0.7.0_AE_CloudOps~ZS with 3 leg(s)
- 20261016T090814Z LEG P1 closed: safe-apply targeted at the two policies: plan 2 add 0 change 0 destroy, Apply complete 2 added 0 changed 0 destroyed; ge
- 20261016T090814Z LEG S1 closed: simulate-principal-policy as the internal reader, one resource per call: GetObject on a probe key under each of the 4 pr
- 20261016T090814Z LEG V1 closed: terraform plan -lock=false targeted at aws_iam_role_policy.etfs_gap_read and aws_iam_role_policy.mdpf_gap_read: No chang
- 20261016T090814Z CLOSED -- all 3 legs proven
