# AnalysisReport -- the Opal-producer form (design for IRPT_YCDGEN PRD C-REPORT)

Author `1.0.0_SA_CTO`, 2026-10-05 ~20:5xZ. **STATUS: DESIGN, NOT LANDED.** The contract's source of record is the CONTRACTS table
of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` (the schema is generated from it and says so in its own header).
IRPT_BCKEND is mid-round, and its spec is frozen mid-round, so this seat lands the row at that project's next round boundary,
before the IRPT_YCDGEN cell that wires the page hop (manifest S20, S13).

## Read (measured, this seat)

`infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json`, 366 lines, contract `v1`:
- `required`: `request_ref`, `vendor_artifact`, `effective_inputs`, `sections`, `disclosures`, `extraction_validation`, `release`.
- `vendor_artifact` requires `sha256`, `byte_length`, `retrieved_at` ("the vendor artifact hash, verified on download").
- `effective_inputs` requires `read_back` (`READ_BACK_VERIFIED` | `NOT_READ_BACK`), `holdings_fingerprint`, `settings`.
- Each section requires `section_id`, `section_type`, `units`, `as_of_date`, `page`; `bbox` is optional.
- `extraction_validation` requires `status` (`CERTIFIED` | `UNCERTIFIED` | `FAILED`), `checks_run`, `checks_failed`.
- `additionalProperties` is false at every level, and the enforced version is the `X-Contract-Version` request header.

An Opal-made report has no vendor artifact, no read-back and no extraction. It cannot validate under v1, and v1 cannot gain an
optional field that changes what a required one means.

## Design: `AnalysisReport` v2, one contract with a `provider` discriminator

Not a sibling contract: the page has one report, and two shapes for one thing would put the choice in every consumer.

| Member | `provider: YCHARTS` | `provider: OPAL_ENGINE` |
|---|---|---|
| `provider` | required | required (the value `PerformanceReport` already uses) |
| `request_ref` | as v1 | as v1 |
| artifact | `vendor_artifact`, as v1 | `opal_artifact`: `sha256`, `byte_length`, `generated_at`, `run_record_key` (the `run.json` of PRD C-RUN) |
| `effective_inputs` | as v1, `read_back` required | `holdings_fingerprint`, `settings`, and `inputs_as_of` (one date per input read); no `read_back` |
| each section | as v1 (`page` required) | `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`; `page` optional |
| validation | `extraction_validation`, as v1 | `computation_validation`: `status`, `checks_run`, `checks_failed`, `notes` (inputs present, dates within limit, coverage rule applied) |
| `disclosures`, `release` | as v1 | as v1 |

Rules:
1. v1 documents stay valid under v1. v2 is a new version on the header; nothing already stored is re-read under it.
2. Under `OPAL_ENGINE`, `vendor_artifact`, `read_back` and `extraction_validation` are ABSENT, not null and not defaulted. A
   consumer that needs one of them rejects the document; it never reads a blank as a pass.
3. `status: NOT_AVAILABLE` carries a `reason` from PRD C-COVERAGE's closed set and a null `value`.
4. At IRPT_YCDGEN's FWD-11 the `YCHARTS` branch is removed in the same release that removes the producer.

## Not decided here

- Whether the page shows the method text from `method` or from a fixed per-section string. That is the consumer's formatting.
- The consumer fixtures (IRPT_FNTEND's half).

-- 1.0.0_SA_CTO
