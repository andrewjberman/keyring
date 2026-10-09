# TO LGIC_ENFORCE.TO-EN-aa-1 -- round 21 EN-aa-1: row Z-S1: a required registry that is missing fails the run closed
<to_id>LGIC_ENFORCE.TO-EN-aa-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-aa-1` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0v) | **outcome_ref:** FWD-5 |
**depends_on:** none (slot ~1)

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

`EN-aa-1` (row `LGIC_ENFORCE-Z-S1`, ruled in the analysis section 2: "`lib/opal_lgctfm.py` `read_text()` (:198-202) returns
`""` for a MISSING file, so in a sparse worktree with no `LEGACY_SERVED_PATHS.json` every graded literal changes verdict silently ...
DEC-6 says 'a missing input fails closed', and this fails OPEN"). `read_json()` returns `None` the same way.

**Build** in `lib/opal_lgctfm.py` (and its test `lib/tests/test_opal_lgctfm.py`):
1. A read of a REQUIRED registry -- `scopes.json`, `remediations.json`, `LEGACY_SERVED_PATHS.json` -- raises when the file is absent,
   with the message `MISSING INPUT <repo-relative path>`. Optional reads elsewhere keep their behaviour.
2. `walk` (and every subcommand that reads them) checks the three required registries BEFORE any discovery or row, prints the
   `MISSING INPUT` line, and exits non-zero having written no contract or verdict rows.
3. A test arm for each of the three files: absent -> the raise and its message; present -> unchanged.

### ACCEPTANCE

<criterion id="AA1R21-AC1" cell_refs="EN-aa-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py failclosed</invocation><expect>PASS-R21-FAILCLOSED</expect></criterion>
`AA1R21-AC1` -- in a sparse worktree without LEGACY_SERVED_PATHS.json the walk exits non-zero, prints MISSING INPUT naming it, writes no contract; the same walk in the full checkout completes.

<criterion id="AA1R21-AC2" cell_refs="EN-aa-1"><invocation>timeout 1500 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r21/check_en_r21.py unit</invocation><expect>PASS-R21-UNIT</expect></criterion>
`AA1R21-AC2` -- the engine's own test, with the new arms, holds.

<expected_criteria>AA1R21-AC1, AA1R21-AC2</expected_criteria>

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
lib/opal_lgctfm.py
lib/tests/test_opal_lgctfm.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/registries.r21.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-aa-1.registries-fail-closed.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-aa-1.registries-fail-closed.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.21, round-21 cell `EN-aa-1` (section 0v).
<owned_cells>EN-aa-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AA1R21-AC1, AA1R21-AC2. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-aa-1.registries-fail-closed.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AA1R21-AC1,AA1R21-AC2 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-aa-1.registries-fail-closed.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** the sparse and full runs' exit codes and last lines; which subcommands now check the three registries first; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant; the walk only reads the live plane.
comp-adversary: RUN -- the cheapest pass is a raise that fires only for LEGACY_SERVED_PATHS.json, or a check placed after discovery so rows are written first: the arm requires no contract.json in the sparse run, and AC2's test arms cover all three files. Breaking the full run: the arm runs the real full walk to rc 0. BLIND: the arm exercises one missing file in a real sparse tree; the other two are proved by the test arms only.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/ROUND_ANALYSIS.round20.md` section 3 (`1.0.0_SA_CTO~DELL1`, msg 2861); decomposition section 0v. Base dry-run at the cut, by the issuer at
base 4ca1f1092e: AA1R21-AC1 base: FAIL as expected (the sparse walk exits 1 on an unrelated missing input -- org/modules/graph for comp-iam -- and prints no MISSING INPUT; at the base the three registry reads return empty silently, so only a check placed BEFORE discovery can pass). AA1R21-AC2 base: PASS as expected (unit: 4 passed). The arm's temporary sparse worktree is removed after each run (0 left).
