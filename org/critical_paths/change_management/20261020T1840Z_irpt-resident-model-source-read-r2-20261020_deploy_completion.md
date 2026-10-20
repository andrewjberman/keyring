# Deploy Completion Record
**Date opened:** 2026-10-20T18:40:59.897291+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T184931Z
**Deploy:** IRPT_ANLREQ TO-APPLY-MODELGRANT v2: one-statement IAM grant (s3:GetObject on two exact keys of opal-data-portal-v2) on aws_iam_role_policy.runner_resident, re-pin 680818fdb3e
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy Sid list and sha256, four baseline simulations | R0 baseline implicitDeny on all four | R0 baseline implicitDeny on all four at 2026-10-20T18:41Z: 14 Sids, ReadTheModelReturnSeriesAndPositioning absent; GetObject on both keys and a third key, PutObject on the first key all implicitDeny; control PutObject on a ycharts_opal_reports key allowed; open-deploys denominator 52 worktrees and 147 distinct entries, none non-terminal on the ycharts stack, the role or its policy (a18 read-evidence reference only); no open IB2 IAM act (status grant ledger CLOSED 18:35:13Z); COO blob 640730617653 and CTO half naming it | CLOSED 20261020T184311Z |
| C | verify | scoped plan at the re-pin reads 0 to add 1 to change 0 to destroy with exactly one added statement | plan output and diff read | C plan 0 to add 1 to change 0 to destroy at 2026-10-20T18:4xZ from a throwaway detached worktree at the re-pin 680818fdb3e (fmt -check resident.tf rc 0, init, scoped -target plan saved); only attribute changed: policy; Sids 14 -> 15, exactly one new statement ReadTheModelReturnSeriesAndPositioning (Allow, s3:GetObject, the two exact opal-data-portal-v2 ARNs, no Condition), 0 removed, 0 changed; planned document sha256 c970dc35...1b35 (equals the first attempt's informational plan); before sha256 7038867f... equals R0 | CLOSED 20261020T184435Z |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed | safe-apply of the saved plan 2026-10-20T18:46:34Z..18:47:12Z rc 0 (first attempt 18:45:31Z blocked by the halt gate on 8 already-READ routine messages, none STOP-class, broker showed 0 not-READ rows; nothing applied; re-run with HALT_ACK=1): Apply complete! Resources: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.runner_resident) | CLOSED 20261020T184755Z |
| V | verify | after-reads G1 to G4: byte-equal other statements, simulation, replan No changes, host-role reads of both objects | G1 G2 G3 G4 lines | G1 new=[ReadTheModelReturnSeriesAndPositioning] removed=[] changed=[] (14 -> 15 Sids, others byte-equal per Sid, exact statement shape); G2 GetObject allowed on both keys, PutObject (both), DeleteObject, GetObjectVersion and GetObject on a third key implicitDeny; G3 replan No changes at 2026-10-20T18:48Z; G4 host role irpt-ycharts-runner-role read both objects rc 0 (780910 and 6890 bytes, AES256), series parses, positioning 1f8b gunzip and JSON ok; sha256 7038867f... -> c970dc35... (= planned) | CLOSED 20261020T184931Z |

## Log

- 20261020T184059Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T184311Z LEG R0 closed: R0 baseline implicitDeny on all four at 2026-10-20T18:41Z: 14 Sids, ReadTheModelReturnSeriesAndPositioning absent; GetOb
- 20261020T184435Z LEG C closed: C plan 0 to add 1 to change 0 to destroy at 2026-10-20T18:4xZ from a throwaway detached worktree at the re-pin 680818fdb
- 20261020T184755Z LEG A closed: safe-apply of the saved plan 2026-10-20T18:46:34Z..18:47:12Z rc 0 (first attempt 18:45:31Z blocked by the halt gate on 8
- 20261020T184931Z LEG V closed: G1 new=[ReadTheModelReturnSeriesAndPositioning] removed=[] changed=[] (14 -> 15 Sids, others byte-equal per Sid, exact s
- 20261020T184931Z CLOSED -- all 4 legs proven
