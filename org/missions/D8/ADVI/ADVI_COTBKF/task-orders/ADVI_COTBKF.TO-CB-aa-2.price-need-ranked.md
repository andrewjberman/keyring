# TO ADVI_COTBKF.TO-CB-aa-2.price-need-ranked -- round 27 CB-aa-2: the ranked price-need file for every UNPRICED security-span

<to_id>ADVI_COTBKF.TO-CB-aa-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~51</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aa-2` (`decompositions/ADVI_COTBKF_DECOMP.round27.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily-return chain (`data/assets/scripts/silver/commonwealth_daily_valuation.py` and siblings) values each holding with a
same-day close from Opal's price stores; a holding with no price leaves its day UNPRICED (blank, never filled). Round 26's census
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census/`) classes 74,846 of 79,495 non-MATCH months UNPRICED:
94.2%. Prices are now supplied by dell1's backfill data-queue project MDPF_DEMQUE, whose store keys on Commonwealth's 9-character
CUSIP (contract `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md`; index at
`s3://opal-data-assets/yahoo/global/silver/price_history/index/index.parquet`). The ranking method is the CRO's
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md`, section 6): tier P1 if any
holder is MATCHED to a current Cottonwood account in the crosswalk
(`s3://opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/crosswalk.parquet`), P2 if a holder is AMBIGUOUS or
AWAITING_PERSON, P3 otherwise; within a tier, score = held days x holding accounts, weighted by the largest single purchase amount.

**Your item (the CTO's ADDENDUM 2, E2: "the price input for UNPRICED ... the lever").** A new script
`data/assets/scripts/silver/commonwealth_price_need.py --data-dir <dir> --out <dir>` that, from a default run's day values (re-run
`commonwealth_sweep_regrade.py --before-cash-leg method_r25` into a data-dir under your `.scratch` if needed), lists every security that
leaves at least one held account-day UNPRICED, with: `cusip` (as Commonwealth delivered it), `symbol` (as delivered, may be blank),
`first_unpriced`, `last_unpriced` (the held span needing prices), `unpriced_account_days`, `accounts`, `tier` (P1/P2/P3), `score`,
`in_demque_index` (is the CUSIP already in the store's index; if so, does the store's valid range cover the span), and `rank`. Rows
already fully covered by the store are listed with `covered=True` and ranked last. Write it to the FIXED path
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.csv` (key namespace stated in a header comment
line: `# key=Commonwealth 9-char CUSIP`) plus a `.md` summary beside it. LAST printed line exactly:
`PRICE-NEED securities=<n> p1=<a> p2=<b> p3=<c> covered=<k> unpriced_account_days=<d>`.

Tests `data/assets/scripts/silver/tests/test_commonwealth_price_need.py` (stubs): tiering by the crosswalk; scoring order within a tier; a
store-covered span ranks last; the counts sum.

### ACCEPTANCE

<criterion id="CB27aa2-AC1" cell_refs="CB-aa-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_price_need.py</invocation><expect>passed</expect></criterion>
`CB27aa2-AC1` -- tiers, scores, covered-last and the sums on stubs.

<criterion id="CB27aa2-AC2" cell_refs="CB-aa-2"><invocation>python data/assets/scripts/silver/commonwealth_price_need.py --data-dir .scratch/advi_cotbkf/r27 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED</invocation><expect>PRICE-NEED securities=</expect></criterion>
`CB27aa2-AC2` -- the ranked file written at the fixed path from a default run's day values (data-dir `.scratch/advi_cotbkf/r27`).

<criterion id="CB27aa2-AC3" cell_refs="CB-aa-2" judgment="true"/>
`CB27aa2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the tiers follow the CRO's rule from the crosswalk; the spans are the held unpriced days; nothing invented for a security the data does not hold.

<expected_criteria>CB27aa2-AC1,CB27aa2-AC2,CB27aa2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Reads.** S3 reads of the buckets the chain reads plus the MDPF_DEMQUE index; never `opal-data-bd`, `opal-data-49financial`,
  `opal-data-inf`, `opal-data-inflection`, `opal-data-demo`. No S3 write. No vendor call is needed (the pull is dell1's).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W51-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_price_need.py
data/assets/scripts/silver/tests/test_commonwealth_price_need.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.csv
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.md
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round27.md</decomp_doc> (round 27), cell `CB-aa-2`.
<owned_cells>CB-aa-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB27aa2-AC1, CB27aa2-AC2, CB27aa2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~51/ADVI_COTBKF.TO-CB-aa-2.price-need-ranked.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB27aa2-AC1,CB27aa2-AC2,CB27aa2-AC3` BEFORE the flip. Mechanical: CB27aa2-AC1,
CB27aa2-AC2; a judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the PRICE-NEED line, the top 20 rows, the tier counts, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the need is the held unpriced span from the chain's own day values, tiered by the crosswalk; BLIND: a living client matched only by name (the crosswalk matches by account; such a client reads P3 -- the CRO's rec 4).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 2 (msgs 2213, 2257), E2; CTO msgs 1459, 1495 (the need list's fixed path and key namespace).
