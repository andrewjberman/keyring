# TO ADVI_COTBKF.TO-CB-bc-1.no-device-default -- round 55 CB-bc-1: the private sweeps config has no device default; manifest hash fields are asserted

<to_id>ADVI_COTBKF.TO-CB-bc-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~82</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>55</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bc-1` (`decompositions/ADVI_COTBKF_DECOMP.round55.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** Counts, sha256
and reason codes only, in code, tests, your report, commit messages and rows. Do not print the contents of the private config.

**Problem 1 (row ADVI_COTBKF-D2-S77; CTO round-54 analysis @0ac41554df, section 3).**
`data/assets/scripts/silver/commonwealth_sweeps.py` sets `SWEEPS_CONFIG_DEFAULT` to a path that exists on one box only, and loads the
config at import. Workspace code carries no device path.

**Problem 2 (row ADVI_COTBKF-D2-S80, the same analysis).** Nothing asserts that a tracked mint manifest still states its hashes.

**Your item.** No S3 write and no deploy.

1. **Tests alone first.** Commit these two new files ALONE first; report the red pytest line.
   - `data/assets/scripts/silver/tests/test_commonwealth_sweeps_config_env.py`. Each arm runs `python -c "import commonwealth_sweeps"`
     in a SUBPROCESS with `data/assets/scripts/silver` as its working directory, and asserts:
     - with `COTBKF_SWEEPS_CONFIG` removed from the child environment: a non-zero exit, and `SweepsConfigError` in stderr;
     - with `COTBKF_SWEEPS_CONFIG` passed through from the test's own environment: exit 0. This arm FAILS (it does not skip) when
       the variable is not set in the test's own environment;
     - the source text of `commonwealth_sweeps.py` contains neither `SWEEPS_CONFIG_DEFAULT` nor the string `C:/dev`.
   - `data/assets/scripts/silver/tests/test_cotbkf_manifest_hash_fields.py`. For every tracked `ard_*manifest.json` under
     `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/*/`: every value, at any depth, whose key contains `sha256` matches
     `[0-9a-f]{64}` in full. It prints `DENOMINATOR manifests=<m> sha_fields=<n> not_64_hex=<k>` and fails when `m` is 0 or `k` is
     not 0. This test passes already at the base; the first one is the red one.
2. **Fix, in one place.** In `commonwealth_sweeps.py`: delete `SWEEPS_CONFIG_DEFAULT`; `load_sweeps_config(path=None)` takes the path
   from its argument, else from `COTBKF_SWEEPS_CONFIG`; when neither gives a path it raises `SweepsConfigError` naming the variable.
   The sha256 check, the pinned constant and the import-time load stay exactly as they are.
3. **Census the importers.** Count the tracked `.py` files that import `commonwealth_sweeps` (use the Grep tool, pattern
   `commonwealth_sweeps`, glob `*.py`), and report the count and how many are outside `data/assets/scripts/silver/`. Do not edit
   them.
4. **Run** the three acceptance invocations below, exactly as written, from the worktree root in Git Bash.

**Where a second box gets the file.** The config exists on dell2 only, at `C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` (sha256 pinned in the module as
`SWEEPS_CONFIG_SHA256`). It never enters the repo or S3. A second box receives a copy from `0.0.0_AB_MSTR~DELL2` over the box-to-box
file route, places it outside its checkout, and sets `COTBKF_SWEEPS_CONFIG` to that path. Put this paragraph, without the dell2 path,
into the docstring of `load_sweeps_config`.

### ACCEPTANCE

<criterion id="CB55bc1-AC1" cell_refs="CB-bc-1"><invocation>COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json python -m pytest data/assets/scripts/silver/tests/test_commonwealth_sweeps_config_env.py -q</invocation><expect>passed</expect></criterion>
`CB55bc1-AC1` -- the module refuses to import without the variable, imports with it, and carries no device path.

<criterion id="CB55bc1-AC2" cell_refs="CB-bc-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_manifest_hash_fields.py -q -s</invocation><expect>not_64_hex=0</expect></criterion>
`CB55bc1-AC2` -- every sha256-named field of every tracked mint manifest is 64 lower-case hex, with the denominator printed.

<criterion id="CB55bc1-AC3" cell_refs="CB-bc-1"><invocation>COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB55bc1-AC3` -- the silver suite passes with the variable set, 0 failed.

<expected_criteria>CB55bc1-AC1,CB55bc1-AC2,CB55bc1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** any other module or test, `_cotbkf_acct_check.py`, `surprise-channel/` except your own NEW row, any other task
  order.
- **No S3 write.** No push.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W82-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken a test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps_config_env.py
data/assets/scripts/silver/tests/test_cotbkf_manifest_hash_fields.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round55.md</decomp_doc> (round 55), cell `CB-bc-1`.
<owned_cells>CB-bc-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB55bc1-AC1, CB55bc1-AC2, CB55bc1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~82/ADVI_COTBKF.TO-CB-bc-1.no-device-default.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB55bc1-AC1,CB55bc1-AC2,CB55bc1-AC3` BEFORE the flip. All three are
mechanical.
</proof_of_spec>

**REPORT (counts only):**
- the red pytest line of the tests-alone commit, and the three acceptance pytest lines with the DENOMINATOR line of AC2;
- the importer census: tracked `.py` files importing the module, and how many sit outside `data/assets/scripts/silver/`;
- the silver suite line WITHOUT the variable set (expected to fail at collection; report the counts, do not fix);
- commits, with the tests-alone commit first;
- every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local module default and two local tests; the importer census in the order is the read of who loads the module, and no scheduled producer was found to import it by row D2-S77 (not checked there, so the census is reported, not assumed).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- tests alone first, red at the base; the negative arm runs in a subprocess with the variable removed; the positive arm fails, never skips, when the variable is unset; the sha256 pin is untouched; BLIND: a runner that imports the module without the variable now fails at import by design, and the importer census is the only read of who that is.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-54 analysis @0ac41554df (msg 3985), sections 3 and 4; rows ADVI_COTBKF-D2-S77 and D2-S80; `3.0.0_SA_CVO` REMEDIATION_v34 @3cbc307fd3.
