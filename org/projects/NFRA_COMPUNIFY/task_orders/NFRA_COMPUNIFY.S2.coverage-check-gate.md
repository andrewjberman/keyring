<task_order>
<id>NFRA_COMPUNIFY.S2</id>
<title>NFRA_COMPUNIFY S2 -- THE GATE: build comp-coverage-check (the machine-checkable non-redundancy invariant as enforcement) -- fails when a tool is unplaced OR overlaps a sibling without a declared distinct_from.</title>
<issued_to>0.7.0_AE_CloudOps (gate-infra lane) -- if firefight-pinned, a dedicated build instance (see &lt;allocation&gt;).</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPUNIFY is complete; this TO was last touched 2026-06-30, predating the project close 2026-06-30. Closed as a record act, not a work verdict. Prior status: PASS -- 2026-06-30T20:46Z CTO arch-gate PASS (double-grounded: CTO selfcheck 5/5 + COO~B independent selfcheck all-green; the B6 gate caught a REAL mid-build drift = production proof). comp-coverage-check committed (6560cc103 + 1eb50c3cb), wired advisory B6 in safe-commit.sh + ledger meta_tools + comp-which-routable; AC5 projection-currency in-gate. CTO manifest ruling: comp-coverage-check stays ledger-registered (NO curated tools_index entry -- auto-firing gate, not a situational reflex; curated subset legitimately omits it). Feeds V1 (CVO).</status>
<priority>P2 -- the enforcement that keeps the map true to the territory by gate, not prose (CTO ruling #4). Follows S1.</priority>
<project>NFRA_COMPUNIFY</project>
<dependencies>S1 (needs the populated ledger + the distinct_from declarations to check against).</dependencies>

<context>
CTO ruling #4 (PRD section 6): the non-redundancy invariant is a GATE, not just a doc -- the way the rest of the comp-rail teaches at violation time. comp-coverage-check enforces the load-bearing invariant so the coverage map cannot silently drift from the territory.
</context>

<scope>
  1. Build comp-coverage-check (a comp-tool subcommand and/or a commit/CI gate) that reads comp-coverage-map.yaml and FAILS when: (a) any registered comp-tool is UNPLACED (no single home), or (b) two tools touch the same RESOURCE without a declared distinct_from concern-difference (a silent overlap).
  2. Tri-state honest output (mirror the comp-rail conventions): PASS (every tool one home, every overlap declared) / FAIL (unplaced or silent-overlap, with the offending node named) / UNVERIFIABLE (could-not-read the ledger -- a finding, never a silent PASS).
  3. Register it on the comp-rail (comp-which-routable; manifest entry) + wire it as the COMPUNIFY acceptance gate so future tool additions must place themselves or fail.
  4. NEVER false-PASS a ledger it could not fully read (the never-false-clean discipline).
  5. PROJECTION-CURRENCY (CTO regeneration-ownership ruling, 2026-06-30): comp-coverage-check ALSO asserts the tools_index projection is CURRENT -- run comp_coverage_view.py --verify as part of the gate; a STALE projection (manifest inventory drifted from the ledger union) FAILS the gate. The regeneration itself (comp_coverage_view.py emit -> writes the manifest) runs as an EXEC/CI step, NOT AE-inline (the manifest is ANY_EXEC/exec-controlled; AE inline-regen would be an SoD break). This keeps the ledger the single writer and the manifest a verified-current projection.
</scope>

<locked_rulings>Carry all 4 CTO rulings. This TO IS the materialization of ruling #4.</locked_rulings>

<compiler_tools_mandate>
  <step><run>comp-which "how do existing comp gates (comp-manifest-check / comp-surface-check) wire into commit"</run><expect>match the existing gate pattern so comp-coverage-check fits the established enforcement surface, not a new bespoke mechanism.</expect></step>
  <step><run>comp-coverage-check (the new tool) against the S1 ledger</run><expect>PASS on the landed S1 ledger; deliberately inject an unplaced tool + a silent overlap and confirm it FAILS each with the node named.</expect></step>
</compiler_tools_mandate>

<acceptance_criteria>
  1. comp-coverage-check exists, registered + comp-which-routable, fails on unplaced-tool AND on silent-overlap (both demonstrated), PASSes the clean S1 ledger, and reports UNVERIFIABLE rather than false-PASS on an unreadable ledger.
  2. Wired as the COMPUNIFY enforcement gate.
  3. RAVC2 to COO~B (cc CTO); feeds V1 (CVO verifies the gate actually enforces).
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_COMPUNIFY_PRD.md (section 6 ruling 4, section 8)</ref>
  <ref type="depends-on">NFRA_COMPUNIFY.S1 (populated ledger)</ref>
  <ref type="pattern">existing comp-manifest-check / comp-surface-check gates</ref>
</references>
</task_order>
