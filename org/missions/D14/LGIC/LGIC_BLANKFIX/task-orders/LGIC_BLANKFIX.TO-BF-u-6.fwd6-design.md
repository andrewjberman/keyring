# TO LGIC_BLANKFIX.TO-BF-u-6 -- round 6 BF-u-6: the design of the check that tells a name's creator at creation -- from the estate's past pre-write refusals, design only

<to_id>LGIC_BLANKFIX.TO-BF-u-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete -- proof-of-spec VALID (rc=0)</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-u-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round6.md`) | **outcome_ref:** FWD-6 |
**depends_on:** BF-u-1 merged on this slot; handed by continuing the slot

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first. At the round-5 close it read
`roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0
hole=0`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round5_second_seat.txt`. One line per name: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`,
`NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`. Each unmapped root is printed `UNMAPPED <root> names=N`. The CTO's reading is
`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots and their
names), `opal_naming_rootmap.py` (`load_map`, `resolve`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and
`all` commands). The registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `name_rulings.json`,
`event_rules.json`, `legacy_addresses.json`, `resources.json`, `systems.json`); only `4.0.0_SA_CRO` writes it. Read the modules
your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code
and output; no new dependency; no AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider`
passes whole at the base (194 passed), and every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base EXCEPT
`test_opal_naming_keyfill.py`, which is red (row `LGIC_BLANKFIX-S7`; cell `BF-u-4` repairs it). None may newly fail after your
build. A test you write asserts relations and the rows it needs by name, never a typed total of repository names, roots or
registry rows: those move every day, and the registry's lane is adding map entries during this round.

### THE CELL

`BF-u-6` (item E5, which serves FWD-6: `1.0.0_SA_CTO` msg 106956, analysis amended @cbdf36254c). The analysis: "FWD-6: the creator
hears at creation. The check, run before any name is written, refuses a new stored name the canon would print as FIX. Design only
in round 6." The PRD's FWD-6 is `org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md` lines 66-71: its ACCEPT has two halves -- the person
is told at that moment AND told what they owe to make the name placeable; and the list of unplaceable names is no longer than it
was the last time anyone ran the check. The design answers both.

The estate's past patterns are `org/tier1_exec/4.0.0_SA_CRO/deliverables/PRE_WRITE_REFUSAL_PATTERNS_20261008.md` (`4.0.0_SA_CRO` @cbf52722b0): 29 checks that refuse before a write lands,
each with where it lives, what it refuses, its bypass and its known failures. Two rows bear most directly: the commit-time naming
gate already in the tree (CLAUDE.md rule 30, WARN today) and the precedent at the end of its patterns section (rows keyed on a path
that break on a move, the E2 failure).

**Build: a design, no code.** Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md` with these sections, each a `## ` heading:
`Outcome` (FWD-6's PRD text, quoted with its line numbers), `Past patterns` (each pattern of the CRO's file you use or reject, and
why; the naming gate's row answered by name), `Where it runs`, `The decision rule`, `What it refuses and what it lets through`
(with a deliberately wrong and a deliberately right example from the live run's lines, and what the person is told they owe),
`The exercise that would prove it` (with its negative arm), `What it does not cover`. Every repository path it cites must exist.
Then write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd6_design.py`: it checks the seven headings are present in that order and that every backticked
repository path in the file exists, and prints `FWD6-DESIGN ok=True headings=7 paths=N missing=0`.

### ACCEPTANCE

<criterion id="BU6-AC1" cell_refs="BF-u-6"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd6_design.py</invocation><expect>FWD6-DESIGN ok=True</expect></criterion>
`BU6-AC1` -- the design has its seven parts and cites only paths that exist.

<criterion id="BU6-AC2" cell_refs="BF-u-6" judgment="true"/>
`BU6-AC2` (judgment) -- `3.0.0_SA_CVO` reads the design against FWD-6's ACCEPT (PRD lines 66-71): could it be built and exercised as written, does it tell the person what they owe, and does its exercise hold a negative arm? You record the artifacts' paths and NO verdict.

<expected_criteria>BU6-AC1,BU6-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round6.md</decomp_doc> (round 6), cell `BF-u-6`.
<owned_cells>BF-u-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BU6-AC1, BU6-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-u-6.fwd6-design.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BU6-AC1,BU6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the design's decision rule in one paragraph; each pattern used or rejected; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a design that restates the analysis's sentence without reading the estate's patterns (one section answers each pattern); a design that refuses but never says what is owed (the ACCEPT's second half is a heading's content); a cited file that does not exist (the check counts missing paths); BLIND: whether the design can be built in one round -- that is the CTO's reading.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round5.md @34ba4c1c90, amended @cbdf36254c (the CTO's enrichment list E1 to E6); decomposition round 6. Base dry-run at the cut: BU6-AC1 base FAIL as expected (file absent).
