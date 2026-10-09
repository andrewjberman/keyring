# TO ADVI_COTBKF.TO-CB-ab-1.split-dvr-inkind-repair -- round 28 CB-ab-1: repair split, distribution and in-kind days (rule method_r28)

<to_id>ADVI_COTBKF.TO-CB-ab-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~53</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ab-1` (`decompositions/ADVI_COTBKF_DECOMP.round28.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out says so and is never filled in. The chain, under `data/assets/scripts/silver/`: `commonwealth_daily_valuation.py` (holdings x
same-day close from Opal's price stores; cash), `commonwealth_daily_returns.py` + `commonwealth_flows.py`, `commonwealth_monthly_grade.py`
(TOLERANCE_PCT 0.05), cash-leg rules in `commonwealth_sweeps.py` (default `method_r26`), run by `commonwealth_sweep_regrade.py`
(`--before-cash-leg` / `--after-cash-leg`; LAST line ends `... regressions=<n> movers_back=<m> year_chain_same=<b> ...`).

Round 27's trace (`commonwealth_diff_trace.py`; `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/diff_trace.md` and
rows D2-W50-S1..S3 in the surprise channel) found three valuation defects that put KNOWN-WRONG values on specific days:
- **S1, splits (59 months, 6 securities):** the stores' closes are split-adjusted over their whole history while the rebuilt quantity is
  as traded. E.g. B3S605610 2025-11, NFLX 64110L106, 10-for-1 on 2025-11-17: day +274.90% before repair, -0.78% after. 14 splits are
  confirmed from the accounts' own rows (a row whose quantity ratio is within 0.5% of an integer k in 2..50, or 1/k, on the split day).
- **S3, distributions (13 months):** on a `dvr` day the close steps up by about the distribution per share while the shares also step up.
- **S2, in-kind (1 month):** an `li` row's Amount (5,302) is far below the shares' value (14,453), so the flow is understated.

**Your item (the CTO's ADDENDUM 3, E1).** A new cash-leg/valuation rule `method_r28`, layered on `method_r26`, made the DEFAULT, with ONE
named repair per defect, each stated (and committed) before the real run:
1. **Splits:** for each confirmed split (from the account rows; where dell1's store
   `s3://opal-data-assets/yahoo/global/silver/price_history/cusip=<CUSIP>/splits.parquet` holds the CUSIP, its split history is the
   source, and a disagreement between the two is printed, never resolved silently), value every day before the split date with the
   stored close x the cumulative ratio of later splits (as-traded). A split that cannot be confirmed leaves its days as they are, named.
2. **Distributions:** on a `dvr` day, value the new shares at the day's as-traded close and keep the distribution as income once, so the
   value does not count the step twice; where the close step cannot be separated, the day is blank with reason `DVR_CLOSE_STEP`.
3. **In-kind `li`:** value an in-kind transfer-in at the shares' as-traded close (quantity x close) when the delivered Amount is below it
   by more than a stated band, or blank the day with reason `INKIND_UNDERSTATED`; never the delivered Amount silently.
Re-grade `--before-cash-leg method_r26 --after-cash-leg method_r28`; print the 73 round-27 traced months with their new verdict and the
whole grade; regressions must be 0.

Tests `data/assets/scripts/silver/tests/test_commonwealth_split_repair.py` (stubs): a 10-for-1 split day returns the true move, not
+900%; a day before the split is valued as-traded; a `dvr` day counts the distribution once; an understated `li` is valued from the shares
or blanked with its reason; `method_r26` is unchanged.

### ACCEPTANCE

<criterion id="CB28ab1-AC1" cell_refs="CB-ab-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_split_repair.py</invocation><expect>passed</expect></criterion>
`CB28ab1-AC1` -- each repair on a stub of its defect; `method_r26` unchanged.

<criterion id="CB28ab1-AC2" cell_refs="CB-ab-1"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r26 --after-cash-leg method_r28 --data-dir .scratch/advi_cotbkf/r28 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53</invocation><expect>regressions=0</expect></criterion>
`CB28ab1-AC2` -- the repairs regress no month that matched under `method_r26`.

<criterion id="CB28ab1-AC3" cell_refs="CB-ab-1" judgment="true"/>
`CB28ab1-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each repair is named with its test, decided from the rows or the store's split history before the run, never from the reported return; a day that cannot be repaired is blank with its reason.

<expected_criteria>CB28ab1-AC1,CB28ab1-AC2,CB28ab1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Reads.** S3 reads of the buckets the chain reads plus dell1's price store; never `opal-data-bd`, `opal-data-49financial`,
  `opal-data-inf`, `opal-data-inflection`, `opal-data-demo`. No S3 write. Egress is open except Bloomberg; none is needed.
- **No rule-fitting; blank, never filled.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W53-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time; never an edit of an existing row), and do not
  weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_daily_returns.py
data/assets/scripts/silver/commonwealth_flows.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/tests/test_commonwealth_split_repair.py
data/assets/scripts/silver/tests/test_commonwealth_cash_leg.py
data/assets/scripts/silver/tests/test_commonwealth_sweeps.py
data/assets/scripts/silver/tests/test_commonwealth_method.py
data/assets/scripts/silver/tests/test_commonwealth_carried_levels.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round28.md</decomp_doc> (round 28), cell `CB-ab-1`.
<owned_cells>CB-ab-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB28ab1-AC1, CB28ab1-AC2, CB28ab1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/ADVI_COTBKF.TO-CB-ab-1.split-dvr-inkind-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB28ab1-AC1,CB28ab1-AC2,CB28ab1-AC3` BEFORE the flip. Mechanical:
CB28ab1-AC1, CB28ab1-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SWEEP-REGRADE line, each repair (file and line, its test), the 73 by new verdict, any split disagreement, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- each repair from the rows or the store's split history, stated before the run; unrepairable days blank with reason; BLIND: a split the rows do not record and the store does not hold (left as is, named).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 3 (msg 2476), E1; rows D2-W50-S1..S3; issuer draft @c8bdb8342f.
