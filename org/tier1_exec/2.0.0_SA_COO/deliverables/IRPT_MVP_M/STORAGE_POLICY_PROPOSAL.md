# IRPT private reporting store: bounded R20 record and implementation plan

Status: PROPOSED; no policy acknowledgement, provisioning or write claimed.
Authority: completion CONTRACT v1.2 S7. Owner: M naming, P provisioning.

## Exact exception for adjudication

Pipeline: IRPT reporting artifacts for 49financial, cottonwood and inflection.
Axis: A2, bucket placement. Departure: the listed private firm reporting and
per-request workflow artifacts are homed in the registered product bucket
`opal-data-irpt` while retaining the canonical firm in every key. This departs
from firm platinum/state home rules R6/R7/R21 only for the families below.
Gold/Platinum custody, directory, holdings and model datasets retain their
canonical long-form firm buckets. No global/composite relabeling is proposed.

Why: one report/export repository can preserve immutable report revisions,
original input/vendor evidence, and recovery state with a single declared
placement policy, while authorization remains firm- and owner-bound.

Acknowledged by/date: OWED. Doctrine R20 and section 4 require sovereign
acknowledgement. CTO should record whether the existing Andrew instruction
already supplies this exact acknowledgement or obtain it through the normal
route; M will not write an invented approval. The register carrier is
`infra/logic/06_CONFORMANCE_LEDGER.md` section 6, owned by its existing grantor.

Kind: CONDITIONAL on enforced firm namespace, current account/prospect access
checks before and after object retrieval, server-only address construction,
immutable content/version references, least-privilege producer grants and
joint reader/writer cutover. Losing any condition closes writes/reads through
the repository until corrected. No secondary fallback or migration deletion.

## Registered families proposed to P

| Family | Tier | Table | Producer |
|---|---|---|---|
| ORIGINAL_CSV | state | prospect_inputs | Y intake |
| NORMALIZED_PORTFOLIO | state | normalized_portfolios | Y normalizer |
| REQUEST_COMPOSITION | state | request_compositions | P/Y request assembly |
| ORIGINAL_VENDOR_PDF | state | vendor_documents | P/Y provider workers |
| EXTRACTION_EVIDENCE | state | extraction_evidence | Y extraction |
| PERFORMANCE | platinum | performance_reports | P repository |
| ANALYSIS | platinum | analysis_reports | Y via P repository |
| EXPORT_BUNDLE | state | export_bundles | P export |
| EXPORT_PDF | state | export_pdfs | P renderer publication |
| EXPORT_RECEIPT | state | export_receipts | P export |
| SELECTED_ACCOUNTS | state | selected_accounts | M selection |

State families are request/input/export records, not canonical custody datasets
or a substitute for Gold Parquet. Platinum families contain bounded JSON reports.
All families retain immutable accepted versions; no expiry/deletion until an
approved retention rule accounts for every report/index reference. Interrupted,
unindexed writes are inaccessible; cleanup is a separate approved operation.

## Builder and consumer seam

`destination(firm, family, artifact_id, sha256) -> (bucket, key)` reads the
canonical registry. Firm must be an enabled client FIRM in long form; family is
closed; artifact id and digest are validated single path components. Key grammar
is `irpt/{firm}/{tier}/{table}/{artifact_id}/{sha256}.{extension}` through the
canonical builder. Neither bucket nor key comes from browser input. Existing
`address()` defaults stay unchanged for all other datasets. A pending exception
cannot produce a writable address. P packages the registry-backed adapter with
the report service, uses exact VersionId plus digest on reads, and exposes no
storage address to the browser.

Implementation: add an unprovisioned PRODUCT scope `irpt`; add a bounded
destination-policy registry record consumed and validated by `lib/opal_naming.py`;
generate impacted views, never hand-edit generated maps. Tests cover every
family, all three firms, unknown family/firm, global/alias refusal, path traversal,
content identity, pending exception refusal, and unchanged custody destinations.
P supplies final producer IAM/retention/IaC plan before provisioning. Canonical
naming owners review the limited registry/builder patch. This document is a
concrete policy proposal, not a granted exception or acceptance evidence.
