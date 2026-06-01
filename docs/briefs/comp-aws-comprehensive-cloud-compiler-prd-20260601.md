# PRD — comp-aws: comprehensive AWS cloud compiler + certified resource graph

**Author:** 1.0.0_SA_CTO · **Trigger:** Andrew-direct 2026-06-01 ("a batch script that checks all tf modules, lambdas, ec2s, dynamodb, s3 buckets, everything … hand audit the entire aws cloud and test compilers against it until we have literally everything categorized, typed, perfect … all relationships, all structures") · **Mechanism:** AE CloudOps · **Ground-truth + certify:** CVO (+ AE/Andrew) · **Decompose + project-register:** COO.
**Status:** DRAFT. Generalizes the proven `comp-lambdamap` pattern (Phase-1 check built today, **~0.33s static run**, caught a TF-vs-disk bug the manual audit missed) to the ENTIRE AWS surface. Candidate ADHC_* project (COO/Andrew to assign the code — this is multi-phase + fabric-significant).

## 1. Goal
A single batch compiler that derives a **typed, certified graph of the entire AWS cloud** — every resource categorized + typed, every relationship captured — reconciled across IaC (Terraform), live AWS, and on-disk source, and **validated against a human hand-audit until 0-diff** ("everything categorized, typed, perfect"). It becomes the maintained source of truth for cloud structure + relationships, replacing hand-maintained artifacts (the lambda source-map drift class writ large).

## 2. Node taxonomy (resource classes — "everything")
- **Compute:** Lambda (`comp-lambdamap`), EC2 + instance profiles, Step Functions, (ECS/Fargate if any).
- **Data/Storage:** S3 buckets (+ bucket policies — incl the unmanaged-by-TF class we hit on opal-data-portal-v2), DynamoDB tables, (RDS if any).
- **Eventing/Messaging:** EventBridge rules + schedules, SNS topics, SQS queues, S3 event-notifications.
- **Edge/Network:** CloudFront distributions (+ OAC/OAI, behaviors, Lambda@Edge), API Gateway, VPC/subnets/SGs, Route53.
- **Identity/Secrets:** IAM roles + policies (`comp-iam`), Secrets Manager, KMS keys.
- **Observability:** CloudWatch log groups, alarms, metric filters.
Every node carries: id, type, owning-TF-module, deployed-state, source provenance (sha/commit), owner-pipeline.

## 3. Edge taxonomy (typed relationships — "all relationships")
- **compute→identity:** lambda/EC2 → IAM role → policies (the grant set; `comp-iam` already does the grant side).
- **compute→data:** lambda/EC2 → S3 (read/write, derived from IAM ∩ env-var ∩ code), → DynamoDB, → Secrets, → KMS.
- **trigger:** EventBridge / S3-event / Step Functions / API-GW / schedule → lambda.
- **edge:** CloudFront → S3 origin (+ OAC condition), CloudFront behavior → Lambda@Edge / origin.
- **IaC:** TF module → resources; **declared(TF) ↔ live(AWS)** (the drift edge); TF resource → artifact (S3 zip / image).
- **pipeline DAG:** S3 bronze→silver→gold, lambda chains, Step-Function flows (feeds/extends the existing comp-graph pipeline layer that comp-trace/comp-blast already traverse).

## 4. Triple ground-truth + reconcile
1. **IaC (TF parse)** — declared state (reuse `comp-iam`/`comp-lambdamap` TF-parse; extend to all resource types). Cheap/static (~sub-second/class per the comp-lambdamap wall-clock).
2. **Live AWS (`aws` describe/list)** — actual deployed state. **The cost driver** (network + API rate limits) — must be SNAPSHOT + cached + batched + parallelized, NOT called every run. A periodic live-snapshot the static compile diffs against.
3. **On-disk source** — sha/provenance.
Reconcile → drift classes: DECLARED≠LIVE (drift) · DECLARED-no-LIVE (never-deployed) · **LIVE-no-DECLARED (unmanaged/manual/orphan — the high-value class; e.g. the unmanaged portal-v2 bucket policy)** · NO-TF-LINKAGE · NO-PROVENANCE · UNCATEGORIZED (the cert gap).

## 5. The hand-audit certification loop (Andrew's method)
This is the acceptance oracle, mirroring the fabric's honesty-not-perfection / certification pattern:
- **Phase 0 — HAND AUDIT:** humans (CVO + AE, Andrew sign-off) enumerate the entire cloud by hand — every resource + every relationship — into a ground-truth fixture. This is the oracle, not the deliverable.
- **Phases 1..N — per-class compilers:** `comp-lambdamap` (done), `comp-iam` (exists), then `comp-s3`, `comp-ec2`, `comp-dynamodb`, `comp-eventbridge`, `comp-cloudfront`, `comp-secrets-kms`, … each `derive`-from-truth + emit typed nodes/edges into the comp-graph.
- **CERTIFY:** diff each class's compiler output vs the hand-audit → fix the compiler until **0-diff** (every resource categorized + typed, every relationship captured). On 0-diff, the **compiler becomes the maintained source of truth** for that class; the hand-audit becomes its regression fixture. "Perfect" = every class compiler-certified 0-diff + 0 uncategorized/untyped nodes + 0 untyped edges.
- `comp-aws` orchestrates the per-class compilers + emits the unified typed graph + reports the certification frontier (what % categorized/typed/certified).

