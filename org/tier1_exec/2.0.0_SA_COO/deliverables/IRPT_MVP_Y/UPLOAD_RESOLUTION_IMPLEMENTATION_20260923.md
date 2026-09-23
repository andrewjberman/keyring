# Upload resolution: local implementation and exact integration handoff

Y source **6cfe01c3e238e9a90e88d3a501b25ac0eaf41540**, isolated branch
`irpt-mvp-y-20260922`. Ancestors e203236b6a and54a9262488. Authority fd32cac392,
57c263bee4 and078349b96c. This is a partial source implementation, not a completed
upload journey, installed service, global serialization proof or live acceptance.
CTO reviews directly; P's existing paired1385 integration remains first priority.

The companion `UPLOAD_RESOLUTION_IMPLEMENTATION_EVIDENCE_20260923.json` contains
the exact 15-file delta from1385, synthetic executable v2 examples, fixture hash
and checks. No new source producer, secret read, vendor call or deployment occurred.

## Implemented and exercised

- Dedicated `intake/template_reader.py`: A/B-only CSV/XLSX, relationship-based
  selected worksheet, exact source text/coordinates, four bases, complete bounded
  findings, formulas refused, cash/duplicate notices, weight tolerance/percent proposal.
- `portfolio.freeze_template_portfolio`: explicit v2 discriminator; v1 path retained.
  Exact Decimal USD, current/target/reference-notional and normalization disclosures,
  provider receipt required, complete unresolved/price findings. Consolidation follows
  the whole census. Reverification rebuilds v2 arithmetic and refuses rehashed drift.
- `generate/normalized_input.py`: actual recipe bridge accepts verified v2 provider
  identities without inventing canonical keys; retains disclosures through binding.
- `intake/security_resolution.py`: namespace/account/revision cache, canonical
  reference evidence kept separate, one unresolved batch, whole-response validation
  before set difference. Exact miss and gated security both advertise CHECK_THEN_SWAP;
  service/malformed/route failures remain UNAVAILABLE. Suggestions require FOUND.
- `intake/resolution_kimi.py`: fixed kimi-k3/temperature1, minimized symbols-only
  prompt, bounded typed output, required pre-call durable telemetry, token telemetry,
  transient-only one retry, terminal timeout/BADJSON/EMPTY/LENGTH_STARVED outcomes.
  Swap refuses KIMI_WEB_SEARCH_UNVERIFIED absent a pinned provider-QA capability.
- `session/operation_lease.py` + broker factory: one durable provider-account key,
  CAS fences, renewal/assert/release, two-second reservation spacing, in-flight deadline
  quarantine, no unfenced fallback. Actual broker plus ReplayTransport tests exercise it.
- `session/controller.py`: pure durable transition/outbox contract, failed-pull status
  AND body classification, one refresh, verified new session, exact command binding,
  owned-host-only stop, once-only continuation. No control-plane interpreter installed.
- `.tools/irpt-ticker-check.py`: default labelled synthetic 50-symbol matrix, separate
  exact five-symbol CRO replay, explicit authorized api/scoped endpoint mode. No login.

## Measured checks

At the final source pin: intake164 PASS +18subtests; generation236 PASS +32subtests;
new session35 PASS. Total435 tests +50subtests. Existing session regression separately
reports rotation/eviction/controls/network-guard positive control all true. Its first
attempt stopped before assertions on missing packaged FirmDestinationPolicy; rerun
used exact policy bytes from CLOUD b475b96309c0034b513f19393138984d05716d0e.
These are Y executions, not a CTO independent verdict.

Set the existing handoff dependency environments from DUAL_OWNER_HANDOFF_20260923.md.
Additionally extract the three CRO JSON files at d7d044ba7a under a local directory
and set `IRPT_LOOKUP_FIXTURE_ROOT` to that directory. Then run, in separate processes:

```powershell
python -m pytest infra/aws/lambda/investor-reporting/intake/tests -q
python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests -q
python -m pytest infra/aws/lambda/investor-reporting/ycharts/session/tests/test_operation_lease.py infra/aws/lambda/investor-reporting/ycharts/session/tests/test_controller.py -q
python .tools/irpt-ticker-check.py
python .tools/irpt-ticker-check.py --capture-root .runtime/lookup-d7d044
```

The capture replay returns3 FOUND/2 exact NOT_FOUND for its five requested IDs.
The default 50-symbol run is synthetic; it proves no live database coverage.

## P shared schema/storage/runtime requirements

These interfaces are ready for paired review; no P-owned file was edited by Y.

1. Admit v1/v2 as explicit closed discriminator arms. The actual v2 object and hashes
   are in the evidence JSON. `source.lane=TEMPLATE_UPLOAD`, `file_type=csv|xlsx`,
   `upload_id`, `content_sha256`; original artifact family proposed ORIGINAL_HOLDINGS
   with appropriate MIME. Keep legacy CSV_UPLOAD/ORIGINAL_CSV and v1 replay unchanged.
   v2 holdings are YCHARTS_SECURITY/decimal-dollar text, supported by retained exact
   provider receipts. Do not relabel these as canonical source keys.
2. Mutually exclusive `file_base64`+`file_type` and legacy `csv_base64` request arms.
   `freeze_template_portfolio` returns either NEEDS_CORRECTION with complete findings
   or NORMALIZED with frozen input. Current UploadService still implements only v1;
   public schema, original-family storage and retained-input readers must be paired
   before enabling the new path. Binding disclosure propagation is not PDF publication.
