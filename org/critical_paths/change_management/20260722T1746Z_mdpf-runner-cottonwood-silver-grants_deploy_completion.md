# Deploy Completion Record
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
