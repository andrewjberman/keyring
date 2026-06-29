# Deploy Completion Record
**Date opened:** 2026-06-29T13:13:09.084247+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T132044Z
**Deploy:** SCTY.W2 AWS-IAM-1 Moltbot full decommission -- retire dormant privesc chain (CTO GATE-PASS 2026-06-29)
**Authored by:** 0.7.0_AE_CloudOps~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit 0c5ead90c (iam_legacy.tf moltbot removal) | hash pushed origin/CLOUD | 0c5ead90c pushed origin/CLOUD (691f421c2..0c5ead90c) | CLOSED 20260629T131319Z |
| L2 | activation | boto3 detach+delete MoltbotEC2Profile (DeleteConflict pre-step) | get-instance-profile NoSuchEntity | stage_profile: removed role + deleted profile; live get-instance-profile now NoSuchEntity | CLOSED 20260629T131319Z |
| L3 | verify | shared-infra safe-apply moltbot IAM removal | 0/0/3 destroy + 0-diff post-apply + 3 roles/policy gone live | safe-apply 0/0/3 destroyed; post-apply plan 'No changes'; live get-role MoltbotEC2Role=NoSuchEntity | CLOSED 20260629T131458Z |
| L4 | activation | boto3 delete moltbot-sg + CodeBuild moltbot-openclaw-build + its log-group | describe NotFound x3 | stage_directs deleted all 3; live: SG InvalidGroup.NotFound, CodeBuild in projectsNotFound, log-group [] empty | CLOSED 20260629T131525Z |
| L5 | activation | secrets schedule-delete-with-window github/moltbot-pat + opal/moltbot-anthropic-key | DeletionDate set x2 | both secrets scheduled-delete 30d window; github/moltbot-pat + opal/moltbot-anthropic-key recover-until 2026-07-29 (reversible) | CLOSED 20260629T131549Z |
| L6 | git | CI resource-map update + moltbot repo-dir removal commit | hash pushed origin/CLOUD | commit a5c036ab6 pushed origin/CLOUD (CI resource-map MoltbotEC2Role removed + 23 dead moltbot EC2 files git-rm'd) | CLOSED 20260629T131902Z |
| L7 | verify | CVO 0-residual handoff | CVO artifacts handed + sweep clean | author 0-residual sweep CLEAN (IAM roles/policies/profiles/EC2/SG/Lambda/CodeBuild all []; 2 secrets in intended recovery window); artifact security/own-attack-surface/SCTY.W2_moltbot-teardown-0residual_20260629.md; CVO handoff sent | CLOSED 20260629T132044Z |

## Log

- 20260629T131309Z OPENED by 0.7.0_AE_CloudOps~B with 7 leg(s)
- 20260629T131319Z LEG L1 closed: 0c5ead90c pushed origin/CLOUD (691f421c2..0c5ead90c)
- 20260629T131319Z LEG L2 closed: stage_profile: removed role + deleted profile; live get-instance-profile now NoSuchEntity
- 20260629T131458Z LEG L3 closed: safe-apply 0/0/3 destroyed; post-apply plan 'No changes'; live get-role MoltbotEC2Role=NoSuchEntity
- 20260629T131525Z LEG L4 closed: stage_directs deleted all 3; live: SG InvalidGroup.NotFound, CodeBuild in projectsNotFound, log-group [] empty
- 20260629T131549Z LEG L5 closed: both secrets scheduled-delete 30d window; github/moltbot-pat + opal/moltbot-anthropic-key recover-until 2026-07-29 (reve
- 20260629T131902Z LEG L6 closed: commit a5c036ab6 pushed origin/CLOUD (CI resource-map MoltbotEC2Role removed + 23 dead moltbot EC2 files git-rm'd)
- 20260629T132044Z LEG L7 closed: author 0-residual sweep CLEAN (IAM roles/policies/profiles/EC2/SG/Lambda/CodeBuild all []; 2 secrets in intended recover
- 20260629T132044Z CLOSED -- all 7 legs proven
