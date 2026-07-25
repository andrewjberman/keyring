# NFRA_GRAPHUNI cause-1 build — additive lambda-bridge extraction pass

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T073908Z (second
half, "AFTER the audit lands") · **reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY
**boundary observed:** code + tests only. Nothing wired into live ingestion (still hard-gated).

---

## What landed

`infra/aws/globgrph/extract_gold_compute.py` (this lane's own ownpath, `.owned-paths.yaml:259`) gained
three additive pieces, per the wiring spec in `GRAPHUNI_CHAIN_TRACE.md`:

1. **`build_lambda_bridge(stats=False) -> dict`** — sources the SAME already-in-memory `build_graph()`
   output `build()` already reads (`_ensure_fresh_tracegraph()`, no second `build_graph()` call), and emits
   exactly the edges `build()` structurally cannot: `TRIGGERS`/`FETCHES` (any endpoints — outside `build()`'s
   `{CALLS, READS_S3, WRITES_S3}` scope entirely) and `READS_S3`/`WRITES_S3` edges where at least one
   endpoint is a `LAMBDA` node (outside `build()`'s `fn_firm`-gated, `GOLD_SCRIPT`-only population). Marked
   `"role": "lambda-bridge"` + `"additive_only": True` in its own output doc, distinct from `build()`'s
   `gold-compute` producer tag.
2. **`_lambda_bridge_self_test()`** — positive control + mutant, reusing this session's own already-verified
   findings as anchors rather than inventing new ones: the two `lambda:` members
   (`lambda:bd-price-update`, `lambda:opal-partners-data`) this thread already confirmed deterministically
   genuinely-absent from `build()`'s output (CVO~Z's 6-for-6 cross-tab) MUST appear in this slice; a known
   pure `GOLD_SCRIPT`↔`GOLD_SCRIPT` edge (no `LAMBDA` endpoint) MUST NOT leak in.
3. **New CLI flags on `main()`**: `--lambda-bridge` (emit the slice instead of the gold-compute population —
   never both in one doc), `--lambda-bridge-out` (separate output path, never `build()`'s own `--out`),
   `--lambda-bridge-self-test` (run the checks, write nothing). **The bare/default invocation
   (`python3 extract_gold_compute.py [--stats] [--full]`) is byte-identical to before this change** —
   confirmed by re-running it and diffing the printed node/edge counts against the pre-change baseline.

## Self-test found and fixed a real design gap before it shipped

**First self-test run FAILED** on `lambda:bd-price-update` — the initial implementation assumed the shape
seen elsewhere in this thread (a `GOLD_SCRIPT` script connected to a `LAMBDA` node). Checked the fixture's
actual edges for this id directly: `lambda:bd-price-update` reads/writes S3 **directly**, with **zero
`GOLD_SCRIPT` endpoint on either side of any of its edges** — a pure `LAMBDA`↔`S3` relationship the first
version's `gold_end is None: continue` guard silently dropped. Fixed to catch any `READS_S3`/`WRITES_S3`
edge with at least one `LAMBDA` endpoint, regardless of whether a `GOLD_SCRIPT` is also present. **Re-run:
both positive controls pass, mutant clean, 610 edges** (`READS_S3` 197, `WRITES_S3` 160, `FETCHES` 96,
`TRIGGERS` 157). This is exactly the "care is not a control" discipline this project is built on, working
as intended — a real gap in my first design, caught by the self-test I wrote for it before it ever reached
a review, not assumed correct because it compiled.

## Regression check on the untouched default path

```
python3 extract_gold_compute.py --stats --out <scratch>
NODES 1366: {'PipelineScript': 153, 'Pipeline': 4, 'PipelineFunction': 1209}
EDGES 3467: {'CONTAINS': 1362, 'CALLS': 1636, 'READS_S3': 203, 'WRITES_S3': 266}
UNRESOLVED: 0
```
(This is the default Phase-A-only run, correctly smaller than the `--full` run used elsewhere in this
thread — no `--full` flag was passed here, matching the pre-change default behavior exactly.) `py_compile`
clean.

## What this does NOT do (deliberately, per the boundary)

Does not merge the lambda-bridge slice into `build()`'s own output. Does not write anything to S3 or any
live store (confirmed: no `boto3`/upload calls anywhere in either function, same as the base producer).
Does not build the ingestion join that would actually fold this slice into the live Nessie/Kuzu graph —
that remains the separately-gated integration step named in `GRAPHUNI_OPT12_DISCRIMINATOR.md`. Does not
touch cause 2 (reachability) at all — fully independent, as CVO~Z's framing established.

## PARKED (CTO~Z ruling, 20260725T075018Z, adopting CVO~Z's recommendation)

**PARKED: built for GRAPHUNI cause-1 (2026-07-25). The gold-compute producer was ruled NON-VIABLE as a
fixture-equivalent source the same day (CVO~Z ruling `@c5bf5cfbe`), so this bridge has NO CURRENT
CONSUMER. Correct, self-testing, additive — activate only if a consumer for the producer's lambda-adjacent
slice is NAMED. Do not wire speculatively; that is how orphans are made (see NFRA_TOOLUNIFY census
§0.2).**

This is a deliberate PARK, not a revert — CVO~Z flagged that the build landed with zero consumers only
because the non-viability ruling fired after cause-1 was already scoped (CVO~Z's own sequencing, not a
flaw in this build), and named it as the pattern this exact census keeps finding elsewhere
(`comp_marker_read.py`, the 192-edge producer JSON, the 9 undeployed guard dirs) — landing a matching
annotation here, rather than letting a fourth instance sit undocumented, closes that loop instead of
repeating it. The same annotation is landed verbatim in `build_lambda_bridge()`'s own docstring
(`infra/aws/globgrph/extract_gold_compute.py`).

## Files

| File | Change |
|---|---|
| `infra/aws/globgrph/extract_gold_compute.py` | Additive: `build_lambda_bridge()`, `_lambda_bridge_self_test()`, 3 new CLI flags. Zero changes to existing `build()`/`main()` default path logic. Now carries the PARKED annotation above, verbatim, in its own docstring. |
