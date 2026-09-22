# IRPT: distance to an end-to-end MVP and a three-agent completion proposal

Author: `1.0.0_SA_CTO`, 2026-09-22. Product assessment requested directly by Andrew; not a canonical round analysis, L9 grade, PRD admission, or implementation order. Post-slug progression remains held at `bc87e045b5`.

## Recommendation

Use three senior Codex implementation agents with responsibility across frontend and backend, one for each product function, supported by a small shared contract and an integrated acceptance gate. Give them permission to finish the connection they discover inside IRPT, with explicit shared-file ownership, rather than requiring a new worker round for each missing adapter.

There is enough architecture and reusable code to begin substantive implementation without another discovery cycle. There is not evidence that the MVP is nearly operational. The reviewed evidence establishes **zero of the three requested product journeys end to end**. This is a proof count, not a claim that zero useful code exists or that every possible runtime path was exercised.

The remaining work includes new connecting behavior and economic correctness, beyond deployment or UI polish. Three capable agents can plausibly close it; three simultaneous independent rewrites would recreate the current boundary failures. The largest uncertainty is source completeness and live provider behavior, particularly Cottonwood performance, complete custody/security membership, and recoverable YCharts execution. Reasoning effort cannot eliminate those measurements.

## Evidence checked for this assessment

- Opened the supplied package index. It now contains **five** briefs: Sensitivity, Performance, Model Overlay, Storage, and Reporting Backend/LGIC.
- Read all five briefs. Verified **270 manifest entries** against their copied SHA-256 hashes; zero mismatches. Checked **308 local HTML link targets**; none missing. Repeated copies are included in these counts.
- Compared every manifest entry categorized `References` whose original exists locally with its current original: zero changed copies. This is not a claim about missing originals, all background files, current cloud deployments, or portal hosting state.
- Workspace HEAD observed during review: `8eb2100142a6c10bb2b638390fcacf2e647c2319`; portal HEAD: `7dd3d067a17ee00b878ecfceff23c557649a2331`. Shared workspace may advance.
- Directly read current performance entry/transport, generation entry/job, export entry, and report/status dispatch; checked actual frontend request carriers and adapter calls. The major disconnections in the briefs remain present.
- Re-ran CRO's network-free synthetic probe against current model builder functions. It reproduced all three defects below. Local evidence: `.runtime/codex-seats/1.0.0_SA_CTO/mvp_assessment/holdings_math_probe.json`.
- Read current decomposition headers and backend round-18 purpose. Frontend is round 15, backend round 18. Those rounds concern bounded repairs, including the render identity chain. Completing that chain does not implement generation, provider performance, or the complete model data foundation.
- Cloud inventory, schedule state, and deployed-code statements below are attributed to CRO's dated September 22 audits in the package. I did not repeat AWS inspection, invoke vendors, or perform a signed-in browser journey during this assessment.

## Actual distance by product

| Product | Reusable foundation | Remaining minimum product work | Assessment |
|---|---|---|---|
| Model Overlay | Three source builders; canonical node/identity work; serving/projection; existing holdings components | Complete custody census and positions; correct allocation and observed-value attribution; accepted Gold/Platinum publication; real selected-account scope; model/non-model/unresolved dollar split and complete drilldown | Bounded data product, with material correctness and coverage work |
| Performance | BD/Orion parsing and normalization; recorded research; existing authentication helpers elsewhere; chart/table/layout components | Canonical-to-vendor mapping; authenticated parameterized requests for all three firms; correct HTTP request/response shapes; immutable report storage; complete frontend mapping and export | Primarily connector completion, but provider behavior needs tenant-specific acceptance |
| Sensitivity | Parser; YCharts recipe/transport/session libraries; extraction/certification; analysis and print components | CSV upload/ownership and selected-custody normalization; units and security resolution; one public request contract; durable worker/session composition; extraction/publication; status/history/correction; export | Largest chain and likely critical path |

**Model correctness is demonstrably unfinished.** The current synthetic probe doubles a $100 unassigned 49F account to $200, turns $120 of Inflection custody across two accounts into $200 at the roots, and reports Cottonwood weights of 100%/75% for a $100/$300 pair rather than 25%/75%. These are synthetic counterexamples, not measured client losses. They rule out simply enabling the existing holdings publisher.

