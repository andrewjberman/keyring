# TO ADVI_COTBKF.TO-CB-z-2.nonmatch-census -- round 26 CB-z-2: the final rule as default; the non-MATCH census with its denominator

<to_id>ADVI_COTBKF.TO-CB-z-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~48</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-z-2` (`decompositions/ADVI_COTBKF_DECOMP.round26.md`) |
**outcome_ref:** FWD-3 | **depends_on:** `CB-z-1`

---

## WORKER FACE

### THE CELL

FWD-3 and the chain as in CB-z-1 (same worker, continued). After CB-z-1 the rule `method_r26` exists (`method_r25` plus ASF's treatment,
or equal to it when ASF is NO-SOURCE). Round 25's real run: 82,593 graded months under `method_r25`, MATCH 3,098, DIFF 886,
UNGRADABLE 78,609. Earlier rounds' classes are a guide only: UNGRADABLE months come mostly from unpriced days (about 8% of
account-days are priced from Opal's stores) and from non-positive or blank bases; DIFF months have been traced in past rounds to cash
legs, fees, dividends and carried levels.

**Your item (the CTO's analysis, E1).** "The remaining non-MATCH census under the default: the denominator printed (MATCH of the total);
every non-MATCH classed with counts; no class unexplained." The CTO ruled `method_r25` the default (msg 2113).
1. Make `method_r26` the DEFAULT cash-leg rule in `commonwealth_sweeps.py` and the runner. `method_r25` and every earlier rule stay
   selectable and unchanged.
2. A new script `data/assets/scripts/silver/commonwealth_nonmatch_census.py --grades <dir> --data-dir <dir> --out <dir>`. It reads the
   persisted month grades and day values of a default run. It classes EVERY non-MATCH month (DIFF and UNGRADABLE) by ONE class, using
   rules printed before the counts. For UNGRADABLE, the class is the blank-day reason that blanks the month (e.g. UNPRICED,
   NON_POSITIVE_BASE, FIRST_DAY, no reported return). For DIFF, it is the largest traced driver of the month's difference. A month no rule
   fits is `unexplained:<what was checked>`. Write `nonmatch_census.md` + `.parquet`. LAST line exactly:
   `NONMATCH-CENSUS total=<n> match=<m> diff=<d> ungradable=<u> classes=<k> unexplained=<x>`.
3. Run the default (`--before-cash-leg method_r25`, no `--after-cash-leg`, so the after arm is the new default) into a data-dir under your
   `.scratch`, and `--out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census`. Then run the census on that
   folder and that data-dir.

Tests `data/assets/scripts/silver/tests/test_commonwealth_nonmatch_census.py` (stubs): an unpriced month classes UNPRICED; a DIFF month
classes by its largest driver; a month no rule fits is `unexplained:`; the counts sum to the total.

### ACCEPTANCE

<criterion id="CB26z2-AC1" cell_refs="CB-z-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_nonmatch_census.py</invocation><expect>passed</expect></criterion>
`CB26z2-AC1` -- the classes on stubs; the unexplained fallback; the counts sum to the total.

<criterion id="CB26z2-AC2" cell_refs="CB-z-2"><invocation>python data/assets/scripts/silver/commonwealth_nonmatch_census.py --grades org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census --data-dir .scratch/advi_cotbkf/r26 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census</invocation><expect>unexplained=0</expect></criterion>
`CB26z2-AC2` -- every non-MATCH month of the default run classed; no class unexplained. (Use `.scratch/advi_cotbkf/r26` as the step-3 data-dir.)

<criterion id="CB26z2-AC3" cell_refs="CB-z-2" judgment="true"/>
`CB26z2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the classes are decided by rules printed before the counts; the denominator is the whole graded population; no month is forced into a class.

<expected_criteria>CB26z2-AC1,CB26z2-AC2,CB26z2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets the chain already
  reads; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **No rule-fitting; blank, never filled.**
- **Refusal clause.** If a criterion cannot be met as written (e.g. a class that cannot be explained), stop, write the reason in your
  report and a NEW surprise row (id `ADVI_COTBKF-D2-W48-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), name the
  unexplained months, and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_nonmatch_census.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_nonmatch_census.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_method.py
data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round26.md</decomp_doc> (round 26), cell `CB-z-2`.
<owned_cells>CB-z-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB26z2-AC1, CB26z2-AC2, CB26z2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/ADVI_COTBKF.TO-CB-z-2.nonmatch-census.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB26z2-AC1,CB26z2-AC2,CB26z2-AC3` BEFORE the flip. Mechanical: CB26z2-AC1,
CB26z2-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the default SWEEP-REGRADE line, the NONMATCH-CENSUS line, the classes with counts, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the census denominator is the whole graded population; classes by printed rule; BLIND: a cause that spans every month equally (it shows as one large class, which the report names).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` analysis ADDENDUM 1 (msg 2113), E1 and the default ruling.
