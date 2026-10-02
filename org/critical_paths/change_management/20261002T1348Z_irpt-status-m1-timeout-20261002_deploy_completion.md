# Deploy Completion Record
**Date opened:** 2026-10-02T13:48:36.659897+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T140400Z
**Deploy:** S270 M1: irpt-status timeout 15 -> 29 s, one line (CTO batch 171); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | verify | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this | timeout 29 read back, CodeSha256 unchanged | before-read 13:56:46Z timeout 15, CodeSha256 BNe2n9cV; fresh targeted plan timeout 15 -> 29 only (plan_m1_d1.txt); HALT_ACK safe-apply 0/1/0 (apply_m1.txt); read back 14:00:48Z timeout 29, CodeSha256 BNe2n9cV unchanged, Successful | CLOSED 20261002T140400Z |
| V1 | verify | a cold default-page history answers 200 | REPORT and Init durations read | cold default-page history HTTP 200, 22 items, REPORT 15066.11 ms, Init 145.69 ms (was 15000 ms timed out, HTTP 500); warm limit=50 9792.75 ms; single read 732.27 ms; status 3920.14 ms (S270/S270_TIMING_AFTER_M1_20261002.json). Mitigation only: cold history is over the 10 s bar -> M2 | CLOSED 20261002T140400Z |

## Log

- 20261002T134836Z OPENED by 2.0.0_SA_COO~Y with 2 leg(s)
- 20261002T140400Z LEG D1 closed: before-read 13:56:46Z timeout 15, CodeSha256 BNe2n9cV; fresh targeted plan timeout 15 -> 29 only (plan_m1_d1.txt); HALT_
- 20261002T140400Z LEG V1 closed: cold default-page history HTTP 200, 22 items, REPORT 15066.11 ms, Init 145.69 ms (was 15000 ms timed out, HTTP 500); war
- 20261002T140400Z CLOSED -- all 2 legs proven
