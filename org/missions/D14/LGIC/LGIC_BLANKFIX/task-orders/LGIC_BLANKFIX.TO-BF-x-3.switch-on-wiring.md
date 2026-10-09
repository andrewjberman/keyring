# TO LGIC_BLANKFIX.TO-BF-x-3 -- round 9 BF-x-3: switch-on wiring: safe-commit and safe-apply act on the placement step's refusal; safe-apply hands the plan gate its tree

<to_id>LGIC_BLANKFIX.TO-BF-x-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-x-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round9.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none (first on slot ~2)

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

`BF-x-3` (item E3). Rows W1-S19 and W1-S20 (in `org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md`), ruled in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`: today `.tools/safe-commit.sh` and
`.tools/safe-apply.sh` act on the naming gate's exit only while `org/mcp/naming-gate.enforce` is present (or `NAMING_GATE_ENFORCE=1`),
so `org/mcp/naming-place.enforce` alone blocks nothing (W1-S19); and safe-apply gives the plan-mode gate no tree, so the placement
step finds an added resource's root by its name (W1-S20). The FWD-6 design is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md`.

**Build:**
1. `.tools/safe-commit.sh`: while `org/mcp/naming-place.enforce` is present, a placement-step refusal from `.tools/naming-gate.py`
   blocks the commit, whatever `naming-gate.enforce` says. Tell it apart from the older limb's REFUSE by a line or exit code the gate
   already prints, or add one to the gate; the older limb's warn window is unchanged.
2. `.tools/safe-apply.sh`: the same for `.tools/naming-apply-gate.py`, in both its pre-plan and plan stages; and hand the plan gate
   the Terraform root directory it plans (an argument the gate reads), so the placement step reads the root, not a name.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/exercise_switch_on.py`: in a temporary copy (never the repository's `org/mcp/`), it runs the real scripts' naming
   limbs on a hand-built unplaceable name with the placement switch PRESENT and `naming-gate.enforce` ABSENT (both safe-commit's
   and safe-apply's limbs block), and with the placement switch ABSENT (neither blocks) -- the DIFFERENCE CONTROL -- and a plan-mode
   arm showing the gate received the tree. It prints one line per arm (expected, got), then last:
   `SWITCH-ON ok=True arms=N held=N`. It never leaves a switch file or temporary file in the repository.

### ACCEPTANCE

<criterion id="BX3-AC1" cell_refs="BF-x-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/exercise_switch_on.py</invocation><expect>SWITCH-ON ok=True</expect></criterion>
`BX3-AC1` -- with the placement switch present a refusal blocks both scripts; absent, neither; the plan gate gets its tree.

<criterion id="BX3-AC2" cell_refs="BF-x-3"><invocation>python .tools/naming-apply-gate.py --self-test</invocation><expect>NAMING-APPLY-GATE-SELF-TEST: PASS</expect></criterion>
`BX3-AC2` -- the apply gate's own self-test passes with the tree argument's arm added.

<expected_criteria>BX3-AC1,BX3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never created in the repository.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
.tools/safe-commit.sh
.tools/safe-apply.sh
.tools/naming-apply-gate.py
.tools/naming-gate.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md</decomp_doc> (round 9), cell `BF-x-3`.
<owned_cells>BF-x-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BX3-AC1, BX3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-x-3.switch-on-wiring.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BX3-AC1,BX3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; each arm's expected and got; the diff stat of each script; the switch file's state at your last commit (absent); commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a switch that refuses only while the older switch is on (the arm with naming-gate.enforce absent); a changed warn window for the older limb; a switch file created in org/mcp/ (temporary copy only); a plan gate still guessing the root; BLIND: seats whose worktree base predates the merge run the old scripts until re-based.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md @2ba21c4271 (`1.0.0_SA_CTO`, item E3); decomposition round 9. Base dry-run at the cut, by the
issuer at base 9d55470156: BX3-AC1 base: FAIL as expected (file absent); BX3-AC2 base: PASS as expected (ran: NAMING-APPLY-GATE-SELF-TEST: PASS; extended by the cell).
