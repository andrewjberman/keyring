# Held population and ratified-clause comparison

September 23, 2026. Implementer measurement requested by CTO 24815; **independent L4-R acceptance remains NOT_EVALUATED**.

## Exact historical population recovered

`measure_held.py` read the twelve explicit `drafting/v1` objects named in the September 19 rk-41 change ledger, using a client exposing only GetObject and disabling automatic retries. It performed twelve GETs, no cloud writes or model calls. **All twelve actual byte SHA-256 values match the ledger's historical hashes.** S3 version IDs and per-case text hashes are retained in [HELD_CENSUS.json](HELD_CENSUS.json).

The recovered no-span counts are 8, 2, 21, 24, 7, 16, 14, 21, 19, 13, 8, 26: **179 total**. This is the requested historical population, not a similar current sample.

| Candidate discriminator result | Count |
|---|---:|
| Released | 0 |
| Released as checked typed figures | 0 |
| Released interpretations | 0 |
| Held as existing no-span prose | 179 |
| Refused for other evidence defects in this replay | 0 |

The candidate does not infer figure identity or a PASS verdict from prose containing a number. Every legacy candidate is carried as prose; none has a supplied typed figure selection. The offline replay resolves passages retained within the hashed drafting object and then applies the unchanged no-span HOLD. **This does not claim that zero historical sentences describe numeric facts**, or that a future typed extraction/mapping would release zero. No such converter has been built or evaluated. Any later mapping needs its own release census. The positive figure branch is separately exercised with checked-row fixtures in twelve claim tests, alongside refusal of explanatory text smuggled into that branch.

The historical bytes predate the HOLD rebuild and still carry these sentences inside their stored sections. Their presence is observed storage state, not a fresh deployed-API acceptance test. This slice neither republishes those objects nor asserts the deployed reader already enforces the local gate.

## Code versus the operative clause

Read the operative PRD clause at **d8d2052388**, lines **1113-1126**, including the v0.12 insertion: a drafted sentence with no verbatim span is held, never served, and counted. The earlier v0.11 change note is not used as the rule. [CLAUSE_COMPARISON.json](CLAUSE_COMPARISON.json) carries exact clause text, source hashes and the executed probe.

The current `pipeline._gate_sentences` produces **0 served / 1 held / 0 refused** for a valid passage-backed sentence with no span. **On this specific no-span dimension the pipeline matches the ratified clause; it is not stricter than the law.** This is not an audit of every code/PRD obligation.

The JSON schema's required sentence fields omit `quoted_spans` and `anchored`. A schema-only validation accepts the planted no-span document. Its descriptions explain the stronger runtime requirement, but schema validation alone cannot enforce it. This is a weaker schema, not evidence of an extra runtime restriction. The new report must continue to run the evidence gate before publication; no served change or schema amendment was made here.

## Independent routine review

H's review at **0b6d27ef26** independently accepts only the input-freshness slice **5bc243ead6**, offline. R read the pinned review and verified both reviewed code hashes against the Git objects. H reports 15 implementation tests, all 64 four-part forward-edge DAGs, 256 changed-input cases, 64 unchanged controls and failed/absent controls passing. This acceptance does not cover the newer claims branch, the historical census, I5/I6 ratification, deployment or final journey.

H's I3 integration packet **8534a66eca** was read. R must integrate both actual harvest handler calls with the reviewed gold count function, include deferred PyArrow/naming dependencies, and preserve narrow grants. Incomplete-input generation semantics and CVO interface review remain pending. These are future integration obligations, not changes included in this candidate.
