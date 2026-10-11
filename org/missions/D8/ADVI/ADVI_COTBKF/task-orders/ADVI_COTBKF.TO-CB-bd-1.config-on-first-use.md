# TO ADVI_COTBKF.TO-CB-bd-1.config-on-first-use -- round 56 CB-bd-1: the private sweeps config loads on first use, not at import

<to_id>ADVI_COTBKF.TO-CB-bd-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~83</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>56</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bd-1` (`decompositions/ADVI_COTBKF_DECOMP.round56.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** Counts, sha256
and reason codes only, in code, tests, your report, commit messages and rows. Do not open, print or copy the private config. Every
value in a test you write is SYNTHETIC (invented; never copied from the private config or any data file).

**The problem (row ADVI_COTBKF-D2-S83; CTO msg 4022, ruling (c)).** `data/assets/scripts/silver/commonwealth_sweeps.py` reads the
private config at IMPORT (`_REJECTED_RAW.update(... load_sweeps_config() ...)`, then `CANDIDATES_REJECTED` is built from it). Since
round 55 the path comes from `COTBKF_SWEEPS_CONFIG` alone, so without that variable every module that imports it fails at import and
the silver suite reads 20 collection errors.

**Your item.** No S3 write and no deploy.

1. **Tests alone first.** Add `data/assets/scripts/silver/tests/test_commonwealth_sweeps_lazy_config.py` and commit it ALONE first;
   report its red pytest line. It asserts:
   - in a SUBPROCESS with `COTBKF_SWEEPS_CONFIG` removed from the child environment and `data/assets/scripts/silver` as the working
     directory, `python -c "import commonwealth_sweeps"` exits 0;
   - in the same kind of subprocess, the first read of the rejected-candidate data (for example `commonwealth_sweeps.CANDIDATES_REJECTED`)
     exits non-zero with `SweepsConfigError` in stderr;
   - the sha256 check refuses SYNTHETIC bytes: a temp file with invented content, passed as the path, raises `SweepsConfigError`;
   - with the loader's result replaced by a synthetic dict (monkeypatch), the rejected-candidate data contains the synthetic entry
     and the static entries.
2. **Fix, in the one module.** The config is loaded on FIRST USE through ONE function, at most once per process.
   - `SWEEPS_CONFIG_SHA256`, the single pin, the `SweepsConfigError` class and its messages stay exactly as they are. No second sha,
     no test flag and no test path in product code.
   - Every public name importers use today stays importable and returns the same value once loaded (for example through a
     module-level `__getattr__`). You may NOT edit an importer; if an importer cannot work without an edit, that is the refusal
     clause.
3. **Tests that now need config behaviour with the variable unset** replace that one loader's result with a synthetic dict. Put a
   shared fixture in `data/assets/scripts/silver/tests/conftest.py` if more than one test needs it. Update
   `test_commonwealth_sweeps_config_env.py` (round 55) so its "refuses" arm asserts the refusal at FIRST USE, and its other arms stand.
4. **Control.** Run the SWEEP-REGRADE invocation of CB56bd1-AC3 BEFORE your fix (at your branch base) and AFTER it, saving both last
   lines under your deliverables folder. They must be byte-identical. Each run takes about 10 minutes: run it in the background and
   wait for it; do not cut it short.

### ACCEPTANCE

<criterion id="CB56bd1-AC1" cell_refs="CB-bd-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_commonwealth_sweeps_lazy_config.py data/assets/scripts/silver/tests/test_commonwealth_sweeps_config_env.py -q</invocation><expect>passed</expect></criterion>
`CB56bd1-AC1` -- import needs no file; first use without the variable gives the named error; the pin refuses synthetic bytes.

<criterion id="CB56bd1-AC2" cell_refs="CB-bd-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB56bd1-AC2` -- the silver suite collects and passes with the variable unset: 0 failed, 0 errors, and no test newly skipped (report
the skip count; it was 11 before this order).

<criterion id="CB56bd1-AC3" cell_refs="CB-bd-1"><invocation>COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --data-dir C:/dev/ajb_workspace/.scratch/advi_cotbkf/r28 --out .scratch/w83/rg_after</invocation><expect>SWEEP-REGRADE sweeps=2 rejected=517 double_drop_months=0 fixed=0 months_before=3678/293/78622 months_after=3678/293/78622 control_same=True regressions=0</expect></criterion>
`CB56bd1-AC3` -- with the real config the chain output is unchanged: the last line carries the expected text and is byte-identical to
your own before-run.

<expected_criteria>CB56bd1-AC1,CB56bd1-AC2,CB56bd1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** any `commonwealth_*.py` other than `commonwealth_sweeps.py`; `_cotbkf_acct_check.py`; the three id and manifest
  tests of rounds 53 to 55 other than the one named in step 3; `surprise-channel/` except your own NEW row; any other task order.
- **No S3 write.** No push. The SWEEP-REGRADE run reads local files only.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit and the fix is not an ordinary code correction inside
  your grant, stop and report its exact refusal line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W83-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken a test, and do not skip one.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round56.md</decomp_doc> (round 56), cell `CB-bd-1`.
<owned_cells>CB-bd-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB56bd1-AC1, CB56bd1-AC2, CB56bd1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~83/ADVI_COTBKF.TO-CB-bd-1.config-on-first-use.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB56bd1-AC1,CB56bd1-AC2,CB56bd1-AC3` BEFORE the flip. All three are
mechanical.
</proof_of_spec>

**REPORT (counts only):**
- the red pytest line of the tests-alone commit;
- the pytest lines of CB56bd1-AC1 and CB56bd1-AC2, with passed, failed, errors and skipped counts;
- the silver suite line WITH the variable set as well;
- both SWEEP-REGRADE last lines and whether they are byte-identical;
- which tests you changed and why, by file and count;
- commits, with the tests-alone commit first;
- every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one local module and its tests; row ADVI_COTBKF-D2-S84 is the read of who imports it: 11 hand-run scripts, 0 found in any Terraform, YAML or shell file.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- tests alone first, red at the base; both subprocess arms remove the variable from the child environment; the pin is exercised with synthetic bytes; the chain control is the SWEEP-REGRADE line before and after with the real config; BLIND: a script that reads the rejected data only on a rare branch now fails there rather than at import, later than before.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4022 (ruling (c)) answering issuer msg 4021; msg 4017 (withdrawn fixture ruling); rows ADVI_COTBKF-D2-S83 and D2-S84; round 55 drain @1f79a8182c.
