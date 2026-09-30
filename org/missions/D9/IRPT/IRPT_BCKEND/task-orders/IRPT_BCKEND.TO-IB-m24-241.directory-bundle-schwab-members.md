# TO IRPT_BCKEND.TO-IB-m24-241 -- the directory bundle ships schwab_account_codes (row S217)

<to_id>IRPT_BCKEND.TO-IB-m24-241</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~82</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-241`
(`decompositions/IRPT_BCKEND_DECOMP_R24_M.md`) | **outcome_ref:** FWD-2 (the directory) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-241` -- row `IRPT_BCKEND-S217`. The directory bundle `investor-reporting.tar.gz` (key
`code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` in bucket `opal-data-mdpf`) is built from the
`investor_reporting` entry in `.tools/safe_deploy_core.py` (members dict near lines 285-372). That entry lists a fixed
set of 10 files. `data/assets/scripts/gold/investor_reporting/directory_runner.py` at CLOUD imports
`schwab_account_codes` at MODULE level (line ~121, `import schwab_account_codes as _sac`, added by IB-mr-213 UIC-16).
`schwab_account_codes.py` (which reads `schwab_account_codes.json` beside it) is NOT a member, so a bundle built as
defined raises ImportError on every directory fire. The Holdings packages already carry both files
(`_IRPT_HOLDINGS_CLOSURE`, same file) -- only the directory bundle is short.

**Build (LOCAL -- no upload, no mint):**
1. Add two members to the `investor_reporting` bundle's `members` in `.tools/safe_deploy_core.py`:
   `data/assets/scripts/gold/investor_reporting/schwab_account_codes.py` and
   `data/assets/scripts/gold/investor_reporting/schwab_account_codes.json`, each with `repo_path` equal to its key and
   its own `sha_metadata_key` (follow the naming of the neighbouring members, e.g. `schwab-account-codes-sha256` and
   `schwab-account-codes-json-sha256`). Update the closure comment above the entry to name them and why (the runner's
   module-level import; row S217). Change nothing else in the entry.
2. Read `schwab_account_codes.py` whole: if it reads its JSON by a path relative to its own file (e.g.
   `os.path.dirname(__file__)`), the bundle layout (members stored at their repo paths) keeps the two side by side --
   confirm that in the extracted tree. If it reads by any other path, stop with a row.
3. Run the check below. Also run `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q -p no:cacheprovider`
   and `python -m py_compile .tools/safe_deploy_core.py` and report both lines (drain hygiene, not criteria).

### ACCEPTANCE

<criterion id="IBM24-241-AC1" cell_refs="IB-mr-241"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R24_CHECKS/r24_directory_bundle_imports.py</invocation><expect>BUNDLE-IMPORTS</expect></criterion>
`IBM24-241-AC1` -- a locally built bundle carries every module directory_runner.py imports at load, and `import
directory_runner` succeeds from the extracted tree alone.

<expected_criteria>IBM24-241-AC1</expected_criteria>

Dry-run at the base 2026-09-29 18:1xZ: NOT-IMPORTABLE: module-level sibling imports not in the bundle:
['schwab_account_codes'] -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** No upload, no `--mint-bundle`, no push. The bundle ships at 0.0.0_AB_MSTR's push, after the drain.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W82-S<k>`), and do not weaken the test to pass.

<paths>
.tools/safe_deploy_core.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R24_M.md</decomp_doc> (round 24, workstream ~M), cell `IB-mr-241`.
<owned_cells>IB-mr-241</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM24-241-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~82/IRPT_BCKEND.TO-IB-m24-241.directory-bundle-schwab-members.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM24-241-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two member entries as written, the check line, the suite and py_compile lines, the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched; the directory schedule already fires the bundle once shipped.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change.
comp-adversary: RUN -- 1 live bundle read (ETag 4155283a, 10 members) and 2 module-level import sweeps (live vs CLOUD directory_runner.py and holdings_snapshot.py): the only NEW load-time import missing is schwab_account_codes; holdings_snapshot.py's five sibling imports are identical in the live bundle (not new); BLIND: how schwab_account_codes.py resolves its JSON path is unread at the cut (step 2 reads it).
lane: the <paths> block IS the grant; ~M owns the directory runner's gold side and cut the import.
</preflight>

Source: row IRPT_BCKEND-S217 (@43aa2951dc); CTO 102945.
