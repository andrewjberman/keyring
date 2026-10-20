# Deploy Completion Record
**Date opened:** 2026-10-20T18:25:49.876997+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T183513Z
**Deploy:** IRPT_ANLREQ TO-APPLY-STATUSGRANT: irpt-status-role reads the YCHARTS_OPAL_REPORT PDF family: one statement's resource list extended by three entries on aws_iam_role_policy.irpt_status, drained commit 9b614db42a1
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy Sid list, retained-families resources, sha256, simulation get and getversion on the 7b PDF key | R0 baseline implicitDeny get and getversion | R0 baseline implicitDeny get and getversion on run 7b's PDF key at 2026-10-20T18:27Z: 5 Sids, retained-families statement 18 resources, no ycharts_opal_reports entry, canonical sha256 262fc75f...adb9c; control: original_holdings GetObject allowed; PutObject and DeleteObject implicitDeny; open-deploys denominator 54 worktrees and 146 distinct entries, none non-terminal against the ops stack, the role or its policy | CLOSED 20261020T182839Z |
| C | verify | scoped plan at the drained commit reads 0 to add 1 to change 0 to destroy with exactly three added resource entries | plan output and diff read | C plan 0 to add 1 to change 0 to destroy at 2026-10-20T18:3xZ from a throwaway detached worktree at the drained commit 9b614db42a1 (iam.tf blob 04b6c4e8a8b8 equal, fmt -check iam.tf rc 0, init, scoped -target plan saved); only attribute changed: policy; Sid list unchanged (5 Sids, same order); one statement changed: ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly, resources 18 -> 21, added exactly arn:aws:s3:::opal-data-irpt/irpt/{49financial,cottonwood,inflection}/state/ycharts_opal_reports/*, 0 removed, Action and Effect unchanged; planned document sha256 eed357ca...23f3c0 | CLOSED 20261020T183115Z |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed | safe-apply of the saved plan 2026-10-20T18:32:59Z..18:33:43Z rc 0 (first attempt 18:31:52Z blocked by the halt gate on 6 already-READ routine messages, nothing applied; re-run with HALT_ACK=1 after a broker read showed 0 unread): Apply complete! Resources: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.irpt_status) | CLOSED 20261020T183425Z |
| V | verify | after-reads G1 to G3: byte-equal other statements, simulation, replan No changes | G1 G2 G3 lines | G1 sid list equal (5), only ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly changed, resources 18 -> 21 (plus exactly the three ycharts_opal_reports/* entries), rest of the statement and the other four byte-equal; G2 get and getversion allowed on run 7b's PDF key, put and delete implicitDeny, original_holdings get allowed as at R0; G3 replan No changes at 2026-10-20T18:34Z; sha256 262fc75f... -> eed357ca... (equals the planned value) | CLOSED 20261020T183513Z |

## Log

- 20261020T182549Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T182839Z LEG R0 closed: R0 baseline implicitDeny get and getversion on run 7b's PDF key at 2026-10-20T18:27Z: 5 Sids, retained-families statemen
- 20261020T183115Z LEG C closed: C plan 0 to add 1 to change 0 to destroy at 2026-10-20T18:3xZ from a throwaway detached worktree at the drained commit 9
- 20261020T183425Z LEG A closed: safe-apply of the saved plan 2026-10-20T18:32:59Z..18:33:43Z rc 0 (first attempt 18:31:52Z blocked by the halt gate on 6
- 20261020T183513Z LEG V closed: G1 sid list equal (5), only ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly changed, resources 18 -> 21 (plus exa
- 20261020T183513Z CLOSED -- all 4 legs proven
