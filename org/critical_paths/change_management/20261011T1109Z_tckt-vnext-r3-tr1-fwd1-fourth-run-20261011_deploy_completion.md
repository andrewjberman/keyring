# Deploy Completion Record
**Date opened:** 2026-10-11T11:09:18.669248+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R3-tr-1: the FOURTH run of the FWD-1 journey on DEV, runner at 83b4f0c597 (blob 8f9e6ec5), one run, one 30-min token, firm 49financial only; two-step cleanup, the row lives two hours after an accepted submission
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | the pin, the prechecks and the pair's section-6 conditions, before any write | runner committed blob sha256 reads 8f9e6ec58abeac8e9cd8970479621b819ff6f847ba16cf0e7315a69cf67759d6 and the working file matches; r3_checks.py rn-row and rn-regress both OK; clamp_precheck.py --out <r3_tr1 path> reads READ27 27/27; irpt-status live CodeSha256 starts Iw3FADFr (it MOVED since run 3); opal-ticket-api starts t1EoiJRZ; TICKET_DL_MAP key count plus recipient COUNT and DOMAINS only; the filer row ABSENT by ConsistentRead; the st30 V1 install output named with its path and read green; the dead-letter read named; and the open-deploy union re-taken at one fresh instant with its per-tree denominator over FIVE names including the resident |  | OPEN |
| L1 | activation | ONE invocation of fwd1_run.py at the new pin: row, token, census, hops a-g, both report-route arms, the zero-call read at exp+300s | the return code (0 complete and row removed, 3 accepted and row LEFT with cleanup owed, 1 failure, 2 trace exists) and the last 30 output lines, and the trace at deliverables/r3_tr1/r3_tr1_run4_trace.json which must not exist beforehand |  | OPEN |
| L2 | verify | the after-reads the runner does not do, and the branch | from the trace: result, each hop, hop (d)'s http_status + status_state + status_public_reason_code + its three key lists + accepted_state if accepted (CTO condition 4), both arms, job_last_read, the zero-call block and verdict, the cleanup block (state, row_left_in_place, row_delete_not_before); what the run leaves under 49financial BY ID named as immutable test artifacts in a client firm's store (CTO condition 5); every WE_DL_* and WE_CLIENT_* line as tokens and counts with no recipient inferred and WE_DL_SENT on an empty map a BLOCKING row; the first refused answer's code as served, classed public or internal |  | OPEN |
| L3 | verify | cleanup proven -- step 6 on return code 3, step 7 on return code 0 | on rc 3: my own ConsistentRead reads PRESENT right after the run, then ONE --finish-cleanup no earlier than row_delete_not_before (rc 4 ROW_DELETE_TOO_EARLY is expected, not a failure), then my own ConsistentRead reads ABSENT; on rc 0: my own ConsistentRead reads ABSENT. The ledger closes only after that absent read |  | OPEN |

## Log

- 20261011T110918Z OPENED by 0.7.0_AE_CloudOps~TV2 with 4 leg(s)
