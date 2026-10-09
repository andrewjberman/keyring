# TO LGIC_BLANKFIX.TO-BF-y-2 -- round 10 BF-y-2: the override is bound to the commit message, with a forged-row negative arm

<to_id>LGIC_BLANKFIX.TO-BF-y-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-y-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round10.md`) | **outcome_ref:** FWD-6 |
**depends_on:** BF-y-1 (same slot, same scripts)

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

`BF-y-2`. The forge hazard declared in BF-x-4's proof and ruled in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round9.md` R2 and XA-...-3003 (a): `override_valid` in
`.tools/naming-gate.py` honours any audit row younger than 600 s that names the refused name, so a pre-written row can admit a
later commit. The ruling: the override is bound to the commit message, not to a log row by age.

**Build:**
1. `.tools/safe-commit.sh` computes `sha256` of the exact commit message it will commit (the `-m`/`-F` text, as passed) and writes
   it as the audit row's `msg_sha256` (the field BF-y-1 leaves empty), and hands the gate the same message (a file path argument
   or an environment variable naming a file).
2. `.tools/naming-gate.py` `override_valid` passes a refused name only when the staged audit row's `msg_sha256` equals the hash of
   the message it is handed AND the message carries a non-empty `# naming-place-override:` line; the 600 s window is retired.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_override_bound.py`: in a temporary repository built from copies of the real scripts (switch present there
   only), the arms: a real override passes; a FORGED row (a valid-looking row whose `msg_sha256` belongs to a different message)
   is refused -- the negative arm; a row with the right hash but a message without the override line is refused; a hand-set
   variable passes nothing. Last line: `OVERRIDE-BOUND ok=True arms=N held=N`. It writes nothing in the repository. Keep
   `exercise_audit_in_commit.py` passing.

### ACCEPTANCE

<criterion id="BY2-AC1" cell_refs="BF-y-2"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_override_bound.py</invocation><expect>OVERRIDE-BOUND ok=True</expect></criterion>
`BY2-AC1` -- an override passes only when its row's hash is this commit's message; a forged row is refused.

<criterion id="BY2-AC2" cell_refs="BF-y-2"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_audit_in_commit.py</invocation><expect>AUDIT-IN-COMMIT ok=True</expect></criterion>
`BY2-AC2` -- the audit row still travels in the commit it permits.

<criterion id="BY2-AC3" cell_refs="BF-y-2" judgment="true"/>
`BY2-AC3` (judgment) -- 3.0.0_SA_CVO reads BF-y-1's and BF-y-2's arms against row D1-W2-S2 and the forge hazard: is an override now visible fabric-wide in git and impossible to admit with a row written for another commit? You record the artifacts' paths and NO verdict.

<expected_criteria>BY2-AC1,BY2-AC2,BY2-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- The judgment criterion gets its artifact paths and NO verdict from you.
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
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round10.md</decomp_doc> (round 10), cell `BF-y-2`.
<owned_cells>BF-y-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BY2-AC1, BY2-AC2, BY2-AC3 (BY2-AC3 judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-y-2.override-bound-to-message.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BY2-AC1,BY2-AC2,BY2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; each arm's expected and got; the binding as built; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a hash over a message other than the one committed (the arm commits and re-reads the landed message); a forged row passing (negative arm); the age window left as a second way in; BLIND: a seat with write access to the audit file can still write a correct row for its own message, which is the audited override itself.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round9.md @1bd6fcf3dd + ADDENDUM 1 (`1.0.0_SA_CTO~DELL1`, msgs 2050, 2088), item ADDENDUM 1 (2); decomposition round 10. Base dry-run at the cut, by the
issuer at base 9f252e010a: BY2-AC1 base: FAIL as expected (file absent); BY2-AC2 base: FAIL as expected (file absent; written by BF-y-1).
