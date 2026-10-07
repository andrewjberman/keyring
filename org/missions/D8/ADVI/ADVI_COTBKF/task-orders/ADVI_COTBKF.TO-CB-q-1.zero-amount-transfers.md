# TO ADVI_COTBKF.TO-CB-q-1.zero-amount-transfers -- round 17 CB-q-1: zero-Amount security transfers valued at quantity x the same-day close

<to_id>ADVI_COTBKF.TO-CB-q-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~35</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-q-1` (`decompositions/ADVI_COTBKF_DECOMP.round17.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. Round 16 built the chain (all under `data/assets/scripts/silver/`): `commonwealth_daily_valuation.py`
(holdings x same-day close -> `account_day_value.parquet`), `commonwealth_daily_returns.py` + `commonwealth_flows.py` (after-fee
daily return, external flows out -> `daily_returns.parquet`), `commonwealth_monthly_grade.py` (months chained, compared with
Commonwealth's Month TWR at TOLERANCE_PCT 0.05). Parquet goes to `--data-dir`, default `<repo>/.scratch/advi_cotbkf/fwd3/`. Its real
run graded 4,231 fully priced months: 1,947 MATCH, 2,284 DIFF.

**Your item (row D2-S27).** External flow rows mostly carry `Amount` 0 when they move securities rather than cash: on the applied
transactions `lo` 18,157 of 49,689, `li` 1,424 of 61,144, `trfo` 611, `trfi` 60, `trco` 147 of 147 carry Amount 0. Today such a
day reads blank with reason `FLOW_UNVALUED`. Value it instead:
1. `commonwealth_daily_valuation.py` also writes `security_day_price.parquet` (`cusip, date, price, store`) to `--data-dir` -- the
   same-day prices it already resolves (cash at 1.0 included); nothing else in it changes;
2. `commonwealth_daily_returns.py` takes `--prices` (default: that file in `--data-dir`) and values a flow row whose `Amount` is 0 or
   null as `abs(Quantity) x that day's price` of its CUSIP, with the direction the FLOW table already gives; when that price is
   missing the day stays blank, `FLOW_UNVALUED`. A row with a non-zero Amount is unchanged;
3. the last line gains three fields:
   `DAILY-RETURNS account_days=<n> computed=<c> blank=<b> flow_types=<k> of 61 zero_amount=<z> valued=<v> blank_no_price=<p>`;
4. `daily_returns.md` names ONE account-month that contains a valued zero-Amount transfer and is fully priced, with its monthly
   grade before (blank) and after (computed, graded) -- run `commonwealth_monthly_grade.py` for it.

Run the valuation first (its defaults), then the returns. Tests, in a NEW file
`data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py` (the existing tests must still pass) -- a zero-Amount transfer of 10 shares at a close of 5 is a
flow of 50; with no close it blanks the day; a control: a non-zero Amount row is unchanged.

### ACCEPTANCE

<criterion id="CB17q1-AC1" cell_refs="CB-q-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py</invocation><expect>passed</expect></criterion>
`CB17q1-AC1` -- zero-Amount valuation, the no-price blank and the unchanged control on stubs.

<criterion id="CB17q1-AC2" cell_refs="CB-q-1"><invocation>python data/assets/scripts/silver/commonwealth_daily_returns.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~35</invocation><expect>zero_amount=</expect></criterion>
`CB17q1-AC2` -- the count of zero-Amount transfers, how many valued and how many blank for no price, on the real data, recorded.

<criterion id="CB17q1-AC3" cell_refs="CB-q-1" judgment="true"/>
`CB17q1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the one account-month in daily_returns.md reads correctly before and after: the transfer's value is quantity x that day's close, and the month's grade follows from it.

<expected_criteria>CB17q1-AC1,CB17q1-AC2,CB17q1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W35-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round17.md</decomp_doc> (round 17), cell `CB-q-1`.
<owned_cells>CB-q-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB17q1-AC1, CB17q1-AC2, CB17q1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~35/ADVI_COTBKF.TO-CB-q-1.zero-amount-transfers.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB17q1-AC1,CB17q1-AC2,CB17q1-AC3` BEFORE the flip. Mechanical: CB17q1-AC1, CB17q1-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the DAILY-RETURNS line, the account-month before and after, commits. You will then be handed CB-q-2 in the same worktree.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- a zero-Amount flow valued only from a same-day close; a missing close blanks the day; a non-zero Amount is untouched; BLIND: corporate-action transfers with no price.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-16 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_16_20261007.md` @8b6829c89f (msg 1100); decomposition round 17.
