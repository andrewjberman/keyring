# TO ADVI_COTBKF.TO-CB-r-1.non-positive-base -- round 18 CB-r-1: the non-positive-base rule in the end-of-day return, then re-graded

<to_id>ADVI_COTBKF.TO-CB-r-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~37</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-r-1` (`decompositions/ADVI_COTBKF_DECOMP.round18.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x same-day
close -> `account_day_value.parquet`, `security_day_price.parquet`), `commonwealth_daily_returns.py` + `commonwealth_flows.py`
(after-fee daily return, external flows out at the END of the day, zero-Amount transfers valued at quantity x close ->
`daily_returns.parquet`), `commonwealth_monthly_grade.py` (months chained, compared with Commonwealth's Month TWR at TOLERANCE_PCT
0.05 -> `monthly_grade.csv`). Parquet goes to `--data-dir`, default `<repo>/.scratch/advi_cotbkf/fwd3/`; run the three in that
order with their defaults (the valuation reads the price stores from S3 read-only on a cold cache, about two minutes). Round 17's
real run: `MONTHLY-GRADE months=82593 match=1973 diff=2264 ungradable=78356 tolerance_pct=0.05`.

**Your item (the CTO's ruling on row D2-W35-S2).** "A day whose prior-day value is zero OR negative reads BLANK, never computed, with
reason `NON_POSITIVE_BASE`. A month containing such a day reads UNGRADED, with the count of blank days, under the same rule as an
unpriced day. It is never interpolated." Today the end rule blanks only a ZERO base (`ZERO_BASE`) and computes a negative one;
about 26,903 days follow a negative prior-day value.
1. In `commonwealth_daily_returns.py`, under the end rule, a prior-day value `<= 0` blanks the day with reason `NON_POSITIVE_BASE`
   (it replaces `ZERO_BASE`; a zero base behaves as before apart from the reason's name; the start rule already blanks it);
2. re-run the chain on the real data and print, before and after the change, the blank days by reason and the graded months
   MATCH / DIFF / UNGRADABLE, in `non_positive_base.md` under `--out`, with ONE last line exactly:
   `NON-POSITIVE-BASE days_blanked=<n> months_before=<match>/<diff>/<ungradable> months_after=<match>/<diff>/<ungradable>`
   (a small runner `data/assets/scripts/silver/commonwealth_non_positive_base.py` is allowed to produce it).

Tests `data/assets/scripts/silver/tests/test_commonwealth_non_positive_base.py` (stubs): a negative prior-day value gives a blank day
with `NON_POSITIVE_BASE`; a zero prior-day value is blank as before; a positive one computes unchanged (the control).

### ACCEPTANCE

<criterion id="CB18r1-AC1" cell_refs="CB-r-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_non_positive_base.py</invocation><expect>passed</expect></criterion>
`CB18r1-AC1` -- the negative, zero and positive-base cases on stubs.

<criterion id="CB18r1-AC2" cell_refs="CB-r-1"><invocation>python data/assets/scripts/silver/commonwealth_non_positive_base.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~37</invocation><expect>NON-POSITIVE-BASE days_blanked=</expect></criterion>
`CB18r1-AC2` -- the re-grade on the real data, before and after, by reason and by grade.

<expected_criteria>CB18r1-AC1,CB18r1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W37-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_non_positive_base.py
data/assets/scripts/silver/tests/test_commonwealth_non_positive_base.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_flow_timing.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round18.md</decomp_doc> (round 18), cell `CB-r-1`.
<owned_cells>CB-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB18r1-AC1, CB18r1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~37/ADVI_COTBKF.TO-CB-r-1.non-positive-base.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB18r1-AC1,CB18r1-AC2` BEFORE the flip. Mechanical: CB18r1-AC1, CB18r1-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the NON-POSITIVE-BASE line, the before/after table, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the ruling applied as written (blank, never computed or interpolated); the positive-base control unchanged; BLIND: why the base goes negative (short positions or an overdrawn sweep).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-17 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_17_20261008.md` @0ae2f15e5c (msg 1185); decomposition round 18.
