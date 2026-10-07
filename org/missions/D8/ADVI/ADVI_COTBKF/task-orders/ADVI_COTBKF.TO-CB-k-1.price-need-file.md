# TO ADVI_COTBKF.TO-CB-k-1 -- round 11 CB-k-1: the price-need FILE for MDPF_SECHIST -- every unpriced security with its source and days, no fetch

<to_id>ADVI_COTBKF.TO-CB-k-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~27</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-k-1` (`decompositions/ADVI_COTBKF_DECOMP.round11.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-k-1`, FWD-3: the Commonwealth backfill needs daily prices for 4,634 securities. Opal's own usable stores price 1,720 of them. The
other **2,914 securities, 8,091,310 security-days**, will be pulled by another project (MDPF_SECHIST, on another box) from vendor
sources, under Andrew's per-use word -- NOT by you. You write the FILE that project consumes.

These figures come from the price census, `data/assets/scripts/analysis/commonwealth_price_census.py` (run on this box's calendar
covering 2010-2027): `universe=4634 priced_any=1720 security_days_covered=1297651 security_days_needed=9388961`. Build
`data/assets/scripts/analysis/commonwealth_price_need_file.py`, read-only, which **reuses the census's own functions by import** (its
universe, its per-security needed window, its matching against the six USABLE stores; never copy them, never re-derive a different
basis) and, for every security with any uncovered day, writes one row:
`security_id` (CUSIP, else the census's key), `asset_class`, `source`, `first_date_needed`, `last_date_needed`, `days_needed` (uncovered
days only).

**Source** per PRD v0.4 ADDENDUM 2 (`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` lines 214-222): `YAHOO` for equity, ETF and
fund securities (Equity; ETF; Mutual Fund, Mutual Fund (Closed End), Unit Investment Trust); `BLOOMBERG_SITE_Z` for fixed income and
everything else. Use the census's asset-class reading of each security.

Write `PRICE_NEED_FOR_SECHIST.csv` (the rows) and `PRICE_NEED_FOR_SECHIST.json` (totals per source and overall, the census line it
reconciles to, and the basis stated in words) to `--out`. The script's LAST line exactly:
`PRICE-NEED-FILE securities=<n> security_days=<d> yahoo_securities=<a> yahoo_days=<b> bloomberg_securities=<c> bloomberg_days=<e> sums_ok=<True|False> fetched=0`
where `sums_ok` is True when the per-source counts add to the totals and the totals equal the census's `universe - priced_any` and
`security_days_needed - security_days_covered`. **No price is fetched** -- no vendor import, no network beyond the S3 reads the census
already makes.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_price_need_file.py` (stubs, no AWS): a stub census of 4 securities (2
priced fully, 1 equity partly covered, 1 bond uncovered) writes 2 rows with the right uncovered day counts and sources and `sums_ok=True`;
a stub whose per-source totals are forced off prints `sums_ok=False` (the control); the module imports no vendor client (assert
`yfinance`, `blpapi`, `requests` and `urllib.request` are absent from its imports).

### ACCEPTANCE

<criterion id="CB11k1-AC1" cell_refs="CB-k-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_price_need_file.py</invocation><expect>passed</expect></criterion>
`CB11k1-AC1` -- rows, sources, the sums control and the no-vendor-import arm on stubs.

<criterion id="CB11k1-AC2" cell_refs="CB-k-1"><invocation>python data/assets/scripts/analysis/commonwealth_price_need_file.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27</invocation><expect>PRICE-NEED-FILE securities=2914 security_days=8091310</expect></criterion>
`CB11k1-AC2` -- the real FILE reconciles to the census (the per-source figures and `sums_ok` on the same line are recorded, not presumed).

<expected_criteria>CB11k1-AC1,CB11k1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only. No vendor call of any kind** (Yahoo, Bloomberg, any API): that is egress needing Andrew's word. No S3 write.
- **Never read a FIRM bucket** (the census's BARRED grading stands).
- **Refusal clause.** If the totals do not reconcile to the census as written, stop, report the measured numbers and a surprise row (id
  `ADVI_COTBKF-D2-W27-S<k>` -- rows filed on this box carry the D2 coordinate), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_price_need_file.py
data/assets/scripts/analysis/tests/test_commonwealth_price_need_file.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round11.md</decomp_doc> (round 11), cell `CB-k-1`.
<owned_cells>CB-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB11k1-AC1, CB11k1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/ADVI_COTBKF.TO-CB-k-1.price-need-file.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB11k1-AC1,CB11k1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the PRICE-NEED-FILE line, the per-source totals, the top 10 securities by days_needed, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time file.
comp-iam: DECLARED-NOT-APPLICABLE the census's S3 reads under the dell2 identity; denominator the census's USABLE stores; BLIND: none needed.
comp-adversary: RUN -- the basis is the census's own (reused by import), reconciled by a sums check with a control; no vendor import, tested; BLIND: which securities a vendor can actually price (MDPF_SECHIST's to measure).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-10 analysis (msg 549), E1; rows S17, S19, S20, D2-W26-S2; PRD v0.4 ADDENDUM 2.
