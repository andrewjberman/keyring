# R interface reconciliation

**Candidate design, not a ratified served contract.** September 23, 2026. I5/I6 belong to R; no existing drafting or Posture schema is amended in this slice.

## Existing contract and measured conflict

At base `db3267d079`, `lib/research/drafting/schema.json` requires marked sentences with evidence and a verbatim verdict. `pipeline.py` holds sentences with no quoted span; accepted claims have a verified span and `anchored=True`. Its five limbs are a different shape from the new per-part report. Existing `lib/research/posture/posture.schema.json` defines O-1 verdict/basis/cites and machine marking.

The analysis brief's M3/M4 admits typed figure citations and P10 cites accepted part-sentence/figure IDs. A correct figure-only revenue claim with no filing quote cannot clear the existing no-span HOLD. R sent this concrete semantic fork to CTO at 16:48:41 UTC. The existing gate remains intact. A separately typed figure/synthesis branch requires an explicit contract decision and the applicable review. R will not manufacture quotation spans to make a numeric claim pass.

## Input/method stamp implemented now

| Field | Meaning |
|---|---|
| `input_id` | Stable logical dependency identifier, not a storage address |
| `state` | `present`, `absent`, or `failed` |
| `key` | Existing builder-produced retained-object key supplied by its reader; optional for absence/failure |
| `content_sha256` | Hash of exact retained bytes, required only for present inputs |
| `reason` | Explicit absence/read-failure reason; never a fabricated empty successful document |
| `part_id` | Report part consuming the inputs |
| `method_version`, `method_sha256` | Independently versioned method and exact prompt/schema artifact byte digest |
| `depends_on` | Other part IDs used by this part; complete acyclic graph required |

Positive example: unchanged `headline_results`, `management_reading`, `recommendation_delta`, `posture` all return no stale reasons. Difference arm: change only headline filing bytes; headline names the changed hash, recommendation and Posture name their stale upstream parts, management remains fresh. Refused examples: cyclic graph, unknown upstream, duplicate input ID, present input with malformed/missing hash. Failed-read example: identical repeated failures stay stale, while an unchanged explicit absence can be fresh. Fresh does not mean complete, accepted or authorized.

The executable examples are `lib/research/reports/tests/test_inputs.py`. All fixture keys are labelled `fixture/...`; none is a deployable address.

## I4 consumption boundary

C's 16:49:51 message describes the current substrate: five members, artifact URI/hash/method/current and inputs_count; full inputs are in referenced gold documents. R preserves that shape. A semantic `content_sha256` embedded in a gold artifact is not presumed equal to the SHA-256 of its complete stored bytes. C is supplying retained examples and explicit hash semantics. No live caller or normalization adapter is asserted by this slice.

## I5/I6 decisions and acceptance examples still to deliver

- Report identity: canonical security, as-of and immutable revision; method version, input manifest and held counts.
- Passage claim: exact source/key/hash and known passage ID; unknown, foreign or mismatched evidence refuses; no-span follows the existing HOLD until a ruled typed alternative exists.
- Figure claim: stable figure/value/unit/basis/period/vintage and exact-match controls; semantics pending the above ruling.
- Synthesis: only accepted part-sentence or figure dependencies; dropped/held upstream claims never become admissible through Posture.
- Replacement: failed or empty candidate preserves the prior accepted revision; serving and export select that exact revision.
- Storage: canonical registered TABLE and generated builder; undecided registry owner is a full dependency result. No handwritten production key.
- Authorization: existing narrow firm/source scope must apply to current report, selected history and export alike.

These are required examples, not claims that the absent producer/store/API already passes them.
