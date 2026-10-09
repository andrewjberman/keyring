# TO ADVI_COTBKF.TO-CB-y-2.carried-levels -- round 25 CB-y-2: trace the 39 carried levels to their first wrong month

<to_id>ADVI_COTBKF.TO-CB-y-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~47</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-y-2` (`decompositions/ADVI_COTBKF_DECOMP.round25.md`) |
**outcome_ref:** FWD-3 | **depends_on:** `CB-y-1`

---

## WORKER FACE

### THE CELL

FWD-3 and the chain as in CB-y-1 (same worker, continued). After CB-y-1 the cash-leg rules include `method_r25` (the unlisted types
with their sourced treatments) layered on `method`. Round 24's cause table
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md`) names 39 regressions `carried_level:*`:
`pre_first_valued_day` 16 (the arms already differ on the account's first valued day: postings made while the account was unvalued),
`ManAltF` 14 (e.g. a -105.20 level from a `ManAltF` debit on 2017-10-09, D49141625), `trade_cash` 3 (e.g. a -140,000 net sale credit
with no offsetting purchase debit, RGY004222 2024-10), `csltfee` 2, and one each `cash_leg_difference`, `dv`, `fch`, `mixed_rows`.

**Your item (the CTO's round-24 analysis, E2).**
1. Trace each of the 39 to its FIRST WRONG MONTH: the earliest month in which the method's carried cash level departs from what the
   account's own rows support (the posting, its date and amount, and why it is wrong: missing leg, double leg, posting before the first
   valued day, a sale with no matching purchase, ...). Table it in the report, one row per month, with the first-wrong-month and its
   cause; a month whose level cannot be traced is `untraced:<what was checked>`.
2. Where ONE general rule fixes a traced cause, add it as rule `method_r25b` layered on `method_r25` and re-grade `method_r25` ->
   `method_r25b`; any fix must leave every month MATCH under `method_r25` still MATCH (`regressions=0`). Where no general rule fixes it,
   leave it traced and unfixed. No account special-cased; no fix chosen by its effect on the grade.
Run `--before-list v1 --after-list v1 --before-cash-leg method_r25 --after-cash-leg method_r25b --out
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/levels`. If no general fix exists, `method_r25b` equals
`method_r25` and the run reports `regressions=0` trivially; say so.

**AMENDMENT 1 (issuer, 2026-10-09 ~00:3xZ): the ex-dates landed -- grade the 22 dividend months both ways (round 24 AC4's parked clause; CTO msg 1957 E3).** dell1's MDPF_DEMQUE served them @5a392db104: `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/EXDATES_ADVI_COTBKF_20261009.csv` (columns cusip, ticker, pay_date, ex_date, yahoo_dividend_per_share, claim, source; 39 rows, 16 CUSIPs, all `measured`). It is on origin box/dell1 and reaches box/dell2 after the 01:00Z integrate; until then materialize it at that same repo path in your worktree with `MSYS_NO_PATHCONV=1 git show origin/box/dell1:<path> > <path>` (run `git fetch origin box/dell1` first), as an UNTRACKED read-only input -- never stage or commit it. Measured by the issuer: only 2 of the 39 have the ex-date in a different month from the pay date (XOM 30231G102: pay 2025-06-10 / ex 2025-05-15; pay 2025-09-10 / ex 2025-08-15). Do: add per-arm options `--before-dividend-date` / `--after-dividend-date` (pay|ex) to the runner; run the 22 dividend_row months of round 24 (listed in `deliverables/2.0.0_SA_COO~C2/EXDATE_REQUEST_DELL1_DATA_QUEUE_20261009.md`) at pay and at ex on the `method_r25b` cash leg; print each month's verdict both ways and its swing, the total, and the LAST line extended with `dividend_both=<graded>/22`. Neither date is adopted as the default by this amendment. AC4 below.

Tests in `data/assets/scripts/silver/tests/test_commonwealth_carried_levels.py` (stubs): each fix shipped, on a stub of its cause; a
month unaffected by the fix grades the same.

### ACCEPTANCE

<criterion id="CB25y2-AC1" cell_refs="CB-y-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_carried_levels.py</invocation><expect>passed</expect></criterion>
`CB25y2-AC1` -- each shipped fix on a stub of its cause; an unaffected month unchanged.

<criterion id="CB25y2-AC2" cell_refs="CB-y-2"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r25 --after-cash-leg method_r25b --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/levels</invocation><expect>regressions=0</expect></criterion>
`CB25y2-AC2` -- any carried-level fix regresses no month that matched under `method_r25`.

<criterion id="CB25y2-AC4" cell_refs="CB-y-2"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r25b --after-cash-leg method_r25b --before-dividend-date pay --after-dividend-date ex --ex-dates org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/EXDATES_ADVI_COTBKF_20261009.csv --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/dividends</invocation><expect>dividend_both=22/22</expect></criterion>
`CB25y2-AC4` -- (AMENDMENT 1) the 22 pay-dated dividend months graded at pay and at ex date, each swing printed.

<criterion id="CB25y2-AC3" cell_refs="CB-y-2" judgment="true"/>
`CB25y2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each of the 39 is traced to a first wrong month with its posting and cause, or named untraced with what was checked; any fix is one general rule, not fitted to the grade.

<expected_criteria>CB25y2-AC1,CB25y2-AC2,CB25y2-AC3,CB25y2-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **No rule-fitting; blank, never filled.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W47-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_carried_levels.py
data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py
data/assets/scripts/silver/tests/test_commonwealth_method.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round25.md</decomp_doc> (round 25), cell `CB-y-2`.
<owned_cells>CB-y-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB25y2-AC1, CB25y2-AC2, CB25y2-AC3, CB25y2-AC4. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/ADVI_COTBKF.TO-CB-y-2.carried-levels.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB25y2-AC1,CB25y2-AC2,CB25y2-AC3,CB25y2-AC4` BEFORE the flip. Mechanical: CB25y2-AC1,
CB25y2-AC2, CB25y2-AC4; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the 39 by first wrong month and cause, any fix (file and line), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- each level traced to the posting that built it; any fix one general rule graded against E1's baseline; BLIND: a level built before the delivery's first row (it stays untraced).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-24 analysis @cdf5f13f3f (msg 1957), E2.
