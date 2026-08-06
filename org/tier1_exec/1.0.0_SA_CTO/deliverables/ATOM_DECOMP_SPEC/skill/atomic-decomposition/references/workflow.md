# Heavy Workflow

## Closure algorithm

Maintain a frontier of discovered code, artifacts, resources, controls, and consumers. For each item, record stable identity, evidence, incoming edges, outgoing edges, and classification. Add every new endpoint to the frontier. Closure exists only when each endpoint is in scope, an explicit boundary, external, or an unresolved item with owner and next probe.

## Phases

### P0 - Identity and scope

Pin objective, decision, authority, mutation mode, repositories, accounts, regions, environments, tenants, time window, invariants, exclusions, and denominator. Record the current consumer contract before proposing change.

### P1 - Repository census

Enumerate entry points, dispatchers, configurations, manifests, infrastructure code, ownership files, tests, documentation, and relevant history. Bind documented names to stable paths and commits. Do not assume naming means deployment.

### P2 - Script I/O and line dependencies

For every in-scope symbol record file, line span, callers, callees, reads, writes, fields, grain, filters, join keys, aggregation, incremental state, failure behavior, and side effects. Parse structured formats and ASTs where practical; use literal search to catch dynamic dispatch and string-built keys.

### P3 - Artifact lineage

For each artifact enumerate all writers and consumers, storage URI, format, schema, partitions, identity keys, freshness, retention, and field provenance. Distinguish raw source, normalized data, analytic output, publication copy, and serving object.

### P4 - Deployed resource census

Enumerate live functions, rules, schedules, queues, notifications, jobs, hosts, containers, roles, buckets, databases, log groups, and monitors. Bind each to source path, digest/version, environment, role, last modification, and evidence timestamp. Repository silence cannot prove a resource is unused.

### P5 - Recursive control graph

Trace EventBridge rules and Scheduler schedules, S3 notifications, queue subscriptions, direct function calls, Step Functions, SSM, EC2/container launchers, CI jobs, and manual paths. Follow targets recursively. Capture enabled state, payload, retries, dead-letter behavior, role, and timezone.

### P6 - Runtime and cadence

Prove configured, invoked, completed, artifact-producing, and serving states independently. Reconcile schedule expressions with logs, metrics, object timestamps, and consumer reads. Explain missed, duplicate, or manual runs. Measure a bounded window and state it.

### P7 - Consumer contracts

Identify every downstream surface and pin path pattern, format, schema/version, required fields, grain, identity, ordering, null behavior, freshness, and compatibility policy. Preserve the contract unless its migration is explicitly in scope.

### P8 - Reconciliation

Compare documentation, code, graph, deployed state, runtime, artifacts, and consumers. Register contradictions rather than averaging them away. Prefer direct measured evidence, then deployed configuration, source, and documentation, while accounting for freshness and denominator.

### P9 - Target architecture

Define one owner per responsibility, canonical source-to-serving flow, contracts between layers, control plane, observability, replay/idempotency, security, and failure recovery. State what remains firm-specific and what becomes shared.

### P10 - Atomic migration waves

Each package declares objective, dependencies, reads, writes, acceptance proof, rollback, owner, and replaced capability. Sequence characterization, implementation, shadow output, field and identity parity, bounded cutover, observation, and expansion.

### P11 - Cleanup and decommission

Maintain a replacement ledger from every old resource/function to its successor or approved retirement. Disable before delete where possible, observe a drain window, search all trigger and consumer surfaces, remove configuration and documentation, then prove absence. Retain rollback until its window closes.

### P12 - Validation and closure

Execute all gate tests against evidence. Close only with no blocking unknown, no unresolved contradiction affecting the decision, no unclassified frontier item, and explicit acceptance of residual risk.

## Re-entry

Any contradiction, new resource, unexpected output, or consumer mismatch reopens the earliest affected phase. Update ledgers first, then regenerate narrative views.
