<task_order>
<id>NFRA_GRAPHUNI.P0-CVO</id>
<title>NFRA_GRAPHUNI P0 (CVO) -- capture the PRE-DELTA no-regression FIXTURE: snapshot the four structure-tools' current answers BEFORE any re-point. The load-bearing risk control.</title>
<issued_to>3.0.0_SA_CVO (owns the no-regression fixture + one-head verify)</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_GRAPHUNI is complete; this TO was last touched 2026-06-30, predating the project close 2026-07-01. Closed as a record act, not a work verdict. Prior status: dispatched -- 2026-06-30T20:20Z GO'd to 3.0.0_SA_CVO on CTO decomp-approval. P0 IMMEDIATE, time-critical (pre-delta capture before any P1 mutation). CVO's FIXTURE-LOCKED signal is the HARD GATE that releases ~D's P1 dispatch (COO~B holds P1 on it). Priority over COMPUNIFY V1.</status>
<priority>P0 IMMEDIATE -- the LOAD-BEARING risk control (PRD section 4). TIME-CRITICAL ORDER: this fixture MUST capture answers while the OLD caches are still authoritative -- i.e. BEFORE P1's first derive/mutation. Read-only; runs parallel to ~D's P0 audit.</priority>
<project>NFRA_GRAPHUNI</project>
<dependencies>NONE -- captures CURRENT (pre-delta) state. HARD ORDERING: must lock BEFORE NFRA_GRAPHUNI.P1 (the first graph mutation). Pairs with NFRA_GRAPHUNI.P0 (~D's audit).</dependencies>

<context>
The PRIMARY project risk (MSTR-named, CTO Ruling 4 + section 4): a re-pointed comp-blast/comp-platinum MUST return the SAME answers as the pre-delta caches -- zero coverage regression. The empirical guard is a frozen fixture captured BEFORE any re-point, while the current caches are still the source of truth. P2 verifies each re-pointed tool reproduces this fixture SET-equal; any delta blocks that tool's D3 retirement. If the fixture is captured AFTER a mutation, the regression baseline is corrupted -- hence this is ordered FIRST, with ~D's read-only audit, before P1.
</context>

<scope>
  1. Snapshot a REPRESENTATIVE set of CURRENT (pre-delta) answers from the live caches/tools:
     - comp-blast: (function name -> blast-radius set) over a representative function sample.
     - comp-xref: (symbol -> xref set) over a representative symbol sample.
     - comp-platinum: (component -> full-stack chain) over a representative component sample.
     - comp-trace: a sampled set of trace walks.
  2. Ensure the sample is REPRESENTATIVE -- hot paths covered (the answers are SET-based; capture them order-independent so P2's set-equality comparison is clean).
  3. Freeze the fixture as a durable artifact (the P2 comparison baseline). Independently confirm it captures the coverage the gap-list (~D's P0) says the tools traverse -- so a post-re-point match genuinely proves no-regression.
</scope>

<acceptance_criteria>
  1. A frozen pre-delta fixture: {comp-blast, comp-xref, comp-platinum, comp-trace} current answers over a representative (hot-path-covering) sample, set-form, durable.
  2. Captured BEFORE any P1 graph mutation -- evidenced (vintage/timestamp vs the P1 derive).
  3. CVO attests the fixture is representative + sufficient to detect a real coverage regression per-tool in P2.
  4. RAVC2 to COO~B, cc CTO. This fixture is the P2 per-tool no-regression gate + part of the section-8 acceptance.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_GRAPHUNI_PRD.md section 4 + Ruling 4 (da61986ff)</ref>
  <ref type="pair">NFRA_GRAPHUNI.P0 (~D's D1 audit/gap-list)</ref>
  <ref type="gates">NFRA_GRAPHUNI.P2 (per-tool re-point) -- each tool's D3 retirement gated on reproducing this fixture set-equal</ref>
</references>
</task_order>
