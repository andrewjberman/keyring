# TO ADVI_COTBKF.TO-CB-y-1.unlisted-types -- round 25 CB-y-1: a sourced treatment for each unlisted row type, `ftax` first

<to_id>ADVI_COTBKF.TO-CB-y-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~47</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-y-1` (`decompositions/ADVI_COTBKF_DECOMP.round25.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out is never filled in. The chain, all under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py`,
`commonwealth_daily_returns.py` + `commonwealth_flows.py`, `commonwealth_monthly_grade.py` (TOLERANCE_PCT 0.05), with the cash-leg
rules in `commonwealth_sweeps.py` selected by the runner `commonwealth_sweep_regrade.py` (`--before-cash-leg` / `--after-cash-leg`).
Round 24 made `method` the default: Commonwealth's stated TWR method per the CRO's research
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COMMONWEALTH_TWR_METHOD.md` (advisory fees `man`/`ManAltT`/`ManCheck` a
drag; `fch`, `genmain`, `fee`, `misc`, `csltfee`, `pcf`, `ManAltF` flows; dividends, `int`, `12b1` income; sweeps + CFNCASH one cash
position; carried levels propagated). The runner's LAST line ends `... regressions=<n> movers_back=<m> year_chain_same=<b> r22_named=<k>/25`;
`regressions` counts months MATCH in the before arm and DIFF in the after arm.

Round 24's real run (`conditional` -> `method`): `months_after=3059/925/78609 year_chain_same=True regressions=98`, every regression
named in `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md`. 35 of them hold a row type the CRO's
table does not name, kept INTERNAL by default (row W46-S3): `ftax` 29, `ftax+stax` 1, `cbf` 3, `fco` 1, `stp` 1. The full unlisted set
is ASF, bcf, cbf, fco, stp, term, ftax, stax, frntax. Specimen: 0QF879431 2016-03, a withdrawal that includes an `ftax` of 129.63;
reported 0.00, computed -0.1616.

**Your item (the CTO's round-24 analysis, E1).**
1. For EACH unlisted type, a treatment (drag / flow / income / internal) with its stated SOURCE, decided before any run: the delivered
   files' own field documentation, the row's pairing in the delivery (e.g. an `ftax` riding a withdrawal on the same day and amount),
   or Commonwealth's documented method. A type with no source stays INTERNAL and is said so. Put the table in a new rule `method_r25`,
   layered on `method`; `method` stays selectable and unchanged.
2. Re-grade `--before-list v1 --after-list v1 --before-cash-leg method --after-cash-leg method_r25` with
   `--out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/unlisted`. In `sweep_regrade.md`: the source table; each
   of the 35 now MATCH or named with a traced cause; the whole grade; every MATCH -> DIFF month named. Do not change a treatment
   because of its effect on the grade.

Tests `data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py` (stubs): an `ftax` riding a same-day withdrawal is treated
per its stated source; a type with no source stays internal; `method` is unchanged by the new rule.

### ACCEPTANCE

<criterion id="CB25y1-AC1" cell_refs="CB-y-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py</invocation><expect>passed</expect></criterion>
`CB25y1-AC1` -- each sourced treatment on a stub; an unsourced type stays internal; `method` unchanged.

<criterion id="CB25y1-AC2" cell_refs="CB-y-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method --after-cash-leg method_r25 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/unlisted</invocation><expect>regressions=0</expect></criterion>
`CB25y1-AC2` -- the sourced treatments regress no month that matched under `method` (the 3,059 baseline).

<criterion id="CB25y1-AC3" cell_refs="CB-y-1" judgment="true"/>
`CB25y1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: every treatment cites a source decided before the run; each of the 35 is MATCH or carries a traced cause; no treatment was chosen by its effect on the grade.

<expected_criteria>CB25y1-AC1,CB25y1-AC2,CB25y1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **No rule-fitting.** A treatment comes from its stated source, never from its effect on the grade.
- **Blank, never filled.** A value, return or month that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W47-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time; never an edit of an existing row), and do not
  weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py
data/assets/scripts/silver/tests/test_commonwealth_method.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round25.md</decomp_doc> (round 25), cell `CB-y-1`.
<owned_cells>CB-y-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB25y1-AC1, CB25y1-AC2, CB25y1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/ADVI_COTBKF.TO-CB-y-1.unlisted-types.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB25y1-AC1,CB25y1-AC2,CB25y1-AC3` BEFORE the flip. Mechanical: CB25y1-AC1,
CB25y1-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, the source table, the 35 by result, every MATCH -> DIFF month, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- each treatment carries a source decided before the run; BLIND: a type whose only evidence is its effect on the grade (it stays internal).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-24 analysis @cdf5f13f3f (msg 1957), E1; row D2-W46-S3.
