# TO ADVI_COTBKF.TO-CB-bs-1.dividend-adjusted-series -- round 71 CB-bs-1: nine fund series against their own distributions; then the count of that shape over every fund series

<to_id>ADVI_COTBKF.TO-CB-bs-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~116</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bs-1` (`decompositions/ADVI_COTBKF_DECOMP.round71.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code. No vendor is asked: the Yahoo cache on disk is read as it stands.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_71_20261011.md` section 2 item 2 and section 3 item 1; row ADVI_COTBKF-D2-W113-S1 in the channel; the round-70 scan, all files
under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~113/` (the nine fund series it classed NOISY and read by eye:
AMCPX, AMRMX, CWGIX, WGIFX, CPXIX, FINFX, NEWFX, AWSHX, WMFFX; its pairing rules and print types); the round-68 record
`.../0.9.0_WK_ADVI_COTBKF~103/SPINOFF_CLAIMS.json` (`source_adjusted_for`, and its finding that the silver price store's raw points
equal Yahoo's adjusted close times a constant for four tickers); `data/assets/scripts/silver/commonwealth_daily_valuation.py`
(`as_traded_store`, `read_yahoo_close`, the price-basis docstrings: which tickers the as-traded basis SUBSTITUTES with Yahoo's
unadjusted close and which it leaves on the store's own value) and `commonwealth_price_basis_census.py` (how a ticker gets into the
Yahoo cache and how the basis census classes it).

**The claim to test.** Nine fund series' close sits below the traded price in the past, at a ratio of 0.47 to 0.84, and rises in
jumps to about 1.00 by 2025-2026. That is the shape of a DIVIDEND-ADJUSTED close used as a price: a vendor's adjusted series scales
every past close down by each later distribution. If so, those funds are valued low in the past, and the count of wrong series is
not eight. It was read by eye. You test it.

**Your item.**

1. **The nine, against their own distributions.** For each fund: the ratio series (build close over the custodian's price print, the
   round-70 pairs), and the fund's distribution dates and per-share amounts taken from a source INDEPENDENT of the close series: the
   custodian's own dividend and reinvestment rows for that CUSIP (a distribution's date; its per-share amount where a row gives both
   an amount and the shares it was paid on, or where a reinvestment row gives the price; say exactly how you derive a per-share
   amount and on how many rows), and, separately, the Yahoo cache's own dividend column for the ticker if the cache carries one.
   Then the test: build the cumulative adjustment factor those distributions imply (each distribution scales every earlier close by
   one minus the distribution over the close before it) and compare it, date by date, with the observed ratio. Report per fund: the
   pairs, how many lie within 2 percent of the implied factor, the correlation of the two series, the dates where the observed ratio
   steps and whether a distribution sits on each step. A fund reads `DIVIDEND_ADJUSTED`, `NOT_DIVIDEND_ADJUSTED` or `UNDECIDED`.
2. **The mechanism, from the code and the caches:** for each of the nine, which store its close came from (`store` in the build's price
   table), whether the as-traded basis substituted it with Yahoo's unadjusted close or left the store's value, and why (is the ticker
   in the Yahoo cache at all; what did the basis census class it). If the Yahoo cache holds both an unadjusted and an adjusted close
   for the ticker, compare the BUILD's close with each: which one is it equal to, on how many dates.
3. **The whole table, counts only.** How many fund securities (Mutual Fund, Mutual Fund (Closed End), and separately ETF and Equity,
   which also pay distributions) have a close in the build's table; of them how many were substituted with the unadjusted close and
   how many were left on the store's value; and for those left, how many show the same shape. Use a test that does not need trade
   pairs, since most securities have too few: where the Yahoo cache carries both closes, the build's close against each; where it
   does not, say so and count them as untested. Print the denominators: fund series in the table, tested, reading adjusted, reading
   not adjusted, untested.
