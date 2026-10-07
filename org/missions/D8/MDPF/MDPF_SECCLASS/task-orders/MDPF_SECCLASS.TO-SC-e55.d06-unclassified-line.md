# TO MDPF_SECCLASS.TO-SC-e55 -- round 9 SC-e-55: C-S13: 49 Financial's firm mix serves its residual as its own Unclassified line, so the top-level mix sums to 1.0

<to_id>MDPF_SECCLASS.TO-SC-e55</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~38</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-55` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-2, FWD-13 | **depends_on:** none (slot ~38 queue: this order, then TO-SC-e57, then TO-SC-e56)

---

## WORKER FACE

### THE CELL

`SC-e-55`. Round-8 analysis section 3, C-S13 (REMEDIATION_v6): "the residual is served as its own line, 'Unclassified', so the
top-level mix sums to 1.0. That matches FWD-13's rule that a security the list does not hold is shown as unclassified. Owner
`2.0.0_SA_COO~M1`; a served move under its own pair."

**Measured by 3.0.0_SA_CVO (C-S13):** the served `s3://opal-data-bd/platinum/firm/mix_summary.json` (2026-10-07T05:49Z, as-of
2026-10-05): sum(mix.pct) = 0.9967614; sum(mix.market_value) = 2,001,258,931.56 against `mix_periods[2026-Q4].total_aua` =
2,007,761,226.11 (about $6.5M in no class).

**The producer:** `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py`. Its top-level `mix` deliberately omits `unclassified`
("top-level mix is 3-class per the frozen shape (census-refusal-confirmed); unclassified rides the period rows + composition bucket",
~:158-163), while `composition.unclassified` carries the residual. Its SUM-IDENTITY guard (classes + unclassified == total) stays.

**Build:**
1. `mix` carries a fourth key `unclassified` (market_value, pct) equal to the residual the emitter already computes. If a shape census
   (`--census`) refuses the new key, the census file that freezes the shape is part of the change: name it in your report and in a
   row, and do NOT edit any file outside `<paths>` (stop on that criterion instead).
2. A test `data/assets/scripts/gold/runners_49f/tests/test_d06_unclassified_line.py`: on a fixture with an unclassified position the
   four pcts sum to 1.0 and the four market values to the total.
3. A LOCAL run of the emitter against the live canonical inputs with
   `--out org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D06_MIX_DRY_RUN_20261007.json`, never uploaded (the inputs are opal-data-bd; read the a07 and b01 paths from the emitter's
   own CLI and its runner).
4. The half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md`: the act (the served
   `platinum/firm/mix_summary.json` gains the line at the next scheduled run after the code ships), its blast radius (every reader of
   that key: list them), both branches, rollback per key, both halves UNSIGNED.

**Shipped file:** `data/assets/scripts/gold/` is a shared home the pre-push deploy gate ships (`.tools/safe_deploy_core.py`
`shared_repo_homes`): your branch stays OFF every pushed range until both halves sign.

### ACCEPTANCE

<criterion id="SC9-e55-AC1" cell_refs="SC-e-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/assets/scripts/gold/runners_49f/tests/test_d06_unclassified_line.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e55-AC1` -- the four-key mix sums to 1.0 on a fixture.

<criterion id="SC9-e55-AC2" cell_refs="SC-e-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/d06_mix_sum_check.py</invocation><expect>D06-MIX-SUM ok=True</expect></criterion>
`SC9-e55-AC2` -- the local run against live inputs: four keys, pct sum 1.0, market values equal total_aua, the new line equal to composition.unclassified.

<criterion id="SC9-e55-AC3" cell_refs="SC-e-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC9-e55-AC3` -- the half request carries the act, blast radius, both branches, rollback and two UNSIGNED halves.

<expected_criteria>SC9-e55-AC1,SC9-e55-AC2,SC9-e55-AC3</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e55-AC1 FAIL as expected (PYTEST-BAD rc=4, no test file); SC9-e55-AC2 FAIL as expected (no D06_MIX_DRY_RUN file); SC9-e55-AC3 FAIL as expected (NOT-READY: half absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- No upload, no deploy, no S3 write: the local run writes only the `--out` file.
- Never push: a shipped shared-home file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W38-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py
data/assets/scripts/gold/runners_49f/tests/test_d06_unclassified_line.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D06_MIX_DRY_RUN_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-55`.
<owned_cells>SC-e-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e55-AC1, SC9-e55-AC2, SC9-e55-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~38/MDPF_SECCLASS.TO-SC-e55.d06-unclassified-line.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e55-AC1,SC9-e55-AC2,SC9-e55-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the residual before and after, the dry-run line, every reader of the served key, the census file if one refused, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ); the emitter's schedule is read by the worker from its runner, unchanged by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no grant changes; the local run reads opal-data-bd with the box's existing read.
comp-adversary: RUN -- the frozen-shape census (a new key may be refused: stop, do not widen); the SUM-IDENTITY guard (kept); the served key's readers (listed in the half); BLIND: consumers outside the repo.
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.
