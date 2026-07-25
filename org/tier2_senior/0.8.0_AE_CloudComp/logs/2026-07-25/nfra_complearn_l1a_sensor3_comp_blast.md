# NFRA_COMPLEARN L1a-SENSOR-3 — DAG-shaped residue sensor (comp-blast) — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** NFRA_COMPLEARN L1a-SENSOR-3 (MCP dispatch from 1.0.0_SA_CTO~Z 20260725T090835Z;
off-main-fabric group convention, no XML TO)
**Status:** COMPLETE
**Cycle wall:** ~09:08Z dispatch → ~09:35Z deliverables on disk

---

## Objective

Build L1a residue sensor #3 — the DATA/DAG-shaped one where `doc_only` is honestly N/A — per the
ontology docs' build order (COMPLEARNS opens on TOOLUNIFY's verified exit bar). Derive the tool's
traversal from its own code, diff against the source's real unit enumeration, emit a conformant
boundary_report, controls + denominator + UNKNOWN first-class.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `pytest` (L0a conformance) | `test_boundary_report_conformance.py -q` | PASS | 17/17 on this tree before any sensor work |
| `commit-gate` | `.tools/commit-gate.sh l1a_sensor3_comp_blast.py` | PASS | py_compile + AST + ruff py39 clean |
| `l1a_sensor3_comp_blast.py` (new) | `--grain node_type --graph <nonexistent>` | REFUSE rc=3 | NEGATIVE CONTROL — refusal, never everything-is-residue |
| `l1a_sensor3_comp_blast.py` | `--grain node_type --graph <synthetic mini-DAG>` | PASS rc=0 | POSITIVE CONTROL — CLEAN, conformant (BR008-only) |
| `l1a_sensor3_comp_blast.py` | `--grain edge_type --emit <census dir>` | PASS rc=0 | R1 real: 13/13 covered (BFS AST-verified type-blind at run time); declared-set drift in-band; conformance clean |
| `l1a_sensor3_comp_blast.py` | `--grain node_type --emit <census dir>` | VERDICT rc=2 | R2 real: covered 3 / orphan 7; 2 dead filter members in-band; conformance BR008-only by design |

**What worked:** deriving the traversal by EXECUTING the tool's own code (`_producer_node_types()`
called, not read) and by run-time AST inspection (type-blind BFS verified each run, degrading to
UNKNOWN if a filter ever appears) — both derivations re-verify themselves on every invocation, so the
sensor cannot silently carry a stale traversal claim. The live path-convention standing rule fired
mid-build: handing a `/cygdrive/c/...` fixture path to native python3 failed exactly as the rule
predicts; corrected to native `C:/...` and the miss is disclosed here rather than hidden.

**What failed (mine, disclosed):** the one `/cygdrive` slip above — caught immediately by the
sensor's own REFUSE (which is the negative-control behavior doing its job on an unintended input).

**Gap found:** two live frozen-enumeration drifts inside the comp-blast engine (deliverable §4.1/4.2):
`_producer_node_types()` misses 7 live node_types and carries 2 dead members; `EDGE_TYPES` misses 8
live edge_types and carries 3 dead. Routed to CTO~Z, not actioned.

Auto-log rows: the sensor is not a registered comp-tool (registration is explicitly UNBUILT scope), so
no comp_log_auto rows; session line appended to `org/compiler-tools-log.md` manually.

---

## Work Completed

1. Read, in dispatch order: `IMPLEMENTATION_LEVELS_AND_SEQUENCING.md` (§4 L1a + §6 failure modes),
   `SENSOR_CONTRACT_PLATFORM_OR_PATTERN.md` (§3 DAG inversion), `boundary_report.py` + conformance
   suite (BR008 open-set; `{applicable,count,method}`; N/A-never-0).
2. Stated tool choice + unit-grain decision to CTO~Z BEFORE building (20260725T091429Z): comp-blast;
   the DAG's TYPE plane; two reports (edge_type / node_type), two traversal modes (BFS / producer
   filter); proceeding under ALWAYS-PROCEED with Monitor live for interjection.
3. Grounding sweep before coding: live census (10 node_types / 13 edge_types), measured mention map
   (5/13 edge, 7/10 node literals in engine files), BFS walk bodies read, `__main__` guard confirmed.
4. Built `l1a_sensor3_comp_blast.py` (census dir, commit-gate clean). Ran negative control, positive
   control, R1, R2 — separate invocations, TRUE_RC in stdout throughout.
5. Authored `L1A_SENSOR3_comp-blast.md` + emitted both report JSONs to the census dir (on disk for
   CTO~Z commit).

## Decisions Made

| Decision | Rationale |
|---|---|
| Two reports, one per grain, never cross-aggregated | address-portability rule; grains are different address spaces |
| R2 keeps `dag_node_type` (BR008) rather than coercing to a known space | open-set visibility is the design; coercion is the vocabulary-poverty defect the type exists to detect |
| `member` = applicable true, count 0 (not N/A) | the cell is expressible at this grain — no unit occupies it for these traversals; N/A would be a false claim of inapplicability |
| UNKNOWN excluded from `surface_total` with printed disclosure | keeps BR004 accounting balanced while keeping UNKNOWN first-class and visible |
| Traversal derivations re-run at every sensor invocation | a one-time derivation is a declared claim by the second run; live re-derivation cannot drift |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.../NFRA_TOOLUNIFY_CENSUS/l1a_sensor3_comp_blast.py` | New — sensor code | No — CTO~Z-owned path, on-disk for CTO~Z commit |
| `.../NFRA_TOOLUNIFY_CENSUS/L1A_SENSOR3_comp-blast.md` | New — deliverable | No — same |
| `.../NFRA_TOOLUNIFY_CENSUS/L1A_SENSOR3_comp-blast.report.{edge_type,node_type}.json` | New — emitted reports | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_complearn_l1a_sensor3_comp_blast.md` | This log | This session, own lane author |
| `org/compiler-tools-log.md` | Session line appended | This session |

## Blockers

None.

## Current State

L1a-SENSOR-3 delivered: DAG shape, doc_only honestly N/A, both controls pass as separate invocations,
both real reports emitted and conformant (clean / BR008-only), two live frozen-enumeration findings
routed. Reported to CTO~Z + CVO~Z this turn. Event-driven, standing by.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit the 4 census-dir files; rule on §4.1/§4.2 (filter + declared-set
   drift); decide the `dag_node_type` KNOWN_ADDRESS_SPACES question (§5).
2. **[3.0.0_SA_CVO~Z]** Independent re-derivation — invocations + RCs in deliverable §3; both
   mechanism claims self-re-derive on any run of the sensor.
3. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.
