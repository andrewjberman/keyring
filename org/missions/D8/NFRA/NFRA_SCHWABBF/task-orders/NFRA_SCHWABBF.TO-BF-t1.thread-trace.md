# TO NFRA_SCHWABBF.TO-BF-t1 -- thread hop 6: the trace -- one master and day, bronze at the builder's address, no second form, balances read

<to_id>NFRA_SCHWABBF.TO-BF-t1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~4</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-t-1` (`decompositions/NFRA_SCHWABBF_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-t-1`, FWD-1's DONE WHEN: "one trace: the oldest day pulled from Schwab, stored at the builder's address, converted the existing way, and the balances read." FWD-1 ACCEPT: "An analyst can say what that 0840 account held on its oldest day
without asking Schwab again, and the figure came from a file Opal pulled from Schwab, not from a stand-in."
This tool is the trace the issuer runs at release act R8, after the real pull. It asks the BUILDER where a day's files should be, so it cannot agree with the key function it is grading.

**What exists (read, never edit).** `lib/opal_naming.py` `address()`: for 08403355, `address('schwab','08403355','bronze','acc','date=2023-10-17')` is `s3://opal-data-assets/schwab/08403355/bronze/acc/date=2023-10-17`; the silver balance table is at
`address('schwab','08403355','silver','dim_balance','date=YYYY-MM-DD') + '/data.parquet'` (real example, measured 2026-10-20: `date=2026-10-16/data.parquet`, 15,807 bytes).
Today the stored bronze is still in the OLD layout `schwab/08403355/bronze/acc/YYYYMMDD/<name>` (real example: `acc/20261016/08403355.CRS20261016.ACC.zip`) until the issuer's cutover.

**Build `data/canonical/schwab/keyform/thread_trace.py`** (stdlib + boto3 + the parquet reader the repo's silver code already uses; do not add a dependency):
`python thread_trace.py --master M --day YYYY-MM-DD [--form builder|legacy|any]` (default `builder`). Prints one line per hop and a final verdict:
1. `HOP bronze: HELD n=<files> prefix=<the builder address>` when the builder's partition for the `acc` feed holds at least one object; `HOP bronze: NOT-HELD form=<builder|legacy>` otherwise. With `--form any` it looks in both layouts and prints which one held the file; `--form builder` looks only in the builder's.
2. `HOP second-form: NONE` or `HOP second-form: FOUND n=<k> prefix=<old-layout prefix>`: the old-layout partition `schwab/M/bronze/acc/YYYYMMDD/` for the same day. FWD-4: "never finds the same day stored two different ways". Under `--form builder` a found second form makes the verdict FAIL.
3. `HOP silver: READ rows=<n> table=dim_balance` after reading the day's `dim_balance` parquet, then `BALANCES` lines naming the real balance column(s) the file carries (discover them from the file; print column name, count of non-null, and the SUM of each numeric balance column; NEVER print account numbers or any row-level identifier).
4. Verdicts and exit codes: `THREAD-OK master=M day=D` rc 0 when bronze is held in the required form, no forbidden second form, and silver was read with rows > 0. `THREAD-FAIL reason=<...>` rc 1 when a hop that should be there is wrong.
   The typed absence is a different answer: when the day has no bronze in any layout and no silver, print `NOT-HELD master=M day=D cause=no-bronze-no-silver` and exit 2 -- an absence of a day is not a failure of the tool, and it must be distinguishable from one.
5. Injectable store so tests need no S3.

**Tests `data/canonical/schwab/tests/test_thread_trace.py`** (fake store): builder form held + silver rows -> `THREAD-OK` rc 0; legacy only under `--form builder` -> `THREAD-FAIL`; legacy only under `--form any` -> OK with the form named; both forms present under `--form builder` -> FAIL naming the second form;
no bronze and no silver -> `NOT-HELD ... cause=no-bronze-no-silver` rc 2; the printed lines contain no account number (feed a fake parquet with an account-number column and assert it never appears in the output).

### ACCEPTANCE

<criterion id="BF1-t1-AC1" cell_refs="BF-t-1"><invocation>python -m pytest data/canonical/schwab/tests/test_thread_trace.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-t1-AC1` -- the trace on a fake store: success, wrong form, second form, typed absence, and no identifier in the output.

<criterion id="BF1-t1-AC2" cell_refs="BF-t-1"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-16 --form any</invocation><expect>^THREAD-OK master=08403355 day=2026-10-16</expect></criterion>
`BF1-t1-AC2` -- the seam probe against the REAL neighbor: the real 0840 day 2026-10-16 (bronze still in the old layout, silver present) traces end to end under `--form any`.

<criterion id="BF1-t1-AC3" cell_refs="BF-t-1"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-17 --form any</invocation><expect>^NOT-HELD master=08403355 day=2026-10-17 cause=no-bronze-no-silver</expect></criterion>
`BF1-t1-AC3` -- the negative arm on a real Saturday (no bronze, no silver): the typed absence, not a failure and not a pass.

<expected_criteria>BF1-t1-AC1,BF1-t1-AC2,BF1-t1-AC3</expected_criteria>

Dry-run at the base 2026-10-20: AC1 "no tests ran" (rc 4); AC2 and AC3 "can't open file" (rc 2) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS calls are read-only list/get in AC2 and AC3. Nothing is written to S3. No deploy.
  If the real reads are refused (no read identity in your shell), stop on AC2/AC3, write a surprise row naming the refusal, and do not weaken the criteria.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/thread_trace.py
data/canonical/schwab/tests/test_thread_trace.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. (`data/canonical/schwab/keyform/__init__.py` is created by the worker of `TO-BF-m1` on another branch; run the tool by file path, as AC2 and AC3 do.)

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP.md</decomp_doc> (round 1), cell `BF-t-1`.
<owned_cells>BF-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-t1-AC1, BF1-t1-AC2, BF1-t1-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~4/NFRA_SCHWABBF.TO-BF-t1.thread-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-t1-AC1,BF1-t1-AC2,BF1-t1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the THREAD-OK and NOT-HELD lines, the balance column names found in the real `dim_balance` file (names only), the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell reads under the seat's own identity and adds no grant; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the oracle independence (asks the builder, not the function under test) is a design constraint in the face.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 FWD-1, FWD-4; decomposition round 1 cell BF-t-1; release act R8.
