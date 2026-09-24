# X10 enforcement matrix -- 2026-09-24 (2.0.0_SA_COO~P)

Policy irpt-x10-v1, state PENDING_ENFORCEMENT, policy_sha256 cb9c4e6e9541fefc315f57844490309ad15c9735593fe3a165b067a3087dc220. Destinations 36 (3 firms x 12 families, opal_naming preview). Live IAM swept 2026-09-24T01:1xZ: 18 of 18 irpt-* roles; 1 statement names opal-data-irpt. LIVE = a deployed role holds s3:PutObject on the exact prefix; DECLARED = address exists, no deployed writer. Bucket objects: 0.

| firm | family | tier/table | prefix | status | deployed writer |
|---|---|---|---|---|---|
| 49financial | ANALYSIS | platinum/analysis_reports | irpt/49financial/platinum/analysis_reports/ | DECLARED | - |
| 49financial | EXPORT_BUNDLE | state/export_bundles | irpt/49financial/state/export_bundles/ | DECLARED | - |
| 49financial | EXPORT_PDF | state/export_pdfs | irpt/49financial/state/export_pdfs/ | DECLARED | - |
| 49financial | EXPORT_RECEIPT | state/export_receipts | irpt/49financial/state/export_receipts/ | DECLARED | - |
| 49financial | EXTRACTION_EVIDENCE | state/extraction_evidence | irpt/49financial/state/extraction_evidence/ | DECLARED | - |
| 49financial | NORMALIZED_PORTFOLIO | state/normalized_portfolios | irpt/49financial/state/normalized_portfolios/ | DECLARED | - |
| 49financial | ORIGINAL_CSV | state/prospect_inputs | irpt/49financial/state/prospect_inputs/ | DECLARED | - |
| 49financial | ORIGINAL_VENDOR_PDF | state/vendor_documents | irpt/49financial/state/vendor_documents/ | DECLARED | - |
| 49financial | PERFORMANCE | platinum/performance_reports | irpt/49financial/platinum/performance_reports/ | DECLARED | - |
| 49financial | PERFORMANCE_SOURCE_EVIDENCE | state/performance_source_evidence | irpt/49financial/state/performance_source_evidence/ | DECLARED | - |
| 49financial | REQUEST_COMPOSITION | state/request_compositions | irpt/49financial/state/request_compositions/ | DECLARED | - |
| 49financial | SELECTED_ACCOUNTS | state/selected_accounts | irpt/49financial/state/selected_accounts/ | DECLARED | - |
| cottonwood | ANALYSIS | platinum/analysis_reports | irpt/cottonwood/platinum/analysis_reports/ | DECLARED | - |
| cottonwood | EXPORT_BUNDLE | state/export_bundles | irpt/cottonwood/state/export_bundles/ | DECLARED | - |
| cottonwood | EXPORT_PDF | state/export_pdfs | irpt/cottonwood/state/export_pdfs/ | DECLARED | - |
| cottonwood | EXPORT_RECEIPT | state/export_receipts | irpt/cottonwood/state/export_receipts/ | DECLARED | - |
| cottonwood | EXTRACTION_EVIDENCE | state/extraction_evidence | irpt/cottonwood/state/extraction_evidence/ | DECLARED | - |
| cottonwood | NORMALIZED_PORTFOLIO | state/normalized_portfolios | irpt/cottonwood/state/normalized_portfolios/ | DECLARED | - |
| cottonwood | ORIGINAL_CSV | state/prospect_inputs | irpt/cottonwood/state/prospect_inputs/ | DECLARED | - |
| cottonwood | ORIGINAL_VENDOR_PDF | state/vendor_documents | irpt/cottonwood/state/vendor_documents/ | DECLARED | - |
| cottonwood | PERFORMANCE | platinum/performance_reports | irpt/cottonwood/platinum/performance_reports/ | LIVE | irpt-performance-adapter-role |
| cottonwood | PERFORMANCE_SOURCE_EVIDENCE | state/performance_source_evidence | irpt/cottonwood/state/performance_source_evidence/ | LIVE | irpt-performance-adapter-role |
| cottonwood | REQUEST_COMPOSITION | state/request_compositions | irpt/cottonwood/state/request_compositions/ | DECLARED | - |
| cottonwood | SELECTED_ACCOUNTS | state/selected_accounts | irpt/cottonwood/state/selected_accounts/ | DECLARED | - |
| inflection | ANALYSIS | platinum/analysis_reports | irpt/inflection/platinum/analysis_reports/ | DECLARED | - |
| inflection | EXPORT_BUNDLE | state/export_bundles | irpt/inflection/state/export_bundles/ | DECLARED | - |
| inflection | EXPORT_PDF | state/export_pdfs | irpt/inflection/state/export_pdfs/ | DECLARED | - |
| inflection | EXPORT_RECEIPT | state/export_receipts | irpt/inflection/state/export_receipts/ | DECLARED | - |
| inflection | EXTRACTION_EVIDENCE | state/extraction_evidence | irpt/inflection/state/extraction_evidence/ | DECLARED | - |
| inflection | NORMALIZED_PORTFOLIO | state/normalized_portfolios | irpt/inflection/state/normalized_portfolios/ | DECLARED | - |
| inflection | ORIGINAL_CSV | state/prospect_inputs | irpt/inflection/state/prospect_inputs/ | DECLARED | - |
| inflection | ORIGINAL_VENDOR_PDF | state/vendor_documents | irpt/inflection/state/vendor_documents/ | DECLARED | - |
| inflection | PERFORMANCE | platinum/performance_reports | irpt/inflection/platinum/performance_reports/ | DECLARED | - |
| inflection | PERFORMANCE_SOURCE_EVIDENCE | state/performance_source_evidence | irpt/inflection/state/performance_source_evidence/ | DECLARED | - |
| inflection | REQUEST_COMPOSITION | state/request_compositions | irpt/inflection/state/request_compositions/ | DECLARED | - |
| inflection | SELECTED_ACCOUNTS | state/selected_accounts | irpt/inflection/state/selected_accounts/ | DECLARED | - |

Totals: LIVE 2 / DECLARED 34 of 36.

Not covered here: bucket policy, KMS key policy, permission boundaries; the retention arms (CTO); the EXERCISED arm (first live reserve -> promote -> reopen, CALL-3 after ACTIVE).
ACTIVE requires: CTO acceptance in one review; M writes state ACTIVE + enforcement_ref = accepting commit in reporting_policies.json; then the CALL-3 plan and the first live receipts.
