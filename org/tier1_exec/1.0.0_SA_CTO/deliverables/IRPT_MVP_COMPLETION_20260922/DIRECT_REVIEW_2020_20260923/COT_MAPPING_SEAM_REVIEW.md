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


## Closure - actual source paired with latest P

M9b3fb2a8a27701d141fff97e47cf7658cb44bdfb paired with
P5765ea21a564cbbfd4eefaf8e84a44c13dbf94a2 closes M-P-MAP-01.
CTO ran the exact M callback over real S3, verified version/hash receipt, and fed its
actual output to the latest P requests_for. Both request shapes pass; source_revision
is the exact object digest string and full versioned source_provenance remains.
No vendor I/O or cloud writes. COT_MAPPING_REPAIR_PROOF.json preserves the receipt.
P5765 packages the older M614 mapper; use the corrected9b3 mapper for final package.
P's extra dict compatibility does not redefine the current string interface.