3. Strong read(key)->dict|None and linearizable compare_and_swap(key,expected_version,
   replacement)->bool. None means create-if-absent. Exact operation row keys:
   version,fence,holder,session_fence,expires_at,next_allowed_at,observed_at,in_flight_until.
   Version/fence are positive integers; session fence nonnegative; times epoch seconds.
   Normalize any SDK Decimal representation at the installed boundary. Do not TTL/delete
   released rows: that would erase monotonic fencing and spacing. No local-lock fallback.
4. Key is PROVIDER_OPERATION#sha256(`ycharts` + NUL + enrolled numeric account ID as text).
   It excludes generation so refresh cannot evade serialization. All report workers,
   check/typeahead/candidate validation and refresh controllers share this account row.
   The existing capture publication lease remains distinct.
5. `SessionBroker.operation_transport(raw_transport, lease, holder, ttl, invoke, clock,
   wait, request_budget)` requires an enrolled user ID and matching published session.
   `invoke(existing_transport, four_request_args, hard_deadline)` MUST enforce a total
   wall-clock limit. The old urllib720s inactivity timeout is insufficient. Late result
   rejection alone cannot prevent overlap with a still-running old call. P must name
   the actual deadline-enforcing runtime boundary and demonstrate it before installation.
   Mutations whose outcome is unknown still require reconciliation.
6. D2 controller interpreter must persist a CAS transition and outbox effect before
   side effects, deduplicate effect_id, renew/assert account fencing, enforce overall
   deadline and produce measured events. Reuse existing runner/SSM/library. Host events
   include host_id/workflow_id/lifecycle_token/started_by_workflow and current ownership;
   existing/operator workloads are never stopped. Failed owned work may emit fenced
   cleanup; lost ownership records cleanup_required without executing a stop.
7. Install resolver routes in the actual current api/scoped Entry with verified current
   viewer and concrete data firm, retained async state/idempotency/queue/fencing/expiry,
   bounded polling, and no browser-supplied actor authority. Supply actual current route
   assembly/package manifest; historical NO-HANDLER observations are not live facts.
8. Install exact-role read for existing astn/kimi/api-key and existing configured Kimi
   endpoint through ordinary concrete plan review. No key value enters Y artifacts.
   Advisory send(payload,timeout_seconds) is server-installed; telemetry sink must durably
   accept BEFORE_CALL before any send. One provider lease must be released before Kimi
   wait and reacquired/session-revalidated before candidate checks.

## Canonical source dependency

M1fd1c8f0fb establishes no installed identity/dated-price facade currently satisfies
the required source/currency/share-class/date evidence. Classifier guesses cannot prove
identity, incompatible ticker-first/CUSIP-first keys cannot be joined blindly, and carried
or interpolated prices are not exact dated USD evidence. Current Shares returns complete
SHARES_PRICE_UNAVAILABLE rows. M/P must pin actual payload/immutable provenance and adapter
before enabling it. The local v2 pure price arm presently expects exact source-qualified
canonical_key, USD, same date, decimal price, price_basis=EXACT_DATED_SHARE_CLASS and
provenance.sha256; this spelling is a proposed consumer contract pending M/P pairing.

## K3 QA candidate, not executed

The exact offline-created call is
`KimiAdvisory(send=installed_send, telemetry=durable_sink).call("check", "ALPPL")`.
It emits model kimi-k3, temperature1, max_tokens16000, timeout120s, and the symbols-only
check prompt defined by prompt_for. One transient retry maximum; hard total budget includes
both attempts. For swap, use symbol BREIT, model kimi-k3, max_tokens32000, timeout240s.
The exact tools/tool_choice fields must come from the configured endpoint's verified QA
contract, not a guessed API feature. Without that receipt the call refuses before egress.

P must name installed_send/configured endpoint and exact tools payload for CTO review.
Expected QA evidence: redacted request configuration, actual model, provider tool/search
trace, retrieved source URLs/content provenance, token/reasoning usage, duration, response
schema, timeout/unsupported-tool behavior. Model-generated URLs alone do not prove search.
Subsequent displayed candidates must pass the canonical broker's deterministic FOUND check.
This document grants no key read, model probe or YCharts call.

## Remaining Y implementation and honest limits

Y still owes UploadService/Entry v2 composition, durable resolution worker/request adapter,
approval-bound new revisions and rejection-round lineage, UI findings/check/swap/exclusion,
per-row vendor rejection/status propagation, and runtime W1 invocation through the new
broker/controller. Screen/PDF publication must refuse missing disclosures. Existing broker
`eviction_verdict` has a historical status-only fallback; the new conservative classifier
is not yet wired into that path. Do not install the new feature via that fallback or claim
self-heal completion. A passing legacy regression does not close that semantic gap.

Next paired dependency is P's closed v2/storage/runtime mapping, not a new user permission
question. Y continues its owned work; missing installed source evidence remains visible.
No v2 request is admitted by the existing v1 service until that pairing is complete.

Push state LOCAL for this source branch. Origin CLOUD measured b475b96309c0034b513f19393138984d05716d0e.
MSTR99720/CTO184248 release the prior push hold for MSTR-coordinated publication; Y does not push.
Compiler note: comp-find found estate_report_runner after comp-which's90s fallback timeout.
Commit reflex's broker.py warning cited unrelated org/mcp/broker.py LD-0125 (read); no MCP
broker was edited. One E731 test-style gate failure was corrected before safe-commit passed.
