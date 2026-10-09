# TO ADVI_COTBKF.TO-CB-x-1.commonwealth-method -- round 24 CB-x-1: rebuild the after arm on Commonwealth's stated TWR method

<to_id>ADVI_COTBKF.TO-CB-x-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~46</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-x-1` (`decompositions/ADVI_COTBKF_DECOMP.round24.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x same-day
close; cash), `commonwealth_daily_returns.py` + `commonwealth_flows.py` (daily return, external flows out at the end of the day),
`commonwealth_monthly_grade.py` (months chained vs Commonwealth's Month TWR, TOLERANCE_PCT 0.05). `commonwealth_sweeps.py` holds the
sweep list (v1: FDIC66606, FDIC66853) and the cash-leg rules selected per arm by the runner `commonwealth_sweep_regrade.py`
(`--before-cash-leg` / `--after-cash-leg`: `r19`, `repaired`, `conditional` -- the current default -- and `divfee`, withdrawn); the
runner persists `month_grades_before/after.parquet`, prints the round-19 movers (`deliverables/0.9.0_WK_ADVI_COTBKF~41/mover_classes.parquet`,
causes `.../~42/mover_causes.parquet`), round 22's 25 recovered months, the no-sweep control and the regressions, and ends
`... control_same=<b> regressions=<n> movers_back=<m>`.

Round 23's real run (`r19` -> `conditional`): `months_after=2058/1525/79010 control_same=True regressions=1 movers_back=0`. Round 22's
25 recovered months are 0 of 25 MATCH; the CTO named the cause: a wrong cash level carried into later months (D2-S35). Five rule trials
traded one error for another; the CTO ruled "the method, not more rules".

**Your item (the CTO's round-23 analysis, E1).** Implement, as ONE new cash-leg rule `method` and the default, Commonwealth's stated
method from the CRO's research `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COMMONWEALTH_TWR_METHOD.md` (read it in
full; its table is the specification):
- a daily-valued, geometrically linked TWR on the whole account, cash and sweeps included as ONE cash position at par; moves between
  sweep and CFNCASH are internal;
- investment-management fees are a DRAG inside the return, not a flow: `man`; `ManAltT` and `ManCheck` on the owing account; `ManAltF`
  is an external flow out of the paying account;
- other charges are EXTERNAL FLOWS: `fch`, `genmain`, `fee`, `misc`, `csltfee`, `pcf`;
- `12b1`, dividends (`dv`/`dvr`/`dvlt`/`dvst`) and interest `int` are income;
- **carried cash levels propagate day to day:** each cash posting changes the cash balance from that day on, so a level is never lost
  or double-counted in later months (D2-S35). A day whose value cannot be worked out stays blank with its reason, never filled.
Dividend dating is NOT adopted by assumption: the file dates dividends by PAY date; the CRO infers EX-date. Implement both as a runner
option (`--dividend-date pay|ex`, default `pay`, as delivered) and grade every month containing a cross-month dividend BOTH ways,
printing the swing per month and in total, BEFORE either is adopted.

Run `--before-list v1 --after-list v1 --before-cash-leg conditional --after-cash-leg method`. In `sweep_regrade.md`:
1. the whole grade before and after;
2. round 22's 25 months, EACH either MATCH or named with its traced cause;
3. the 163 round-19 movers re-counted by verdict;
4. the cross-month dividend months graded pay vs ex with the swing;
5. the no-sweep control (months of accounts with no listed sweep, unchanged before and after);
6. the YEAR-CHAIN control: for each account-year where Commonwealth's year row chains its month rows, Opal's chained months for that
   year agree with Opal's own year chain the same way (state the rule you test before the counts).
Extend the runner's LAST line, keeping the rest: `... control_same=<b> regressions=<n> movers_back=<m> year_chain_same=<True|False>
r22_named=<k>/25`.

**AMENDMENT 1 (CTO ruling msg 1944, 2026-10-08 ~23:3xZ, on row D2-W46-S1).** "A no-sweep control is ill-posed for an account-wide method, so the year-chain (103/103) is the control." AC2's expectation becomes `year_chain_same=True`; the no-sweep figures stay printed as information. "The method becomes the default once the packet names a cause for each of the 98 regressions: 35 are unlisted types, and the other 63 each need one." So, before the flip: in `sweep_regrade.md`, a table of all 98 MATCH -> DIFF months (account, month, computed before/after, reported) with ONE named cause each -- `unlisted_type:<type>` for the 35, and for each of the other 63 a cause read from that month's rows (e.g. a dividend row and its date, a fee type, a flow), traced, never forced; a month whose cause cannot be read is `unexplained:<what was checked>`. Do not change any treatment to clear one. The ex-date grading stays NOT GRADED (row W46-S2; round 25 sources ex-dates through the dell1 queue).

Tests `data/assets/scripts/silver/tests/test_commonwealth_method.py` (stubs): a `man` fee lowers the day's return and is not a flow;
an `fch` is a flow out and does not lower the return; a dividend at pay date vs ex date lands on the expected day; a cash posting
carries into the next month's starting value exactly once.

### ACCEPTANCE

<criterion id="CB24x1-AC1" cell_refs="CB-x-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_method.py</invocation><expect>passed</expect></criterion>
`CB24x1-AC1` -- the fee drag, the charge flow, both dividend dates and the carried cash level, each on a stub.

<criterion id="CB24x1-AC2" cell_refs="CB-x-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg conditional --after-cash-leg method --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46</invocation><expect>year_chain_same=True</expect></criterion>
`CB24x1-AC2` -- (AMENDMENT 1) the year-chain control replaces the no-sweep control, ill-posed for an account-wide method (CTO msg 1944).

<criterion id="CB24x1-AC3" cell_refs="CB-x-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg conditional --after-cash-leg method --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46</invocation><expect>year_chain_same=True</expect></criterion>
`CB24x1-AC3` -- Opal's months chain into its years the way Commonwealth's do.

<criterion id="CB24x1-AC4" cell_refs="CB-x-1" judgment="true"/>
`CB24x1-AC4` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the rule follows the CRO's table row by row; round 22's 25 are each MATCH or named with a traced cause; every cross-month dividend month is graded both ways with the swing printed and neither date adopted by assumption.

<expected_criteria>CB24x1-AC1,CB24x1-AC2,CB24x1-AC3,CB24x1-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **No rule-fitting.** The CRO's table decides each row type's treatment; do not change a treatment because of its effect on the grade.
  Where the table says "untested" (`ManCheck`, `12b1`), implement it as written and report its measured effect.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W46-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time; never an edit of an existing row), and do not
  weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_monthly_grade.py
data/assets/scripts/silver/tests/test_commonwealth_method.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round24.md</decomp_doc> (round 24), cell `CB-x-1`.
<owned_cells>CB-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB24x1-AC1, CB24x1-AC2, CB24x1-AC3, CB24x1-AC4. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/ADVI_COTBKF.TO-CB-x-1.commonwealth-method.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB24x1-AC1,CB24x1-AC2,CB24x1-AC3,CB24x1-AC4` BEFORE the flip.
Mechanical: CB24x1-AC1, CB24x1-AC2, CB24x1-AC3; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the rule (file and line per row type), round 22's 25 by verdict, the 163 re-counted, the dividend swing, both controls, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the treatment of each row type comes from the CRO's table, never from its effect on the grade; dividend dating graded both ways before adoption; two controls; BLIND: row types the table does not list (they are reported, never silently treated).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-23 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_23_20261008.md` @19a4a6e00b (msg 1740), E1; CTO msg 1710; CRO research @35c8aa0d75; row D2-S35.
