# Explicit primary policy and capture isolation: bounded PASS

Reviewer: `3.0.0_SA_CVO~P`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.

- Backend: `cf11337d2e651a63623336ca29fdb67472983b37`.
- Declared package: `f7e0a07c437d352b5891337a29d8d46bc916719a`.
- Portal wire: `33e139259d06438674b1d10d48f5a221c26e44f7`.

No defect was reproduced within the requested provider/served-refusal, schema and declared-package boundary. The actual served path returns no performance report for unproven SmartX, Black Diamond or Orion calculations. Recorded captures cannot certify a current selected set through either the guarded entry or the legacy handler. This PASS is for refusal and boundary correctness, not successful performance delivery.

## Policy and replay

49 Financial has explicit SMARTX primary policy with no invented endpoint, credential or data destination. Its BLACK_DIAMOND route is a separate verification route. Cottonwood remains BLACK_DIAMOND; Inflection remains ORION. Other firms cannot obtain the 49F verifier. An unregistered provider returns `UNSUPPORTED_PROVIDER` without falling through to Orion.

`run` performs no provider request and returns `report: null`, `contract_validated: false`, explicit coverage and absence reasons. Legacy mode/token/transport/label arguments cannot make it return a capture. The guarded entry translates a missing validated report into an unavailable response without data. The legacy handler can return HTTP-shaped statusCode 200 containing the explicit unavailable outcome; that is not report success. The guarded request remains the public authorization boundary.

Historical parser economics are preserved under `replay_capture`, using the exact offline transport class and restricted synthetic account sets/window. Changed IDs, an Inflection subset, or a changed window refuse. Supplied controls also exercise rejection of a non-offline transport and another tenant's labels. No live transport was constructed or invoked by the reviewer. The transport module still contains historical live plumbing, but no enabled provider path is established by this change.

## Reproduced checks

| Evidence | Result |
| --- | --- |
| Supplied performance adapter, entry selection and primary policy suite | 57 PASS |
| Canonical closure over declared flat package | 18 Python members PASS; documented lazy-import exemption retained |
| Supplied real flat guarded-entry controls | PASS: unproven SmartX refuses; controlled provider sees exact selection; post-call revocation refuses |
| Additional reviewer controls | 18 PASS, zero forbidden provider/replay/transport calls |
| Both source schema provider enums and packaged schema | SMARTX, BLACK_DIAMOND, ORION, UNKNOWN admitted explicitly |
| Pinned generator rendering of PerformanceReport wire | Exact match after CRLF normalization |

The 18 reviewer controls cover recorded/live argument variants for all three primary policies; all three legacy handler calls refusing capture release; explicit primary/verifier separation; other-tenant verifier refusal; unsupported-provider refusal; empty, duplicate or wider selections; actual guarded-entry refusal; exactly retained account IDs and requested dates passed to the real provider function; missing selection and query transport override refusal before provider invocation; revoked selection refusal before provider invocation; and changed replay set/subset/window refusal.

The additional assertions reuse the pinned supplied entry setup, with synthetic directory/ownership/selection storage and forbidden-call sentinels. They are reviewer-written controls against actual reconstructed modules, not a separate real backend or live three-firm data run. The supplied controlled READY result stubs provider output; it is not an actual successful source calculation.

## Package denominator and schema

The maps contain **216 total function objects: one changed and 215 unchanged**. This independently confirms the committed producer evidence and corrects the notification's claim of 216 other entries. All top-level map metadata compares equal. The performance object changes only `files`, `staged_from`, `_build_note` and `note`; deployment metadata remains equal.

All 28 unique members were reconstructed and recorded by SHA-256: 16 staged members verified against their declared source pins/hashes and 12 direct members verified equal at backend and package pins. Older shared dependencies remain pinned as declared; this review does not upgrade them to another lane's current implementation. The added packaged PerformanceReport schema has SHA-256 `5493d31259dde3f9b7932cd81e27be3e7f58ec6ca91b9e61a94b3f546cb41bd1`.

The generator was imported and its `renderModule` applied to the pinned versioned schema; the resulting module equals the pinned portal file after line-ending normalization. This is content/code-generation parity, not a raw-byte equality claim between versioned and internal schemas, which have different metadata. Archive schema hashes in the JSON reflect the extracted files; staged package hashes reflect Git blobs. SMARTX enum admission alone does not demonstrate provider capability. Project typecheck remains producer-reported; no full portal test or mounted prospect review is added.

## Artifacts and remaining gates

`primary_policy_probe_cf11.py` builds isolated pinned source and flat-package snapshots and runs all checks. `primary_policy_cases.py` contains the additional assertions, SHA-256 `8b89843adc1280a10077dae2f4ae28f3ab1fbb9ecd05bf11d7ea95cb996b5da5`. `primary_policy_probe_cf11.json` records full pins, map denominator, member hashes, source schema hashes and all subprocess output. All five subprocesses exit 0; Ruff passes for both reviewer files.

The real-provider selected-account/request/response/window proof remains open. Baseline provider/source-readiness findings are not closed by making the service unavailable. No actual SmartX calculation, BD independent verification, Orion calculation, deployed package/layer/IAM, authenticated HTTP, mounted browser, live connector, source census or full P1-P8/S1-S7 acceptance is claimed. No implementation file was changed. Prior R-P07/R-P08/R-P09 bounded closures remain separate.

Peer-only interface evidence: CVO~Y review `1308dd5a64` on `c2a01fb3f8` reports an offline canonical bridge preserving identity and dollars. It explicitly excludes current access, artifact retrieval, checkpoint provenance and mutation fencing; actual M source/vendor/runtime and all 14 integrated criteria remain unproven. Its counts are not included here.
