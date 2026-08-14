# MDPF_TRGALN.TO-5 DRAFT — atom_decomp truth-pass on Inflection stacked-bar holes (READY TO FILE at MSTR allocation)

**Status: DRAFT — assignee allocation is at MSTR** (PRD v1.1 §8.2 @f50ee7223b: atom_decomp method
homed at CRO; CRO base live). The moment MSTR names the owner, COO files this verbatim as
`org/<owner-tier-path>/task_orders/MDPF_TRGALN.TO-5.inflection-atom-decomp-truth-pass.md` with
issued_to set — zero authoring delay at the §8.2 gate (TO-0..TO-3 applied + proofed).

---

<task_order id="MDPF_TRGALN.TO-5" project="MDPF_TRGALN">
<issued_to>PER MSTR ALLOCATION (atom_decomp homed at CRO)</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued>(at filing)</issued>
<status>pending</status>
<priority>P0 — GO from COO when TO-0..TO-3 are applied + proofed (§8.2 gate). Completes TONIGHT.
Andrew's explicit method call: atom_decomp on ALL relevant surfaces BEFORE any fix is pursued.</priority>

<references>
  <ref type="prd">docs/architecture/MDPF_TRGALN_PRD.md v1.1 @f50ee7223b — §8 verbatim + §8.2 measured localization, §7 proof schema</ref>
</references>

## SCOPE (PRD §8.2)

atom_decomp truth-pass across the full surface chain: served
`platinum/mdpf/inflection/aggregate-aua-timeseries.json` → gold slice
(`portal/gold/mdpf/inflection/`) → builder (`dim_mdpf_aggregate_aua_timeseries.build_inflection_artifact`
+ carry-forward union logic) → monolith inputs (`orion/inflection/silver/fact_assets`,
`eclipse/inflection/silver/*`) → vendor rawest available.

**Measured starting facts (v1.1, 05:0xZ, 443 served dates 2024-11-01→2026-08-11):**
- 7 FULLY-EMPTY dates (model AND non_model null): 2026-05-20, 05-29, 06-30, 07-10, 07-13, 07-14,
  08-05 — the "did not used to be here" regression class.
- 390/443 dates model_aua sum == 0 (gray-only bars); first nonzero model date 2026-05-15.
- Which zero dates are TRUE history (model program ramp) vs MISSING is exactly what this pass
  adjudicates — assume NEITHER way.
- 2026-08-05 is also the platinum-cutover carry-forward date — correlation TESTED, not assumed.

## DELIVERABLE

Per-date truth table for every hollow/empty date:
`TRUE-ZERO | MISSING-AT-SURFACE-X | REGRESSION-INTRODUCED-AT-COMMIT/CUTOVER-Y`,
with the MECHANISM of the 7 fully-empty dates named (grounded per Rule 22 — source/graph citation
with vintage, not inference). Proof artifact per PRD §7 at
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_TRGALN/proof_TO-5.json` (claims = per-date
truth entries), regardless of owner — one proof home per project.

Downstream: TO-6 (surgical backfill, staged at AE) consumes the truth table and touches ONLY
MISSING dates. Roll-forward is fallback-only on Andrew's explicit word.

<acceptance_criteria>
1. Every hollow/empty date carries exactly one truth verdict with surface-level grounding.
2. The 7 fully-empty dates' mechanism named and source-cited (file:line @ commit or live read).
3. 08-05/cutover correlation tested and reported either way.
4. No fixes applied in this TO — truth only; fixes are TO-6's.
</acceptance_criteria>
</task_order>
