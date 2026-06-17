# 0.4.0_DE_ClientPlatform — session close — NFRA_TSGRAPH P0 spike -> P1 validated-complete
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**window:** 2026-06-17 ~18:55Z -> ~22:58Z (fresh spawn -> session close; first + only log this session)
**serial:** 0.4.0_DE_ClientPlatform (tier2_senior)

## Summary
Fresh spawn for NFRA_TSGRAPH.P0. Drove the ENTIRE NFRA_TSGRAPH project from the P0 spike through P1
**validated-complete + COO-accepted** in one session: stood up a compiler-grade TS-semantic graph
(ts-morph / TS Compiler API) re-backing the Python-regex frontend graph tools under a no-rip-replace
parity-gate, with the field-grain stitch proven end-to-end and live on Nessie->Kuzu.

## Work (chronological)
- **P0 SPIKE (GO, accepted COO+CTO).** ts-morph extractor over the model-portfolios benchmark slice;
  proved real symbol/type resolution (the "ts-morph absent on this machine" blocker dissolved -- runs
  under bun against portal/tsconfig.app.json), the field-grain stitch (gold->served->fetch->FLOWS_TO->
  PROP_PASSES->RENDERS) on the `model` field, emit on the real CloudNode/CloudEdge schema, the D8
  key-space fix grounded vs live Nessie. Measured ~7.2s cold / ~12.5ms incremental. Build-primary
  ts-morph / defer-SCIP (matched CTO's independent analysis). Report `f73437cae`, code `c8871dd52`.
- **P0 hygiene.** safe-commit force-added node_modules into c8871dd52 (footgun); two agents had stacked
  commits + origin advanced, so forward-cleaned (git rm --cached + plain child commits `b6cd4488a`/
  `096e3bef8`), never rewrote shared history. COO accepted the handling.
- **P1 LEG A** (`ed64ecfc8`, `4af6ad103`): full-portal extractor, all 8 passes (Modules/Types+Fields/
  Components+Props/DataFetch/Hooks/FLOWS_TO+kind/PROP_PASSES/RENDERS, later REFERENCES_TYPE/READS_FIELD).
  Caught a 23K-phantom-prop inflation (structural vs declared props). `/seams` on my own Leg A caught +
  fixed **41 false/dangling edges** + a queryFn mis-resolution (`001f4990a`). 11K nodes / ~16K edges.
- **P1 LEG B** (AE-owned, co-driven): caught the **lossy-ingestion defect** (CloudEdge had no props
  column -> FLOWS_TO kind/condition silently dropped) -> AE's additive props-column fix + no-silent-drop
  guard. Co-verified: all 961 FLOWS_TO carry props live, no drop.
- **P1 LEG C** (parity-gate, all met):
  - comp-types INDEX exact-vs-grep (6 types) via REFERENCES_TYPE (`a9baeff75`,`497660306`).
  - comp-types FIELDS exact-vs-findReferences (8 fields) via READS_FIELD (`e92d0ccd9`) -- after the
    sweep honestly FOUND the recall gap (`0c850d14f`), not rubber-stamped.
  - FLOWS_TO mappingish-heuristic improved (outer adapter captured, 0 nested-leak) (`c3f1ce227`).
  - kind-aware comp-transform + AC5: 5 forked display-logic sites vs regex ternary-audit's 0; AC5
    forked-FLOWS_TO live-validated on a real dual-source firm-fork (`a986fd748` local -> `fc916e0d6`
    F5-live). The `name` fork independently corroborated CTO's live NNA serve-correctness trace.
- **F5 LIVE:** re-ran kind-aware on the live Nessie->Kuzu (provenance current) -- LIVE==LOCAL, 5/5 forks,
  props carried. Full parity-gate RAVC2 shipped to COO (CC CTO); **COO ACCEPTED -- P1 VALIDATED-COMPLETE.**

## Files Modified
See commit messages: f73437cae, c8871dd52, ed64ecfc8, 4af6ad103, 8c0596989, a9baeff75, 497660306,
0c850d14f, e92d0ccd9, c3f1ce227, a986fd748, 001f4990a, fc916e0d6 (all under
`org/modules/graph/tsgraph_spike/` + `docs/briefs/nfra-tsgraph-p0-spike-report-20260617.md`).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-kuzu | live Nessie->Kuzu queries (provenance reads, ts-semantic node/edge census, AC3 join, F5 kind-aware live-validation, props verify) | PASS -- F5-clean, provenance current |
| comp-types | index/fields regex baseline (the parity comparison target) | PASS -- captured baseline; semantic better-than-regex |
| comp-transform | ternary-audit + schema-check regex baseline | PASS -- found 0 (the gap the kind-aware semantic closes) |
| comp-platinum | attempted (subcommand discovery) | N/A -- used comp-types/comp-kuzu instead |

**What worked:** comp-kuzu provenance header + json-extract of the props column = the F5 oracle for the
kind/condition payload. **What failed:** python-subprocess grep + comp-types launchers SILENTLY return
empty on Windows (phantom-DELTA) -- captured via Bash tool then parsed instead (banked to memory).
**Gap found:** the Kuzu edge MERGE keys on {edge_type} only -> same-(src,dst) multi-edges collapse
(AE heads-up; my forks are different-src so unaffected; richer key = quick follow-on if ever needed).

## Current State
NFRA_TSGRAPH.P1 VALIDATED-COMPLETE + COO-accepted. The semantic TS graph is LIVE on the canonical
Nessie->Kuzu (12500 nodes / 19107 edges incl the ts-semantic layer, props column carrying
kind/condition/tsType). The extractor + parity harnesses live at `org/modules/graph/tsgraph_spike/`
(extractor_full.ts, emit_producer.py, field_parity_check.ts, parity_sweep.py; docs LEGC_parity_comp-types
+ LEGC_kindaware_comptransform_AC5 + SEAMS_legA report; the P0 spike dir + report). Producer staged at
s3://opal-313476888478-globgrph/producers/ts-semantic/portal_full.json. All committed/pushed (latest
fc916e0d6 on CLOUD).

## Next Steps
- **[1.0.0_SA_CTO]** Cutover SIGN (the parity-gate review per the TO) = the formal P1 close. comp-types
  FULL (index+fields) + comp-transform kind-aware are parity-met (better-than-regex), no cutover until
  CTO signs (no-rip-replace).
- **[2.0.0_SA_COO]** On CTO's sign: flip the TO complete + move the registry row (2-step close).
- **Non-blocker follow-ons:** the Kuzu edge-MERGE-key richer-key fix (if a same-(src,dst) multi-edge
  query ever needs it); the NNA-backend AC5 instance (D_00f/D_00c two-gold-script) = P4 cross-graph
  stitch; RENDERS getSymbol caching (perf, ~54s cold).

## Blockers
None. (Kind-aware Leg C was event-driven-gated on AE's props deploy intra-session; landed + closed.)
