# TO ADVI_COTBKF.TO-CB-aa-3.fwd3-serve-builder -- round 27 CB-aa-3: the FWD-3 serve builder (daily returns, values, month grades)

<to_id>ADVI_COTBKF.TO-CB-aa-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~52</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aa-3` (`decompositions/ADVI_COTBKF_DECOMP.round27.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3, as the PRD states its acceptance: "for any Cottonwood account in the delivery, an analyst reads its return for any single day
from 2013 to June 2026; strung together over a month, the days give the same return Commonwealth reported for that month, or the
difference is shown with its reason; a day that cannot be worked out says so and is never filled in; Commonwealth's own monthly, yearly
and since-inception returns, with its benchmark, are readable beside them as reported." The chain that computes it lives under
`data/assets/scripts/silver/` (default cash leg `method_r26`; runner `commonwealth_sweep_regrade.py` writes day parquet to `--data-dir`
and month grades beside its report). Commonwealth's reported figures are the served silver performance table
(`lib/opal_naming.address("commonwealth", <cottonwood scope>, "silver", "performance", "date=2026-06-23")`). Today nothing of the
daily build is served (endpoint read row W49-S1).

**Your item (the CTO's ADDENDUM 2, E3: "a cell serving FWD-3").** A builder
`data/assets/scripts/silver/commonwealth_fwd3_serve.py` with three modes:
- `--build --data-dir <dir> --out <dir>`: from a default run's day values and month grades, write three parquet tables locally:
  `daily_returns` (account, date, value, flow, return, blank_reason), `account_day_value` (account, date, cusip, quantity, close, value,
  price_source), `month_grades` (account, month, computed, reported Month TWR, Year TWR, ITD TWR, benchmark as reported, verdict, reason).
  Every row carries the cash-leg rule and run commit. Blank stays null with its reason; nothing is filled.
- `--dry-run`: print each table's TARGET address taken from `lib/opal_naming.address(...)` (never typed), its row count, schema and a
  content hash. Write nothing remote.
- `--verify`: read the three tables back from their served addresses and compare row counts and content hashes with the local build;
  print `FWD3-VERIFY tables=3 match=<True|False>`.
`--apply` (the S3 write) is implemented but is NOT run by you: the SERVED write is CB-aa-4, by the box applier under a pair. LAST line
of `--dry-run` exactly: `FWD3-SERVE mode=dry daily_rows=<n> value_rows=<v> month_rows=<m> keys=3 addresses_from_builder=True`.
Also print, for ONE account of your choice (a MATCHED, living client), its whole daily span and its months beside the reported figures
-- the read an analyst would do.

Tests `data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py` (stubs): the three schemas; blanks stay null with a reason;
addresses come from the builder (a monkeypatched builder changes them); `--verify` detects a changed row.

### ACCEPTANCE

<criterion id="CB27aa3-AC1" cell_refs="CB-aa-3"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py</invocation><expect>passed</expect></criterion>
`CB27aa3-AC1` -- schemas, null-with-reason, builder addresses and the verify check on stubs.

<criterion id="CB27aa3-AC2" cell_refs="CB-aa-3"><invocation>python data/assets/scripts/silver/commonwealth_fwd3_serve.py --dry-run --data-dir .scratch/advi_cotbkf/r27 --out .scratch/advi_cotbkf/fwd3_serve</invocation><expect>addresses_from_builder=True</expect></criterion>
`CB27aa3-AC2` -- the dry run names three builder addresses with row counts and hashes (data-dir `.scratch/advi_cotbkf/r27` from a default run; build first).

<criterion id="CB27aa3-AC3" cell_refs="CB-aa-3" judgment="true"/>
`CB27aa3-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the three tables carry what FWD-3's acceptance names (daily return, the reported monthly/yearly/ITD figures and benchmark beside the computed month, blank with reason); the one-account read reads as an analyst's.

<expected_criteria>CB27aa3-AC1,CB27aa3-AC2,CB27aa3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **No S3 write.** `--apply` is never run in this cell; the dry run and the local build only. S3 reads of the buckets the chain reads;
  never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection`, `opal-data-demo`.
- **Names from the builder (rule 30).** Every address from `lib/opal_naming.address`; a builder refusal is a missing registry row to
  report, never a typed workaround.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W52-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round27.md</decomp_doc> (round 27), cell `CB-aa-3`.
<owned_cells>CB-aa-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB27aa3-AC1, CB27aa3-AC2, CB27aa3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~52/ADVI_COTBKF.TO-CB-aa-3.fwd3-serve-builder.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB27aa3-AC1,CB27aa3-AC2,CB27aa3-AC3` BEFORE the flip. Mechanical: CB27aa3-AC1,
CB27aa3-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the FWD3-SERVE dry-run line, the three addresses, row counts and hashes, the one-account read, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a builder run by hand; no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE reads only under the dell2 identity; BLIND: the write identity (CB-aa-4's).
comp-adversary: RUN -- addresses from the builder; blanks stay null; the served tables carry what the acceptance names; BLIND: a consumer page reading these tables (none yet; the analyst read is a script read).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 2 (msgs 2213, 2257), E3; endpoint read row W49-S1.
