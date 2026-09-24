# CTO direct review: P binding with M publication replay

Candidate `e36b007fa1`; P implementation `00b54afab1`; M runtime
`3539ad2ae5` with docstring correction `200ba442f5`.
Authority `999998e448`. Reviewer: `1.0.0_SA_CTO` per Andrew's instruction.

**Bounded PASS for local binding/storage/publication-history integration.**
Y may consume the concrete reader. This does not approve economic admission,
production authorization adapters, final packaging or deployment.

Read the complete P store, reader and tests at the submitted pin. The store
uses the configured requests table and separate CUSTODY_BINDING namespace,
server-generated snapshot IDs, canonical payload digests, a 300000-byte cap,
conditional create, strong readback and exact idempotent conflict checks.
The reader rechecks its supplied current-selection authority before and after
source loading, compares retained owner/selection/economic evidence, and delegates
historical acceptance checks to M's actual pinned publication reader. Exceptions
are mapped to a generic private-custody refusal. No request-facing writer or
default economic interpreter/validator is installed.

## Direct test evidence

Isolated candidate archive:
`C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-binding-4e08f4d726834edab6cd49c87d915a20/source`.
Included repository test dependencies from the same candidate, including registry,
producer, naming, source-map, schema and Terraform declaration files.

```text
python -m pytest infra/aws/lambda/investor-reporting/_scope/tests/test_custody_binding.py infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py infra/aws/lambda/investor-reporting/holdings/tests/test_snapshot.py infra/aws/lambda/investor-reporting/holdings/tests/test_publication_entry.py -q -p no:cacheprovider --tb=short --maxfail=3
115 passed in 1.85s; exit 0
```

Unchanged tests exercise conditional conflicts, failed strong readback, generic
errors, revoked/changing authority, missing or changed economic capability and
actual M capture/replay through P across same-date corrections. S3 and DynamoDB
are fakes; successful economic/current-selection callbacks are synthetic. These
tests do not establish complete original-row economics or real principal access.
That limitation agrees with P's handoff and remains an integrated acceptance gate.

## Evidence manifest correction required before package closure

Checked all 27 entries of P's CUSTODY_BINDING_SEAM_EVIDENCE_20260923.json
against the candidate's committed bytes and Git blob identities:

- All 27 Git blob IDs match.
- 14 SHA-256 values match exact committed bytes, including all listed runtime
  source and test files.
- 12 documentation SHA-256 values match only after LF-to-CRLF checkout conversion.
- P `IRPT_MVP_P/STATUS.md` SHA-256 matches neither committed bytes nor that CRLF
  conversion, although its recorded Git blob ID matches.

P must publish an unambiguous corrected manifest: hash exact Git blob bytes for
source evidence, explicitly pin the measured commit, and separately identify
archive bytes when packaging. Regenerate the status-file hash from that pin;
do not label these mixed hashes exact committed-byte parity. This documentation
finding does not block Y local integration and requires no unchanged suite rerun.

Next required artifact remains P/Y's paired consumer candidate with original-row
eligibility/provenance checks and a corrected manifest. Mandatory economic ports
must remain absent/refusing until real source capability is implemented and
reviewed. Publication acceptance alone cannot fill them. No cloud action follows
from this review.
