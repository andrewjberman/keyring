# Deploy Completion Record
**Date opened:** 2026-09-27T01:21:55.933779+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T222045Z -- gate: external / the Monday 2026-09-28 22:10Z scheduled fire of bd-asset-dim-pipeline-trigger, which is L4's evidence source and requires no new vendor authorization (held since 2026-09-27T01:47:58.720333+00:00)
**Deploy:** opal-bd-asset-dim-download arms its shutdown BEFORE the non-zero exit, so a failing run reports Failed and still stops its runner (NFRA_MCPINDEX MX-s-4 step 2, on 2.0.0_SA_COO~O's Z-S17 ruling)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 72.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: the shutdown moved above the failure branch | commit hash | 03e744ec3f -- the two shutdown lines moved above the failure branch with the reason beside them; the branch keeps its exit 1; a plain echo Done. closes the success path. 60 -> 66 runCommand lines. Asserted in the edit script, not eyeballed: exactly one shutdown -h and exactly one exit 1 survive, and no pre-existing line was dropped. | CLOSED 20260927T013528Z |
| L2 | activation | SSM document opal-bd-asset-dim-download, new DocumentVersion via update-document | describe-document LatestVersion advances past 2 and Hash changes from 5130ead6f5b0f201739af7a6fc65cb67574f7de2e6f89fee9e5f18a67d442129 | ssm update-document -> DocumentVersion 3, Active. Hash 5130ead6f5b0f201739af7a6fc65cb67574f7de2e6f89fee9e5f18a67d442129 -> 490af5249f84285f037cd200b210283e8f57edfa383a316234fede1008b77d66. Default moved to 3 so default and $LATEST agree. v1 and v2 retained; nothing destroyed. NO INSTANCE INTERACTION: update-document creates a version and sends nothing to i-0e6f6dc014fdcf1cd, which is the constraint the Z-S17 ruling placed on this act. | CLOSED 20260927T013528Z |
| L3 | verify | the LIVE content at the version the trigger Lambda pins | get-document at $LATEST shows shutdown -h ABOVE exit 1, exactly one of each | get-document at $LATEST -- the version the trigger Lambda pins -- RE-READ by this seat rather than taken from the update call: 'shutdown -h' at index 58, 'exit 1' at index 63, so the shutdown PRECEDES the exit; exactly one of each; LIVE == REPO compared line by line; 66 lines. | CLOSED 20260927T013528Z |
| L4 | verify | one failing run that records Failed AND ends with the instance stopped | the scheduled Monday 22:10Z fire: SSM Status Failed plus i-0e6f6dc014fdcf1cd State stopped afterwards | PLANTED failure, admitted by AC4 ('a real or planted failure'), and the issuer's 215826Z ruling superseded the entry's Monday-fire gate. ssm:e77e84c7-6e1f-4772-9dae-d00dc52b9965 AWS-RunShellScript on i-0e6f6dc014fdcf1cd: Status=Failed ResponseCode=1, ExecutionStart 2026-09-27T22:15:03.689Z. The script under test is the LIVE v3 runCommand indices 52-65 copied programmatically from ssm get-document (describe-document independently re-read by this seat: LatestVersion 3, DefaultVersion 3, Active, Hash 490af5249f84285f037cd200b210283e8f57edfa383a316234fede1008b77d66, matching L2's recorded post-hash), with exactly ONE substitution -- the log destination moved to logs/_planted_probes/ so the probe can never be miscounted inside the asset-dim-download-*.log corpus. ORDERING PROVEN IN BOTH DIRECTIONS: stdout emits 'Shutting down in 2 minutes...' BEFORE 'ERROR: Asset-dim pipeline failed (download_rc=1 merge_rc=99)', and stderr carries the OS's own confirmation 'Shutdown scheduled for Sun 2026-09-27 22:17:03 UTC' alongside 'failed to run commands: exit status 1' -- so the shutdown was really armed, not merely echoed. INSTANCE STOPPED: ec2 describe-instances read running at 22:16:53Z, stopping at 22:17:16Z, stopped at 22:17:38Z, i.e. the 22:17:03Z scheduled halt fired. WHAT THIS DOES NOT COVER, stated: the bun downloader and the BD portal login were NOT invoked (no vendor contact), so this proves the wrapper's exit/shutdown ordering, NOT that a real login failure produces the non-zero rc -- that is already evidenced by 69 consecutive real failures since 2026-06-23. The Monday 2026-09-28 22:10Z scheduled fire remains the end-to-end acceptance. | CLOSED 20260927T222020Z |
| L5 | git | the ledger state committed | commit hash | 631d541258 -- the entry with L1-L3 closed. First attempt hit rc=128 on a git index.lock race with a concurrent seat; nothing committed, confirmed by asking the repository (git log) rather than grepping the tool's own prose, with a bogus-hash negative control. Retried clean. | CLOSED 20260927T014757Z |

## Log

- 20260927T012155Z OPENED by 0.7.0_AE_CloudOps~I with 5 leg(s)
- 20260927T013528Z LEG L1 closed: 03e744ec3f -- the two shutdown lines moved above the failure branch with the reason beside them; the branch keeps its ex
- 20260927T013528Z LEG L2 closed: ssm update-document -> DocumentVersion 3, Active. Hash 5130ead6f5b0f201739af7a6fc65cb67574f7de2e6f89fee9e5f18a67d442129 
- 20260927T013528Z LEG L3 closed: get-document at $LATEST -- the version the trigger Lambda pins -- RE-READ by this seat rather than taken from the update
- 20260927T014757Z LEG L5 closed: 631d541258 -- the entry with L1-L3 closed. First attempt hit rc=128 on a git index.lock race with a concurrent seat; not
- 20260927T014758Z HELD-SOVEREIGN-GATED gate=external/the Monday 2026-09-28 22:10Z scheduled fire of bd-asset-dim-pipeline-trigger, wh
- 20260927T222020Z LEG L4 closed: PLANTED failure, admitted by AC4 ('a real or planted failure'), and the issuer's 215826Z ruling superseded the entry's M
- 20260927T222045Z CLOSED -- all 5 legs proven
