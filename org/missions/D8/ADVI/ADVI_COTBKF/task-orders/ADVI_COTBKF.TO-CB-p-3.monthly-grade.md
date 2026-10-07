# TO ADVI_COTBKF.TO-CB-p-3.monthly-grade -- round 16 CB-p-3: the monthly grade against Commonwealth's reported returns

<to_id>ADVI_COTBKF.TO-CB-p-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~34</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-p-3` (`decompositions/ADVI_COTBKF_DECOMP.round16.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none (built against the interfaces fixed in the decomposition)

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out says so and is never filled in. Step 1 (daily holdings) is done. This round builds steps 2-4 against STUB prices, so that when
the price history lands the whole chain is one run. The three steps are built in parallel by three workers against fixed files:

| file | columns |
|---|---|
| `account_day_value.parquet` (step 2 writes) | `account` str, `date` date, `value` float (null unless complete), `holdings` int, `priced_holdings` int, `complete` bool |
| `daily_returns.parquet` (step 3 writes) | `account` str, `date` date, `value` float, `flow` float, `ret` float (decimal; null when blank), `blank_reason` str |
| `monthly_grade.csv` (step 4 writes) | `account, month (YYYY-MM), computed_pct, reported_pct, diff_pct, grade (MATCH/DIFF/UNGRADABLE), reason` |

**Your step: 4, the monthly grade.** Build `data/assets/scripts/silver/commonwealth_monthly_grade.py`, read-only:
1. read `daily_returns.parquet` (`--returns`) and Commonwealth's monthly returns: silver performance, `reporting_period=Month`
   (address via `lib/opal_naming.address("commonwealth", <cottonwood scope via opal_naming.lookup>, "silver", "performance",
   "date=2026-06-23")`); every row is `PerfType=TWR`, `NetGross=True`; `PerfNum` is in PERCENT to 2 decimals; key
   `Account_Number` + `StartDate`..`EndDate` (a calendar month);
2. per account and month: `computed_pct = (prod(1 + ret) - 1) * 100` over the month's trading days;
3. grade with `TOLERANCE_PCT = 0.05` (a module constant, stated before any real run): MATCH when `abs(diff_pct) <= 0.05`; DIFF
   otherwise, with a reason; UNGRADABLE when any trading day of the month has a null `ret` (reason: the count and the first blank
   reason), when the reported value is not finite, or when either side is absent -- never MATCH;
4. write `monthly_grade.csv` and `monthly_grade.md` to `--out`; LAST line exactly:
   `MONTHLY-GRADE months=<m> match=<a> diff=<d> ungradable=<u> tolerance_pct=0.05`;
5. `--stub` runs on a built-in example (one account, three months: one matching, one off by 0.2, one with a blank day) and prints
   the same line with ` stub=True` appended.

**Tests** `data/assets/scripts/silver/tests/test_commonwealth_monthly_grade.py` (stubs, no AWS): MATCH inside the tolerance, DIFF
outside it, UNGRADABLE for a month with one blank day and for an inf reported value; a control: diff 0.05 is MATCH and 0.06 is DIFF.

### ACCEPTANCE

<criterion id="CB16p3-AC1" cell_refs="CB-p-3"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_monthly_grade.py</invocation><expect>passed</expect></criterion>
`CB16p3-AC1` -- the three grades, the tolerance edge and the never-MATCH-on-blank rule on stubs.

<criterion id="CB16p3-AC2" cell_refs="CB-p-3"><invocation>python data/assets/scripts/silver/commonwealth_monthly_grade.py --stub --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~34</invocation><expect>MONTHLY-GRADE months=3 match=1 diff=1 ungradable=1 tolerance_pct=0.05 stub=True</expect></criterion>
`CB16p3-AC2` -- the grade end to end on the built-in example.

<expected_criteria>CB16p3-AC1,CB16p3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large parquet output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`. Do not edit any existing script.
- **Unpriced is blank.** A value, return or month that cannot be worked out is null with its reason, never estimated or filled.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W34-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_monthly_grade.py
data/assets/scripts/silver/tests/test_commonwealth_monthly_grade.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round16.md</decomp_doc> (round 16), cell `CB-p-3`.
<owned_cells>CB-p-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB16p3-AC1, CB16p3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~34/ADVI_COTBKF.TO-CB-p-3.monthly-grade.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB16p3-AC1,CB16p3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the MONTHLY-GRADE stub line, how you read PerfNum's units and the month key, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand; no schedule until FWD-3 is served.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the tolerance fixed in code before data; a blank day can never grade MATCH; inf reported values are UNGRADABLE; BLIND: Commonwealth's own method beyond TWR net.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 999 (yes to round 16); draft @661c50a7ac; decomposition round 16.