4. **Reach, counts only:** for the series that read DIVIDEND_ADJUSTED, the priced holding account-days and the MEASURED account-days
   that rest on a close before the security's last distribution (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet` and
   `daily_returns.parquet`). And the direction: a close that is too low in the past by a growing factor overstates the return across
   each distribution date; say on how many measured account-days a distribution date of a held, adjusted series falls.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~116/DIVIDEND_ADJUSTED_SERIES.json`, a `.csv` of the series reading DIVIDEND_ADJUSTED (columns: cusip, ticker, kind, store, substituted,
   first_date, last_date, min_ratio, distributions, priced_holding_account_days, measured_account_days; CUSIPs only in the column
   named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `nine` (a list of `{"ticker", "pairs", "within_2pct_of_implied",
   "correlation", "steps", "steps_on_a_distribution", "store", "substituted", "equals_adjusted_close_on", "equals_unadjusted_close_on",
   "reads"}`), `per_share_source` (how the distribution amounts were derived, and on how many rows), `table` (`{"fund_series",
   "substituted", "left_on_store", "tested", "reads_adjusted", "reads_not_adjusted", "untested"}`), `other_kinds` (the same counts for
   ETF and Equity), `reach` (`{"priced_holding_account_days", "measured_account_days", "measured_days_on_a_distribution_date"}`),
   `headline` (one sentence carrying the count that reads adjusted WITH the tested and untested denominators beside it),
   `not_established`.

### ACCEPTANCE

<criterion id="CB71bs1-AC1" cell_refs="CB-bs-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~116/DIVIDEND_ADJUSTED_SERIES.json',encoding='utf-8'));n=d['nine'];t=d['table'];print('DIVIDEND-ADJUSTED-RECORD nine=%d nine_reads=%s fund_series=%d substituted=%d left_on_store=%d tested=%d reads_adjusted=%d reads_not_adjusted=%d untested=%d measured_account_days=%d'%(len(n),','.join(sorted(set(x['reads'] for x in n))),t['fund_series'],t['substituted'],t['left_on_store'],t['tested'],t['reads_adjusted'],t['reads_not_adjusted'],t['untested'],d['reach']['measured_account_days']))"</invocation><expect>DIVIDEND-ADJUSTED-RECORD nine=9</expect></criterion>
`CB71bs1-AC1` -- all nine carry a reading, and the whole-table count is printed with its tested and untested denominators.

<criterion id="CB71bs1-AC2" cell_refs="CB-bs-1" judgment="true"/>
`CB71bs1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the distributions come from a source independent of
the close series; each reading follows from the comparison shown, and UNDECIDED is used where it does not; the whole-table count
states what was tested and what was not; no correction is sized on what was not tested.

<expected_criteria>CB71bs1-AC1,CB71bs1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
- Before committing run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`
  after your commit, keep CUSIPs in CSV columns named `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call
  (no Yahoo, no Bloomberg): the Yahoo cache on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price or
  per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W116-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round71.md</decomp_doc> (round 71), cell `CB-bs-1`.
<owned_cells>CB-bs-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB71bs1-AC1, CB71bs1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~116/ADVI_COTBKF.TO-CB-bs-1.dividend-adjusted-series.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB71bs1-AC1,CB71bs1-AC2` BEFORE the flip. Mechanical: CB71bs1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** how the per-share distributions were derived and on how many rows; each of the nine with its pairs, fit to the implied factor, steps on a distribution, store, whether substituted, which close it equals, and its reading; the mechanism; the whole-table counts with tested and untested; the same for ETF and Equity; the reach; the headline sentence; the `DIVIDEND-ADJUSTED-RECORD` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the distributions come from the custodian's rows, a source independent of the close series under test; UNDECIDED is a legal reading; the whole-table count must print tested and untested, so nine found by eye cannot size a correction; BLIND: a fund whose distributions the custodian's rows do not carry (never held across one) cannot be tested this way.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-71 analysis @efaa09a585 (msg 5458), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v41 @76875db91b.
