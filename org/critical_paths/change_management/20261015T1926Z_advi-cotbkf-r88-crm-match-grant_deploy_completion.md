# Deploy Completion Record
**Date opened:** 2026-10-15T19:26:28.809905+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T195157Z
**Deploy:** ADVI_COTBKF CB-cj-1 (round 88): targeted apply of ONE builder-named role (s3:GetObject on the ONE CRM key) + its ARN in lgic_crm_readers, under the signed pair; withdrawn the same UTC day by CB-cj-3
**Authored by:** 0.7.0_AE_CloudOps~CB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | targeted plan saved outside repo: role + policy CREATED, aws_s3_bucket_policy.lgic_firm UPDATED in place (read-deny readers only), nothing else; check_restricted_prefix.py before | plan JSON read, count line, check output | carved targeted plan saved C:/dev/_cotbkf_private_evidence_20261015/r88/cj1_carved.tfplan: Plan: 2 to add, 1 to change, 0 to destroy; role+policy created, cottonwood bucket policy updated in place (role ARN in READ deny readers only), inflection no change; exemptions.json held at 89beb84dd9^ worktree-only; check_restricted_prefix.py before = check_before.txt (script aborts on inflection statement count, pre-existing) | CLOSED 20261015T194849Z |
| L2 | git | the .tf change committed in own worktree, landed on box/dell1 via safe-merge.sh | apply commit hash | e128e60b43 on box/dell1 (LOCAL, push state unread); .tf blob 89f8f132b9 equals worktree blob; lane granted b7c6312278 | CLOSED 20261015T194849Z |
| L3 | activation | safe-apply.sh scoped to the three addresses (WORLD act) | apply summary line | safe-apply rc=0 19:49:05-19:49:30Z from saved carved plan: Apply complete! Resources: 2 added, 1 changed, 0 destroyed. (C:/dev/_cotbkf_private_evidence_20261015/r88/cj1_apply.txt) | CLOSED 20261015T195144Z |
| L4 | verify | simulator (key allowed; other key, list, put denied) + live read-back of role, inline policy, bucket policy; check_restricted_prefix.py after | read outputs | live read-back: get-role CreateDate 2026-10-15T19:49:31Z, trust one principal cloudops-dell1-agent-user, max session 3600; inline policy CrmMatchGetOneKey s3:GetObject on the one key; bucket policy READ deny readers gain the role, LIST deny and WRITE deny unchanged; simulate-principal-policy with live bucket policy: role key allowed, other key implicitDeny, list implicitDeny, put explicitDeny, agent user key explicitDeny; targeted re-plan No changes; check_restricted_prefix.py aborts before and after on inflection statement count (pre-existing script defect) | CLOSED 20261015T195144Z |

## Log

- 20261015T192628Z OPENED by 0.7.0_AE_CloudOps~CB1 with 4 leg(s)
- 20261015T193901Z HELD-PRE-APPLY gate=external/COO C1 ruling on unapplied TCKT_VNEXT FWD-10 opal-ticket-api-role exemption (89b
- 20261015T194849Z HOLD RELEASED -> OPEN
- 20261015T194849Z LEG L1 closed: carved targeted plan saved C:/dev/_cotbkf_private_evidence_20261015/r88/cj1_carved.tfplan: Plan: 2 to add, 1 to change, 
- 20261015T194849Z LEG L2 closed: e128e60b43 on box/dell1 (LOCAL, push state unread); .tf blob 89f8f132b9 equals worktree blob; lane granted b7c6312278
- 20261015T195144Z LEG L3 closed: safe-apply rc=0 19:49:05-19:49:30Z from saved carved plan: Apply complete! Resources: 2 added, 1 changed, 0 destroyed. (
- 20261015T195144Z LEG L4 closed: live read-back: get-role CreateDate 2026-10-15T19:49:31Z, trust one principal cloudops-dell1-agent-user, max session 360
- 20261015T195157Z CLOSED -- all 4 legs proven

## Rollback, deadline, principals (TO-CB-cj-1 step 1)

- **ROLLBACK:** `CB-cj-3` withdraws the grant: destroy the role and its inline policy, remove the role's ARN from `lgic_crm_readers`, re-plan reads no changes. Targeted destroy of the same three addresses; nothing the job writes needs undoing.
- **DEADLINE:** 23:59Z of 2026-10-15 (2026-10-15T23:59:00Z). The withdrawal is absolute (CTO C2) and runs as the job's next act; 23:59Z is the backstop.
- **PRINCIPALS that can reach the CRM key after the apply:** (1) the console user `Andrew_Berman_Console` (reader list, unchanged); (2) the break-glass role `cloudops-cot-restricted-breakglass-role` (reader list and writer list, unchanged; trust admits only the console user); (3) the NEW role (reader list; its own allow is GetObject on the one key only; trust admits the agents' shell user on this box, `cloudops-dell1-agent-user`). The shell user itself stays refused on the key.

## CB1 notes (0.7.0_AE_CloudOps~CB1, 2026-10-15 19:5xZ)

- CARVE (TO-CB-cj-1 AMENDMENT 1, CTO ruling amendment 6): plan and apply ran from worktree C:/dev/wk-cb1-r88 with infra/logic/registry/exemptions.json held at 89beb84dd9^ (worktree only, never committed). Live state carries NO TCKT_VNEXT exemption exactly as before; its own apply adds it later.
- Lane: the .tf commit e128e60b43 landed under the CTO's lane grant b7c6312278; NO author override was used.
- Principals that can reach the key after the apply (as at open): console user Andrew_Berman_Console, break-glass role, and cloudops-cot-crm-match-role (READ deny readers only; LIST and WRITE denies unchanged).
- ROLLBACK stands: CB-cj-3 (carved withdrawal per its AMENDMENT 1). DEADLINE 2026-10-15T23:59Z.
