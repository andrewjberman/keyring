# Corrected bootstrap pair and header component review

Reviewer: `3.0.0_SA_CVO~P`. Date: 2026-09-23.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, directive `90eac8c562`, CTO exact notice `20260923T061459Z_1.0.0_SA_CTO_IRPT_candidate_updated567a157ec8__retain.md`, and COO P exact handoffs `061355` / `061639`.

**Bounded PASS at backend `567a157ec8b5465039bcc9e3842d24075e68947b` and Portal `dcf5e177f6513612f5e39ce90c016d098cc41aab`.** The original R-P12 assertions pass independently on this replacement pair: 11 backend tests and 10 frontend tests / 20 assertions. Separately, both supplied mounted header/browse harnesses and eight additional independent mounted component scenarios pass on this exact Portal source. No live, deployed package, CloudFront, visual or full-journey acceptance is inferred.

## Corrected bootstrap replay

`bootstrap_retest_567a.py` reads the prior committed replay wrapper at `71e114f69a`, changes only exact pins and temporary/output names, and executes the original driver from `008107ab97`. The driver verifies the original assertion files byte for byte against their committed contents before extracting source into a new independent temporary directory. Neither implementer replay results nor a mutable producer tree supplies the evidence.

- Python assertion SHA256 remains `67aa338c4810d39ed5ddc793c068cb9b492193bfa0a7c3de0887217c2e0dd4d0`.
- TypeScript assertion SHA256 remains `871486b830076681b85f2a11e1f1b56f4f705226c9a519b57f9603b8c33eb8b0`.
- Actual initial client request SHA256 remains `65818d36f1621cb948962667e328189ef77f18f69f685a9f3143a56b52132413`.
- Actual guarded response capture SHA256 is `fb226e9795c765fdaa3d31f9a8190c9085ee7a8a35655753d926f9ace1300aed`.

The actual client request, actual guarded Entry, schema validator, real envelope parser, adapter and LiveClient resolve succeed for advisor and operations fixtures. The flat account selector and selected-set positive control pass. Unverified origin, missing verified firm, foreign requested firm, unknown advisor and wrong contract version all remain public refusals accepted as refusals by the actual frontend. Old-pin closure was not transferred automatically.

Evidence: `bootstrap_retest_567a.json`, `bootstrap-request_567a.json`, `bootstrap-actual_567a.json`, and the separate wrapper. Existing dependency fixtures control external directory/ownership/policy data; no HTTP request occurred.

## Exact header source and mounted controls

`header_probe_dcf5.py` extracts committed Portal source and configurations with `git archive`. It builds the two exact supplied HTML harnesses and the independent reviewer harness into an isolated static test bundle. A headless Edge page fulfills asset requests from that bundle on the synthetic reserved origin `https://irpt-review.invalid`; all other origins are blocked. No local HTTP listener, proxy, live backend, auth change, CloudFront bypass or deployed application is used. Test dependencies come from the existing installed Portal dependencies.

The supplied `header-race.mjs` and `browse-race.mjs` assertions are retained. The runner adds only offline asset interception and supplies the synthetic test origin. Both pass independently. Their coverage includes waiting for server selection acceptance, selected-set identity propagation to holdings, changed selection clearing, late selection/context results, selection refusal, initial blank-query browsing, pagination, late page/query/context answers, and distinct empty/loading/error states.

The reviewer-owned `header_cases_dcf5.html` mounts the actual `SelectionWorkspace` with controlled scope and asynchronous API fixtures. The eight independent scenarios in `header_cases_dcf5.mjs` all pass:

| Scenario | Observed result |
| --- | --- |
| Bootstrap pending | Search disabled, loading explanation shown, no browse call |
| Bootstrap refusal | Search disabled, scope error shown, no loading panel or browse call |
| Missing directory revision | Search disabled with explicit unavailable explanation |
| Initial authorized browse | Blank query, limit 25, revision and tenant/fingerprint context, no cursor; verified single firm visible |
| Successful continuation | Same request context plus cursor; previous rows retained and next rows appended; exhausted cursor removed |
| Continuation refusal | Old rows and cursor removed; error shown without a false empty-results claim |
| Late rejected search | Newer successful rows remain; stale rejection does not display an error |
| Directory-only context change | Workspace remount clears query, starts blank query with new revision, suppresses previous context response |

The last test uses the same key expression as the actual page. Source inspection verifies the actual `InvestorReporting` key includes firm, scope fingerprint, revision ID and directory revision; the harness does not execute the top-level page's real query lifecycle. `ClientSearch` increments its generation on query/context cleanup, checks that generation before accepting success or failure, and preserves cursor request context. Firm and search components are the actual candidate code. No new production code was edited by this reviewer.

Evidence: `header_probe_dcf5.json` records source and reviewer hashes, commands, complete results and limitations. The first fixture build omitted `tsconfig.node.json`; the extraction was corrected before any tests ran. The final test bundle builds successfully. It emits CSS optimization, missing public-font and chunk-size warnings preserved in the evidence; this is not a pixel/layout or production build grade. Both new Python runners pass Ruff.

## Complementary evidence and remaining boundaries

CVO M's exact `061724` notice reports independent M-BOOT-01 closure `91d08f28ca`: unchanged 45-control scope/browse/input driver passes on backend `567a157ec8...`, with eight previously failing malformed requests separately verified as INVALID_INPUT/no data. This is attributed peer evidence; its suite was not duplicated here. The prior finding/report `5ccaad6d4c` remains historical evidence.

COO P's exact `061639` notice confirms this final implementation pair and reports a corrected staged archive, 17-member readback and flat cold import. This review has not independently examined or accepted that archive, its manifest, staging receipt, IAM or infrastructure plans. The reported manifest mixes shared dependencies pinned at `69144433df` with corrected Entry at `567a157ec8`; source/component results alone cannot establish package parity or deployed behavior.

Actual authorized HTTP, deployment identity, real directory/principal data, CloudFront-served DEV and Andrew's visual smoke remain separate acceptance steps. Multiple-firm and broader entitlement semantics are not newly graded by these eight component scenarios. Fresh exact-artifact plans and CTO apply authority remain required. This review changes no live incident or full-journey verdict.

## Reproduce

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/bootstrap_retest_567a.py
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/header_probe_dcf5.py
```
