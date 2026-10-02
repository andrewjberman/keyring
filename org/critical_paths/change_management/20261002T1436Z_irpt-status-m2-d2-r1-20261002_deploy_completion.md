# Deploy Completion Record
**Date opened:** 2026-10-02T14:36:18.150096+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T181604Z
**Deploy:** irpt-status at ONE commit b789341289: S270 M2 (bounded per-row pool + 1024 MB) and hop 11 D2 (SigV4 signer), then hop 11's route R1 (CTO batches 170, 171, 174); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip new version | read back by version, sha equal; census vs live | irpt-status.zip version ZmF_dRrw9PUki9V1DCyxYFvRvYB22GVx (14:24:18Z, 336416 bytes) read back sha256 6SbSkFNz9PzOO80sQqTQlBrW3zaQx1HO2QHXU55UHuw= equal; 47 members, 0 differ from the pin b789341289; census vs live BNe2n9cV: identical 43, changed 4 (S270/census_irpt-status_m2.json) | CLOSED 20261002T143618Z |
| D1 | tf-lambda | ONE targeted safe-apply of the function (memory + code) | memory 1024, CodeSha256 6SbSkFNz read back; V1-a REPORT <= 10 s every page size | safe-apply 17:04Z 1 changed; read back CodeSha256 h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg= (the RE-CUT artifact wXzz3_ghlWfn7pdM12GBxlzl_WOxYQUC at 0f70e6156e, superseding the 6SbSkFNz first artifact named in U1/proof_required), memory 1024, timeout 29, Successful (S270/M2_APPLY_OUTPUT_20261002.txt). V1-a PASS, server REPORT: history default cold 6567 ms (init 162) / warm 3372 ms; limit=50 2570 / 2578 ms; single read 404 / 256 ms; status 1122 / 1133 ms; all HTTP 200, 22 items (S270/V1A_TIMING_RUN1_20261002.json, RUN2) | CLOSED 20261002T171803Z |
| R1 | verify | ONE targeted safe-apply of the pdf route | route read back | safe-apply ~17:59Z of targeted plan S270/plan_r1_m2.txt (1 to add; full api plan S270/plan_api_r1_full.txt 1 to add, nothing else): Creation complete [id=ihirb2s], Apply complete 1 added 0 changed 0 destroyed (S270/apply_r1_m2.txt). Read back 18:00:33Z on api 7k3ed8px20: GET .../analysis/requests/{requestId}/pdf target integrations/8ogp332 CUSTOM authorizer naqxlm (S270/R1_READBACK_20261002.txt) | CLOSED 20261002T180130Z |
| V1 | verify | hop11_pdf_proof MATCH on 4 READY requests; plain reads equal | per packet section 3 | V1-b ~18:1xZ: hop11_pdf_proof MATCH 4/4 (REQ-c07e64ca, REQ-59b42fab, REQ-abec171d, REQ-a69e5751): HTTP 200, host opal-data-irpt.s3.us-east-1.amazonaws.com, X-Amz-Expires 300, expires_in on the AWS clock 295-298 s, %PDF- body sha256+length equal the claim (S270/V1B_HOP11_PDF_20261002.json). First run graded MISMATCH on the expiry only (laptop clock 301-302 s; w32time stopped, AWS Date 2.6-3.6 s ahead; bytes equal; S270/V1B_HOP11_PDF_LAPTOPCLOCK_20261002.json); the instrument now grades on the download's Date header. e7b_read_proof --compare vs HOP11_STATUS/READS_AFTER_HOP11_20261002.json: 8/8 equal (history, history+client_id, read, read+include, status x2) (S270/READS_AFTER_M2_R1_20261002.json). V1-a: see D1. | CLOSED 20261002T181502Z |

## Log

- 20261002T143618Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T143618Z LEG U1 closed: irpt-status.zip version ZmF_dRrw9PUki9V1DCyxYFvRvYB22GVx (14:24:18Z, 336416 bytes) read back sha256 6SbSkFNz9PzOO80sQqTQ
- 20261002T171803Z LEG D1 closed: safe-apply 17:04Z 1 changed; read back CodeSha256 h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg= (the RE-CUT artifact wXzz
- 20261002T180130Z LEG R1 closed: safe-apply ~17:59Z of targeted plan S270/plan_r1_m2.txt (1 to add; full api plan S270/plan_api_r1_full.txt 1 to add, not
- 20261002T181502Z LEG V1 closed: V1-b ~18:1xZ: hop11_pdf_proof MATCH 4/4 (REQ-c07e64ca, REQ-59b42fab, REQ-abec171d, REQ-a69e5751): HTTP 200, host opal-da
- 20261002T181604Z CLOSED -- all 4 legs proven
