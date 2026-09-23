# IRPT live scope and investor discovery repair

Owner/adjudicator: 1.0.0_SA_CTO. Authority: Andrew's current live smoke report, the completion CONTRACT.md and delegated worker-fork adjudication. This is an ordinary P/M completion repair, not a restart of the held B/F canonical cycles.

## Observed failure

Andrew reports: "Scope could not be resolved. Nothing below is scoped, so nothing below is shown."

On clarification: "After typing an investor name in the input box. there is no option for firm selection anywhere, nor is there a loaded paginated list".

The deployed Portal is PROD e83ebbfe4f83228f42925b24f77f43e6b6d2a037, tag portal-v2.1.184 (peeled independently), deployed by successful run 35820826235. DEV 3a298311dfab63928e7b912e0f62355ec8b7ce59 has successful CI 35820519811 and an identical tree. Publication success does not close this failed live journey.

CTO measured source facts on the promoted tree:

- InvestorReporting/index.tsx emits this exact message for the resolve-scope query's isError state. The request is POST /api/scoped/investor-reporting/directory/resolve through the shared authenticated apiRequest transport.
- An errored scope becomes null. FirmDropdown renders nothing without more than one permitted firm; ClientSearch creates no search runner without scope, but still renders an editable input. The timing of an error after typing does not by itself establish that a directory-search request caused it.
- The current ClientSearch starts with no rows and implements a minimum-two-character, 25-result type-ahead query. It has no initial browse load or paginated investor-list control.
- The actual failing HTTP response/runtime cause has not yet been measured. P reports the preceding backend push deployed zero functions and skipped first-mint missing functions; M must measure the relevant live directory/scope route rather than infer availability from merged code.

## Ownership and execution

M remains the sole directory/scope/header/shared-selection integration owner under CONTRACT section 3. M owns initial authorized investor browse, firm context, and pagination semantics. P coordinates the live repair and integrates shared API transport, wire adapters, route declarations, and runtime composition. Exact delegated file claims must be agreed before edits; no competing header writers. CVO M independently grades selection/access and CVO P grades the assembled HTTP/UI boundary.

P and M first produce the exact failed operation, status/public reason, live target/configuration, missing dependency or defect, and a bounded repair/deployment plan. Preserve sensitive client evidence in protected locations; messages and logs carry sanitized diagnostics and references.

## Acceptance

1. Authorized page entry resolves real permitted scope; loading, failed lookup, and genuinely empty permissions are distinct. A failed bootstrap cannot leave an apparently functioning search that performs no request. No guessed firm catalogue, fixture fallback or broadened permission.
2. The user can see the current authorized firm context and select among permitted firms. A single permitted firm is visibly identified even when there is no choice. An unavailable catalogue is explained rather than silently disappearing.
3. An initial authorized investor list loads without requiring a guessed investor name. Search filters the list; pagination uses the actual server contract, with stable ordering, bounded pages, and explicit loading/empty/error states. Firm/search changes reset pagination and stale responses cannot cross contexts.
4. Selection continues through the existing server-accepted selected-account-set contract. Cross-firm/foreign-principal negative controls remain enforced; permission revocation and stale cursors cannot expose rows.
5. Review the exact assembled producer/consumer pins, then measure the real deployed HTTP/UI journey. Offline fixtures, a build, an unrelated route, or a successful frontend deploy cannot close this live failure. Andrew performs the visual smoke.

Existing render-key/render-deployment, vendor-egress, and other reserved operational gates remain scoped to their actual actions. They do not stop the unrelated directory/header repair. If runtime provisioning is required, prepare the concrete least-privilege change and route its actual gate to CTO; do not issue a blanket deployment or bypass.

Status at creation: OPEN. P and M have received the exact report, source findings, owner allocation and acceptance target. No live fix or smoke PASS claimed.
