# Tool Adapters

Use the best available tools, but keep the evidence contracts tool-independent.

## Repository and history

- Start with rg --files and rg for names, paths, bucket keys, ARNs, environment variables, dispatch maps, and dynamic string fragments.
- Use language parsers or ASTs for imports, calls, symbols, and line spans. Verify dynamic dispatch with literal search.
- Inspect git log, show, blame, and relevant commits to reconstruct provenance, replacements, and abandoned migrations.
- Parse JSON, YAML, Terraform, CloudFormation, and manifests structurally.

## Graph

- Query the current Kuzu head through the underlying repository script, for example python infra/aws/globgrph/kuzu_cli.py. Do not rebuild a graph merely to answer a query when freshness is adequate.
- Use comp-blast, comp-trace, and comp-heat as accelerators when available. Their results remain advisory until corroborated.
- Do not invoke comp-pipescript unless the operator explicitly authorizes it. Direct tool/script alternatives must remain available.
- Record graph head/freshness, node and edge denominator, query, and limitations.
- A missing edge can result from dynamic code, parser coverage, stale indexing, external configuration, or a deployed orphan.

## Live cloud

Enumerate before filtering. For AWS, inspect as applicable:

- EventBridge rules and targets, Scheduler schedules, S3 notification configurations;
- Lambda configuration, versions/aliases, event-source mappings, policies, source package metadata;
- Step Functions, SQS/SNS, Glue, Batch, ECS, EC2/SSM, IAM roles and policies;
- CloudWatch logs and metrics, CloudTrail, object listings/heads, and deployment tags.

Follow every target recursively. Capture account, region, timestamp, role, retry/DLQ, payload, and enabled state. Never equate a configured rule with a successful run.

## Data

Record exact URI/key, format, schema, field types, grain, identity keys, partitions, row/object counts, min/max dates, null/duplicate behavior, and sample policy. Compare identity sets and field values, not only totals. Separate source capture, normalization, analytics, publication, and serving copies.

## Logs and runtime

Use a declared time window. Correlate trigger identity, invocation ID, completion, row counts, artifact key/version, and consumer read. Retention gaps produce PARTIAL or UNKNOWN, not inactivity proof.

## Collection discipline

Store raw tool output separately from normalized ledgers. Log command/query, execution time, target, exit status, and truncation. Redact secrets without deleting identity-bearing metadata. If access fails, record the denied probe and the permission needed.
