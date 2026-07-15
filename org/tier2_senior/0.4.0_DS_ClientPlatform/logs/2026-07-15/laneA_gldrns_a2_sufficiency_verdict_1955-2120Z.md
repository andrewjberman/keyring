# OPAL_GLDRNS.A2 COMPLETE — the B/C->D sufficiency verdict: 88 fields versed, 5 MISSING to CTO, 10 divergences pre-declared

**archetype:** TRACE
**secondary_archetypes:** VALIDATE, SCRIBE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-15 ~19:55Z -> ~21:20Z
**TO:** OPAL_GLDRNS.A2 (batch GO 192248Z; A1 closed-accepted 205419Z with 3 findings rulings folded)

## Summary

Deliverable: `deliverables/BC_TO_D_SUFFICIENCY_VERDICT_49F_20260715.md`. Column-level census of all
8 D publishers (static source extraction @ 0f248d7f9, raw pass preserved in scratchpad; extraction
caveat + lower-bound labeling stated in-doc) mapped against the ratified plan (baba79230), dictionary
v0.5, Wave-2 cores (80240881d), D1 dim v1.1. **The C5b answer: planned shapes SUFFICIENT except 5
MISSING cells** — M1 served-firm-AUA authority post-cert (the biggest: what number the portal headline
shows) + M2 role_aua table owner (proposed C_08 emit; kills the inverted D_02 edge) structural; M3
office dim, M4 pct_priced, M5 hh_seen single-cell. 88 fields versed (CARRIED 61 / RENAMED 3 /
DERIVED-IN-D 7 / MISSING 5 / UNKNOWN 2 / DELETED-LAYER 10); 10 divergences PRE-DECLARED for the S4
harness (synthetic term disappears; classifier swap; tax-from-title; binary fee-presence; cert
retirement; SCD2 role periods; FIFO->vendor lots; first-seen semantics; per-type history floors vs MAX
windows; ofc pending M3). cohort_a discrimination cell (CTO ruling 3): live consumer, FAIL-SILENT on
the 404 (49financial/index.tsx:191-196 calls, :309 conditional render) -> renders-and-fails class ->
escalated CTO+DT, fix held for their verdict. Andrew DIRECTIVE 8 (via CTO 210455Z) folded mid-flight:
sec-7 IMPROVEMENT-CANDIDATES (8 rows, each naming its D-emitter — manifest-based cleanup, schema_version
everywhere, basis labels, 36MB pass-through retirement/gzip, path-grammar unification, role_aua-as-C_08,
dual-write retirement, incremental publish).

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| comp-pipescript io x8 | cited from A1 (same session, same vintage) | PASS-EMPTY | D-group dynamic keys; the A1/A2 docs are the mandated manual review |
| comp-kuzu | 3 queries (schema discovery + account_performance edges) | PASS w/ caveat | provenance header read: graph_nodes STALE >6h cadence — used as CORROBORATION only (script-grain edges match census; column grain only exists in source). Learned: edge table = CloudEdge, no `kind` property; bd legacy producer named C_03.account_performance in-graph; C_01b.role_aua_backfill exists (strengthens M2/I6) |
| comp-blast | not re-run in A2 | — | one sentence why: A1's D_04 blast + the source-import census carry the shared-C-table consumer map at COLUMN grain, which blast does not model; the A1 utf-8 workaround stands for any future run |
| comp-glob | 1x (W1 census locate) | PASS | on-rails |
| custom static extractor (python, scratchpad) | 1x over 8 scripts | PASS | 204-line raw census; method + caveat stated in deliverable sec-1 |

Appended org/compiler-tools-log.md line same commit.

## MCP traffic

IN: CTO A1 acceptance + 3 rulings (205419Z); CTO FYI Andrew DIRECTIVE 8 template + improvement-candidates
ask (210455Z). OUT: A1 RAVC close; ACK of rulings; A2 RAVC close + cohort_a escalation (this window's end).

## Blockers

NONE for the lane. A2's M1/M2 are CTO decision cells (the TO's designed output, not blockers); A3 opens
now per the batch GO and does not need them resolved to build the harness (it needs A2's divergence
list, which exists).

## Current State / Next Steps

1. **[NOW]** A3 opens: the S4 parity harness (committed, field-level, streak accounting, declared
   divergences report DESIGN / undeclared FAIL) + the read-only dry-fit (D_04 preferred) against
   canonical seed C-equivalents, scratch-sink absolute, comp-pipescript postdeps before ANY execution,
   CTO gate before any execution beyond read-only analysis.
2. Watchers: inbox Monitor bmzbcge9k LIVE. A1 @ 9be9c2402 origin-verified; A2 commit next to this log.
