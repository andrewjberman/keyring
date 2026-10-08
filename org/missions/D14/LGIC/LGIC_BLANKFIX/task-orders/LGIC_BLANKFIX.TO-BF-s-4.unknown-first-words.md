# TO LGIC_BLANKFIX.TO-BF-s-4 -- round 5 BF-s-4: first-segment words the canon does not hold -- a real path is ruled, a pattern is printed as a pattern

<to_id>LGIC_BLANKFIX.TO-BF-s-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-2, FWD-8 |
**depends_on:** BF-s-1 merged; the registry rulings landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Two roots read with no hole and were graded by a seat that built none of the check (`bd-pipeline`, 142
names; `investor-reporting/directory`, 18). The run over all 13 roots the root map covers reads 412 names and 38 holes on 9
roots: the table is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_MAPPED_ROOTS_round4.txt` and each root's whole output is under
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round4/`. The CTO's reading is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`), `opal_naming_scope.py`, `opal_naming_rootmap.py`,
`opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`, the `crossfirm` command),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`, the `lines` and `keys` commands). The
registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `event_rules.json`, `legacy_addresses.json`,
`resources.json`, `systems.json`); the map is `infra/logic/registry/root_map.json`. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no
AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed)
and every `lib/tests/test_opal_naming_*.py` script prints `ok=True`; none may fail after your build. A test you write asserts
relations and the rows it needs by name, never a typed total of repository names or registry rows: those move every day.

### THE CELL

`BF-s-4`. Four lines print `HOLE` because a word is in no vocabulary: stored-file prefixes `bbg/` (`investor-reporting/core`) and
`firms/` (`investor-reporting/export`), the group name `calculated-group` (`investor-reporting/performance`) and the secret
`astn/kimi/api-key` (`investor-reporting/ycharts`). For each the question is the CTO's: is it a real stored path, group or
secret, or a pattern in the code? A real one gets a registry ruling; a pattern is printed as a pattern and never as a name.

**THE RULINGS.** `4.0.0_SA_CRO` rules this class in the registry first. The files, the row shapes and the commits are named in AMENDMENT 1, written into this order before it is handed to you. If this order reaches you with no AMENDMENT 1, stop and report.

**Build** in `lib/opal_naming_rootcheck.py`, to what AMENDMENT 1 names for each of the four: a ruled name prints its answer; a
name the registry marks as a code pattern prints `PATTERN` with the registry's sentence; a name with neither keeps its `HOLE`.
Extend the test with one case per branch and the DIFFERENCE CONTROL for the pattern mark.

### ACCEPTANCE

<criterion id="BS4-AC1" cell_refs="BF-s-4"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BS4-AC1` -- a registry mark is what makes a line a pattern, and a ruling what makes it a name.

<criterion id="BS4-AC2" cell_refs="BF-s-4"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>unknown_word_holes=0</expect></criterion>
`BS4-AC2` -- over every mapped root no hole of this class remains.

<expected_criteria>BS4-AC1,BS4-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-4`.
<owned_cells>BF-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS4-AC1, BS4-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-s-4.unknown-first-words.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS4-AC1,BS4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the four lines before and now, whole; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a real stored path printed as a pattern to clear a hole (only the registry's mark does it; the difference control); a word added to a vocabulary by the worker (no registry file is in the grant); BLIND: the same words on unmapped roots.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS4-AC1 base PASS as expected (same test; extended by the cell); BS4-AC2 base FAIL as expected (ran: no such command).
