# Holdings actual user journey: FAIL

Andrew reports localhost5174, Cottonwood Anna ****9237/BROKERAGE: resolved selected
one account,1of1 in scope (842permitted), exact scope match, directory2026-09-17,
scope asofunknown. The page lists account IDs acc_0698a3de842dbe7b3d48c787 and
acc_d486fc9455d6b2aa18e13af1. Holdings shows Unavailable / No source age yet /
NOT_READY [code not defined by the v1 contract] / Contact support.
This contradicts live-journey completion; prior deployment parity remains valid.

CTO read actual Lambda CloudWatch22:16Z calls: START/END/duration only, no cause
telemetry. Those logs cannot identify which selected reference/date was sent.
Actual strongly consistent DDB query found8Cottonwood selection records, no more
pages. Separate0698,d486 andcombined records exist, all directory revision38aa7846.

Actual extracted deployed bcb3 reader over S3:
- d486 default/date2026-09-22: READ_OK59nodes.
- 0698 default/date2026-09-22: selected accounts absent from accepted publication.
- combined0698+d486 default/date2026-09-22: same absent-coverage refusal.
- each selection with explicit2026-09-23: no accepted holdings revision for date.
These read-only checks prove a data coverage/date boundary, not the exact request
Andrew sent. M traces the real selection and query; no identity collapse or happy
account substitution. Prepare complete supported COT coverage, at least both Anna
accounts accounted for, preserving existing accepted publication and exact source
census/reconciliation. Publication update requires concrete CAS plan review.

Portal Page.tsx named-code list contains only CONTRACT_VERSION/ROUTE_UNKNOWN,
with generated source at58e387b454. P owns the shared public-reason contract/render
repair so unavailable data is meaningful rather than an undefined implementation
code. M owns account/data/UI diagnosis and end-to-end correction. Do not fabricate
empty holdings, infer date shifts, or ask Andrew to choose only a supported account
as a substitute for completing the product.
