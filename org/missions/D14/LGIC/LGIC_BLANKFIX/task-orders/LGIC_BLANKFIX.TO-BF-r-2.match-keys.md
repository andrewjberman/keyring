# TO LGIC_BLANKFIX.TO-BF-r-2 -- round 3 BF-r-2: the match keys -- an exception may carry its role; a legacy row matches on bucket and key

<to_id>LGIC_BLANKFIX.TO-BF-r-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-r-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round3.md`) | **outcome_ref:** FWD-1, FWD-4 |
**depends_on:** BF-r-1 merged; the two registry shapes landed by 4.0.0_SA_CRO; handed by AMENDMENT 1

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline` prints one line per name of
that root: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it
exits 1 while any line is a `HOLE`. Round 2's run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`: 140 names,
9 right, 113 fix, 9 not asked, 1 pattern, 6 carded, 2 refused, 0 holes. A seat that built none of it read that run and could act on
122 of the 140 lines from the line alone; its grade, with the 18 lines it could not act on, is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md` -- read it first. The modules are under `lib/`:
`opal_naming.py` (`grade`), `opal_naming_scope.py` (`root_items`, `root_table`, `contested`), `opal_naming_rootmap.py` (`load_map`,
`resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py` (`policy_roles`, `system_for`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read
the ones your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency. The bar for the library: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at
the base (194 passed); no test may fail after your build.

### THE CELL

`BF-r-2`. Two rulings of `1.0.0_SA_CTO` (`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`): (1) an inline policy takes its ROLE's
system; a root-map exception changes that only when the exception NAMES the owning role; an exception keyed (name, type) with no
role never overrides a role's answer. Round 2 built the opposite for three policies (row `LGIC_BLANKFIX-W2-S4`: a ruled exception
won over the role). (2) A legacy-address row is bucket-scoped and a key matches it on (bucket, key).

**THE SHAPES.** The registry's lane (`4.0.0_SA_CRO`) writes both shapes first: how a root-map exception carries its role, and how
a legacy row carries its bucket. Their exact field names are written into this order as AMENDMENT 1 before it is handed to you. If
this order reaches you with no AMENDMENT 1, stop and report.

**Build:**
1. `lib/opal_naming_rootmap.py`: `load_map` accepts the role field AMENDMENT 1 names on an exception; `resolve(map, root, name,
   type, role=None)` matches an exception that names a role only when `role` equals it, and reports in `basis` whether the
   exception matched with a role (`exception-with-role`) or without (`exception`).
2. `lib/opal_naming_rootcheck.py`: for an `IAM_POLICY` whose declaration `policy_roles(root)` knows, the system is the role's,
   unless `resolve(..., role=THAT-ROLE-NAME)` returns `basis` `exception-with-role`. An `exception` without a role does not
   override the role.
3. `lib/opal_naming_keyfill.py`: confirm on the shape AMENDMENT 1 names that a legacy match requires the row's bucket to equal
   the key's bucket (round 2 built this on the field `bucket`); change it only if the landed shape differs.
4. Extend the three modules' tests: the DIFFERENCE CONTROL for the role: the same policy with an exception that names its role
   takes the exception's system, and with the same exception WITHOUT a role takes the role's system.
5. A command `python lib/opal_naming_rootcheck.py keys ROOT --map PATH`: for every inline policy of the root, one line with the
   system printed, the role's system, the exception if any and which won; last line
   `ROOTCHECK-KEYS ok=True root=... policies=N role=N exception_with_role=N exception_without_role_overriding=0`.

### ACCEPTANCE

<criterion id="BR2-AC1" cell_refs="BF-r-2"><invocation>python lib/tests/test_opal_naming_rootmap.py</invocation><expect>ROOTMAP-TEST ok=True</expect></criterion>
`BR2-AC1` -- an exception overrides a role only when it names that role (the difference control).

<criterion id="BR2-AC2" cell_refs="BF-r-2"><invocation>python lib/opal_naming_rootcheck.py keys infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json</invocation><expect>exception_without_role_overriding=0</expect></criterion>
`BR2-AC2` -- on the real root no role-less exception overrides a role's system.

<expected_criteria>BR2-AC1,BR2-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootmap.py
lib/tests/test_opal_naming_rootmap.py
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
lib/opal_naming_keyfill.py
lib/tests/test_opal_naming_keyfill.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md</decomp_doc> (round 3), cell `BF-r-2`.
<owned_cells>BF-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BR2-AC1, BR2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-r-2.match-keys.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BR2-AC1,BR2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the three policies of row W2-S4 with what each printed before and prints now; the root run's last line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a role-less exception still winning by a path the test does not reach (AC2 counts it on the real root, zero required); an exception with a role matched on the wrong role (the difference control); a legacy match loosened while reading the new shape (the round-2 keyfill tests are kept); BLIND: policies attached outside Terraform.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @ef7133ec9a (the CTO's enrichment list); decomposition round 3. Base dry-run at the cut: BR2-AC1 base PASS as expected (ran: ROOTMAP-TEST ok=True assertions=15; extended by the cell); BR2-AC2 base FAIL as expected (ran: no such command).
