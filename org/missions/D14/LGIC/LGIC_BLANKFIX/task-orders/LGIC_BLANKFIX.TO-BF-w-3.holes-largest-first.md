# TO LGIC_BLANKFIX.TO-BF-w-3 -- round 8 BF-w-3: holes filled root by root, largest hole count first -- registry rows drafted for the registry's lane, reader defects fixed, the rest owned

<to_id>LGIC_BLANKFIX.TO-BF-w-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-w-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round8.md`) | **outcome_ref:** FWD-2 |
**depends_on:** BF-w-2 merged on this slot (uncounted first, the CTO's order); handed by continuing the slot

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all --map infra/logic/registry/root_map.json`)
runs every Terraform root the root map covers and prints the denominator of roots first; `infra/logic/README.md` "Run the naming
check" explains its lines and fields. At the round-7 close it read `roots_total=87 mapped=63 unmapped=24 completed=63 stopped=0
items=1598 ... hole=285 carded_class_holes=205 source_bucket_holes=14 event_rule_holes=7 unknown_word_holes=0 other_holes=59
stale_hints=0 uncounted=301`; the whole output is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round7.txt`. The CTO's reading of round 7 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md` -- read
it first. Its ruling for FWD-2: no ceiling short of the full list; order (1) uncounted to 0, (2) holes by root, largest first, (3)
the held map entries; every round reports `hole` and `uncounted` before and after, with their denominators.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader), `opal_naming_rootmap.py`, `opal_naming_cadence.py`, `opal_naming_keyfill.py`,
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `_ruling_of`, the `lines`, `keys` and `all`
commands). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS
call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed), and
every `lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move every
day, and the registry's lane may add rows during this round.

### THE CELL

`BF-w-3` (item E3). The CTO: "fill holes on the roots with the most, until the round's slots run out; report `hole` before and after."
Each HOLE line's text has an owner in the accepted FWD-6 design's owner table (`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md`, 18 texts): most are
`4.0.0_SA_CRO` (a registry row), some are the creator (a rename), some `1.0.0_SA_CTO` (a rule defect). Row `LGIC_BLANKFIX-W4-S3`: a
schedule whose name is built in a local has no cadence row because the cadence reader sees only literal names
(`lib/opal_naming_cadence.py`).

**Build:**
1. Rank the mapped roots by HOLE count from the live `all` run. Work from the top, root by root, for as long as the round allows; a
   root is finished when every HOLE line of it has a disposition.
2. For each HOLE line, by its owner: a registry row -> draft it in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/REGISTRY_ROWS_round8.json`, keyed by registry file
   (`key_rulings.json`, `name_rulings.json`, `event_rules.json`, ...), each row in that file's `_about.row_fields` shape with a `_cite`
   (`file:line` that decides it); a cadence-reader defect of W4-S3's kind -> fix it in `lib/opal_naming_cadence.py` with a test case;
   anything else -> listed in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/HOLES_OWNED_round8.md` with its owner and what they owe.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_holes_fill.py`: it copies `infra/logic/registry/` to a temporary folder, merges the drafted rows into
   the copy (`_cite` stripped), runs the root check against the copy once, and prints one line per worked root (hole before -> after),
   then last: `HOLES-FILL ok=True before=N after=N roots_worked=N rows=N refused=0 owned_elsewhere=N`; `ok=True` when `after < before`,
   no drafted row is refused by the registry's own validation, and the roots were worked in descending hole order.

### ACCEPTANCE

<criterion id="BW3-AC1" cell_refs="BF-w-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/check_holes_fill.py</invocation><expect>HOLES-FILL ok=True</expect></criterion>
`BW3-AC1` -- holes fall with rows the registry would accept, worked largest root first.

<criterion id="BW3-AC2" cell_refs="BF-w-3"><invocation>python lib/tests/test_opal_naming_cadence.py</invocation><expect>CADENCE-TEST ok=True</expect></criterion>
`BW3-AC2` -- the cadence reader's test holds.

<expected_criteria>BW3-AC1,BW3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round8.md</decomp_doc> (round 8), cell `BF-w-3`.
<owned_cells>BF-w-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BW3-AC1, BW3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-w-3.holes-largest-first.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BW3-AC1,BW3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; hole before and after with the denominator; per worked root before -> after; rows by registry file; every hole owned elsewhere, by owner; the rows file's path for 4.0.0_SA_CRO; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a row typed to silence a line without evidence (each row cites the line that decides it); a hole moved to another class rather than filled (before and after are per root and by class); rows the registry's validation refuses (counted, must be 0); BLIND: rows the registry's owner may rule differently -- that is the CRO's write.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round7.md @ec6f56562b (the CTO's enrichment list E1 to E5); decomposition round 8. Base dry-run at the cut: BW3-AC1 base FAIL as expected (file absent; the trunk reads hole=285 over 63 mapped roots); BW3-AC2 base PASS as expected (ran: CADENCE-TEST ok=True cases=53; extended by the cell if it fixes the reader).
