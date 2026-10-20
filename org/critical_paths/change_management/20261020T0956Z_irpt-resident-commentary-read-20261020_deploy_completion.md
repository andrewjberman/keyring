# Deploy Completion Record
**Date opened:** 2026-10-20T09:56:59.331046+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T100537Z
**Deploy:** IRPT_ANLREQ TO-APPLY-IAMGRANT: resident role irpt-ycharts-runner-role gains read (GetObject, GetObjectVersion) of the ANALYSIS_COMMENTARY draft prefixes; one statement on aws_iam_role_policy.runner_resident, pin 430cd08b2a
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: policy Sid list and canonical sha256, simulation get and put implicitDeny | R0 baseline printed | R0 baseline implicitDeny get and put at 2026-10-20T09:57Z: 13 Sids, no ReadTheAnalysisCommentaryDraft, canonical sha256 9c4fcf53...3f0d; controls: put on ycharts_opal_reports allowed, get on original_holdings allowed; open-deploys denominator 47 worktrees, 162 blobs read, no open write entry on the ycharts stack, the role or its policy (one HELD-SOVEREIGN-GATED NFRA_TRNSPT entry names the role only as a gate reference) | CLOSED 20261020T095829Z |
| C | verify | scoped plan at the pin: 0 to add 1 to change 0 to destroy, one statement added | plan lines printed | C plan 0 to add 1 to change 0 to destroy at 2026-10-20T10:0xZ from a detached worktree at pin 430cd08b2a (fmt -check rc 0, init, scoped -target plan saved); only attribute changed: policy; Sid list 13 -> 14, added exactly ReadTheAnalysisCommentaryDraft (Allow s3:GetObject s3:GetObjectVersion on 3 analysis_commentaries/* prefixes), 0 removed, 0 changed in place; plan-before equals live R0 document; naming gate PASS 2 graded | CLOSED 20261020T100305Z |
| A | activation | safe-apply of the saved plan on aws_iam_role_policy.runner_resident | apply complete 0 added 1 changed 0 destroyed | safe-apply of the saved plan 2026-10-20T10:03:20Z..10:04:12Z rc 0: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.runner_resident) | CLOSED 20261020T100537Z |
| V | verify | after-reads G1 G2 G3 | G1 G2 G3 printed | G1 new=[ReadTheAnalysisCommentaryDraft] removed=[] changed=[] (13 -> 14 Sids, others byte-equal per Sid); G2 get allowed, getversion allowed, put implicitDeny on run-6 analysis_commentaries key, ycharts_opal_reports put and original_holdings get allowed as at R0; G3 replan No changes at 2026-10-20T10:04:52Z; document sha256 9c4fcf53... -> 7038867f... | CLOSED 20261020T100537Z |

## Log

- 20261020T095659Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T095829Z LEG R0 closed: R0 baseline implicitDeny get and put at 2026-10-20T09:57Z: 13 Sids, no ReadTheAnalysisCommentaryDraft, canonical sha256 
- 20261020T100305Z LEG C closed: C plan 0 to add 1 to change 0 to destroy at 2026-10-20T10:0xZ from a detached worktree at pin 430cd08b2a (fmt -check rc 
- 20261020T100537Z LEG A closed: safe-apply of the saved plan 2026-10-20T10:03:20Z..10:04:12Z rc 0: Apply complete! Resources: 0 added, 1 changed, 0 dest
- 20261020T100537Z LEG V closed: G1 new=[ReadTheAnalysisCommentaryDraft] removed=[] changed=[] (13 -> 14 Sids, others byte-equal per Sid); G2 get allowed
- 20261020T100537Z CLOSED -- all 4 legs proven
