# TO MDPF_SECCLASS.TO-SC-e57 -- round 9 SC-e-57: S28: the FWD-10 planner stops writing a GICS sector into sub_asset_class; a resolved sector lands only in gics_sector

<to_id>MDPF_SECCLASS.TO-SC-e57</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~38</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-57` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-10, FWD-12 | **depends_on:** none (slot ~38 queue: after TO-SC-e55)

---

## WORKER FACE

### THE CELL

`SC-e-57`. Round-8 analysis section 3, S28: "the producer stops writing a GICS sector into `sub_asset_class`. Sector lands only in
`gics_sector` (FWD-12). An existing row is not rewritten before FWD-12's writer runs."

**Measured:** `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py` `classify_canonical_row()` ~:172-181 sets
`planned["sub_asset_class"] = sector` when `gics_status == "RESOLVED"` and the sector is in `GICS_SECTORS`; otherwise a non-US listing
takes its `COUNTRY_REGION` value; otherwise `low_confidence`. Contract 0.5.0 declares `gics_sector` (closed values; SC-e-54 adds Real
Estate this round).

**Build:** a resolved sector goes to `planned["gics_sector"]` only; `sub_asset_class` comes from the country-region rule or is absent
with `low_confidence: True`; `input` keeps naming what set the sub-class. The FWD-10 producer
(`infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py`) writes put-on-absence only, so existing rows are not
rewritten: confirm that from its code and say so; edit it ONLY if it writes the field itself. Tests in
`infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py` updated for the new rule.

### ACCEPTANCE

<criterion id="SC9-e57-AC1" cell_refs="SC-e-57"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e57-AC1` -- the module's tests pass under the new rule (control at base: 23 passed under the old rule).

<criterion id="SC9-e57-AC2" cell_refs="SC-e-57"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/sc_e57_no_sector_in_subclass.py</invocation><expect>SC-E57 ok=True</expect></criterion>
`SC9-e57-AC2` -- no planned sub_asset_class is a GICS sector; resolved sectors land in gics_sector; the region rule still applies.

<expected_criteria>SC9-e57-AC1,SC9-e57-AC2</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e57-AC1 PASS at base as a control (23 passed, old rule; the worker's test edits make it the build check); SC9-e57-AC2 FAIL as expected (`us_sub=Information Technology`, `us_gics=None`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- No deploy, no Lambda rebuild, no table write: the deployed producer takes the module at its next build, an issuer act.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W38-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py
infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py
infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-57`.
<owned_cells>SC-e-57</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e57-AC1, SC9-e57-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~38/MDPF_SECCLASS.TO-SC-e57.fwd10-sector-out-of-subclass.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e57-AC1,SC9-e57-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the rule before and after, whether the producer writes the field itself, AC1/AC2 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the module change schedules nothing; the producer's schedule is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes.
comp-adversary: RUN -- S28 and CTO batch 268's held swap (HDB, RYAAY); put-on-absence (existing rows untouched); BLIND: other importers of the module (the worker lists them).
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.
