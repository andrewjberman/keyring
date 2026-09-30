# TO MDPF_SECCLASS.TO-SC-e2 -- round 2 SC-e-2: instrument-kind-population

<to_id>MDPF_SECCLASS.TO-SC-e2</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~5</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-2` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-8 | **depends_on:** SC-e-1 (same seeder file)

---

## WORKER FACE

### THE CELL

`SC-e-2`, analysis item E2 (row W2-S3). `instrument_kind` is absent on 2,163 of 2,309 rows (fund 135, single_security 11).
The seed and constituent default runs skip existing rows, and the scheduled rows were written without it (no
Schwab/GICS input wired). This runs after SC-e-1 in your worktree. Build on its seeder change.

**Build (LOCAL build + record: no table write):**
1. **Name the input source first.** Find, among inputs the estate already holds, what can say fund vs single security
   per ticker: the Schwab security master, Bloomberg security type fields, the ETF constituents feed, or other. Name
   it, with its path and coverage. If the only candidate for a row is bd-securities, that row's kind is a write into an
   EXISTING row from bd-securities, which is outside Andrew's word: count those rows separately
   (`from_bd_securities`) and leave them out of `rows`. No default and no guess.
2. **An instrument_kind-only update mode.** A new script, `infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py`,
   does one conditional update per row: `SET instrument_kind` on `attribute_not_exists(instrument_kind)`, touching no
   other attribute, with `--dry-run`. Where W2-S3 needs it, the constituents seeder gains a matching kind-only mode.
   Run in dry-run only.
   **Amendment 1 (row MDPF_SECCLASS-W5-S1):** round-1's `infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py`
   `test_constituent_seeder_never_sets_classified_by` pins the pre-contract rule. Under the CTO's four-label ruling and
   SC-e-1, the constituents seeder sets `classified_by = "constituents"`. Update that one test to assert the
   `constituents` label on a written row and the refusal of a seed or scheduled row. Loosen nothing else.
   **Note (row MDPF_SECCLASS-W5-S3):** the site-Z `--universe amgt-library` path is NOT on local CLOUD; it sits on
   origin/CLOUD pending 0.0.0_AB_MSTR's sync. Do not merge origin. That path's labelling follows after the sync.
3. **Tests** in `infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py`:
   - only `instrument_kind` changes;
   - a row that already has it is refused;
   - an unknown kind is left absent.
4. **Census and half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_KIND_CENSUS_20260930.json` as `{"table_rows_at_build", "source_named",
   "rows_absent_kind", "would_set", "defaulted": 0, "from_bd_securities", "rows": [{"ticker", "instrument_kind",
   "source"}]}`. Write the half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INSTRUMENT_KIND_20260930.md`.

**Standing rulings (carried from the round-2 decomposition):**
- Andrew-direct 2026-09-30 ~02:2xZ: "yes, bd-securities values can seed new rows. THey just don't overwrite existing rows."
  So a bd-securities value may seed a NEW row and never writes into an EXISTING one. A write to an existing row from a
  bd-securities value is outside his word: stop, and name it in the half for his decision.
- CTO C-WRITER ruling (analysis @151c890591, section 1): `classified_by` is `seed` / `scheduled` / `constituents` /
  `legacy`; `seed` always wins; `scheduled` and `constituents` write only where no row exists; a missing label reads as
  `legacy`.
- The live `etf-classifications` holds 2,309 rows (release step 2, ledger CLOSED @f13cddd058). Read and print its row
  count at build time as `table_rows_at_build` in your evidence file.

### ACCEPTANCE

<criterion id="SC2-e2-AC1" cell_refs="SC-e-2"><invocation>python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC2-e2-AC1` -- a kind-only conditional update, no default.

<criterion id="SC2-e2-AC2" cell_refs="SC-e-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py kind</invocation><expect>KIND-CENSUS</expect></criterion>
`SC2-e2-AC2` -- the source named, every planned row sourced, nothing defaulted.

<criterion id="SC2-e2-AC3" cell_refs="SC-e-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INSTRUMENT_KIND_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC2-e2-AC3` -- the kind write's half.

<expected_criteria>SC2-e2-AC1,SC2-e2-AC2,SC2-e2-AC3</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e2-AC1 no tests ran; SC2-e2-AC2 NOT-MET (evidence absent); SC2-e2-AC3 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W5-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py
infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py
infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_KIND_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INSTRUMENT_KIND_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-2`.
<owned_cells>SC-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e2-AC1, SC2-e2-AC2, SC2-e2-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~5/MDPF_SECCLASS.TO-SC-e2.instrument-kind-population.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e2-AC1,SC2-e2-AC2,SC2-e2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the source named and its coverage, would_set / from_bd_securities, the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E2), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E2; Andrew-direct 2026-09-30 ~02:2xZ.
