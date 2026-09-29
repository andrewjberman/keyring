# TO MDPF_SECCLASS.TO-SC-k2 -- instrument_kind (O8) and industry on every seed row

<to_id>MDPF_SECCLASS.TO-SC-k2</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~2</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-k-2` (`decompositions/MDPF_SECCLASS_DECOMP.md`) |
**outcome_ref:** FWD-8, FWD-3 | **depends_on:** IRPT_BCKEND IB-mr-251 drained (same seed source; spawned after it)

---

## WORKER FACE

### THE CELL

`SC-k-2`. FWD-8 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`): "The shared list says whether each
security is a fund or an individual stock". The field is `instrument_kind`, with the values and definitions in
`org/standards/MDPF_SECCLASS_CONTRACT.json` (`fund`, `single_security`). CTO 103036 adds `industry`: the GICS
industry-group name, a new etf-classifications field, filled from Bloomberg's GICS industry group as an input and
decoded through the one client's `resolve()` (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py:262`).

The table `etf-classifications` (344 rows) is written by the seed path from the seed source
`infra/aws/lambda/v2_portal/_shared/etf_classification.py`, via `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py`.
Its merge rule, `merge_item` at :72, has the module win where it knows a value. A second seeder,
`yang_pipeline/seed-etf-constituents.py`, writes the ETF-constituent stock rows (AAPL's live row reads
`updated_by 'seed-etf-constituents ...'` and sector as `sub_asset_class`). That is row MDPF_SECCLASS-S1.

**THE RULE THAT BINDS THIS CELL (Andrew-direct 2026-09-29, verbatim): "the canonical table should not be overwritten by
anything in bd-securities."** Neither seeder reads bd-securities, and nothing you add may read it.

**Build (LOCAL build + record: no seed run against the table, no deploy):**
1. **Seed source.** Give every row in `etf_classification.py` an `instrument_kind` and, where GICS knows it, an
   `industry`. GLD, PHYS and VXX are `fund`. Absent means absent: never default either field. Keep IB-mr-251's PHYS row
   exactly as it landed.
2. **Seed path.** `seed-etf-classifications.py` writes both fields and sets `classified_by = "seed"`. The
   constituents seeder writes `instrument_kind = single_security` for its stock rows, plus `industry`. Neither may
   change an existing row's `asset_class` or `sub_asset_class` except where the census lists it.
3. **Tests** in `infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py`:
   - every seed row's `instrument_kind` is a contract value;
   - GLD, PHYS and VXX read `fund`;
   - a constituent stock row reads `single_security`;
   - a row with no known industry carries no `industry` attribute;
   - no code path imports or reads bd-securities.
4. **Census.** Run both seeders with `--dry-run` against the LIVE table and write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_SEED_FIELDS_CENSUS_20260929.json` as
   `{"seed_rows", "live_rows", "kinds": {ticker: kind}, "class_changes": [{"ticker", "before", "after"}],
   "other_diffs": [{"ticker", "field", "live", "seed"}]}`.
   The seed-vs-live diff is PRD Part V's reproducibility read: live rows equal seed output, or the difference is listed.
5. **Half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_FIELDS_20260929.md`
   (`## The act`, `## Blast radius`, `Rollback per key`), for the seed run that writes both fields (and 251's PHYS row).
   It covers the readers of the table (Positioning's two surfaces, the IR Holdings producer after 251), every listed
   class change, and a rollback per key (the prior item, from the census).

### ACCEPTANCE

<criterion id="SC1-k2-AC1" cell_refs="SC-k-2"><invocation>python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC1-k2-AC1` -- both fields on the seed rows, contract values only, absent never defaulted, no bd-securities read.

<criterion id="SC1-k2-AC2" cell_refs="SC-k-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_seed_fields.py</invocation><expect>SEED-FIELDS</expect></criterion>
`SC1-k2-AC2` -- every seed row's kind, GLD/PHYS/VXX as fund, and the seed-vs-live diff listed.

<criterion id="SC1-k2-AC3" cell_refs="SC-k-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_FIELDS_20260929.md</invocation><expect>HALF-READY</expect></criterion>
`SC1-k2-AC3` -- the half for the seed run, for the issuer to sign and send.

<expected_criteria>SC1-k2-AC1,SC1-k2-AC2,SC1-k2-AC3</expected_criteria>

Dry-run at the base 2026-09-29 22:0xZ: AC1 "no tests ran", AC2 NOT-READY (census absent), AC3 NOT-READY -- FAIL as
expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** Seeders run with `--dry-run` only: no table write, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W2-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification.py
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py
infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_SEED_FIELDS_CENSUS_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_FIELDS_20260929.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP.md</decomp_doc> (round 1), cell `SC-k-2`.
<owned_cells>SC-k-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC1-k2-AC1, SC1-k2-AC2, SC1-k2-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~2/MDPF_SECCLASS.TO-SC-k2.seed-kind-and-industry.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC1-k2-AC1,SC1-k2-AC2,SC1-k2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the kind and industry counts, the rows with no industry, the constituents seeder's role (row S1), the census
(class changes, other diffs), the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the seed path is a run, not a schedule.
comp-iam: RUN -- the seed path runs with the operator's credentials (seed-etf-classifications.py writes via boto3 batch_writer); no role change is needed for the fields; unmeasured whether any reader's role limits attributes (none is known).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; decomposition findings inlined (two seeders, merge rule, 251's PHYS row).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-FIELD; CTO 103036, 103040; Andrew-direct 2026-09-29 ~21:4xZ; row MDPF_SECCLASS-S1.
