# TO ADVI_COTBKF.TO-CB-a-3 -- round 1 CB-a-3: the analyst read -- one account's history oldest to newest, one row traced to the delivered file

<to_id>ADVI_COTBKF.TO-CB-a-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~3</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-a-3` (`decompositions/ADVI_COTBKF_DECOMP.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none (the lineage contract is fixed in the decomposition)

---

## WORKER FACE

### THE CELL

`CB-a-3`, hop 4 of the round-1 thread, FWD-1: "An analyst picks one Cottonwood account and reads its whole transaction history, 2013 to
June 2026, from Opal's own store, and can trace each row to the file Commonwealth sent." Nothing is read from Box, a download folder or a
spreadsheet. You build the READ and prove it on fixtures; the issuer runs it on the real store after the S3 writes (the round's FWD-1
exercise). Read only: it writes nothing anywhere.

**What it reads (the decomposition's LINEAGE CONTRACT, exactly):**
- the silver transactions table: parquet under a prefix, hive-partitioned `trade_year=<YYYY>/`, with the 20 vendor columns
  (`Advisor_ID, Account_Number, Transaction_Type, Transaction_Description, Cusip, FundCode, Symbol, Quantity, Amount, AI, Trade_Date,
  Cost_Date, Settle_Date, Asset_Type, CA_Event_Id, LongShort_Indicator, Position_Type, Security_Description, Transaction_Note, AsOfDate`;
  `Account_Number` a string with leading zeros; the four dates `date32`; `Quantity`, `Amount`, `AI` `float64`) plus `source_zip`,
  `source_zip_sha256`, `source_file`, `source_line` (1-based physical line in the member file, header = line 1);
- the bronze zip (the delivered zip, untouched) and the manifest JSON `{"delivery", "data_date", "received_date", "files":
  [{"name_as_shipped", "bytes", "sha256", "bronze_key", "members": [{"path", "bytes"}]}], "builder": {...}}`.
- In production these are the builder's keys: silver `address('commonwealth','cottonwood','silver','transactions','date=2026-06-23')`,
  manifest `address('commonwealth','cottonwood','bronze','manifest','date=2026-06-23')` + `/manifest.json`, and the zip's `bronze_key`
  from the manifest. Every one also accepts a local path (fixtures).

**Build `data/assets/scripts/analysis/commonwealth_account_history.py`:**
1. CLI: `--account <Account_Number as text>`, `--silver <local dir or s3 prefix>` (default: the builder key above), `--manifest <local file
   or s3 key>` (default: the builder key), `--trace <n>` (the n-th row of that account's history, 1-based; default 1), `--self-test`.
   Device-free (LD-0405).
2. History: every row of that account, sorted oldest to newest by `Trade_Date`, then `source_line`; print a header line and one line per
   row (trade date, type, symbol or Cusip, quantity, amount, `source_line`), then `HISTORY account=<a> rows=<n> first=<date> last=<date>`.
   An account the table does not hold prints `HISTORY account=<a> rows=0` and exits 2.
3. Trace: for row `--trace`, print its lineage; find its zip in the manifest by `source_zip`; read the zip (from the manifest's
   `bronze_key`, or the local path given); check the zip's SHA-256 equals both the row's `source_zip_sha256` and the manifest's `sha256`;
   read line `source_line` of `source_file` inside it; compare that raw line with the row's 20 vendor values re-joined by `|` (dates as
   `YYYY-MM-DD`, numbers as written in the file). Print `TRACE account=<a> row=<n> file=<source_file> line=<k> sha256_ok=<True|False>
   line_match=<True|False>`. Any False exits 3.
4. `--self-test`: build a fixture (a zip with one member of a few lines, its manifest, the silver parquet from it) in a temp dir, run the
   history and the trace, then TAMPER the fixture zip's line and run the trace again; print, as the LAST line,
   `ACCOUNT-HISTORY-SELFTEST history_ok=<True|False> trace_ok=<True|False> tamper_caught=<True|False>`.
5. Tests `data/assets/scripts/analysis/tests/test_commonwealth_account_history.py` (pytest, fixtures in `tmp_path`): order oldest to
   newest with a same-day tie broken by `source_line`; leading zeros kept in `--account`; an absent account exits 2; a SHA-256 mismatch and
   a changed line each exit 3.

### ACCEPTANCE

<criterion id="CB3-AC1" cell_refs="CB-a-3"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_account_history.py</invocation><expect>passed</expect></criterion>
`CB3-AC1` -- the read's behaviour on fixtures: order, absent account, SHA-256 mismatch and changed-line refusals.

<criterion id="CB3-AC2" cell_refs="CB-a-3"><invocation>python data/assets/scripts/analysis/commonwealth_account_history.py --self-test</invocation><expect>ACCOUNT-HISTORY-SELFTEST history_ok=True trace_ok=True tamper_caught=True</expect></criterion>
`CB3-AC2` -- the seam on a fixture (the real store is written only after the drain): a history read and a trace through the real CLI,
with the tampered-line difference control caught.

<expected_criteria>CB3-AC1,CB3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call** in your tests or self-test (fixtures only; an S3 read path is written but exercised by the issuer).
- **Read only:** the script writes nothing outside a temp dir.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W3-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_account_history.py
data/assets/scripts/analysis/tests/test_commonwealth_account_history.py
data/assets/scripts/analysis/tests/__init__.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit (`lib/opal_naming.py` included).

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.md</decomp_doc> (round 1), cell `CB-a-3`.
<owned_cells>CB-a-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB3-AC1, CB3-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~3/ADVI_COTBKF.TO-CB-a-3.account-history-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB3-AC1,CB3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test output, the CLI, the test list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read tool run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's real run reads opal-data-assets with the laptop profile.
comp-adversary: RUN -- cross-firm (cottonwood scope only); read-only (writes nothing); BLIND: the real store's shape until the issuer's apply (the lineage contract fixes it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.3 @5567e751f1 section 2 hop 4, FWD-1; decomposition @c10cf0c76a (the lineage contract).
