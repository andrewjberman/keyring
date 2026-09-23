# COT mapping consumer seam - CTO direct review

M614ad2f16b58bfc968ea26c903883afde50f9c3b paired with P9e1bc3a7514b8e092df1014e17282fbb3ce12305.
Verdict: REWORK, M-P-MAP-01, one return-field mismatch.

Exported exact M source/tests and declared unchanged P currency dependency into
isolated scratch. Called real make_cot_mapping_loader with the test's versioned
parquet S3 double, then passed its actual result directly to P bd_selected.requests_for.
Result: SelectedPerformanceRefused('source mapping evidence required') before any
vendor I/O. M returns source_revision=dict; published P contract requires nonempty
str. Standalone mapper tests assert the dict, so miss the consumer seam.

Ruling: retain P's published source_revision string contract. M returns the exact
source object's sha256 as source_revision and keeps the complete existing receipt
(bucket/key/version/hash/source_date) under additional source_provenance. P's evidence
already preserves the whole mapping; no producer receipt is discarded. One real
callback-to-P requests_for check closes this mismatch; no broad rerun required.

M reports actualS3 selected account3positions/1165.21,7receipts, schema/reconciliation
PASS in COT_SELECTED_REAL_SOURCE_20260923.json. This review did not independently
rerun the liveS3 build and does not convert that report to an E2E pass. Source7033
selected validation remains bounded accepted. Final mapping, attestation, newly
classified blank-row behavior, publication and authenticated drill remain distinct.
