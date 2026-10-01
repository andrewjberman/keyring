# Deploy Completion Record
**Date opened:** 2026-10-01T01:10:17.094293+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T012125Z
**Deploy:** NFRA_MCPMSP r2: Opal-internal reader role (no Deny). Blast radius: aws_iam_role.int_reader, aws_iam_role_policy.int_reader, aws_iam_role_policy.gw_assume_int_reader (one role, its policy, one AssumeRole policy on opal-gateway-role). Rollback: terraform destroy -target of exactly those three.
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted safe-apply of the three internal-reader addresses | plan and apply lines | safe-apply targeted (HALT-GATE passed, zero STOP-class lines): Plan: 3 to add, 0 to change, 0 to destroy; Apply complete! Resources: 3 added, 0 changed, 0 destroyed. role arn:aws:iam::313476888478:role/gateway-global-internal-reader-role; gw_firm_deny not targeted | CLOSED 20261001T012124Z |
| L2 | verify | simulate role + gateway AssumeRole (e1a.AC2) and Deny-absent control (e1a.AC3) | AC2+AC3 lines | e1a.AC2: firm-key=allowed global-key=allowed; gateway AssumeRole=allowed (PASS); e1a.AC3: gateway firm-key GetObject=allowed; gateway-firm-deny-policy present=0 (PASS) | CLOSED 20261001T012125Z |

## Log

- 20261001T011017Z OPENED by 0.9.0_WK_NFRA_MCPMSP~1 with 2 leg(s)
- 20261001T012124Z LEG L1 closed: safe-apply targeted (HALT-GATE passed, zero STOP-class lines): Plan: 3 to add, 0 to change, 0 to destroy; Apply complete
- 20261001T012125Z LEG L2 closed: e1a.AC2: firm-key=allowed global-key=allowed; gateway AssumeRole=allowed (PASS); e1a.AC3: gateway firm-key GetObject=all
- 20261001T012125Z CLOSED -- all 2 legs proven
