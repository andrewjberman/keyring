# TO ADVI_COTBKF.TO-CB-b-4 -- round 2 CB-b-4: the coverage table (FWD-6) -- for each kind of record, how far back it goes, generated from the data

<to_id>ADVI_COTBKF.TO-CB-b-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~7</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-b-4` (`decompositions/ADVI_COTBKF_DECOMP.round2.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none (the table contracts are fixed in the decomposition)

---

## WORKER FACE

### THE CELL

`CB-b-4`, ENRICHMENT BACKLOG item 2, FWD-6: "A person can see what this backfill covers and what it does not ... for each kind of record,
how far back it goes ... nobody mistakes one for another." C-COVERAGE: "One coverage table, generated from the data itself: for each record
kind, its earliest and latest date and its row count. The brief's measurements are the expectation, not the source." You build the
generator and prove it on fixtures. You write NOTHING to S3: the real run and `--apply` are the issuer's acts, after this round's silver
tables are rebuilt.

**What it reads (the decomposition's contracts):** three silver tables, each a parquet prefix (local dir or `s3://`), every row carrying
`source_zip`, `source_zip_sha256`, `source_file`, `source_line`, `source_record`:
- transactions -- `trade_year=<YYYY>/` partitions; date column `Trade_Date` (`date32`);
- performance -- `reporting_period=<Month|Year|InceptionToDate>/` partitions; date columns `StartDate`, `EndDate` (`date32`);
- positions -- unpartitioned; date column `AsOfDate` (`date32`).
Builder keys in production: `address('commonwealth', <scope>, 'silver', <table>, 'date=2026-06-23')` for `transactions`, `performance`,
`positions`, and the output `coverage`; read the scope through `opal_naming.lookup` (a typed `cottonwood` is refused by the naming gate).

**Build `data/assets/scripts/silver/commonwealth_coverage.py`:**
1. CLI: `--transactions`, `--performance`, `--positions` (each a local dir or `s3://` prefix; default the builder keys), `--out <local dir>`,
   `--apply` (writes to S3 at the `coverage` builder key; unit-tested on a stub, never run by you), `--self-test`. Device-free (LD-0405).
2. One row per record kind, columns exactly `record_kind, source_file, date_column, earliest, latest, rows, distinct_accounts, note`:
   `transactions` (Trade_Date); `performance_month`, `performance_year`, `performance_inception` (by `ReportingPeriod`; earliest =
   min `StartDate`, latest = max `EndDate`); `positions` (AsOfDate). `note` states the grain in words (for example "one day only" when
   earliest == latest). All values computed from the tables; nothing typed from the brief.
3. Writes `coverage.parquet` and `coverage.json` (the same rows) under `--out` or the builder key, and prints one line per row then, as the
   LAST line, `COVERAGE kinds=<n> rows_total=<n>`.
4. `--self-test`: build the three fixture tables in a temp dir (two months of transactions, performance rows of each period, one positions
   day), run the generator, check every value against the fixture by recomputation, and print `COVERAGE-SELFTEST kinds=5 ok=True`.
5. Tests `data/assets/scripts/silver/tests/test_commonwealth_coverage.py`: earliest/latest/rows per kind; the positions note says one day;
   an empty table yields its kind with rows=0 and a note, never a missing row; `--apply` writes the builder key on a stub.

### ACCEPTANCE

<criterion id="CB2b4-AC1" cell_refs="CB-b-4"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_coverage.py</invocation><expect>passed</expect></criterion>
`CB2b4-AC1` -- the generator's behaviour on fixtures.

<criterion id="CB2b4-AC2" cell_refs="CB-b-4"><invocation>python data/assets/scripts/silver/commonwealth_coverage.py --self-test</invocation><expect>COVERAGE-SELFTEST kinds=5 ok=True</expect></criterion>
`CB2b4-AC2` -- the seam on fixtures (the rebuilt tables are written only after the drain): the five kinds, each value recomputed.

<expected_criteria>CB2b4-AC1,CB2b4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`, no AWS call** in tests or self-test.
- **Rule 13:** a DS-lane script; your commit is a candidate; no `safe-deploy`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W7-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_coverage.py
data/assets/scripts/silver/tests/test_commonwealth_coverage.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round2.md</decomp_doc> (round 2), cell `CB-b-4`.
<owned_cells>CB-b-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB2b4-AC1, CB2b4-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~7/ADVI_COTBKF.TO-CB-b-4.coverage-table.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB2b4-AC1,CB2b4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test output, the output schema, the test list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time generator run by hand.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's apply runs under the laptop profile into a new prefix of opal-data-assets.
comp-adversary: RUN -- generated from the data, never from the brief (C-COVERAGE); cross-firm (cottonwood scope); BLIND: CRM and document kinds (later rounds add their rows; the generator takes tables as arguments so it grows without a rewrite).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 backlog item 2, C-COVERAGE, FWD-6; decomposition round 2.
