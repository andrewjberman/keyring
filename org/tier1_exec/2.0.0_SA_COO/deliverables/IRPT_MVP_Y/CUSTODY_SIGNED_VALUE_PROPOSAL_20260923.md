# Custody signed-value policy proposal

Owner: `2.0.0_SA_COO~Y`. Status: PROPOSED, for direct CTO review.
Authority: CTO exact inbox message `20260923T152436Z_1.0.0_SA_CTO_IRPT_CTO_consumes_factory_and_actual_sou.md` under the IRPT completion CONTRACT.
Source inspected: Y `819c9e399086cffb2876a21fbc2cee01724b0bd7`.
Producer evidence: M `abfb3eaf8242cf5df26c7e1074e0e555245d969a`, `CUSTODY_NORMALIZATION_SOURCE_HANDOFF_20260923.md` and companion JSON.

## Recommendation and immediate behavior

Keep both production source callbacks unconfigured/refusing. Do not expand the existing normalized-portfolio v1 or recipe admission to signed/zero holdings. First require an accepted security-level custody source and a server-owned snapshot binding. Preserve signed and zero positions as source evidence; refuse the entire selected portfolio for analysis when any actual position cannot be represented by the selected recipe. No absolute values, omitted rows, synthetic cash, model substitution, gross-as-net conversion, or offsetting positions to conceal a short.

The proposed distinction is between preserving source facts and accepting them for analysis. A retained source record is not a NORMALIZED_PORTFOLIO eligible for dispatch. Any new retained artifact family or schema must be agreed with P and the retention owner before implementation; this proposal does not create one. Existing authorized source receipts remain the evidence of refusal meanwhile.

## Exact current downstream compatibility

Paths below are relative to `infra/aws/lambda/investor-reporting/` at the Y pin above.

| Boundary | Current rule | Consequence |
| --- | --- | --- |
| `intake/portfolio.py:_row_amount`, `_number` | Decimal provenance; spelling excludes negative sign and numeric value must be greater than zero. Numeric domain bounded to 28 digits/exponent magnitude 18. | Signed and zero rows cannot be frozen by the present API. The same helper validates positive price and reference notional; changing it globally would widen unrelated rules. |
| `intake/portfolio.py:freeze_parsed_portfolio` | Retains every original row and sums by resolved security; USD copied, shares multiplied by a dated positive USD quote, weights use explicit notional. | The consolidation is safe for the current positive domain. It must not be reused to cancel signed source positions before eligibility checking. Weights are not actual custody AUM. |
| `ycharts/generate/normalized_input.py:_amount`, `prepare_normalized_upload` | Exact decimal text, strictly positive values and total, canonical identity, no cash adjustment. | Rehashed signed/zero artifacts still cannot enter the actual normalized upload preparation. |
| `ycharts/generate/recipe.py:_dollars`, `holdings_csv`, `step_upload`, `items_body` | Strictly positive dollar amounts for CSV, vendor echo reconciliation, and portfolio items. | A normalizer-only relaxation is incompatible with the upload and create/readback path. |
| `ycharts/generate/recipe.py:validate_envelope` | Its legacy envelope check rejects negatives but permits an individual zero if the total is positive. | This weaker check does not establish zero compatibility: the later `_dollars` gate rejects it. Do not use envelope success as acceptance evidence. |
| `ycharts/generate/frozen_worker.py:prepare` | Reads accepted bytes and calls `prepare_normalized_upload` before returning worker inputs. | Keep refusal before transport; never refresh, net, or repair accepted input during replay. |
| Published `RequestComposition.schema.json` plus `CompositionAdmission` | Shape/owner/source binding and hash validation; semantic normalized input handling is Y-owned. | A schema-valid envelope or matching hash is not proof that signed economics are supported. Pair any future semantic version with submission and worker gates. |

No live vendor behavior was queried. Positive-only behavior above is a local source constraint; it does not claim that the vendor supports or rejects shorts or zeros economically.

## Proposed source representation and eligibility

The future source contract must carry each actual position's account, immutable position/lot identity, original signed decimal text and units, canonical security mapping revision, exact custody clock, accepted publication locator/version/revision, and source receipts. It must enumerate the whole selected account population, including empty accounts and all cash/liabilities, and independently reconcile each account before aggregation. Missing/unknown is never numeric zero. Keep corrections linked to their original rows.

