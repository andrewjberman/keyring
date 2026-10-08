# TO ADVI_COTBKF.TO-CB-w-2.divfee-legs -- round 23 CB-w-2: the dividend and fee cash legs on sweep-trade days

<to_id>ADVI_COTBKF.TO-CB-w-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~45</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>withdrawn</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-w-2` (`decompositions/ADVI_COTBKF_DECOMP.round23.md`) |
**outcome_ref:** FWD-3 | **depends_on:** `CB-w-1`

---

## WORKER FACE

### THE CELL

FWD-3 and the chain as in CB-w-1 (same worker, continued). After CB-w-1, the runner selects the cash-leg rule per arm among `r19`,
`repaired` and `conditional` (the funding credit only where no CFNCASH leg exists; the default), and its LAST line ends
`... control_same=<True|False> regressions=<n> movers_back=<m>`. The round-19 movers' causes: `.../deliverables/0.9.0_WK_ADVI_COTBKF~42/mover_causes.parquet`
(75 `other:sweep_trade_day` among the 147 `neither`).

**Your item (the CTO's round-22 analysis, E2; row W43-S1).** Dividend rows (cash in) fund sweep buys and `man`/`fch` fee rows (cash out)
are paid by sweep sales, with no matching cash leg in the chain; 94 of the 122 `neither` movers still DIFF after round 22 carry such a
row on a sweep-trade day. "The dividend and fee legs are layered only after the regression count reads 0, so that each rule's effect
stays separately measurable."
1. A new cash-leg rule `divfee`, layered on `conditional`: a dividend that funds a sweep buy credits cash, and a fee paid by a sweep sale
   debits cash, so the account value moves by the dividend or fee once and the sweep legs net to zero. One general rule over the row
   types, no account special-cased. `r19`, `repaired`, `conditional` stay selectable and unchanged; make `divfee` the default.
2. Re-grade `--before-cash-leg conditional --after-cash-leg divfee` (list v1 both arms). In `sweep_regrade.md`: the 75
   `sweep_trade_day` movers counted back to MATCH; every round-19 mover still DIFF named (account, month, computed, reported); the
   whole grade before and after; the control. `regressions` counts against the `conditional` arm (E1's baseline).

**AMENDMENT 1 -- CLOSE (CTO ruling msg 1707, 2026-10-08 ~21:4xZ, on row D2-W45-S4).** "Stop adding rules ... Drain the chain with the conditional credit as the default; CB-w-2 closes refused, citing W45-S4." Do: make `conditional` the DEFAULT again in `with_sweep_cash`, `commonwealth_daily_valuation.run` and the runner; `divfee` stays selectable, unchanged, with its tests. Confirm the default run equals CB-w-1's: the runner with `--before-cash-leg r19` and no `--after-cash-leg` prints `regressions=1`. Keep `divfee/sweep_regrade.md` as the record. Set `<status>withdrawn</status>` (the round-close vocabulary's terminal state for a refused order); AC2 stays recorded FAIL in the proof instance, never re-graded.

Tests in `data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py` (add to it): a dividend funding a same-day sweep buy moves the
value by the dividend once; a fee paid by a same-day sweep sale moves the value by the fee once; a dividend with no sweep buy is
unchanged from `conditional`.

### ACCEPTANCE

<criterion id="CB23w2-AC1" cell_refs="CB-w-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py</invocation><expect>passed</expect></criterion>
`CB23w2-AC1` -- the dividend and fee each move the value once; the no-sweep dividend unchanged.

<criterion id="CB23w2-AC2" cell_refs="CB-w-2"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg conditional --after-cash-leg divfee --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/divfee</invocation><expect>regressions=0</expect></criterion>
`CB23w2-AC2` -- the dividend/fee rule regresses no month that matched under E1's conditional credit.

<criterion id="CB23w2-AC3" cell_refs="CB-w-2" judgment="true"/>
`CB23w2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: one general rule over the row types; the 75 are counted back from the persisted grades and every month still DIFF is named, not forced; the non-sweep control is unchanged.

<expected_criteria>CB23w2-AC1,CB23w2-AC2,CB23w2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W45-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_zero_amount_flows.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round23.md</decomp_doc> (round 23), cell `CB-w-2`.
<owned_cells>CB-w-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB23w2-AC1, CB23w2-AC2, CB23w2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/ADVI_COTBKF.TO-CB-w-2.divfee-legs.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB23w2-AC1,CB23w2-AC2,CB23w2-AC3` BEFORE the flip. Mechanical: CB23w2-AC1,
CB23w2-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the rule (file and line), the 75 back-to-MATCH count, every round-19 mover still DIFF, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- one general rule over row types layered on E1's baseline so its effect is measured alone; BLIND: fee or dividend row types outside dv/dvr/man/fch (they stay named in the remaining DIFFs).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-22 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_22_20261008.md` @4899e3797f (msg 1501), E2; row D2-W43-S1.
