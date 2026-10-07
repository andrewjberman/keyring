# TO ADVI_COTBKF.TO-CB-b-3 -- round 2 CB-b-3: the price-coverage read -- which existing Opal stores price the 4,634 Commonwealth securities, over which days

<to_id>ADVI_COTBKF.TO-CB-b-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~6</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-b-3` (`decompositions/ADVI_COTBKF_DECOMP.round2.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-b-3`, ENRICHMENT BACKLOG item 1b, the step C-DAILY puts FIRST: before any daily return is built, measure how much of the needed
daily price history Opal ALREADY holds. PRD C-DAILY: "Price history is read from Opal's existing stores first (build ladder rung 2),
with the coverage of those stores over these securities printed; a security no Opal store prices leaves its days UNPRICED, and any
outside price vendor (Bloomberg, Yahoo Finance or other) waits for Andrew's per-use word." This cell is a READ: it writes nothing to any
store and calls no vendor.

**The universe, measured.** The silver transactions table at
`s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/` (parquet, `trade_year=<YYYY>/` partitions; columns
include `Cusip`, `Symbol`, `Asset_Type`, `Trade_Date`, `Account_Number`) holds 4,634 distinct non-blank CUSIPs: Equity 1,830, Mutual Fund
978, Fixed Income 778, Cash Equivalent 488, ETF 349, Mutual Fund (Closed End) 99, Unit Investment Trust 58, Annuity 29, Alternative
Investment 22, Cash 3. Read it read-only with boto3 under the default profile (the table is being rebuilt this round with more rows; the
DISTINCT securities and their date spans do not change).

**"Needed" days, as an upper bound stated as such:** for each CUSIP, every NYSE trading day from its first `Trade_Date` in the table
through 2026-06-23 (a holding may be sold earlier; the daily-holdings build is a later round, so this is the most a valuation could need).
Use `lib/trading_calendar.py` for the trading days.

**Find the stores -- by subtraction from a printed denominator, never from memory alone.** Census the estate for any stored DAILY close
price series keyed by CUSIP, ticker or an id that maps to them: use `comp-estate --layers` and `comp-find` (for example over column names
such as close/price/px_last in `data/` and `lib/`), and read `integrations/bloomberg/READ_HERE.md` FIRST before touching anything
Bloomberg. Known starting points, to be confirmed and not assumed complete: the G4 `security_market` series at
`s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/` (Bloomberg-derived, about 730 days); the Bloomberg derived layer (current-day
only per its READ_HERE); the Yang / MDPF model-portfolio price pickles (`data/yang_pkl`). Print every store you checked, with what it
holds (key, date range, row or file count) and why it is or is not a price series.

**Build `data/assets/scripts/analysis/commonwealth_price_coverage.py`:** reads the universe and each confirmed store (read-only), matches
a security to a store by CUSIP, else by ticker (`Symbol`), and computes, per store and per `Asset_Type`: securities priced on any day;
security-days covered within the needed window; the needed total. Writes
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/PRICE_COVERAGE_20261006.json` (per store, per asset type, the
union across stores, and the list of stores checked with their verdict) and a short `.md` beside it, and prints as the LAST line:
`PRICE-COVERAGE universe=<n> stores_checked=<k> stores_with_prices=<m> priced_any=<s> security_days_covered=<c> security_days_needed=<d>`.
`--self-test` runs the coverage arithmetic on a fixture (two securities, two stores, a partial window) and prints
`PRICE-COVERAGE-SELFTEST ok=True`.

Tests `data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py`: CUSIP match before ticker; a ticker match on a reused
symbol is reported as such; days outside the needed window are not counted; the union never double-counts a day two stores both cover.

### ACCEPTANCE

<criterion id="CB2b3-AC1" cell_refs="CB-b-3"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py</invocation><expect>passed</expect></criterion>
`CB2b3-AC1` -- the coverage arithmetic and matching on fixtures.

<criterion id="CB2b3-AC2" cell_refs="CB-b-3"><invocation>python data/assets/scripts/analysis/commonwealth_price_coverage.py</invocation><expect>PRICE-COVERAGE universe=4634 stores_checked=</expect></criterion>
`CB2b3-AC2` -- the seam with the real store: the full universe read from S3 and a coverage line printed with its denominators (bound:
the universe count equals the measured 4,634).

<criterion id="CB2b3-AC3" cell_refs="CB-b-3" judgment="true"/>
`CB2b3-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: the store census is complete enough to rely on -- every Opal store that holds a
daily price series was checked and is named with its verdict, so an UNPRICED security is unpriced by Opal, not merely by the stores this
cell happened to know.

<expected_criteria>CB2b3-AC1,CB2b3-AC2,CB2b3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **Read only.** S3 and estate READS under the default profile only; no write to any bucket, table or file outside the grant.
- **No vendor call of any kind:** no YCharts, Bloomberg terminal or API, Yahoo, gateway market-data tool, or web price source. Opal's own
  stored data only (Andrew's per-use word gates every vendor).
- **Within 120 seconds** for CB2b3-AC2: cache what you read under `.scratch/` and let the script read the cache when present.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W6-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_price_coverage.py
data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round2.md</decomp_doc> (round 2), cell `CB-b-3`.
<owned_cells>CB-b-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB2b3-AC1, CB2b3-AC2, CB2b3-AC3 (judgment: record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO;
never PASS or FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/ADVI_COTBKF.TO-CB-b-3.price-coverage-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB2b3-AC1,CB2b3-AC2,CB2b3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `PRICE-COVERAGE` line, the stores checked with their verdicts, coverage by asset type, the result file paths, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; S3 reads under the laptop profile.
comp-adversary: RUN -- vendor egress (forbidden on the face; Opal stores only); cross-firm (reads Opal's shared price stores, no other firm's client data; the universe is cottonwood's); BLIND: stores the census does not reach (the judgment criterion asks the CVO to grade exactly that).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 C-DAILY, backlog item 1, manifest S10 ("price coverage unread"); decomposition round 2 (measured constraint 4).
