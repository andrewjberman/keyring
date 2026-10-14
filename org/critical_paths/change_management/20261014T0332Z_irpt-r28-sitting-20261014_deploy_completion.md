# Deploy Completion Record
**Date opened:** 2026-10-14T03:32:04.830293+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T035431Z
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R28: release-28 synthetic sitting (FA 49financial, CW cottonwood, svc-irpt-packager) against opal-ticket-api and the upload door; two users rows and one partner row for the sitting, removed after exp; one synthetic ticket stays; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8, AMENDMENTS 1-2
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | step 1 reads (COO half hash, three legs at expected CodeSha256, grants, census); FA and CW keys and GSI ABSENT; write FA and CW users rows and the FA partner row (attribute_not_exists); read back; mint one token per identity (FA, CW, PK), memory only | rows PRESENT, tokens minted | Step 1: COO half hash e9bb20d7fe (AMENDMENTS 1 and 2 read); irpt-status, opal-ticket-api, irpt-ycharts-generate at their expected CodeSha256 and the resident root 0485393f3a-r28 from ledger irpt-resident-r28's V1; grants read as met (simulation, then used for real); census 36 worktrees, 107 entries, 6 name a sitting surface, all CLOSED on trunk. FA and CW keys and the email index ABSENT, FA partner row ABSENT. Rows written 03:33:21Z-22Z (attribute_not_exists) and read back PRESENT as designed: FA (success+irpt-r28-fa-20261014@simulator.amazonses.com, 49financial, active), CW (irpt-r28-cw-20261014@opal.invalid, cottonwood, active), FA partner row (synthetic advisorKey). Signing key read once; three tokens minted 03:33:22Z, exp 03:52:22Z (1140 s), memory only, never written. | CLOSED 20261014T035431Z |
| T4 | verify | T4a, T4b, LIST-A, LIST-B, GET-B (status, code, body sha256 only) | per-request record | T4a 201 (ticket in the five-member view, no answers or attachment echoed); T4b 400 with the item count 31 -> 31; LIST-A 200, 16 rows all with exactly the eight projection members, 16 of 16 firm 49financial analysis_request (read back by ConsistentRead), the T4a ticket present with package_state NONE, no pointer value in the body; LIST-B 200, 2 rows, 0 shared with FA's; GET-B 403 with no ticket field. Per-request UTC start, status and body sha256 in SITTING_TRACE.txt; no body kept. | CLOSED 20261014T035431Z |
| D | verify | D1 to D4 through the upload door as FA, then C1 parseIrEnvelope from portal origin/PROD | per-arm record | D1 to D4 all FAIL: each of the four posts as FA was refused NOT_AUTHORIZED (HTTP 200 refusal envelope, identical body sha256 3fa42669.. for four different files; function log InputAccessDenied classifier NOT_AUTHORIZED) before the file was read; no provider call, nothing stored. Cause: ports ordinary_authorizer is None in reports/generate_installed.py, so no non-Opal viewer is admitted (surprise row IRPT_ANLREQ-D2-S93, BLOCKING). C1: the three bodies PARSED by parseIrEnvelope from portal origin/PROD 10e7664d6c, but they were refusal envelopes, so C1 did not exercise a NEEDS_CORRECTION or NORMALIZED answer. No refusal arm admitted. | CLOSED 20261014T035431Z |
| P5 | verify | PKG-1, PKG-2, PKG-3 as svc-irpt-packager; report_ref once; item sha unchanged on 2 and 3; per-window invocation and token counts | per-request record | PKG-1 200, report_ref set once {request_id, revision 1, recorded_by svc-irpt-packager, recorded_at} read back by ConsistentRead; PKG-2 (AMENDMENT 2: the literal repeat) 409 PACKAGE_ALREADY_ATTACHED, item sha256 unchanged; PKG-3 (AMENDMENT 2: with prior_attached_at, a different request_id) 409 REPORT_REF_ALREADY_RECORDED_OTHER, item sha256 unchanged. Counts per request window from the ticket service's log group: exactly 1 invocation per ticket request; sends only in the T4a window (WE_CLIENT_SENT 1 to the simulator address, WE_DL_UNCONFIGURED 1 so no staff mail); CW's windows sent nothing; streams searched 1, events 27 (not VOID); the service writes no authorize-decision line. SITTING_COUNTS.txt. | CLOSED 20261014T035431Z |
| X | activation | after the later exp: delete the written rows (attribute_exists); FA and CW ABSENT by GSI and ConsistentRead (bounded 5 min); partner row ABSENT | four ABSENT lines | Rows deleted 03:52:27Z with attribute_exists, after the later exp 03:52:22Z (FA users, CW users, FA partner); FA and CW ABSENT by the email-index GSI and by ConsistentRead (4 of 4 lines in SITTING_REMOVAL.txt) and the partner row ABSENT; re-read independently by this seat afterwards. The synthetic ticket stays (no delete route): TCK-20261014-2965a5e0, open, 49financial, package and report_ref set. | CLOSED 20261014T035431Z |

## Log

- 20261014T033204Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
- 20261014T035431Z LEG M closed: Step 1: COO half hash e9bb20d7fe (AMENDMENTS 1 and 2 read); irpt-status, opal-ticket-api, irpt-ycharts-generate at their
- 20261014T035431Z LEG T4 closed: T4a 201 (ticket in the five-member view, no answers or attachment echoed); T4b 400 with the item count 31 -> 31; LIST-A 
- 20261014T035431Z LEG D closed: D1 to D4 all FAIL: each of the four posts as FA was refused NOT_AUTHORIZED (HTTP 200 refusal envelope, identical body sh
- 20261014T035431Z LEG P5 closed: PKG-1 200, report_ref set once {request_id, revision 1, recorded_by svc-irpt-packager, recorded_at} read back by Consist
- 20261014T035431Z LEG X closed: Rows deleted 03:52:27Z with attribute_exists, after the later exp 03:52:22Z (FA users, CW users, FA partner); FA and CW 
- 20261014T035431Z CLOSED -- all 5 legs proven
