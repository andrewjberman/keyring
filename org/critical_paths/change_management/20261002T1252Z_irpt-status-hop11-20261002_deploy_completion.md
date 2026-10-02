# Deploy Completion Record
**Date opened:** 2026-10-02T12:52:54.552787+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T133446Z
**Deploy:** hop 11 on irpt-status: IAM vendor_documents line, code at ONE commit 38986d35bb (hop 11 + item 22 served + batch 154 guard + IB-pr-293 riding), the API route GET .../requests/{requestId}/pdf (CTO batches 123, 154, 163); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip new version on opal-313476888478-lambda-artifacts/investor-reporting | read back by version, sha equal; census vs live | irpt-status.zip version 9S5jAZLrUIb7OsqZW_jkSSc9HjI63f5E (12:12:48Z, 335359 bytes) read back sha256 BNe2n9cV2tgsXE7pNy295NEhbiQsFM0VRE8OXeaolZU= equal; 47 members, 0 differ from the pin 38986d35bb; census vs live X/JLmPJZ: identical 41, changed 5, added 1 (HOP11_STATUS/census_irpt-status_hop11.json) | CLOSED 20261002T125254Z |
| I1 | verify | ONE targeted safe-apply of aws_iam_role_policy.irpt_status | the three vendor_documents resources added, nothing else; policy read back | LANDED-VERIFIED: targeted plan 1 change (plan_i1.txt), safe-apply 0/1/0 (apply_i1.txt); read back: ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly carries irpt/{inflection,cottonwood,49financial}/state/vendor_documents/* (i1_readback.txt) | CLOSED 20261002T133445Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this | code move only; CodeSha256 BNe2n9cV read back | LANDED-VERIFIED: render ports at the pin NONE (RENDER_PORTS_AT_PIN_20261002.txt, the CTO half's added stop); targeted plan code move only (plan_d1.txt); safe-apply 0/1/0; live CodeSha256 BNe2n9cV2tgsXE7pNy295NEhbiQsFM0VRE8OXeaolZU= since 13:12:18Z; plain reads equal to before, history differing only by the 2 new arms requests (20 common items equal); item 22 serves (history client_id unknown -> items []) | CLOSED 20261002T133445Z |
| R1 | verify | ONE targeted safe-apply of the pdf API route | 1 to add; route read back on 7k3ed8px20 | ROLLED BACK: created 13:1xZ (route rz8ukjs, integrations/8ogp332, CUSTOM); destroyed 13:2xZ after V1's PDF download failed (plan_r1_rollback.txt, apply_r1_rollback.txt); 0 /pdf routes on 7k3ed8px20 read back. CTO batch 170 keeps I1/D1 | CLOSED 20261002T133446Z |
| V1 | verify | hop11_pdf_proof MATCH on READY requests; item 22 served; plain reads equal | per packet section 3 | HOP 11 NOT SERVED: the route answered 200 with a SigV2 presigned URL (AWSAccessKeyId/Signature/Expires); S3 refused the download 400 InvalidArgument 'Requests specifying Server Side Encryption with AWS KMS managed keys require AWS Signature Version 4'. Item 22 and the guard SERVED. Fix forward: D2 (s3v4 signer) + R1 again under a new half (CTO batch 170) | CLOSED 20261002T133446Z |

## Log

- 20261002T125254Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261002T125254Z LEG U1 closed: irpt-status.zip version 9S5jAZLrUIb7OsqZW_jkSSc9HjI63f5E (12:12:48Z, 335359 bytes) read back sha256 BNe2n9cV2tgsXE7pNy29
- 20261002T133445Z LEG I1 closed: LANDED-VERIFIED: targeted plan 1 change (plan_i1.txt), safe-apply 0/1/0 (apply_i1.txt); read back: ReadRetainedAnalysisF
- 20261002T133445Z LEG D1 closed: LANDED-VERIFIED: render ports at the pin NONE (RENDER_PORTS_AT_PIN_20261002.txt, the CTO half's added stop); targeted pl
- 20261002T133446Z LEG R1 closed: ROLLED BACK: created 13:1xZ (route rz8ukjs, integrations/8ogp332, CUSTOM); destroyed 13:2xZ after V1's PDF download fail
- 20261002T133446Z LEG V1 closed: HOP 11 NOT SERVED: the route answered 200 with a SigV2 presigned URL (AWSAccessKeyId/Signature/Expires); S3 refused the 
- 20261002T133446Z CLOSED -- all 5 legs proven
