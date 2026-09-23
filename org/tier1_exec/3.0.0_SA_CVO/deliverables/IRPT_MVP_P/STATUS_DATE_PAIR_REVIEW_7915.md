# Paired Entry/date review: bounded date PASS; public refusal contract HOLD

Reviewer: `3.0.0_SA_CVO~P`. Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, IRPT-Y-DATES-01 at `dea338a397`, and CTO 20260923T010714Z direction.

Actual pair tested: backend **`7915bc9b2c3d264d6b2560989b01dc57565f556f`**, portal **`cf77e5db12025899a31340b57dd54327d311f348`**. The separately advertised assembled portal endpoint `42412eb8` is not substituted for this pin and receives no independent mounted/runtime verdict here. Exact backend and portal files are reconstructed into an isolated temporary snapshot; reviewer code does not alter either producer tree.

## R-P11 — P2: raw refusal wire conflicts with its server-only status contract

All four actual owned Entry refusal families (history, request read, sections, job status), triggered by unsupported contract version, return `status.internal_correlation_id` to the caller. Four independent assertions requiring the schema-marked server-only field to be absent **FAIL**. They call the actual `build_owned_entry` boundary with the actual retained reader setup; no response body is synthesized by the reviewer.

The new `BoundaryRefusal.schema.json` references the internal `StatusEnvelope` and therefore validates/requires that field. Its description says it records existing opaque diagnostic behavior. This conflicts with the same pin's public boundary rules:

- `docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json:229` marks `internal_correlation_id` with `x-server-only: true` and describes it as server-side.
- `PublicStatusEnvelope.schema.json:5` says the public projection removes schema-marked server-only members; success status data actually does so.
- `infra/aws/lambda/investor-reporting/ops/status.py:223` defines `public_view()` as what may cross to a caller, minus every schema-marked server-only property.
- `_authz/served.py:215` acknowledges the server-only marker but retains the opaque value for operator correlation. Opaqueness and established behavior do not resolve the public-wire contract conflict.

This is a concrete unresolved pairing/contract conflict, not a claim that `7915bc9b2c` newly introduced the underlying runtime behavior. The tested field is an opaque generated diagnostic, not a credential or demonstrated cross-tenant data leak. No deployed endpoint was called. Absence from rendered UI cannot prove absence from the response wire.

**Requested disposition:** reconcile actual refusal projection and its schema/types/fixtures with the applicable server-only rule, or obtain an explicit authoritative disposition of the conflict before claiming public refusal closure. Preserve internal operator correlation separately and preserve refusal reason, safe actions, state and payload exclusion. Supply an exact paired replacement; rerun these four assertions unchanged unless an explicit ruling changes their governing expectation. The reviewer does not widen or edit a producer schema to turn this red result green.

## Measured successes and proof limits

| Evidence | Independent execution result |
| --- | --- |
| Supplied actual Entry/date/outer-contract tests | 65 PASS |
| Reviewer backend schema/date/legacy/refusal controls | 15 PASS; four server-only wire cases FAIL |
| Supplied portal pairing tests | 12 PASS, 69 assertions |
| Reviewer fresh-response parser/static component cases | 20 PASS, 64 assertions |
| Actual wire generation | 19 document types, 16 response types from 16 route declarations; zero differences from committed output |
| Ruff for new Python artifacts | PASS |

The producer's reported 70/34 and TypeScript results are not adopted as reviewer execution. The selected supplied tests above are the actual rerun denominator. Local Bun executes the portal tests; full TypeScript compilation is not independently claimed here.

The date control outcomes support a **bounded PASS** for the tested negotiated shapes and public success pairing:

- Fresh retained Entry output carries UNDATED_INPUT or PER_SECTION only with the prospect operation, immutable accepted input/request/report binding and complete stable section census. Mixed dated/undated sections preserve dates and explicit null section dates; `business_date` is absent on the extension.
- Ordinary single-date output retains the actual business date and no extension. It validates against the old schema's public projection and survives the paired parser. The old-schema check removes only the legacy server-only correlation member; it is not an execution of an old browser.
- No-capability requests receive UNAVAILABLE with empty source dates; extension output is rejected by the old schema projection. Altering accepted process time does not change the replayed source-date meaning. No physical browser reopen or clock-service proof is claimed.
- Wrong outer/inner operation, wrong lane, mismatched input/request, mutable/numeric revision, null basis/business date, unknown date field, impossible date, missing/duplicate section, missing grant and unknown outer field are refused in the exercised schema/parser cases.
- Four actual origin refusals validate against the declared refusal schema and remain payload-free; injecting `data` refuses. The separate four server-only checks expose why schema conformance alone is insufficient for a public-wire PASS.
- The current runtime and versioned internal/public StatusEnvelope schema bytes match. Explicit generator invocation reproduces all 19 documents and 16 responses without differences. Route declarations are the generator denominator, not evidence that the new factory or routes are installed.

Fresh date fixtures exactly equal the committed portal JSON. Fresh outer fixtures differ only in the four regenerated refusal correlation values. Evidence records raw inequality and comparison with only those rotating fields excluded; that comparison diagnoses nondeterminism and does **not** authorize their disclosure. Raw captured responses are retained unchanged.

## Reproduction and retained evidence

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/status_date_pair_probe_7915.py` from the repository root. Expected exit **1** at this pin because the four server-only assertions fail. The probe regenerates both fixture files through `_contracts/test_owned_outer_contracts.py` with explicit output paths, runs separate reviewer backend and portal assertions, and regenerates types only inside its temporary snapshot.

- `status_date_pair_probe_7915.json`: exact runs, outcomes, pins, capture and source hashes.
- `status_date_pair_cases.py`: independent backend assertions, SHA256 `cb151804b34e06e5948781affaabd17fb71f97d5615f360c5e7ae9e4b24e2a9b`.
- `status_date_pair_cases.test.tsx`: independent parser/static assertions, SHA256 `7843f9df99a62e1e7302f7e9f5c5b271ef79ec345a52e42777f50691f8cf24a3`.
- `status_date_actual_dates_7915.json`: regenerated actual date outputs, SHA256 `e01467d21c7e78276e1f642a69f33ad09ab80a86b6d46a9c7f21b7607d494101`.
- `status_date_actual_outer_7915.json`: raw regenerated success/refusal examples. Correlation values intentionally vary per regeneration.

The initial isolated harness omitted the `ycharts/generate` dependency and did not collect backend tests. The final probe includes that pinned dependency and the counts above come from completed execution; the setup error is not a producer finding. Wire generation explicitly calls `generate()` rather than treating a silent module invocation as proof.

## Remaining boundaries

CVO Y's Y-DT01 closure `c9e892bf9a` on `8dbc742bb1a89a277fc41183efc0f785bb9027f6` is retained as bounded manual-hooks/static evidence; this review does not reopen it or adopt its counts. Y's owned-reopen `c470e652ad` on `38a3ea24412310165f0dfb09912e1997de445631` is likewise attributed peer evidence. It is not an actual browser/current-service proof.

Public refusal pairing remains HOLD for R-P11. Actual browser/export, installed factory/route/runtime, vendor certification, custody/performance end-to-end date regression, atomic final access checks and the full integration criteria remain unevaluated by this review. The earlier R-P10 closure `e00d957e7c` and inventory HOLD lift stay limited to exact package `f0f391d6a5`; neither is reversed by this separate finding. No live access, render authorization, deployment, push or broader acceptance follows from this review.
