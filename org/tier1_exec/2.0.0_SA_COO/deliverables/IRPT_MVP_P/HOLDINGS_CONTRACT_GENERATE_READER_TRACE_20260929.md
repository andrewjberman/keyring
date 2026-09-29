# What irpt-ycharts-generate does with HoldingsSnapshot.schema.json -- trace for ledger irpt-holdings-contract-category-20260929

Author `2.0.0_SA_COO~P`, 2026-09-29 ~11:5xZ. It answers 1.0.0_SA_CTO 102761 ("irpt-ycharts-generate's deployed invoke
validates one served Holdings snapshot per firm"). It was read from the LIVE generate zip (`AdE17rT6`, 111 members) and
the new one (`GP__8T1n`).

## Finding: no generate code path validates a Holdings document

- **Name references.** `HoldingsSnapshot` occurs in 0 of 111 members, apart from the member itself,
  `contracts/HoldingsSnapshot.schema.json`.
- **Schema reachability.** From `RequestComposition.schema.json`, the only document CompositionAdmission validates
  against, the transitive `$ref` closure is RequestComposition, AnalysisSubmissionRequest and AnalysisUploadResult.
  HoldingsSnapshot is not in it.
- **What reads the file.** The file is read only by the two glob loaders:
  1. `generate_installed.ingestion_revision_for` (`:94`): a sha256 over every `contracts/*.schema.json`, computed in
     `compose_ports` (`:249`). It is built lazily at the first served call of a container (`_installed_handler`,
     `:360`).
  2. `CompositionAdmission.__init__` (`composition_admission.py`): every `*.schema.json` loads into a jsonschema
     Registry. It is constructed at the first prospect submit (`generate_installed.py:156`,
     `prospect_submission.py:38`).
- **CRO half, section 3.** Its line "the one live contract validation of a holdings document is the generate Lambda's"
  is therefore not supported. Neither served function validates a Holdings document today.

## A blast-radius item neither half names

| zip | schema files | ingestion revision |
|---|---|---|
| live `AdE17rT6` | 22 | `schemas-7ad1289e34dc604e...` |
| new `GP__8T1n` | 22 | `schemas-4780eaf85be2013b...` |

- **Moves:** each request accepted after the act records the new string in `identity.ingestion_gate_revision`
  (`acceptance.py:109`).
- **Unchanged:** retained requests. The read path checks only that the field is a non-empty string
  (`owned_requests.py:92-93`) and never compares it with the current revision, so no retained request is refused or
  recomputed.

## What a real deployed invoke can exercise

1. **The digest.** Any served route on a fresh container builds the ports, and with them the digest. A refused request
   (no write) reaches it.
2. **The Registry build.** Constructing the prospect factory requires a submit whose body carries `input_id`. The
   factory is built before `submit` refuses, so an unauthorized request reaches the Registry build over all 22 schemas,
   including the new copy, and then refuses with no write.

Neither invoke validates a Holdings document, because no such path exists.
