# Deploy Completion Record
**Date opened:** 2026-07-02T21:35:21.901650+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260702T214640Z
**Deploy:** Grant quartz-si2-spike-role s3:GetObject on _ops/canonical-schwab-si2/* (S3->box code-deploy path; least-privilege, never-widen)
**Authored by:** 0.6.2_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit the scoped iam.tf change on CLOUD | hash pushed | commit 21a5c66f9 pushed to CLOUD (scoped iam.tf: SchwabOpsCodeRead GetObject on _ops/canonical-schwab-si2/* only) | CLOSED 20260702T213626Z |
| L2 | verify | CTO sec-gate the least-privilege scope BEFORE apply | CTO RAVC OK | CTO sec-gate APPROVED 214114Z: least-privilege + never-widen + firm-scoped + orthogonal-to-repoint; GO on safe-apply | CLOSED 20260702T214253Z |
| L3 | activation | safe-apply the IAM change (0-add/1-change/0-destroy) | apply complete + 0-diff | safe-apply complete (HALTGT passed): 0-add/1-change/0-destroy; re-plan No changes (0-diff) | CLOSED 20260702T214633Z |
| L4 | verify | LIVE aws iam get-role-policy shows SchwabOpsCodeRead GetObject (Rule 22a applied-layer, not comp-iam DESIRED) | live policy JSON | LIVE aws iam get-role-policy: SchwabOpsCodeRead = s3:GetObject on opal-data-schwab/_ops/canonical-schwab-si2/* ONLY (no raw read); applied-layer verified Rule 22a | CLOSED 20260702T214637Z |

## Log

- 20260702T213521Z OPENED by 0.6.2_AE_PartnerETL with 4 leg(s)
- 20260702T213626Z LEG L1 closed: commit 21a5c66f9 pushed to CLOUD (scoped iam.tf: SchwabOpsCodeRead GetObject on _ops/canonical-schwab-si2/* only)
- 20260702T214253Z LEG L2 closed: CTO sec-gate APPROVED 214114Z: least-privilege + never-widen + firm-scoped + orthogonal-to-repoint; GO on safe-apply
- 20260702T214633Z LEG L3 closed: safe-apply complete (HALTGT passed): 0-add/1-change/0-destroy; re-plan No changes (0-diff)
- 20260702T214637Z LEG L4 closed: LIVE aws iam get-role-policy: SchwabOpsCodeRead = s3:GetObject on opal-data-schwab/_ops/canonical-schwab-si2/* ONLY (no 
- 20260702T214640Z CLOSED -- all 4 legs proven
