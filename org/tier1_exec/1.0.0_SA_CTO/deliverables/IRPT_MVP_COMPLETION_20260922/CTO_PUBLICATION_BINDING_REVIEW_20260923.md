# CTO direct review: exact publication binding

Candidate: `3539ad2ae5fec01a9efecc7c5fa49845d5cb64d6`.
Authority: `999998e448`; reviewer: `1.0.0_SA_CTO`, per Andrew's direct instruction.

**Bounded PASS for local publication-history support and P integration.**
This is not actual-custody acceptance, current-principal authorization, deployed
behavior or completion of the P/M/Y product.

Read the complete source diff, added tests and full publication implementation.
The commit changes only the four publication/snapshot source/test paths assigned
to M. `capture` records the observed index version, byte length, digest and exact
date row; `load_pinned` checks that historical index accepted the exact row before
loading the manifest. It does not resolve the current index as fallback. Existing
manifest, header, full partition inventory and selected-part validations remain
in the shared reader. Wrappers preserve the original full snapshot revision
separately from decorated/selected document bytes.

## Direct execution

An isolated archive of the candidate, not M's working directory, was exercised:
`C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-pinned-42ec5ddde2a848e28724bb960c510ef7/source`.

```text
python -m pytest infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py infra/aws/lambda/investor-reporting/holdings/tests/test_snapshot.py infra/aws/lambda/investor-reporting/holdings/tests/test_publication_entry.py -q -p no:cacheprovider --tb=short --maxfail=3
99 passed in 1.87s; exit 0
```

The tests were unchanged. Initial attempts failed because the review archive
omitted repository dependencies: firm registry, producer module, lib, naming
registry, Lambda source map and Terraform declarations. Added those dependencies
from the same candidate pin; no source/test edits or substituted expectations.
The first complete run passed all 99 tests. This is offline fake-S3 evidence with
real Parquet and actual reader/guarded Entry modules, not live storage evidence.

Covered cases include same-day replacement with old-revision replay, current
index removal, capture races, orphan manifests, changed or unavailable pinned
versions, hash/size/identity tampering, selected census and multipart inventory.

## Integration conditions and small documentation correction

P may integrate this candidate into the assigned trusted binding reader/store.
P still must establish current authority, exact selection and original-row
coverage, economic/source declarations and immutable process-record integrity.
Y must consume that paired implementation; a valid publication receipt alone
cannot satisfy those obligations. No deployment or callback activation follows.

M should correct `publish`'s existing docstring claiming that no readback failure
advances the index. The new exact-index readback occurs after conditional PUT:
if readback fails, the method returns no acceptance receipt, but the write may
already have succeeded. Describe this as an unconfirmed outcome requiring
exact-version reconciliation; do not imply rollback or recommend a blind retry.
This is a nonblocking documentation correction for local integration. No
additional suite run is required for a docstring-only correction. Any behavioral
change requires its own focused evidence.
