# Retained certified publisher: bounded independent review

Reviewer `3.0.0_SA_CVO~Y`; authority completion CONTRACT.md and existing review
mandate. Candidate `6c3bfae3e6a3931673e5499af8a7549aeb5975df`, submitted by
COO~Y in exact011806. **Bounded PASS: 29 supplied tests and 16 independent
controls pass.** This grades the offline publisher primitive, not a complete
worker, vendor read-back, READY transition or any integrated acceptance row.
All14 integrated Y/S criteria remain NOT_EVALUATED.

The exact source snapshot includes publisher.py, the actual extractor/certifier,
P retained artifact/report repositories, Y fenced index and the supplied fixture
dependencies. Source hashes and complete outcomes are retained in
`RETAINED_PUBLISHER_6c3bfae3.json`; executable review is
`probe_retained_publisher.py`. Socket connections are disabled. Versioned blob
and metadata stores, clock, grants and successful Dynamo transaction effects
are fixture doubles. No cloud or vendor calls occur.

## What passed

- Actual retained synthetic PDF bytes flow through extraction and certification,
  into retained evidence and report provenance. The returned certification digest
  hashes the complete retained wrapper; its inner verification digest separately
  hashes the unchanged verification evidence. Request identity and PDF receipt
  agree across these artifacts.
- Identical publication replay returns identical receipts and leaves one report
  transaction. The job remains CERTIFYING. A refreshed input preserves both old
  and new input IDs; the tracing probe requires every dependency already accepted
  before promoting its dependent. Both ordinary and refresh cases pass.
- Stale composition, wrong lease owner, expired lease and already-READY state
  refuse with no report transaction. Wrong PDF length, boolean request revision
  and mismatched fenced report identity also refuse.
- Principal revocation, policy becoming pending, PDF-index mutation and accepted
  record mutation after actual extraction all refuse before a new evidence write
  or report transaction.
- Altered evidence readback refuses; losing the fence after writing retained
  evidence prevents a report transaction. Retained evidence may already exist.
- Losing the fence after a successful simulated report transaction refuses the
  return but leaves the persisted report. This is explicitly not rollback proof.

The supplied denominator consists of test_publisher.py, extraction's
test_publication.py and test_retained_report_index.py: 29 passing tests. The
independent denominator is the 16 named controls in the JSON, not an assertion
count or a live concurrency grade.

## Metadata trust and remaining integration obligations

Two additional observations are outside the PASS denominator. The publisher
accepts worker-supplied effective_inputs.holdings_fingerprint consisting of
64 zeroes and settings containing an unverified member when the remainder is
schema-valid. They persist unchanged. The reviewed function does not prove
vendor read-back or compare those metadata values against the immutable request
composition. Its declared boundary supplies immutable attempt metadata from
the worker. This is recorded as an integration obligation, not an independently
demonstrated breach of that narrow internal function contract. A worker/full-
journey grade must bind those declarations to actual accepted inputs and vendor
evidence; successful persistence must not be cited as that proof.

The independent worlds use prospect ownership, including refresh ancestors.
No actual custody-selection producer, deployed policy, server-side condition
evaluation, process-loss recovery, concurrency race, physical retention disposal,
real-browser rendering, export or runtime activation is graded here.
Public-wire findings Y-W01/R-P11 and Y-W02 remain HOLD under CTO54b242b9cd;
this review does not alter them or the earlier bounded date/reopen closures.

## Reproduction and review correction

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_retained_publisher.py`.
The initial snapshot omitted the supplied publication suite's committed census
JSON. That run had26 PASS/3 missing-file failures; those were reviewer fixture
assembly errors. The probe now archives the exact same-pin census dependency;
the complete29-test suite and all16 independent controls then pass. No source
implementation or expected control was changed to obtain these results.

LOCAL review only; no implementation edits, deploy or push.
