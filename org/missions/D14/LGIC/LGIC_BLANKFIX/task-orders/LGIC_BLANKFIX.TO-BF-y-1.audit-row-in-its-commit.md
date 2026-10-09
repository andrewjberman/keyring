# TO LGIC_BLANKFIX.TO-BF-y-1 -- round 10 BF-y-1: the override's audit row is committed in the same commit it permits

<to_id>LGIC_BLANKFIX.TO-BF-y-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-y-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round10.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none (first on slot ~1)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all
--map infra/logic/registry/root_map.json`) runs every Terraform root the root map covers and prints the denominator of roots
first; `infra/logic/README.md` "Run the naming check" explains its lines and fields. At this cut, on the base your worktree is
made from, it reads: `ALL-ROOTS ok=True roots_total=87 mapped=78 unmapped=9 completed=78 stopped=0 items=2263 right=558 fix=1460 not_asked=222 pattern=23 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0 stale_hints=0 uncounted=1 counted_at_caller=17`. The round-9 close is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9.txt`. The CTO's reading of round 9 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round9.md` -- read it first, with its
ADDENDUM 1 (this round is three cells: the two override fixes and the nine held entries). The round-9 drain end is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ROUND9_DRAIN_END.md`.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader and `UNCOUNTED_REASONS`), `opal_naming_rootmap.py`, `opal_naming_cadence.py`,
`opal_naming_keyfill.py`, `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `place`, `check_root`, `_ruling_of`,
`all_roots`, `HOLE_OWED`, the `lines`, `keys` and `all` commands). The gates: `.tools/naming-gate.py` (commit time),
`.tools/naming-apply-gate.py` (plan time), called by `.tools/safe-commit.sh` and `.tools/safe-apply.sh`. The registry is
`infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before you build. Import with
`sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS call and no network
call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (193 passed, 1 skipped), and every
`lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move
every day, and the registry's lane may add rows during this round. **The switch file `org/mcp/naming-place.enforce` is PRESENT since
@4d2bfc6dfd:** the placement refusal is live on every commit and apply. No cell deletes, moves or edits it; exercise the gates
only in a temporary copy, and never write a real override audit row.

### THE CELL

`BF-y-1`. Row D1-W2-S2 and the laptop CTO's ruling XA-...-3003 (a) (msgs 2045, 2050): today `.tools/safe-commit.sh`
appends the override's audit line to `org/naming-place-override-audit.log`, which `.gitignore` (`*.log`) ignores, so an override is
visible only on the box that wrote it. The ruling: the audit row is committed in the same commit it permits. The override as built
in round 9 is described in `org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/LGIC_BLANKFIX.TO-BF-x-4.placement-override.md` and exercised by `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/exercise_override.py` -- read both, and the override
blocks in `.tools/safe-commit.sh` (search `naming-place-override`) and `.tools/naming-gate.py` (`override_valid`, `apply_override`).

**Build:**
1. `.tools/safe-commit.sh` writes the audit row as ONE JSON line to the TRACKED file `org/audit/naming-place-override-audit.jsonl` (fields: `utc`,
   `author`, `id`, `reason`, `names` (list), `msg_sha256` left empty for cell BF-y-2) and adds that file to THIS commit's
   pathspec, so the landed commit carries its own audit row. The `.log` file is no longer written. Nothing else in the commit
   flow changes; a commit with no override line does not touch the audit file.
2. `.tools/naming-gate.py` reads the override's row from the staged (index) copy of `org/audit/naming-place-override-audit.jsonl`, not from a file on
   disk only, so the row it honours is the one that will land.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_audit_in_commit.py`: in a temporary git repository built from copies of the real scripts (switch present
   there only), it commits once WITH the override line and once WITHOUT, and reads the landed commits: the first carries the
   audit row in `git show --stat` and its id matches the gate's OVERRIDDEN line; the second leaves the audit file untouched and is
   refused (the DIFFERENCE CONTROL). Last line: `AUDIT-IN-COMMIT ok=True arms=N held=N`. It writes nothing in the repository.

### ACCEPTANCE

<criterion id="BY1-AC1" cell_refs="BF-y-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_audit_in_commit.py</invocation><expect>AUDIT-IN-COMMIT ok=True</expect></criterion>
`BY1-AC1` -- an overridden commit carries its own audit row; a commit without the line is refused and leaves the file untouched.

<criterion id="BY1-AC2" cell_refs="BF-y-1"><invocation>python .tools/naming-gate.py --self-test</invocation><expect>NAMING-GATE-SELF-TEST: PASS</expect></criterion>
`BY1-AC2` -- the commit gate's self-test passes with the index-read arm added.

<expected_criteria>BY1-AC1,BY1-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
.tools/safe-commit.sh
.tools/naming-gate.py
org/audit/naming-place-override-audit.jsonl
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round9.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round10.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round10.md</decomp_doc> (round 10), cell `BF-y-1`.
<owned_cells>BF-y-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BY1-AC1, BY1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-y-1.audit-row-in-its-commit.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BY1-AC1,BY1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; each arm's expected and got; the audit row's shape as built; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- an audit row left only on disk (the exercise reads the landed commit); a commit with no override touching the audit file (control arm); a real audit row or switch change in the repository (temporary repository only); BLIND: seats that commit without safe-commit.sh never write a row.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round9.md @1bd6fcf3dd + ADDENDUM 1 (`1.0.0_SA_CTO~DELL1`, msgs 2050, 2088), item ADDENDUM 1 (1); decomposition round 10. Base dry-run at the cut, by the
issuer at base 9f252e010a: BY1-AC1 base: FAIL as expected (file absent); BY1-AC2 base: PASS as expected (ran: NAMING-GATE-SELF-TEST: PASS; extended by the cell).
