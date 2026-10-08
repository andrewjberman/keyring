# TO LGIC_BLANKFIX.TO-BF-v-4 -- round 7 BF-v-4: a root's names=0 means nothing to name -- names built in a local, a module or a generated .json are counted or printed UNCOUNTED

<to_id>LGIC_BLANKFIX.TO-BF-v-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-v-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md`) | **outcome_ref:** FWD-2, FWD-7 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first. At the round-6 close it read
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0
hole=0 ... stale_hints=0`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round6.txt`. One line per name: `KIND type current -> detail  [where]`, kinds
`RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`. Each unmapped root is printed `UNMAPPED <root> names=N`. The
CTO's reading of round 6 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, on the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND6_L9_GRADE_BU6_BU7_20261008.md` -- read the analysis first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots and their
names, `root_items`), `opal_naming_rootmap.py` (`load_map`, `resolve`), `opal_naming_cadence.py`, `opal_naming_keyfill.py`,
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and `all`
commands). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS
call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed), and
every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move every
day, and the registry's lane may add map entries during this round.

### THE CELL

`BF-v-4` (item E3; row `LGIC_BLANKFIX-W1-S14`, ARMED, disarm owner `1.0.0_SA_CTO`). `root_items` in `lib/opal_naming_scope.py`
takes a root's names from `opal_naming.census_repo()`, which reads only literal names. A root that builds a name in a `locals`
block, through a module, or in a generated `.json` (for example `nfra-agentbus`: `name = local.role_a_name`; `etfs-rivalfunds`:
`generated.auto.tfvars.json`) reads `names=0` or a partial count. Round 6's sort found 11 such roots among the 24 that read
`names=0`: the `verdict: DECLARES-NAMES` sections of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/MAP_ENTRIES_FOR_RULING_round6.md`. The CTO: "Make the census count those names or print
them as `UNCOUNTED` with a reason; a root's `names=0` must mean nothing to name."

**Build** in `lib/opal_naming_scope.py` and `lib/opal_naming_rootcheck.py` (not in `lib/opal_naming.py`):
1. For a root, find every named resource the literal reader does not count: a resource block of a type the census grades whose
   name attribute is not a string literal, and a `module` block whose called module builds its names from input variables. Where
   the expression resolves to a literal inside the root's own files (a `locals` value that is a literal, a `.json`/`.tfvars.json`
   value the root reads), count it as an ordinary item with its `where` at the declaring line. Otherwise it is UNCOUNTED, with a
   reason naming what was not followed (`local`, `var`, `module`, `json`, `interpolation`).
2. The `all` command: each root's `UNMAPPED` line gains `uncounted=N` at its end; a mapped root prints one
   `UNCOUNTED <type> <attribute> = <expression> -- <reason>  [file:line]` line per case; the `ALL-ROOTS` last line gains ONE field
   `uncounted=N` at its END (no other field moves). A mapped root's names newly counted by step 1 are graded like any other.
3. The DIFFERENCE CONTROL in `lib/tests/test_opal_naming_scope.py`, on `.tf` text the test writes to a temporary folder: a literal
   name counted once; a name from a literal `local` counted; a name from `var.` UNCOUNTED with reason `var`; a module call
   UNCOUNTED with reason `module`; a root with none of these reads `uncounted=0`.
4. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_declares_names.py`: it reads the `verdict: DECLARES-NAMES` roots from the ruling file named above,
   runs the `all` command once, and for each such root reads its `UNMAPPED` line. Last line:
   `DECLARES-CHECK ok=True roots=N still_zero=N`; `ok=True` when every such root reads `names` > 0 or `uncounted` > 0 and `roots`
   equals the ruling file's count of that verdict.

### ACCEPTANCE

<criterion id="BV4-AC1" cell_refs="BF-v-4"><invocation>python lib/tests/test_opal_naming_scope.py</invocation><expect>SCOPE-TEST ok=True</expect></criterion>
`BV4-AC1` -- the difference control: literal, literal local, var, module, none.

<criterion id="BV4-AC2" cell_refs="BF-v-4"><invocation>python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json</invocation><expect>uncounted=[0-9]+</expect></criterion>
`BV4-AC2` -- the estate run counts uncounted names at the end of its last line.

<criterion id="BV4-AC3" cell_refs="BF-v-4"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_declares_names.py</invocation><expect>DECLARES-CHECK ok=True</expect></criterion>
`BV4-AC3` -- every root round 6 found declaring names behind a zero now reads more than zero.

<expected_criteria>BV4-AC1,BV4-AC2,BV4-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_scope.py
lib/tests/test_opal_naming_scope.py
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md</decomp_doc> (round 7), cell `BF-v-4`.
<owned_cells>BF-v-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BV4-AC1, BV4-AC2, BV4-AC3. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-v-4.uncounted-names.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BV4-AC1,BV4-AC2,BV4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; the before-and-after of the all command's last line; every root whose names count moved, before and after; the UNCOUNTED reasons by count; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a zero kept by not looking (each DECLARES-NAMES root is read back by name); an UNCOUNTED line that hides a name the root's own files resolve to a literal (step 1 resolves locals and .json first, and the test proves it); a field slipped into the middle of the last line (it goes at the end); BLIND: names built only at apply time in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round6.md @ea45e82c70 (the CTO's enrichment list E1 to E5); decomposition round 7. Base dry-run at the cut: BV4-AC1 base PASS as expected (ran: SCOPE-TEST ok=True assertions=362; extended by the cell); BV4-AC2 base FAIL as expected (ran: ALL-ROOTS ok=True ... stale_hints=0; no uncounted field); BV4-AC3 base FAIL as expected (file absent; the ruling file holds 11 DECLARES-NAMES verdicts).
