# TO LGIC_BLANKFIX.TO-BF-x-6 -- round 9 BF-x-6: fill the holes on the newly mapped roots, largest root first

<to_id>LGIC_BLANKFIX.TO-BF-x-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-x-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round9.md`) | **outcome_ref:** FWD-2, FWD-7 |
**depends_on:** none (4.0.0_SA_CRO's write landed @1e660e15be)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all
--map infra/logic/registry/root_map.json`) runs every Terraform root the root map covers and prints the denominator of roots
first; `infra/logic/README.md` "Run the naming check" explains its lines and fields. At this cut, on the base your worktree is
made from, it reads: `ALL-ROOTS ok=True roots_total=87 mapped=78 unmapped=9 completed=78 stopped=0 items=2259 right=554 fix=1457 not_asked=174 pattern=23 carded=0 refused=0 hole=51 carded_class_holes=33 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=6 other_holes=12 stale_hints=0 uncounted=17`. The round-8 close is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ALL_ROOTS_round8.txt`. The CTO's reading of round 8 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md` -- read it first; its
ENRICHMENT LIST E1 to E6 is this round, one cell per item. The round-8 drain end is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ROUND8_DRAIN_END_AND_DELL1_HANDOFF.md`.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader and `UNCOUNTED_REASONS`), `opal_naming_rootmap.py`, `opal_naming_cadence.py`,
`opal_naming_keyfill.py`, `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `place`, `check_root`, `_ruling_of`,
`all_roots`, `HOLE_OWED`, the `lines`, `keys` and `all` commands). The gates: `.tools/naming-gate.py` (commit time),
`.tools/naming-apply-gate.py` (plan time), called by `.tools/safe-commit.sh` and `.tools/safe-apply.sh`. The registry is
`infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before you build. Import with
`sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS call and no network
call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (193 passed, 1 skipped), and every
`lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base except `test_opal_naming_rootcheck.py`, which reads
`ROOTCHECK-TEST ok=False` there on case 5 only (row S12; cell BF-x-2, first on slot ~1, repairs it). None may newly fail after your
build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move
every day, and the registry's lane may add rows during this round. **The switch file `org/mcp/naming-place.enforce` is absent and
stays absent:** no cell creates it, in the repository or outside a temporary folder; turning it on is `1.0.0_SA_CTO`'s act after
this round is graded.

### THE CELL

`BF-x-6` (item E6). `4.0.0_SA_CRO` wrote the 15 round-8 entries and confirmed the scope-`global` extension
(@1e660e15be; rulings `org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND8_RULINGS_20261009.md`), so the map now reads
`mapped=78 of 87, hole=51 (the 10 H8 names among them)` -- the 15 newly mapped roots carry the new holes. The round-8 cell that did this on the older roots is
`org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/LGIC_BLANKFIX.TO-BF-w-3.holes-largest-first.md`; its rows file and checker are in
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/` -- read them, follow the same shape.

**Build:**
1. Rank the roots newly mapped at @1e660e15be by HOLE count from the live `all` run; work from the top, root by root, for as long as
   the round allows; a root is finished when every HOLE line of it has a disposition.
2. Each HOLE line by its owner (the FWD-6 owner table, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md`): a registry row -> drafted in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/REGISTRY_ROWS_round9.json`,
   keyed by registry file, each row in that file's `_about.row_fields` shape with a `_cite` (`file:line` that decides it); a
   cadence-reader defect -> fixed in `lib/opal_naming_cadence.py` with a test case; anything else -> `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/HOLES_OWNED_round9.md`
   with its owner and what they owe. A name graded `NOT-GRADED` is not yours to fill: cell `BF-x-1` rules it NOT-ASKED this round;
   list it under that owner and do not draft a row for it.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_holes_new_roots.py`: it copies `infra/logic/registry/` to a temporary folder, merges the drafted rows into the
   copy (`_cite` stripped), runs the root check against the copy once, prints one line per worked root (hole before -> after), then
   last: `NEW-ROOTS-FILL ok=True mapped=N before=N after=N roots_worked=N rows=N refused=0 owned_elsewhere=N`; `ok=True` when
   `after < before`, no drafted row is refused by the registry's own validation, and the roots were worked in descending hole order.

### ACCEPTANCE

<criterion id="BX6-AC1" cell_refs="BF-x-6"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/check_holes_new_roots.py</invocation><expect>NEW-ROOTS-FILL ok=True</expect></criterion>
`BX6-AC1` -- holes on the new roots fall with rows the registry would accept, largest root first.

<criterion id="BX6-AC2" cell_refs="BF-x-6"><invocation>python lib/tests/test_opal_naming_cadence.py</invocation><expect>CADENCE-TEST ok=True</expect></criterion>
`BX6-AC2` -- the cadence reader's test holds.

<expected_criteria>BX6-AC1,BX6-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never created in the repository.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md</decomp_doc> (round 9), cell `BF-x-6`.
<owned_cells>BF-x-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BX6-AC1, BX6-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/LGIC_BLANKFIX.TO-BF-x-6.holes-on-new-roots.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BX6-AC1,BX6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last lines whole; mapped and hole before and after; rows drafted per registry file; owned-elsewhere per owner; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a row drafted for a NOT-GRADED name (listed under BF-x-1 instead); a registry edit (rows are drafted in the folder; only 4.0.0_SA_CRO writes the registry); roots worked out of hole order (the checker asserts the order); BLIND: names whose literal lives only in AWS; roots still unmapped (9 of 87).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md @2ba21c4271 (`1.0.0_SA_CTO`, item E6); decomposition round 9. Base dry-run at the cut, by the
issuer at base 9d55470156: BX6-AC1 base: FAIL as expected (file absent); BX6-AC2 base: PASS as expected (ran: CADENCE-TEST ok=True cases=59).
