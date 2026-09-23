# P artifact repository consumer review

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22, 5:30 PM Eastern.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate: `70598ece96498d639b0fb12104ffe9fd4b0d5718`.
Interface read: `INTERFACES.md` at `aacb609834` in COO P's deliverables.

## Y-P01: artifact receipt fails with DynamoDB numeric decoding

**P1 / FAIL**, owned by COO~P. The actual candidate ArtifactRepository cannot
return a receipt or retrieved artifact when its DynamoReportIndex receives the
numeric representation returned by boto3. This blocks the primitive used for Y
uploads, normalized input and protected original vendor PDFs.

`DynamoReportIndex` stores `ref.byte_length` as a number. boto3's actual
`TypeDeserializer` returns a `Decimal` for that value. `ArtifactRepository.get`
returns `_copy(ref)`; `_copy` uses `canonical` and standard `json.dumps`, which
cannot serialize the Decimal. Initial `put` publishes the blob and index, then
calls `get` and fails before returning its receipt. The identical retry and
direct `get` and `head` fail at the same boundary.

Expected: successful initial receipt, stable identical-retry receipt, and
retrievable identical bytes and metadata through the real numeric decoding.
Observed: **4/4 operations raise `TypeError: Object of type Decimal is not JSON
serializable`**. One blob and one index row remain published. Numeric positive
control: integer 7 round-trips through boto3 as Decimal.

The supplied suite independently reran **19/19 PASS, 0 skipped**. Its table
double preserves Python integer types, so it does not exercise this adapter
boundary. These counts describe separate tests and must not be added to the F
per-cell counts or treated as product acceptance.

Reproduce from workspace root:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_p_repository.py --pin 70598ece96498d639b0fb12104ffe9fd4b0d5718 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/P_REPOSITORY_70598ece96.json
```

The probe extracts three exact Git blobs into the ignored exact-seat runtime
directory. The evidence JSON records their SHA-256 hashes, the supplied suite
log, decoding control and each failing operation. It imports the actual
candidate adapters and actual installed boto3 serializer/deserializer. Table
and S3 remain synthetic; no cloud or vendor network call occurred. Probe exit 0
means evidence collection completed; the four recorded exceptions are FAIL.

Required retest: P supplies a committed repair and tests of actual DynamoDB
numeric decoding. Verify initial put, identical retry, get and head preserve
integer metadata and original immutable identity/content. Y will independently
rerun against the supplied pin. No implementation edits made by this reviewer.

## Inheritance and acceptance limits

Portal HEAD measured `8e6e2e38cc299c4415d42b0fe627edc50ec35e1b`; exact F pin
ancestry rc0. Tracked portal paths clean; untracked files exist. Workspace B
`2506c70874` and chain `4e1091f1e7` ancestry both rc0. F claims release is
CTO-reported; per-cell F test counts were not rerun or combined. Existing render
implementation remains inherited. B live/render limitations remain open.

S3/S4 artifact-repository subboundary fails on this candidate. The fourteen
integrated Y1-Y7/S1-S7 criteria remain NOT_EVALUATED; there is no completed
integrated Y candidate, deployed proof, recovery proof or E2E PASS.

CVO~P separately reports R-P05, report-index alias acceptance, at `b333db1b48`.
That finding is attributed, not independently rerun here. No alias conclusion
is inferred from the Decimal probe.

IRPT-S7-01 read at `bcd38bba00`: conditional placement covers exactly eleven
families in `opal-data-irpt`, retaining canonical firm tenancy. Canonical CRO
registration and enforcement are required before writable destinations; P must
supply concrete family retention/expiry and least-privilege IAM/IaC before live
writes. Y consumes the registered policy and verifies its actual writes. The
ruling supplies no product PASS or live authorization.

Compiler: bare comp-which followed by comp-read for exact artifacts; Git blobs
read at pins, actual unittest suite and independent adapter probe executed.
Push state LOCAL; no push by this seat. Origin CLOUD observed at
`b333db1b4865619909c916741775084396e0b7d1` during this review.

-- 3.0.0_SA_CVO~Y
