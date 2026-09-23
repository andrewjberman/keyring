# R-P12: actual bootstrap producer/consumer contract failure

Reviewer: 3.0.0_SA_CVO~P. Authority: org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md, live defect directive 90eac8c562 and exact CTO operative review GO 20260923T051852Z.

**FAIL reproduced across actual modules before repair.** Source backend `cd8d11825424e45fe82f1e78df0396904c0b9ae0` paired with published Portal commit `e83ebbfe4f83228f42925b24f77f43e6b6d2a037`. The backend pin is the prior reviewed source baseline, not a claim that its hash is currently deployed. This finding corroborates CTO's source diagnosis; it does not establish the status or cause of Andrew's actual failing HTTP request.

## Reproduction and result

The driver reconstructs both exact Git snapshots. It calls the real `LiveClient.resolveScope` with the initial request read from InvestorReporting/index.tsx: tenant cache token `bootstrap`, null requested firm/client/relationship and empty requested account list. A controlled transport captures the real serialized request; no HTTP call occurs:

```json
{"firm_id":null,"client_id":null,"relationship_id":null,"account_ids":[],"entitlement_revision":null}
```

Method/path: `POST /api/scoped/investor-reporting/directory/resolve`; contract header: `X-Contract-Version: v1`. Existing directory selection test fixtures supply verified principal headers and the directory/ownership/policy loaders. Only the real ENTRY's dependency ports are replaced. Its actual guard, id projection, resolve function, pure handler and envelope builder all execute. Advisor and operations principals each have two permitted accounts.

Both bootstrap responses have the expected v1 outer operation/firm/data/grant structure, but `data` is a selection result with `ok:false`, `resolved_scope:UNSUPPORTED`, empty `account_ids`, zero `account_count`, null `fingerprint`, `provider_calls:0`, and the reason that selection matches nothing. The published ResolvedScope rejects the extra selection-result fields and requires seven absent fields: viewer_policy, principal_class, entitlement_revision, verified_request_firm_id, permitted_account_set, permitted_account_set_fingerprint and requested_scope.

The fresh producer responses are then fed to the actual `parseIrEnvelope` / `adaptResolvedScope` path and actual `LiveClient.resolveScope`. Both principal lanes fail with `EnvelopeMismatch`, field `data`, public reason `ENVELOPE_DATA`. The parser invokes the real scope adapter, whose required scope members are missing. An independently supplied published-valid document remains a passing adapter/parser control.

Separately, sending an actual flat account request also leaves the selection empty. Source `directory/entry.py:resolve` reads `params.get("selection") or {}`. A nested-selection diagnostic reaches the real handler and returns the two accounts in the fixture's shared directory entry, demonstrating the different carrier it reads. That diagnostic still is not a valid ResolvedScope and is not a recommended repair or a new public contract. The flat request assertion requires that the agreed requested account be recorded in requested_scope; the baseline does not do so.

| Unchanged reviewer assertions | Baseline |
| --- | --- |
| Backend: published bootstrap response and permitted scope for two principal lanes; flat requested-account record | 5 FAIL |
| Backend: five auth-negative families plus existing actual selected-set positive | 6 PASS |
| Frontend: actual parse/adapter pipeline and LiveClient for two principal lanes | 4 FAIL |
| Frontend: published-valid document plus five fresh actual auth refusals | 6 PASS, 12 assertions |
| Actual client request capture | PASS |
| Ruff, two reviewer Python files | PASS |

Preserved negative controls are unverified origin, missing verified firm, foreign requested firm, unknown advisor, and unsupported contract version. Each remains a valid public refusal without data or internal correlation and is refused by the actual frontend. The existing actual server-accepted selected-set positive still passes. The failure is not caused by disabling the guard or replacing it with a copy.

## Immutable evidence and repair retest

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/bootstrap_probe_cd8.py`. Exit 1 is the recorded failing baseline, not a successful candidate verdict. `bootstrap_probe_cd8.json` retains complete outputs, source hashes and snapshot path. `bootstrap-request_cd8.json` and `bootstrap-actual_cd8.json` retain the actual request and fresh controlled producer results, including the nested diagnostic and auth controls.

- Backend assertion file `bootstrap_cases_cd8.py`: SHA-256 `67aa338c4810d39ed5ddc793c068cb9b492193bfa0a7c3de0887217c2e0dd4d0`.
- Frontend assertion file `bootstrap_cases_cd8.test.ts`: SHA-256 `871486b830076681b85f2a11e1f1b56f4f705226c9a519b57f9603b8c33eb8b0`.
- Actual request capture: SHA-256 `65818d36f1621cb948962667e328189ef77f18f69f685a9f3143a56b52132413`.
- Actual response capture: SHA-256 `2c313e8ac40efbcc4c472b3f10eb4ffb3560b79ad79b5a0373c0a77c10761ba9`.

Preserve these assertion bytes for the exact repair candidate; a separate retest driver may select new producer/consumer pins and new output names. Do not replace this failing capture or weaken expected behavior to accept selection-result data, invent policy or bypass current authorization. P/M own implementation. CVO M retains selection/access review; CVO P retains assembled consumer/HTTP boundary review.

## Live boundary

This is an actual-module exercise with controlled external dependencies. No network, real UI, live backend configuration, credentials, provisioning, rendering or vendor call was used. The source behavior is consistent with a bootstrap query rejecting before search typing, but the real failing HTTP status/public reason and deployed cause still require measurement. Initial browse/pagination/firm visibility and the five live acceptance criteria remain open. Andrew performs visual smoke. Prior consumer PASS and successful frontend publication do not close this incident; no full-product grade is changed.
