# TO ADVI_COTBKF.TO-CB-bf-1.bond-day-guard -- round 58 CB-bf-1: the mint re-reads the bond count on the exact files, and the build refuses to measure a bond-holding day under method_version 3

<to_id>ADVI_COTBKF.TO-CB-bf-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~85</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>58</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bf-1` (`decompositions/ADVI_COTBKF_DECOMP.round58.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** Counts, sha256,
bond CUSIPs and reason codes only, in code, tests, your report, commit messages and rows. Every value in a test is SYNTHETIC.

**Why (CTO msg 4131; round 57 record `deliverables/0.9.0_WK_ADVI_COTBKF~84/BOND_ACCRUAL_MEASURE.md` -- read it first).** The stored
bond close carries accrued interest, so the method stamped on Cottonwood's measured rows (`method_version` 3) states an income basis
that is false for a bond priced from that store. Today no measured account-day holds a bond, because bonds are unpriced. Nothing
forbids it tomorrow. Two things must be in the code before the mint:

**Your item, all in `data/assets/scripts/silver/commonwealth_account_return_daily.py`.** No S3 write, no deploy; do NOT run `--apply`.

1. **A count over the exact files of a manifest.** Add a mode `--bond-check --manifest <manifest> [--days-dir <dir>]`:
   - it reads the day files the manifest lists (from `--days-dir`, default the adapter's own scratch) after re-hashing each against
     the manifest's `sha256`, and refuses a file that differs;
   - a MEASURED row is one whose return is present (`return_basis` `TWR`); a BOND-HOLDING account-day is one where the account holds
     at least one CUSIP whose silver `Asset_Type` is `Fixed Income` (the rule round 57 used, `commonwealth_transactions.py:53`);
     state in a comment, with the source, where the holdings of an account-day are read from;
   - it prints exactly one last line:
     `ARD-COTTONWOOD-BOND-CHECK days=<d> rows=<r> measured_rows=<m> measured_rows_on_bond_days=<k> fixed_income_cusips=<n>`;
   - it exits 0 only when `k` is 0.
2. **The mint runs the same count first.** `apply_days` calls it on the manifest it was given, before any write, prints the same
   line, and refuses the whole run (a named error, nothing written) when `k` is not 0.
3. **The build guard.** In `build`, a row that would be emitted as MEASURED on a bond-holding account-day while the entry's
   `method_version` is 3 is refused with a named error class `BondDayMeasuredError` that says how many such rows and on how many
   days. It does not silently blank them: a bond day that becomes priced needs a new method row, and that is another project's
   decision.
4. **Tests alone first.** Add `data/assets/scripts/silver/tests/test_commonwealth_ard_bond_guard.py` and commit it ALONE first;
   report its red line. With synthetic frames and a faked S3 it asserts: the count is 0 on a set with no bond day and exits 0; the
   count is non-zero on a set with one measured bond day and the mode exits non-zero; `apply_days` on that set raises and makes zero
   S3 calls; `build`'s guard raises `BondDayMeasuredError` on a measured bond day under `method_version` 3 and does not raise when
   the bond day is blank.

**Inputs.** The real day files are in the BASE checkout, read-only for you: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47` (3,325 day directories). Round 57's analysis
scripts are still in this worktree at `.scratch/w84/` if you want to see how the holdings of an account-day were read; do not commit
them. Any commonwealth script you run needs the variable in its command line (see the invocations below).

### ACCEPTANCE

<criterion id="CB58bf1-AC1" cell_refs="CB-bf-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_commonwealth_ard_bond_guard.py -q</invocation><expect>passed</expect></criterion>
`CB58bf1-AC1` -- the count, the mint's refusal and the build guard behave as step 4 lists, 0 failed, 0 skipped.

<criterion id="CB58bf1-AC2" cell_refs="CB-bf-1"><invocation>COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json python data/assets/scripts/silver/commonwealth_account_return_daily.py --bond-check --manifest org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json --days-dir C:/dev/ajb_workspace/.scratch/advi_cotbkf/ard_cottonwood_r47</invocation><expect>ARD-COTTONWOOD-BOND-CHECK days=3325 rows=1691729 measured_rows=107316 measured_rows_on_bond_days=0</expect></criterion>
`CB58bf1-AC2` -- on the exact 3,325 files the mint will land, 0 measured rows sit on a bond-holding day, with all three
denominators printed. If your count of rows or measured rows differs from 1,691,729 or 107,316, do not adjust anything: that is the
refusal clause.

<criterion id="CB58bf1-AC3" cell_refs="CB-bf-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB58bf1-AC3` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before this order.

<expected_criteria>CB58bf1-AC1,CB58bf1-AC2,CB58bf1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** any other product file (in particular nothing under `data/assets/scripts/gold/`, which is IRPT_DASHBD's), any
  other test, any manifest, anything under `C:/dev/ajb_workspace/` (read only), `surprise-channel/` except your own NEW row.
- **Do NOT run `--apply` or `--verify-served`.** No AWS or S3 call of any kind; tests fake S3. No push.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit and the fix is not an ordinary code correction inside
  your grant, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. Print counts, never an account id or an
  account's value.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W85-S<k>`, `"fabric": "dell2"`, carrying no account id). Do not weaken a test.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/test_commonwealth_ard_bond_guard.py
data/assets/scripts/silver/tests/conftest.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round58.md</decomp_doc> (round 58), cell `CB-bf-1`.
<owned_cells>CB-bf-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB58bf1-AC1, CB58bf1-AC2, CB58bf1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~85/ADVI_COTBKF.TO-CB-bf-1.bond-day-guard.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB58bf1-AC1,CB58bf1-AC2,CB58bf1-AC3` BEFORE the flip. All three are
mechanical.
</proof_of_spec>

**REPORT (counts only):**
- the red pytest line of the test-alone commit; the three acceptance lines, with the full `ARD-COTTONWOOD-BOND-CHECK` line;
- where the holdings of an account-day are read from, with file and line, and how long the real count took;
- how the mint's refusal and the build guard are wired, in two sentences;
- commits, with the test-alone commit first; every gate refusal, verbatim; anything you could not run or verify.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and a new test; row ADVI_COTBKF-D2-S84 is the read of who runs it, nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the apply path gains a refusal and is not run.
comp-adversary: RUN -- the test alone first, red at the base; the count re-hashes each file against the manifest before reading it, so it counts the files the mint lands; the mint's refusal is tested with zero S3 calls asserted; the guard has a negative arm (a blank bond day does not raise); BLIND: a bond whose silver Asset_Type is not 'Fixed Income' (bond funds, mislabelled rows) is outside the rule, as it was in round 57.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4131 (two conditions) answering issuer msg 4129; round 57 packet @6edfe081c7 and record `deliverables/0.9.0_WK_ADVI_COTBKF~84/BOND_ACCRUAL_MEASURE.json`; row ADVI_COTBKF-D2-W84-S1.
