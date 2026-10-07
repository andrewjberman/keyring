# TO MDPF_SECCLASS.TO-SC-e54 -- round 9 SC-e-54: the contract edits in one cell -- the sub-class bound for every class, 11 sectors, full industry-group names with a vendor decode table, and the sector writer reading it

<to_id>MDPF_SECCLASS.TO-SC-e54</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~36</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-54` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-12, FWD-17, FWD-11 | **depends_on:** none. Slot `~36`, first in its queue (then `TO-SC-e49`, `TO-SC-e50`, `TO-SC-e46`,
each of which reads this cell's contract).

---

## WORKER FACE

### THE CELL

`SC-e-54`: "The contract edits, one cell (2.5-2.7): every class's closed `sub_asset_class` list as the bound (cash included);
`gics_sector` adds Real Estate (11); `gics_industry_group` carries the full GICS names with a vendor-spelling decode table in the same
file; pin tests; the sector writer maps through the decode table (a spelling not in it leaves the field empty and is listed)"
(DECOMP_R9). The rulings, verbatim from `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`:
- **2.5 (W26-S6, cash):** "The contract's closed `sub_asset_class` list is the bound for every class, cash included. A DIRECT or AI
  verdict lands if it is a member of the contract's list, not only of the values the table happens to hold. The 15 old cash rows are
  re-planned under that bound."
- **2.6 (W24-S2, sectors):** "11, as GICS defines them: Real Estate is added to the contract's `gics_sector` values with its pinned
  test and the issuer's check."
- **2.7 (W24-S1, vendor spellings):** "The contract's closed industry-group list carries the full GICS names. The writer maps the
  vendor's 30-character spelling to the full name through a decode table declared in the same contract file. A spelling not in the
  table leaves the field empty, and the row is listed."

**The contract today** (`org/standards/MDPF_SECCLASS_CONTRACT.json`, version 0.5.0): `fields.gics_sector.values` holds 10 sectors (no
Real Estate); `fields.gics_industry_group.values` holds 23 vendor spellings, six cut at 30 characters (e.g. `Commercial & Professional
Serv`, `Health Care Equipment & Servic`, `Technology Hardware & Equipmen`); there is NO `sub_asset_class` field. The sector writer
`infra/aws/lambda/mdpf-secclass/sector-writer/lambda_function.py` (TO-SC-e28, built, not applied) reads the vendor spelling as-is.

**Build:**
1. **Contract** (one file, the version moves to 0.6.0):
   - `fields.gics_sector.values`: the 11 GICS sectors (the 10 plus `Real Estate`); keep its record keys, update `held_not_measured`.
   - `fields.gics_industry_group.values`: the 25 full GICS industry-group names (the issuer's check lists them); add
     `fields.gics_industry_group.vendor_decode`: an object mapping every one of 0.5.0's 23 vendor spellings (and any other spelling
     you measure in `s3://opal-data-etfs/bbg/*/characteristics.parquet`, read-only) to its full name.
   - `fields.sub_asset_class`: a new field with `values_by_class`, an object over exactly the six classes {cash, fixed_income,
     equity, structured, alternatives, commodities}, each a closed list of distinct strings. Ground each list in the live table's
     sub-classes per class (read-only scan) plus the cash sub-classes the contract needs (the table holds 0 cash rows today: name the
     source of each cash value). Give the field the same record keys the other fields carry (`serves`, `definition`, `rule24_record`).
   - ASCII only; keep the file's existing key order where it has one.
2. **Pin tests:** `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py` moves its version pin to 0.6.0 and pins the
   11 sectors (Real Estate among them).
3. **The sector writer:** map `GICS_INDUSTRY_GROUP_NAME` through `vendor_decode` (read from the contract file, never typed twice);
   a spelling not in the table leaves `gics_industry_group` empty and the row is listed in the run list with state `NO-DECODE`.
   Sector values outside the 11 stay `OUT-OF-LIST`. Tests in `infra/aws/lambda/mdpf-secclass/sector-writer/tests/test_decode_table.py`
   (pytest, DynamoDB and S3 stubbed): a truncated spelling writes the full name; an unknown spelling writes nothing and is listed;
   Real Estate is admitted. The existing writer tests keep passing.
4. Row W24-S6 (the seed-wins dicts the writer reads do not exist yet) rides this cell only if the fix sits in the same function you
   edit; otherwise leave it and say so.

### ACCEPTANCE

<criterion id="SC9-e54-AC1" cell_refs="SC-e-54"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/issuer_check_sc_e54.py</invocation><expect>SC-E54-CONTRACT ok=True</expect></criterion>
`SC9-e54-AC1` -- the contract carries the 11 sectors, the 25 full industry-group names with a decode table over every measured
spelling, and a closed sub-class list for each of the six classes.

<criterion id="SC9-e54-AC2" cell_refs="SC-e-54"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e54-AC2` -- the contract's pin tests pass at the new version.

<criterion id="SC9-e54-AC3" cell_refs="SC-e-54"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/mdpf-secclass/sector-writer/tests/test_decode_table.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e54-AC3` -- the decode-table tests pass (a truncated spelling writes the full name; an unknown one writes nothing and is listed; Real Estate admitted). The writer's existing tests are the issuer's drain check.

<expected_criteria>SC9-e54-AC1,SC9-e54-AC2,SC9-e54-AC3</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`contract_version 0.5.0 not above 0.5.0`); AC2 PASS as expected (control: 21
passed at 0.5.0; it fails once the version moves unless the pin moves with it); AC3 FAIL as expected (`PYTEST-BAD rc=4`: no
`tests/test_decode_table.py`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- The R10/R11 issuer checks are READ-ONLY to you.
- **No apply, no deploy, no upload, no table write, no model call.** The sector writer is not applied in this cell; its apply is a
  laptop cloud-operations seat's act through `safe-apply`.
- **No package install and no download of any kind**, including a Terraform provider (row S49).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W36-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/standards/MDPF_SECCLASS_CONTRACT.json
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py
infra/aws/lambda/mdpf-secclass/sector-writer/lambda_function.py
infra/aws/lambda/mdpf-secclass/sector-writer/tests/
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-54`.
<owned_cells>SC-e-54</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e54-AC1, SC9-e54-AC2, SC9-e54-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~36/MDPF_SECCLASS.TO-SC-e54.contract-edits-bound-sectors-decode.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e54-AC1,SC9-e54-AC2,SC9-e54-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the new version, each class's sub-class list and its source, every decode pair, any spelling measured outside 0.5.0's 23,
the decode tests by name, W24-S6 ridden or not, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell edits a contract, its pin test and a built-not-applied writer; no schedule moves.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes; the writer's declared role (TO-SC-e28) is unchanged.
comp-adversary: RUN -- contract 0.5.0 read (10 sectors, 23 vendor spellings, no sub_asset_class field); the issuer's check pins 11 sectors, 25 groups and the decode coverage (positive control on a synthetic contract: ok; dropping one sector: refused). BLIND: whether the vendor emits spellings beyond the 23 (the worker measures); the cash sub-class source (the table holds 0 cash rows).
lane: the <paths> block IS the grant. None of these files is a shipped lib/_shared member.
</preflight>

Source: PRD v0.13 @90f99888cd; analysis rulings 2.5-2.7 @1ca9e97fc9; DECOMP_R9 @5d70aab6c9; TO-SC-e27, TO-SC-e28 (round 8).
