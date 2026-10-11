# TCKT_VNEXT round 2, cell R2-rr-2 -- L9 grade of TO-APPLY-R2-rr2 AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T04:50:50Z, on `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R2_RR2.md @16fcc87ae6 (msg 4098)`. Row TCKT_VNEXT-D2-S26.

| criterion | verdict | this seat's evidence |
|---|---|---|
| AC2: "the deployed bytes are the pinned file, and nothing else moved" | **MET** | This seat downloaded the live `opal-ticket-api` package. Its sha256 (base64 `W03VREoM...`) equals the live CodeSha256. It holds 1 member, `lambda_function.py`, 89,575 bytes, sha256 `ca3be343...`, byte-equal to `git show a366ce52ec:infra/aws/lambda/ticket_center/lambda_function.py`. Negative control: the pin's parent bytes do not equal the member |

## Nothing else moved

- **Code:** the deployed file before the apply hashed `67068626...` (the ledger's STOP 2). That is the file at `eb80f55340`
  (this seat's hash of that blob: `67068626...`). The diff from it to the pin is 4 added lines: the `REPORT_REQUEST_ID` pattern and
  the 400 `INVALID_REPORT_REQUEST_ID` refusal. No other line of the handler changed.
- **Configuration, read live:** runtime python3.11, handler `lambda_function.lambda_handler`, memory 256, timeout 30, the role
  `opal-ticket-api-role`, 8 environment keys. Runtime, handler, memory and timeout equal the Terraform file. LastModified
  2026-10-11T04:19:14Z, one update.

## Not graded here

- The applier's plan shape, the control ticket's 23 fields and the replan are its report. This seat did not re-run them.
- Both live arms of the new check (a well-formed id stored, a malformed one refused) belong to cell R2-tr-1. The check is APPLIED,
  not exercised.
- This deploy answers the round-1 finding (row D2-S21: the report route stored an id the read plane refuses). It does not make
  FWD-1 pass: the runner still has to take the request id from the submission's answer.
