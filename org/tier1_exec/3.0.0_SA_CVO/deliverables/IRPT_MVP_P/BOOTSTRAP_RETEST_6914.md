# R-P12 independent bootstrap retest

Reviewer: `3.0.0_SA_CVO~P`. Date: 2026-09-23.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, live-scope directive `90eac8c562`, and exact CTO handoff `20260923T060635Z_1.0.0_SA_CTO_IRPT_review_handoff69144433df_plus_cdc60.md`.

**R-P12 CLOSED for the original bounded offline client/producer/consumer contract failure at the pair below.** Independent replay passes all 11 backend tests and all 10 frontend tests (20 assertions). All five original failing backend cases and all four original failing frontend cases now pass. The five authorization-negative families continue to refuse on both sides. This does not close the live scope incident, broader scope semantics, initial browse/header acceptance, or a full journey.

## Exact pair and independence

- Backend: `69144433df8c4938cf95cb81e46ac04ae72cc61e`.
- Portal: `cdc60da247597940b278dd43779b3953565093b7`.
- Original review/assertion commit: `008107ab97`.
- Actual extracted directory Entry SHA256: `41256ae9edb0ca362151fb5ce5113f05b570bc270bd9ee52e43c11faf1591539`, matching the handoff.

The reviewer independently extracted committed source with `git archive` into a new temporary directory. Neither the implementer's working tree nor its replay receipt was used as test evidence. `bootstrap_retest_6914.py` reads the original committed driver, verifies both local assertion files against their committed bytes, and adapts only source pins, temporary/output names, and the scope statement. Original driver capture logic and test assertions remain unchanged; original baseline output files are preserved.

| Original assertion file | SHA256 |
| --- | --- |
| `bootstrap_cases_cd8.py` | `67aa338c4810d39ed5ddc793c068cb9b492193bfa0a7c3de0887217c2e0dd4d0` |
| `bootstrap_cases_cd8.test.ts` | `871486b830076681b85f2a11e1f1b56f4f705226c9a519b57f9603b8c33eb8b0` |

## Observed result

The actual `LiveClient.resolveScope` still sends the same flat initial request to `POST /api/scoped/investor-reporting/directory/resolve`: null firm/client/relationship selectors, empty account IDs, and null entitlement revision. Request capture SHA256 remains identical to the baseline: `65818d36f1621cb948962667e328189ef77f18f69f685a9f3143a56b52132413`.

Actual guarded `ENTRY.handle` now returns the published ResolvedScope document for both established verified advisor and operations fixtures. The response includes server policy, principal class, verified firm, entitlement revision, both permitted accounts and fingerprint, requested/resolved FIRM scope, and directory revision. A flat explicit account request is recorded as requested ACCOUNT scope. The real schema validator, actual `parseIrEnvelope` / `adaptResolvedScope`, and actual `LiveClient.resolveScope` all accept the returned document. Existing selected-account-set positive control also passes.

Source inspection confirms the resolve operation now consumes flat selectors and invokes the canonical scope resolver with guarded directory, ownership, policy and revision artifacts, checks that its permitted set cannot expand the guarded set, and returns `browser_safe_view`. The old selection-result return shape is removed from this operation. This inspection supports the observed repair; full scope algebra and browse/cursor correctness remain the separate M review.

Unverified origin, missing verified firm, foreign requested firm, unknown advisor, and unsupported contract version remain public refusals without data or exposed internal correlation ID. The published valid frontend fixture remains a positive control.

## Reproduction and artifacts

Run from the repository root:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/bootstrap_retest_6914.py
```

- `bootstrap_retest_6914.json`: exact pins, original assertion hashes, source hashes, independent command results and limits.
- `bootstrap-request_6914.json`: real client request capture.
- `bootstrap-actual_6914.json`: real guarded producer responses; SHA256 `fb226e9795c765fdaa3d31f9a8190c9085ee7a8a35655753d926f9ace1300aed`.
- `bootstrap_retest_6914.py`: separate replay wrapper; Ruff passes.

## Remaining limits

External directory, ownership and policy dependencies use the existing controlled fixtures. No HTTP network, deployed backend hash measurement, real browser, runtime apply, provider access, or rendering occurred. The implementer's additional browse suite was not rerun or adopted as independent evidence. CVO M owns the complementary full-scope, authorization, browse/cursor/context review. Header/UI changes remain separate. Initial authorized listing, visible firm context, pagination and stale-response reset require their own exact candidate evidence; live acceptance still needs deployed HTTP and Andrew's CloudFront-served DEV review. Package proof and fresh exact-artifact plans remain prerequisites to the CTO live-apply ruling.
