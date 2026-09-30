# TO MDPF_SECCLASS.TO-SC-e14 -- round 6 SC-e-14: the round's repairs -- the find_by CUSIP filter, the seed PRE-READ count, and S4's attribute_exists

<to_id>MDPF_SECCLASS.TO-SC-e14</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~11</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-14` (`decompositions/MDPF_SECCLASS_DECOMP_R6.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-14`. Three small repairs, batched. The live table `etf-classifications` now holds 348 rows keyed `CUSIP:<9>` with
`identifier_namespace = "CUSIP"` (written 2026-09-30 16:44Z). Two readers can see them and must not, and two update
scripts can create rows they should only update.

**(a) The `find_by_*` filter.** `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` has
`find_by_asset_class` and `find_by_sub_asset_class`, which query the two GSIs (both project ALL attributes). Filter out
every row whose `identifier_namespace` is `"CUSIP"` from both methods' results. The same file exists as two byte-identical
copies:
- `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py`
- `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py`
Apply the identical change to both copies so all three stay byte-identical. (Confirm both paths exist before editing; if
either path differs, find the real copy and say so in your report.)

**(b) The seed PRE-READ count.** `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` and
`seed-etf-constituents.py` scan the whole table and print a PRE-READ / existing-row count. Exclude `CUSIP:`-keyed rows
from that count and print the excluded number beside it. Do not change what either script writes.

**(c) S4.** `infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py:89` and `set-instrument-kind.py:96`
update with `ConditionExpression attribute_not_exists(<attr>)` only. An update on a ticker that has no row would create
a skeleton row. Add `attribute_exists(ticker)` to each condition (one clause each). Row: `MDPF_SECCLASS-S4`.

**Build (LOCAL build + record: no table write):**
1. Make changes (a), (b) and (c).
2. Tests:
   - `infra/aws/lambda/v2_portal/_shared/tests/test_find_by_cusip_filter.py`: with DynamoDB stubbed, a
     `identifier_namespace = "CUSIP"` row is filtered from both `find_by_*` methods; a ticker row is not.
   - `infra/aws/lambda/v2_portal/yang_pipeline/tests/test_update_requires_existing_row.py`: with DynamoDB stubbed, each
     update script's condition refuses an update on an absent key and still lands an update on a present key whose
     attribute is absent.
3. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_client_copies_identical.py`: sha256 of the
   one client and its two copies; prints `COPIES-IDENTICAL 3 of 3 <sha>` when all match, and each path's hash otherwise.
4. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_seed_preread_count.py`: runs both seed scripts
   with `--dry-run` against the LIVE table (read only) and prints `SEED-PREREAD seed=<n> excluded_cusip=<n>
   constituents=<n> excluded_cusip=<n>` from their own output.

### ACCEPTANCE

<criterion id="SC6-e14-AC1" cell_refs="SC-e-14"><invocation>python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_find_by_cusip_filter.py infra/aws/lambda/v2_portal/yang_pipeline/tests/test_update_requires_existing_row.py infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC6-e14-AC1` -- the filter and the update-condition tests pass.

<criterion id="SC6-e14-AC2" cell_refs="SC-e-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_client_copies_identical.py</invocation><expect>COPIES-IDENTICAL 3 of 3</expect></criterion>
`SC6-e14-AC2` -- the one client and its two copies stay byte-identical.

<criterion id="SC6-e14-AC3" cell_refs="SC-e-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_seed_preread_count.py</invocation><expect>SEED-PREREAD</expect></criterion>
`SC6-e14-AC3` -- both seed dry-runs print a PRE-READ count excluding the `CUSIP:` rows, with the excluded count.

<expected_criteria>SC6-e14-AC1,SC6-e14-AC2,SC6-e14-AC3</expected_criteria>

Dry-run at the base 2026-09-30 19:3xZ: AC1 no such test files (FAIL as expected); AC2 no such check (FAIL as expected);
AC3 no such check (FAIL as expected).

**Import note (1.0.0_SA_CTO DECISION 103371):** this cell changes no import in a runner-deployed script, so the
deployed-layout import criterion does not apply.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write, no Lambda deploy. The seed scripts run in `--dry-run` only.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W11-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/etf_classifications_dynamodb.py
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/etf_classifications_dynamodb.py
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py
infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py
infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py
infra/aws/lambda/v2_portal/_shared/tests/test_find_by_cusip_filter.py
infra/aws/lambda/v2_portal/yang_pipeline/tests/test_update_requires_existing_row.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_client_copies_identical.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_seed_preread_count.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py
infra/aws/lambda/v2_portal/_shared/tests/test_set_instrument_kind.py
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R6.md</decomp_doc> (round 6), cell `SC-e-14`.
<owned_cells>SC-e-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC6-e14-AC1, SC6-e14-AC2, SC6-e14-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~11/MDPF_SECCLASS.TO-SC-e14.round6-repairs-cusip-guards-and-s4.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC6-e14-AC1,SC6-e14-AC2,SC6-e14-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** each diff, the test line, the three hashes, both seed PRE-READ lines verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- no new call; the filter and the conditions change what existing calls return or refuse.
comp-adversary: RUN -- 1 act read (CUSIP_ROWS ledger CLOSED @8b03d64dcc, 348 CUSIP rows live), 1 half read (CUSIP_ROWS CTO half condition 5), 1 remediation read (REMEDIATION_v3 S4); BLIND: whether any caller of find_by_* has landed since the census (the census read 0; condition 5 forbids one landing before this filter).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO rounds 4-5 analysis @533bcae124 section 4 items 2 and 3; CUSIP_ROWS CTO half @1f4792c45a condition 5;
REMEDIATION_v3 MDPF_SECCLASS-S4.

## AMENDMENT 1 (2.0.0_SA_COO~M, 2026-09-30 ~20:4xZ) -- grant the two older tests the S4 change breaks

Ruling on row `MDPF_SECCLASS-W11-S1` (the issuer rules inside its own decomposition). The S4 condition
`attribute_exists(ticker) AND attribute_not_exists(<attr>)` breaks four assertions that pin the old condition string, in
`infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py` and `test_set_instrument_kind.py`. Two more assertions
in `test_classified_by_v2.py` already fail on CLOUD because round 4 (SC-e-10) moved the contract to 0.3.0 and they still
pin 0.2.0 and four `classified_by` values. Both files are now in `<paths>`.

- Update the four S4 assertions to the new condition string. They must still prove what they proved: only the named
  attribute changes, and an already-set row is refused.
- Update the two contract assertions to the contract at HEAD: version 0.3.0, five `classified_by` values including `model`.
  Read the contract file for the values; do not type them from this text.
- No assertion is weakened or deleted. AC1 now runs the two files beside your two new ones; its expectation is unchanged.
- `test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged` fails on CLOUD's unmodified script. It is NOT
  granted: record it in row W11-S1 as pre-existing, with the failing line, and leave it.
- Re-run all three criteria, re-validate the proof (VALID rc=0), flip `<status>` back to complete, and commit.

Gate limb: none graded this modification (a modification of an existing order; `.tools/to-pipeline-gate.py` LIMB 6 fires on
new orders only, and this order declares no placeholders).
