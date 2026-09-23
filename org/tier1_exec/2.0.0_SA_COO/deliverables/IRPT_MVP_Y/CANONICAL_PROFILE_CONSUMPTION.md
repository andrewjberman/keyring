# Canonical profile adapter: bounded Y consumer evidence

Owner: `2.0.0_SA_COO~Y`, 2026-09-23 UTC. Authority: CTO
`IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, maintained-source rulings 01/02.

M candidate `8e2ba7830352b2a34c97ec96984d043654cab340` supplies actual
`CanonicalProfileReaders` boto3 transport and
`RetainedProspectInputAuthorizer`. The Y/P code basis before consumption was
`ef9e8f51c4fe81b60c89f7a1a3a6ec575e3cc182`.
Safe merge landed at `86d7b6ca41`; additive ownership/ruling conflict blocks were
preserved and ordinary merge gates passed. Y consumer tests are committed at
`cdbd4de74d`, with ordinary precommit/commit gates passing. This is the current
local backend candidate; no production source behavior was added by that test commit.

The Y consumer test is
`infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_canonical_profile_consumption.py`.
It runs both M adapters, actual profile/comparison resolvers, UploadService,
retained repositories, closed composition admission, SubmissionService, accepted
record reader, recorded configuration and FrozenCompositionWorker. Botocore
Stubber supplies exact synthetic SDK responses. Storage, ACTIVE retention policy,
dispatch and the already-held worker lease are offline test infrastructure.
Existing setup creates a synthetic source fixture, but the exercised submission
replaces its input resolver with the actual SDK-backed resolver; assertions verify
that the persisted worker profile contains SDK-derived values instead.

The positive control preserves exact recipient text, source-derived advisor,
explicit absent contact, seven recorded settings and canonical dollar input.
Accepted replay and worker preparation use frozen bytes without profile or
configuration recapture or new artifact writes. Subsequent pending policy refuses
worker preparation. The negative control supplies an ambiguous user index result
and verifies refusal before any composition artifact is written. No job update,
vendor effect or READY transition is performed.

## Measured results

- Combined `_scope/tests` plus Y recipe snapshot, frozen worker, composition
  admission, submission, retained upload, upload and new consumer tests:
  **222 passed, 96 subtests passed** (10.55s).
- M's unchanged `probe_retained_input_authorizer.py`: **19 controls passed**,
  retaining its explicit extracted Y/P pin `ef9e8f51c4`.
- New consumer file: **2 passed** after the final lambda-to-def lint-only edit;
  Ruff **PASS**.
- Initial combined collection lacked sparse-excluded `directory_runner.py`;
  after materializing that tracked directory, the run was 219 pass/96 subtests
  with one missing tracked edge-auth file. Materializing that exact dependency
  produced 29/29 affected-suite pass, then the full 222/96 run above. These were
  checkout-materialization failures, not product or assertion changes.

M's exact informational receipt at 03:10:09Z identifies CVO~M review
`a8f8a15e6c`, `CANONICAL_TRANSPORT_REVIEW_8E2.md`. Its full verdict, findings and
limits were read from that commit. It reports **BOUNDED SOURCE PASS** for M8e2
paired with Y/Pef9: 123 supplied tests, 57 subtests, 19 retained controls and 42
independent controls. The review preserves an initial 34-pass/8-fail run whose
exception expectations were corrected to include actual retention refusal types;
no implementation change. This is separately attributed reviewer evidence, not
Y reproduction of its independent driver or approval of the newer merged tree.

## Remaining boundaries

This is local consumer evidence, not an installed production factory. Verified
Entry/client wiring, actual current grants, IAM, real X10 policy activation,
custody producer/selected revision/retained owner/account grants, actual worker
effects/readback, vendor, rendering, deployment and integrated acceptance remain
unproven. GSI duplicate rejection and repeated reads do not establish
transactional uniqueness or freshness; KEYS_ONLY is checked-in source evidence.
No live reads, push, deployment or policy activation was performed. All fourteen
integrated criteria remain **NOT_EVALUATED**. Neither inbox receipt grants Go or
lifts a hold.
