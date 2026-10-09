# TO ADVI_COTBKF.TO-CB-v-1.cash-leg-repair -- round 22 CB-v-1: a non-sweep sale that funds a sweep buy credits cash; re-graded

<to_id>ADVI_COTBKF.TO-CB-v-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~43</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-v-1` (`decompositions/ADVI_COTBKF_DECOMP.round22.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x same-day
close; cash), `commonwealth_daily_returns.py` + `commonwealth_flows.py` (after-fee daily return, external flows out at the end of the
day), `commonwealth_monthly_grade.py` (months chained vs Commonwealth's Month TWR, TOLERANCE_PCT 0.05). Round 19 made the two FDIC
bank sweeps (`commonwealth_sweeps.py`, sweeps-v1: FDIC66606, FDIC66853) cash, their buys and sells INTERNAL, and made the sweep's
sale proceeds and purchase cost land in cash. `commonwealth_sweep_regrade.py` re-runs the chain for two arms (`--before-list
none|v1|v2`, `--after-list ...`, `--data-dir`, `--out`), persists `month_grades_before/after.parquet` beside `sweep_regrade.md`, and
prints a control (months of accounts with no listed sweep on or before the month).

Round 19's re-grade (arm `none` -> arm `v1`) moved 163 months MATCH -> DIFF: 16 in accounts holding 316067107 and 147 "neither"
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~41/mover_classes.parquet`); the 147 classed 72 `sweep_balance`
and 75 `other:sweep_trade_day` (`.../0.9.0_WK_ADVI_COTBKF~42/mover_causes.parquet`, `mover_causes.md`). Both are READ only.

**Your item (the CTO's round-21 ruling on D2-S32, E1).** "In the after arm, a sweep buy debits cash. The non-sweep sale that funded it
credits no cash. So the account's value steps down and never steps back." Trace: D49141714 2019-02, arm difference a constant
-4,010.86 on all 19 days (= the net sweep buys), value 4,061.90 before and 51.04 after, month 3.31% after against 0.04% reported;
acct#65b3b3ea 2024-12, steps of -199.98 and -188.14 on its two sweep-trade days.
1. Repair the cash leg in the chain so that the proceeds of a sale of a NON-sweep security land in cash in the v1 arm, so a sale that
   funds a sweep buy leaves the account's value continuous. Find where the round-19 change made the sweep leg debit cash without the
   matching credit, and fix it there; do not special-case these accounts. `CFNCASH` stays cash; the sweep list is unchanged.
2. Re-grade with the runner: before arm = the chain as it stands at your cut with list v1, after arm = the repaired chain with list v1
   (add runner options `--before-cash-leg r19|repaired` and `--after-cash-leg r19|repaired`, default `repaired`; `r19` reproduces the chain at your cut exactly). In `sweep_regrade.md`
   print: the whole grade before and after; all 163 movers with their verdict under arm `none` (round 19 before), v1 unrepaired and
   v1 repaired; the count of the 72 and of the 75 that return to MATCH; EVERY month left DIFF, named (account, month, computed,
   reported), never forced; and the control. Keep the runner's LAST line format.
Run with `--out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~43` and a `--data-dir` under your worktree's
`.scratch/`.

Tests `data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py` (stubs): a same-day sale of a non-sweep security funding a buy
of a listed sweep leaves the day's value unchanged (debit and credit net to zero within rounding) and the day's return 0; a sale with
no sweep buy credits cash as before; a sweep sell paying an `lo` of cash still moves the value once (round 19's case).

### ACCEPTANCE

<criterion id="CB22v1-AC1" cell_refs="CB-v-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py</invocation><expect>passed</expect></criterion>
`CB22v1-AC1` -- a sale funding a sweep buy leaves the value continuous; round 19's sweep-funded withdrawal still moves the value once.

<criterion id="CB22v1-AC2" cell_refs="CB-v-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg r19 --after-cash-leg repaired --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~43</invocation><expect>control_same=True</expect></criterion>
`CB22v1-AC2` -- the repaired chain re-graded against the unrepaired one; months of accounts with no listed sweep unmoved.

<criterion id="CB22v1-AC3" cell_refs="CB-v-1" judgment="true"/>
`CB22v1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the repair is one general cash-leg rule (no account special-cased), the 72 and the 75 are counted back to MATCH from the persisted grades, and every month still DIFF is named, not forced.

<expected_criteria>CB22v1-AC1,CB22v1-AC2,CB22v1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W43-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it; a NEW row, never an edit of an
  existing one), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round22.md</decomp_doc> (round 22), cell `CB-v-1`.
<owned_cells>CB-v-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB22v1-AC1, CB22v1-AC2, CB22v1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~43/ADVI_COTBKF.TO-CB-v-1.cash-leg-repair.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB22v1-AC1,CB22v1-AC2,CB22v1-AC3` BEFORE the flip. Mechanical: CB22v1-AC1,
CB22v1-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the repair (file and line, before and after), the 72 / 75 back-to-MATCH counts, every remaining DIFF month, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- one general cash-leg rule, never an account special case; the movers counted from the persisted grades; BLIND: a second mechanism that also returns some movers to MATCH by coincidence (the named remaining DIFFs are where it would show).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-21 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_21_20261008.md` (msg 1449), section 2 and E1; rows D2-W42-S1, D2-S32.
