# TO LGIC_BLANKFIX.TO-BF-s-8 -- round 5 BF-s-8: the proof checker reads a directory given as an artifact path as a refusal, not a traceback

<to_id>LGIC_BLANKFIX.TO-BF-s-8</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-s-8` (`decompositions/LGIC_BLANKFIX_DECOMP.round5.md`) | **outcome_ref:** the pipeline's own gate |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Two roots read with no hole and were graded by a seat that built none of the check (`bd-pipeline`, 142
names; `investor-reporting/directory`, 18). The run over all 13 roots the root map covers reads 412 names and 38 holes on 9
roots: the table is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/ALL_MAPPED_ROOTS_round4.txt` and each root's whole output is under
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/all_roots_round4/`. The CTO's reading is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`), `opal_naming_scope.py`, `opal_naming_rootmap.py`,
`opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`, the `crossfirm` command),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`, the `lines` and `keys` commands). The
registry is `infra/logic/registry/` (`root_map.json`, `key_rulings.json`, `event_rules.json`, `legacy_addresses.json`,
`resources.json`, `systems.json`); the map is `infra/logic/registry/root_map.json`. Read the modules your cell touches or calls before
you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no
AWS call and no network call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed)
and every `lib/tests/test_opal_naming_*.py` script prints `ok=True`; none may fail after your build. A test you write asserts
relations and the rows it needs by name, never a typed total of repository names or registry rows: those move every day.

### THE CELL

`BF-s-8`. Row `LGIC_BLANKFIX-S5`: a worker reported that `.tools/proof-of-spec-check.py` exits 2 with a `PermissionError` when a
proof-of-spec instance names a DIRECTORY as an artifact path. A checker's answer is `VALID` or a refusal with its reason; a
traceback is neither. The CTO put the fix in this round. The report was NOT reproduced by the issuer: reproduce it first.

1. **Reproduce.** In a temporary folder build the smallest instance and governing order the checker accepts (copy the shape of
   `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-q-6.every-mapped-root.proof_of_spec.json`
   and its order), with one artifact row whose path is a directory that exists. Run the checker; record rc and the last lines. If
   it does NOT crash, stop there: report what you ran and what it printed, file one row, and change nothing.
2. **Fix**, minimally, in `.tools/proof-of-spec-check.py`: an artifact path that is a directory is a violation with its reason
   ("artifact-resolution: PATH is a directory; name its files"), on every route that opens an artifact path; rc is the
   checker's ordinary refusal code, never 2 from an exception.
3. **Its own arms.** The checker has a `--self-test`; add one arm for the directory case and one control beside it (the same
   instance with the path naming a file validates). Run `python .tools/proof-of-spec-check.py --self-test` before and after:
   every arm that passed before must pass after; report both counts.
4. `.tools/tests/test_proof_checker_directory.py`, a plain script: the reproduction as a test, with the DIFFERENCE CONTROL.
   Last line `PROOF-DIR ok=True directory=refused file=valid crash=False`. With the argument `--self-test` the same script
   runs `python .tools/proof-of-spec-check.py --self-test`, reads its `RESULT: N of M arm(s) behaved` line, and prints
   `PROOF-SELFTEST ok=True arms=M behaved=N`; `ok=True` only when N equals M and M is at least 59 (57 at the cut plus your two).
This file is a gate every seat's commit runs. Change nothing else in it, and run `bash .tools/commit-gate.sh` on it.

### ACCEPTANCE

<criterion id="BS8-AC1" cell_refs="BF-s-8"><invocation>python .tools/tests/test_proof_checker_directory.py</invocation><expect>PROOF-DIR ok=True</expect></criterion>
`BS8-AC1` -- a directory path is refused with its reason and the same instance naming a file validates.

<criterion id="BS8-AC2" cell_refs="BF-s-8"><invocation>python .tools/tests/test_proof_checker_directory.py --self-test</invocation><expect>PROOF-SELFTEST ok=True</expect></criterion>
`BS8-AC2` -- the checker's own arms still pass.

<expected_criteria>BS8-AC1,BS8-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- You may NOT edit any other file under `.tools/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
.tools/proof-of-spec-check.py
.tools/tests/test_proof_checker_directory.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the saved tables and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round4.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round5.md</decomp_doc> (round 5), cell `BF-s-8`.
<owned_cells>BF-s-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BS8-AC1, BS8-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-s-8.proof-checker-directory.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BS8-AC1,BS8-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the reproduction's rc and output before the fix; the self-test's arm counts before and after; the diff stat; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a gate edit that breaks every commit on the fabric (the self-test before and after; commit-gate on the file; the issuer re-runs both at the merge); a fix that turns every unreadable path into a silent pass (the face says a violation with its reason); a crash that was never real (the face orders the reproduction first and a stop if it does not crash); BLIND: other unhandled path shapes (a symlink, a device) -- not asked.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round4.md @095d99c984 (the CTO's enrichment list); decomposition round 5. Base dry-run at the cut: BS8-AC1 base FAIL as expected (file absent); BS8-AC2 base FAIL as expected (file absent); beside it, ran at the cut: python .tools/proof-of-spec-check.py --self-test prints RESULT: 57 of 57 arm(s) behaved.
