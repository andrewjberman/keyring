# TO ADVI_COTBKF.TO-CB-ax-1.cot-gold-failclosed -- round 50 CB-ax-1: cot B_00 and the writer run with no opal_naming and fail closed

<to_id>ADVI_COTBKF.TO-CB-ax-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~77</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>50</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ax-1` (`decompositions/ADVI_COTBKF_DECOMP.round50.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Two cot gold scripts run in production from the code mirror `s3://opal-data-cot/code/gold/`. The gold run syncs only that prefix
(`data/cot/scripts/gold/gold_dispatch.sh`:497-498).
- **`data/cot/scripts/gold/build_canonical_prices_v2.py` (the price writer):**
  - imports `from opal_naming import legacy_address, lookup` at module level (around :115);
  - builds its S3 keys at run time from `legacy_address()` rows (around :112-122).
- **`data/cot/scripts/gold/B_00.canonical_holdings.py`:** imports `opal_naming` inside `_ff_worker` (around :1362-1365), to read its
  own firm.

The mirror carries NO `opal_naming` and no naming schema. So from the mirror the writer fails at import, and B_00 fails the day
`schwab/silver/rps/` fills (row D2-S72).

Separately, round 46 turned the writer's `ticker_overrides` loading fail-OPEN: empty overrides plus a WARN (row D2-S71).

**CTO ruling (ADDENDA 21 and 22).**
- **Own firm:** both scripts resolve their OWN firm from the pinned `scopes.json` beside them, with NO `opal_naming` import at run
  time. If `scopes.json` is missing or lacks the firm, the run STOPS before any write.
- **Keys:** every key the code writes stays the legacy pipeline's own constant. No address is built at run time.
- **`ticker_overrides`:** missing or unreadable means STOP before any write. The empty default and the WARN path are deleted. It
  resolves beside the module first.

**Your item.** Code and tests only. No deploy, no S3 write.

1. **Writer.**
   - Remove the run-time `opal_naming` import.
   - Own firm: read it from `Path(__file__).parent / 'scopes.json'` with a minimal JSON reader of the fields it needs (as the existing
     `source_firm` resolver already does). Missing, or no own-firm row, means raise and STOP.
   - Keys: write each S3 key as ONE plainly typed module constant, never split. The round-48 test
     `data/assets/scripts/silver/tests/test_cotbkf_no_split_key_literals.py` must stay green. If the commit-time naming gate refuses a
     plain legacy key, STOP that branch: name the R20 case in a BLOCKING row, and never bypass it with parts.
   - `ticker_overrides`: restore fail-closed. Missing or unreadable means raise before any write.
2. **B_00 `_ff_worker`.** Remove the `opal_naming` import and the `../../../../data` tree computation. Read the own firm from the
   beside-module `scopes.json` the same way, and STOP if it is missing.
3. **Tests**, in `data/cot/scripts/gold/tests/test_cot_gold_failclosed.py`:
   - (a) the writer and B_00 copied ALONE with `scopes.json` and `ticker_overrides.py` into a temp dir, with NO `lib/` on the path,
     import and run: B_00's `_ff_worker` on a synthetic rps-filled day, with no ImportError;
   - (b) `scopes.json` absent means both STOP with a named error before any write (0 rows);
   - (c) `ticker_overrides.py` absent means the writer STOPS with a named error (0 rows);
   - (d) with the file present, 757 overrides and 1 correction load (the repo file's own counts; print them).
   Commit the test ALONE first; it must fail at the base. The existing gold and silver suites stay green.

### ACCEPTANCE

<criterion id="CB50ax1-AC1" cell_refs="CB-ax-1"><invocation>python -m pytest data/cot/scripts/gold/tests/test_cot_gold_failclosed.py -q</invocation><expect>passed</expect></criterion>
`CB50ax1-AC1` -- assertions (a)-(d) pass. The test alone was committed first and failed at the base.

<criterion id="CB50ax1-AC2" cell_refs="CB-ax-1" judgment="true"/>
`CB50ax1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- no run-time `opal_naming` in either script;
- every key a plain legacy constant with no split;
- fail-closed on both files;
- no change beyond these.

<expected_criteria>CB50ax1-AC1,CB50ax1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Code and tests only.** No S3 write and no deploy. Both suites stay green: `data/cot/scripts/gold/tests` and
  `data/assets/scripts/silver/tests`.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W77-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/cot/scripts/gold/build_canonical_prices_v2.py
data/cot/scripts/gold/B_00.canonical_holdings.py
data/cot/scripts/gold/tests/test_cot_gold_failclosed.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round50.md</decomp_doc> (round 50), cell `CB-ax-1`.
<owned_cells>CB-ax-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB50ax1-AC1, CB50ax1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~77/ADVI_COTBKF.TO-CB-ax-1.cot-gold-failclosed.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB50ax1-AC1,CB50ax1-AC2` BEFORE the flip. Mechanical: CB50ax1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the pytest lines (the new test and both suites); the keys as constants (before and after equal); the override counts;
the files that must ship beside the scripts; commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change; the redeploy is CB-ax-2 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first; scripts run copied ALONE (no lib/) to prove no run-time opal_naming; both fail-closed arms; keys unchanged and not split; BLIND: another module-level import the mirror lacks (the copied-alone run surfaces it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDA 21 and 22 (msgs 3597, 3620); rows D2-S71, D2-S72, W75-S1.
