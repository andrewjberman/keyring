# TO ADVI_COTBKF.TO-CB-ar-1.stale-pin-census -- round 44 CB-ar-1: the source_firm census stops when the served registry pin is stale

<to_id>ADVI_COTBKF.TO-CB-ar-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~71</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ar-1` (`decompositions/ADVI_COTBKF_DECOMP.round44.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Cottonwood's price writer resolves `source_firm` from a PINNED copy of the registry, which is deployed beside it at
`s3://opal-data-cot/code/gold/scopes.json` (round 42; a copy of `infra/logic/registry/scopes.json` at blob 261c0cf8). When the repo's
`scopes.json` changes, the served pin is silently stale.

The census that grades Cottonwood's price rows for cross-firm breaches is
`python data/assets/scripts/silver/commonwealth_cot_price_rewrite.py --source-firm-only --out <dir>`. Its LAST line is
`SOURCE-FIRM-CENSUS ...`.

**Your item (CTO, CB-ap-2 CTO half @d92ed8390f).** In `--source-firm-only` mode, BEFORE the census:
1. Read the served object `opal-data-cot` `code/gold/scopes.json` (`get_object`) and compute its sha256.
2. Compute the sha256 of the repo file `infra/logic/registry/scopes.json`.
3. Print `PIN-CHECK served=<sha> repo=<sha> same=<True|False>`.
4. On a mismatch, or when the served pin is missing (404), STOP: print
   `SOURCE-FIRM-CENSUS refused reason=<stale_pin|missing_pin>` as the LAST line, exit non-zero, and run no census.
5. On a match, run the census unchanged.

Add a test, `data/assets/scripts/silver/tests/test_cot_price_rewrite_pin_check.py`. With S3 faked, it asserts: (a) same bytes -> the
census runs; (b) different bytes -> refused `stale_pin`, non-zero; (c) a missing pin -> refused `missing_pin`, non-zero. Commit the
test ALONE first; it must fail at the base.

### ACCEPTANCE

<criterion id="CB44ar1-AC1" cell_refs="CB-ar-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cot_price_rewrite_pin_check.py -q</invocation><expect>passed</expect></criterion>
`CB44ar1-AC1` -- the three assertions pass. The test alone was committed first and failed at the base.

<expected_criteria>CB44ar1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Code and test only.** No S3 write. A read of the one pin key is allowed. `data/assets/scripts/silver/tests/` stays green.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W71-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_cot_price_rewrite.py
data/assets/scripts/silver/tests/test_cot_price_rewrite_pin_check.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round44.md</decomp_doc> (round 44), cell `CB-ar-1`.
<owned_cells>CB-ar-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB44ar1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~71/ADVI_COTBKF.TO-CB-ar-1.stale-pin-census.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB44ar1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pytest lines (the test and the silver suite); the diff summary; commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a manually run census.
comp-iam: DECLARED-NOT-APPLICABLE one GetObject of the pin key under the dell2 identity.
comp-adversary: RUN -- the test alone first; a missing pin is refused, never passed; BLIND: a pin stale in a field the writer does not read (the check is whole-file sha256, so it still refuses -- conservative by design).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` CB-ap-2 CTO half @d92ed8390f (msg 3486).
