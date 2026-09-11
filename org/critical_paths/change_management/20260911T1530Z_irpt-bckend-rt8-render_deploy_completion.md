# Deploy Completion Record
**Date opened:** 2026-09-11T15:30:55.719579+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-8 arm (a) UNLOCKED -- the export render on irpt-ycharts-runner, on Andrew's word (1.0.0_SA_CTO 95983, 14:5xZ, VERBATIM 'Yes ycharts runner may be started')
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the ycharts root's header and runner_declared_state description amended to say that starting the host FOR A RENDER is not the gated sign-in; the export root's render document made self-deploying and the render host granted the exports prefix from THIS root | commit hash |  | OPEN |
| L2 | s3-prefix | the host half uploaded to s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ | head-object per file with sizes |  | OPEN |
| L3 | activation | safe-apply of the export root (document + host grant) and the ycharts root (description only, no state change) | safe-apply output plus the ycharts plan summary |  | OPEN |
| L4 | verify | THE RENDER ITSELF: a submit through the DEPLOYED controller, ec2 start-instances, ssm send-command irpt-export-render-run, the command output captured VERBATIM whatever it says, and the outbound-origin guard denominator | SSM command output and any S3 object written |  | OPEN |
| L5 | verify | THE HOST RETURNED TO ITS DECLARED STATE: ec2 stop-instances, describe-instances reads stopped, and the ycharts root re-plans with no state drift | describe-instances plus terraform plan |  | OPEN |

## Log

- 20260911T153055Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 5 leg(s)
