# Deploy Completion Record
**Date opened:** 2026-10-02T06:13:38.885829+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T064307Z
**Deploy:** hop 3's proof on st10: an upload resolves while another job's generation is in flight (legs P, S if needed, A one Overview job, B one upload during A); window packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | ONE liveness read of the stored session from the host | PROBE_VERDICT line | HOP3_PROOF/LEG_P_OUTPUT_20261001.txt: one GET of /custom_pdf_reports/generate/14141822 through the resident's session classes, status 200 JSON, waf_action None, login False; PROBE_VERDICT=LIVE at 2026-10-02T06:24:58Z | CLOSED 20261002T062525Z |
| S1 | verify | ONE operator sign-in, only if P1 read NOT_LIVE | LEG_S_VERDICT line, or 'not run: P1 read LIVE' | not run: P1 read LIVE (no sign-in; the CTO half's 08:21Z clock was not reached) | CLOSED 20261002T062525Z |
| A1 | verify | ONE Overview attempt: one K4, one K5, the job to terminal | the out file, the job's terminal state, every receive with its time, the journal's VENDOR_REQUESTS line | H3_A_overview_cottonwood.json/.log + LEG_A_RUNNER_20261002.txt: one login, K4 UP-7b1406fd.. NORMALIZED 06:26:01, K5 REQ-93441e4e201b40e3b119c46b QUEUED 06:26:06; journal EVICTED 06:26:09, VENDOR_REQUESTS kept=1, refresh CAPTURE_FAILED CHALLENGE_CAPTCHA_UNSUPPORTED; terminal ATTENTION SESSION_REFRESH_ALREADY_USED 06:41:13; job row vendor_requests 2 records (template GET 403 x2), one per receive | CLOSED 20261002T064307Z |
| B1 | verify | ONE upload, no K5, fired while A's job is non-terminal | A's job state before and after; B's normalization state; the journal's RESOLVE line | LEG_B_RUNNER_20261002.txt + H3_B_upload_cottonwood.json: gate read A's job SUBMITTING 06:27:04; one login, one K4 UP-d3b01928.. RESOLVING 06:27:14, no K5; journal RETRY PROVIDER_READ_UNAVAILABLE:OPERATION_BUSY 06:27:16, 06:28:16, 06:29:16, ATTENTION RESOLVE_RETRY_EXHAUSTED 06:30:17; row NEEDS_CORRECTION reason RESOLVE_RETRY_EXHAUSTED; A still SUBMITTING 06:30:22 | CLOSED 20261002T064307Z |
| V1 | verify | the outcome read and written | OUTCOME file committed after its values are read | INTERIM_FINDINGS_20261002.md @8054620d91 (reported first; ruled CTO batch 120) and OUTCOME_HOP3_PROOF_20261002.md, read for values before commit | CLOSED 20261002T064307Z |

## Log

- 20261002T061338Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261002T062525Z LEG P1 closed: HOP3_PROOF/LEG_P_OUTPUT_20261001.txt: one GET of /custom_pdf_reports/generate/14141822 through the resident's session cl
- 20261002T062525Z LEG S1 closed: not run: P1 read LIVE (no sign-in; the CTO half's 08:21Z clock was not reached)
- 20261002T064307Z LEG A1 closed: H3_A_overview_cottonwood.json/.log + LEG_A_RUNNER_20261002.txt: one login, K4 UP-7b1406fd.. NORMALIZED 06:26:01, K5 REQ-
- 20261002T064307Z LEG B1 closed: LEG_B_RUNNER_20261002.txt + H3_B_upload_cottonwood.json: gate read A's job SUBMITTING 06:27:04; one login, one K4 UP-d3b
- 20261002T064307Z LEG V1 closed: INTERIM_FINDINGS_20261002.md @8054620d91 (reported first; ruled CTO batch 120) and OUTCOME_HOP3_PROOF_20261002.md, read 
- 20261002T064307Z CLOSED -- all 5 legs proven
