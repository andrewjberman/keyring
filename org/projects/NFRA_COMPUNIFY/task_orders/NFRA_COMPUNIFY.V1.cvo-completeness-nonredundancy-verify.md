<task_order>
<id>NFRA_COMPUNIFY.V1</id>
<title>NFRA_COMPUNIFY V1 -- CVO VERIFY: completeness (every tool one home, zero unplaced) + non-redundancy (every overlap declared, zero silent) + tools_index-is-generated-view + seam-IDs-shared-with-COMPDRIFT. The PRD section 8 acceptance/exit.</title>
<issued_to>3.0.0_SA_CVO (the completeness + non-redundancy verifier -- PRD-named).</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>complete -- SPRING-CLEAN 2026-08-25: project NFRA_COMPUNIFY is complete; this TO was last touched 2026-06-30, predating the project close 2026-06-30. Closed as a record act, not a work verdict. Prior status: staged</status>
<priority>P-verify -- the acceptance gate. Event-driven on S1 (+ S2/S3) landing; lighter than the build, so CVO can hold it alongside its firefight gates.</priority>
<project>NFRA_COMPUNIFY</project>
<dependencies>S1 (the populated ledger + censuses) is the minimum; S2 (the gate) + S3 (routing) fold in as they land.</dependencies>

<context>
PRD section 8 acceptance/exit. CVO holds the load-bearing honesty verify for the whole macro: is the MAP actually COMPLETE and NON-REDUNDANT, against ground truth -- not merely authored. Grounds against the real ledger + a real comp-which/raw-grep reproduction, never the builder's self-report.
</context>

<scope>
  Verify against the landed artifacts (ground truth, not self-report):
  1. COMPLETENESS -- every comp-tool placed at exactly one (surface|seam) x granularity x concern node; ZERO unplaced. Cross-check the tool set against the live manifest/registry so no tool is silently omitted.
  2. NON-REDUNDANCY -- every shared-resource overlap carries a declared distinct_from concern-difference; ZERO silent overlaps. Spot-reproduce: pick a declared overlap (e.g. the IAM x3) and confirm the three concerns are genuinely distinct in behavior, not just labeled.
  3. GENERATED-VIEW -- tools_index is a regenerated projection of the ledger (ruling #1), NOT a parallel hand-maintained catalog. Confirm regenerating it changes nothing vs the committed view.
  4. ONE-SEAM-ARTIFACT -- COMPUNIFY's seam axis references the SAME drift-topology.yaml seam IDs COMPDRIFT uses (ruling #2); no duplicated/diverging seam set.
  5. GATE HONESTY (once S2 lands) -- comp-coverage-check actually FAILS an injected unplaced-tool + silent-overlap, and reports UNVERIFIABLE rather than false-PASS on an unreadable ledger.
  6. GAP-CENSUS GROUND TRUTH -- a sampled flagged gap (e.g. ms-cloud high-level) reproduces as a real coverage gap (a raw-grep/escape on that surface), not a phantom.
</scope>

<acceptance_criteria>
  1. A CVO verdict per the 6 axes above, each grounded in a cited live read (sharpest-test-binds; could-not-verify is a finding, never a silent pass).
  2. PASS = the macro's exit is met (ledger + both censuses landed, gate live + enforcing, generated-view confirmed, seam IDs shared). Any FAIL routes back to the build lane via COO~B with the specific node/axis.
  3. RAVC2 to COO~B (cc CTO + MSTR). This verdict closes the COMPUNIFY macro and authorizes the COMPDRIFT/COMPLEARN re-points at the now-stable schema.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_COMPUNIFY_PRD.md (section 8 acceptance/exit)</ref>
  <ref type="verifies">NFRA_COMPUNIFY.S1 (+ S2, S3)</ref>
  <ref type="grounding-discipline">CLAUDE.md Rule 22; /verify-channel + /seams completeness method</ref>
</references>
</task_order>
