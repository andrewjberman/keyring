# TO MDPF_SECCLASS.TO-SC-t2 -- thread hop 2: the BD assets dimension takes class and sub-class from the canonical row

<to_id>MDPF_SECCLASS.TO-SC-t2</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~3</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-t-2` (`decompositions/MDPF_SECCLASS_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** SC-t-1

---

## WORKER FACE

### THE CELL

`SC-t-2`, thread hop 2 (PRD section 2): "BD classifier library -> BD silver assets dimension
(`data/black_diamond/scripts/silver/build_bd_assets_dim.py:154`) takes class and sub-class from the canonical row."
Your previous order (SC-t-1) moved `data/black_diamond/scripts/gold/lib/etf_classifier.py` onto `etf-classifications`,
with no fold, no guesses, and unknown for a ticker the table lacks. Build on your branch's library.

`build_bd_assets_dim.py` `apply_blend` (~:152) consults `ETFClassifier.instance()` only for COARSE BD super-class values
(`COARSE_SUPER_CLASSES`), printing a scan of bd-securities, and keeps BD's own super class otherwise.

**Build (LOCAL build + record: no upload, no deploy):**
1. Every asset's class and sub-class comes from its canonical row through the library, not only for coarse BD values.
   A BD super class never overrides a canonical row. An asset with no row is unclassified by name, and the dimension
   carries a `class_source` column (`etf-classifications`, or `unclassified`) so a reader can tell which applies. Keep
   the dimension's existing columns and add only what this needs.
2. The stale print that names a bd-securities scan goes.
3. **Tests** in `data/black_diamond/scripts/silver/tests/test_assets_dim_canonical.py`, on a stubbed library:
   - a canonical row overrides a BD super class;
   - an unknown ticker is unclassified with `class_source = unclassified`;
   - GLD, PHYS and VXX carry their canonical classes.
4. **Census** from a REAL local build of the assets dimension on the latest BD day, written to
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_SILVER_CENSUS_20260929.json` as
   `{"as_of", "artifacts": [the dimension's local path], "rows", "class_sources": {source: count}, "unclassified",
   "unclassified_names": [...], "moved_vs_current": n}`.

### ACCEPTANCE

<criterion id="SC1-t2-AC1" cell_refs="SC-t-2"><invocation>python -m pytest data/black_diamond/scripts/silver/tests/test_assets_dim_canonical.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC1-t2-AC1` -- the canonical row decides, and an unknown is unclassified by name.

<criterion id="SC1-t2-AC2" cell_refs="SC-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_bd_build_census.py silver</invocation><expect>BUILD-CENSUS</expect></criterion>
`SC1-t2-AC2` -- a real local build where every class came from the canonical table.

<expected_criteria>SC1-t2-AC1,SC1-t2-AC2</expected_criteria>

Dry-run at the base 2026-09-29 22:0xZ: AC1 "no tests ran", AC2 NOT-CENSUSED (census absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** Reads `opal-data-bd`; no upload, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W3-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/silver/build_bd_assets_dim.py
data/black_diamond/scripts/silver/tests/test_assets_dim_canonical.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_SILVER_CENSUS_20260929.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP.md</decomp_doc> (round 1), cell `SC-t-2`.
<owned_cells>SC-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC1-t2-AC1, SC1-t2-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~3/MDPF_SECCLASS.TO-SC-t2.bd-assets-dim-canonical.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC1-t2-AC1,SC1-t2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the dimension's change, the census (rows, class sources, unclassified, moved), the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the silver schedule is unchanged.
comp-iam: RUN -- the silver build's principal reads etf-classifications through the library; the grant is drafted once, in SC-t-3's half.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; decomposition findings inlined (apply_blend coarse-only consult).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 2 (S04).
