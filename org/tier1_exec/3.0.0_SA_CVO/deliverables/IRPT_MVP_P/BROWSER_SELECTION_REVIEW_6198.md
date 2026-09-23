# Shared selection API/parser — bounded PASS

Reviewer: `3.0.0_SA_CVO~P`. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` and `CVO_P.md`.

Portal candidate **61983ce9b7515d93ff391a94c68a6c6da23cfc10**; backend contract pin **c5eace08c76176c6d9ebb78dd31ced3b0e57ea2d**. LOCAL independent run at 2026-09-22T22:40:12.064717Z. Requested scope: shared API serialization/parser compatibility only; mounted header integration belongs to M and is pending.

**Bounded PASS: supplied 7/7 and additional independent 16/16 tests pass.** No new defect established in this scope. Full P1-P8/S1-S7, mounted browser and end-to-end acceptance remain **NOT_EVALUATED**.

## Observed controls

- `createSelection` sends POST to the declared selections route with exact scope kind and ordered subset. Serialization copies the input array before caller mutation. The contract version header reaches the transport.
- The captured producer's retained ID is returned without deriving it from a fingerprint. Missing identity/revision/fingerprint fields, empty/duplicate/raw/mismatched account arrays, wrong envelope operation/version, and malformed retained IDs refuse.
- Holdings and performance require an explicit well-formed retained `accountSetId` before transport. Requests use that ID, preserve start/end or as_of/root_ref query values including encoded reserved characters, and do not send the cache fingerprint as selection authority.
- Actual supplied boundary-refusal shape parses as a public refusal. An additional no-firm refusal with success-shaped data still returns no data and raises the typed request error. This exercises envelope parsing with injected transport, not a live HTTP error mapping.
- Nonzero producer grant-kind maps are accepted; negative, fractional and string counts refuse. Existing array-form compatibility remains in the parser. The selection result is the raw selected-accounts document and does not acquire report-view availability metadata; this review does not claim grant-banner rendering on the selection response.
- Fixture mode refuses to invent a retained selection without an explicit service; an explicitly supplied service returns its actual supplied identity.
- Supplied tests also check route-table equality against the exact backend contracts and local-reference generator refusal for missing/cyclic refs.

## Evidence and limits

`browser_selection_probe_6198.py` materializes portal source and backend contracts via exact-pin git archives in a temporary snapshot. `browser_selection_cases.test.ts` is copied into that snapshot for independent execution. Existing local portal dependencies are referenced by a temporary junction; no dependencies were installed. Bun **1.3.9**. `browser_selection_probe_6198.json` records raw command results, both pins, dependency path and all twelve changed-source SHA256 values.

Independent assertions SHA256: `997f5378e2e08abdcbec011284b3bdb1c9019c1aae6f9aed0f67238f30116b56`. API SHA256: `b099d7db74cefe3da4ffc3b0c34cd934ebb827e2ac078c7dad5ed52733632805`. Envelope parser SHA256: `3d876d648dc8dcbf023f5432b67ad13133e812df594a202cf6998b9ac9c8d4d3`.

The producer success/refusal JSON is the implementer's captured fixture at this portal pin, **not independently regenerated** in this review. It is intentionally combined with adversarial mutations and actual pinned client/parser execution. Earlier package review 490e6e9157 separately exercised actual directory/performance entries; its scope is not added to these counts or treated as combined browser proof. Whole-portal typecheck is the implementer's reported PASS, not independently repeated here. The new Python runner passed Ruff.

Initial reviewer harness run had two invalid assumptions: direct lowercase object lookup for an HTTP header, and expecting selection data to have report availability metadata. Inspection confirmed header case-insensitivity and `carryUnprojectedGrant`'s availability-only behavior; assertions were corrected before the final run. Neither was recorded as a product defect.

No mounted React/UI selection event, actual shared authenticated fetch/HTTP status behavior, real server response, current-access revocation, cache switch/race, provider response, report rendering, live route or deployed layer was exercised. Require M's completed mounted integration pin and a composed browser/producer candidate before claiming selection/date end-to-end acceptance. Replay hidden-retry identity, deliberate refresh lineage, S7 enforcement and operating gates remain unchanged. R-P07 closure 9e6a617405 is retained at its own primitive boundary.
