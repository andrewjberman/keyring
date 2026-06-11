# CVO Certification — NFRA_GLOBGRPH AC7 (versioning + cross-layer Cypher on the real unioned graph)

**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-11 · **Verdict: AC5 + AC2 CERTIFIED PASS; AC3 diff-oracle DEFERRED to tomorrow-AM nightly artifact (correct non-manufactured path). AC7 closes on AC3.**
**Method:** live Cypher on the local unioned stitch DB (`infra/aws/globgrph/kuzu_stitch_db`) + deploy-evidence verification for the versioning path.

## AC5 (cross-layer Cypher traversal) — **CERTIFIED PASS (independent, live)**
Queried the real unioned stitch graph directly:
- **2901 nodes / 4042 edges**, **3 layers**: pipeline 1495, aws 1180, portal 226. (The cited 2931→2901 / 4455→4042 delta = the D5 junk-node fix `bd5a6a82c` — I certify the cleaner post-fix state.)
- **0 untyped** (`node_type IS NULL OR ''` = 0) — AC4 bar holds on the unioned graph.
- **Cross-layer traversal lands:** `MATCH (c:PORTAL_COMPONENT)-[*1..6]->(b:S3_BUCKET)` → **15 distinct portal components reach an S3 bucket** (matches AE~B's cited "15 components reach a bucket"). The §7-class audit query — portal feature → its backing bucket — resolves on the unioned graph.
- **Cross-layer stitch edges confirmed:** pipeline→aws 840, aws→pipeline 145, portal→aws 48 — the stitch genuinely connects all three layers (it is not three disjoint subgraphs). portal→aws = the API_ROUTE→LAMBDA `ROUTES_TO` join; pipeline↔aws = gold-script↔bucket/IAM.

This is the binding "you can query it across layers" half of the LD-0168 AC7 bar — independently reproduced.

## AC2 (atomic versioning) — **PASS (deploy-evidence verified)**
The Nessie-atomic-commit path (Item-2b incremental_updater) is LIVE and the 409-commit-storm is fixed:
- `2ce19eaee` (tag `globgrph-v0.1.7`, 0-diff, live-sha verified): `upsert_nodes` collapsed to ONE `overwrite(...)` commit with reload-per-attempt retry/backoff; ESM `maximum_concurrency=2`; `source_code_hash` on repo zip.
- Post-fix smoke (real CloudTrail-shape S3 event): DERIVED S3_BUCKET → ICEBERG_UPSERT `nodes_written=1 failed=0` through the new single-commit path; batches clean, debounce correct, queue drained.
- The atomic-across-Iceberg-tables / no-half-written-graph-on-`main` property is structurally satisfied by the single-overwrite-commit design. Accepted on verified-deploy evidence (a fresh manufactured run is neither needed nor permitted per cost-governance doctrine).

## AC3 (diff correctness — CVO's N→N+1 oracle) — **DEFERRED to tomorrow-AM nightly artifact**
AC3 = "`graph_changes` for N→N+1 exactly matches the independently-computed node/edge set-diff (ADDED/REMOVED/MODIFIED + drift-class transitions)." This is explicitly **CVO's diff-oracle** and **structurally requires a real N→N+1** (two consecutive committed snapshots). The real exercise is tonight's **02:00Z nightly vs Item-2b** run, reviewed tomorrow AM per **LD-0176** (review scheduled-run artifacts next morning; do not manufacture a run — `feedback_no_adhoc_gold_runs` / `feedback_no_overnight_watcher_agents`).
- **My commitment:** tomorrow AM I run the AC3 diff-oracle against the nightly's `graph_changes` (N→N+1), independently recompute the set-diff, and confirm exact match → that closes AC7.

## Disposition
**AC7: AC5 (cross-layer Cypher) + AC2 (atomic versioning) CERTIFIED PASS now; AC3 (N→N+1 diff-correctness oracle) deferred to the tomorrow-AM nightly artifact review.** GLOBGRPH's "versions + you can query it across layers" bar is demonstrated; the one remaining piece is the diff-oracle that needs a real consecutive-snapshot pair, correctly scheduled to the nightly rather than a manufactured run.
