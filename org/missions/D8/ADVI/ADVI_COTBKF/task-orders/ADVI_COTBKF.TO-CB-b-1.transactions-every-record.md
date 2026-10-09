# TO ADVI_COTBKF.TO-CB-b-1 -- round 2 CB-b-1: the transactions converter keeps EVERY delivered record (no de-duplication) and numbers each one

<to_id>ADVI_COTBKF.TO-CB-b-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~4</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-b-1` (`decompositions/ADVI_COTBKF_DECOMP.round2.md`) | **outcome_ref:** FWD-1,
FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-b-1`, the round-2 remediation. Round 1's converter `data/assets/scripts/silver/commonwealth_transactions.py` dropped 1,360 records
that are exact repeats of another record. The CTO ruled (PRD v0.4, C-SILVER): with no transaction id, two identical records may be two
real events (two equal reinvestments on one day), so EVERY delivered record is kept, and each row carries its source record number.
You change the converter and prove it on the real file into a LOCAL directory. You write NOTHING to S3: `--apply` is the issuer's act.

**Read the current script and its tests first** (both at your worktree's HEAD; they were written in round 1 by another worker). Keep
everything that is not named below: the CLI, the typing, the lineage columns, the partitioning, the self-verify, the `--apply` refusals.

**The input, measured.** `$HOME/Downloads/Files.zip` (READ ONLY) holds
`Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip`; its member
`CFN_SCTASK0548380_Portfolio_Accounting_Performance/CFN_SCTASK0548380_Historical_Transactions_20260623_102751.txt` holds 1,416,497
records (a `csv.reader(delimiter='|')` parse: every record 20 fields) on 1,416,500 physical lines -- three records of account acct#1059baa6
each span two lines (156036+156037, 156038+156039, 156040+156041) through a CRLF inside a quoted `Transaction_Note`. 1,360 records are
exact repeats of an earlier record. 1,533 accounts; trade dates 2013-04-03 to 2026-06-22.

**Change:**
1. Remove the de-duplication: every record is one row. Two identical records are two rows with different `source_line`.
2. Add the lineage column `source_record` (int64): the 1-based ordinal of the record in the file, header excluded. Column order: the 20
   vendor columns, then `source_zip`, `source_zip_sha256`, `source_file`, `source_line`, `source_record` (25 columns).
   `(source_file, source_record)` is unique.
3. Count the file's records independently of the row build (a `csv.reader` pass over the same bytes) and REFUSE to write (rc 4, nothing
   written) when the table's rows differ from it.
4. Keep the field `dropped_dup=` in the last line (it must read 0) and APPEND two fields, so the LAST line is exactly:
   `SILVER-TRANSACTIONS lines=<physical> rows_out=<n> dropped_dup=<k> blank=<b> unexplained=<u> accounts=<a> columns=<c> min_trade=<d> max_trade=<d> lineage_sample=<ok>/<n> records=<r> rows_eq_records=<True|False>`.
5. Tests in `data/assets/scripts/silver/tests/test_commonwealth_transactions.py`: update round 1's duplicate test (a repeat is now KEPT, two
   rows, two `source_line` values), and ADD tests whose names contain `keeps_every_record` or `source_record`: two identical records in
   the fixture give two rows; `source_record` runs 1..N with a multi-line record counted once; the rows-vs-records refusal (rc 4, nothing
   written) when the build is forced short (difference control). Every test in the file passes.

### ACCEPTANCE

<criterion id="CB2b1-AC1" cell_refs="CB-b-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_transactions.py -k "keeps_every_record or source_record"</invocation><expect>passed</expect></criterion>
`CB2b1-AC1` -- the new behaviour on a fixture: repeats kept, `source_record` numbering, the rows-vs-records refusal. (The whole file must also
pass; report its line.)

<criterion id="CB2b1-AC2" cell_refs="CB-b-1"><invocation>python data/assets/scripts/silver/commonwealth_transactions.py --source "$HOME/Downloads/Files.zip" --outer-member "Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip" --data-date 2026-06-23 --out .scratch/advi_cotbkf/silver_r2 --verify-sample 50</invocation><expect>rows_out=1416497 dropped_dup=0 blank=0 unexplained=0 accounts=1533 columns=25 min_trade=2013-04-03 max_trade=2026-06-22 lineage_sample=50/50 records=1416497 rows_eq_records=True</expect></criterion>
`CB2b1-AC2` -- the seam with the real file: every one of the 1,416,497 records is a row, 25 columns, 50 of 50 sampled rows traced to their
raw lines.

<expected_criteria>CB2b1-AC1,CB2b1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`, no AWS call** (the tests stub the client). The apply is the issuer's act under a ledger entry.
- **The input is read-only.** Never write into `Downloads`.
- **Within 120 seconds:** CB2b1-AC2 runs under the worker's `timeout 120` (round 1's run took about 20 s; keep the streaming build).
- **Rule 13:** a DS-lane script; your commit is a candidate; no `safe-deploy`. Read the scope through `opal_naming.lookup` (the naming gate
  refuses a typed `cottonwood`, row ADVI_COTBKF-W1-S1).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W4-S<k>`), and do not weaken the test or the expected value.

<paths>
data/assets/scripts/silver/commonwealth_transactions.py
data/assets/scripts/silver/tests/test_commonwealth_transactions.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round2.md</decomp_doc> (round 2), cell `CB-b-1`.
<owned_cells>CB-b-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB2b1-AC1, CB2b1-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~4/ADVI_COTBKF.TO-CB-b-1.transactions-every-record.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB2b1-AC1,CB2b1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `SILVER-TRANSACTIONS` line, the whole test file's result, the diff summary, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time backfill, run by hand (C-ONE-TIME); no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's apply runs under the laptop profile into the existing prefix.
comp-adversary: RUN -- every record kept (C-SILVER v0.4); the rows-vs-records refusal guards a short build; cross-firm (cottonwood scope from the registry); no shadow pipeline (the same table replaced in place by the issuer); BLIND: whether any reader already consumes the round-1 table (none: no gold, no page, C-SCOPE-OUT).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 C-SILVER; CTO msgs 105714, 105718; rows ADVI_COTBKF-W2-S1, S3; decomposition round 2.
