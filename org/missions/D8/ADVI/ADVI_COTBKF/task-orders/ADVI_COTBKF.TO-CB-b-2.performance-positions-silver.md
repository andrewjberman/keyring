# TO ADVI_COTBKF.TO-CB-b-2 -- round 2 CB-b-2: Commonwealth's performance and positions files to silver, every record, typed, with lineage

<to_id>ADVI_COTBKF.TO-CB-b-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~5</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-b-2` (`decompositions/ADVI_COTBKF_DECOMP.round2.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-b-2`, ENRICHMENT BACKLOG item 1a: Commonwealth's own performance figures and its one-day positions become two silver tables, as
reported. FWD-3: "Commonwealth's own monthly, yearly and since-inception returns, with its benchmark, are readable ... as reported."
You build the converter and prove it on the real files into a LOCAL directory. You write NOTHING to S3: `--apply` is the issuer's act.

**The input, measured.** `$HOME/Downloads/Files.zip` (READ ONLY) holds
`Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip` (SHA-256
`a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b`), whose members under `CFN_SCTASK0548380_Portfolio_Accounting_Performance/` are:
- `CFN_SCTASK0548380_Historical_Performance_TWR_Cumulative_NetofFees_20260623_102759.txt`: pipe-delimited, 88,654 records, every one 13
  fields, all distinct. Header `Advisor_ID|Account_Number|ReportingPeriod|PerfType|NetGross|Annualize|StartDate|EndDate|PerfNum|
  BenchMark1Value|BenchMark1Description|Account_Status|AsOfDate`. `ReportingPeriod` is `Month` 80,709 / `Year` 6,425 /
  `InceptionToDate` 1,520. `StartDate`, `EndDate` are ISO dates; **`AsOfDate` is `MM/DD/YYYY` (`06/23/2026`)**; `NetGross`, `Annualize` are
  `True`/`False`. First row: `HJH|acct#da970705|Month|TWR|True|False|2023-10-01|2023-10-31|0.06|-1.58|Bloomberg US Aggregate Bond|1|06/23/2026`.
- `CFN_SCTASK0548380_Historical_Positions_20260623_102747.txt`: 469 records, every one 11 fields, all distinct. Header
  `Advisor_ID|AccountNumber|Cusip|FundCode|Symbol|Security_Description|Quantity|LongShort_Indicator|Position_Type|AsOfDate|Account_Status`
  (`AccountNumber` has no underscore); `AsOfDate` ISO (`2026-06-23`).
- Match a member by its FILE NAME, never by a substring of the full path: the folder name contains "Performance".

**Build `data/assets/scripts/silver/commonwealth_portfolio_files.py`:**
1. CLI as the transactions converter's: `--source <path or s3://>` (the inner zip, or with `--outer-member` the outer zip), `--data-date
   2026-06-23`, `--out <local dir>`, `--apply` (S3 at the builder keys; written and unit-tested with a stub, never run by you),
   `--verify-sample <n>` (default 50). Device-free (LD-0405). Read the scope through `opal_naming.lookup` (a typed `cottonwood` is refused
   by the commit naming gate). Keys: `address('commonwealth', <scope>, 'silver', 'performance' | 'positions', 'date=<data-date>')`.
2. Parse with `csv.reader(delimiter='|')` (a quoted field may span lines). Keep EVERY record and EVERY vendor column (C-SILVER v0.4); the
   row count must equal the file's record count, else REFUSE (rc 4, nothing written).
3. Types: performance -- `StartDate`, `EndDate`, `AsOfDate` `date32` (parse `AsOfDate` as `%m/%d/%Y`); `PerfNum`, `BenchMark1Value`
   `float64` (empty -> null); `NetGross`, `Annualize` `bool`; every other column a string. Positions -- `AsOfDate` `date32`; `Quantity`
   `float64`; every other column a string (`AccountNumber`, `Cusip`, `FundCode` keep leading zeros).
4. Lineage on every row (the decomposition's contract): `source_zip`, `source_zip_sha256`, `source_file`, `source_line` (1-based physical
   line of the record's first line; header = line 1), `source_record` (1-based record ordinal, header excluded).
5. Partitions: performance `reporting_period=<value>/`; positions unpartitioned. pyarrow parquet.
6. Self-verify: read the output back; re-read `--verify-sample` seeded-random rows per table from the member by `source_line` and compare
   field by field (the dates and floats by value, as written).
7. LAST line exactly:
   `PORTFOLIO-FILES performance_records=<r> performance_rows=<n> positions_records=<r> positions_rows=<n> unexplained=<u> lineage_sample=<ok>/<n>`
   (`lineage_sample` sums both tables' samples).
8. Tests `data/assets/scripts/silver/tests/test_commonwealth_portfolio_files.py` (pytest, fixture zip in `tmp_path`): the `MM/DD/YYYY` date
   typed; booleans typed; leading zeros kept; two identical records kept as two rows; a quoted multi-line field counted as one record;
   partition layout; the rows-vs-records refusal (rc 4) when the build is forced short; `--apply` writes the builder keys on a stub.

### ACCEPTANCE

<criterion id="CB2b2-AC1" cell_refs="CB-b-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_portfolio_files.py</invocation><expect>passed</expect></criterion>
`CB2b2-AC1` -- the converter's behaviour on a fixture, including the rows-vs-records refusal.

<criterion id="CB2b2-AC2" cell_refs="CB-b-2"><invocation>python data/assets/scripts/silver/commonwealth_portfolio_files.py --source "$HOME/Downloads/Files.zip" --outer-member "Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip" --data-date 2026-06-23 --out .scratch/advi_cotbkf/silver_portfolio --verify-sample 50</invocation><expect>PORTFOLIO-FILES performance_records=88654 performance_rows=88654 positions_records=469 positions_rows=469 unexplained=0 lineage_sample=100/100</expect></criterion>
`CB2b2-AC2` -- the seam with the real files: every performance and positions record a row, 50 sampled rows per table traced to their raw
lines.

<expected_criteria>CB2b2-AC1,CB2b2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`, no AWS call** (the tests stub the client). The apply is the issuer's act under a ledger entry.
- **The input is read-only.** Never write into `Downloads`.
- **Within 120 seconds** for CB2b2-AC2.
- **Rule 13:** a DS-lane script; your commit is a candidate; no `safe-deploy`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W5-S<k>`), and do not weaken the test or the expected value.

<paths>
data/assets/scripts/silver/commonwealth_portfolio_files.py
data/assets/scripts/silver/tests/test_commonwealth_portfolio_files.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit (`data/assets/scripts/silver/commonwealth_transactions.py`
may be READ as a pattern; do not edit or import from it).

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round2.md</decomp_doc> (round 2), cell `CB-b-2`.
<owned_cells>CB-b-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB2b2-AC1, CB2b2-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~5/ADVI_COTBKF.TO-CB-b-2.performance-positions-silver.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB2b2-AC1,CB2b2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `PORTFOLIO-FILES` line, both schemas as written, the partition listing, the test list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time backfill, run by hand (C-ONE-TIME); no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's apply runs under the laptop profile into new prefixes of opal-data-assets.
comp-adversary: RUN -- as reported (no return is computed here; C-DAILY is later); every record kept; cross-firm (cottonwood scope); sensitive fields (neither file carries C-SENSITIVE's four); BLIND: the date format of AsOfDate in performance (measured MM/DD/YYYY, inlined).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 backlog item 1, C-SILVER, FWD-3; decomposition round 2 (measured constraints 2, 3).
