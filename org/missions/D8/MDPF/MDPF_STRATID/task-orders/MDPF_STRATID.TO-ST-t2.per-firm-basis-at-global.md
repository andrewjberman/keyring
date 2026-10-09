# TO MDPF_STRATID.TO-ST-t2 -- round 1 ST-t-2: the SMA registry declares each strategy's basis at Global per firm
<to_id>MDPF_STRATID.TO-ST-t2</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~2</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `ST-t-2` (`decompositions/MDPF_STRATID_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`ST-t-2`. Whether a strategy's dollars are ADDED to Global or are already inside it depends on the FIRM the dollars come from, not
only on the strategy. Cottonwood's PFDE sleeve sits outside the Models and outside Global's population, so at Global it is ADDITIVE;
49financial's sleeves already sit inside Global's non-model dollars, so there they are CARVE-OUTS. The registry must say this, per
(strategy, firm), with a declared default per firm.

**The contract (PRD v0.3 C-BASIS, verbatim in substance):** the basis axis gains a firm dimension `(member, firm) -> carve_out |
additive`. The default is set per FIRM by where that firm's non-model dollars sit, declared once per firm: OUTSIDE Global's population
-> ADDITIVE; INSIDE -> CARVE-OUT; a firm with no declared population is NOT counted (its sleeves are listed elsewhere, not your cell). A
per-(member, firm) declaration overrides the firm default.

**Round-1 rows (issuer ruling R1/R2, exactly these):** firm population `49financial` = inside; `cottonwood` UNDECLARED this round;
`inflection` undeclared. One (member, firm) row: `("pfde", "cottonwood")` = additive. One scope row so the category tree accepts the
additive PFDE entry at Global: `SMA_BASIS_BY_SCOPE[("pfde", "global")]` = additive (the tree validates the by_model entry's basis against
`sma_basis_of(member, scope)`; measured 2026-10-08: without this row it refuses with "Two declarations of the same fact disagree").

**The estate, read at the base.** `data/mdpf/scripts/gold/mdpf_category_registry.py`: `SMA_BASIS_CARVE_OUT` / `SMA_BASIS_ADDITIVE` /
`SMA_BASIS_VALUES` (:337-339); `SMA_MEMBERS` (:343-369); `SMA_BASIS_VERIFIED` (:375); `SMA_BASIS_BY_SCOPE` (:385-387); the import-time
check `_check_sma_basis_declared` (:407-436) -- extend it, keep its "never default" stance; `sma_basis_of(member_id, scope)` (:439-447).

**Build:**
1. `SMA_FIRM_POPULATION = {"49financial": "inside"}` (values `inside` / `outside`; a firm absent = undeclared) and
   `SMA_BASIS_AT_GLOBAL_BY_FIRM = {("pfde", "cottonwood"): SMA_BASIS_ADDITIVE}`, each with a comment citing PRD v0.3 C-BASIS and the
   decomposition's R1.
2. `sma_global_basis_of(member_id, firm_id) -> "additive" | "carve_out" | None`: the (member, firm) row wins; else the firm default
   (`outside` -> additive, `inside` -> carve_out); else None (undeclared -> not counted). A non-SMA member -> None.
3. `SMA_BASIS_BY_SCOPE[("pfde", "global")] = SMA_BASIS_ADDITIVE`.
4. The import check refuses: a population value outside `inside`/`outside`; a (member, firm) row naming a non-member or an invalid basis.
5. Tests in NEW `data/mdpf/tests/stratid/test_stratid_basis.py` (own sys.path preamble to `data/mdpf/scripts/gold`, like
   `data/mdpf/tests/taxsma/test_taxsma_cot_global_fold.py`), these exact names: `test_pfde_cottonwood_is_additive_at_global`,
   `test_firm_population_inside_defaults_carve_out`, `test_undeclared_firm_population_is_not_counted`,
   `test_member_firm_row_overrides_firm_default`, `test_import_refuses_an_invalid_firm_row` (reload the module under a monkeypatched table),
   `test_global_scope_basis_of_pfde_is_additive`.

### ACCEPTANCE

<criterion id="ST1-t2-AC1" cell_refs="ST-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t2_tests.py</invocation><expect>T2-OK</expect></criterion>
`ST1-t2-AC1` -- the six named tests pass.

<criterion id="ST1-t2-AC2" cell_refs="ST-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R1_CHECKS/st_t2_regress.py</invocation><expect>T2-REGRESS-OK</expect></criterion>
`ST1-t2-AC2` -- the TaxSMA Cottonwood-into-Global fold tests (readers of `sma_basis_of`) still pass.

<expected_criteria>ST1-t2-AC1 ST1-t2-AC2</expected_criteria>

Run each invocation from the worktree root. At the base (2026-10-08 ~20:5xZ): AC1 `T2-BAD no file ...`; AC2 `T2-REGRESS-OK`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- No AWS call of any kind. Do not change any existing `SMA_MEMBERS` row, `SMA_BASIS_VERIFIED`, or the `("tax", "cottonwood")` scope row.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W2-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/gold/mdpf_category_registry.py
data/mdpf/tests/stratid/test_stratid_basis.py
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP.md</decomp_doc> (round 1, the thread), cell `ST-t-2`.
<owned_cells>ST-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: ST1-t2-AC1, ST1-t2-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~2/MDPF_STRATID.TO-ST-t2.per-firm-basis-at-global.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> ST1-t2-AC1 ST1-t2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: SERVED -- the registry is read by the served category tree; no figure moves until ST-t-3 adds a by_model entry carrying the row.
direct_act: false -- the class is SERVED.
</preflight>

Source: PRD v0.3 ENDPOINT FWD-1, C-BASIS; decomposition round 1 hop 2, rulings R1, R2.
