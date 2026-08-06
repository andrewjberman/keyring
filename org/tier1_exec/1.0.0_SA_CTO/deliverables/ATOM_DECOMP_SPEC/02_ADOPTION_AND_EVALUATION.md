# Adoption and Evaluation

## 1. Adoption stages

1. Use the packaged skill manually on one read-only system audit.
2. Require the charter and ledgers on one active migration.
3. Add lightweight CI checks for ledger headers, stable IDs, linked evidence, and gate status.
4. Add provider adapters only after repeated manual evidence shows a stable collection contract.
5. Promote the skill into a workflow orchestrator when at least three unlike systems complete with the same phase/gate model.

Do not automate live mutation. Collection may be automated; cutover and deletion remain explicitly authorized actions.

## 2. Workflow engine interface

The future engine should accept a charter and emit immutable raw evidence, normalized ledgers, run state, and reports. Each collector returns:

- collector name/version and execution identity;
- target scope and denominator;
- command/query with secret-safe redaction;
- timestamps, status, truncation, and raw-output URI;
- normalized nodes, edges, observations, and limitations.

The orchestrator maintains the frontier, queues unresolved endpoints, invalidates downstream reports when evidence changes, and enforces G0-G7. Provider adapters cannot mark absence or advance gates directly.

## 3. Evaluation suite

Forward-test on at least these scenarios:

1. A local service refactor with no cloud resources.
2. A data pipeline with dynamic object keys and multiple consumers.
3. A cloud system where the repository and deployment disagree.
4. A scheduler audit with native storage notifications and direct invokes.
5. A decommission request containing a quiet but still configured predecessor.
6. A migration with a fixed frontend contract and vendor-specific source gaps.

Score denominator closure, edge recall, contradiction detection, claim reproducibility, consumer-contract preservation, work-package atomicity, rollback quality, cleanup completeness, and false absence assertions.

## 4. Acceptance targets

- No test may infer absence from one source.
- All discovered endpoints must be classified.
- All volatile evidence must have timestamps and scope.
- A hidden runtime edge must reopen the relevant phase.
- Count-equal but identity-different trigger sets must fail parity.
- A dispatch without artifact/consumer proof must not pass G5.
- A deletion package without a replacement or approved retirement must fail G6.
- Another agent must reproduce material claims from the cited locators.

## 5. Ownership and versioning

Version the skill, evidence schema, and collector adapters independently. A schema change requires migration guidance for open runs. Store completed runs with the code commit, deployed-state timestamp, graph head, and evidence manifest that supported the decision.

The initial package is a specification and portable skill, not a standing scheduled process. It arms no timers and performs no autonomous cloud changes.
