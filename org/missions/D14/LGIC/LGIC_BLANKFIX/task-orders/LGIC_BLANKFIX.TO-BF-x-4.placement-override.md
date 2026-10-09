# TO LGIC_BLANKFIX.TO-BF-x-4 -- round 9 BF-x-4: one audited override for the placement step (design arm H)

<to_id>LGIC_BLANKFIX.TO-BF-x-4</to_id>
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

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-x-4` (`decompositions/LGIC_BLANKFIX_DECOMP.round9.md`) | **outcome_ref:** FWD-6 |
**depends_on:** BF-x-3 (same slot, same scripts)

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

`BF-x-4` (item E4). Row W1-S21 (in `org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md`), ruled in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`: there is no override, so with the switch on a creator
whose name the canon cannot yet place has no way through. The shape the CTO named: `# surprise-row-override: <reason>` -- read today
by `.tools/safe-commit.sh` (search it for `surprise-row-override` and `SURPRISE_ROW_OVERRIDE`): a commit-message line, audited, then
exported for the hook. "A drain has none."

**Build:**
1. `.tools/safe-commit.sh` reads a commit-message line `# naming-place-override: <reason>` (reason required, non-empty), appends one
   audit line to `org/naming-place-override-audit.log` (UTC time, author, reason, the refused names), and exports
   `NAMING_PLACE_OVERRIDE` for the gate; `.tools/naming-gate.py` then prints the refusal as `OVERRIDDEN` and does not block.
   `.tools/safe-merge.sh` and every other path get no override.
2. The DIFFERENCE CONTROL: with the line, the refusal passes and is logged; without it (or with an empty reason), it blocks; the
   environment variable set by hand without safe-commit's audit line does not pass a refusal (the gate requires the audit row's
   presence, or safe-commit is the only setter -- choose one and state it in the gate's docstring).
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/exercise_override.py`: the arms above, in a temporary copy with the placement switch present there only; one line per
   arm, then last: `OVERRIDE-ARMS ok=True arms=N held=N`. It leaves no switch, temporary or audit file in the repository.

### ACCEPTANCE

<criterion id="BX4-AC1" cell_refs="BF-x-4"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/exercise_override.py</invocation><expect>OVERRIDE-ARMS ok=True</expect></criterion>
`BX4-AC1` -- with the audited line a refusal passes and is logged; without it, it blocks; a hand-set variable does not pass.

<criterion id="BX4-AC2" cell_refs="BF-x-4"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`BX4-AC2` -- the commit gate's self-test passes with the override's arms added.

<criterion id="BX4-AC3" cell_refs="BF-x-4" judgment="true"/>
`BX4-AC3` (judgment) -- 3.0.0_SA_CVO reads BF-x-3's and BF-x-4's arms against rows W1-S19, W1-S20 and W1-S21: do the three switch-on preconditions the CTO named now hold, so the switch could be turned on? You record the artifacts' paths and NO verdict.

<expected_criteria>BX4-AC1,BX4-AC2,BX4-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never created in the repository.
- The judgment criterion gets its artifact paths and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
.tools/safe-commit.sh
.tools/naming-gate.py
org/naming-place-override-audit.log
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md</decomp_doc> (round 9), cell `BF-x-4`.
<owned_cells>BF-x-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BX4-AC1, BX4-AC2, BX4-AC3 (BX4-AC3 judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-x-4.placement-override.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BX4-AC1,BX4-AC2,BX4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; each arm's expected and got; the override's grammar as built; the switch file's state at your last commit (absent); commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- an override that is a silent environment downgrade (a hand-set variable passes nothing); an override on the merge path; an unaudited pass; the audit log polluted by the exercise (temporary copy only); BLIND: a seat committing without safe-commit (bare git commit) never reaches the override or the gate.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md @2ba21c4271 (`1.0.0_SA_CTO`, item E4); decomposition round 9. Base dry-run at the cut, by the
issuer at base 9d55470156: BX4-AC1 base: FAIL as expected (file absent); BX4-AC2 base: PASS as expected (ran: NAMING-GATE-SELF-TEST: PASS; extended by the cell).
