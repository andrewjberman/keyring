# TO ADVI_COTBKF.TO-CB-c-1 -- round 3 CB-c-1: the price-need measurement -- per security, trading days held, by asset class, and the total

<to_id>ADVI_COTBKF.TO-CB-c-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~8</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-c-1` (`decompositions/ADVI_COTBKF_DECOMP.round3.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-c-1`. The CTO (round-2 analysis): "one measurement cell: per security, trading days held (first to last appearance), split
equity/ETF/fund vs fixed income, total rows. That number decides the vendor ask to Andrew." A READ: it writes nothing to any store and calls
no vendor.

**The input.** The silver transactions table `s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/`
(parquet, `trade_year=<YYYY>/`; read-only with boto3, default profile): 1,416,497 rows; columns include `Cusip` (4,634 distinct, none blank),
`Symbol`, `Asset_Type`, `Trade_Date` (`date32`). `Asset_Type` values: Equity 1,830 CUSIPs, Mutual Fund 978, Fixed Income 778, Cash
Equivalent 488, ETF 349, Mutual Fund (Closed End) 99, Unit Investment Trust 58, Annuity 29, Alternative Investment 22, Cash 3. Read the
table with pyarrow column projection (`Cusip`, `Asset_Type`, `Trade_Date` only).

**Definitions (exactly):**
- A security is a CUSIP. Its asset type is its most frequent `Asset_Type` across its rows (ties: alphabetical first); print how many CUSIPs
  carry more than one `Asset_Type`.
- **Days held** of a security = the NYSE trading days from its FIRST `Trade_Date` to its LAST `Trade_Date` in the table, inclusive, using
  `lib/trading_calendar.py`. A security seen on one day has 1.
- Groups: `equity` (Equity), `etf` (ETF), `fund` (Mutual Fund, Mutual Fund (Closed End), Unit Investment Trust), `fixed_income` (Fixed
  Income), `other` (Cash Equivalent, Cash, Annuity, Alternative Investment, anything else).
- **Total rows** = the sum of days held over all securities: the security-days a daily price history would need.

**Build `data/assets/scripts/analysis/commonwealth_price_need.py`:** compute per security (cusip, asset_type, group, first, last,
days_held) and per group (securities, security_days); write
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~8/PRICE_NEED_20261007.csv` (one row per security) and
`PRICE_NEED_20261007.json` (the group totals and the grand total); print one line per group, then as the LAST line exactly
`PRICE-NEED securities=<n> security_days_total=<t> equity=<d> etf=<d> fund=<d> fixed_income=<d> other=<d>` (each `<d>` a group's
security-days). Device-free (LD-0405).

Tests `data/assets/scripts/analysis/tests/test_commonwealth_price_need.py` (fixtures in `tmp_path`, no AWS): a one-day security has 1; a
weekend and an NYSE holiday inside the span are not counted; the group mapping; the tie rule for mixed `Asset_Type`; the total is the sum
of the groups.

### ACCEPTANCE

<criterion id="CB3c1-AC1" cell_refs="CB-c-1"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_price_need.py</invocation><expect>passed</expect></criterion>
`CB3c1-AC1` -- the definitions on fixtures.

<criterion id="CB3c1-AC2" cell_refs="CB-c-1"><invocation>python data/assets/scripts/analysis/commonwealth_price_need.py</invocation><expect>PRICE-NEED securities=4634 security_days_total=</expect></criterion>
`CB3c1-AC2` -- the real table read from S3; the universe equals the measured 4,634 (bound) and the total is printed with its split.

<expected_criteria>CB3c1-AC1,CB3c1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **Read only.** S3 reads of the one table above, default profile; no write anywhere outside the grant; never read `opal-data-bd` or
  `opal-data-inf` (the cross-firm law).
- **No vendor call of any kind.**
- **Within 120 seconds** for CB3c1-AC2 (column projection; round 2's full-table reads took under 60 s).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W8-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_price_need.py
data/assets/scripts/analysis/tests/test_commonwealth_price_need.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round3.md</decomp_doc> (round 3), cell `CB-c-1`.
<owned_cells>CB-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB3c1-AC1, CB3c1-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~8/ADVI_COTBKF.TO-CB-c-1.price-need.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB3c1-AC1,CB3c1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `PRICE-NEED` line, the per-group table, the mixed-type count, the result file paths, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; S3 reads under the laptop profile.
comp-adversary: RUN -- cross-firm (reads only this project's own table); vendor (none); BLIND: an account selling and re-buying a security leaves a gap the first-to-last span still counts (the CTO's definition, an upper bound per security, stated as such).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO round-2 analysis msg 105855; decomposition round 3.