**Performance has not yet become a real request-to-report service.** The frontend sends dates in query parameters and an account-set fingerprint in the path; the entry reads different date fields and interprets the path value as an account ID. BD and Orion adapter calls pass `None` as their request bodies. LiveTransport lacks provider authentication. Report output is wrapped differently from the browser's expected payload. Existing financial parsing should be retained; a new return engine is unnecessary.

**Sensitivity lacks its assembled execution path.** Six of the composer's seven keys do not intersect the generation entry's accepted field list. The worker entry still refuses even after its live-consent check because its dependencies are not assembled. Its attempt record has empty sections and `UNCERTIFIED` extraction. The sections route is wired to a status loader. Parser support for shares/weights is not proof that the dollar-only recipe supports generation with those units.

**Export remains shared unfinished work.** `export/entry.py:submit_export` raises `NOT_READY`; the real controller is not called. Render-auth repairs are necessary, but an offline render identity PASS alone cannot establish report-to-bundle-to-PDF completion.

## The shared work that must have an owner

Four contracts should be fixed once, in a compact implementation agreement using the existing schemas and libraries:

1. **Selection and identity:** firm, relationship, selected account set, entitlement revision, source revision, server-owned vendor crosswalks; separate prospect ownership without invented client accounts. The selected set is not the entire permitted universe.
2. **Data and publication:** accepted source revisions; complete custody baseline; model membership at supported grain; actual values and reconciliation; immutable Gold and bounded Platinum projections; atomic release pointer and honest freshness.
3. **Report lifecycle:** input/reference, request/revision, durable job/attempt, raw vendor evidence, normalized report, current entitlement checks, history/status and reload recovery. The durable record must precede dispatch; an identical request hash is not by itself durable idempotency.
4. **Export:** immutable source report -> frozen bundle -> scoped renderer -> validated PDF -> stored receipt -> authorized download. Performance export must not fetch a new period or recalculate the displayed result.

The first executable acceptance should cross the actual browser client and actual API entry, rather than another pair of independently designed fixtures. Shared interfaces should ship with a producer-to-consumer example and a negative control.

## Proposed three-agent split

These are proposed responsibilities, not issued task orders or registered seats.

| Agent | Primary outcome and owned shared work | Boundaries and first proof |
|---|---|---|
| 1 — Data foundation and Model Overlay | Complete firm census/positions, three model joins, LGIC placement/naming integration, publication, common directory/selection/grants, holdings API and model UI | Owns the selection and accepted-snapshot interfaces. First prove one selected investor reconciles from custody through API to all UI roots; then all three firms and the synthetic counterexamples |
| 2 — Performance and report/export platform | BD/Orion request/auth integration, immutable shared report repository/history, reporting store IaC, performance API/UI, shared export submit/controller/render/receipt/download assembly | Owns common report persistence and export interfaces. Agent 1 supplies naming policy; agent 3 supplies analysis payloads. First prove one real 49F report survives reload and produces an identical frozen PDF; then independent COT/INF and subset proofs |
| 3 — Sensitivity | Both input lanes, normalized portfolio and unit conversion, comparison/profile composition, durable YCharts worker/session execution, PDF extraction/certification, analysis status/history/correction and UI | Consumes Agent 1's accepted positions and Agent 2's report/export interfaces. First prove a dollar CSV Overview from actual browser submission through certified report and exported PDF; then account lane, remaining units and variants |

Use separate branches/worktrees from a pinned accepted baseline, with one integration owner and regular integration of working paths. Shared files such as routes, schemas, frontend client/adapters, auth, naming registries, and Terraform roots must have one named merge owner. Agents can propose coordinated edits to them without concurrently owning incompatible contracts. Product-specific portions can be developed in parallel.

The CTO should own the compact agreement, integration decisions, and assembled acceptance. CVO review should test the complete journeys and high-consequence boundaries, while implementation agents fix ordinary in-scope failures directly. Do not introduce a fresh planning/recut round for every connector discovered inside an agreed outcome. Any change to the existing operating process is a proposal for Andrew; this assessment does not enact it.

