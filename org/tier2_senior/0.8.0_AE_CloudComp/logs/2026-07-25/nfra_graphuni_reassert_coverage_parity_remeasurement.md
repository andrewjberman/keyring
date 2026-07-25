# NFRA_GRAPHUNI.P2/D2 Coverage-Parity Re-Measurement — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CVO~Z dispatch (ruling on Andrew-direct "reopen it, have CVO deal with it"), 20260725T055641Z
**Status:** COMPLETE

---

## Objective

Andrew ruled to reopen the month-old deferred NFRA_GRAPHUNI.P2/D2 re-point architectural decision, routing
it to CVO~Z. CVO~Z independently re-verified my prior claims (zero call sites, the deferral commit content,
the fixture's existence) and dispatched a fresh coverage-parity re-measurement using the existing P0-CVO
fixture's deterministic re-assert recipe — not a new approach — with a specific ask to re-derive the
`gold:D_01.partner_analytics` blast-radius case (month-old: 13 vs expected 216) and report per-target
SHA/set match counts, not just aggregate totals.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3` (custom re-assert script) | monkeypatched `cli._get_graph()` -> marker-head `TraceGraph`, drove real `cli.main()` blast/trace/xref in-process | PASS | 45/45 targets attempted, 13/45 matched; script written to this lane's own deliverables path, reads CVO's fixture dir read-only |

**What worked:** reusing the fixture's own real `cli.main()` code path (via monkeypatch + argv simulation)
instead of reimplementing blast/trace/xref answer logic — meant the comparison tests only the graph SOURCE,
not a second, independently-written (and independently-buggy) answer formatter.

**What failed:** first run hung past a 120s timeout with zero output — `load_marker_head_graph()` +
45 in-process CLI calls is slow; needed `python3 -u` (unbuffered) + a 300s timeout to see it complete
cleanly (RC=0). Not a defect, just wall-clock.

**Gap found:** none new in the tooling; the coverage gap found is in the estate (see Findings), not the
measurement method.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

### 1. Read the fixture's own re-assert recipe (`FIXTURE_ATTESTATION.md` §7) before building anything

Confirmed the deterministic sample file is `sample.deterministic.json` (not `sample.json` as the original
`repro_2_capture_layer_a.py` expects — a minor naming drift, worked around by reading the actual filename).
Confirmed the firm-aware S3 canonicalization precondition (§7) and located both required maps
(`NFRA_GRAPHUNI.P1-D.bucketless_to_qualified.json`, `NFRA_GRAPHUNI.P1.d_s3key_firm_qualified.json`) already
on disk, exactly as cited in the attestation.

### 2. Wrote the re-pointed capture script

`deliverables/NFRA_GRAPHUNI_REASSERT/repro_2_capture_layer_a_REPOINTED.py` — monkeypatches
`org.modules.graph.cli._get_graph` to return `comp_marker_read.load_marker_head_graph().as_tracegraph()`,
then calls the real `cli.main()` in-process (argv simulated, stdout captured) for every blast/trace/xref
target in the deterministic sample, applies firm-aware S3 canonicalization before comparing, and diffs
against the frozen `fixture_layer_a.tool_answers.json`. First placed the script inside CVO~B's fixture
directory by mistake — that lane is owned (would have hit the same `ANY_EXEC` class of lock as
`grain_baseline.json` earlier this session); relocated to my own deliverables path before running anything,
reading the CVO fixture directory read-only throughout.

**comp-platinum explicitly excluded**: confirmed via source read that `platinum_cli.py` does not consume
`TraceGraph`/`.comp-graph/graph.json` at all — a separate `graph_cache.py`-backed routing/DAG/dataflow
projection — so a clean graph-source swap does not apply to it. Named as a scope boundary, not silently
dropped from the totals.

### 3. Ran it, got a decisive result

13/45 (29%) matched overall (blast 11/28, trace 2/8, xref 0/9). The specifically-requested sharp case
(`gold:D_01.partner_analytics`, script-level, expected 216) reproduced at 13 — near-identical to the
month-old number, confirming the regression is real and unresolved by a month of estate growth, not stale.
**New this pass**: the SAME target's function-level form
(`gold:D_01.partner_analytics:generate_header_metrics`, expected 39) matched EXACTLY, 39/39. This split
(function-level clean, script-level broken) points precisely at `comp_marker_read.py::_project()`'s
documented "script-grain s3 rollup" step as the likely mechanism, rather than a wholesale population
shortfall — corroborated independently by 2 of the 9 xref cases showing complete zero-coverage
specifically on file-path-form (script-grain) queries, while most of the other 7 xref cases are near-misses
consistent with ordinary growth since the fixture's vintage, not regression.

Full detail: `deliverables/NFRA_GRAPHUNI_REASSERT/REASSERT_20260725_REPORT.md` +
`REASSERT_20260725_result.json` (all 45 per-target results).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Reuse `cli.main()` in-process via monkeypatch rather than reimplementing blast/trace/xref logic | Isolates the test to the graph SOURCE only — a hand-written second implementation would risk its own bugs and defeat the point of a clean parity comparison. |
| Relocate the script out of CVO~B's fixture directory | That directory is CVO-owned (same `ANY_EXEC`-class lock pattern hit earlier this session on `grain_baseline.json`); read-only access to it is fine, writing a new file there is not this lane's to do. |
| Do not attempt comp-platinum this pass | It uses a structurally different graph source (no TraceGraph at all); forcing a comparison would either be meaningless or require building a second, much larger re-point harness — out of scope for "report per-target match counts," flagged instead. |
| Report the function-vs-script split as the headline addition, not just the aggregate rate | The aggregate (13/45) alone would read the same as the month-old finding; the split is genuinely new information that narrows where a fix should look. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/repro_2_capture_layer_a_REPOINTED.py` | New — the re-pointed measurement script | Yes — this lane's own path |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/REASSERT_20260725_result.json` | New — full 45-target raw result | Yes |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/REASSERT_20260725_REPORT.md` | New — the write-up | Yes |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_reassert_coverage_parity_remeasurement.md` | This log | Yes |

---

## Blockers

None. The 3-option architectural decision (re-populate / re-run pinned / re-baseline — plus a 4th,
narrower option this measurement surfaces: targeted script-grain-rollup repair) is CVO~Z's/CTO~Z's to make,
not blocking this report.

---

## Current State

Fresh, reproducible, per-target measurement delivered. The month-old coverage regression is confirmed still
present and, this pass, localized to a specific mechanism (script-grain s3 rollup) rather than characterized
only in aggregate. Reported to CVO~Z (verifies, per the ruling chain) + CTO~Z this turn.

---

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify this measurement (script + result JSON are on disk, reproducible); rule on
   disposition — the narrower "fix the script-grain rollup" option this pass surfaces, or one of the
   original three.
2. **[1.0.0_SA_CTO~Z]** Route direction once Andrew/CVO~Z have seen this, per the prior hold instruction.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
