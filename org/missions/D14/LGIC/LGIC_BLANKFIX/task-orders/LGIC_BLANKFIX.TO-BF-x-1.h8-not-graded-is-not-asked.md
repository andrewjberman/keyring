# TO LGIC_BLANKFIX.TO-BF-x-1 -- round 9 BF-x-1: the H8 rule: verdict NOT-GRADED maps to NOT-ASKED

<to_id>LGIC_BLANKFIX.TO-BF-x-1</to_id>
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

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-x-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round9.md`) | **outcome_ref:** FWD-2 |
**depends_on:** BF-x-2 (same slot, same test file; case 5 is red until BF-x-2 lands)

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

`BF-x-1` (item E1). The CTO's ruling on H8 (`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md` "Rulings on the graduated rows"): the ten names in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/HOLES_OWNED_round8.md`
(Route 53 records, IAM users, and log groups whose `aws-waf-logs-` prefix AWS itself requires) are types the canon deliberately does
not grade, and some are not ours to name at all. "This is a rule, not a grammar: the canon gains no DNS or IAM-user grammar."

**Build** in `lib/opal_naming_rootcheck.py` (and its test) only:
1. In `decide()`, an item whose grader verdict is `NOT-GRADED` is decided `NOT-ASKED` with the detail
   `this type is outside the canon, no name is owed` -- the CTO's sentence, verbatim. Nothing else in `decide()` moves.
2. If `HOLE_OWED` (or any owner table the test reads with `ast`) carries a needle that only the NOT-GRADED HOLE text matched, remove
   that needle, so the test's "no stale needle" check still holds; every HOLE text the module can still print keeps an owner.
3. A case in `lib/tests/test_opal_naming_rootcheck.py`: an item graded NOT-GRADED decides NOT-ASKED with that sentence, and the
   DIFFERENCE CONTROL -- an item graded with any other verdict and no canonical form still decides as it did at the base.
4. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_h8_rule.py`: it runs the `all` command once, reads each `OWNED` line of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/HOLES_OWNED_round8.md` (root, type, name), and
   prints one line per name (the kind the live run gives it), then last:
   `H8-RULE ok=True owned=N not_asked=N hole_before=N hole_after=N mapped=N`; `hole_before` is read from the ALL-ROOTS line of
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9_base.txt`; `ok=True` when every owned name reads NOT-ASKED, `owned` equals `not_asked`, and `hole_after < hole_before`.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-09 ~06:3xZ; row LGIC_BLANKFIX-D1-W1-S1):** the baseline this order's checker reads is the issuance base's own run, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9_base.txt` (78 mapped roots, hole=51, uncounted=17 at 9d55470156), not the round-8 close (63 mapped roots). The cut named the wrong file; every other word of the order stands.

### ACCEPTANCE

<criterion id="BX1-AC1" cell_refs="BF-x-1"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BX1-AC1` -- NOT-GRADED decides NOT-ASKED; any other ungraded verdict decides as before.

<criterion id="BX1-AC2" cell_refs="BF-x-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_h8_rule.py</invocation><expect>H8-RULE ok=True</expect></criterion>
`BX1-AC2` -- the ten H8 names read NOT-ASKED on the live run and hole falls.

<expected_criteria>BX1-AC1,BX1-AC2</expected_criteria>

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
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round8.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round9.md</decomp_doc> (round 9), cell `BF-x-1`.
<owned_cells>BF-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BX1-AC1, BX1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-x-1.h8-not-graded-is-not-asked.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BX1-AC1,BX1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; hole before and after with mapped; the ten names' kinds; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a rule wider than NOT-GRADED (the control keeps other ungraded verdicts as they were); a stale owner needle; the H8 names counted by a typed total (the checker reads them by name from the owned list); BLIND: the grader's NOT-GRADED set beyond the three H8 types -- the case asserts the rule, not the census of types.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md @2ba21c4271 (`1.0.0_SA_CTO`, item E1); decomposition round 9. Base dry-run at the cut, by the
issuer at base 9d55470156: BX1-AC1 base: FAIL as expected (ran: ROOTCHECK-TEST ok=False cases=319 -- case 5, row S12, repaired by BF-x-2 first; the NOT-GRADED case is added by the cell); BX1-AC2 base: FAIL as expected (file absent; the trunk reads hole=51 with the 10 H8 names HOLE).
