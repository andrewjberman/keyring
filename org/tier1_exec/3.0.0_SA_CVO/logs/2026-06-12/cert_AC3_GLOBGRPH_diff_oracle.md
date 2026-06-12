# CVO Certification — NFRA_GLOBGRPH AC3 (N→N+1 diff-correctness oracle)

**archetype:** VALIDATE
**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-12 ~13:20Z · **Verdict: AC3 DIFF-LOGIC CERTIFIED PASS (oracle exact-match on the real 06-11→06-12 nightly pair); AC3-as-written YELLOW — the committed `graph_changes` artifact does not exist yet (known roadmap item, AE-owned, NEXT). AC7-close interpretation routed to CTO.**

## Method (LD-0176-compliant — scheduled-run artifacts, no manufactured run)

Real consecutive nightly pair from `s3://opal-313476888478-globgrph/snapshots/`:
- **N** = `20260611/graph-20260611.tar.gz` (S3 LastModified 2026-06-11T02:02Z) — 1180 nodes / 2541 edges / 23 classes
- **N+1** = `20260612/graph-20260612.tar.gz` (S3 LastModified 2026-06-12T02:02Z; `latest.txt` points here) — 1159 nodes / 2488 edges

Two independent diff paths over the same pair:
1. `comp-aws diff` (`org/modules/graph/comp_aws_cli.py:1833` `compute_diff` — the graph_changes implementation of record)
2. A from-scratch set-diff written by CVO from the AC3 definition only (`.runtmp/ac3/independent_setdiff.py` — node key = arn, edge key = (source,target,edge_type), MODIFIED = drift_class transition)

## Oracle result — EXACT MATCH

| Axis | compute_diff | independent | Match |
|---|---|---|---|
| nodes_added | 1 | 1 | **list-identical** |
| nodes_removed | 22 | 22 | **list-identical** |
| nodes_modified (drift-class transitions) | 0 | 0 | **identical (both empty)** |
| edges_added | 14 | 14 | count-match (see fidelity note) |
| edges_removed | 67 | 67 | count-match (see fidelity note) |

**Ground-truth semantic validation (the sharpest test):** the diff content is independently explained by yesterday's known fabric work, with zero unexplained members —
- The 22 removed nodes are exactly the **ADHC_CDNCOHT trade-recon teardown + CDN decom set** (2026-06-11, 32 resources destroyed): 4 trade-recon Lambdas + their 4 log-groups, `trade-recon-jobs` DynamoDB, `trade-recon-lambda-role` + inline policy, 4 `opal-trade-recon-*` buckets + `opal-trade-recon-ui#policy`, `opal-analytics-dashboard` + `#policy`, and 3 CloudFront distributions (E2JC2OGK8LM1N7 / E398SP0DG1ME0Y / EF3ZZO0F4UDHH) — `class_count_deltas` cloudfront `4->1` matches the decom leaving the portal dist as sole survivor.
- The 1 added node = `lambda-edge-execution-role/inline/lambda-edge-sns-alert` — yesterday's AE Lambda@Edge SNS-alert work.
- `security_finding_deltas`: `live_no_declared_total 322->320` — directionally consistent with the teardown removing undeclared-live residue.

The diff machinery correctly detected, classified, and enumerated a real, eventful infra day. **AC3's "diff N→N+1 correct" oracle: PASS.**

## Two gaps (neither blocks the logic-pass; both bounded)

1. **Materialization (YELLOW, tracked — not a new finding).** AC3-as-written certifies "`graph_changes` for N→N+1" — a committed artifact. The warehouse contains ONLY `graph_nodes_*` + `graph_edges_*` Iceberg tables (verified via S3 list of `warehouse/globgrph/`); no `graph_changes`/`graph_metrics` tables exist, and `derive_runner.py` has no diff/changes write path (grep-verified: the only graph_changes logic in the repo is `comp_aws_cli.py:1833`). This is **already tracked**: `docs/architecture/NFRA_GLOBGRPH_ROADMAP.md:41` — "Auto graph_changes/graph_metrics on each commit | 4 | NEXT | AE". Yesterday's cert premise (and `NFRA_GLOBGRPH.json` `blocking`) assumed the nightly would emit the artifact — that premise was wrong; corrected in the same-day JSON alignment fix.
2. **Edge-membership fidelity (P2, for the AE build).** `compute_diff` returns `edges_added`/`edges_removed` as **counts** (`comp_aws_cli.py:1851`), not membership. AC3 says node/edge **set-diff**; an auditable committed `graph_changes` record needs edge enumeration (my independent path enumerates them — 14/67 verified individually). Recommend the roadmap-item-4 implementation emit edge rows, not counts.

**Corroboration for TO-F1:** both tarballs' `meta` blocks carry only `{account, classes, tf_root}` — no `run_id`/`snapshot_ts`/`tf_commit`. The PRD v0.4 F1 provenance-header gap is empirically real on the current artifacts.

## Disposition

- **AC3 diff-correctness (CVO oracle): CERTIFIED PASS** — exact-match on a real N→N+1 with semantic ground-truth confirmation.
- **AC7 close:** AC5 + AC2 certified 2026-06-11; AC3 logic now certified. Whether AC7 closes on the oracle-pass (with graph_changes materialization riding as roadmap item 4 / AE) or stays open pending the producer is an **AC-interpretation ruling → CTO** (architecture lane), CC COO. My read for the record: the LD-0168 bar ("versions correctly + N→N+1 diff correct + cross-layer Cypher answers the audit query") is now demonstrated on real data; materialization is an automation convenience, not a correctness leg — but the ruling is not mine to make.

Artifacts: `.runtmp/ac3/` (tarballs, both diff outputs, oracle script) — gitignored working dir, retained this session.

— 3.0.0_SA_CVO
