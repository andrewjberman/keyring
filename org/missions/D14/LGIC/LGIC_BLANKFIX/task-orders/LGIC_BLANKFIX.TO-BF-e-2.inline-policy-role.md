# TO LGIC_BLANKFIX.TO-BF-e-2 -- round 2 BF-e-2: an inline policy takes its role's system -- keyed on the policy, its type and its role

<to_id>LGIC_BLANKFIX.TO-BF-e-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-2` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** Round 1 built one command: `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline`
prints one line per name of that root, each of kind `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED` or `HOLE`, and exits 1 while any
line is a `HOLE`. Its last run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`: 140 names, 10 right, 101 fix,
6 not asked, 1 pattern, 6 carded, 16 holes. The modules, all under `lib/`: `opal_naming.py` (`grade(name, type) -> (verdict,
canonical)`, `census_repo()`, `census_tf_names()`), `opal_naming_scope.py` (`root_items(root)`), `opal_naming_rootmap.py`
(`load_map`, `resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py` (`word_for`, `cadences`),
`opal_naming_keyfill.py` (`fill_keys`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read the ones your cell touches or
calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new
dependency. The bar for the library's own suite: `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider` fails six
named tests at the base (see `lib/tests/test_opal_naming_fourth_verdict.py` for the list); no test that passes at the base may fail.

### THE CELL

`BF-e-2`. Six lines of the round-1 run are `HOLE` with the detail "an inline policy takes its role's system; the root map does not
decide it": `pipeline-chain` (`iam.tf:256` and `:614`), `runner-shared-read` (`:496`), `gold-layer-trigger` (`:596`),
`events-emit` (`:683`), `cloudfront-invalidate` (`:713`). An inline policy (`aws_iam_role_policy`) belongs to the role it
attaches to. Two policies of this root share the name `s3-access` on different roles (`iam.tf:363`, `:855`), so a key of
(name, type) cannot hold the answer: the key is (name, type, parent role).

**Build** `lib/opal_naming_policyrole.py` (a new module):
1. `policy_roles(root) -> list[dict]`: one dict per `aws_iam_role_policy` resource block in the root's `.tf` files, with `name`
   (the policy's `name` literal), `where` (the same `file:line` `opal_naming.census_tf_names()` reports for that name), `role_ref`
   (the `role = ...` expression as written), `role_name` (the role's own `name` literal, resolved by following a reference of the
   form `aws_iam_role.X.name` or `.id` to resource `aws_iam_role` `X` in the root; `None` when the reference is anything else),
   `role_system` and `basis`. `role_system` is the system slot of the role's graded canonical form
   (`opal_naming.grade(role_name, "IAM_ROLE")`, the first hyphen-separated token of the canonical when it is not a blank);
   `None` with a plain-words `basis` when the role cannot be resolved, raises, or its own canonical carries a `{system}` blank.
2. `system_for(root, name, where) -> dict | None`: the row for that declaration, matched on (`name`, `where`).
3. Command line: `python lib/opal_naming_policyrole.py root ROOT` prints one line per inline policy and a last line
   `POLICYROLE-ROOT ok=True root=... policies=N resolved=N unresolved=N`; `ok=True` when `policies` equals the count of
   `aws_iam_role_policy` blocks found independently by a plain text count of that resource header in the root's files, and
   `resolved + unresolved == policies`.

**Build** `lib/tests/test_opal_naming_policyrole.py`, a plain script on small `.tf` text it writes to a temporary root-shaped
folder: a policy on a role whose name grades to a system gives that system; the DIFFERENCE CONTROL: two policies with the SAME
name on two roles of DIFFERENT systems give two different answers; a `role` that is a variable gives `None` with its basis. And
on the real root: the two `s3-access` declarations resolve to different roles. Last line `POLICYROLE-TEST ok=True assertions=N`.

You do not edit `lib/opal_naming_rootcheck.py`: cell `BF-e-8` wires `system_for` into the run.

### ACCEPTANCE

<criterion id="BE2-AC1" cell_refs="BF-e-2"><invocation>python lib/tests/test_opal_naming_policyrole.py</invocation><expect>POLICYROLE-TEST ok=True</expect></criterion>
`BE2-AC1` -- a policy takes its role's system, and the same name on two roles gives two answers.

<criterion id="BE2-AC2" cell_refs="BF-e-2"><invocation>python lib/opal_naming_policyrole.py root infra/aws/terraform/bd-pipeline</invocation><expect>POLICYROLE-ROOT ok=True</expect></criterion>
`BE2-AC2` -- every inline policy of the real root is read, the count checked against an independent text count.

<expected_criteria>BE2-AC1,BE2-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_policyrole.py
lib/tests/test_opal_naming_policyrole.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-2`.
<owned_cells>BF-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE2-AC1, BE2-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-e-2.inline-policy-role.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE2-AC1,BE2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; for each of the six hole names and both `s3-access` declarations: the role and the system; every unresolved policy with its basis; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a policy given the wrong role's system because two share a name (the key carries the declaration's where; the difference control is two same-named policies); a role resolved by guessing from the policy's name (only an explicit reference is followed); BLIND: policies attached outside Terraform.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE2-AC1 base FAIL as expected (file absent); BE2-AC2 base FAIL as expected (file absent).
