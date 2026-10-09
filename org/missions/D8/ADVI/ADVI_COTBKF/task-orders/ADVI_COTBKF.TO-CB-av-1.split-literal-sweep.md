# TO ADVI_COTBKF.TO-CB-av-1.split-literal-sweep -- round 48 CB-av-1: sweep the remaining split key literals onto the registry rows

<to_id>ADVI_COTBKF.TO-CB-av-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~75</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-av-1` (`decompositions/ADVI_COTBKF_DECOMP.round48.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-at-1

---

## WORKER FACE

### THE CELL

Round 45 removed the split key literals from `data/assets/scripts/silver/commonwealth_cot_price_rewrite.py`. Its two keys now come
from `lib/opal_naming.legacy_address()` rows in `infra/logic/registry/legacy_addresses.json`: `<own>-silver-prices-prefix`
(`silver/prices/`) and `<own>-code-gold-scopes-pin` (`code/gold/scopes.json`).

The same pattern remains at two sites (row ADVI_COTBKF-D2-W72-S1):
- `data/assets/scripts/silver/commonwealth_bd_txn_provenance.py`:37 (the `silver/prices` key);
- `data/cot/scripts/gold/build_canonical_prices_v2.py`:65 (`_SILVER = '/'.join(['silver', ''])`).

The :103 site in the provenance script is a regex fragment, not a key, and is out of scope.

**CTO ruling (ADDENDUM 20 @3a563d35b1).** Sweep both key sites onto the validated `legacy_addresses` rows. The cell's grep covers EVERY
COTBKF script and expects 0.

**Your item.** Code and tests only. No deploy, no S3 write.

1. **Replace the two sites** with keys from the existing rows via `legacy_address()`. If a needed key has no row, add it, validated by
   `python lib/opal_naming.py validate`. Never use parts or a bypass. The keys must be unchanged: print them before and after.
2. **Add the test** `data/assets/scripts/silver/tests/test_cotbkf_no_split_key_literals.py`. It ast-parses EVERY COTBKF script and
   expects 0 split key literals. Print the denominator of files scanned. The scripts are:
   - `data/assets/scripts/silver/commonwealth_*.py`;
   - `data/cot/scripts/gold/build_canonical_prices_v2.py`;
   - `data/cot/scripts/gold/B_00.canonical_holdings.py`.
   Use the same rule as round 45's `test_cot_price_rewrite_no_split_literals.py`: string concatenations or joins that form a path-like
   key, excluding regex fragments. Commit the test ALONE first; it must fail at the base, with the two sites.
3. **Both suites stay green:** `data/cot/scripts/gold/tests` and `data/assets/scripts/silver/tests`.

### ACCEPTANCE

<criterion id="CB48av1-AC1" cell_refs="CB-av-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_split_key_literals.py -q</invocation><expect>passed</expect></criterion>
`CB48av1-AC1` -- 0 split key literals across every COTBKF script. The test alone was committed first and failed at the base.

<expected_criteria>CB48av1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **START ONLY AFTER CB-at-1 has drained.** It edits the writer too. The issuer spawns you then. Base your worktree on that drain.
- **Code and tests only.** No S3 write and no deploy. The writer's redeploy is a later SERVED cell under its own pair.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W75-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_bd_txn_provenance.py
data/cot/scripts/gold/build_canonical_prices_v2.py
data/assets/scripts/silver/tests/test_cotbkf_no_split_key_literals.py
infra/logic/registry/legacy_addresses.json
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round48.md</decomp_doc> (round 48), cell `CB-av-1`.
<owned_cells>CB-av-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB48av1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~75/ADVI_COTBKF.TO-CB-av-1.split-literal-sweep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB48av1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pytest lines (the test with its file denominator, and both suites); the keys before and after; any row added; commits,
with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change; the writer's redeploy is a later SERVED cell.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first; the repo-wide grep with a printed denominator; the keys unchanged; no bypass by parts; BLIND: a COTBKF script outside the named globs (the denominator names what was scanned).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 20 @3a563d35b1 (msg 3565); row D2-W72-S1.