## 6. Integration — it POPULATES the existing comp-graph
The comp-graph substrate (`org/modules/graph/`, consumed by comp-trace / comp-blast / comp-iam) already models pipeline/portal layers. comp-aws is the **AWS-resource-layer populator**: it adds the full typed resource+relationship layer so comp-trace/comp-blast/comp-iam answer cloud-structure questions categorically (blast-radius of an S3 bucket, every consumer of a DynamoDB table, every unmanaged resource). This is the AWS-infra instance of the compiler typed-edge thesis.

## 6a. Cloud-shape snapshot archive (Andrew-direct addendum)
**Every comp-aws graph compile PERSISTS the printed graph representation** to a dedicated archive folder — building a time-series of cloud "shapes" in an agent-readable format for backup, diff-over-time, and forensics.
- **WHAT:** the canonical compiled graph (typed nodes + edges) — the full shape of the cloud at run-time.
- **FORMAT:** agent-readable canonical **JSON** as the inner payload (so a future agent untars and reads/diffs the graph directly — not an opaque blob), archived as a **gzipped tarball** (`.tar.gz`) per Andrew.
- **WHERE:** a dedicated archive folder (e.g. `org/modules/graph/aws-shapes/`), timestamped filenames (`aws-shape_<YYYY-MM-DDTHHMMZ>_<tf-commit>.tar.gz`) so a shape is attributable to its ground-truth (TF-commit + live-snapshot time = reproducible).
- **WHEN:** every full graph compile (`derive`); check-only/no-op runs need not snapshot.
- **VALUE:** shape-diff over time (what changed in the cloud between two dates), restorable cloud inventory, drift-over-time forensics, agent-readable history — the cloud's structural black-box recorder.
- **SUB-DECISIONS for TO-decomp:** (a) retention — keep-all (gzipped JSON is tiny) vs dedup/skip-if-identical-to-last vs age-out tail; (b) durability — local dedicated folder for fast agent access + **S3-archive** for durable history (matches the existing artifact-store pattern, doesn't bloat the worktree) vs git-committed; lean = local-recent-N + S3-archive-all; (c) a `latest` pointer + a lightweight index/manifest (timestamp series + per-shape node/edge counts) so agents locate + diff shapes WITHOUT untarring every archive.

## 7. Scalability (from the comp-lambdamap wall-clock)
- Static IaC compile: ~0.33s/169-lambdas → whole-cloud static likely single-digit seconds → CI-gate-able every push.
- Live reconcile: snapshot-and-cache (periodic, e.g. nightly or on-demand) + batched/parallel describe calls + rate-limit aware; the CI static check diffs against the cached snapshot, not live AWS.

## 8. Ownership + phasing
- **ws CTO:** this design + the node/edge type schema (the relationship taxonomy is the load-bearing design).
- **AE CloudOps:** mechanism — per-class compilers + live-AWS reconcile + comp-graph population + CI.
- **CVO:** Phase-0 hand-audit (ground-truth) + per-class certification verify (0-diff oracle).
- **COO:** TO-decompose + register as the ADHC_* project; sequence the per-class compilers (lambda done → S3/IAM next given recent incidents → EC2/Dynamo/eventing → edge/network → observability).
- Phase order favors the classes with recent pain first: S3 (bucket-policy/unmanaged), IAM (grants), Lambda (done), then breadth.

## 9. Acceptance criteria
- AC1: node taxonomy covers every AWS resource class in use (reconciles to the Phase-0 hand-audit; 0 uncategorized).
- AC2: edge taxonomy captures every relationship class in §3; 0 untyped edges between captured nodes.
- AC3: triple-reconcile (TF/live/source) with the §4 drift classes; LIVE-no-DECLARED (unmanaged) surfaced categorically.
- AC4: each per-class compiler certified 0-diff vs the hand-audit (the "perfect" bar), then becomes source-of-truth + the audit becomes its regression fixture.
- AC5: `comp-aws` batch-run emits the unified typed graph into comp-graph; static run CI-gate-able (sub-10s); live reconcile snapshot-cached.
- AC6: comp-lambdamap + comp-iam absorbed/orchestrated as the first certified sub-compilers (no duplication).
- AC7 (snapshot archive): every `comp-aws derive` run writes a timestamped, TF-commit-stamped **gzipped tarball of the canonical JSON graph** to the dedicated cloud-shapes archive (+ a `latest` pointer + an index of the timestamp series with node/edge counts), so agents can locate + diff cloud shapes over time without untarring all. Durability via S3-archive + local-recent-N (TO-decomp settles retention).

## 10. Notes
- Validated premise: comp-lambdamap (one class) already caught a real TF-vs-disk bug the manual audit missed — the derive-from-truth + certify-vs-hand-audit method demonstrably finds what hand-maintenance can't. comp-aws scales that to the whole cloud.
- This is large + multi-phase → warrants a formal ADHC_* project + a phased TO roadmap (COO). The hand-audit (Phase 0) is the long pole + the highest-value artifact (it's the oracle + the durable cloud-inventory).
