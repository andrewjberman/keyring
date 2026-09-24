# R interface reconciliation

**Candidate design, not a ratified served contract.** September 23, 2026. I5/I6 belong to R; no existing drafting or Posture schema is amended in this slice.

## Existing contract and measured conflict

At base `db3267d079`, `lib/research/drafting/schema.json` requires marked sentences with evidence and a verbatim verdict. `pipeline.py` holds sentences with no quoted span; accepted claims have a verified span and `anchored=True`. Its five limbs are a different shape from the new per-part report. Existing `lib/research/posture/posture.schema.json` defines O-1 verdict/basis/cites and machine marking.

The analysis brief's M3/M4 admits typed figure citations and P10 cites accepted part-sentence/figure IDs. A correct figure-only revenue claim with no filing quote cannot clear the existing no-span HOLD. R sent this concrete semantic fork to CTO at 16:48:41 UTC. CTO message 24807 rules a checked typed FIGURE admissible on I2 provenance; interpretation/inference is PROSE and retains the existing verbatim gate. This settles semantics, not ratified text. The offline candidate below is not wired to served output; the applicable L4-R review remains required.

`lib/research/reports/claims.py` implements the discriminator structurally. A figure candidate has exactly `kind` and `figure_id`; model text or restated numbers are refused. Its projection is copied from a caller-owned typed row carrying security, value, unit, basis, period, vintage, PASS verdict and a present source matching the retained-byte manifest. This trusts the upstream I2 check, not model-supplied catalog rows. Actual I2 adapter and live validation remain outstanding. Prose requires passage evidence; citing a figure ID as passage evidence refuses. No-span prose is held; invented spans refuse; exact cited spans pass with machine marking. These checks preserve the existing gate; a valid quote by itself does not independently prove every inference in surrounding prose.

Twelve new controlled cases exercise both accepted/refused arms and the HOLD branch. Existing drafting schema/pipeline bytes are unchanged. [EVIDENCE_CLAIMS.json](EVIDENCE_CLAIMS.json) records candidate hashes and test output for CVO review.

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

C's 16:49:51 message describes the current substrate: five members, artifact URI/hash/method/current and inputs_count; full inputs are in referenced gold documents. R preserves that shape. A semantic `content_sha256` embedded in a gold artifact is not presumed equal to the SHA-256 of its complete stored bytes. C's 16:56:31 follow-up commits to separate retained-byte and semantic hashes and a missing-extraction FAILED control. It clarifies that `prior_reports[i].sha256` currently hashes extraction JSON bytes despite being paired with `bronze_key`; R must not label that as a bronze-byte checksum. Durable examples are still pending, and these details are peer-reported until independently reproduced. No live caller or normalization adapter is asserted by this slice.

## I5/I6 decisions and acceptance examples still to deliver

- Report identity: canonical security, as-of and immutable revision; method version, input manifest and held counts.
- Passage claim: exact source/key/hash and known passage ID; unknown, foreign or mismatched evidence refuses; no-span follows the existing HOLD until a ruled typed alternative exists.
- Figure claim: stable figure/value/unit/basis/period/vintage and exact-match controls; offline discriminator implemented under 24807, actual I2 adapter and L4-R acceptance pending.
- Synthesis: only accepted part-sentence or figure dependencies; dropped/held upstream claims never become admissible through Posture.
- Replacement: failed or empty candidate preserves the prior accepted revision; serving and export select that exact revision.
- Storage: canonical registered TABLE and generated builder; undecided registry owner is a full dependency result. No handwritten production key.
- Authorization: existing narrow firm/source scope must apply to current report, selected history and export alike.

These are required examples, not claims that the absent producer/store/API already passes them.
