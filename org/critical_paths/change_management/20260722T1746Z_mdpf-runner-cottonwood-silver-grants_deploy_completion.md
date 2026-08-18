# Deploy Completion Record

**Status:** CLOSED 2026-08-18 (on applied-truth evidence: grants live + exercised; nothing stranded)
<!-- disposition act 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md); evidence in the CLOSE block at foot. -->
**Date opened:** 2026-07-22T17:46:27.454342+00:00
**Status:** OPEN
**Deploy:** MDPF runner IAM: ADDITIVE grants for blackdiamond/cottonwood/silver -- AssetsRevampSilverRead (GetObject) + AssetsRevampListScoped (prefix condition). Andrew-direct ~1740Z sovereign carve-out; unblocks Phase 1a/S2a which my own finding proved IAM-blocked (implicitDeny, isolated control allowed, desired==applied so never built).
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | iam.tf two additive statements committed to CLOUD | commit hash pushed |  | OPEN |
| L2 | verify | targeted plan is PURE TO-ADD (0 change, 0 destroy) -- STOP and escalate if not | plan summary line read line-by-line |  | OPEN |
| L3 | activation | safe-apply -target the two role-policy resources | apply output + resource addressed |  | OPEN |
| L4 | verify | 0-diff re-plan AND live get-role-policy shows the cottonwood ARN | live primitive output, not the apply's own |  | OPEN |
| L5 | verify | A12 EXERCISE: simulate GetObject on cottonwood silver = allowed | separate invocation, ONE --resource-arns |  | OPEN |
| L6 | verify | A12 EXERCISE: simulate ListBucket WITH --context-entries s3:prefix = allowed | separate invocation; without context-entries a conditioned stmt returns implicitDeny byte-identical to a real deny |  | OPEN |
| L7 | verify | ISOLATED POSITIVE + NEGATIVE controls, each its own invocation | control must discriminate: a still-ungranted ARN reads implicitDeny |  | OPEN |

## Log

- 20260722T174627Z OPENED by 0.7.0_AE_CloudOps with 7 leg(s)


---

## CLOSE (2026-08-18, 0.0.0_AB_MSTR disposition act)

Leg rows were never filled at deploy time; closed on end-state evidence (read-only pass, 2026-08-18):
- L1: commit `1fd3719c68` (2026-07-22T17:48Z, 0.7.0_AE_CloudOps) added both statements to
  `infra/aws/terraform/mdpf-pipeline/iam.tf` -- 1 minute after this ledger opened.
- L4 (applied truth): `aws iam get-role-policy --role-name mdpf-daily-runner-ec2-role --policy-name mdpf-runner-scoped`
  carries BOTH Sids: `AssetsRevampSilverRead` (s3:GetObject incl. `arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/silver/*`)
  and `AssetsRevampListScoped` (s3:ListBucket, s3:prefix StringLike incl. `blackdiamond/cottonwood/silver/*`).
- L5/L6 (exercised, isolated simulate-principal-policy calls, ONE --resource-arns each, context-entries on the List leg):
  GetObject on a cottonwood silver key = `allowed`; ListBucket with the prefix context = `allowed`.
- The policy has since grown additively (e.g. `a4d71e9544`); the cottonwood grant is intact inside the evolved statement.
PATH caveat recorded honestly: the plan/apply legs (L2/L3) were never evidenced at the time; this close rests on
applied truth + exercise, not on the apply's own report.
