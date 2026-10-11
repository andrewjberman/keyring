# Deploy Completion Record
**Date opened:** 2026-10-11T08:06:55.813314+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R2-tr-1 THIRD AND LAST GO (AMENDMENT 2 @f0d4c2db95, CTO half @4a0e63f033): the FWD-1 thread re-run, runner at f4153fc637 with a per-run idempotency token, one run, firm 49financial only
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | the prechecks, the new pin and the CTO pre-GO placement, before any write | runner sha256 reads f8ef2b1f6630bfe8071d3395d99048f2d0a34dbbd7b3cdc949c1227cd0c62bb4; r2_checks.py rn-safety, rn-token and rn-zero3 all print OK; opal-ticket-api live CodeSha256 starts W03VREoM; irpt-status live starts 6idtFvAm; TICKET_DL_MAP key count plus recipient COUNT and DOMAINS only; reread_27.py reads READ27 27/27; the open-deploy union re-taken at a single fresh instant with its denominator; and CTO AMENDMENT 3's pre-GO condition -- the 06:22:18 MISSING_REQUEST_FIELD event PLACED with its line |  | OPEN |
| L1 | activation | ONE invocation of fwd1_run.py at f4153fc637: row, token, census, hops a-g, both report-route arms, cleanup | the runner's rc and its last 30 output lines, and the trace at deliverables/r2_tr1/r2_tr1_run3_trace.json (which must not exist beforehand); the per-run idempotency_token as traced, shown to differ from run 2's sar1b- value |  | OPEN |
| L2 | verify | the after-reads the runner does not do | per-hop results and both arms from the trace; the zero-call block's three numbers and latest_event_time as PRINTED (CTO AMENDMENT 3 part 2: streams_active_in_window==0 is ZERO-CALLS-PROVEN on its own when the read is >=5 min after the window closes and the group's most recent event time is real and outside it); token_exp and row_deleted_at; the WE_CLIENT_* and WE_DL_* counts per run ticket as tokens and counts with NO recipient inferred, and WE_DL_SENT on an empty map still a BLOCKING row; the served refusal code quoted exactly, and for a branch E the service's own reason token from /aws/lambda/irpt-ycharts-generate; for branch A, CTO condition 5's ids |  | OPEN |
| L3 | verify | cleanup proven, independent of the runner's own read | my own ConsistentRead of the filer row reads ABSENT after the process exits, and the delete time is later than the token exp |  | OPEN |

## Log

- 20261011T080655Z OPENED by 0.7.0_AE_CloudOps~TV2 with 4 leg(s)
