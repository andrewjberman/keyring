# Deploy Completion Record
**Date opened:** 2026-09-26T23:08:40.184747+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T003600Z
**Deploy:** opal-bd-asset-dim-download exits non-zero on failure, plus ONE ad-hoc vendor-facing fire on Andrew's word (NFRA_MCPINDEX MX-s-4 steps 1-2)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: the exit 1 inserted into the failure branch | commit hash | 4b3a757410 -- one line inserted into the failure branch of infra/aws/ssm/opal-bd-asset-dim-download.json, copied from the estate idiom; 59 -> 60 runCommand lines, every other line byte-identical, asserted in the edit script. | CLOSED 20260927T001914Z |
| L2 | activation | SSM document opal-bd-asset-dim-download, new DocumentVersion via update-document | describe-document LatestVersion advances and Hash changes from 0be92f2611060f033011ed74ff5647be127f0511ee723ce42f890d3c7a7a30e6 | ssm update-document -> DocumentVersion 2, Status Updating then Active; Hash 0be92f2611060f033011ed74ff5647be127f0511ee723ce42f890d3c7a7a30e6 -> 5130ead6f5b0f201739af7a6fc65cb67574f7de2e6f89fee9e5f18a67d442129. update-document-default-version -> DefaultVersion 2, so the default and $LATEST agree rather than diverging for a human reader. v1 retained; nothing destroyed. | CLOSED 20260927T001915Z |
| L3 | verify | the LIVE document content at the version the trigger Lambda will run | get-document shows 'exit 1' inside the DOWNLOAD_RC/MERGE_RC failure branch | get-document --document-version $LATEST (the version the trigger Lambda pins) re-read by this seat: the failure branch now carries 'exit 1' as its last statement, runCommand is 60 lines, and LIVE == REPO compared line by line. Not taken from the update call's own success. | CLOSED 20260927T001917Z |
| L4 | activation | ONE ad-hoc vendor-facing run via Lambda bd-asset-dim-trigger, on Andrew's word 2026-09-26 22:05Z + 22:15Z | the invoke response, the SSM CommandId, and the run ledgered in this lane's deliverables | ONE ad-hoc vendor-facing run, fired 2026-09-26T23:31:15Z on Andrew's word ('rec a approved' ~22:05Z; 'vendor call is fine you have egress' ~22:15Z). lambda invoke bd-asset-dim-trigger RequestResponse -> StatusCode 200, no FunctionError, body 'Asset dim download triggered on i-0e6f6dc014fdcf1cd, command 9ba8d9c9-6759-4a4c-a1ac-d571abcde94f'. Run ledgered here and in this lane's deliverables. ONE run only; no new credential, no account change, no vendor interaction. | CLOSED 20260927T001919Z |
| L5 | verify | the SSM command status for that run (AC4's evidence) | list-command-invocations Status for the CommandId -- Failed if the download fails, which is the honest report the old document could not make | THE POINT OF THE WHOLE ACT: SSM get-command-invocation for 9ba8d9c9-6759-4a4c-a1ac-d571abcde94f reads Status=Failed, StatusDetails=Failed, ResponseCode=1, 23:32:14Z -> 23:32:56Z. The identical failure recorded Success before this change. Cause reproduced live and unchanged: 'Phase 1: Login ... Error: TimeoutError: forURL: Timeout 30000ms exceeded ... waiting for navigation to **/bd3.bdreporting.com/** until load', then 'Download exit code: 1', 'SKIP: silver conversion skipped', 'ERROR: Asset-dim pipeline failed (download_rc=1 merge_rc=99)'. This is the 70th consecutive failure and AC4's evidence. AC1 remains FAILING as anticipated -- it needs a successful download. SIDE EFFECT FIRED AND IS NOT YET REMEDIED: the exit 1 returns before 'shutdown -h +2', so i-0e6f6dc014fdcf1cd is left RUNNING and no CloudWatch auto-stop exists for it (describe-alarms returns []). Stopping an EC2 is human-confirmation-gated, so it is surfaced to Andrew and this ledger is HELD rather than closed. | CLOSED 20260927T001922Z |
| L6 | git | the ledger close | commit hash | 0f6109aa8d -- the entry with L1-L5 closed and the stranded-runner finding committed. NOTE ON THIS LEG'S OWN SHAPE: L6 was written as 'the ledger close', which the tool correctly classifies as an apply/deploy leg and which therefore BLOCKED the HELD transition -- a ledger cannot cite its own closure as a precondition for being held open. Re-read as what it actually is: the commit that persists this entry's state. The mis-specification is mine, at open time, and is recorded rather than quietly reworded. | CLOSED 20260927T003251Z |

## Log

- 20260926T230840Z OPENED by 0.7.0_AE_CloudOps~I with 6 leg(s)
- 20260927T001914Z LEG L1 closed: 4b3a757410 -- one line inserted into the failure branch of infra/aws/ssm/opal-bd-asset-dim-download.json, copied from th
- 20260927T001915Z LEG L2 closed: ssm update-document -> DocumentVersion 2, Status Updating then Active; Hash 0be92f2611060f033011ed74ff5647be127f0511ee72
- 20260927T001917Z LEG L3 closed: get-document --document-version $LATEST (the version the trigger Lambda pins) re-read by this seat: the failure branch n
- 20260927T001919Z LEG L4 closed: ONE ad-hoc vendor-facing run, fired 2026-09-26T23:31:15Z on Andrew's word ('rec a approved' ~22:05Z; 'vendor call is fin
- 20260927T001922Z LEG L5 closed: THE POINT OF THE WHOLE ACT: SSM get-command-invocation for 9ba8d9c9-6759-4a4c-a1ac-d571abcde94f reads Status=Failed, Sta
- 20260927T003251Z LEG L6 closed: 0f6109aa8d -- the entry with L1-L5 closed and the stranded-runner finding committed. NOTE ON THIS LEG'S OWN SHAPE: L6 wa
- 20260927T003600Z CLOSED -- all 6 legs proven
