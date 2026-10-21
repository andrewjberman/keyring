# Deploy Completion Record
**Date opened:** 2026-10-20T22:46:15.501217+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T234458Z
**Deploy:** NFRA_SCHWABBF fence rows applied ahead of the 0840 window
**Authored by:** 0.7.0_AE_CloudOps~NFRA2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | shared-infra: the scoped exemption rows on the opal-data-49financial and opal-data-cottonwood bucket policies | get-bucket-policy shows the rows and the principal reads pass | ROWS LANDED, OUTSIDE TERRAFORM by issuer ruling 2.0.0_SA_COO~SB msg 110066 branch 2 (instance-level -target plan still 10 add + 2 change): put-bucket-policy of planned_49f.json and planned_cw.json at 2026-10-20T23:15:42Z (opal-data-49financial, 42->54 statements) and 23:15:46Z (opal-data-cottonwood, 7->14); read-back equals plan after normalization, 0 statements removed, DenyForeignFirmPrincipals only gained ArnNotLike ARNs; targeted plan afterwards: both bucket policies no-op (10 add left = other firms' buckets, not applied); rollback = before_49f.json / before_cw.json via put-bucket-policy. Reads NOT MET BY SEQUENCE (issuer ruling msg 110069): gateway-schwab-catalog-read-role NOT LIVE-TESTABLE (assume-role AccessDenied), simulated explicitDeny by the role's own policy, widening is site Z's reader IAM update; quartz-si2-spike-role pulls PutObject implicitDeny, identity grant is TO-BF-r3 step C; complete explicitDeny by ResourcePolicy (fence works). Evidence: org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA2/r2/ | CLOSED 20261020T234458Z |

## Log

- 20261020T224615Z OPENED by 0.7.0_AE_CloudOps~NFRA2 with 1 leg(s)
- 20261020T234458Z LEG L1 closed: ROWS LANDED, OUTSIDE TERRAFORM by issuer ruling 2.0.0_SA_COO~SB msg 110066 branch 2 (instance-level -target plan still 1
- 20261020T234458Z CLOSED -- all 1 legs proven
