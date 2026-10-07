# TO MDPF_SECCLASS.TO-SC-e27 -- round 8 SC-e-27: FWD-12, FWD-17 -- the contract's next version: the two C-SECTOR attributes and the new key form

<to_id>MDPF_SECCLASS.TO-SC-e27</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~24</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-27` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-12, FWD-17 | **depends_on:** MDPF_SECCLASS.TO-SC-e25 AND MDPF_SECCLASS.TO-SC-e26 -- starts only after BOTH
drain. Slot ~24's second order.

---

## WORKER FACE

### THE CELL

`SC-e-27`: the contract's next version. This cell is the ONE writer of `org/standards/MDPF_SECCLASS_CONTRACT.json` this round. It
declares the two C-SECTOR attributes with their closed values, the new key form for a security with neither ticker nor CUSIP, and
moves the pin test to the new version.

Contract notes (PRD v0.12 ADDENDUM v0.5, v0.7, v0.10):
- **C-SECTOR:** one NEW attribute for the sector and one NEW attribute for the industry group on `etf-classifications`, names and
  closed values declared as data in the contract with the four-postulate record (`rule24_record`) and a token census. NOT the
  legacy `sector` attribute (179 seed rows of another grain; keeps its bytes); `sub_asset_class` is not rewritten.
- **C-NOCHAR:** labels only; no measurement enters the table.
- **Key form:** declared before any row with no ticker and no CUSIP is written.

**Inputs (the deliverables of the two orders this one depends on; read the NEWEST of each):**
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SECTOR_INDUSTRY_GROUP_VALUES_<YYYYMMDD>.json` and
  `.../C_SECTOR_FOUR_POSTULATE_RECORD_<YYYYMMDD>.md` (from `TO-SC-e25`): the proposed names, the measured value sets
  (`sources.characteristics.sector_values` and `.industry_group_values`), the four postulates.
- `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/KEY_FORM_PROPOSAL_<YYYYMMDD>.md` (from `TO-SC-e26`): the one
  `PROPOSED KEY FORM:` line and its record.

**The contract at the cut (measured 2026-10-07):** `contract_version` `0.4.0`; top-level keys `_what, contract_version, project,
prd, fields`; seven fields: `instrument_kind, identifier_namespace, classified_by, classification_confidence, low_confidence,
security_bloomberg, listing_country`. `identifier_namespace` values: `BLOOMBERG, CUSIP, TICKER`.

**The pin test is RED at the cut** (measured 2026-10-07): `python -m pytest -q
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py` -> 2 failed, 15 passed:
`test_contract_version_is_exactly_the_pinned_one` (`PINNED_CONTRACT_VERSION = "0.3.0"` at line 60 against 0.4.0) and
`test_contract_lists_identifier_namespace_with_ticker_and_cusip` (expects `['CUSIP', 'TICKER']`, the contract has BLOOMBERG too).
Move the pin to your new version and the namespace assertion to the contract's real value set, which now includes the new key
form if you add it to `identifier_namespace`. Add tests that pin the two new fields' value sets exactly.
NOT yours: `infra/aws/lambda/v2_portal/_shared/tests/test_model_classifier.py:245-248` also pins `0.3.0` and is red at the cut; it
belongs to cell `SC-e-31`. Do not edit it; name it in your report.

**Build:**
1. Edit `org/standards/MDPF_SECCLASS_CONTRACT.json`: bump `contract_version` (0.5.0 unless a reason is stated); add the two new
   fields, each with `values` (closed list, exactly the measured set), `definitions` or a definition line, the absent/null
   reading, its source (`GICS_SECTOR_NAME` / `GICS_INDUSTRY_GROUP_NAME` of the Bloomberg characteristics file) and its
   `rule24_record` (from SC-e-25's record); declare the new key form (in `identifier_namespace` or its own block, your call,
   stated) with its rule24 record. Keep every 0.4.0 field byte-for-byte unless a change is required and stated.
2. Edit `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`: the pin and the namespace test as above, plus the
   new pinned value-set tests.
3. ASCII only. No reader or writer code changes in this cell.

### ACCEPTANCE

<criterion id="SC8-e27-AC1" cell_refs="SC-e-27"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC8-e27-AC1` -- the pin test passes at the new version, with the new fields' value sets pinned.

<criterion id="SC8-e27-AC2" cell_refs="SC-e-27"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e27.py</invocation><expect>SC-E27-CONTRACT ok=True</expect></criterion>
`SC8-e27-AC2` -- the contract declares exactly two new fields whose values equal SC-e-25's measured sets, carries SC-e-26's key form verbatim, and keeps the seven 0.4.0 fields.

<expected_criteria>SC8-e27-AC1,SC8-e27-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=1 2 failed, 15 passed`); AC2 FAIL as expected
(`contract_version 0.4.0 not above 0.4.0`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`,
  uncommitted. The R10 issuer checks are READ-ONLY to you.
- **No table write, no deploy.** Declaring a field does not populate it (R8 rule 24 (iv)).
- **Refusal clause.** If a criterion cannot be met as written (for example SC-e-25's measured set is unusable as a closed list),
  stop, write the reason in your report and a surprise row (id `MDPF_SECCLASS-W24-S<k>`), and do not weaken the test.

<paths>
org/standards/MDPF_SECCLASS_CONTRACT.json
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-27`.
<owned_cells>SC-e-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e27-AC1, SC8-e27-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~24/MDPF_SECCLASS.TO-SC-e27.contract-next-version.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e27-AC1,SC8-e27-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the new version, the two field names and value counts, the key form and where it is declared, every other pin test
the version move turns red (by file), commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): no gate names the contract file. A contract edit arms nothing.
comp-iam: RUN -- R8 battery; not applicable to a contract file.
comp-adversary: RUN -- R8 battery; issuer reads 2026-10-07: contract 0.4.0 seven fields; test_classified_by_v2.py red at base (pin 0.3.0 at :60; namespace at :100-102); test_model_classifier.py:245-248 also pins 0.3.0 (SC-e-31's file). BLIND: the readers of contract_version beyond these (git grep at the cut names 18 .py files that read the contract file; none other pins the version).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 @87ad6d2e4c (ADDENDUM v0.5, v0.7, v0.10); DECOMP_R8 @495efa3c32.
