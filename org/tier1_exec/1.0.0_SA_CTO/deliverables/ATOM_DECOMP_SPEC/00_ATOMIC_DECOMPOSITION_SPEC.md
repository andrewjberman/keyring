# Atomic Decomposition Specification

**Version:** 1.0.0, 2026-08-06
**Owner:** 1.0.0_SA_CTO~A
**Purpose:** generalize the system-understanding and migration-planning method used for ADVI_PERFORMANCE.

## 1. Product definition

Atomic Decomposition is a two-layer operating system for high-risk refactors:

1. An adaptive skill converts an ambiguous request into a bounded investigation charter.
2. A heavy workflow builds a closed, evidence-backed model from code through live serving state and turns it into atomic migration and cleanup packages.

The skill is intentionally flexible at intake and strict at proof. Different systems require different collectors, but every claim, edge, gate, and work package follows the same contracts.

## 2. Why it exists

Complex systems do not have one truth surface. Documentation describes intent; source describes one implementation; graph databases expose parsed relationships; cloud configuration describes deployment; logs describe observed execution; artifacts describe produced data; consumers reveal what is actually served. These can all disagree.

A conventional code review misses deployed orphans, native cloud triggers, dynamic references, runtime failures, stale maps, hidden consumers, and incomplete cleanup. Atomic Decomposition forces reconciliation across those surfaces before a migration decision.

## 3. Meaning of atomic

Atomic does not mean small. A work package is atomic when it:

- has one bounded objective and owner;
- declares every dependency, read, write, resource, and contract;
- can be assigned, committed, tested, accepted, and rolled back independently;
- names the old capability it replaces;
- has no hidden cutover or cleanup obligation.

## 4. Architecture

### Layer A - adaptive assessment

The skill classifies the request as code, data, cloud, schedule, consumer-contract, migration, and/or decommission work. It pins scope, authority, mutation mode, denominators, invariants, access, freshness, and open questions. Full is the default for standardization and migration.

Output: a decomposition charter and required phase set.

### Layer B - heavy workflow

The workflow runs P0-P12 from repository census through verified absence. It maintains a dependency frontier and normalized ledgers. Narratives and diagrams are generated views; they do not replace evidence.

Output: current state, target state, migration waves, cleanup plan, validation matrix, and residual-risk statement.

## 5. Non-negotiable laws

1. Declared, deployed, invoked, completed, artifact-producing, and serving are separate states.
2. Static graph silence is not absence.
3. Trigger counts are not trigger identity parity.
4. An immediate target map is not a recursive control graph.
5. A successful dispatch is not target, artifact, or consumer success.
6. Consumer contracts remain fixed unless explicitly migrated.
7. Tool errors reduce coverage; they do not produce clear verdicts.
8. No deletion precedes replacement, parity, cutover, drain, rollback, and negative proof.

## 6. Closure model

The workflow is complete only when:

- every discovered node is in scope, a named boundary, external, or an owned unknown;
- every material claim has reproducible evidence and limitations;
- decision-relevant contradictions are resolved;
- required gates G0-G7 pass or have explicit approved waivers;
- no blocking unknown remains;
- cleanup has verified the absence of replaced paths across code, cloud, runtime, data, and consumers.

## 7. Package map

- skill/atomic-decomposition/SKILL.md: adaptive operating instructions.
- skill/atomic-decomposition/references/workflow.md: P0-P12 execution.
- references/evidence-model.md: proof and ledger semantics.
- references/tool-adapters.md: repository, Kuzu, cloud, data, and log collection.
- references/output-contracts.md: deliverables, gates, and work-package contract.
- templates/: ready-to-fill charter and core ledgers.
- 01_ADVI_CASE_STUDY.md: derivation from the ADVI_PERFORMANCE investigation.
- 02_ADOPTION_AND_EVALUATION.md: how to operationalize and test the method.

## 8. Intended use

Use this package before broad refactors, pipeline standardization, cloud migration, system consolidation, scheduler repair, ownership transfer, or decommissioning. It can also be run in read-only mode for an audit. It should not be used to inflate narrow, fully local edits into an infrastructure investigation when omitted surfaces provably cannot affect the requested result.
