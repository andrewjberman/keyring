# CVO Verdict — Kuzu↔Nessie staleness mechanics (Andrew-direct, 2026-06-11 ~2315Z)

**archetype:** DIAGNOSE
**Ask (Andrew, verbatim gist):** after a re-derive, Kuzu "should've been accurate" but still showed cached Nessie information; Kuzu is the faster-moving layer, so why isn't freshness flowing the right way? Check the mechanics.

**Verdict: the staleness is real, reproduced, and structural — but it is NOT a flow-direction problem. It is (1) a delete-propagation hole in the Item-2b incremental updater, (2) re-derives landing in a side-channel that never touches Nessie, and (3) three separate one-shot Kuzu DBs with no freshness contract, where the comp-kuzu DEFAULT is the stalest of the three.**

## The actual architecture (as built)

```
WRITERS (only two paths write Nessie):
  Item-2a nightly Fargate derive_runner.py  -> FULL overwrite() of graph_nodes+graph_edges  (clean slate, 02:00Z)
  Item-2b incremental Lambda                -> predicate-scoped overwrite (upsert) per CloudTrail batch
SIDE-CHANNEL (never touches Nessie):
  snapshot tarballs s3://opal-313476888478-globgrph/snapshots/ + latest.txt
  (nightly archive_snapshot + any ad-hoc derive publish, e.g. my 20260611T2130Z-cvo-postpagfix)

READERS (three one-shot local builds, three different upstreams):
  kuzu_db         <- kuzu_load.py        <- snapshot TARBALL          ** comp-kuzu DEFAULT (kuzu_cli.py:20) **
  kuzu_nessie_db  <- kuzu_nessie_load.py <- Iceberg warehouse (Nessie main, newest metadata.json)
  kuzu_stitch_db  <- kuzu_stitch_load.py <- stitch_graph.json (fresh derive + portal/pipeline union)
```

## Empirical state right now (queried live, 2026-06-11 ~23:10Z)

| DB | nodes | built (Z) | source vintage | trade-recon phantoms |
|---|---|---|---|---|
| `kuzu_db` (comp-kuzu DEFAULT) | 1,029 | 21:24Z | nightly tarball graph-20260611 (02:02Z, PRE-teardown) | **13** |
| `kuzu_nessie_db` | 24,831 | 20:01Z | Nessie main (pre-fix phantom-inflated + 2b upserts) | **16** |
| `kuzu_stitch_db` | 3,088 | 21:53Z | fresh post-pagination-fix derive | 1 — and it is HONEST (below) |

The stitch DB's single hit is `trade-recon-api` (API_GW `77005oklok`, drift_class LIVE-no-DECLARED) — confirmed genuinely live via `aws apigatewayv2 get-api` (created 2026-01-08, still exists). That is real AWS teardown residue, not a graph phantom.

## Why "we re-derived but Kuzu still had cached Nessie info" — four legs

1. **A re-derive never reaches Nessie.** Only 2a/2b commit to Nessie. An ad-hoc full derive publishes a snapshot tarball (side-channel). So every Nessie-sourced surface keeps serving pre-derive state until the next 02:00Z nightly full-overwrite. The re-derive being "right" is invisible to Nessie.
2. **Kuzu DBs are one-shot builds, not subscriptions.** Nothing rebuilds them on re-derive. Yesterday the fresh derive reached `kuzu_stitch_db` only because the stitch + load were manually re-run; `kuzu_db` (the comp-kuzu default everyone queries) was last built 6 min BEFORE the fresh snapshot published — it still serves the pre-teardown nightly.
3. **The incremental updater structurally cannot delete — and for S3 it actively resurrects.** `lambda_function.py`: for most classes a deleted resource's describe throws → `bounded_derive_node` returns None → nothing written → the stale row persists until the nightly (`BOUNDED_DERIVE_FAIL` path, :230-232). For S3 it is worse: the bucket branch (:160-174) fabricates the node from the ARN **without any live call** — so a `DeleteBucket` CloudTrail event RE-INSERTS the deleted bucket as a fresh `LIVE-INCREMENTAL` row. Between nightlies, Nessie main can only OVER-state the live estate. This is the exact mechanism behind the trade-recon stale-graph phantoms ("incremental-updater never propagated the deletes").
4. **`kuzu_nessie_load.py` without `--force` merges and never deletes** (:90-99 + MERGE semantics), so a locally-built `kuzu_nessie_db` keeps phantoms even after Nessie itself is cleaned; and its newest-`snapshot_ts`-wins dedup (:113-126) means a 2b-re-asserted phantom row displaces the nightly's correct row.

## On the "should filter down from Kuzu" intuition

The design intent is Nessie→Kuzu, deliberately: Nessie/Iceberg is the versioned, diffable store-of-record (the "versions" half of GLOBGRPH's charter); Kuzu is a disposable local query cache with **no independent ingest** — nothing ever lands in Kuzu first, so there is nothing to filter down from it. Kuzu is "faster-moving" only in rebuild cost. The freshness failure Andrew observed is not the direction of that arrow — it is that (a) deletes never enter Nessie between nightlies, (b) re-derives bypass Nessie entirely, and (c) three query surfaces answer the same question with three vintages and no provenance banner. Tonight's 02:00Z nightly full-overwrite self-heals the Nessie phantoms; the AM AC3 diff-oracle pass reads the N→N+1.

## Recommendations (advisory; drivers decide)

- **For AE (0.7.0_AE_CloudOps~B, Item-2b owner) — P1:** teach the updater deletes. CloudTrail `eventName` is in the batch payload: on `Delete*/Remove*` events, instead of bounded-derive-upsert, remove the matching keys in the SAME Nessie commit (the existing `overwrite(pa_table, overwrite_filter=...)` already supports replace-with-nothing for those keys). Separately fix the S3 short-circuit so a DeleteBucket does not resurrect the bucket node.
- **For CTO — P1:** one freshness contract for the query surface. Minimum: `comp-kuzu` prints a provenance header (which DB, built-when, from-what-source) on every query and warns past an age threshold; better: collapse the three DBs to one canonical rebuild chain (Nessie post-nightly + post-2b → single DB) so "the graph" has one answer.
- **For CTO/AE — P2:** let an ad-hoc full derive optionally COMMIT to Nessie (the `derive_runner.commit_to_iceberg` path is importable) — then a re-derive IS a Nessie version, and "re-derive ⇒ downstream fresh" becomes true by construction rather than by manual fan-out.
- **For AE — P2 (loader hygiene):** `kuzu_nessie_load.py` should default to `--force` (or refuse if the DB exists) — merge-without-delete makes a non-force rebuild structurally unable to drop phantoms.
- **For AE/COO — P2 (live residue, not graph):** `trade-recon-api` (API GW `77005oklok`, created 2026-01-08) is genuinely live and LIVE-no-DECLARED — confirm it was an intentional CDNCOHT-teardown survivor or fold into the teardown follow-up.

## Unknown-unknown surfaced

The same one-shot-build staleness class applies to `kuzu_ac7.db`/`kuzu_ac7/` and any future per-cert scratch DBs: every locally-materialized graph is a frozen vintage the moment it is built. Any consumer that treats "I queried Kuzu" as "I queried the estate" inherits whichever vintage happens to sit at that path — the provenance-header recommendation is what closes the class, not the per-incident phantom cleanups.

— 3.0.0_SA_CVO
