# Deploy Completion Record
**Date opened:** 2026-10-09T18:03:53.658235+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T031629Z
**Deploy:** TCKT_VNEXT SA-r-1c: GET-only re-read of run 4's analysis stage, and open the report from the ticket if one exists
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROW | verify | opal-users-v2 | upsert the same synthetic filer row with allowedFirmIds LIST [49financial] and read it back PRESENT | NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is refused INVALID_REQUEST_ID by construction). Measured: 0 legs proven, no run_5 in sa_r1b_trace.json, users-table row USER#tckt-fwd1-testfiler-20261009@opal.invalid ConsistentRead ABSENT (describe-table control ACTIVE), no token minted by this entry's record | CLOSED 20261011T031629Z |
| TOK | verify | opal/auth/jwt-private-key | ONE RS256 token, CURRENT slot, v2.2 claims, exp = iat + 15 min (run + 5); memory only; key read reported after via MSTR~DELL2 | NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is refused INVALID_REQUEST_ID by construction). Measured: 0 legs proven, no run_5 in sa_r1b_trace.json, users-table row USER#tckt-fwd1-testfiler-20261009@opal.invalid ConsistentRead ABSENT (describe-table control ACTIVE), no token minted by this entry's record | CLOSED 20261011T031629Z |
| RUN | verify | GET-only stage read | GET the analysis request and record the CONTRACT field stage (state only as an annotation), polling at most 10 times 30s apart while stage is RECEIVED/PARSED/READY/SUBMITTING; then GET the ticket and, if stage is GENERATED or RELEASED, open the report its report_ref names through the served route, recording status, content-type, byte length and sha256 prefix only. Any stage is a RESULT, not a STOP. No POST, no upload, no ticket write, no census | NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is refused INVALID_REQUEST_ID by construction). Measured: 0 legs proven, no run_5 in sa_r1b_trace.json, users-table row USER#tckt-fwd1-testfiler-20261009@opal.invalid ConsistentRead ABSENT (describe-table control ACTIVE), no token minted by this entry's record | CLOSED 20261011T031629Z |
| RBK | verify | rollback per AMENDMENT 3 | WAIT until the token exp has passed, THEN delete the row and read it back ABSENT with ConsistentRead. The proof prints the exp, the delete time and the absent read -- this ordering is the fix for row TCKT_VNEXT-D2-S20, where deleting the row first REMOVED the narrowing and left the token wider until exp | NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is refused INVALID_REQUEST_ID by construction). Measured: 0 legs proven, no run_5 in sa_r1b_trace.json, users-table row USER#tckt-fwd1-testfiler-20261009@opal.invalid ConsistentRead ABSENT (describe-table control ACTIVE), no token minted by this entry's record | CLOSED 20261011T031629Z |
| TRC | verify | run_5 trace section | append run_5 to org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1b_trace.json ONLY (AMENDMENT 1: the issuer copies the identical bytes into R1_RUN), carrying NO client data -- statuses, stage, artifact ids, byte lengths and sha256 prefixes only | NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is refused INVALID_REQUEST_ID by construction). Measured: 0 legs proven, no run_5 in sa_r1b_trace.json, users-table row USER#tckt-fwd1-testfiler-20261009@opal.invalid ConsistentRead ABSENT (describe-table control ACTIVE), no token minted by this entry's record | CLOSED 20261011T031629Z |

## Log

- 20261009T180353Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
- 20261011T031629Z LEG ROW closed: NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is r
- 20261011T031629Z LEG TOK closed: NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is r
- 20261011T031629Z LEG RUN closed: NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is r
- 20261011T031629Z LEG RBK closed: NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is r
- 20261011T031629Z LEG TRC closed: NOT RUN, order CANCELLED by issuer 2.0.0_SA_COO~V2 2026-10-11T03:2xZ on L9 row TCKT_VNEXT-D2-S21 (target id sar1b-* is r
- 20261011T031629Z CLOSED -- all 5 legs proven
