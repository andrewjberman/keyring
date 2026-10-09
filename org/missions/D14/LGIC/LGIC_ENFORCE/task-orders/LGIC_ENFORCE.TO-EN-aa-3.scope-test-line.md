# TO LGIC_ENFORCE.TO-EN-aa-3 -- round 21 EN-aa-3: the naming scope test reads the generated role's json line instead of a typed line number
<to_id>LGIC_ENFORCE.TO-EN-aa-3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-aa-3` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0v) | **outcome_ref:** FWD-5 |
**depends_on:** none (slot ~3)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_ENFORCE's seven outcomes are all REALIZED (FWD-5 at round 20). The CTO's round-20 analysis
(`org/missions/D14/LGIC/LGIC_ENFORCE/ledger/ROUND_ANALYSIS.round20.md`) keeps the project open for two gate holes measured on its own mechanism, plus one red test, and names round 21's three
items. When both holes are closed and graded, the round-21 analysis is the close read.

**The instruments.** `lib/opal_lgctfm.py` is the legacy-transform engine (`walk`, `forks`, `plan`, `run`); `walk` reads three
registries: `infra/logic/registry/scopes.json`, `infra/logic/registry/remediations.json` and
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`. A full `walk --subject cottonwood --seed
opal-data-assets/cottonwood/ --out <dir>` takes about 2.5 minutes at the base and reads the live plane through `comp-find`. The commit
gate is `.tools/naming-gate.py` (`--diff FILE`, `--self-test`), called by `.tools/safe-commit.sh`; it asks
`lib/opal_naming_rootcheck.py place(name, typ, root)` for a name in a mapped root (kinds RIGHT, FIX, NOT-ASKED, PATTERN, CARDED,
REFUSED, HOLE). The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. The switch file
`org/mcp/naming-place.enforce` is PRESENT and no cell touches it. Python 3.9 syntax, ASCII only, no new dependency. The bar:
`python -m pytest lib/tests -q -p no:cacheprovider` (193 passed, 1 skipped at the base) and `.tools/naming-gate.py --self-test`
(PASS) must not newly fail. The checks are `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py` (read-only; read it before you build -- each arm states what it runs).

**Client-data bound (0.0.0_AB_MSTR msgs 2712, 2739, 2758, 2796).** Search ONLY inside paths you name (lib/, .tools/, infra/,
org/missions/D14/LGIC/), never the whole repo and never in history. Never open, search, copy or git show anything under
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/, any org/**/W73_S*_EVIDENCE.json, or any cottonwood manifest.

### THE CELL

`EN-aa-3` (row `LGIC_ENFORCE-D1-S2`; analysis section 2: "`lib/tests/test_opal_naming_scope.py` reads `ok=False` on the
trunk (one `etfs-rivalfunds` failure); round 21 fixes it or names its owner"). Measured by the issuer: the test's named case
(:350-352) asserts `etfs-rivalfunds-daily-role` is counted at `generated.auto.tfvars.json:11`; ETFS_RIVALS' generator moved it to
line 13 (86c14e4b3a), and `root_extra()` reports `:13` correctly. The reader is right; the test typed a line number.

**Build** in `lib/tests/test_opal_naming_scope.py` only: the named case derives the expected line from the file itself (the line
of `infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json` holding that role name) and keeps asserting the name is
counted at its json line. Change no other assertion and no reader.

### ACCEPTANCE

<criterion id="AA3R21-AC1" cell_refs="EN-aa-3"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py scope</invocation><expect>PASS-R21-SCOPE</expect></criterion>
`AA3R21-AC1` -- the scope test reads SCOPE-TEST ok=True.

<expected_criteria>AA3R21-AC1</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** No AWS write, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` and `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py` are never edited.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W<n>-S<k>`, `<n>` your slot, `<k>` one above the highest in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing) in `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never weaken a check or an expected value. A fact in this
  order the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/tests/test_opal_naming_scope.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/scope.r21.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-aa-3.scope-test-line.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-aa-3.scope-test-line.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.21, round-21 cell `EN-aa-3` (section 0v).
<owned_cells>EN-aa-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AA3R21-AC1. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-aa-3.scope-test-line.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AA3R21-AC1 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-aa-3.scope-test-line.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** the old and new assertion; the test's last line; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- the cheapest pass deletes the named case or retypes 11 as 13: the order requires the line derived from the file, and the drain reads the diff. BLIND: the arm reads ok=True; whether the case still discriminates is the drain's diff read.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/ROUND_ANALYSIS.round20.md` section 3 (`1.0.0_SA_CTO~DELL1`, msg 2861); decomposition section 0v. Base dry-run at the cut, by the issuer at
base 4ca1f1092e: AA3R21-AC1 base: FAIL as expected (SCOPE-TEST ok=False assertions=826, the etfs-rivalfunds :11 case; 3 min run).
