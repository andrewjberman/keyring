# TO LGIC_BLANKFIX.TO-BF-s-6 -- round 5 BF-s-6: the run over every root prints its denominator -- how many roots exist, how many the map covers, and each it does not

<to_id>LGIC_BLANKFIX.TO-BF-s-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none

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

`BF-s-6`. The run over every mapped root exists only as a worker's script in a deliverables folder, and it does not say how much
of the estate it leaves out. FWD-9 ("the check can be read as finished from one run anyone can repeat") cannot be graded on it.

**Build** in `lib/opal_naming_rootcheck.py` a command `python lib/opal_naming_rootcheck.py all --map PATH`:
1. The denominator first: every Terraform root (use `opal_naming_scope`'s own enumeration of roots; do not write a second one),
   how many the map covers, and EACH root it does not cover by name with its name count from the scope.
2. Then each mapped root, in sorted order: its `ROOTCHECK` last line and `COMPLETED` or `STOPPED` (a root whose run raises is
   printed with the exception text and counted, never dropped).
3. Then totals over the completed roots per kind, and the holes per CLASS. The class of a `HOLE` line is decided by ONE function
   in this module, `hole_class(line_type, detail) -> str`, with the values `carded`, `source_bucket`, `event_rule`,
   `unknown_word`, `other`: carded = the detail says a card skipped it and gave no name; source_bucket = a bucket on a root that
   serves more than one firm whose firm could not be filled; event_rule = an event rule whose token is not ruled; unknown_word =
   a word in no vocabulary or a first segment that is neither a source nor a tier; `other` = none of these (printed whole).
4. Last line `ALL-ROOTS ok=True roots_total=N mapped=N unmapped=N completed=N stopped=N items=N right=N fix=N not_asked=N
   pattern=N carded=N refused=N hole=N carded_class_holes=N source_bucket_holes=N event_rule_holes=N unknown_word_holes=N
   other_holes=N`; `ok=True` when `mapped + unmapped == roots_total`, `completed + stopped == mapped`, each completed root's
   counts sum to its `items`, and the five class counts sum to `hole`. `ok` does not depend on `hole`, `stopped` or `unmapped`.
   Exit 0 when `ok`, whatever the holes.
5. `lib/opal_naming.py` is NOT in your grant: the issuer adds the `census --all-roots` entry at the merge.

**Extend** `lib/tests/test_opal_naming_rootcheck.py`: `hole_class` on one real line of each class taken from the saved outputs
under `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round4/` (copy the line text into the test), the DIFFERENCE CONTROL (a line
that names no card is not `carded`), and on a small temporary map: a root the map leaves out is listed as unmapped, and a root
whose run is made to raise is `STOPPED` and counted.

### ACCEPTANCE

<criterion id="BS6-AC1" cell_refs="BF-s-6"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BS6-AC1` -- every hole takes one class, an unmapped root is named, and a stopped root is counted.

<criterion id="BS6-AC2" cell_refs="BF-s-6"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>ALL-ROOTS ok=True</expect></criterion>
`BS6-AC2` -- the real estate: the denominator sums and every mapped root is run or counted.

<expected_criteria>BS6-AC1,BS6-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-6`.
<owned_cells>BF-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS6-AC1, BS6-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-s-6.all-roots-denominator.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS6-AC1,BS6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the unmapped roots with their name counts; the class counts; every `other` hole whole; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- the unmapped roots left out so the run reads as the whole estate (mapped + unmapped == roots_total; each unmapped root named); a stopped root dropped (completed + stopped == mapped); a second enumeration of roots that disagrees with the scope's (the face forbids it); BLIND: names that live only in AWS -- the repository plane.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS6-AC1 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=138; extended by the cell); BS6-AC2 base FAIL as expected (ran: no such command).
