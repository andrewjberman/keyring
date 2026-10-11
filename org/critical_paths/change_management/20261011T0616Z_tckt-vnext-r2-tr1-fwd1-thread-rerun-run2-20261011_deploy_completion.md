# Deploy Completion Record
**Date opened:** 2026-10-11T06:16:09.093557+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R2-tr-1 SECOND GO (AMENDMENT 1 @bc3a095fd2): the FWD-1 thread re-run on DEV, one run, one token, firm 49financial only, runner at 2d2b309be9
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | the prechecks and the pin, before any write | runner sha256 reads 10f1abb9...9557; rn-safety, rn-zero and rn-arms all OK; opal-ticket-api live CodeSha256 starts W03VREoM; irpt-status live starts 6idtFvAm; TICKET_DL_MAP key count plus recipient COUNT and DOMAINS only for the row 49financial resolves to; reread_27.py at bc3a095fd2 reads READ27 27/27 (anything else is Branch D again); the open-deploy union re-taken at a single fresh instant with its per-tree denominator |  | OPEN |
| L1 | activation | ONE invocation of fwd1_run.py: row, token, census, hops a-g, both report-route arms, cleanup | the runner's rc and its last 30 output lines, and the trace at deliverables/r2_tr1/r2_tr1_trace.json (which must not exist beforehand) |  | OPEN |
| L2 | verify | the after-reads the runner does not do | per-hop results and both arms from the trace; the zero-call block's three numbers per group and its verdict (0 streams searched is VOID, control >= 1, matches == 0); token_exp and row_deleted_at; CTO condition 5's retained request id, report id and upload id; every WE_DL_* and WE_CLIENT_* line over iat..exp as tokens and counts; the first refused answer's reason code quoted as served and classed public or internal |  | OPEN |
| L3 | verify | cleanup proven, independent of the runner's own read | my own ConsistentRead of the filer row reads ABSENT after the process exits, and the delete time is later than the token exp |  | OPEN |

## Log

- 20261011T061609Z OPENED by 0.7.0_AE_CloudOps~TV2 with 4 leg(s)
