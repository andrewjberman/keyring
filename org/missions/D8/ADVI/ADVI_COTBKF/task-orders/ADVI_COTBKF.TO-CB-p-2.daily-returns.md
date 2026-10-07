# TO ADVI_COTBKF.TO-CB-p-2.daily-returns -- round 16 CB-p-2: the daily after-fee return per account, flows taken out

<to_id>ADVI_COTBKF.TO-CB-p-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~33</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-p-2` (`decompositions/ADVI_COTBKF_DECOMP.round16.md`) |
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

**Your step: 3, daily return.** Build `data/assets/scripts/silver/commonwealth_daily_returns.py`, read-only:
1. **the FLOW table** -- a module `data/assets/scripts/silver/commonwealth_flows.py` that decides, for EVERY transaction type in
   `commonwealth_signs.SIGN` and `NO_SHARE_MOVEMENT` (61 types; the census
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29/tx_types.csv` lists them with a description), whether it is an
   EXTERNAL FLOW (money or securities entering or leaving the account from outside: contributions, distributions, transfers in and
   out) or INTERNAL (trades, dividends, interest, reinvestment, corporate actions, and every fee -- fees are NOT flows, so the return
   is after fees). One reason per type, in the module, as `commonwealth_signs` does. The flow amount of a row is its `Amount`; a
   flow row whose `Amount` is zero or null blanks that day with reason `FLOW_UNVALUED`;
2. read `account_day_value.parquet` (`--values`) and silver transactions (`commonwealth_daily_holdings.load_tx_pos()`); a
   transaction on a non-trading day counts on the next trading day;
3. per account, per trading day t: `ret_t = (value_t - flow_t) / value_(t-1) - 1` (flows at end of day); `ret` is null with a reason
   when value_t or value_(t-1) is null (`UNPRICED`), when value_(t-1) is 0 (`ZERO_BASE`), or `FLOW_UNVALUED`; an account's first day
   has no return (`FIRST_DAY`);
4. write `daily_returns.parquet` to `--data-dir` (default `<repo>/.scratch/advi_cotbkf/fwd3/`) and `daily_returns.md` to `--out`;
   LAST line exactly: `DAILY-RETURNS account_days=<n> computed=<c> blank=<b> flow_types=<k> of 61`;
5. `--stub` runs steps 2-4 on a built-in three-day, one-account example (a deposit on day 2) and prints the same line with
   ` stub=True` appended.

**Tests** `data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py` (stubs, no AWS): a known path with a mid-period deposit
returns the hand-computed daily returns; a control: dropping the deposit row changes day 2's return; a blank value blanks that day
and the next; every type in the signing table has a flow decision (61 of 61).

### ACCEPTANCE

<criterion id="CB16p2-AC1" cell_refs="CB-p-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py</invocation><expect>passed</expect></criterion>
`CB16p2-AC1` -- the return formula, the flow control and the blank rule on stubs.

<criterion id="CB16p2-AC2" cell_refs="CB-p-2"><invocation>python data/assets/scripts/silver/commonwealth_daily_returns.py --stub --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~33</invocation><expect>flow_types=61 of 61 stub=True</expect></criterion>
`CB16p2-AC2` -- every type decided, and the step runs end to end on the built-in example.

<expected_criteria>CB16p2-AC1,CB16p2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large parquet output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`. Do not edit any existing script.
- **Unpriced is blank.** A value, return or month that cannot be worked out is null with its reason, never estimated or filled.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W33-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round16.md</decomp_doc> (round 16), cell `CB-p-2`.
<owned_cells>CB-p-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB16p2-AC1, CB16p2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~33/ADVI_COTBKF.TO-CB-p-2.daily-returns.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB16p2-AC1,CB16p2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the DAILY-RETURNS stub line, the flow decisions you found hardest (types and reasons), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand; no schedule until FWD-3 is served.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- fees are not flows (after-fee); every type decided with a reason; dropping a deposit moves the return; BLIND: a flow row with no Amount (FLOW_UNVALUED).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 999 (yes to round 16); draft @661c50a7ac; decomposition round 16.
