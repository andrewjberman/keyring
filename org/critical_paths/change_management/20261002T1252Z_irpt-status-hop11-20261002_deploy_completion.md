# Deploy Completion Record
**Date opened:** 2026-10-02T12:52:54.552787+00:00
**Status:** OPEN
**Deploy:** hop 11 on irpt-status: IAM vendor_documents line, code at ONE commit 38986d35bb (hop 11 + item 22 served + batch 154 guard + IB-pr-293 riding), the API route GET .../requests/{requestId}/pdf (CTO batches 123, 154, 163); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip new version on opal-313476888478-lambda-artifacts/investor-reporting | read back by version, sha equal; census vs live | irpt-status.zip version 9S5jAZLrUIb7OsqZW_jkSSc9HjI63f5E (12:12:48Z, 335359 bytes) read back sha256 BNe2n9cV2tgsXE7pNy295NEhbiQsFM0VRE8OXeaolZU= equal; 47 members, 0 differ from the pin 38986d35bb; census vs live X/JLmPJZ: identical 41, changed 5, added 1 (HOP11_STATUS/census_irpt-status_hop11.json) | CLOSED 20261002T125254Z |
| I1 | verify | ONE targeted safe-apply of aws_iam_role_policy.irpt_status | the three vendor_documents resources added, nothing else; policy read back |  | OPEN |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this | code move only; CodeSha256 BNe2n9cV read back |  | OPEN |
| R1 | verify | ONE targeted safe-apply of the pdf API route | 1 to add; route read back on 7k3ed8px20 |  | OPEN |
| V1 | verify | hop11_pdf_proof MATCH on READY requests; item 22 served; plain reads equal | per packet section 3 |  | OPEN |

## Log

- 20261002T125254Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261002T125254Z LEG U1 closed: irpt-status.zip version 9S5jAZLrUIb7OsqZW_jkSSc9HjI63f5E (12:12:48Z, 335359 bytes) read back sha256 BNe2n9cV2tgsXE7pNy29
