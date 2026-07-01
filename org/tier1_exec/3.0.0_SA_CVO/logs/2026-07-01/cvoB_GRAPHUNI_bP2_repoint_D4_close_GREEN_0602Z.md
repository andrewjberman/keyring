# CVO~B GRAPHUNI (b) per-tool re-point + D4 one-head -- GREEN. GRAPHUNI closes (vintage-unified).

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~0558-0602Z
**Trigger:** ~D RAVC (b) per-tool re-point -- all 4 structure tools head-pinned build_graph (cli.py e0d839996 + graph_cache 70ff64a56). Joint verdict (b)-GO converged (CTO 055325Z accepted both my caveats).
**Method (per my fixture-owner ruling + CTO convergence):** set-equality vs the FROZEN fixture using its EXACT capture method; classify every delta MATCH / SOURCE-DRIFT (legit) / RE-POINT-REGRESSION (block). (b) = same build_graph EXTRACTION -> zero re-point regression by construction; validated, not assumed.

## VERDICT: **GREEN** -- all 4 tools re-pointed with ZERO re-point regression; D4 no-divergent-vintage confirmed. GRAPHUNI closes VINTAGE-unified. (a) graph-unification = the tracked finish I own.

## Per-tool set-equality (re-pointed vs frozen fixture, fixture-exact method) = GREEN
- **comp-blast: 28/28 byte set-equal** (all sampled fn/script/s3 targets; D_01.partner_analytics=216, NOT the 13 the literal Kuzu-projection would give -- the coverage my fixture caught is PRESERVED).
- **comp-trace: 6/6 byte set-equal** (up+down sets; the 2 documented empty-both-ways soft-spots excluded per FIXTURE_ATTESTATION S5).
- **comp-platinum: 8/8 byte set-equal** (component-page chain SHAs).
- **comp-xref: 7/9 byte set-equal + 2/9 SOURCE-DRIFT** (`main`/`log`): matched-node-ID SET IDENTICAL (semantic answer unchanged); only the raw header count -1 (110->109 / 80->79). DECISIVELY confirmed source-drift, NOT re-point regression: a FORCE-FRESH build_graph rebuild gives the SAME 109/79 as the cache-served re-pointed tool -- both differ from the 20h-stale fixture (110/80). So re-pointed == fresh build_graph; the fixture is simply stale on gold source since its 06-30 21:48Z capture.

**Zero RE-POINT regression across all 4 tools.** Every non-MATCH is grounded source-drift (re-pointed == fresh build_graph), never a coverage loss -- exactly the bar per the joint verdict ("no re-point regression," not "byte-identical to a stale snapshot").

## D4 one-head / no-divergent-vintage = GREEN
graph_cache head-pin (70ff64a56, "honor source fingerprint, no divergent-vintage serve"): the DEFAULT now serves the build_graph cache ONLY when the source fingerprint matches current source; a drift degrades to a cache-miss -> rebuild. So no structure tool can serve a stale/divergent vintage -- the exact stale-cache-phantom class that produced the INF_D_00e 1347-phantom I caught pre-fire is STRUCTURALLY eliminated. Combined with comp-kuzu/comp-depth on the marker-current head (5434137157015633165), all tools are pinned to the current vintage.

## HONEST LABEL (CTO + CVO concurred -- do NOT oversell)
GRAPHUNI closes **VINTAGE-unified**: anti-drift (D4 one-vintage, phantom-class killed), same answers, no re-point regression. It is NOT **GRAPH-unified**: comp-blast/trace/xref/platinum read head-pinned build_graph; comp-kuzu/comp-depth read the Nessie marker-head -- two graphs, one vintage. Andrew's "ONE graph, natural to traverse" goal = option **(a)**, gated on REAL population work (the missing cross-script s3 bridges my fixture DOCUMENTED, not cosmetic). I own the (a) coverage-equivalence proof with a PINNED measurement method (--direction both, all classes, set-form -- since the coverage number swings 5-16x by method).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| repro-method set-equality (blast/trace/xref/platinum) vs frozen fixture | independent per-tool re-point no-regression | PASS -- blast 28/28, trace 6/6, platinum 8/8, xref 7/9+2-source-drift; ZERO re-point regression |
| `cli.py build` force-rebuild + xref compare | confirm the xref delta is source-drift (fresh==cache != stale-fixture) | PASS -- fresh 109/79 == cache-served, != fixture 110/80 => source-drift, not regression |
| graph_cache 70ff64a56 mechanism read | D4 source-fingerprint drift-gate | PASS -- serve-if-fresh-else-rebuild; no divergent-vintage serve |

What worked: classifying deltas as SOURCE-DRIFT-vs-REGRESSION via a force-fresh rebuild (re-pointed==fresh proves zero re-point delta) is the airtight discrimination -- it kept a legit 20h source-drift from false-REDing the re-point AND would have caught a real regression. The fixture caught the real Kuzu-projection coverage gap earlier (216->13) AND now certifies the (b) path is answer-clean -- the same control doing both jobs.

## Next Steps
1. **[2.0.0_SA_COO~B]** GREEN -> 2-step close GRAPHUNI (label VINTAGE-unified; carry (a) as the tracked true-unification follow-on). With GRAPHDEPTH P3 GREEN, the NFRA_COMP*/GRAPH* group is closed.
2. **[3.0.0_SA_CVO~B]** I own the (a) coverage-equivalence workstream: pin the measurement method + prove the unified Nessie slice is coverage-complete (cross-script s3 bridges) before any literal-Kuzu re-point. That is the true "one graph, natural" finish.

-- 3.0.0_SA_CVO
