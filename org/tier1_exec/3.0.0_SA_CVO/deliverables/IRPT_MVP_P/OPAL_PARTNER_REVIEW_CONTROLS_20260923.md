# Narrow resumed Opal/partner review controls

Owner: `3.0.0_SA_CVO~P`. Status: **PREPARED; replacement review UNFINISHED / NOT EVALUATED.** No replacement source pins have been supplied as of the exact COO P `20260923T131532Z` notice. This is a control specification, not executed candidate tests or a verdict.

Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, CTO exact notices `131358` and `131629`, and its full `LOCAL_LIVE_PARTNER_SCOPE_20260923.md`. Andrew narrowly resumed localhost/live-data iteration for this repair. Other work remains held; no cloud apply or Portal promotion is authorized.

## Known baseline and actual module boundaries

CTO reports authenticated browser HTTP 200 with `ok:false`, status UNAVAILABLE / reason UNEXPECTED. Its exact deployed-byte offline reproduction produces Opal null-selector BucketUnmapped and explicit partner FIRM_BINDING using synthetic identity, the real bucket map and a fail-if-called S3 stub. That record distinguishes real signed-in browser evidence from synthetic server reproduction. This reviewer has not independently repeated the live trace and does not call the synthetic reproduction an actual token capture.

Portal reported base is `fac3b6a0c7cb55dd75d3c190a1382ce710030381`; CTO local launcher source is `de405810577ac0c3b427ff9b54c877d03ec9ab2e`. These are baseline references, not replacement candidates. Reading the exact latter source identifies these seams:

- `InvestorReporting` creates the actual API and calls `resolveScope` from `useQuery`. Its bootstrap key contains literal bootstrap segments plus selected firm. Authenticated identity is not visibly present in that page key; whether outer auth/query lifecycle clears it must be tested, not inferred as a leak from the key alone.
- The initial `global` choice serializes a null requested firm. The page waits for ResolvedScope before passing a verified firm catalogue to `FirmDropdown`. The replacement must break that bootstrap dependency without granting access from browser identity.
- The page remount key carries firm, scope fingerprint, revision ID and directory revision. Actual auth changes, not only a synthetic remount, must invalidate the previous principal's results.
- `SelectionWorkspace` sends an actual server selection request, then derives downstream tenant from resolved scope and accepted selection references. Global-to-selected-firm transitions must be inspected and exercised so a global/Opal placeholder cannot become the data tenant.
- Existing pure firm helpers expose Global and derive the rest from server-permitted firms. They do not by themselves demonstrate real Opal roster authority or partner enforcement.

Existing reusable reviewer harnesses at `169301f2cd` are `bootstrap_retest_567a.py`, `header_probe_dcf5.py`, and `header_cases_dcf5.{html,mjs}`. Their controlled fixtures cannot close the resumed live gap. The new browser layer must mount the actual top-level page with actual auth/query lifecycle and the actual LiveClient/transport, rather than replacing the API or directly injecting a fabricated ResolvedScope and calling that signed-in proof. Controlled asynchronous fixtures remain useful for adversarial race scheduling and are labeled separately.

## P reviewer control matrix

All rows are **NOT RUN on the replacement**. Capture source/serving pins, principal class, selected/requested tenant, operation, sanitized request shape, response status/reason and whether old data survives. Do not record tokens, passwords, raw investor data or full authenticated headers in deliverables.

