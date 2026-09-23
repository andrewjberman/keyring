# Owned AnalysisReport reader review

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026 Eastern.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact candidate: `9ac485733e365452960b47d18cf0fba04ef73f7e`.

Result: **44 supplied tests PASS; independent 11 PASS / 1 FAIL**.
**Y-R01 P2 OPEN**: a malformed numeric certification digest in a persisted READY
receipt is accepted by the reader, although the canonical writer requires a string.
This is a bounded receipt-validation finding, not demonstrated unauthorized
access or live publication bypass. Integrated criteria remain
**0 PASS / 0 FAIL / 14 NOT_EVALUATED**.

## Y-R01 reproduction and evidence

The actual `DynamoGenerationStore.put_state(..., 'READY', detail)` requires
report_id, revision and certification_sha256 to be nonempty strings. The reader
instead applies its digest regex to `str(detail.get(k, ''))`. For
certification_sha256, the original value is never used subsequently, so coercion
silently admits a JSON number whose decimal spelling consists of 64 hex digits.

Independent paired controls use the same accepted request, retained report,
owner, composition hash, report ID and revision:

1. Set certification_sha256 to the string containing 64 `1` characters: the
   reader returns the complete synthetic schema-valid report as expected.
2. Set it to `int('1' * 64)`, serialize/deserialize it through actual job_detail
   JSON, and repeat the read: the reader again returns the complete report.
   **Expected:** READY_REPORT_RECEIPT_REQUIRED before report retrieval.
3. Pass the same numeric detail to actual DynamoGenerationStore.put_state:
   CERTIFIED_REPORT_RECEIPT_REQUIRED, before any write/lease operation.
4. Omit certification_sha256: the reader correctly refuses before report fetch.

The normal canonical writer cannot produce this numeric receipt. The negative
control injects malformed persisted metadata, testing the reader's own stated
receipt validation. There is no demonstrated path for an untrusted HTTP caller
to set this record, no owner bypass, and no claim that the synthetic report was
ever certified by the real pipeline. Severity P2 applies to this bounded read
contract. Repair should enforce the existing string types before regex matching;
the original paired controls should remain unchanged for retest.

## Executed evidence

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_owned_report.py --pin 9ac485733e --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/OWNED_REPORT_9ac485733e.json
```

The probe archives the exact IRPT source/contracts/registry into the ignored
seat runtime directory and records SHA-256 for each source. It composes actual
OwnedAnalysisReader, OwnedRequestReader, DynamoAcceptance, DynamoGenerationStore
and P retained repositories/schema with supplied offline storage, clock and
ACTIVE-policy fixtures. Socket connections are forbidden in both processes.
The report fixture is explicitly synthetic; its retained source dependency is
real within the offline repository composition. This is not vendor/certifier
publication evidence or runtime installation.

Supplied tests: `test_owned_report.py` (15), `test_owned_requests.py` (18),
`test_retained_uploads.py` (11): **44 PASS**, one combined denominator. The first
independent run completed with **11 PASS / 1 FAIL**, exit1 for the preserved
negative assertion. No test scenario or implementation was changed after that
result. JSON retains supplied output, source hashes and all control results.

Other independent checks passed:

- Complete report matches the repository fixture; returned copy mutation does
  not change a later read.
- READY receipt changes after the report blob, including only a changed digest,
  refuse with READY_REPORT_CHANGED.
- Accepted record change after report read refuses ACCEPTED_RECORD_CHANGED.
- Report retention-reference substitution refuses REPORT_RETENTION_BINDING.
- Loss of the report source retention row refuses RetentionExpired.
- Loss of the composition retention service refuses RETENTION_SERVICE_REQUIRED.
- Current accepted-owner authorization loss refuses REQUEST_UNAVAILABLE.
- Wrong owner produces zero blob and job reads.

The string positive, canonical-writer negative and missing-digest negative are
included in the 11 passing checks, not additional denominators.

## Boundaries and peer update

Final job/index/authorization/retention checks are sequential, not an atomic
snapshot. This review does not establish the real certifier's receipt provenance,
report input economics, HTTP access, deployed retention/IAM, browser reload,
vendor execution or released report/export flow. All 14 integrated criteria
remain NOT_EVALUATED while Y-R01 remains a separate primitive finding.

Exact CVO~M notice 20260923T001008Z is informational peer evidence:
review95d2117e97 reports nine verified source versions, custody7522 roots matching
IN_CLIENT_BOOK versus overlay5917, with1622 custody-only and17 overlay-only.
Custody09-21 and SmartX09-22 cannot be economically spliced or certify Y's
normalized custody port. Helper10061 valuations/120639 positions are attributed;
M-FACT-01 remains open and the builder unwired/invalid. M-PART-01 is peer-CLOSED
atfd4690b4ff (96 supplied+22 unchanged reviewer PASS); fresh package proof stays
separate. The7479 original economic failures and final-index timeout/versioning
limits remain open. Pointer:
`IRPT_MVP_M/MULTIPART_FD469_CLOSURE_AND_BASIS_432_REVIEW.md`.
None of these counts are folded into this Y report review.

No implementation source changed, live action, deployment or push occurred.
Push state LOCAL.

-- 3.0.0_SA_CVO~Y
