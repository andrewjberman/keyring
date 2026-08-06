---
name: atomic-decomposition
description: Map software, data, and cloud systems end to end before refactoring, migration, standardization, or decommissioning. Use when Codex must prove script I/O, line-level dependencies, data lineage, deployed resources, schedules and triggers, runtime behavior, consumer contracts, migration waves, cleanup obligations, or resource absence by reconciling source, graph, cloud, log, and artifact evidence.
---

# Atomic Decomposition

Convert an ambiguous system-change request into a closed evidence model and independently executable work packages.

## Rules

1. Start read-only unless mutation is explicitly authorized.
2. Pin system identity, environment, scope, denominator, and consumer boundary.
3. Keep declared, deployed, invoked, completed, artifact-producing, and serving states separate.
4. Treat static graphs as lower bounds. Search dynamic references and inspect live state.
5. Give every claim a source, locator, measurement time, scope, denominator, and limitation.
6. Treat tool failure as a coverage limitation, never absence proof.
7. Expand every discovered node until it is in scope, a named boundary, external, or an owned unknown.
8. Preserve consumer contracts unless their migration is separately approved.
9. Delete nothing before replacement, parity, cutover, drain, rollback, and absence proof.

Read [workflow.md](references/workflow.md) before starting. Use [evidence-model.md](references/evidence-model.md) for ledgers, [tool-adapters.md](references/tool-adapters.md) for collection, and [output-contracts.md](references/output-contracts.md) for gates.

## Compile the assessment

Create a charter containing:

- objective, decision to enable, authority, mutation mode, and deadline;
- repositories, accounts, regions, environments, firms/variants, and data roots;
- invariants such as fixed frontend shape or serving path;
- available live access and evidence freshness;
- known questions, exclusions, and owners.

Use the full workflow for migration, standardization, or cleanup. A focused run may omit a phase only when the omission cannot affect the conclusion and is recorded as a boundary.

## Run the frontier

Execute phases P0-P12 in [workflow.md](references/workflow.md). At each level, enumerate incoming and outgoing edges and add undiscovered nodes to the frontier:

1. repository and ownership;
2. file, symbol, call site, and line span;
3. artifact, field, grain, identity key, and partition;
4. deployed resource and source provenance;
5. schedule, event, notification, direct invocation, and retry path;
6. runtime execution, completion, produced artifact, and serving consumer.

Stop only when the frontier is empty and every exclusion has a reason. Diagrams are views over ledgers, not sources of truth.

## Record truth

Use statuses PROVEN, PARTIAL, CONTRADICTED, UNKNOWN, and NOT_APPLICABLE. Use evidence classes SOURCE, DECLARED, DEPLOYED, RUNTIME, DATA, CONSUMER, DECISION, and ABSENCE.

Resolve conflicts by evidence strength and freshness, but retain the contradiction record. Count parity is not identity parity. Invocation success is not serving proof.

## Decompose migration

An atomic work package has one objective plus explicit dependencies, reads, writes, acceptance proof, rollback, owner, and replacement obligation. It must be independently assignable, committable, testable, and reversible.

Sequence change as characterize, shadow, contract and identity parity, bounded cutover, drain observation, then predecessor removal. Keep the old serving path until cutover proof passes.

## Enforce gates

| Gate | Required proof |
|---|---|
| G0 Scope | Identity, authority, mode, denominator, boundaries, constraints |
| G1 Current state | Required inventories and closed dependency frontier |
| G2 Reconciliation | Freshness stated; contradictions resolved or blocking |
| G3 Target contract | Canonical ownership and preserved consumer contract |
| G4 Migration ready | Atomic waves, field gaps, tests, owners, rollback |
| G5 Cutover ready | Shadow parity, controls, serving-path verification |
| G6 Cleanup ready | Replacement ledger, drain complete, negative probes |
| G7 Closed | Acceptance passes, predecessors absent, residual risk accepted |

Never claim completion while a required gate is open. Report blocked gates and the exact next probe instead.
