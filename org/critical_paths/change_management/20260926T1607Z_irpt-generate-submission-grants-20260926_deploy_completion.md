# Deploy Completion Record
**Date opened:** 2026-09-26T16:07:03.193225+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T161105Z
**Deploy:** irpt-ycharts-generate-role: READ NORMALIZED_PORTFOLIO + RETAIN REQUEST_COMPOSITION (~Y patch @e5daacce0b; CTO 101275)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | activation | aws_iam_role_policy.generate | safe-apply of the saved plan 0/1/0; replan No changes | plan 0 add / 1 change / 0 destroy (aws_iam_role_policy.generate: + ReadNormalizedPortfolioInputsOnly, + RetainRequestCompositionsOnly, 3 firm scopes each); safe-apply (HALT_ACK=1, terraform 1.9.8, backend ycharts root @be7647e48f) 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; replan detailed-exitcode 0 | CLOSED 20260926T161105Z |
| V1 | verify | IAM simulation | K5's two denied actions (GetObjectVersion on normalized_portfolios; PutObject on request_compositions) DENIED before -> ALLOWED after for the generate role; a foreign prefix still denied (negative arm) | iam_simulate_pairs.py on irpt-ycharts-generate-role, 5 pairs (cottonwood state prefixes): BEFORE 0 of 5 allowed (K5's s3:GetObjectVersion normalized_portfolios, s3:PutObject + s3:GetObjectVersion request_compositions all implicitDeny = the K5 denial reproduced); AFTER 3 of 5 allowed, 5 of 5 met expectation (PutObject on normalized_portfolios and GetObject on an ungranted family still implicitDeny). Identity plane only; the full-path list (CTO 101275) is ~Y's and runs next. | CLOSED 20260926T161105Z |

## Log

- 20260926T160703Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260926T161105Z LEG G1 closed: plan 0 add / 1 change / 0 destroy (aws_iam_role_policy.generate: + ReadNormalizedPortfolioInputsOnly, + RetainRequestCom
- 20260926T161105Z LEG V1 closed: iam_simulate_pairs.py on irpt-ycharts-generate-role, 5 pairs (cottonwood state prefixes): BEFORE 0 of 5 allowed (K5's s3
- 20260926T161105Z CLOSED -- all 2 legs proven
