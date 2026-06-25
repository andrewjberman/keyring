# Deploy Completion Record
**Date opened:** 2026-06-25T21:32:27.162916+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T213329Z
**Deploy:** cot-exporter role: OTP-relay + kimi grants for cot BD auto-auth
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| cot-iam | verify | cot-exporter role has otp-relay Get/Put + kimi Get, firm-sep | true | Applied in-place (cot-exporter-policy). comp-iam live: cot-exporter-ec2-role now has GetSecretValue blackdiamond/cot/credentials-*+session-*+otp-relay-* (Get/Put on session+otp-relay), GetSecretValue astn/kimi/api-key-*; cross-firm Deny on opal-data-bd+opal-data-inf INTACT; ZERO blackdiamond/49f/* (firm-sep). CVO certs cot-scoped. | CLOSED 20260625T213329Z |

## Log

- 20260625T213227Z OPENED by 0.7.0_AE_CloudOps with 1 leg(s)
- 20260625T213329Z LEG cot-iam closed: Applied in-place (cot-exporter-policy). comp-iam live: cot-exporter-ec2-role now has GetSecretValue blackdiamond/cot/cre
- 20260625T213329Z CLOSED -- all 1 legs proven
