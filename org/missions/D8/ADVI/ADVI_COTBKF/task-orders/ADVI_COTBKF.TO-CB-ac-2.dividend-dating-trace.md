# TO ADVI_COTBKF.TO-CB-ac-2.dividend-dating-trace -- round 29 CB-ac-2: read-only dividend-dating trace of the 4 regressed months

<to_id>ADVI_COTBKF.TO-CB-ac-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~55</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ac-2` (`decompositions/ADVI_COTBKF_DECOMP.round29.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily-return chain (`data/assets/scripts/silver/`, default cash leg `method_r28`, run by `commonwealth_sweep_regrade.py`) moved
4 account-months from MATCH under `method_r26` to DIFF under `method_r28`: B3S728504 and B3S728506, 2023-05 and 2023-06 (row
D2-W53-S3; `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/`). The worker's unmeasured guess: pay-date versus
ex-date dividend dating, which the split-scaled position now weights more. Dividends in the delivery carry the pay date only. Ex-dates are
available from dell1's price store `s3://opal-data-assets/yahoo/global/silver/price_history/cusip=<CUSIP>/dividends.parquet` (the CUSIPs
it holds) and from `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/EXDATES_ADVI_COTBKF_20261009.csv` (39 rows). The
re-grade runner already takes `--before-dividend-date` / `--after-dividend-date` (pay|ex) and `--ex-dates`.

**Your item (CTO ADDENDUM 4, msg 2789).** READ-ONLY: no rule change. A script
`data/assets/scripts/silver/commonwealth_div_dating_trace.py --grades <dir> --data-dir <dir> --out <dir>` that, for each of the 4 months,
prints every dividend row of the account in and around the month (CUSIP, pay date, ex-date where a source holds it -- naming the source --,
amount), the day values under `method_r26` and `method_r28`, and the month's computed return at pay date and at ex date (where ex-dates
exist), against the reported return. It names, per month, whether dividend dating explains the regression (`dividend_dating`), something
else it can read (`other:<what>`), or `untraced:<what was checked>` -- by a rule written in the script before its run. Write
`div_dating_trace.md`. LAST line exactly: `DIV-TRACE months=4 dividend_dating=<a> other=<b> untraced=<c>`.

### ACCEPTANCE

<criterion id="CB29ac2-AC1" cell_refs="CB-ac-2"><invocation>python data/assets/scripts/silver/commonwealth_div_dating_trace.py --grades org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53 --data-dir .scratch/advi_cotbkf/r28 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55</invocation><expect>DIV-TRACE months=4</expect></criterion>
`CB29ac2-AC1` -- the 4 months traced (data-dir `.scratch/advi_cotbkf/r28`: rebuild it with the default re-grade if absent).

<criterion id="CB29ac2-AC2" cell_refs="CB-ac-2" judgment="true"/>
`CB29ac2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the class of each month is decided by the script's rule from the printed rows, not from the reported return.

<expected_criteria>CB29ac2-AC1,CB29ac2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No rule change, no S3 write. Reads of the buckets the chain reads plus dell1's store; never `opal-data-bd`,
  `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection`, `opal-data-demo`.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W55-S<k>`, `"fabric": "dell2"`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_div_dating_trace.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round29.md</decomp_doc> (round 29), cell `CB-ac-2`.
<owned_cells>CB-ac-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB29ac2-AC1, CB29ac2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55/ADVI_COTBKF.TO-CB-ac-2.dividend-dating-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB29ac2-AC1,CB29ac2-AC2` BEFORE the flip. Mechanical: CB29ac2-AC1; a
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the DIV-TRACE line, each month's class with its rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only trace.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- read-only, class by a rule written before the run; BLIND: an ex-date no source holds (named).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 4 (msg 2789); row D2-W53-S3.