Keep current round findings and proven repairs. When both slugs arrive, pin them as inherited evidence under the existing hold, then reconcile the proposed implementation baseline without repeating or discarding those repairs. R18-e remains the prerequisite to render key provisioning/deployment unless Andrew changes that gate explicitly.

## MVP acceptance and sequencing

The full requested MVP remains all three functions across all three firms, both sensitivity input lanes, the three advertised sensitivity variants, supported amount units, and branded exports for performance and sensitivity. Dollar CSV/Overview and one-firm performance are early integration milestones, not a silent reduction of that endpoint.

Advance through four integrated milestones:

1. **Shared boundary works:** actual selection is preserved through the real HTTP event; owned input/report identities resolve correctly; contracts and destination policy agree.
2. **First complete journeys:** one reconciled model snapshot; one live provider performance report; one dollar CSV Overview through durable execution. Persistence and reopening work from the outset.
3. **Complete requested matrix:** three firms; selected account/relationship/subset; actual model/non-model/unresolved cases and drilldowns; both sensitivity lanes, shares/weights and three variants; truthful dates/coverage and correct display units.
4. **Integrated release proof:** screen/report/PDF revision equality; page reload; worker interruption/redelivery; uncertain vendor mutation reconciliation; expired provider session; missing mapping/history; corrections; revoked entitlement; cross-firm denial. Each result carries one trace linking input, source/provider request, retained response, displayed report and final artifact.

Optional narrative, Graph/email intake, historical model UI, estate-wide upstream migrations, and expanded product features should stay outside the initial closure unless required by an existing accepted endpoint. Existing source adapters remain usable under declared legacy paths while the bounded IRPT cutover is completed.

## Storage decision and remaining uncertainty

The backend-design brief is compatible with the intended separation: firm-complete model Gold/Platinum in canonical firm buckets; private report records in a proposed product artifact store; DynamoDB authoritative for workflow state. LGIC supplies the general patterns. It does not yet provide the proposed `opal-data-irpt` placement as an already registered destination for private firm records. The current builder routes firm state to firm buckets; the brief itself calls out the missing reporting placement policy/registry support.

Adopt that bounded IRPT placement treatment as part of the implementation agreement if proceeding with the proposed store. This is a specific architectural decision and code/registry change, not a reason to redesign LGIC or halt unrelated connector work. Do not make mass migration/deletion of the research bucket a prerequisite to the first completed journey. New writes and readers must cut over together, with retained old evidence and explicit mapping where needed.

I would not promise a percentage or calendar deadline from task counts. There is clear reusable implementation, and seven coherent work packages (four shared, three product-specific), but no timing measurement of the remaining critical path. The first complete live journeys will expose the remaining vendor/data uncertainty far more effectively than further isolated fixture rounds. This is a substantive completion sprint, not a final configuration pass.

## Source anchors

- Desktop package: `C:/Users/AndrewBerman/Desktop/Investor Reporting Briefs - 2026-09-22/INDEX.html`, five adjacent `Brief.md` files and per-folder manifests/audits.
- `infra/aws/lambda/investor-reporting/performance/entry.py:52`, `:72`; `transport.py:108`; `bd_adapter.py:260`, `:285`; `orion_adapter.py:118`; `handler.py:85`.
- `portal/src/api/endpoints/investor-reporting.ts:995`, `:1012`, `:1052`; `portal/src/pages/InvestorReporting/tabs/analysis/composer.ts:102`.
- `infra/aws/lambda/investor-reporting/ycharts/generate/entry.py:67`, `:101`; `job.py:491`, `:586`; `ops/entry.py:102`; `export/entry.py:188`.
- `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`; CRO's `holdings_math_probe_20260922.py`, copied and rerun in the CTO runtime evidence directory above.
- `infra/logic/02_DOCTRINE.md`; package Backend/LGIC brief and its builder evidence.

No new development/deployment agents, vendor calls, cloud writes, PRD edits, or canonical progression were initiated for this assessment.
