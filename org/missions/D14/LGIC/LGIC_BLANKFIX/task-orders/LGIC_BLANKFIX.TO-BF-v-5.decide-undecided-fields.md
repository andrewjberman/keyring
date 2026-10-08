# TO LGIC_BLANKFIX.TO-BF-v-5 -- round 7 BF-v-5: the 180 UNDECIDED fields of the drafted map entries decided, largest roots first -- and how many entries would land

<to_id>LGIC_BLANKFIX.TO-BF-v-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-v-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md`) | **outcome_ref:** FWD-7, FWD-2 |
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

`BF-v-5` (item E4; row `LGIC_BLANKFIX-S10`). Round 6 drafted a root-map entry for each of the 74 unmapped roots
(`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/MAP_ENTRIES_FOR_RULING_round6.md`, 74 `### ` sections). `4.0.0_SA_CRO` built the entries from it and validated each against the loader:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND6_NOTES_20261008.md` (read it whole). Only `inf-pipeline` loads; 60 ordinary entries carry 180 UNDECIDED fields between them (source
51, fills 49, scope 33, exceptions 26, system 19, why 2), listed per root in the notes; the 13 `names: none` entries can now load
(round 6's `BF-u-2`). The CTO: "Decide the 180 UNDECIDED fields for the largest roots first, so drafted map entries can land;
measure how many land." The map is written only by `4.0.0_SA_CRO`; your cell hands that seat entries it can write.

**Build** in your deliverables folder:
1. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/MAP_ENTRIES_round7.json`: `{"roots": {<root>: <entry>}}` with one entry for EACH of the 74 roots of the
   ruling file, in the shape `infra/logic/registry/root_map.json`'s `_about.row_fields` defines (ordinary, or `names: 'none'`), plus a `_cite` object
   giving, for every field, the repository `file:line` that decides it -- or the string `UNDECIDED` as the field's value with
   `_cite` saying what was read that does not decide it. Start from the round-6 drafts; work the roots in order of name count,
   largest first, deciding every field the root's own files and the registry decide. A value is never taken from a folder's name
   alone. The two empty roots (`canonical-schwab-si2-schedule`, `opal-assets-absence`) keep `why: UNDECIDED`, citing the CRO's
   recommendation to retire them rather than add a third value.
2. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_entries_land.py`: for each entry, it merges that entry alone into a temporary copy of
   `infra/logic/registry/root_map.json` and calls `opal_naming_rootmap.load_map` on it; an entry LANDS when it carries no `UNDECIDED` value and the
   loader accepts it; it is HELD when it carries one; it is REFUSED when it carries none and the loader refuses it. Then it merges
   every landing entry together into one temporary map and runs the `all` command on it once. It prints one line per root (verdict,
   root, the undecided fields), then the `ALL-ROOTS` line of the merged run, and last:
   `ENTRIES-LAND ok=True entries=N land=N held=N refused=0 undecided_fields=N merged_ok=True`; `ok=True` when `refused=0`,
   `land + held == entries`, `entries` equals the ruling file's section count, and the merged run prints `ok=True`.

### ACCEPTANCE

<criterion id="BV5-AC1" cell_refs="BF-v-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_entries_land.py</invocation><expect>ENTRIES-LAND ok=True</expect></criterion>
`BV5-AC1` -- every drafted entry either lands or names what holds it, none is refused, and the landing entries run whole together.

<expected_criteria>BV5-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round6.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round7.md</decomp_doc> (round 7), cell `BF-v-5`.
<owned_cells>BF-v-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BV5-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-v-5.decide-undecided-fields.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BV5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; land/held counts and undecided_fields against round 6's 180; the ten largest roots with each field decided or what holds it; the merged ALL-ROOTS line; the entries file's path for 4.0.0_SA_CRO; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a field filled from a folder's spelling so an entry lands (each decided value cites the file and line that decide it); an entry dropped so the counts look better (entries is checked against the ruling file); a value the loader accepts but the root's files contradict (the cite is re-read); BLIND: names that live only in AWS.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round6.md @ea45e82c70 (the CTO's enrichment list E1 to E5); decomposition round 7. Base dry-run at the cut: BV5-AC1 base FAIL as expected (file absent; the CRO's notes read 1 of 74 loading, 180 undecided fields).
