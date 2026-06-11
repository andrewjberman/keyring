# 0.7.0_AE_CloudOps~B — Session Log 2026-06-11 ~18:30Z (Andrew Nessie/Fargate investigation -> Item-2b fix -> P2-STITCH step-1)

Andrew brought ~B online (reallocated from base-AE) to investigate the Nessie/Fargate
graph ecosystem + comp-aws synergy, then directed the work that followed.

## 1. Investigation (the ask) — answered exhaustively
- NFRA_GLOBGRPH = Nessie/Fargate/Iceberg/Kuzu platform; NFRA_COMPAWS = comp-aws producer.
- Versioning: Iceberg graph_nodes/graph_edges in a Nessie catalog (git-semantics: atomic
  catalog-wide commits + audit-baseline-{date} tags + branches) + gzip snapshot tarballs.
- Query: comp-kuzu (Cypher, NOT comp-aws) over a local Kuzu DB loaded by kuzu_nessie_load.py;
  pyiceberg time-travel; comp-aws CLI for derive/metrics/diff.
- Update trigger: NOT git hooks. CloudTrail mgmt events -> EventBridge -> SQS(120s debounce)
  -> Lambda bounded derive -> 1 Nessie commit (Item-2b), + nightly Fargate full derive
  cron(0 2 * * ? *). Deliberately CloudTrail (PRD D2) to catch out-of-band drift. Verified
  .tools/git-hooks has 0 graph refs.
- Live state confirmed: Nessie Fargate 1/1, nightly snapshots 06-08..06-11, incremental
  Lambda Active, DLQ down to 10 from the 298k 409-storm.

## 2. Item-2b phantom-node fix (Andrew-directed) — SHIPPED globgrph-v0.1.9
- Live comp-kuzu demo caught it: graph 24,831 nodes vs ~1,167 real; 23,664 phantom
  LIVE-INCREMENTAL S3_BUCKET nodes = S3 OBJECT KEYS mis-typed as buckets (real buckets = 26).
- Root cause: bounded_derive_node s3 branch name=arn.split(':::')[-1] -> bucket/key per object.
- AC4 (untyped==0) blindspot: phantoms validly TYPED S3_BUCKET -> recommended a grain/identity
  cert-sentinel (S3_BUCKET id !~ '/'; node-count magnitude band) -> filed to CTO; = NFRA_GRAPHS D5.
- Fix: collapse object-ARN->bucket grain + handler dedup. Commit b723f3ea1, ds-gate clean,
  zip->S3, safe-apply HALTGT 0add/1change/0destroy, hash yM0hkuAIEABC, 0-diff verified, tag
  globgrph-v0.1.9. Backlog self-clears next 02:00 nightly. Brief: e906f46da. Filed CTO+COO.

## 3. P2-STITCH-core (Andrew reallocated full scope to ~B; intra-lane with Nessie/Fargate)
- AC5 edge-bar PRE-CLEARED: 342 skipped = 341 wildcard-exempt + 1 (EventBridge->ECS-cluster)
  = CTO's WAVE-4 ECS_CLUSTER fix, KNOWN-TRANSIENT (resolves on next WAVE-4-inclusive nightly
  reload; NO manual derive per cost discipline). 0 dedup-canonicalization violations.
- STEP-1 DONE + committed 9070e3248 + RAVC2-ACCEPTED (COO 185229Z):
  infra/aws/globgrph/extract_portal_stitch.py reuses comp-graph substrate (trace_graph.build_graph
  + cache_cli) -> normalized to FROZEN schema 53816378a -> comp_aws_cli graph-dict shape.
  1751 nodes (PORTAL_BUNDLE/PORTAL_COMPONENT 27/REACT_QUERY_KEY 32/API_ROUTE 166/S3_DATA_KEY 273/
  GOLD_SCRIPT 1252); 615 intra-layer edges (READS/WRITES/FETCHES/QUERIES); 0-dangling; selftest pass.

## RESUME POINT (next focused session) — P2-STITCH step-2: stitch-edge derive
- Join portal->AWS at the boundary: S3_DATA_KEY -[STORED_IN]-> S3_BUCKET(ARN) +
  API_ROUTE -[ROUTES_TO]-> LAMBDA(ARN). The path/name<->ARN identity bridge (PRD sec4.2).
- Reuse CTO's build_firm_gold_dag/FIRM_BUCKET for the firm side (CTO GO).
- Will catalog the 303-vs-173 LAMBDA code-vs-live drift gap (stitch value preview).
- Then step-3 kuzu load of unioned graph, step-4 AC5 traversal (CVO done-gate).
- Dual-tag RAVC2s NFRA_GRAPHS-D4 (unified query) + D5 (grain sentinel / AC5<->0-dangling).
- Nothing time-gated; AC5 verifies on tonight's nightly; morning artifact-review picks up the thread.

Trade-recon teardown: CLOSED (destroy executed under COO 1801Z APPLY-CLEAR; base-AE adc74fff6
removed the .tf blocks; COO 0-diff verified; ADHC_CDNCOHT complete). Nothing on ~B's plate.
