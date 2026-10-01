# Deploy Completion Record
**Date opened:** 2026-10-01T14:21:35.811728+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T143451Z
**Deploy:** NFRA_MCPMSP r2 MS-dn-1: gateway firm-key Deny (TF act #3). Blast radius: aws_iam_role_policy.gw_firm_deny only (one Deny s3:GetObject inline policy on opal-gateway-role, three platinum/mdpf/<firm>/* prefixes of opal-data-portal-v2). Never-widen pair: COO @1fde6055b7 + CTO @ae72f3bcbb. Rollback: terraform destroy -target=aws_iam_role_policy.gw_firm_deny
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted safe-apply of aws_iam_role_policy.gw_firm_deny | plan and apply lines | safe-apply on a saved targeted plan (HALT-GATE passed, no STOP-class lines): Plan: 1 to add, 0 to change, 0 to destroy; Apply complete! Resources: 1 added, 0 changed, 0 destroyed. aws_iam_role_policy.gw_firm_deny = Deny s3:GetObject on platinum/mdpf/{49financial,inflection,cottonwood}/* of opal-data-portal-v2 | CLOSED 20261001T143450Z |
| L2 | verify | simulate gateway role on firm and global keys (e1z.AC2) and host-served read-back (e1z.AC3) | AC2+AC3 lines | e1z.AC2: inflection=explicitDeny cottonwood=explicitDeny global=allowed (PASS); e1z.AC3: ssm:3d38142e-67ad-4fe5-a350-f0d040374aa4 Success matched=9 of 9 mismatched=[] (PASS); AC5 after: 10 of 10 sha256 equal to before (ssm:550b4315-efd0-4601-af12-3d4f8f224b68) | CLOSED 20261001T143450Z |

## Log

- 20261001T142135Z OPENED by 0.9.0_WK_NFRA_MCPMSP~5 with 2 leg(s)
- 20261001T143450Z LEG L1 closed: safe-apply on a saved targeted plan (HALT-GATE passed, no STOP-class lines): Plan: 1 to add, 0 to change, 0 to destroy; 
- 20261001T143450Z LEG L2 closed: e1z.AC2: inflection=explicitDeny cottonwood=explicitDeny global=allowed (PASS); e1z.AC3: ssm:3d38142e-67ad-4fe5-a350-f0d
- 20261001T143451Z CLOSED -- all 2 legs proven
