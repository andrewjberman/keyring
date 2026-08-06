# Evidence Model

## Claim contract

Every material statement must carry:

| Field | Meaning |
|---|---|
| claim_id | Stable identifier |
| question | Exact question being answered |
| answer | Fact, inference, decision, or proposal |
| status | PROVEN, PARTIAL, CONTRADICTED, UNKNOWN, NOT_APPLICABLE |
| confidence | Bounded assessment, never a substitute for status |
| evidence_class | SOURCE, DECLARED, DEPLOYED, RUNTIME, DATA, CONSUMER, DECISION, ABSENCE |
| source_uri and locator | Reproducible source plus line, query, ARN, key, log event, or commit |
| measured_at | UTC collection time |
| scope and denominator | What was tested and the full population claimed |
| limitations | Access, freshness, parser, graph, sampling, or retention limits |
| owner and expiry | Person responsible and revalidation date where volatile |

Keep observations separate from inference. Link contradicting claims bidirectionally and retain the resolution.

## Node levels

- Code: repository, file, symbol, line span, configuration key.
- Data: source, artifact, table/object, field, grain, partition, identity key.
- Resource: function, rule, schedule, queue, job, host, bucket, database, role, monitor.
- Control: trigger, call, notification, subscription, retry, publication.
- Runtime: invocation, completion, artifact production, serving read.
- Consumer: application, endpoint, report, partner, human process.

Use edge types CALLS, READS, WRITES, TRIGGERS, INVOKES, STARTS, PUBLISHES, SERVES, AUTHORIZES, MONITORS, and REPLACES.

## Required ledgers

1. System inventory: stable node, type, owner, environment, path/ARN, state, boundary.
2. Script I/O: symbol and lines, direction, artifact, fields, grain, transforms, state, side effects.
3. Artifact lineage: producer, artifact, consumer, storage, schema, identity, cadence.
4. Resource inventory: service/type, ARN, source/version/digest, role, deployment evidence.
5. Control edges: source, target, mechanism, expression/pattern, payload, retry, DLQ, recursive depth.
6. Runtime observations: start, completion, outcome, counts, artifact, logs, invocation identity.
7. Consumer contracts: path, shape, grain, required fields, identity, freshness, compatibility.
8. Contradictions and unknowns: impact, blocking status, owner, next probe.
9. Migration waves: dependencies, reads, writes, proof, rollback, replacement.
10. Replacement ledger: predecessor, successor, cutover, drain, removal, absence probe.
11. Decision register and validation matrix.

## Absence standard

VERIFIED_ABSENT requires a named denominator and negative probes across repository references, deployed resources, trigger sources, runtime logs/metrics, artifact writes, and consumer reads for an appropriate drain window. A zero-result graph query, missing source file, disabled schedule, or quiet log group alone is insufficient.