| ID | Actual module or boundary | Stimulus and required observation |
| --- | --- | --- |
| OP-P01 | Auth context -> page initialization -> LiveClient | Real signed-in Opal starts Global before successful directory resolution. Capture actual initial serialization; no lookup of a global or opal-capital directory bucket and no arbitrary first partner fallback. |
| OP-P02 | Auth context -> firm control -> bootstrap | External firm user starts and remains in its own firm. No Global/foreign option becomes enabled via browser identity or a stale Opal catalogue. Missing auth does not issue an entitled bootstrap. |
| OP-P03 | Actual client/transport -> server boundary | Manipulate requested firm/global selectors without modifying trusted transport identity; partner cross-firm/Global and forged entitlement claims must be refused. Coordinate server proof with M; do not duplicate its full sweep. |
| OP-P04 | Global response -> real parser/adapter -> rows | At least two authorized firms appear with unambiguous attribution, including duplicate display names. No unauthorized firm is queried or included; no first-firm-only result labeled complete Global. |
| OP-P05 | Global partial/empty/unavailable -> rendered state | Distinguish all-empty authorized result, one unavailable authorized firm with partial coverage, and total refusal/unavailability. Retain coverage/failure context rather than showing partial as complete or unavailable as empty. |
| OP-P06 | Firm choice -> resolve -> browse request | Switch Global to permitted firm and between permitted firms; capture selected firm through real request serialization. Distinguish opaque firm IDs from registry tenant IDs; client identity labels do not mint entitlement. |
| OP-P07 | Query/cache -> signed-in identity transition | Reuse the actual query client through logout/login as a different principal. Prior bootstrap, firm catalogue, rows, cursors and accepted selection cannot be read as current even before new requests settle. Verify outer cache invalidation as well as keys. |
| OP-P08 | Actual login/reload | Reload the real signed-in local page through its existing CloudFront-backed transport. Preserve authorized initial choice behavior, with fresh identity validation and no bypass, hard-coded principal, or borrowed token. |
| OP-P09 | Firm/context generation -> async results | Delay old resolve, page and selection success/failure; switch firm or identity and settle old responses afterward. No stale rows, error, confirmation or downstream request may overwrite the current context. |
| OP-P10 | Browse/page/search -> real client | Initial blank-query bounded page; successful next page; query changes reset cursor. Assert selected firm, directory/entitlement context, query and continuation survive actual serialization and late pages are discarded. |
| OP-P11 | Directory search -> Resolution -> accepted selection | Choosing a row confirms client/relationship/accounts in the existing Resolution area only after server acceptance. No separate client entitlement step or constructed successful ResolvedScope. Refusal clears previously accepted state. |
| OP-P12 | Accepted selection -> downstream reads and caches | Follow the selected result's tenant and accepted account-set identity through each exercised read and cache key. Global is a browse context, not an accepted single-tenant report identity. Mixed/foreign account binding must fail at the server. |
| OP-P13 | Missing/stale roster -> visible choices and state | Server-authority failure must not resurrect a cached Opal catalogue or silently select the first firm. Pair browser observations with M's real Entry missing/stale-roster controls. |
| OP-P14 | Prior bounded safety controls | Replay appropriate unchanged original bootstrap authorization/refusal assertions on exact replacement source where the contract remains applicable. Record intentional contract changes explicitly; never weaken an assertion to turn a new failure into inherited PASS. |

## Coordination and execution gates

The complementary split is confirmed by CTO's exact `131832` notice and M's exact `131857` notice after M consumed its direct `131715` narrow resume. P reviews actual frontend/page/client serialization, auth/cache lifecycle, browser races and Resolution confirmation. M reviews real Entry roster authority (including missing/stale/revoked authority), partner Global/cross-firm forgery, unauthorized-firm query isolation, incomplete Global semantics, selected account tenant binding and server cursor/cache isolation. Both await immutable candidate pins; M also awaits the roster contract. The exact localhost:5174 dev:live route through CloudFront is within the narrow resume, with no bypass or deployment permission.

Start candidate execution on immutable paired backend and frontend pins plus identified dependencies/contracts. Independently extract committed bytes; keep old evidence immutable. Preserve failing controls unchanged for a repair retest. Record real authenticated evidence separately from controlled-module tests and from producer claims.

Before claiming live closure, identify the source actually serving the signed-in page and the deployed backend artifact/config. If replacement source has not reached the real serving boundary, report that limitation and keep live status open. Do not apply it as part of review. Use only the authorized normal login/CloudFront-backed route; no copied origin secret or client-forged trusted headers. Do not modify or stop CTO's localhost instance.

Await P's exact pins and safe evidence references; no credential material should be sent in messages. Return concrete defects/proof to CTO. No candidate PASS, no deployed PASS and no reopening of other held work is implied by this preparation.
