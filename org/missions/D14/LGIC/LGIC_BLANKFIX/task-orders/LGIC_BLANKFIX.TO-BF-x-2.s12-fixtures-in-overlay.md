# TO LGIC_BLANKFIX.TO-BF-x-2 -- round 9 BF-x-2: ROOTCHECK-TEST case 5 and FWD-6 arm F plant their HOLE in the overlay

<to_id>LGIC_BLANKFIX.TO-BF-x-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-x-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round9.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none (first on slot ~1)

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

`BF-x-2` (item E2). Row S12 (`REMEDIATION_v7`, ruled in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`): ROOTCHECK-TEST case 5 and FWD-6 arm F (in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd6_arms.py`)
each used an intake HOLE that `4.0.0_SA_CRO`'s registry write @46d6a05de0 closed, so both read red on the trunk. "The fix ...: plant
the HOLE in the overlay, so the fixture no longer depends on the live registry." Ruling W1-S22 (@b82324057e): while the switch is
absent the commit gate skips the placement step unless `NAMING_PLACE_PREVIEW=1`; arm G runs with it.

**Build:**
1. `lib/tests/test_opal_naming_rootcheck.py` case 5: build its HOLE from the readers' overlay (a registry copy or the in-memory
   overlay the test already uses), never from a live registry row's absence.
2. `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd6_arms.py` arm F: the same, its HOLE planted in the overlay the arm hands the gate. State in the file's docstring that arm G runs
   with `NAMING_PLACE_PREVIEW=1`. Every other arm unchanged.
3. The DIFFERENCE CONTROL, inside the arms run: arm F's planted HOLE is refused with the switch present and passes (printed, not
   refused) with it absent -- the same two outcomes the design states.

### ACCEPTANCE

<criterion id="BX2-AC1" cell_refs="BF-x-2"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BX2-AC1` -- case 5 holds on the trunk and does not read the live registry for its HOLE.

<criterion id="BX2-AC2" cell_refs="BF-x-2"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd6_arms.py</invocation><expect>FWD6-ARMS ok=True</expect></criterion>
`BX2-AC2` -- arms A to G hold on the trunk, arm F from the overlay.

<expected_criteria>BX2-AC1,BX2-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never created in the repository.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md</decomp_doc> (round 9), cell `BF-x-2`.
<owned_cells>BF-x-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BX2-AC1, BX2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-x-2.s12-fixtures-in-overlay.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BX2-AC1,BX2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; each arm's expected and got; the switch file's state at your last commit (absent); commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a fixture that passes because the registry moved (the HOLE is planted, not found); arm G silently skipped (NAMING_PLACE_PREVIEW=1 stated and used); a switch file left behind; BLIND: overlays other fixtures may still read from the live registry -- only case 5 and arm F are in scope.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md @2ba21c4271 (`1.0.0_SA_CTO`, item E2); decomposition round 9. Base dry-run at the cut, by the
issuer at base 9d55470156: BX2-AC1 base: FAIL as expected (ran: ROOTCHECK-TEST ok=False cases=319, 'FAIL: a fixed HOLE: the count shrinks, no new line'); BX2-AC2 base: FAIL as expected (ran: FWD6-ARMS ok=False arms=7 held=5; F holes head=0 post=0; G same_row_text_as_A=False without NAMING_PLACE_PREVIEW).
