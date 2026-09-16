# Connect the publication pool to RESAPP coverage and Chatter

Author: `4.0.0_SA_CRO~W`. 2026-09-15 06:17 UTC.
Authority: Andrew's 60-minute progress/gap-review instruction, recorded at
`ANDREW_DIRECT_20260915_RESAPP_60M_PROGRESS_LOOP_W.md@76ab87a06e`.
Recipient: `1.0.0_SA_CTO~W`, for the PRD/COO cut. This brief does not implement
or deploy another worker.

## Problem and desired result

C-ONE-STORE correctly connects the existing publication pool to two currently
disconnected readers. Its timestamp field is wrong: PRD v0.6 at `2f3b65d8b8`,
lines 367-370 says `published_at` from the article body. The canonical stored
JSON requires **`published`**, with `additionalProperties: false`; it does not
contain `published_at`. A literal reader can turn a populated pool into a
silent zero-count series or lose date ordering.

Outcome: the same admitted article identity appears once per associated
security in the feed and once in the corresponding publication-day count,
with its actual source URL, clean text, and retrieval vintage. Partial or
failed collection must remain distinguishable from a quiet security.

## Exact source contract

Sources checked at 06:15-06:17 UTC:
`lib/opal_data_harvest/article.schema.json`, `security-article.schema.json`,
`catalog.py:14-38,61-81`, `uploads.py:40-83`,
`lib/research/coverage/reader.py:108-135`, and
`lib/research/metrics/chatter_axis.py:201-242`.

| Pool field/path | Consumer meaning |
| --- | --- |
| `publication-links/v1/{security_key}/{publisher}/{digest}.json` | Security association; use its `security_key`, `publisher`, `article_key`. A ticker string is not this key. |
| `article_key = publisher + ':' + article_id` | Stable global identity for one publisher article. Reuse as the feed's `item_id`. |
| `digest = sha256(article_key.encode('utf-8')).hexdigest()` | Filename; do not hash title/date or confuse it with a content hash. |
| `publications/v1/{publisher}/{digest}.json` | One canonical article body, potentially associated with several securities. |
| **`published`** | Publication time; map explicitly to consumer `published_at`. Normalize timezone before daily bucketing. |
| `fetched_at` | Retrieval vintage; never substitute for publication time during backfill. |
| `url` | Canonical source link; map to legacy coverage input `link`, whose output becomes `url`. |
| `title`, `publisher`, `text`, `body_blocks` | Headline, source, and clean body. No article DOM crawl needed. |
| `body_sha256`, `response_sha256` | Clean-text hash and optional upstream-response hash; distinct from S3 object metadata `document-sha256`. |
| `content_status = complete_candidate` | Passed body-shape/completeness checks; not automatically the research item's aboutness or source-admission verdict. |

The association's `first_discovered_at` is a third clock, distinct from both
publication and retrieval time. Missing one of these fields must not be
silently repaired from an unrelated clock.

## Required connections

1. Use one shared pool-reading adapter for coverage and Chatter. Preserve the
   canonical schemas; translate field names at the consumer boundary.
2. Join by the link's stable article key and validate publisher/identity/hash
   agreement. Deduplicate within each security. An article can correctly count
   for two different securities; retries or repeated links must not multiply
   a security's count.
3. Preserve missing-body, malformed-schema, access-denied, and partial-read
   states. Do not collapse these into an empty feed or a zero-mention day.
4. Carry the source qualification/aboutness result separately from body
   completeness. An association is evidence to evaluate, not a reason to
   label every canonical body PASS automatically.
5. A 30-day ranking needs an explicit coverage/completeness state per security
   and date. Current uploads are bounded commissioning samples; they are not
   evidence of a complete 89-name backfill. Mark partial baselines and avoid
   interpreting missing collection as quiet coverage.
6. Reconcile the canonical 89-key universe with the existing ranker input
   (34 eligible tickers in the 06:02 audit). Preserve missing identities and
   the denominator; do not silently lose 55 names while fixing the store.

## Build/package seam

Changing source code is not enough for either deployed consumer. The Chatter
zip builder `infra/aws/terraform/harvest/lambda_src/build_zip.py` enumerates
its current source files and verifies `lib.research.metrics` imports. The
scoped-API builder `build-and-upload-scoped-amgt.sh` computes a Python import
closure under `lib/research`. If a new reader imports the canonical
`lib.opal_data_harvest.catalog` validator, it also needs the JSON schema data
files and `jsonschema` dependency. These are not established as included by
the existing Python-only package checks. Extend the package contract for the
chosen reader and exercise the resulting archive in an isolated runtime;
do not assume a passing repository import proves a deployable artifact.

## Acceptance examples for the consuming cut

- A real bounded pool sample renders its source link/title and lands in the
  day from `published`, even when fetched on a different day.
- The same article linked twice to one security counts once; linked to two
  securities counts once for each. A retry leaves both results unchanged.
- A missing body, an altered body hash, and S3 access denial each produce an
  explicit incomplete/error result, distinguishable from a measured empty day.
- A limited backfill remains marked partial and cannot manufacture a fully
  observed 29-day baseline by filling every absent day with zero.
- The isolated deployed archive imports and exercises the actual pool reader,
  including any non-Python schema assets; readback pins match those bytes.

## Progress context

COO~W has completed the round-10 issuance/drain. Its `prd/stamps/L6.json`
now exists (06:05Z), so the earlier message's missing-stamp statement is
historical. Round-11 issuance was not present in the inspected decomposition
and task-order history at 06:14Z; the new PRD remains under L4-R correction.
This brief supplies connection requirements for that next cut, not a second
parallel implementation or a replacement for the current publication worker.

Push state: LOCAL. No publisher request, broad backfill, or schedule change.
