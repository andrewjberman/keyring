# TO ADVI_COTBKF.TO-CB-ag-1.price-basis-census -- round 33 CB-ag-1: per-ticker price-basis census of the chain's price store

<to_id>ADVI_COTBKF.TO-CB-ag-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~60</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ag-1` (`decompositions/ADVI_COTBKF_DECOMP.round33.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily chain (`data/assets/scripts/silver/`) values each holding at a price from ONE store.
- Location: `s3://opal-data-cot/silver/prices/canonical_prices.parquet`.
- Code path: `data/assets/scripts/analysis/commonwealth_price_census.py` STORES[0], imported by
  `data/assets/scripts/silver/commonwealth_daily_valuation.py`.
- Contents: 11,291,021 rows, 4,003 tickers, columns `date, asset_name, ticker, price, source`.
- Source labels: `linear_interpolation` (7,831,140 rows), `yahoo_finance` (3,396,067 rows / 3,580 tickers), `transaction_observed`,
  `scoped_override`, `bd_txn_price` (1,623 rows / 3 tickers), `transaction_observed_capped`.

Round 32 showed that for SCHB and SCHZ the `yahoo_finance` rows are a DIVIDEND-ADJUSTED Yahoo level from an earlier vintage: a
constant ratio to today's `Adj Close` (1.0054, 1.0216), and below `Close`. The trace is
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~59/base_close_trace.md`; its script is
`data/assets/scripts/silver/commonwealth_base_close_trace.py` (reuse its Yahoo-reading code).

The ruling (CTO ADDENDUM 8) is that valuation must use the AS-TRADED close: Yahoo `Close`, adjusted for splits only, never for
dividends. Dividends enter only as cash.

**Your item.** READ-ONLY: no rule change, no S3 write. Write a script
`data/assets/scripts/silver/commonwealth_price_basis_census.py --out <dir> [--max-tickers N]`. It does the following.

1. **Reads the store as it stands.** Print its row count, ticker count, the S3 object's `LastModified` (the file vintage) and the
   per-label row counts.
2. **Reads Yahoo gently, for every ticker carrying `yahoo_finance` rows.**
   - Use `yfinance.download` with at most 50 tickers per call, `auto_adjust=False` (both `Close` and `Adj Close`), and a pause of at
     least 5 s between calls. Make one pass.
   - Cache the raw pulls under `.scratch/advi_cotbkf/yahoo_census/` so a later rebuild reuses them.
   - Print the number of Yahoo calls made.
   - A ticker Yahoo returns nothing for is counted `no_yahoo`, never dropped.
3. **Classes each ticker by a rule committed in its OWN commit BEFORE the first run.** That commit must hold the script with the
   rule and no output. The rule compares the store's `yahoo_finance` rows to Yahoo on the overlapping dates.
   - `as_traded`: within 0.5% of `Close` on at least 80% of days.
   - `dividend_adjusted`: `store / Adj Close` constant (dispersion within 0.5%) and `store / Close` drifting.
   - `indistinguishable`: `Close` and `Adj Close` equal over the window (no dividends).
   - `mixed`.
   - `no_yahoo`.
   - `other:<what>`.

   Where computable, print a per-ticker implied vintage: the latest dividend date whose effect the store's series already carries.
4. **Counts what rests on adjusted prices,** with denominators.
   - Store rows (`yahoo_finance` + `linear_interpolation`) of `dividend_adjusted` and `mixed` tickers.
   - In the served `account_day_value` (key from `lib/opal_naming.address("commonwealth", "cottonwood", "silver",
     "account_day_value", "date=2026-06-23", "part-00000.parquet")`), the account-days with at least one holding priced from such a
     ticker.
   - The accounts and months those touch.
5. **Names `bd_txn_price` provenance (row ADVI_COTBKF-D2-S48).** Print its 3 tickers, their dates, and which code writes that label.
   Use repo search for the literal `bd_txn_price` and print the file and line. Do NOT read any other firm's bucket to find out.

Write `price_basis_census.md` and a per-ticker CSV `price_basis_census.csv`. LAST line exactly:
`PRICE-BASIS tickers=<n> as_traded=<a> dividend_adjusted=<b> indistinguishable=<c> mixed=<d> no_yahoo=<e> other=<f> yahoo_calls=<k> adv_days_on_adjusted=<m>/<M>`

### ACCEPTANCE

<criterion id="CB33ag1-AC1" cell_refs="CB-ag-1"><invocation>python data/assets/scripts/silver/commonwealth_price_basis_census.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60</invocation><expect>PRICE-BASIS tickers=</expect></criterion>
`CB33ag1-AC1` -- every `yahoo_finance` ticker is classed, with denominators, and the served account-days on adjusted prices are
counted.

<criterion id="CB33ag1-AC2" cell_refs="CB-ag-1" judgment="true"/>
`CB33ag1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the rule commit precedes the output commit in git, and
each class follows from the printed comparison by that rule.

<expected_criteria>CB33ag1-AC1,CB33ag1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Yahoo cache and large output go under
  `.scratch/`, uncommitted.
- **Read-only.** No rule change and no S3 write. Read only the store, the served `account_day_value` key, and Yahoo. Never read
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`. No Bloomberg.
- **Yahoo pacing.** At most 50 tickers per call, at least 5 s between calls, one pass. If Yahoo rate-limits, stop the pass, class the
  unread tickers `no_yahoo` with reason `rate_limited`, and file a row. Do not retry in a tight loop.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W60-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_price_basis_census.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round33.md</decomp_doc> (round 33), cell `CB-ag-1`.
<owned_cells>CB-ag-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB33ag1-AC1, CB33ag1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60/ADVI_COTBKF.TO-CB-ag-1.price-basis-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB33ag1-AC1,CB33ag1-AC2` BEFORE the flip. Mechanical: CB33ag1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the PRICE-BASIS line; the class counts with denominators; the served account-days, accounts and months on adjusted
prices; `bd_txn_price` provenance; the Yahoo call count; commits (rule commit first).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-pass read-only census.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- rule in its own commit before the first run (CVO note on D2-S47); no_yahoo counted, never dropped; Yahoo paced and the call count printed; BLIND: a ticker whose store series mixes vintages (classed mixed, named).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 8 @bff4e48547 (msg 3060); rows D2-W59-S1, D2-S48.
