# TO LGIC_BLANKFIX.TO-BF-x-5 -- round 9 BF-x-5: the 17 module-input names print as counted at the caller; uncounted reads 0

<to_id>LGIC_BLANKFIX.TO-BF-x-5</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-x-5` (`decompositions/LGIC_BLANKFIX_DECOMP.round9.md`) | **outcome_ref:** FWD-2 |
**depends_on:** BF-x-1 (same slot, same files)

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

`BF-x-5` (item E5). The CTO's ruling on W4-S6 (`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`): "A reusable module's input is named by its caller, and the
census already counts it there. The census prints these as counted at the caller, so `uncounted` reads 0 with the 17 listed, and
nothing is lost." At the base the 17 residual UNCOUNTED lines all carry reason `module-input` (`lib/opal_naming_scope.py`
`UNCOUNTED_REASONS`).

**Build** in `lib/opal_naming_rootcheck.py` `all_roots` (and its test) only:
1. A `module-input` line is printed as `COUNTED-AT-CALLER <type> <attribute> = <expression>  [<where>]` and is not added to
   `uncounted`. Every other UNCOUNTED reason prints and counts as before. The ALL-ROOTS line gains the field
   `counted_at_caller=N` after `uncounted=N`; no other field moves.
2. A case in `lib/tests/test_opal_naming_rootcheck.py` with the DIFFERENCE CONTROL: a `module-input` residual prints
   COUNTED-AT-CALLER and does not count; an `apply-time` residual still prints UNCOUNTED and counts.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_counted_at_caller.py`: it reads the base `uncounted` from the ALL-ROOTS line of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9_base.txt`, runs the `all` command
   once, and prints last: `CALLER-COUNT ok=True uncounted_before=N uncounted_after=N counted_at_caller=N other_reasons=N`; `ok=True`
   when `uncounted_after == other_reasons`, `counted_at_caller + uncounted_after == uncounted_before` on a base with no new roots,
   or else the checker names the roots whose names moved and still requires `uncounted_after == other_reasons`.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-09 ~06:3xZ; row LGIC_BLANKFIX-D1-W1-S1):** the baseline this order's checker reads is the issuance base's own run, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9_base.txt` (78 mapped roots, hole=51, uncounted=17 at 9d55470156), not the round-8 close (63 mapped roots). The cut named the wrong file; every other word of the order stands.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-09 ~06:5xZ; row LGIC_BLANKFIX-D1-S2):** `lib/tests/test_opal_naming_scope.py` line 370 asserts `uncounted=` is the LAST field of the ALL-ROOTS line, so the appended `counted_at_caller` field turns SCOPE-TEST red. The grant adds that test file; change only that assertion to read `uncounted` by its key (it already builds `kv`), keeping the count relation it checks. Done when `python lib/tests/test_opal_naming_scope.py` prints `SCOPE-TEST ok=True` beside BX5-AC1 and BX5-AC2 (criteria text unchanged).

### ACCEPTANCE

<criterion id="BX5-AC1" cell_refs="BF-x-5"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BX5-AC1` -- module-input prints COUNTED-AT-CALLER and does not count; apply-time still counts.

<criterion id="BX5-AC2" cell_refs="BF-x-5"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_counted_at_caller.py</invocation><expect>CALLER-COUNT ok=True</expect></criterion>
`BX5-AC2` -- uncounted reads only the residuals the repository cannot decide, with the module inputs listed.

<expected_criteria>BX5-AC1,BX5-AC2</expected_criteria>

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
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
lib/tests/test_opal_naming_scope.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md</decomp_doc> (round 9), cell `BF-x-5`.
<owned_cells>BF-x-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BX5-AC1, BX5-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-x-5.counted-at-caller.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BX5-AC1,BX5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; uncounted before and after by reason; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a name dropped instead of listed (each module-input still prints one line); another reason folded in (the control keeps apply-time counted); a field reorder breaking a reader of the ALL-ROOTS line (new field appended after uncounted); BLIND: readers of the ALL-ROOTS line outside lib/ that parse fields by position -- not swept.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md @2ba21c4271 (`1.0.0_SA_CTO`, item E5); decomposition round 9. Base dry-run at the cut, by the
issuer at base 9d55470156: BX5-AC1 base: FAIL as expected (ran: ROOTCHECK-TEST ok=False cases=319, case 5; the caller case is added by the cell); BX5-AC2 base: FAIL as expected (file absent; the trunk reads uncounted=17, all module-input).