1. Preserve finite positive, negative, positive-zero and negative-zero spellings verbatim in source evidence. A separate exact Decimal value may normalize either zero for arithmetic; retain its original spelling. Reject NaN/infinity/boolean, unbounded numerics, ambiguous units/currency or unknown valuation. Proposed initial numeric limits remain the existing bounded domain; do not truncate values to fit.
2. Preserve actual USD amounts. Signed shares require an admitted exact-date, positive USD price and its real revision; no price can be inferred from an account total. A zero quote is not a zero position. Do not accept weight/model inputs as a custody source.
3. Compute net value, positive subtotal, signed negative subtotal and gross exposure separately from the complete source rows. Require net = positive + negative and gross = positive - negative as consistency checks, in addition to independently sourced account reconciliation. These diagnostics do not authorize the vendor recipe or select an economic denominator.
4. Check recipe eligibility against the original position census BEFORE combining accounts or equal security keys. Any negative or zero actual row refuses the whole current positive-only recipe, even when its security's consolidated value and the portfolio net are positive. Positive cash with explicit canonical CASH identity remains subject to all existing source and reconciliation requirements; cash debit and zero cash are unsupported, not adjusted.
5. For an eligible all-positive source, preserve the full row-to-security contribution mapping and use the existing exact-dollar normalization. Do not treat a complete positive display tree as an accepted security source: M's COT/INF missing securities and 49F allocation/custody completeness problems remain blockers.
6. An idempotent retry uses the already accepted retained input under current authorization. A changed same-day publication is a new source revision, not an automatic retry upgrade. Snapshot authorization must compare the admitted server binding, never hash a selected/redecorated slice as the whole-publication revision.

Proposed internal refusal distinctions: snapshot binding unavailable/changed, security census unavailable/incomplete, unknown valuation, and recipe unsupported signed/zero position. Public reason-code/schema changes belong to P; do not add undeclared wire enum values. Return existing supported refusal envelopes until a paired mapping is committed. Report row coordinates only within current authorized scope.

## Any future signed recipe is a separate admitted change

Do not relax `_number`, `_amount` or `_dollars` merely to pass a fixture. A new recipe/version would need an explicit short/liability/cash/zero policy, supported gross/net/leverage denominator, lossless transport representation, and exact signed/zero upload echo, create/readback and final-report evidence. A vendor accepting a CSV is insufficient. If zero rows or offsetting lots cannot be represented faithfully, that recipe remains ineligible for the entire portfolio; it cannot silently discard them. Hashes and retained references must distinguish the new policy/version, and historical positive-only requests keep their frozen semantics. No such economic acceptance or live execution is authorized by this proposal.

Required paired controls before enabling any new domain: all-positive baseline; positive plus zero; positive plus negative-zero; short with positive net; equal-security long/short that nets positive or zero; negative cash; all-zero and nonpositive net; missing value versus explicit zero; duplicate lot IDs; duplicate parent/child counting; missing selected account; incompatible date/currency/price; wrong tenant/account/snapshot; same-day revision drift during read; revocation before retention and effect; retry after source changes. Assert both exact preserved source provenance and no acceptance/dispatch/vendor call for every unsupported case. A future admitted recipe additionally needs signed echo/readback evidence, not just mocked parser success.

## Ownership and evidence limits

CTO decides bounded producer scope and policy disposition. M supplied facts, not a security source implementation. Y owns normalization and recipe gates; P owns shared integration, wire/schema agreement, package and runtime placement. P reports `e47aed7f71` consumed exact Y819c and docs4be, reproduced 30 factory tests and 265 generation/intake tests plus 50 subtests, verified 29 module hashes and a 73-member flat import/construction with refusing synthetic source ports. Those are P-reported local results, not a Y rerun or installed runtime.

This document changes no production code, schema, numeric acceptance, source callback, package, runtime or cloud state. The inspection found no `NormalizedPortfolio.schema.json` in the published v1 directory; the local document version and semantic gates above are the relevant existing contract. No new test run or economic PASS is claimed. Existing source819c and its prior evidence remain unchanged.
