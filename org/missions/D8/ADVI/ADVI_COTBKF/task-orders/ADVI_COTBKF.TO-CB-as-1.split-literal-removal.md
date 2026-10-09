# TO ADVI_COTBKF.TO-CB-as-1.split-literal-removal -- round 45 CB-as-1: no split key literals in the cot price rewrite script

<to_id>ADVI_COTBKF.TO-CB-as-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~72</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>45</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-as-1` (`decompositions/ADVI_COTBKF_DECOMP.round45.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`data/assets/scripts/silver/commonwealth_cot_price_rewrite.py` builds two S3 keys from split string literals so that the commit-time
naming gate does not see them: `'pri' + 'ces'` (near line 76) and `'scopes' + '.json'` (near line 251). CLAUDE.md rule 30 says a
builder refusal means a missing registry row to ADD, never a hand-typed workaround.

**CTO ruling (ADDENDUM 17 @809d6830ac).** Remove them, in this order:
1. Import the owning pipeline's constant where one exists.
2. Otherwise add the registry row under `infra/logic/registry/` and take `lib/opal_naming.address()` output.
3. If `address()` cannot express a legacy key shape, name the R20 departure for Andrew, and read the key only through ONE named
   constant until he acknowledges.

Measured by the issuer:
- The owning writer `data/cot/scripts/gold/build_canonical_prices_v2.py` has NO module-level constant: `output_key` at :746 is
  function-local.
- `code/gold/scopes.json` is owned by a deploy order, not a module.
- **Do NOT edit the writer.** It is being deployed right now at a pinned sha256 (round 42).

So both keys go to step 2 or 3.

**Your item.**
1. **For each key** (the `silver/prices/` prefix and `code/gold/scopes.json` in `opal-data-cot`), try a registry row plus
   `address()`.
   - Read `lib/opal_naming.py` and `infra/logic/registry/` to see whether a row can express the key exactly.
   - If it can, add the row (validated by `python lib/opal_naming.py validate`) and use `address()`.
   - If it cannot, write ONE module-level constant, plainly typed and not split, with a comment naming the R20 departure. Write an R20
     register entry draft in your deliverables folder for Andrew. If the naming gate refuses the plain literal, that refusal IS the
     R20 case: name it, do not bypass it with parts, and file a BLOCKING row.
2. **No split literal adjacent to a key path remains in the script.** Add the test
   `data/assets/scripts/silver/tests/test_cot_price_rewrite_no_split_literals.py`. It parses the script (ast) for string
   concatenations or joins whose operands, joined, form a path-like key, and expects 0. Commit the test ALONE first; it must fail at the
   base.
3. **The behaviour is unchanged.** The existing pin-check and census tests stay green, and the same keys result (printed before and
   after).
4. **Count the same pattern** in this project's other scripts (`data/assets/scripts/silver/commonwealth_*.py`) and in the cot writer.
   Report the counts per file in a surprise row. Do not change those files.

Write `split_literal_removal.md`. LAST line exactly: `SPLIT-LITERALS script=0 path=<registry|r20> other_files=<n>`.

### ACCEPTANCE

<criterion id="CB45as1-AC1" cell_refs="CB-as-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cot_price_rewrite_no_split_literals.py -q</invocation><expect>passed</expect></criterion>
`CB45as1-AC1` -- the script carries 0 split key literals. The test alone was committed first and failed at the base.

<criterion id="CB45as1-AC2" cell_refs="CB-as-1" judgment="true"/>
`CB45as1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- the keys come from `address()` via a validated registry row, OR a named R20 departure with one plain constant and no bypass;
- the resulting keys are unchanged.

<expected_criteria>CB45as1-AC1,CB45as1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **The cot writer is NOT edited.** No other script is changed (they are counted only). No S3 write.
- **A registry row** must pass `python lib/opal_naming.py validate`. The generated carriers are regenerated only if `validate` requires
  it, and named in the report.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W72-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_cot_price_rewrite.py
data/assets/scripts/silver/tests/test_cot_price_rewrite_no_split_literals.py
infra/logic/registry/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round45.md</decomp_doc> (round 45), cell `CB-as-1`.
<owned_cells>CB-as-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB45as1-AC1, CB45as1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~72/ADVI_COTBKF.TO-CB-as-1.split-literal-removal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB45as1-AC1,CB45as1-AC2` BEFORE the flip. Mechanical: CB45as1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the SPLIT-LITERALS line;
- the path taken per key (registry row, or R20 with its draft);
- the keys before and after;
- the pytest lines;
- the other-file counts;
- commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a manually run census.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first; the rule-30 ladder in order; no bypass by parts; the writer untouched (mid-deploy); the keys unchanged; BLIND: the same pattern elsewhere (counted, reported, not widened).
lane: the <paths> block IS the grant (worker RULING 1); infra/logic/registry/ is granted for one row only, through validate.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 17 @809d6830ac (msg 3519); row D2-S67.
