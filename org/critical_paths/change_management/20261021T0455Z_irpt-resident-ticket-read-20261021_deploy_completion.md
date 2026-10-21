# Deploy Completion Record
**Date opened:** 2026-10-21T04:55:55.216739+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T050113Z
**Deploy:** IRPT_ANLREQ TO-APPLY-TICKETREAD: ONE new customer-managed IAM policy (dynamodb:GetItem only on table opal-tickets, restricted to four attributes with a Null guard) and its attachment to irpt-ycharts-runner-role, so the packager can read the filed ticket for the analysis-audit record
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: five inline policies with sha256, attached list, the new policy absent, the five baseline arms on the role | R0 baseline implicitDeny on the ticket read | R0 baseline implicitDeny on the ticket read at 04:57Z: five inline policies read (hashes equal the audit-policy R0: 693ccc20, 387ffb24, 7622ce68, ed04ec88, c970dc35), attached [AmazonSSMManagedInstanceCore, irpt-audit-write-policy]; the five baseline arms on the role: S1 GetItem with the four attributes implicitDeny; S2, S3a, S3b, S4a to S4d, S5b implicitDeny; S5a GetItem on opal-users-v2 ALLOWED by the role's inline policy irpt-ycharts-runner (printed as the order asks: V must equal it); COO blob 2f30cbbe6e and CTO half naming it; pin 1ce03f969b equal at HEAD 7b7af93771; open-deploys 50 worktrees 152 entries, 14 terminal and 2 non-terminal name the stack/role wording: d12 (SMS, held) and a18 (NFRA_TRNSPT second_reader, HELD-SOVEREIGN-GATED, another stack, names this role only as a read gate); run 7I terminal | CLOSED 20261021T045703Z |
| C | verify | scoped plan at trunk reads 2 to add 0 to change 0 to destroy with exactly the one ticket-read statement and the one attachment | plan output and document read | C plan 2 to add 0 to change 0 to destroy from a throwaway detached worktree at trunk 449781b700b (resident_ticket_read_policy.tf blob 1ce03f969b equal; fmt -check rc 0; init; saved plan with the two -target flags): aws_iam_policy.resident_ticket_read irpt-ticket-audit-read-policy (create) with exactly ONE statement ReadTheFiledTicketForTheAuditOnly (Allow, dynamodb:GetItem only, exactly arn:aws:dynamodb:us-east-1:313476888478:table/opal-tickets with no index and no wildcard; Condition exactly Null dynamodb:Attributes false, ForAllValues:StringEquals dynamodb:Attributes = ticket_id, ticket_type, answers, created_at, StringEqualsIfExists dynamodb:Select = SPECIFIC_ATTRIBUTES); aws_iam_role_policy_attachment.runner_resident_ticket_read (create) to irpt-ycharts-runner-role only; nothing changed or destroyed | CLOSED 20261021T045803Z |
| S | verify | the five arms on the plan's rendered policy document by simulate-custom-policy BEFORE apply | S arms held before apply | S arms held before apply (simulate-custom-policy on the plan's rendered document, one resource per call): S1 GetItem with the four attributes and Select SPECIFIC_ATTRIBUTES ALLOWED (the positive); S2 GetItem with no dynamodb:Attributes entry implicitDeny (the Null guard holds in the simulator); S3a requester and S3b created_by implicitDeny; S4 Query, Scan, BatchGetItem, PutItem implicitDeny; S5 GetItem on opal-users-v2 and on opal-tickets/index/status-index implicitDeny | CLOSED 20261021T045815Z |
| A | activation | safe-apply of the saved plan | Apply complete 2 added 0 changed 0 destroyed | safe-apply 2026-10-21T04:58:29Z to 04:59:28Z rc 0: Apply complete! Resources: 2 added, 0 changed, 0 destroyed (irpt-ticket-audit-read-policy and its attachment to irpt-ycharts-runner-role); halt gate passed without HALT_ACK; broker read at 04:58Z clean | CLOSED 20261021T050113Z |
| V | verify | after-reads G1 to G3: inline policies unchanged, new policy exact, the five arms on the role, replan No changes | G1 G2 G3 lines | G1 five inline policies' canonical sha256 equal R0; attached list R0 plus irpt-ticket-audit-read-policy; default version v1 holds exactly the one statement; entities: the runner role only. G2 the five arms on the role: S1 allowed (matched irpt-ticket-audit-read-policy), S2 implicitDeny, S3a S3b S4a to S4d S5b implicitDeny, S5a allowed by irpt-ycharts-runner equal to R0 (not the new policy). G3 replan of the same targets: No changes | CLOSED 20261021T050113Z |

## Log

- 20261021T045555Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T045703Z LEG R0 closed: R0 baseline implicitDeny on the ticket read at 04:57Z: five inline policies read (hashes equal the audit-policy R0: 693c
- 20261021T045803Z LEG C closed: C plan 2 to add 0 to change 0 to destroy from a throwaway detached worktree at trunk 449781b700b (resident_ticket_read_p
- 20261021T045815Z LEG S closed: S arms held before apply (simulate-custom-policy on the plan's rendered document, one resource per call): S1 GetItem wit
- 20261021T050113Z LEG A closed: safe-apply 2026-10-21T04:58:29Z to 04:59:28Z rc 0: Apply complete! Resources: 2 added, 0 changed, 0 destroyed (irpt-tick
- 20261021T050113Z LEG V closed: G1 five inline policies' canonical sha256 equal R0; attached list R0 plus irpt-ticket-audit-read-policy; default version
- 20261021T050113Z CLOSED -- all 5 legs proven
