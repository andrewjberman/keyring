<task_order>
<id>NFRA_PASSCRAFT.TO-R0</id>
<title>R0 RULING (CVO) -- classify the QUESTION before the CLAIM: rule whether R0 is a NEW rail or R1 read correctly, and own the RAIL_SET the front pass grades against</title>
<issued_to>3.0.0_SA_CVO (owns R0 + the RAIL_SET, independent of the PASSCRAFT design so the grader stays independent of the graded). **STAGED -- HELD, DO NOT ROUTE TO CVO (CTO~A ruling 2026-07-10):** CVO is base-CTO's lane -- routing a rail-ruling to CVO is DRIVING CVO, which is base-CTO's to initiate, not COO~A's/CTO~A's; and COO~A's cross-agent messaging is not Andrew-cleared (same constraint as the base-CTO courtesy notice). R0 is a PROPOSED rail; route it ONLY when Andrew clears the CVO path OR base-CTO's front-pass chain picks up the R0 question on its own. **NOTHING is blocked by this hold** -- TO-2 does not gate on R0 (only its OPTIONAL R0 fold does). CVO is the certifier of this program; this ruling is a CVO deliverable, not a build dispatch -- it gates TO-2's R0 fold but nothing else.</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate. CTO~A REQUESTS the CVO ruling per PRD sec.3c.)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_PASSCRAFT, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: staged</status>
<priority>GATING for TO-2's R0 fold ONLY -- the rest of PASSCRAFT does not block on it. Routed to CVO because R0 is a RAIL question (TOOLPASS sec.5a gives the rail set to CVO, not to the PASSCRAFT design PRD). The grader stays independent of the graded.</priority>
<project>NFRA_PASSCRAFT</project>

<context>
PASSCRAFT sec.3c proposes R0: classify the QUESTION before the CLAIM. A DYNAMIC question (which-branch-ran / what-value-flowed / did-a-side-effect-happen / who-reads-X-at-runtime / what-the-served-artifact-contains) answered FROM SOURCE is auto-`INFERRED`, regardless of reading-confidence. R0 would sit UPSTREAM of R1 and make R1's self-classification mechanical. The tool-1 failure was exactly this class: 4 of 10 findings wrong, all one error -- a DYNAMIC question answered with STATIC evidence. CTO~A requests CVO rule whether R0 is a genuinely new rail or whether R1, read correctly, already covers it.
</context>

<scope>
1. **RULE:** is R0 a NEW rail upstream of R1, or is it R1 applied correctly? Ground the ruling in the RAIL_SET CVO owns (TOOLPASS sec.5a) -- source-cited, not asserted.
2. If R0 is ruled IN: specify it as a rail (the DYNAMIC-question test + the auto-INFERRED disposition) and hand it to PASSCRAFT.TO-2 for the emitter fold.
3. If R0 is ruled OUT: state how R1-read-correctly covers the DYNAMIC-question case, so TO-2 does NOT double-implement it.
4. Own the RAIL_SET going forward as the certification reference the front pass grades against.
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **GRADER INDEPENDENT OF THE GRADED:** CVO owns R0 + the RAIL_SET independent of the PASSCRAFT design (CTO~A arch-gates the design; CVO owns the rails).
  2. The ruling is SOURCE-CONFIRMED, not INFERRED (reserved-word discipline, CLAUDE.md Rule 22): cite the RAIL_SET at file:line @ commit-ish.
</locked_invariants>

<acceptance_criteria>
  - A recorded CVO ruling: R0 IN (specified as a rail) or R0 OUT (R1-covers-it, with the source cite), handed to PASSCRAFT.TO-2.
  - The RAIL_SET is CVO-owned + version-pinned as the front-pass certification reference.
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_PASSCRAFT_PRD.md @ 362272cce (sec.3c R0)</ref>
  <ref type="doctrine">NFRA_TOOLPASS sec.5a -- the rail set is CVO-owned</ref>
  <ref type="gates">NFRA_PASSCRAFT.TO-2 (the R0 emitter fold waits on this ruling)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>A ruling + rail specification. No code, no served artifact.</no_reprocess_needed></data_reprocess_scope>
</task_order>
