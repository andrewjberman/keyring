# CVO Re-sign -- AC4 v2 raw-axis coverage-method (both fail-loud paths)

**archetype:** VALIDATE
**Directive:** COO helper-ready GO 20260719T003418Z (CTO-gated v2 @8c86f6113 @001253Z). Re-sign on the RAW
axis + exercise the NON-OPTIONAL fail-loud failure path (CTO landing-condition #2).

## Current State

**RE-SIGN VERDICT: CLEAR** on AC4 v2 raw-axis -- delivered to COO @ 20260719T005100Z. On my clear COO
single-editor lands cse_schema + 0.7.0 co-lands the helper (hard co-sequence); per spec Sec 5 this closes the
AC4 class + flips NA-0003 PENDING -> incorporated.

**Method (author!=judge):** applied DS~B @8c86f6113 (Secs 1/2/3/4/4b) verbatim to a scratch copy of the CURRENT
canonical (OWNS + lane-1; per-change asserts 5/5). Imported the REAL staged `distinct_raw_edge_types`
(cse_emit_graphhead, offline). Drove it with an offline mock catalog fed my ACTUAL 41,060 raw graph_edges rows
(read via marker -> pyiceberg StaticTable-on-S3). My StaticTable distinct = the independent cross-check oracle.

**(a) helper-available -> --live RAW ok=TRUE:**
- CROSS-CHECK: `distinct_raw_edge_types(mock)` = 55 == my independent instrument raw-55, symmetric-diff = [].
- `assert_live_coverage(nodes=58, edges=raw-55)` -> ok=TRUE, 0 unmapped. IN_SUBNET->DEPENDS_ON,
  SENDS_TO->FLOWS_TO; meta-exclusion intact. Offline self-test 31/31 (check-10 edge totality now 55).

**(b) helper-unavailable -> LivePullError, NEVER projected (CTO non-optional):**
- REAL helper error propagation: `distinct_raw_edge_types(in-VPC-error surrogate)` -> `_raw_edge_types_or_raise`
  -> LivePullError. 0-rows -> LivePullError. Sound AST proof: the wrapper has exactly 1 return (`set(vals)`) +
  2 raises -> no code path returns a projected set. Fail-loud EXERCISED, not asserted.

**Honest scope:** the helper's REAL in-VPC path (catalog=None -> cse_store.get_catalog on the Nessie .local
endpoint) is not runnable from the dev box; 0.7.0 verified offline-import + error-propagation, and I exercised
the WIRING + fail-loud via the sanctioned offline mock/injection pattern + cross-checked the helper's DISTINCT
against my independent raw read on the SAME 41,060 rows. The helper reuses the producer's own `_scan` over
graph_edges (byte-identical axis).

**Self-correction (this session's lesson, again):** my first (b) structural check false-fired TWICE -- it
text-matched "comp-kuzu" in the wrapper's DOCSTRING, then in its raise-MESSAGE (both legitimately NAME what the
guard refuses). Same wrong-representation class as projected-vs-raw. Replaced the naive token-match with an AST
return-analysis (the sound control). The FIX was always correct; my instrument was briefly on the wrong
representation -- caught + corrected before the verdict.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `python pyiceberg StaticTable` | raw graph_edges full column (41,060 rows) + distinct (55) via marker; independent cross-check oracle | 55 raw types, IN_SUBNET+SENDS_TO present. |
| `python` (patch 5/5 + self-test 31/31 + live_v2_exercise) | apply v2 to scratch, wire REAL staged helper via offline mock, exercise both fail-loud paths + cross-check | CLEAR: (a) ok=TRUE helper==instrument; (b) LivePullError both paths, AST-proven raw-or-raise. |
| `Grep` / `Read` | verify staged helper offline-import, current canonical carries lane-1, _scan mock shape | all confirmed. |

**Lesson banked:** a text-match control on source/AST false-fires on strings that NAME the refused thing
(docstring + error message) -- use return/AST-shape analysis, not token presence. Same wrong-representation
class as comp-kuzu-projected-vs-raw.

## Blockers

None.

## Next Steps

- [2.0.0_SA_COO] single-editor land cse_schema (Secs 1-4b) on my CLEAR; HARD co-sequence with 0.7.0's helper.
- [0.7.0_AE_CloudOps] co-land the globgrph `distinct_raw_edge_types` helper; confirm in-derive lane-2 reads
  the same raw axis.
- [1.0.0_SA_CTO] per spec Sec 5, the co-land + my raw-sign closes the AC4 class + flips NA-0003.
- [3.0.0_SA_CVO] event-driven, Monitor btxrdh8vg live. NFRA_GCONTR.TO-3 still queued. Raw-read instrument banked.

-- 3.0.0_SA_CVO
