# TO NFRA_CTLPLN.TO-CT-w-5 -- round 8 CT-w-5: the intake route's install no longer defaults to a --user install into the box interpreter (row D1-S10)

<to_id>NFRA_CTLPLN.TO-CT-w-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~67</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-5` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`) | **outcome_ref:** FWD-15 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-15: one real package goes laptop -> Dell, checked, and the lane's work runs. Round 7's dell1 exercise (row D1-S10, `org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.receive.txt` step 1c) found that `org/devices/intake/intake_receive.py install` runs `pip install --user` for every wheel in the pack into `sys.executable`'s user site. On dell1 that would put click 8.3.1 over the click 8.5.0 that huggingface_hub needs (click>=8.4.2,<9.0.0), a downgrade. The receiving seat had to bypass the tool. You fix the tool.

### BUILD

In `org/devices/intake/intake_receive.py` (read `build_pip_command` at about line 297, `install_pack` at about line 515, the `install` sub-parser at about line 642, and the module docstring at lines 1-20):
1. `install --from <pack>` now REQUIRES exactly one install target, and refuses without one (exit 1, nothing installed, message `REFUSED: install needs a target: --python <interpreter> | --target <new dir> | --user`):
   - `--python <exe>`: build the pip command with that interpreter in place of `sys.executable` (`[<exe>, "-m", "pip", "install", "--no-index", "--no-deps", <wheel>]`, NO `--user`). The interpreter is typically a fresh venv's python. Refuse an `<exe>` that equals `sys.executable` unless `--user` is ALSO given (so the box interpreter is never touched by accident).
   - `--target <dir>`: `pip install --target <dir>` into a NEW or EMPTY folder (the existing non-user branch of `build_pip_command`).
   - `--user`: the old behaviour, kept only when asked for by name.
2. `build_pip_command` takes the interpreter as an argument (default `sys.executable`); the receipt written for each wheel records which target form was used (`install.target_form` = `python`, `target` or `user`) and, for `--python`, the interpreter path.
3. The module docstring's line 17 and the `--help` text say what each target does and that the old default is gone. The child environment, the no-index rule and every receipt gate stay exactly as they are.
4. `org/devices/intake/test_intake_receive.py`: update the cases that call `install` so they pass an explicit target, and add FIVE cases: (a) install with no target is refused and installs nothing; (b) `--python <a real venv python made in the test's temp folder>` installs the synthetic wheel into that venv and the box interpreter's site is untouched (list its `pip list` before and after, equal); (c) `--python sys.executable` without `--user` is refused; (d) `--target` into a new folder installs there; (e) `--user` still builds the old command (dry-run only, no real user install in the test). The test never installs into the machine's own user site.

### RULES FOR THIS CELL

Write surface is exactly the `<paths>`. Every pip command in your tests goes to a local wheel with `--no-index --no-deps`; no request leaves this machine; nothing is installed into the machine's own interpreter or user site. You run no terraform and no aws and push nothing. Use `.tools/safe-commit.sh`. Python 3.9-compatible; ruff clean; ASCII only. The law files CLAUDE.md and org/XXX.md are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W67-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw5-AC1" cell_refs="CT-w-5"><invocation>python org/devices/intake/test_intake_receive.py</invocation><expect>INTAKE-RECEIVE-TEST cases=30/30 ok=True</expect></criterion>
`CTw5-AC1` -- the 25 existing cases (adjusted) and your 5 new ones, 30 of 30.

<criterion id="CTw5-AC2" cell_refs="CT-w-5"><invocation>python org/devices/intake/intake_receive.py install --help</invocation><expect>--python</expect></criterion>
`CTw5-AC2` -- the install verb's help names the new target options.
</proof_of_spec>

<expected_criteria>CTw5-AC1,CTw5-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~67/NFRA_CTLPLN.TO-CT-w-5.intake-install-target-interpreter.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTw5-AC1,CTw5-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-5</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_receive.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- the box interpreter modified by a default (the old default is removed; refusal without a target; `--python sys.executable` refused); a test that installs into the machine's own user site (forbidden; the test uses a venv and a temp --target); a receipt that does not say where the wheel went (target_form recorded); BLIND: the installed state of a Dell's venv after a real run (the next dell1 exercise).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ROUND_ANALYSIS.round7.md`; row NFRA_CTLPLN-D1-S10; `TO-CT-v-3` receive.txt step 1c.
