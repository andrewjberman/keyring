# Y-3 design -- an ETF the classification table holds, admitted as a comparison key (CTO rulings batch 178, ruling 4)

**Seat:** `2.0.0_SA_COO~Y`, 2026-10-02 ~22:2xZ. **Status:** design, read from code; nothing built. It is built after st14's V1.
**Ruling 4, verbatim:** "`~Y` admits an ETF the classification table holds as a comparison key, through the same identity
check as an uploaded symbol. If that changes the meaning of a CONTRACTS row (`AnalysisSubmissionRequest`'s
comparison-key domain), `~Y`'s packet names the row and this seat writes the PRD addendum."

## Where a ticker is refused today (measured in code)

1. **Submission.** `_scope/maintained_sources.py:555-560` matches each key against the packaged model catalogue only.
   `IWM` is refused: "comparison key unknown or ambiguous". `_admitted_comparison` (`:619-634`) also requires a model
   policy hash from ~M (`:584-589`).
2. **Composition.** `reports/request_composition.py:191-208` requires `source_kind == MAINTAINED_CONFIGURATION`. It binds
   the projection's `vendor_id`, `name`, `security_type`, `namespace` and `mapping_evidence`, and refuses an alias
   (two keys, one identity).
3. **Recipe.** `ycharts/generate/recipe.py:728,817-823` sends each comparison's `vendor_id` as the YCharts security id.
   A model is `P:<id>`. An ETF's YCharts id is its bare ticker (the capture's `VNQ` row: id `VNQ`, type `etf`).
4. **The wire.** `AnalysisSubmissionRequest.comparison_keys` already admits `IWM` (pattern `^[A-Za-z0-9][A-Za-z0-9_.:-]*$`).
   The catalogue route already serves ETF entries with `key` = the ticker (`comparison_catalogue.py:152-159`,
   `name_source` `etf_classifications`).

## The change

- **(a) Admission, Lambda.** A key that is not a model, but is a ticker the `etf-classifications` table names, is admitted
  as a `CLASSIFIED_SECURITY` source:
  - projection `{key, vendor_id: <TICKER>, name: <the row's name>, security_type: "etf", namespace: "YCHARTS_SECURITY_ID", mapping_evidence: "ETF_CLASSIFICATIONS:<sha256 of the row's three projected attributes>"}`;
  - no firm restriction: a listed ETF is public;
  - the classifications reader is the catalogue route's own (`classifications_reader`, its Scan grant already applied).
  - An unnamed ticker stays refused: the ruling admits only what the table holds.
- **(b) Composition.** Accepts `CLASSIFIED_SECURITY` beside `MAINTAINED_CONFIGURATION`, with the same field binding and
  alias rule.
- **(c) The identity check, resident.** Before any vendor mutation, the job runs the same `SecurityResolver.check` an
  upload runs, over its classified comparison tickers. Each must be FOUND as an exact provider match: id == ticker,
  type etf, no `features_needed`. Anything else ends the job by name (`COMPARISON_IDENTITY_UNVERIFIED`) before the
  portfolio is created. That is one `securities_info` read per job with an ETF comparison. The receipt's sha256 rides
  the job row.
- **(d) Recipe:** unchanged. `vendor_id` is already what it sends.

## Contract row to name

`AnalysisSubmissionRequest` (`docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json`,
provenance IRPT-MAINTAINED-SOURCE-02 51b5d63a81):
- **Domain today:** a key of the maintained model catalogue.
- **Domain after Y-3:** a maintained model key, or a ticker the `etf-classifications` table names.
- **Wire shape:** unchanged.
The CTO writes the addendum.

## Ships as

One packet: `irpt-ycharts-generate` (a, b) and the resident (c), at one commit. It follows st14, whose artifact is the key's
latest until its D1.
