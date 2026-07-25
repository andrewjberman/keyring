# NFRA_GRAPHUNI OPT1-BUILD — fresh `--full` producer run + member-level set-compare vs. the P0-CVO fixture

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T064248Z + supplement
20260725T064432Z · **ruling basis:** `3.0.0_SA_CVO~Z` Andrew-delegated Option 1 ruling, `@a6fbf13ee9`
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY · **hard boundary observed:** measurement only —
no ingestion wiring, no S3/live writes (confirmed via source read before running: `extract_gold_compute.py`
has zero `boto3`/S3 calls; it produces a local JSON only, "the COMMIT is the single coordinated derive run"
per its own docstring).

---

## VERDICT: **SET-IDENTITY REFUTED — 11/28 (39%) comp-blast targets match.**

Same rate, same root cause as this session's earlier live marker-head re-assert (`REASSERT_20260725_REPORT.md`,
also 11/28). This is not new information about WHETHER the gap exists — it independently confirms it exists
in the freshly-generated, fully-flagged producer output itself, not only in the (differently-sourced) live
graph. Stated per the supplement's explicit bar: **member-level set-equality, per target, not aggregate
counts** — full per-target detail in the sidecar.

## Step 1 — fresh `--full` run, vintage stamped

```
python3 infra/aws/globgrph/extract_gold_compute.py --full --stats \
  --out deliverables/NFRA_GRAPHUNI_REASSERT/gold_compute_producer_FULL_20260725.json
```
Run at **2026-07-25T06:43:52Z** (stamped by this lane at emit time — the tool's own `generated_at` field is
`None` by design, "no Date.now in-tool," per `extract_gold_compute.py`'s own comment; the docstring says
stamping happens externally "at emit time," so I stamped it here rather than repeat the null-vintage cost
CTO~Z flagged). Output: **1366 nodes / 3609 edges** — `CALLS=1636, CONTAINS=1362, READS_S3=345, WRITES_S3=266`.
`coverage.unresolved = []`, `coverage.phase_b_deferred_count = 0` (both zero because `--full` bypasses the
phase_a defer gate entirely — see Step 2). Wrote to **this lane's own path**, not overwriting
`org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` (the historical Phase-A record,
untouched).

**Note on the total:** 345, not the 306 CVO~Z's fixture-derived count expected. This is not a discrepancy to
resolve — it reflects genuine estate growth between the fixture's 2026-06-30 vintage and today (consistent
with every other growth signal found this session — REACT_QUERY_KEY, SQS_QUEUE, etc. all grew similarly).
The fixture's 306 is a fixed point-in-time requirement; today's live producer legitimately emits more. The
question this step answers is not "does the count match" but "does the SET the fixture actually needs
appear inside today's larger set" — answered in Step 3.

## Step 2 — the 2 `S3KEY_FIRM_UNRESOLVED` keys: already resolved, by a prior commit

Both were `gold/timeseries/client_performance.parquet`, reader-firm `mdpf`, in the month-old artifact.
**Confirmed via `git log -S "_READ_OVERRIDE"`: this was already fixed**, commit `62063ee602` (this same
lane), which added a source-grounded cross-firm-read override
(`extract_gold_compute.py:148`, `_READ_OVERRIDE = {("mdpf", "gold/timeseries/client_performance.parquet"):
"inf"}`, grounded at the time against `build_mdpf_inflection_history_from_spine.py`'s actual
`s3://opal-data-INF/...` read) — that commit's own message states it was verified to close both cases
("Phase-B (--full) now emits ... 0 UNRESOLVED (was 2)") but was explicitly **staged, not emitted to S3**,
pending "the coordinated ~B-fired Phase-B derive." This fresh run reconfirms it: both `mdpf`-firm readers
of `client_performance.parquet` now resolve, verbatim in the output, to `opal-data-inf/gold/timeseries/
client_performance.parquet` (`pipeline:mdpf:gold:build_mdpf_wsc_inflection_feeder` and
`pipeline:mdpf:gold:build_mdpf_inflection_history_from_spine`, both present, both correctly firm-qualified).
**No new grounding work was needed this step — the fix already existed and this run verifies it still
holds.**

## Step 3 — canonicalize polarity + namespace, member-level set-compare

