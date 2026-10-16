# Deploy Completion Record
**Date opened:** 2026-10-16T20:05:47.578760+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T202547Z
**Deploy:** TCKT_VNEXT TO-R18-CLOSE PART 1b (run pair AMENDMENT 4, GO msg 9815): claim then complete the ONE synthetic meeting ticket TCK-20261016-9d7654eb as one minted internal identity tckt-r18-filer-20261016@opal.invalid (allowedFirmIds [cottonwood]) on the reused localhost:5174 server; no routing window, no Terraform, no S3, no mail (map is {}); pair blobs b83e173a01 / ea18a44085 / cf7c856072, criterion 60ff76b607
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | four blobs and the start gate read by the applier (ticket open and unassigned, identity row ABSENT, server answers, sweep) | all true and printed | 4 of 4 blobs equal at worktree, HEAD and GO commit 8ae0683c1a (pair b83e173a01, CTO half ea18a44085, origin half cf7c856072, criterion r18_afterread.py 60ff76b607); TO-R18-RUN complete and its ledger CLOSED; ticket TCK-20261016-9d7654eb meeting_request open unassigned firm cottonwood; identity row ABSENT; GET localhost:5174 200 (server reused, not started or stopped); function CodeSha256 JwdnACONAnxw..., CLIENT_NOTICE_CONTACT_MAP {} and TICKET_DL_MAP {}; sweep 94 trees read, 0 failures, no open entry naming opal-ticket-api, opal-tickets or opal-users-v2 in the shared tree | CLOSED 20261016T200803Z |
| M1 | activation | identity row written with attribute_not_exists(PK), PRESENT, ONE token minted in memory, role set printed | iat and exp recorded, exp at most 20 minutes | identity row tckt-r18-filer-20261016@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT; ROLE SET role=user userType=test-filer firmId=opal-capital allowedFirmIds=[cottonwood] other rows under the key: 0; ONE token iat 2026-10-16T20:09:44Z exp 2026-10-16T20:24:44Z life 900s, in memory only. (Attempt 1 at 20:08Z aborted on a script query error BEFORE any token or key read; its row was deleted and read ABSENT; trace kept) | CLOSED 20261016T202213Z |
| K1 | activation | the identity presses Claim on that ticket only in the browser on http://localhost:5174 | status in_progress, assignee the identity, log tokens printed, no WE_CLIENT_SENT | page origin http://localhost:5174 printed; Claim pressed on TCK-20261016-9d7654eb only, http 200; ConsistentRead status in_progress, assignee tckt-r18-filer-20261016@opal.invalid; claim log lines 20:09:49Z: WE_CLIENT_NO_CONTACT firm=cottonwood, WE_CLIENT_NOT_SINGULAR kind=pickup (resolved 0 recipients, refused); WE_CLIENT_SENT 0, WE_CLIENT_SEND_FAILED 0 | CLOSED 20261016T202213Z |
| P1 | activation | the identity presses Complete on that ticket only | status completed, log tokens printed, no WE_CLIENT_SENT | In Progress tab, Complete pressed on the same ticket only, http 200 (resolution prompt answered with a [TEST] note); ConsistentRead status completed; no WE_* line on the complete | CLOSED 20261016T202213Z |
| R1 | verify | identity row deleted after exp | ConsistentRead ABSENT | identity row deleted at 2026-10-16T20:24:49Z, after token exp 20:24:44Z; ConsistentRead ABSENT (R18_CLOSE_RESULT.json) | CLOSED 20261016T202547Z |
| V1 | verify | r18_afterread.py run read-only after the transitions | AFTERREAD-OK or the reading recorded as printed | r18_afterread.py (blob 60ff76b607), read-only: AFTERREAD-OK from 2026-10-16T17:57:19Z: events_scanned=92 WE_CLIENT_SENT=0 WE_CLIENT_NO_CONTACT=1 paged=False \| control from 2026-10-09T00:00:00Z: events_scanned=1864 WE_CLIENT_SENT=7 | CLOSED 20261016T202547Z |

## Log

- 20261016T200547Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261016T200803Z LEG S1 closed: 4 of 4 blobs equal at worktree, HEAD and GO commit 8ae0683c1a (pair b83e173a01, CTO half ea18a44085, origin half cf7c856
- 20261016T202213Z LEG M1 closed: identity row tckt-r18-filer-20261016@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT; ROLE SET rol
- 20261016T202213Z LEG K1 closed: page origin http://localhost:5174 printed; Claim pressed on TCK-20261016-9d7654eb only, http 200; ConsistentRead status 
- 20261016T202213Z LEG P1 closed: In Progress tab, Complete pressed on the same ticket only, http 200 (resolution prompt answered with a [TEST] note); Con
- 20261016T202547Z LEG R1 closed: identity row deleted at 2026-10-16T20:24:49Z, after token exp 20:24:44Z; ConsistentRead ABSENT (R18_CLOSE_RESULT.json)
- 20261016T202547Z LEG V1 closed: r18_afterread.py (blob 60ff76b607), read-only: AFTERREAD-OK from 2026-10-16T17:57:19Z: events_scanned=92 WE_CLIENT_SENT=
- 20261016T202547Z CLOSED -- all 6 legs proven
