# ADVI_PERFORMANCE Case Study

## 1. Request shape

The ADVI work began as a voice-memo request to complete and standardize market-performance analytics for 49 Financial, Inflection, and Cottonwood. The fixed invariant was the existing firm-specific Group D output consumed by Portal. The desired change was to centralize Bronze through Gold A/B/C in opal-data-assets, promote compatible Gold into each firm bucket, retain Group D and publication, then remove replaced paths.

That combination made a source-only review unsafe: three firms, three primary vendors, supplementary sources, shared and firm-specific scripts, cloud triggers, live buckets, historical migrations, and a fixed serving contract.

## 2. How the investigation proceeded

1. Transcribe the voice memo and preserve it as directive evidence.
2. Pin the frontend/Group D contract as an invariant before redesign.
3. Read the named projects, prior PRDs, commits, logs, and runner code.
4. Query the fresh Kuzu head through the underlying script for dependency candidates.
5. Use literal/source analysis to fill dynamic and parser-missed edges.
6. Inventory live AWS schedules, rules, targets, S3 notifications, Lambda configuration, logs, and bucket artifacts.
7. Compare the original trigger baseline with the 2026-08-06 live delta.
8. Reconcile source/vendor fields and grains for Schwab, Orion, and Black Diamond.
9. Design canonical 49F performance truth, then synthesize equivalent requirements for Inflection and Cottonwood.
10. Separate target architecture, implementation waves, cleanup/replacement, and post-cleanup agentic indexing.

## 3. Findings that shaped the generalized method

### Consumer-first boundary

The correct refactor boundary was not the whole application. Group D shape and Portal publication were already correct. This produced the rule: pin the consumer contract first, then move the upstream responsibility without accidental output drift.

### Source systems are not semantically equal

Schwab custodian data is comparatively raw and complete. Orion and Black Diamond expose opinionated derived shapes. The design therefore required a canonical field-and-grain contract derived from 49F, plus explicit known/required/gap matrices for each other firm. Similar filenames or totals could not prove semantic parity.

### Graphs are lower bounds

Kuzu and compiler tools accelerated discovery, but dynamic keys, native cloud configuration, direct invokes, and deployed resources required direct corroboration. No-edge results were treated as coverage limits, not inactivity.

### Trigger inventory is not runtime architecture

The baseline and delta had near-equal trigger totals while identities and fields drifted. Immediate EventBridge/Scheduler targets also omitted S3 notifications and recursive Lambda/SSM/host behavior. This established two rules: identity parity is required, and control tracing must recurse past immediate targets.

### Scheduling was partly corroborated and materially corrected

The investigation corroborated one authoritative ingestion anchor followed by success-driven downstream stages. It refuted the idea that one existing daily Gold schedule per firm could serve as the recovery floor:

- 49F schedules covered Schwab ingestion or legacy/supplementary Black Diamond paths, not a canonical Schwab-native A/B/C dispatcher.
- Inflection had active native S3 fan-in despite disabled visible Gold rules, but its quorum omitted performance and billing and could advance from inadequate marker semantics.
- Cottonwood had the strongest success-marker topology, while a migrated mirror target was failing and first-fire continuity was not yet proven.

The corrected design used durable stage/run identity plus one shared reconciliation control that re-drives only the earliest incomplete idempotent stage.

### Dispatch success is not serving success

Configuration, invocation, completion, expected artifact creation, promotion, Group D execution, Platinum publication, and Portal consumption needed separate proof. This became the multi-state evidence model.

### Cleanup must be designed with migration

Centralization would otherwise leave duplicate Lambdas, rules, scripts, maps, documentation, and bucket paths. A replacement ledger was made part of each work package, with disable/drain/remove/absence gates. Cleanup is not a final search-and-delete exercise.

### Post-cleanup indexing is a separate continuation

The Platinum agentic-query index was intentionally split from the core migration. It depends on stable canonical artifacts, provenance, access policy, and manifests. This produced the rule to isolate useful extensions that rely on the target state instead of widening the critical cutover.

## 4. Durable ADVI source set

The Desktop package includes copies of:

- ADVI_PERFORMANCE_E2E_STANDARDIZATION_PLAN_20260806.md
- ADVI_PERFORMANCE_SCHEDULING_ASSESSMENT_20260806.md
- ADVI_PERFORMANCE_CLEANUP_AND_REPLACEMENT_PLAN_20260806.md
- ADVI_PLATINUM_AGENTIC_QUERY_INDEX_STRATEGY_20260806.md
- TRIGGER_GRAPH_AND_RUNTIME_MAP.md
- TRIGGER_GRAPH_AND_RUNTIME_MAP_DELTA_20260806.md

These are case-study evidence, not generic requirements. The generic laws and workflow live in the skill package.

## 5. Generalization test

The method applies beyond ADVI because it does not assume a vendor, language, cloud service, data layer, or scheduler. It standardizes questions, evidence, identities, gates, and migration obligations while allowing task-specific collectors and target designs.