Reconstructed a real `TraceGraph` object from the fresh producer JSON (script:
`deliverables/NFRA_GRAPHUNI_REASSERT/opt1_setcompare.py`), inverting the producer's own transforms:
- **Node ids:** `pipeline:<firm>:gold:<body>` → `gold:<body>` (exact inverse of
  `extract_gold_compute.py:47-51`'s `_pipeline_id()`).
- **S3 ids:** `opal-data-<firm>/<key>` → `s3:<key>` (strips the bucket-qualification
  `extract_gold_compute.py:140`'s `s3key_id()` adds — the fixture is natively bucketless, so this
  reconstruction needed no firm-aware expansion step the way the live-kuzu re-assert did).
- **`READS_S3` polarity flip** (the specific detail CTO~Z named): the producer emits
  `{source: script, target: s3key}` (script→s3); `build_graph`'s own convention, which the fixture is
  captured against, is `{source: s3key, target: script}` (s3→script, `extract_s3.py:453-455`). Flipped on
  reconstruction. `CALLS` and `WRITES_S3` needed no flip (both already match the fixture's polarity).
- `CONTAINS` edges (1362 of them) are dropped — not a `TraceGraph`/fixture edge type, GRAPHDEPTH-only.

Then drove the **real** `cli.main()` blast code in-process (monkeypatched `_get_graph`, argv simulated,
stdout captured) against the same deterministic sample — identical method to the marker-head re-assert,
different graph *source* only.

**Result: 11/28 comp-blast targets MATCH (39%). SET-IDENTITY REFUTED**, not proven. The sharp case
(`gold:D_01.partner_analytics`, script-level, expected 216) gets **5** in this reconstruction (13 in the
live-marker-head version) — still a large, real gap. The function-level case
(`generate_header_metrics`, expected 39) still **matches exactly, 39/39** — the third independent
confirmation this session that function-grain is clean and script-grain is where the gap lives.

## Residual methodology note (disclosed, not smoothed over)

This reconstruction's script-level mismatches include a secondary pattern the live-marker-head re-assert did
not show as sharply: several of `gold:D_01.partner_analytics`'s own FUNCTION children
(`:generate_header_metrics`, `:main`, `:_get_periods_annual/monthly/quarterly`) appear as `extra_in_new` on
the SCRIPT-level query. Root cause, grounded: `TraceGraph.find_node()` (`trace_graph.py:271-275`) is a
**substring match** on node id — querying `gold:D_01.partner_analytics` legitimately matches every function
under it too (`gold:D_01.partner_analytics:main` contains the query string), and `cmd_blast` unions the
radius across all matches. This is the SAME real code, unmodified, in both the fixture's original capture
and this reconstruction — so it is not a defect I introduced, but I have **not fully traced** why the union
surfaces differently between the two graphs (plausibly: whichever direct-edge structure differs between the
original TraceGraph and this reconstruction changes what a function's OWN radius contributes to the union).
**Not asserted as understood; flagged as a residual, not rounded to a conclusion.** It does not change the
headline verdict (REFUTED) — even excluding these 5 self-referential entries from `extra_in_new`, `old_n=216`
vs `new_n=5` on the sharp case is decisively a real gap, matching the same root cause (missing cross-script
`READS_S3`-mediated reachability) already identified and now triple-confirmed (live marker-head, this
reconstruction, and the function/script split both times).

## Denominator + honesty

28/28 comp-blast targets attempted (the full deterministic sample for this tool), none skipped or sampled
down. **comp-trace and comp-xref were NOT re-derived from this reconstruction** — they would need the same
graph-building step but were not re-run this pass (the dispatch's `--full` + set-compare ask centered on the
producer's own CALLS/READS_S3/WRITES_S3 output, which comp-blast consumes directly; comp-trace/xref
consume the same edges through different traversal logic and would reuse this same reconstructed graph
object if wanted — named as a scope boundary, not silently dropped). **comp-platinum** remains out of scope
per this session's earlier finding (does not consume `TraceGraph` at all).

## What this lane did NOT do

Did not wire the fresh artifact or the reconstructed graph into the live Nessie/Kuzu ingestion path — hard
boundary observed per the dispatch. Did not overwrite the historical Phase-A `P1-D.gold_compute_producer.json`.
Did not modify `extract_gold_compute.py`, `cli.py`, or `trace_graph.py`. Did not re-run comp-trace/comp-xref
against the reconstruction. Did not fully root-cause the `find_node` substring-match residual noted above.

## Files

| File | Role |
|---|---|
| `deliverables/NFRA_GRAPHUNI_REASSERT/gold_compute_producer_FULL_20260725.json` | Step 1 output, this lane's own path |
| `deliverables/NFRA_GRAPHUNI_REASSERT/opt1_setcompare.py` | Step 3 reconstruction + set-compare script |
| `deliverables/NFRA_GRAPHUNI_REASSERT/OPT1_SETCOMPARE_20260725_result.json` | full 28-target per-target result (sidecar for this memo) |
